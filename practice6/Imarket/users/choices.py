from django.db import models


class Role(models.TextChoices):
    SELLER = 'Seller'
    CUSTOMER = 'Customer'
    ADMIN = 'Admin'
