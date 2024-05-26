from django.db import models

class AuthorManager(models.Manager):
    def get_young_authors(self):
        return self.filter(age__lt=30)

    def get_old_authors(self):
        return self.filter(age__gte=60)

class BookManager(models.Manager):
    def get_fiction_books(self):
        return self.filter(genre='Fiction')

    def get_non_fiction_books(self):
        return self.filter(genre='Non-Fiction')