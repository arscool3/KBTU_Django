from django.db import models

# Abstract class
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Custom QuerySet
class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='published')

    def by_author(self, author):
        return self.filter(author=author)

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=10, default='draft')

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
