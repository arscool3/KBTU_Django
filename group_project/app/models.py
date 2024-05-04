from django.db import models

from django.db import models




# Extending Custom QuerySet for Book
class BookQuerySet(models.QuerySet):
    def by_publisher(self, publisher_name):
        return self.filter(publisher__name=publisher_name)

    def recent_books(self, days_ago):
        return self.filter(created_at__gte=timezone.now() - timedelta(days=days_ago))

    def books_with_high_ratings(self, threshold=4):
        return self.annotate(average_rating=Avg('reviews__rating')).filter(average_rating__gt=threshold)

    def books_with_reviews(self):
        return self.annotate(review_count=models.Count('reviews')).filter(review_count__gt=0)

# Extending Custom QuerySet for Review
class ReviewQuerySet(models.QuerySet):
    def recent_high_ratings(self, days_ago, threshold=4):
        return self.filter(created_at__gte=timezone.now() - timedelta(days=days_ago), rating__gt=threshold)

    def reviews_for_book(self, book_name):
        return self.filter(book__name=book_name)


# Custom Manager for Book
class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    def by_author(self, author_name):
        return self.get_queryset().by_author(author_name)

# Custom Manager for Review
class ReviewManager(models.Manager):
    def get_queryset(self):
        return ReviewQuerySet(self.model, using=self._db)

    def high_rating(self, threshold=4):
        return self.get_queryset().high_rating(threshold)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(TimeStampedModel):
    name = models.CharField(max_length=40)

class Publisher(TimeStampedModel):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=100)

class Book(TimeStampedModel):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    objects = BookManager()  # Attach the custom manager


class Review(TimeStampedModel):
    book = models.ManyToManyField(Book, related_name='reviews')
    review_text = models.CharField(max_length=255)
    rating = models.IntegerField(default=1)
    objects = ReviewManager()  # Attach the custom manager


