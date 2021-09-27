from django.test import TestCase
from blog.models import ArticleModel
from datetime import datetime
from django.utils import timezone

# Create your tests here.

class ArticleTest(TestCase):
    def test_article_creation_success(self):
        ArticleModel.objects.create(
            title='test title',
            category='test category',
            author='test author',
            content='test content',
            created_at=datetime.now(tz=timezone.utc))
        test_article = ArticleModel.objects.get(title='test title')
        self.assertEqual(test_article.category, 'test category')
    
class BlogPagesTest(TestCase):
    def test_blog_page(self):
        res = self.client.get('/blog/')
        self.assertEqual(res.content, b'Welcome to my Blog!')