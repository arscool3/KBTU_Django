# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change this to avoid clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Change this to avoid clash
        blank=True
    )

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Link(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='links', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='links')
    created_by = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)

class Click(models.Model):
    link = models.ForeignKey(Link, related_name='clicks', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class LinkUsage(models.Model):
    link = models.ForeignKey(Link, related_name='usage', on_delete=models.CASCADE)
    clicks = models.PositiveIntegerField(default=0)
