from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages

from account.forms import LoginUserForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Giriş yapildi")
                return redirect("index")
            else:
                messages.add_message(request, messages.INFO, "Kullanici zaten kayitli")
                return render(request,"account/login.html",{"form":form})
        else:
            messages.add_message(request, messages.INFO, "Hatali giriş yaptiniz")
            return render(request,"account/login.html",{"form":form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form":form})

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Kayit yapildi")
            return redirect("index")
        else:
            messages.add_message(request, messages.INFO, "Kayit yapilamadi")
            return render(request, "account/register.html", {"form":form})
    else: 
        form = UserCreationForm() 
        return render(request, 'account/register.html', {"form":form})

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Çikiş yapildi")
    return redirect("index")