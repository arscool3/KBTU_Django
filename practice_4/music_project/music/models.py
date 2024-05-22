# music/models.py

from django.db import models
from .managers import ArtistManager, AlbumManager, GenreManager

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    objects = ArtistManager()  # Using custom manager

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    genres = models.ManyToManyField('Genre', related_name='albums')  # Many-to-many relationship with Genre

    objects = AlbumManager()  # Using custom manager

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    albums = models.ManyToManyField('Album', related_name='genres')  # Many-to-many relationship with Album

    objects = GenreManager()  # Using custom manager

    def __str__(self):
        return self.name
