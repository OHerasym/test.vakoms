from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from post.models import Blog, Category, Comment
from django.contrib import messages
from django.template import RequestContext
#from haystack.query import SearchQuerySet
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.views import generic

from .forms import BlogForm, CommentForm
from . import models
from .models import Blog
from app1.models import UserProfile

import smtplib


def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'
    
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
        
    if 'lang' in request.session:
        session_language = request.session['lang']
        
    args = {}
    args.update(csrf(request))
    
    args['articles'] = Blog.objects.all()
    args['language'] = language 
    args['session_language'] = session_language 
    
    return render_to_response('articles.html', args) 


def article(request, article_id=1):   
    return render(request, 'article.html', 
                  {'article': Blog.objects.get(id=article_id) })


def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    
    return response


def create(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/invalid')

    if request.POST:
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save()
            title = request.POST.get('title', '')
            username = request.user.get_username()

            article = get_object_or_404(Blog, title=title)

            if article == None:
                raise "Article is None!!!!"

            article.owner = str(username)
            article.save()

            messages.add_message(request, messages.SUCCESS, "Your Post was added")
            
            return HttpResponseRedirect('/articles/all')
    else:
        form = BlogForm()
        
    args = {}
    args.update(csrf(request))
    args['form'] = form
    
    return render_to_response('create_article.html', args)

def add_comment(request, article_id):
    a = Blog.objects.get(id=article_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()
            
            sender = settings.EMAIL_HOST_USER
            receivers = [a.owner, settings.EMAIL_HOST_USER]
            email_subject = u'New comment in your post!'
            message = u"Hello, visit our Vakoms project again, you have a new comment from %s %s!" % (c.first_name, c.second_name)

            body = '\r\n'.join(['To: %s' % receivers, 
				'From: %s' % sender, 'Subject: %s' % email_subject, '\n %s' % message])

            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login('task.vakoms@gmail.com', 'vakoms2015')
            smtpObj.sendmail(sender, receivers, body)
            smtpObj.quit() 

            messages.success(request, "You Comment was added")
            
            return HttpResponseRedirect('/articles/get/%s' % article_id)
        
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    
    args['article'] = a
    args['form'] = f
    
    return render_to_response('add_comment.html', args)    

def delete_comment(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    
    article_id = c.article.id
    c.delete()
    
    messages.add_message(request, 
                         settings.DELETE_MESSAGE,
                         "Your comment was deleted")
    
    return HttpResponseRedirect("/articles/get/%s" % article_id)


def like_article(request, article_id):
    if article_id:
        a = Blog.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
        
    return HttpResponseRedirect('/articles/get/%s' % article_id)


def search_titles(request):
    #articles = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))            
    
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    if search_text == '':
        articles = None
    else:    
        articles = Blog.objects.filter(title__contains=search_text)

    return render_to_response('ajax_search.html', {'articles' : articles})
