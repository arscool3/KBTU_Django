from django.contrib import admin
from .models import Book, Author, Library, Client


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Client)
# Register your models here.
