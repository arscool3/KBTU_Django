from django import forms

from .models import Courier, Order, User


class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
