# api/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AnimeForm, MangaForm, LightNovelForm, GenreForm, ProfileForm
from .models import Anime, Manga, LightNovel, Genre
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction, IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)
        return redirect('signup_redirect')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def anime_create(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shiki:anime_list')
    else:
        form = AnimeForm()
    return render(request, 'anime_form.html', {'form': form})


@login_required
def manga_create(request):
    if request.method == 'POST':
        form = MangaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manga_list')
    else:
        form = MangaForm()
    return render(request, 'manga_form.html', {'form': form})


@login_required
def light_novel_create(request):
    if request.method == 'POST':
        form = LightNovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('light_novel_list')
    else:
        form = LightNovelForm()
    return render(request, 'light_novel_form.html', {'form': form})


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
def anime_delete(request, anime_id):
    anime = get_object_or_404(Genre, pk=anime_id)
    if request.method == 'POST':
        anime.delete()
        return redirect('shiki:anime_list')
    return render(request, 'anime_delete_confirm.html', {'anime': anime})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('login_redirect')


from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class CustomLogoutView(LogoutView):
    def get_next_page(self):
        next_page = super().get_next_page()
        if next_page:
            return next_page
        else:
            return reverse_lazy('logged_out')


@login_required
def profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'profile.html', {'form': form})