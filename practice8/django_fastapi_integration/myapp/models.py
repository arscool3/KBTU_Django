from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
