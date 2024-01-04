from django.core.paginator import Paginator

from django.shortcuts import render
from .models import Blog, MainPage, Tags

# Create your views here.
def index(request):
    blogs = Blog.objects.filter(is_active=True).order_by("publish_datetime")
    tags = Tags.objects.all()
    main = MainPage.objects.all()

    paginator = Paginator(blogs, 1)
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