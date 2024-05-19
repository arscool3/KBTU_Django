from django.db import models
from django.contrib.auth.models import AbstractUser

from recipe.models import Recipe
# Create your models here.
from .managers import KBTUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    saved_recipes = models.ManyToManyField(Recipe, through="Bookmark")
    photo = models.ImageField(upload_to='users', default='assets/dog.jpeg', blank=True, null=True)

    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = KBTUserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.recipe.title