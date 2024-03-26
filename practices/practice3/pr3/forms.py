from django import forms

class TestForm(forms.Form):
    fname = forms.CharField(label="fname",max_length=50)
    lname = forms.CharField(label="lname",max_length=50)
    age = forms.IntegerField(label="age")