# api/forms.py
from django import forms
from .models import *


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = '__all__'


class LightNovelForm(forms.ModelForm):
    class Meta:
        model = LightNovel
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
