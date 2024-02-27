from django.contrib import admin

from pr_lesson_6.api.models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(CustomUser)