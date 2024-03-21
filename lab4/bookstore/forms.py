from django import forms
from .models import Book, Author, Genre, Publisher

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publisher', 'publish_date']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'nationality']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'location']
