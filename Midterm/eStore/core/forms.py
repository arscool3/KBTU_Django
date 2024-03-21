from django import forms
from .models import * 
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('id','name','photoUrl')

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class StoreItemForm(forms.ModelForm):
    class Meta:
        model = StoreItem
        fields = '__all__'
        

class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ('id','username', 'email', 'password')

class CartForm(forms.ModelForm):
    # user_info = UserForm(source= 'user', read_only = True)
    class Meta:
        model = Cart
        fields = '__all__'

class ProductPriceForm(forms.ModelForm):
    # store_items = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'photoUrl']

    # def get_store_items(self, product):
    #     store_items = StoreItem.objects.filter(product=product).order_by('price')
    #     return [{'store': item.store.store_name, 'price': item.price} for item in store_items]


class CartItemForm(forms.ModelForm):
    # products = ProductPriceForm(source='product', read_only=True)
    # carts = CartForm(source = 'cart', read_only = True)
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Cart.objects.create(user=user)
        return user