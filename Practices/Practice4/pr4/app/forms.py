from django import forms

from .models import *


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = FamilyDoctor
        fields = '__all__'

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
