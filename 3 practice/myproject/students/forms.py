from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label='Student Name', max_length=100)
