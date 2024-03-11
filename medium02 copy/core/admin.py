from django.contrib import admin
from .models import Article,Profile,Topic,Comment,Follow,Like,ReadingList

admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(ReadingList)