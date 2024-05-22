

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Author, Genre, Order, Review

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
