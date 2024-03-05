from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()

class Meta:
    permissions = [
        ("delete_movie", "Can delete a movie"),
    ]