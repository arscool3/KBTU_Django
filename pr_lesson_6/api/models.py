from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)


class Author(Person):
    pass


class CustomUser(Person):
    objects = None


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    user = models.ManyToManyField(CustomUser, related_name='books')
