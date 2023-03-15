from openpyxl import load_workbook
import aiohttp
import asyncio
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from pydantic import ValidationError
from .models import Article
from rest_framework import viewsets
from .schemas import ArticleSchema


async def get_brand_title(article):
    url_card = "https://basket-05.wb.ru/vol{}/part{}/{}/info/ru/card.json".format(article[:3], article[:5],
                                                                                  article)
    url_seller = "https://basket-05.wb.ru/vol{}/part{}/{}/info/sellers.json".format(article[:3],
                                                                                    article[:5], article)
    async with aiohttp.ClientSession() as session:
        async with session.get(url_seller) as resp:
            out = await resp.json()
            brand = out['trademark']
        async with session.get(url_card) as resp:
            out = await resp.json()
            title = out['imt_name']

    return brand, title


class ArticleViewSet(viewsets.ViewSet):
    serializer_class = ArticleSchema.drf_serializer

    def create(self, request, *args, **kwargs):
        if request.FILES:
            uploaded_file = request.FILES["file"]
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            path = fs.path(name)
            wb = load_workbook(path)
            article_set = []
            for cell in wb.active['A']:
                article = str(cell.value)
                brand, title = asyncio.run(get_brand_title(article))
                try:
                    article_schema = ArticleSchema(article=article, brand=brand, title=title)
                    ser = self.serializer_class(article_schema)
                    obj, created = Article.objects.get_or_create(**ser.data)
                    article_set.append(article_schema)
                except ValidationError as e:
                    print(e.json())
                    return Response(e.json())

            ser = self.serializer_class(article_set, many=True)
        else:
            article = request.data['article']
            brand, title = asyncio.run(get_brand_title(article))
            try:
                article_schema = ArticleSchema(article=article, brand=brand, title=title)
                ser = self.serializer_class(article_schema)
                obj, created = Article.objects.get_or_create(**ser.data)
            except ValidationError as e:
                print(e.json())
                return Response(e.json())

        return Response(ser.data)
