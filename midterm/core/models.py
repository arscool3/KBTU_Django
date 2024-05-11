from django.db import models
from django.contrib.auth.models import User
import uuid

class Gist(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=150, null=True, blank=True)
    Visible = models.BooleanField(default=False)
    IsForked = models.BooleanField(default=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

class Commit(models.Model):
    ID = models.AutoField(primary_key=True)
    Comment = models.CharField(max_length=250)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    GistID = models.ForeignKey('Gist', on_delete=models.CASCADE)

class File(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Code = models.TextField()
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    CommitID = models.ForeignKey('Commit', on_delete=models.CASCADE)