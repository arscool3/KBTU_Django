from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    year = models.DateField()

    def __str__(self):
        return self.name

class Book2(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    year = models.DateField()

    def __str__(self):
        return self.author