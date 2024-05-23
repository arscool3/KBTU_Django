from django.db import models
from django.db.models import QuerySet
from django.utils import timezone


class BookQuerySet(QuerySet):
    def available_books(self):
        return self.filter(borrower=None)

    def overdue_books(self):
        # Assuming you add a 'due_date' field to the Book model or a related Borrowing model:
        return self.filter(due_date__lt=timezone.now())


class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    def available_books(self):
        return self.get_queryset().published_authors()

    def overdue_books(self):
        return self.get_queryset().authors_by_genre()


class BorrowerQuerySet(QuerySet):
    def active_borrowers(self):
        return self.filter(books_borrowed__isnull=False).distinct()

    def borrowers_by_genre(self, genre_name):
        return self.filter(books_borrowed__genre__name=genre_name).distinct()


class BorrowerManager(models.Manager):
    def get_queryset(self):
        return BorrowerQuerySet(self.model, using=self._db)

    def active_borrowers(self):
        return self.get_queryset().published_authors()

    def borrowers_by_genre(self):
        return self.get_queryset().authors_by_genre()


class AuthorQuerySet(QuerySet):
    def published_authors(self):
        return self.filter(book__isnull=False).distinct()

    def authors_by_genre(self, genre_name):
        return self.filter(book__genre__name=genre_name).distinct()


class AuthorManager(models.Manager):
    def get_queryset(self):
        return AuthorQuerySet(self.model, using=self._db)

    def published_authors(self):
        return self.get_queryset().published_authors()

    def authors_by_genre(self):
        return self.get_queryset().authors_by_genre()
