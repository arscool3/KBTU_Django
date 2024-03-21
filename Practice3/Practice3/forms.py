from django import forms
from .models import BasicInfo


class BasicForm(forms.ModelForm):
    class Meta:
        model = BasicInfo
        fields = ['name', 'email']
        labels = {
            'name': 'Ваше имя',
            'email': 'Ваш Email',
        }
