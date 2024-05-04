from django.db import models

# Manager for Posts
class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def by_category(self, category_name):
        return self.get_queryset().filter(category__name=category_name)

# Manager for Comments
class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)

    def by_user(self, user):
        return self.get_queryset().filter(user=user)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    objects = PostManager()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    objects = CommentManager()
