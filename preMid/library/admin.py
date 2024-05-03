from django.contrib import admin

from library.models import *

# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Client)
