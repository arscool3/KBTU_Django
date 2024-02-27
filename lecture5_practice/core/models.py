from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BookPublisher(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} - {self.publisher.name}"

class AuthorManager(models.Manager):
    def get_authors_with_email(self):
        return self.exclude(email='')

    def get_authors_with_books(self):
        return self.filter(book__isnull=False).distinct()

class PublisherManager(models.Manager):
    def get_publishers_in_country(self, country_name):
        return self.filter(country=country_name)

    def get_publishers_with_books(self):
        return self.filter(bookpublisher__isnull=False).distinct()
