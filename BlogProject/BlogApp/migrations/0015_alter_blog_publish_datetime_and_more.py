# Generated by Django 5.0.1 on 2024-01-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0014_remove_blog_tags_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='start_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
