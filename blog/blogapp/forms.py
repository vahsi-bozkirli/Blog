from django import forms
from django.forms import widgets
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        labels = {
            "title":"Title"
        },
        widgets = {
            "title": widgets.TextInput(attrs={"class":"class_1"}),
            "date": widgets.TextInput(attrs={'type': 'datetime-local'})
        },
        error_messages = {
            "title": {
                "required":"required field",
                "max_length":"max 120 character"
            }
        }
