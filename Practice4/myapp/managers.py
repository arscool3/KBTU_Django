from django.db import models


class AuthorManager(models.Manager):
    def get_authors_with_books_count(self):
        return self.annotate(books_count=models.Count('book'))

    def get_authors_with_most_books(self, limit=5):
        return self.get_authors_with_books_count().order_by('-books_count')[:limit]


class BookManager(models.Manager):
    def get_books_by_author(self, author_id):
        return self.filter(author_id=author_id)

    def get_books_published_after_year(self, year):
        return self.filter(publishedDate__year__gt=year)
