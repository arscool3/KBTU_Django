# myapp/models.py

from django.db import models

class AuthorManager(models.Manager):
    def authors_with_books(self):
        return self.all()

class PublisherManager(models.Manager):
    def get_publishers_with_magazines(self):
        return self.all()

class Author(models.Model):
    name = models.CharField(max_length=100)
    objects = AuthorManager()

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    objects = PublisherManager()
