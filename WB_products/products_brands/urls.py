from django.urls import path, include
from . import api
from rest_framework import routers


app_name = 'products_brands'

router = routers.DefaultRouter()
router.register('articles', api.ArticleViewSet, 'articles')

urlpatterns = [
    path('', include(router.urls)),
    # path('articles/<str:article_id>/', views.get_article),
    # path('articles/', views.get_all_articles),
]
