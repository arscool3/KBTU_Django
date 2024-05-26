from django.contrib import admin
from Library.models import *

# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Client)
admin.site.register(Loan)
admin.site.register(PublishingOffice)