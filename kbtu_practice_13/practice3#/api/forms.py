from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)