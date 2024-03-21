from django.contrib import admin

# Register your models here.
from .models import Genre, Author, Publisher, UserProfile, Book, Review


admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Review)
admin.site.register(UserProfile)

