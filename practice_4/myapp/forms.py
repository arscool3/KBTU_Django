from django import forms
from .models import Model1

class Model1Form(forms.ModelForm):
    class Meta:
        model = Model1
        fields = ['name']
