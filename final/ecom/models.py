from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .managers import *
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
import jwt
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ecom_user'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self.jwt_token()

    def jwt_token(self):
        payload = {
            'id': self.pk, 
            'exp': datetime.utcnow() + timedelta(hours=12) 
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return token


class Category(models.Model):
    name = models.CharField(max_length=255)
    photoUrl = models.TextField()
    objects = CategoryManager()
    def __str__(self):
        return f'Category name: {self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    photoUrl = models.TextField()
    def __str__(self):
        return f'Product name: {self.name}, category: {self.category} '

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ecom_comment'


    def __str__(self):
        return f"Comment by {self.author.username} on {self.post}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']