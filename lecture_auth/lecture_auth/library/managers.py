from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


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
