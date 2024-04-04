from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.
def list(requset):
    posts = Post.objects.all().order_by('-created_at')
    return render(requset, 'posts/list.html', {'posts': posts})

def search(request):
    search_keyword = request.GET.get('data')
    if search_keyword:
        search_list = Post.objects.filter( Q(title__contains = search_keyword)| Q(content__contains = search_keyword)).order_by('created_at')
    else:
        search_list = Post.objects.all()
    return render(request, 'posts/search.html', {'result': search_list})
