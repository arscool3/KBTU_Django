from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'genre')

    def __str__(self):
        return f"{self.book} - {self.genre}"

class BookManager(models.Manager):
    def published_after(self, year):
        return self.get_queryset().filter(publication_date__year__gt=year)

    def with_genres(self):
        return self.prefetch_related('bookgenre_set')

class BookQuerySet(models.QuerySet):
    def by_author(self, author_name):
        return self.filter(author__name=author_name)

Book.objects = BookManager.as_manager()
Book.objects = BookQuerySet.as_manager()
