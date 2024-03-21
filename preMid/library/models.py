from django.db import models

# Create your models here.
class AbstractTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True

class Author(AbstractTimestampedModel):
    first_name = models.CharField(max_length=255)
    def __str__(self):
        return self.first_name
    class Meta(object):
        db_table = 'author_model'

class Genre(AbstractTimestampedModel):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta(object):
        db_table = 'genre_model'

class Book(AbstractTimestampedModel):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(to=Genre, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    year = models.IntegerField()
    class Meta(object):
        db_table = 'my_book'



class Client(AbstractTimestampedModel):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name
    class Meta(object):
        db_table = 'client'

class ClientQuerySet(models.QuerySet):
    def books_by_genre(self, genre):
        return self.filter(books__genre=genre).distinct()
    def active(self):
        return self.filter(books__isnull=False).distinct()

class BookQuerySet(models.QuerySet):
    def available_books(self):
        return self.filter(client=None)