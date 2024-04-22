from django import forms
from .models import Author, Book, Publisher, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'books_published']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'books']