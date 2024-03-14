from django.contrib import admin
from main.models import Book, Author, Publisher, Country, City

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Country)
admin.site.register(City)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
