from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles', views.articles, name='articles'),
    path('articlesByName/<str:articleName>', views.articlesByName, name="articlesByName"),
    path('testPost', views.testPost, name="testPost")
]