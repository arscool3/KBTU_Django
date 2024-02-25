from django import forms
from .models import MyModel


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel  # If you have a model to save form data, otherwise omit this line
        fields = ['field1', 'field2']  # Define the fields you want in your form


