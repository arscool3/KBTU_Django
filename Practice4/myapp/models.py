from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishedDate = models.DateField()


class Reader(models.Model):
    name = models.CharField(max_length=100)


class ReadingList(models.Model):
    title = models.CharField(max_length=100)
    reader = models.OneToOneField(Reader, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
