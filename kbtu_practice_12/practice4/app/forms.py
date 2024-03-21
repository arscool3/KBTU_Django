from django import forms
from .models import Country, Citizen

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'language', 'population', 'area']


class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = ['name', 'age', 'country', 'has_criminal_issues']