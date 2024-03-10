from django.contrib import admin

from my_app.models import Author, Genre, Book, User, Comment, Favorite, UserProfile, ReadingProgress

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(UserProfile)
admin.site.register(ReadingProgress)