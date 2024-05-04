from django.db import models

# Create your models here.
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(TimeStampedModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title

class Review(TimeStampedModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.book.title}"


class BookQuerySet(models.QuerySet):
    def published_after_year(self, year):
        return self.filter(published_year__gte=year)
    
    def created_at_november(self,month):
        return self.filter(published_month__gte=month)

class ReviewQuerySet(models.QuerySet):
    def with_high_rating(self):
        return self.filter(rating__gte=4)

    def with_low_rating(self):
        return self.filter(rating__gte=1)

class BookManager(models.Manager):

    def get_queryset(self):
        return BookQuerySet(self.model)

class ReviewManager(models.Manager):

    def get_queryset(self):
        return ReviewQuerySet(self.model)


