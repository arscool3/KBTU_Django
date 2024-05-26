from django.db import models
from api.models.book import Book
from api.serializers import UserUpdatingSerializer
from django.contrib.auth.models import User

class UserList(models.Model):
    def __str__(self):
        return f'{self.id}  {self.name}   {self.user.username}'
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")
    books = models.ManyToManyField(Book)
    is_private = models.BooleanField(default=True)