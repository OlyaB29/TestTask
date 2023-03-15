from django.db import models


class Article(models.Model):
    article = models.IntegerField('Артикул', unique=True)
    brand = models.CharField('Название бренда', max_length=500)
    title = models.CharField('Название товара', max_length=500)

    def __str__(self):
        return f'{self.article}: {self.title}'
