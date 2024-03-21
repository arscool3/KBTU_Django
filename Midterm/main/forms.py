from django import forms
from .models import City, Flight_fact, Flight_dim
class TicketSearchForm(forms.Form):
    From = forms.ModelChoiceField(queryset=City.objects.all())
    To = forms.ModelChoiceField(queryset=City.objects.all())
    Flight_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Seat_Class = forms.ChoiceField(choices=[(0, 'Business'), (1, 'Economy')])

class FlightForm(forms.Form):
    Flight = forms.ModelChoiceField(queryset=Flight_fact.objects.all())
    Date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))