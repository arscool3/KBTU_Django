from django import forms
from .models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publishedDate']


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['name']


class ReadingListForm(forms.ModelForm):
    class Meta:
        model = ReadingList
        fields = ['title', 'reader', 'books']
