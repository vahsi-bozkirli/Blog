from django.db import models
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    slug = models.SlugField(null=True,unique=True,db_index=True)
    title = models.CharField(max_length=250)
    desc = models.TextField()
    start_datetime = models.DateTimeField()
    publish_datetime = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tags(models.Model):
    tag = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.tag}"


