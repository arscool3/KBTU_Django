from django import forms

class StudentForm(forms.Form):
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=100)
    StudentID = forms.CharField(max_length=20)
    Faculty = forms.CharField(max_length=100)
