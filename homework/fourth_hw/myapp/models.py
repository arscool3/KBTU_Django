from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Genre(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

