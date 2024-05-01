from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthorQuerySet(models.QuerySet):
    def get_by_name(self, name: str):
        return self.filter(author_name__icontains=name)

    def get_abai(self):
        return self.filter(author_name="Abai")

    def get_all(self):
        return self.all()


class Author(BaseModel):
    objects = AuthorQuerySet.as_manager()
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class BookQuerySet(models.QuerySet):
    def available_books(self):
        return self.filter(copies_available__gt=0)

    def overdue_books(self):
        return self.filter(borrowedbook__return_date__lt=models.F('borrowedbook__expected_return_date'))

    def get_by_title(self, title: str):
        return self.filter(book__title=title)


class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model)


class Book(BaseModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    copies_available = models.IntegerField(default=1)
    objects = BookManager()

    def __str__(self):
        return self.title






class Member(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class BorrowedBook(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
