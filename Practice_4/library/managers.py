from django.db import models

class AuthorManager(models.Manager):
    def get_prolific_authors(self):
        return self.annotate(num_books=models.Count('book')).filter(num_books__gte=3)

    def get_authors_by_genre(self, genre_names):
        return self.filter(book__genre__name__in=genre_names).distinct()

class BookManager(models.Manager):
    def get_books_published_after_year(self, year):
        return self.filter(publication_date__gte=f"{year}-01-01")

    def get_by_author(self, author_name):
        return self.filter(author__name=author_name)