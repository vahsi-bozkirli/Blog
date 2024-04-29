from typing import Any
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget = widgets.TextInput()
        self.fields["password"].widget = widgets.PasswordInput()

    def confirm_login_allowed(self, user: AbstractBaseUser) -> None:
        if user.username.startswith("s"):
            return forms.ValidationError("bu kullanici adi ile giriş yapamazsiniz.")
        
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = widgets.PasswordInput()

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if User.objects.filter(username = username).exists():
            self.add_error("username","bu username daha önce kullanilmiş")
        return username
