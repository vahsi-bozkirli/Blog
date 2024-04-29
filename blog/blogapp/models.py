from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    slug = models.SlugField(null=False,unique=True,db_index=True,editable=False)
    title = models.CharField(max_length=120, null=False)
    desc = RichTextField(null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    is_active = models.BooleanField(default=False)
    user = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
