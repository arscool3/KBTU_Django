from django.contrib import admin
from papers.models import Paper, Tag, Category

admin.site.register(Paper)
admin.site.register(Tag)
admin.site.register(Category)
