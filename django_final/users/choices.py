from django.db import models


class UserTypeChoices(models.TextChoices):
    Customer = "Customer"
    Manager = "Manager"
