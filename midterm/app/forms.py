from django import forms

from .models import Customer, Room, Reservation


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.available()
