from django.db import models
from apps.shops.models import City

# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name