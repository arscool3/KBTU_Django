from django.contrib import admin
from my_app.models import Author, Book, Order, Genre

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Genre)