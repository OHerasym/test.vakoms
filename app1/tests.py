from django.test import TestCase

from post.models import Blog
from django.utils import timezone
from time import time 
from django.core.urlresolvers import reverse

class BlogTest(TestCase):

	def create_article(self, title="test article", body="Blah Blah Blah"):
		return Blog.objects.create(title=title, body=body, pub_date=timezone.now(), likes=0)

	def test_articles_list_view(self):
		a = self.create_article()
		url = reverse('post.views.articles')
		resp = self.client.get(url)
        
		self.assertEqual(resp.status_code, 200)
		self.assertIn((a.title).encode('utf-8'), resp.content)


	def test_article_detail_view(self):
		a = self.create_article()
		url = reverse('post.views.article', args=[a.id])
		resp = self.client.get(url)
        
		self.assertEqual(reverse('post.views.article', args=[a.id]), 
                         a.get_absolute_url())
		self.assertEqual(resp.status_code, 200)
		self.assertIn(a.title, resp.content) 