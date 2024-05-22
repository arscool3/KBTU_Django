
from django import forms
from .models import Artist, Album, Song, Genre

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_date', 'artist', 'genres']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'album']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']
