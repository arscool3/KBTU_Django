from django.db import models

class BookManager(models.Manager):
    def get_books_by_author(self, author_name):
        return self.filter(author__name=author_name)

class PublisherManager(models.Manager):
    def get_publishers_with_magazines(self):
        publishers = self.all()
        for publisher in publishers:
            publisher.magazines = publisher.magazines.all()
        return publishers

class AuthorManager(models.Manager):
    def get_authors_with_books(self):
        return self.select_related('books').all()
