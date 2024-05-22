

from django.shortcuts import render
from .models import Artist, Album, Song

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})
