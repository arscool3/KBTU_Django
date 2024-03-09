from django.contrib import admin

from my_app.models import Author, Genre, Publisher, Book, User, Comment, Favorite

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Favorite)