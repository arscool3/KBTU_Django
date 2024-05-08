from django.contrib import admin

from .models import Author, Book, Publisher, BookPublisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(BookPublisher)