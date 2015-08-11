from django.contrib import admin

from post.models import Blog, Category, Comment
from django_markdown.admin import MarkdownModelAdmin

class BlogAdmin(MarkdownModelAdmin):
	list_display = ("title", "pub_date", "owner")
	#exlude = ['posted']
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title', )}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment)

