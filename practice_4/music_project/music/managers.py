
from datetime import date, timedelta
from django.db import models

class ArtistManager(models.Manager):
    def get_popular_artists(self):
        
        return self.annotate(num_albums=models.Count('albums')).filter(num_albums__gt=100)

class AlbumManager(models.Manager):
    def get_recent_albums(self):
       
        
        one_year_ago = date.today() - timedelta(days=365)
        return self.filter(release_date__gte=one_year_ago)

class GenreManager(models.Manager):
    def get_genre_with_most_albums(self):
        """
        Returns the genre with the most albums.
        """
        # Example query logic: Get the genre with the most albums
        return self.annotate(num_albums=models.Count('albums')).order_by('-num_albums').first()

