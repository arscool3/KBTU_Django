from django import forms
from .models import Student

class MyForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']