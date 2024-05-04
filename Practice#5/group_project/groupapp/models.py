from django.db import models

class AbstractItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Mark this as an abstract class

class Book(AbstractItem):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publication_date = models.DateField()

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey('Reviewer', on_delete=models.CASCADE, blank=True, null=True)

class Reviewer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# Book Manager
class BookManager(models.Manager):
    def published_after(self, year):
        return self.get_queryset().filter(publication_date__year__gt=year)

    def with_reviews(self):
        return self.prefetch_related('review_set')

Book.objects = BookManager.as_manager()

# Review QuerySet
class ReviewQuerySet(models.QuerySet):
    def by_author(self, author_name):
        return self.filter(author__name=author_name)

    def with_high_rating(self, threshold=4):
        return self.filter(rating__gte=threshold)

Review.objects = ReviewQuerySet.as_manager()
