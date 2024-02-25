from django import forms
from .models import Author, Book, Publisher, Magazine

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'genre', 'price']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ['name', 'publisher', 'price']
