from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review of {self.book.title} by {self.user.username}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# class Genre(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Publisher(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
#     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
#
#
# class Review(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField(null=True)
#     rating = models.IntegerField(null=True)
