from django import forms


class StudentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    course = forms.IntegerField()