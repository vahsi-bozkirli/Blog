from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    context = {
        "blogs":Blog.objects.all()
    }
    return render(request,"BlogApp/index.html",context)

def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request,"BlogApp/content.html",{
        "blog":blog
    })