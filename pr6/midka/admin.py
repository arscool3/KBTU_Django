from django.contrib import admin

from midka.models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Customer)