from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "blog/blog.html", {})


def blog_view(request, *args, **kwargs):
    blogs= Blog.objects.all()
    
    context= {'blogs': blogs}
    return render(request, 'blog/blog.html', context)
    
