from django.db import models
from django.db.models import Count

class AuthorManager(models.Manager):
    def authors_with_more_than_one_book(self):
        return self.annotate(num_books=Count('book')).filter(num_books__gt=1)
    
class BookManager(models.Manager):
    def books_published_after_year(self, year):
        return self.filter(publication_date__gt=year)

class PublisherManager(models.Manager):
    def publishers_in_location(self, location):
        return self.filter(location=location)
    
class MagazineManager(models.Manager):
    def magazines_published_by_publisher(self, publisher):
        return self.filter(publisher=publisher)

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    objects = AuthorManager()
    class Meta:
        app_label = 'myapp'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    objects = BookManager()
    class Meta:
        app_label = 'myapp'

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    objects = PublisherManager()
    class Meta:
        app_label = 'myapp'

class Magazine(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=50)
    objects = MagazineManager()
    class Meta:
        app_label = 'myapp'


