from django.shortcuts import render, redirect

from django.db.models import Q
from django.http import HttpResponse

from app.models import Film, Actor, Director, Genre
from .forms import FilmForm, GenreForm, DirectorForm, ActorForm


def get_films(request):
    films = Film.objects
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = FilmForm()
        if name := request.GET.get('name'):
            films = films.filter(name=name.capitalize())
        films = films.all()
        return render(request, "main.html", {"iterable": films, "object": "Film", 'form': form})

def get_films_by_rating(request):
    films = Film.objects.get_film_by_rating()
    return render(request, "main.html", {"iterable": films, "object": "Film"})



def get_director(request):
    directors = Director.objects
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = DirectorForm()
        if name := request.GET.get('name'):
            directors = directors.filter(name=name.capitalize())
        directors = directors.all()
        return render(request, "main.html", {"iterable": directors, "object": "Directors", 'form': form})

def get_genres(request):
    genres = Genre.objects
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = GenreForm()
        if name := request.GET.get('name'):
            genres = genres.filter(name=name.capitalize())
        genres = genres.all()
        return render(request, "main.html", {"iterable": genres, "object": "Genres", 'form': form})
