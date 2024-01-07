from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from .models import Blog, MainPage, Tags
from .forms import BlogForm

# Create your views here.
def index(request):
    blogs = Blog.objects.filter(is_active=True).order_by("publish_datetime")
    tags = Tags.objects.all()
    main = MainPage.objects.all()

    paginator = Paginator(blogs, 10)
    page = 1
    page_obj = paginator.page(page)

    context = {
        "tags": tags,
        "page_obj": page_obj,
        "main": main
    }

    return render(request,"BlogApp/index.html",context)

def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request,"BlogApp/content.html",{
        "blog":blog
    })

def blogs_by_tags(request,slug):
    pass

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        blogs = Blog.objects.filter(is_active=True,title__contains=q).order_by("publish_datetime")
        tags = Tags.objects.all()
        main = MainPage.objects.all()

        paginator = Paginator(blogs, 10)
        page = 1
        page_obj = paginator.page(page)

        context = {
            "tags": tags,
            "page_obj": page_obj,
            "main": main
        }
    else:
        return redirect["index"]
    return render(request,"BlogApp/list.html",context)

def create_post(request):
    form = BlogForm()
    return render(request, "BlogApp/create-post.html",
                  {"form":form})