from django import forms
from django.contrib.auth.forms import UserCreationForm

from library.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'birth_date': DateInput()
        }


class CustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        widgets = {
            'establishment_date': DateInput()
        }


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
        widgets = {
            'due_back': DateInput(),
            'borrowed_date': DateInput(),
        }

