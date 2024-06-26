from django.db import models
from user.models import *
import os
from uuid import uuid4
from django.utils import timezone

# Create your models here.
def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50, unique= 50, blank=True, null=True)

    def __str__(self):
        return f'[{self.name}]'

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    anonymity = models.BooleanField(default=True) 
    category = models.ManyToManyField(to=Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(to=User, through="Like", related_name="liked_posts")
    scrap = models.ManyToManyField(to=User, through="Scrap", related_name="scraped_posts")
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_posts", null=True, blank=True)
    image = models.ImageField(upload_to=upload_filepath, blank=True, null=True)
    video = models.FileField(upload_to=upload_filepath, blank = True, null=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")
    anonymity = models.BooleanField(default=True)
    

class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_likes")

class Scrap(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_scraps")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_scraps")

    def __str__(self):
        return f'[{self.id}] {self.title}'
    

class PostCategory(models.Model):
    category = models.ForeignKey(to = Category, on_delete=models.PROTECT, related_name="categories_postcategory")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="posts_postcategory")