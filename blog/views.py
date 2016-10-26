from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request):
    context = {
        "BlogPosts": BlogPost.objects.all()
    }
    return render(request, 'blog.html', context)

def post(request, slug):
    context = {
        "Post": BlogPost.objects.get(url_slug=slug)
    }
    return render(request, 'post.html', context)
