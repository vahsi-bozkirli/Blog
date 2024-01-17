from django.contrib import admin
from .models import Blog, MainPage, Tags

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","Tags_List",)
    list_editable = ("is_active",)
    search_fields = ("title","desc")

    def Tags_List(self,obj):
        html = ""
        for tag in obj.tags.all():
            html += tag.tag + " "
        return html

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("tag",)

admin.site.register(MainPage)
