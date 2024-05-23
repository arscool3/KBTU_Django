from django.db import models
from django.contrib.auth.models import User

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimestampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(TimestampedModel):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.title

class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.post}"

# Custom QuerySets
class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)

    def by_author(self, author):
        return self.filter(author=author)

class CommentQuerySet(models.QuerySet):
    def approved(self):
        return self.filter(approved=True)

# Add custom querysets to models
Post.add_to_class('objects', models.Manager.from_queryset(PostQuerySet)())
Comment.add_to_class('objects', models.Manager.from_queryset(CommentQuerySet)())
