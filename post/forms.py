from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):  

    class Meta:
        model = Blog
        fields = ('title', 'body', 'pub_date')

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('first_name', 'second_name', 'body')