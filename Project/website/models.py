from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

from Project import settings


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Novel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    cover_image = models.ImageField(upload_to='media/novels/covers/', null=True, blank=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    novel = models.ForeignKey(Novel, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    chapter_number = models.IntegerField()

    def __str__(self):
        return f"{self.title} - Chapter {self.chapter_number}"


class Review(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.novel.title}"


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)


def __str__(self):
    if self.chapter:
        return f"{self.user.username}'s bookmark for {self.novel.title} - Chapter {self.chapter.chapter_number}"
    else:
        return f"{self.user.username}'s bookmark for {self.novel.title}"
