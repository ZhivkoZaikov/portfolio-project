from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/index.html', {"blogs": blogs})

def detail(request, slug):
    blogs = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/detail.html', {'blogs':blogs})
