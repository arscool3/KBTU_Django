from django import forms


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
