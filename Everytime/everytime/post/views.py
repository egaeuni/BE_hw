from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import listForm


def list(request):
    posts = Post.objects.all().order_by('-id')
    form = listForm()
    return render (request, "post/list.html", {'posts': posts, 'form':form})

@login_required
def create(request):
    categories = Category.objects.all() 

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymity')  == 'on'

        categories_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in categories_ids]

        post = Post.objects.create(
            title = title,
            content = content,
            anonymity = anonymity,
            author = request.user,
        )

        for category in category_list:
            post.category.add(category)

        return redirect('post:list')
    return render(request, 'post/create.html', {'categories': categories})

@login_required
def detail(request,id):
    post = get_object_or_404(Post, id =id)
    return render(request, 'post/detail.html', {'post':post})

@login_required
def update(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post:detail', id)
    return render(request, 'post/update.html', {'post': post})

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:list')

@login_required
def create_comment(request, post_id):
    post=get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymity') == 'on'

        comment = Comment.objects.create(
            content = content,
            author = request.user,
            post = post,
            anonymity = anonymity,
        )
        return redirect('post:detail', post_id)
    return render(request, 'post/detail.html', {'comment':comment})

@login_required
def delete_comment(request, post_id):
    comment= get_object_or_404(Comment, id = post_id)
    comment.delete()
    return redirect('post:detail', post_id)


def add_like(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    post.like.add(request.user)
    return redirect('post:detail', post_id)


def add_scrap(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    post.scrap.add(request.user)
    return redirect('post:detail', post_id)


def myscrap(request):
    scraped_posts=Post.objects.filter(scrap=request.user).order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts':scraped_posts})