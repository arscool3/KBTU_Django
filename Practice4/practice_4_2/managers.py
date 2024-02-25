from django.db import models

class AuthorManager(models.QuerySet):
    def get_authors_with_books(self):
        return self.all()

class PublisherManager(models.Manager):
    def get_publishers_with_magazines(self):
        return self.select_related('magazine_set').all()
