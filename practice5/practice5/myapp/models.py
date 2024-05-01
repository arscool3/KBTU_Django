from django.db import models

class Base(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class DirectorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class Director(Base):
    bio = models.TextField()
    age = models.IntegerField()
    objects = DirectorManager()

class GenreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
class Genre(Base):
    objects = GenreManager()

class FilmManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    def get_recent_film(self):
        return self.get_queryset().order_by('relase_date')
    
    def get_films_by_genre(self, genre_name):
        return self.get_queryset().filter(genre__name = genre_name)
    
    def get_film_by_rating(self):
        return self.get_queryset().order_by('-rating')
    

class Film(Base):
    release_date = models.DateField()
    director = models.ForeignKey(Director, on_delete = models.CASCADE)
    genre = models.ManyToManyField(Genre)
    rating = models.FloatField()
   
    objects = FilmManager()

class ActorManager(models.Manager):
    pass

class Actor(Base):
    bio = models.TextField()
    age = models.IntegerField()
    films = models.ManyToManyField(Film, related_name='actors')



    
    
