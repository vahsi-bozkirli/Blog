from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("content/<str:id>", views.blog, name="content")
]