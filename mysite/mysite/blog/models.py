from django.db import models
from django.contrib import admin
import datetime 

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('timestamp',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("Author")

class Author(models.Model):
    name = models.CharField(max_length=100)

admin.site.register(BlogPost, BlogPostAdmin)
