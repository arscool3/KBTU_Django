from django import forms
from .models import Person

class MyForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']