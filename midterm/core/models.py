from django.db import models
from datetime import date
# Create your models here.

# Product model
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default = 0)
    category = models.CharField(max_length=15)
    image = models.ImageField()
    quantity = models.IntegerField(default = 0)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=100)

class Order(models.Model):
    order_date = models.DateField()
    customer_id = models.ForeignKey("Customer", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"Customer #{self.customer_id} ordered item #{self.product_id}"

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        """
        Calculate and return the total price of all products in the cart.
        """
        total = 0
        for item in self.cartitem_set.all():
            total += item.quantity * item.product.price
        return total

    def __str__(self):
        return f"Cart #{self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def subtotal(self):
        """
        Calculate and return the subtotal price of the item (product price * quantity).
        """
        return self.product.price * self.quantity

    def __str__(self):
        return f"CartItem #{self.id} in Cart #{self.cart.id}"