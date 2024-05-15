from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm    #UserCreationForm = Django에서 제공받는 기본 유저 생성폼

class SignUpForm(UserCreationForm):

    class Meta():
        model = get_user_model()   #회원가입에 사용할 모델 = settings.py에 정의한 users 앱의 user 모델을 가져옴
        fields = ['username', 'email', 'nickname']