from django import forms

class CountryForm(forms.Form):
    officialName = forms.CharField(label="Official name",max_length=255)
    englishName = forms.CharField(label="English name",max_length=255)
    area = forms.DecimalField(label="Land area")

class CityForm(forms.Form):
    name = forms.CharField(label="City's name",max_length=255)
    country = forms.CharField(label="Country",max_length=255)

class CitizenForm(forms.Form):
    fname = forms.CharField(label="First name",max_length=255)
    lname = forms.CharField(label="Last name",max_length=255)
    age = forms.IntegerField(label="Age")
    city = forms.CharField(label="City",max_length=255)

class PresidentForm(forms.Form):
    fname = forms.CharField(label="First name",max_length=255)
    lname = forms.CharField(label="Last name",max_length=255)
    age = forms.IntegerField(label="Age")
    country = forms.CharField(label="Country",max_length=255)