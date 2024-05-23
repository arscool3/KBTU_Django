from django.db import models
from .managers import UserManager, TaskManager

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    def __str__(self):
        return self.username

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = TaskManager()

    def __str__(self):
        return self.title
