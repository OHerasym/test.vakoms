#from tastypie.resources import ModelResource
#from tastypie.constants import ALL
from .models import Blog

#class ArticleResource(ModelResource):
#	class Meta:
#		queryset = Blog.objects.all()
#		resource_name = 'article'
#		filtering = { "title" : ALL }