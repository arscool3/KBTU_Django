# Generated by Django 4.2.11 on 2024-05-10 08:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_content_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
