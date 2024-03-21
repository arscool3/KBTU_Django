from django.contrib import admin

from library.models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Borrower)
admin.site.register(Author)