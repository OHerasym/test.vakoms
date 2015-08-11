from django.conf.urls import patterns, url, include
from . import views
#from post.api import ArticleResource

urlpatterns = patterns(
		#url(r'^$', views.BlogIndex.as_view(), name = "index"),
		url(r'^all/$', 'post.views.articles'),
		#url(r'^get/(?P<article_id>\d)/$', 'post.views.article'),
		#url(r'^language/(?P<language>[a-z\-])/$', 'post.views.language'),
		#url(r'^create/$', 'post.views.create'),
		#url(r'^like/(?P<article_id>\d)/$', 'post.views.like_article'),
		#url(r'^add_comment/(?P<article_id>\d)/$', 'post.views.add_comment'),
		#url(r'^delete_comment/(?P<comment_id>\d)/$', 'post.views.delete_comment'),
		#url(r'^search/$', 'post.views.search_titles'),
		#url(r'^api/', include(article_resource.urls)),
	)