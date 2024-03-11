from django import forms

from my_app.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publish_date']
        widgets = {
            'publish_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd'})
        }