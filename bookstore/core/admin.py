from django.contrib import admin
from .models import Author, Genre, Book, Customer, Order, Review

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Review)