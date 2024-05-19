from django import forms
from .models import Booking, Review, Payment, Notification

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['theme', 'date', 'time', 'guests']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message']