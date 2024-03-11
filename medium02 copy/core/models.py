from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
    
class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.TextField(max_length=255, default='', blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.title + "|" + str(self.author)

    def formatted_date_created(self):
        return self.date_created.strftime('%b %d, %Y')

    def get_absolute_url(self):
        return reverse('articles')
    
class ReadingList(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return f"Reading list for {self.profile.user.username}"

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.article.title}'

    def formatted_date_created(self):
        return self.date_created.strftime('%b %d, %Y')

    def get_absolute_url(self):
        return reverse('home')

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.follower.username} follows {self.followed_user.username}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} likes {self.article.title}'
