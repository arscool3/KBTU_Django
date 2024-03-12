# api/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnimeForm, MangaForm, LightNovelForm, GenreForm
from .models import Anime, Manga, LightNovel, Genre
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction, IntegrityError
from django.contrib import messages



def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # get named fields from the form data
            username = form.cleaned_data.get('username')
            # password input field is named 'password1'
            raw_passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)
        # return redirect('anime_list')
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        # create a user form and display it the signup page
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def anime_create(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shiki:anime_list')
    else:
        form = AnimeForm()
    return render(request, 'anime_form.html', {'form': form})


def manga_create(request):
    if request.method == 'POST':
        form = MangaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manga_list')
    else:
        form = MangaForm()
    return render(request, 'manga_form.html', {'form': form})


def light_novel_create(request):
    if request.method == 'POST':
        form = LightNovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('light_novel_list')
    else:
        form = LightNovelForm()
    return render(request, 'light_novel_form.html', {'form': form})


def genre_create(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shiki:genre_list')
    else:
        form = GenreForm()
    return render(request, 'genre_form.html', {'form': form})


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})


def genre_read(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    return render(request, 'genre_detail.html', {'genre': genre})


def genre_update(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('shiki:genre_list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genre_form.html', {'form': form})


def genre_delete(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    if request.method == 'POST':
        try:
            genre.delete()
            return redirect('shiki:genre_list')
        except IntegrityError:
            messages.error(request, "Cannot delete the genre because it has associated records.")
            return redirect('shiki:genre_list')  # Redirect to the genre list page with an error message
    return render(request, 'genre_delete_confirm.html', {'genre': genre})


def anime_list(request):
    anime = Anime.objects.all()
    return render(request, 'anime_list.html', {'anime': anime})


def anime_read(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    return render(request, 'anime_detail.html', {'anime': anime})


def anime_update(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    if request.method == 'POST':
        form = AnimeForm(request.POST, instance=anime)
        if form.is_valid():
            form.save()
            return redirect('shiki:anime_list')
    else:
        form = AnimeForm(instance=anime)
    return render(request, 'anime_form.html', {'form': form})


def anime_delete(request, anime_id):
    anime = get_object_or_404(Genre, pk=anime_id)
    if request.method == 'POST':
        anime.delete()
        return redirect('shiki:anime_list')
    return render(request, 'anime_delete_confirm.html', {'anime': anime})
