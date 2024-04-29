from django.shortcuts import render, redirect

from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
    blogs = Blog.objects.filter(is_active=True).order_by("date")

    context = {
        "blogs": blogs
    }

    return render(request, "blogapp/index.html", context)

def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blogapp/content.html", {
        "blog":blog
    })

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = BlogForm()
    return render(request, "blogapp/create-post.html",
                  {"form":form})

@login_required()
def delete_post(request, slug):
    blog = Blog.objects.get(slug=slug)

    if request.method == "POST":
        blog.delete()
        return redirect("/")
    else:
        form = BlogForm(instance=blog)

    return render(request, "blogapp/delete-post.html",
                  {"blog":blog})

@login_required()
def update_post(request, slug):
    blog = Blog.objects.get(slug=slug)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        form.save()
        return redirect("/")
    else:
        form = BlogForm(instance=blog)

    return render(request, "blogapp/update-post.html",
                  {"form":form})
