from django.contrib import admin
from . import models

admin.site.register([
    models.Category,
    models.Product,
    models.Order,
    models.Cart,
    models.Payment,
    models.UserProfile
])