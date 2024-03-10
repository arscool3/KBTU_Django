from django.db import models
from accounts.models import Account

class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name


class Paper(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    authors = models.ManyToManyField(Account, related_name='papers')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True , related_name = 'papers')
    category = models.ForeignKey(Category, related_name = 'papers', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
