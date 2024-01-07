from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class MainPage(models.Model):
    image = models.ImageField(upload_to="on_main")

class Tags(models.Model):
    slug = models.SlugField(null=False,unique=True,db_index=True,editable=False)
    tag = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.tag}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.tag)
        super().save(*args, **kwargs)    


class Blog(models.Model):
    slug = models.SlugField(null=False,unique=True,db_index=True,editable=False)
    title = models.CharField(max_length=150, null=False)
    desc = RichTextField(null=False)
    start_datetime = models.DateTimeField(null=False)
    publish_datetime = models.DateTimeField(null=False)
    is_active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


