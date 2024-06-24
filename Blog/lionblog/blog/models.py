from django.db import models
from users.models import User
import os
from uuid import uuid4
from django.utils import timezone

# Create your models here.

def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")  #현재 시간을 가져와서 연도, 월을 문자열로 변환한다.
    file_basename = os.path.basename(filename)    #파일의 기본 이름만 사용한다(파일 이름에서 경로제외)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'  
#str(uui4()):  UUID는 중복가능성이 낮은 고유한 식별자이다. UUID를 파일 이름에 추가하여  파일 이름이 중복되지 않도록 한다.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    #to: User 모델을 부모로 지정하겠다 / CASCADE: 연관된 User가 삭제되면 해당 Post 필드도 같이 삭제 / related_name: 역참조는 posts로 하겠다.
    category = models.ManyToManyField(to=Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(to=User, through="Like", related_name="liked_posts")
    image = models.ImageField(upload_to=upload_filepath, blank= True)
    video = models.FileField(upload_to=upload_filepath, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f'[{self.id}] {self.content}'
    

class PostCategory(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name="categories_postcategory")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="posts_postcategory")

class Like(models. Model):
    post = models.ForeignKey(to = Post, on_delete=models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_likes")