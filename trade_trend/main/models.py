from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images', default="static\images\home-appliances.jpg")

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id)

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=(('Pending', 'Pending'), ('Completed', 'Completed'), ('Canceled', 'Canceled')), default='Pending')

    def __str__(self) -> str:
        return str(self.id)
    
class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notification', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    notification_text = models.TextField(max_length=255, default='Your product status updated!')

    def __str__(self) -> str:
        return str(self.id)