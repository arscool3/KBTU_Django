from django.db import models

class CustomAuthorManager(models.Manager):
    def get_authors_with_more_than_one_book(self):
        return self.filter(book__count__gt=1).distinct()

    def get_authors_ordered_by_book_count(self):
        return self.annotate(num_books=models.Count('book')).order_by('-num_books')

class CustomBookManager(models.Manager):
    def get_books_by_genre(self, genre_name):
        return self.filter(genre__name=genre_name)

    def get_books_by_publisher(self, publisher_name):
        return self.filter(publisher__name=publisher_name)
