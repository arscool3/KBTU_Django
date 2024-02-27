# forms.py
from django import forms
from .models import Author, Book, Publisher, BookInstance

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'age']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'location']

class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book', 'publisher', 'publication_date']
