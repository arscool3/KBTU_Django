from django.db import models
from django.contrib.auth.models import User

# QuerySets

class BookQuerySet(models.QuerySet):
    def published_after(self, year):
        return self.filter(publish_date__year__gt=year)

class AuthorQuerySet(models.QuerySet):
    def name_starts_with(self, letter):
        return self.filter(name__startswith=letter)

class PublisherQuerySet(models.QuerySet):
    def located_in(self, location):
        return self.filter(location__icontains=location)

class IllustratorQuerySet(models.QuerySet):
    def bio_contains(self, keyword):
        return self.filter(bio__icontains=keyword)

# Managers

class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    def published_after(self, year):
        return self.get_queryset().published_after(year)

class AuthorManager(models.Manager):
    def get_queryset(self):
        return AuthorQuerySet(self.model, using=self._db)

    def name_starts_with(self, letter):
        return self.get_queryset().name_starts_with(letter)

class PublisherManager(models.Manager):
    def get_queryset(self):
        return PublisherQuerySet(self.model, using=self._db)

    def located_in(self, location):
        return self.get_queryset().located_in(location)

class IllustratorManager(models.Manager):
    def get_queryset(self):
        return IllustratorQuerySet(self.model, using=self._db)

    def bio_contains(self, keyword):
        return self.get_queryset().bio_contains(keyword)

# Models


class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()

    objects = AuthorManager()  

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Illustrator(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    objects = IllustratorManager()  

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    objects = PublisherManager()  

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    summary = models.TextField()
    genre = models.CharField(max_length=100)
    publish_date = models.DateField()

    genres = models.ManyToManyField(Genre, related_name='books')
    illustrators = models.ManyToManyField(Illustrator, related_name='books', blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books', null=True, blank=True)

    objects = BookManager()  

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f"{self.user}'s review of {self.book}"
