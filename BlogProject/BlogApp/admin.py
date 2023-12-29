from django.contrib import admin
from .models import Blog, Tags, MainPage

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active",)
    list_editable = ("is_active",)
    search_fields = ("title","desc")

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tags)
admin.site.register(MainPage)
