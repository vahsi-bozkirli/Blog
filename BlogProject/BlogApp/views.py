from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    context = {
        "blogs":Blog.objects.all()
    }
    return render(request,"BlogApp/frames/_blogs.html",context)

def blog(request, id):
    blog = Blog.objects.get(id=str(id))
    return render(request,"BlogApp/content.html",{
        "blog":blog
    })