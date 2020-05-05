from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'ded/index.html')

def projects(request):
    return render(request, 'ded/projects.html')

def lessons(request):
    return render(request, 'ded/lessons.html')

def about_us(request):
    return render(request, 'ded/about.html')


def news(request):
    posts = Post.objects.all()
    return render(request, 'ded/posts.html', context={'posts': posts})
