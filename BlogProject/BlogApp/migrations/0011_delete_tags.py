# Generated by Django 4.2.7 on 2023-12-29 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0010_alter_blog_desc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
