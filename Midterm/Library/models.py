from django.db import models
from django.utils import timezone

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




class PublishingOffice(models.Model):
    name = models.CharField(max_length=255, default="Publishing Office sample")
    email = models.EmailField(default='default@example.com')
    address = models.CharField(max_length=255, default='default@example.com')

    def _str__(self):
        return f"{self.name} - {self.address}"

    class Meta(object):
        db_table = 'publishing_office'

class BookQuerySet(models.QuerySet):
    def available_books(self):
        return self.filter(available=True)
    def books_by_genre(self, genre__id):
        return self.filter(genre__id=genre__id)

class Book(AbstractTimestampedModel):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    publishing_office = models.ForeignKey('PublishingOffice', on_delete=models.CASCADE, default="AlmatyKitap")
    year = models.IntegerField()
    available = models.BooleanField(default=True)  # Add the available field
    objects = BookQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'my_book'

class ClientQuerySet(models.QuerySet):
    def books_by_genre(self, genre):
        return self.filter(books__genre=genre).distinct()
    def active(self):
        return self.filter(books__isnull=False).distinct()
class Client(AbstractTimestampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(default='default@example.com')
    password = models.CharField(max_length=255, default='arslanchik')
    objects = ClientQuerySet.as_manager()

    def __str__(self):
        return self.name
    class Meta(object):
        db_table = 'client'

class LoanQuerySet(models.QuerySet):
    def available_loans(self):
        return self.filter(client=None)

class LoanManager(models.Manager):
    def get_queryset(self):
        return LoanQuerySet(self.model, using=self._db).select_related('book', 'client')

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)
    objects = LoanManager()

    def __str__(self):
        return f"{self.book} - {self.loan_date}"
    class Meta(object):
        db_table = 'loan'






