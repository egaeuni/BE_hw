from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.db.models import Q

# Create your views here.
def list(requset):
    posts = Post.objects.all().order_by('-created_at')
    return render(requset, 'posts/list.html', {'posts': posts})

def result(request):
    search_keyword = request.GET.get('data')
    search_list = Post.objects.filter( Q(title__contains = search_keyword)| Q(content__contains = search_keyword)).order_by('created_at')
    return render(request, 'posts/result.html', {'result': search_list, 'data': search_keyword})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title = title,
            content = content,

        )
        return redirect('list')
    return render(request, 'posts/create.html')

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    post.views += 1
    post.save()
    return render(request, 'posts/detail.html', {'post' : post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('detail', id)
    return render(request, 'posts/update.html', {'post' : post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('list')