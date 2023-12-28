from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    start_datetime = models.DateTimeField(auto_now_add=True)
    publish_datetime = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)


