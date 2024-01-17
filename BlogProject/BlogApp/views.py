from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404, render, redirect
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
        return redirect("/")
    return render(request,"BlogApp/list.html",context)

def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = BlogForm()
    return render(request, "BlogApp/create-post.html",
                  {"form":form})

def update_post(request, slug):
    blog = Blog.objects.get(slug=slug)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        form.save()
        return redirect("/")
    else:
        form = BlogForm(instance=blog)

    return render(request, "BlogApp/update-post.html",
                  {"form":form})

def delete_post(request, slug):
    blog = Blog.objects.get(slug=slug)

    if request.method == "POST":
        blog.delete()
        return redirect("/")
    else:
        form = BlogForm(instance=blog)

    return render(request, "BlogApp/delete-post.html",
                  {"blog":blog})