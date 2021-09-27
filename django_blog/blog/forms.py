from django.db.models import fields
from django.forms import ModelForm
from .models import ArticleModel

class ArticleForm(ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'category', 'author', 'content']
        