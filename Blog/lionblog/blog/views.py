from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('-id')

    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        category = get_object_or_404(Category, id = category_id)
        posts = category.posts.all().order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
    return render (request, "blog/list.html", {'posts': posts, 'categories': categories})

@login_required
def create(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids]

        post = Post.objects.create(
            title = title,
            content = content,
            author = request.user,
        )

        for category in category_list:
            post.category.add(category)

        return redirect('blog:list')
    return render(request, 'blog/create.html', {'categories': categories})

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'blog/detail.html', {'post': post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('blog:detail', id)
    return render(request, 'blog/update.html', {'post': post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('blog:list')

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    if request.method == "POST":
        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            post = post,              #comment의 post 필드에 get_dbject_or_404로 가져온 post 객체를 넣어 관계 설정
        )
        return redirect('blog:detail', id = post_id)

@login_required
def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.add(request.user)
    return redirect('blog:detail', post_id)

@login_required
def remove_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.like.remove(request.user)
    return redirect('blog:detail', post_id)

def mylike(request):
    liked_posts = Post.objects.filter(like=request.user).order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts': liked_posts})
