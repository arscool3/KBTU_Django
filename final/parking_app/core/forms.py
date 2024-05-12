from django import forms

class ParkingReservationForm(forms.Form):
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
