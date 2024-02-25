from django import forms
from .models import Author, Book, Publisher, Magazine

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'location']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ['title', 'publisher', 'frequency']
