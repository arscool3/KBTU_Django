from django import forms

from .models import School, Student


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ("name", "address")


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "age", "school")
