from django import forms
from .models import *

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['seat_number', 'departure_date', 'airplane', 'consumer']


class AirplaneForm(forms.ModelForm):
    class Meta:
        model = Airplane
        fields = ['name', 'model', 'active']


class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['name', 'email', 'phone']