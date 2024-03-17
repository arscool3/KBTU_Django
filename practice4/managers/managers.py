from django.db import models

class AuthorManager(models.Manager):
    def get_prolific_authors(self):
        return self.annotate(num_books=models.Count('book')).filter(num_books__gte=3)

    def get_authors_with_most_recent_book(self):
        return self.annotate(max_date=models.Max('book__publication_date')).order_by('-max_date')[:5]

class BookManager(models.Manager):
    def get_books_published_after_year(self, year):
        return self.filter(publication_date__gte=f"{year}-01-01")

    def get_books_with_genre(self, genre_name):
        return self.filter(genre__name=genre_name)