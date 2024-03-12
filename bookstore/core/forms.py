from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
