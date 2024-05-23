from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PostManager(models.Model):
    def get_post_by_author(self, author):
        return self.filter(author=author)
    
    def get_post_by_topic(self, topic):
        return self.filter(topic=topic)

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    topics = models.ForeignKey(Topic, on_delete=models.CASCADE)
    objects = PostManager()

    def __str__(self):
        return self.title

class CommentManager(models.Manager):
    def get_comments_by_author(self, author):
        return self.filter(author=author)

    def get_comments_by_post(self, post):
        return self.filter(post=post)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    objects = CommentManager()

    def __str__(self):
        return f"{self.author} wrote comment to {self.post}"


