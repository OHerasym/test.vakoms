from django.db import models
from django.db.models import permalink

import sys
sys.setrecursionlimit(1000)


class Blog(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)
	approved = models.BooleanField(default=False)
	owner = models.CharField(max_length=200)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/articles/get/%i/" % self.id 

	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Enteries"
		ordering = ["-pub_date"]


class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __str__(self):
		return '%s' % self.title


class Comment(models.Model):
	first_name = models.CharField(max_length=200)
	second_name = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	article = models.ForeignKey(Blog)