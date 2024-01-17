from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("content/<slug:slug>", views.blog, name="content"),
    path("search", views.search, name="search"),
    path("create-post", views.create_post, name="create_post"),
    path("update-post/<slug:slug>", views.update_post, name="update_post"),
    path("delete-post/<slug:slug>", views.delete_post, name="delete_post")
]