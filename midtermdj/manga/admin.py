from django.contrib import admin
from .models import Genre, Manga, Chapter, Page, Review, UserProfile

admin.site.register(Genre)
admin.site.register(Manga)
admin.site.register(Chapter)
admin.site.register(Page)
admin.site.register(Review)
admin.site.register(UserProfile)