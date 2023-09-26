from django.urls import path
from article import views

urlpatterns = [
    path('read/', views.ArticleView.as_view(), name="article_view"),
    path('create/', views.ArticleView.as_view(), name="article_create_view"),
]
