from django.db import models

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(TimestampedModel):
    name = models.CharField(max_length=100)
    class Meta:
        app_label = 'my_app'

    def __str__(self):
        return self.name

class Genre(TimestampedModel):
    name = models.CharField(max_length=100)
    class Meta:
        app_label = 'my_app'

    def __str__(self):
        return self.name


class BookQuerySet(models.QuerySet):
    def best_sellers(self):
        return self.order_by('-sales')[:5]

class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model)

    def best_sellers(self):
        return self.get_queryset().best_sellers()

class Book(TimestampedModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sales = models.IntegerField(default=0)

    objects = BookManager()
    class Meta:
        app_label = 'my_app'

    def __str__(self):
        return self.title

class Order(TimestampedModel):
    books = models.ManyToManyField(Book)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        app_label = 'my_app'

    def __str__(self):
        return f"Order {self.id}"