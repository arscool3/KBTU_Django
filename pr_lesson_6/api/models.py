from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)


class Author(Person):
    pass


class CustomUser(Person):
    pass


class CustomUserQuerySet(models.QuerySet):

    def get_name(self, username: str):
        return self.filter(name=username)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    user = models.ManyToManyField(CustomUser, related_name='books')
