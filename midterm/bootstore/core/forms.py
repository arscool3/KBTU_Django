from django import forms
from .models import Book, Author, Publisher
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Author, Publisher

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'price']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
class OrderForm(forms.Form):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Books'
    )
    quantities = forms.IntegerField(
        label='Quantity',
        min_value=1,
        required=False
    )
