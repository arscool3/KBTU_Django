from django.db import models
# noinspection PyUnresolvedReferences
from django.contrib.auth.models import User
from api.models.book import Book

class Review(models.Model) :
    def __str__(self):
        return f'{self.id}'
    review = models.TextField()
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)