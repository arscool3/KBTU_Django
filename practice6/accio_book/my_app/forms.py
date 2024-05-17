from django import forms

from my_app.models import Book, Author, Favorite, User, Genre

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publish_date']
        widgets = {
            'publish_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd'})
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'biography']

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ['book']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

