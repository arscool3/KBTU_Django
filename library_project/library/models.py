from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class BorrowerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional profile fields if needed

    def __str__(self):
        return self.user.username

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.OneToOneField(BorrowerProfile, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.book} - {self.borrower}"
# Create your models here.
