from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    published_date = models.DateField()
    cover_image = models.ImageField(upload_to='manga_covers/', default='manga_covers/Black_Bright.jpg')


    def __str__(self):
        return self.title


class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    number = models.IntegerField()
    upload_date = models.DateField()

    def __str__(self):
        return f"{self.manga.title} - Chapter {self.number}"


class Page(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='pages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='chapter_pages/')
    page_number = models.IntegerField()

    def __str__(self):
        return f"{self.chapter.manga.title} - Chapter {self.chapter.number} - Page {self.page_number}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.manga.title}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)