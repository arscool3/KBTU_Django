from django import forms

from .models import Film, Actor, Genre, Director


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film 
        fields = '__all__'

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor 
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre 
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'