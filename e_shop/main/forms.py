from main.models import Product, Shop, Cart

from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields='__all__'

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields='__all__'

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields='__all__'