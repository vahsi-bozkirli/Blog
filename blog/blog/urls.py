"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp import views as blgv
from account import views as accv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blgv.index, name="index"),
    path('content/<slug:slug>', blgv.blog, name="content"),
    path('create-post', blgv.create_post, name="create_post"),
    path("delete-post/<slug:slug>", blgv.delete_post, name="delete_post"),
    path("update-post/<slug:slug>", blgv.update_post, name="update_post"),
    path('login', accv.user_login, name="user_login"),
    path('register', accv.user_register, name="user_register"),
    path('logout', accv.user_logout, name="user_logout"),
    # path("change-pswd",views.change_password, name="change_pswd")
]
