from django.db import models

from library.managers import *
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Base(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Genre(Base):
    name = models.CharField(max_length=100)


class Author(Base):
    biography = models.TextField(blank=True)
    objects = AuthorManager.from_queryset(AuthorQuerySet)()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    objects = BookManager.from_queryset(BookQuerySet)()

    def __str__(self):
        return self.title


class Borrower(Base):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    books_borrowed = models.ManyToManyField(Book, blank=True)

    objects = BorrowerManager.from_queryset(BorrowerQuerySet)()