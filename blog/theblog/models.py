from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100, default='Title')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    category = models.CharField(max_length=100, default='uncategorized')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' by ' + self.author.username

    def get_absolute_url(self):
        return reverse('post', args=(str(self.id)) )