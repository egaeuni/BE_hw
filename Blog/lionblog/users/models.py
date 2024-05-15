from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)  #unique = True로 사용자끼리 이메일, 닉네임 중복 방지
    nickname = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.username}'