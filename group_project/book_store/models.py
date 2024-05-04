from django.db import models

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AuthorQuerySet(models.QuerySet):
    def authors_with_books(self):
        return self.annotate(num_books=models.Count('book')).filter(num_books__gt=0)

class AuthorManager(models.Manager):
    def get_queryset(self):
        return AuthorQuerySet(self.model)

class Author(AbstractBaseModel):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    objects = AuthorManager()

    def __str__(self):
        return self.name

class BookQuerySet(models.QuerySet):
    def published_after(self, year):
        return self.filter(published_date__year__gt=year)

    def published_before(self, year):
        return self.filter(published_date__year__lt=year)

    def search_by_title(self, keyword):
        return self.filter(title__icontains=keyword)

class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model)

class Book(AbstractBaseModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    objects = BookManager()

    def __str__(self):
        return self.title
    
class Publisher(AbstractBaseModel):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BookPublisher(AbstractBaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    royalties = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.book} - {self.publisher}"
