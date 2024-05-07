from django.db import models


class Consultant(models.Manager):
    def expensive_books(self):
        return self.get_queryset().filter(price__gte=100)

    def fiction_books(self):
        return self.get_queryset().filter(genre='Fiction')


class BookstoreClerk(models.Manager):
    def alphabetically_books(self):
        return self.get_queryset().order_by('name').values()

    def non_fiction_books(self):
        return self.get_queryset().exclude(genre='Fiction')


class Base(models.Model):
    name = models.CharField(max_length=20, default='default')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    price = models.IntegerField()
    objects = models.Manager()
    consultants = Consultant()
    bookstore_clerks = BookstoreClerk()


class Magazine(Base):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.IntegerField()
