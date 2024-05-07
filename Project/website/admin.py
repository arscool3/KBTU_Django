from django.contrib import admin
from .models import Novel, UserProfile, Chapter, Review, Bookmark

# Register your models here.
admin.site.register(Novel)
admin.site.register(UserProfile)
admin.site.register(Chapter)
admin.site.register(Review)
admin.site.register(Bookmark)
