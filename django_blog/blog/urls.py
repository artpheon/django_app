from .views import Home, Article
from django.urls import path, include


urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view())
]
