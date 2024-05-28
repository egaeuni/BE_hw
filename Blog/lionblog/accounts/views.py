from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form':form})
    
    form = SignUpForm(request.POST)
    if form.is_valid():                    #is_valid() = django Form이 제공하는 유효성 검증용 함수
        user = form.save()
        return redirect('accounts:login')
    else:
        return render(request, 'accounts/signup.html', {'form':form})
    
def login_view(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'form': AuthenticationForm})
    
    form = AuthenticationForm(request, data= request.POST)
    if form.is_valid():
        login(request, form.user_cache)                   #form 변수에 저장된 유저 정보로 로그인 시킨 뒤, 사용자를 메인페이지로 이동시킴
        return redirect('blog:list')
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('blog:list')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def myblog(request):
    posts = request.user.posts.all().order_by('-id')  #'-id': 역순으로 정렬
    return render(request, 'accounts/myblog.html', {'posts': posts})

def user_info(request):
    return render(request, 'accounts/user_info.html')