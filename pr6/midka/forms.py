from django import forms
from django.contrib.auth.forms import UserCreationForm

from midka.models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class CustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = '__all__'


class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book', 'due_back']
        user_id = forms.IntegerField()
        book_instance_id = forms.IntegerField()
