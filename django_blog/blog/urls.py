from .views import Blog, Article, ArticleDetailed
from django.urls import path, include


urlpatterns = [
    path('', Blog.as_view()),
    path('articles', Article.as_view()),
    path('articles/<int:id>', ArticleDetailed.as_view())
]
