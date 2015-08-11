"""exuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin



admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'exuser.views.home'),
    url(r'^home/$', 'exuser.views.home'),

    url(r'^markdown/$', include('django_markdown.urls')),
    #url(r'^homes/$', include('post.urls')),
    #url(r'^articles/', include(post.urls)),

    url(r'^articles/get/(?P<article_id>\d+)/$', 'post.views.article'),
    url(r'^articles/language/(?P<language>[a-z\-]+)/$', 'post.views.language'),
    url(r'^articles/create/$', 'post.views.create'),
    url(r'^articles/like/(?P<article_id>\d+)/$', 'post.views.like_article'),
    url(r'^articles/add_comment/(?P<article_id>\d+)/$', 'post.views.add_comment'),
    url(r'^articles/delete_comment/(?P<comment_id>\d+)/$', 'post.views.delete_comment'),
    url(r'^articles/search/$', 'post.views.search_titles'),
    #url(r'^articles/api/', include(article_resource.urls)),

    url(r'^articles/all/$', 'post.views.articles'),

    url(r'^send/$', 'exuser.views.send'),

    url(r'^accounts/login/$', 'exuser.views.login'),
    url(r'^accounts/auth/$', 'exuser.views.auth_view'),
    url(r'^accounts/logout/$', 'exuser.views.logout'),
    url(r'^accounts/loggedin/$', 'exuser.views.loggedin'),
    url(r'^accounts/invalid/$', 'exuser.views.invalid_login'),
    url(r'^accounts/register/$', 'exuser.views.register_user'),
    url(r'^accounts/register_success/$', 'exuser.views.register_success'),
    #url(r'^register_success/', ('yourappname.views.register_success')),
    url(r'^accounts/confirm/(?P<activation_key>\w+)/', ('exuser.views.register_confirm')),

    url(r'^post/$', 'post.views.index'),
    url(
    r'^blog/view/(?P<slug>[^\.]+).html', 
    'post.views.view_post', 
    name='view_blog_post'),
    url(
    r'^blog/category/(?P<slug>[^\.]+).html', 
    'post.views.view_category', 
    name='view_blog_category'),

]
