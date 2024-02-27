from django import forms

from .models import Planet, Satellite, Star, Resident


class PlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'


class SatelliteForm(forms.ModelForm):
    class Meta:
        model = Satellite
        fields = '__all__'


class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = '__all__'


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'

