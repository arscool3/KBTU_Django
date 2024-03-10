from django import forms
from .models import Product, Order, Cart, Payment, UserProfile, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'stock_quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'products', 'total_price', 'status']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'products', 'total_price']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'amount', 'status']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
