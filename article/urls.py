from django.urls import path
from article import views

urlpatterns = [
    path('read/', views.ArticleView.as_view(), name="article_view"),
    path('create/', views.ArticleView.as_view(), name="article_create_view"),
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name="article_detail_view"),
    path('<int:article_id>/update/', views.ArticleDetailView.as_view(), name="article_update_view"),
    path('<int:article_id>/delete/', views.ArticleDetailView.as_view(), name="article_delete_view"),
    path('<int:article_id>/comment/', views.CommentView.as_view(), name="article_comment_view"),
]
