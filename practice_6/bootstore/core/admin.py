from django.contrib import admin
from .models import Author, Publisher, Book, UserProfile, Order, Cart, CartItem, OrderItem

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
