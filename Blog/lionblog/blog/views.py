from django.shortcuts import render
from .models import Post

# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render (request, "blog/index.html", {'posts': posts})