from django.contrib import admin
from .models import Book, Author, Review, Department


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)
admin.site.register(Department)
