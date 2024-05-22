from django import forms
from .models import Book, Author, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']