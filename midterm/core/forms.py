from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class AddProductToOrderForm(forms.Form):
    product_id = forms.IntegerField(label='Product ID')
    quantity = forms.IntegerField(label='Quantity', min_value=1)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity
    
class AddProductToCartForm(forms.Form):
    product_id = forms.IntegerField(label='Product ID')
    quantity = forms.IntegerField(label='Quantity', min_value=1)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity