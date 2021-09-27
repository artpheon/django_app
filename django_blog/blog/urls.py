from .views import Home, Article, ArticleDetailed
from django.urls import path, include


urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view()),
    path('articles/<int:id>', ArticleDetailed.as_view())
]
