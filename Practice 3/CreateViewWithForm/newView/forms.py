from django import forms
from .models import UserName

class NewForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
