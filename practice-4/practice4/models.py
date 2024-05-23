from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

class CategoryManager(models.Manager):
    def get_active_categories(self):
        return self.filter(is_active=True)

    def get_category_by_name(self, name):
        return self.get(name=name)

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    objects = CategoryManager()

    def __str__(self):
        return self.name

class PostManager(models.Manager):
    def get_published_posts(self):
        return self.filter(is_published=True)

    def get_posts_by_user(self, user_id):
        return self.filter(author_id=user_id)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts')

    objects = PostManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]  # Return first 20 characters of the comment
