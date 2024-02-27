from django.db import models
from django.contrib.auth.models import User

from blog.managers import CommentQuerySet, PostQuerySet

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ContentItem(TimeStampedModel):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts')
    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title
    def publish(self):
        self.published = True
        self.save()

    def get_comments_count(self):
        return self.comment_set.count()
    
    def get_approved_comments(self):
        return self.comment_set.filter(approved=True)

    def get_latest_posts(self, num_posts=5):
        return self.objects.order_by('-created_at')[:num_posts]
    
    @staticmethod
    def get_posts_by_category(category_name):
        return Post.objects.filter(categories__name=category_name)
    
    @classmethod
    def create_post(cls, title, content, author, categories=None):
        post = cls(title=title, content=content, author=author)
        post.save()
        if categories:
            post.categories.add(*categories)
        return post

    def add_category(self, category_name):
        category, created = Category.objects.get_or_create(name=category_name)
        self.categories.add(category)
    


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    objects = CommentQuerySet.as_manager()

    def __str__(self):
        return f"{self.author.username} - {self.post.title}"
    def approve(self):
        self.approved = True
        self.save()

    def disapprove(self):
        self.approved = False
        self.save()
    @classmethod
    def create_comment(cls, post, author, text):
        comment = cls(post=post, author=author, text=text)
        comment.save()
        return comment

    def update_comment_text(self, new_text):
        self.text = new_text
        self.save() 

    def get_comment_author(self):
        return self.author

    @staticmethod
    def get_comments_by_user(user):
        return Comment.objects.filter(author=user)

    def get_comment_excerpt(self, length=50):
        return self.text[:length] + '...' if len(self.text) > length else self.text