from django.db import models
# noinspection PyUnresolvedReferences
from api.models.book import Book

class Rating(models.Model) :
    def __str__(self):
        return f'{self.count}'
    count = models.IntegerField(default=0)  # count of voted users
    sum = models.IntegerField(default=0)  # sum of given ratings
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=255,default=0)