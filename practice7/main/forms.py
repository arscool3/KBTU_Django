from django import forms

from .models import Book, Author, Library, Client

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = "__all__"

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"