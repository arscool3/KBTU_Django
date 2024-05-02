from django.db import models

# Create your models here.

class AuthorManager(models.Manager):
    def popular_authors(self):
        return self.filter(popularity__gt=100)
    def active_authors(self):
        return self.filter(is_active=True)


class BookManager(models.Manager):
    def best_sellers(self):
        return self.filter(sales__gt=1000)
    def fiction_books(self):
        return self.filter(genre='Fiction')

class Author(models.Model):
    name = models.CharField(max_length=100)
    popularity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    sales = models.IntegerField(default=0)

    objects = BookManager()

