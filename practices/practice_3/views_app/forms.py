from django import forms
from .models import UserName

class NameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
