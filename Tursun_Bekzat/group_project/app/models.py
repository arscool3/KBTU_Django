from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Department(BaseModel):
    location = models.CharField(max_length=100)
    since = models.IntegerField()


class AuthorQuerySet(models.QuerySet):
    def department_by(self, department):
        return self.filter(department=department)

    def experience_by(self, author):
        return self.filter(experience=author.experience)


class AuthorManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model)



class Author(BaseModel):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    experience = models.IntegerField()


class BookQuerySet(models.QuerySet):
    def published_books(self):
        return self.filter(status='published')

    def authored_by(self, author):
        return self.filter(author=author)

    def sortbyname(self, title):
        return self.filter(title=title)


class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model)


class Book(BaseModel):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    objects = BookManager()

    # Example custom queryset method
    def get_published_books(self):
        return self.objects.published_books()

    # Example custom queryset method
    def get_books_authored_by(self, author):
        return self.objects.authored_by(author)

class Review(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    content = models.TextField()





