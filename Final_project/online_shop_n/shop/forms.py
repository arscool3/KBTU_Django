from django import forms
from .models import Review, Order, OrderItem

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']