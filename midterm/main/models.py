from django.db import models
from django.contrib.auth.models import User

class AuthorManager(models.QuerySet):
  def get_author_by_username(self, _username):
    return self.filter(username=_username)

class Author(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()
  objects = AuthorManager().as_manager()

  def __str__(self):
    return self.user.username


class CategoryManager(models.Manager):
  def get_queryset(self) -> models.QuerySet:
    return super().get_queryset().order_by('name')

class Category(models.Model):
  name = models.CharField(max_length=100)
  objects = CategoryManager()

  class Meta:
    verbose_name_plural = 'categories'

  def __str__(self):
    return self.name

class BookQuerySet(models.QuerySet):
  def order_by_author(self):
    return self.order_by('author')
  
class Book(models.Model):
  title = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  publication_date = models.DateField()
  objects = BookQuerySet().as_manager()

  def __str__(self):
    return self.title

class ConsumerManager(models.Manager):
  def get_queryset(self) -> models.QuerySet:
    return super().get_queryset().order_by('user')

class Consumer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  books = models.ManyToManyField(Book, related_name='consumers')
  objects = ConsumerManager()

  def __str__(self):
    return self.user.username


class ReviewQuerySet(models.QuerySet):
  def order_by_user(self):
    return self.order_by('user')
  
  def order_by_book(self):
    return self.order_by('book')
  
  def order_by_rating_asc(self):
    return self.order_by('rating')

  def order_by_rating_desc(self):
    return self.order_by('-rating')
  
  
class ReviewManager(models.Manager):
  def get_queryset(self):
    return ReviewQuerySet(self.model, self._db)
  
  def order_by_book_name(self):
    return self.get_queryset().order_by_book()
  
  def order_by_username(self):
    return self.get_queryset().order_by_user()
  
  def order_by_rating_asc(self):
    return self.get_queryset().order_by_rating_asc()

  def order_by_rating_desc(self):
    return self.get_queryset().order_by_rating_desc()

class Review(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField()
  rating = models.IntegerField()
  objects = ReviewManager()

  def __str__(self):
    return f"{self.user.username}'s review of {self.book.title}"