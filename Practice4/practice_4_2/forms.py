from django import forms
from practice_4.models import Book, Magazine

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ['title', 'publisher', 'issue_date']
