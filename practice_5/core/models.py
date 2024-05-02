from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class PostQuerySet(models.QuerySet):
    def get_by_author(self, author):
        return self.filter(author=author)

class StoryNoteQuerySet(models.QuerySet):
    def get_by_author(self, author):
        return self.filter(author=author)


class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    objects = PostQuerySet.as_manager()

    def __str__(self) -> str:
        return self.title

class StoryNote(BaseModel):
    note = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.note


class CommentQuerySet(models.QuerySet):
    def get_by_post(self, post):
        return self.filter(post=post)

    def get_recent(self):
        return self.order_by('created_at')
    
    def get_by_author(self, author):
        return self.filter(author=author)
    
    def count_by_post(self, post):
        return self.filter(post=post).count()


class Comment(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    objects = CommentQuerySet.as_manager()

    def __str__(self) -> str:
        return self.author + " " + self.text