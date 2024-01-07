from django import forms

class BlogForm(forms.Form):
    title = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)
    start_datetime = forms.DateTimeField()
    publish_datetime = forms.DateTimeField()
    is_active = forms.BooleanField()
