from django.db import models

# Create your models here.

class Post(models.Model):
    username = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username + self.time_update