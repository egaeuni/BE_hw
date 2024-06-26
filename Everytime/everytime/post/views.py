from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import listForm


def list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        post = Post.objects.filter(category=category).order_by('-created_at')[:4]

    else:
        category = None
        post = Post.objects.all().order_by('-created_at')[:4]

    form = listForm()

    return render(request, "post/list.html", {
        'post': post,
        'form': form,
        'categories': categories,
        'category': category,
    })

@login_required
def create(request,slug):
    category = get_object_or_404(Category,slug=slug)
    posts = Post.objects.filter(category=category).order_by('-id')[0:4]
    categories = Category.objects.all() 

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymity')  == 'on'
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        post=Post.objects.create(
            title = title,
            content = content,
            anonymity = anonymity,
            video = video,
            image = image,
        )
        post.category.add(category)
        post.save()
        
        return redirect('post:create', slug=slug)
    return render(request, 'post/create.html', {'posts':posts, 'slug':slug, 'categories':categories, 'category':category})

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
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        if video:
            post.video.delete()
            post.video = video
        if image:
            post.image.delete()
            post.image = image

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
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymity')  == 'on'

        Comment.objects.create(
            content = content,
            author = request.user,
            post = post,
            anonymity = anonymity,
        )
        return redirect('post:detail', post_id)
    return render(request, 'post/detail.html')

@login_required
def delete_comment(request, comment_id):
    comment= get_object_or_404(Comment, id = comment_id)
    post_id = comment.post.id
    comment.delete()
    return redirect('post:detail', post_id)


def add_like(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    post.like.add(request.user)
    return redirect('post:detail', post_id)

def remove_like(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    post.like.remove(request.user)
    return redirect('post:detail', post_id)

def add_scrap(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    post.scrap.add(request.user)
    return redirect('post:detail', post_id)

def remove_scrap(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    post.scrap.remove(request.user)
    return redirect('post:detail', post_id)

def myscrap(request):
    scraped_posts = Post.objects.filter(scrap=request.user).order_by('-id')
    return render(request, 'accounts/myscrap.html', {'posts': scraped_posts})