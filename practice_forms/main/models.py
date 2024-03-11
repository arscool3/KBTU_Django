from django.db import models

# Create your models here.
class Computer(models.Model):
    name = models.CharField(max_length = 30)
    year = models.IntegerField(default=2010)
    price = models.FloatField(default=100000)

    def __str__(self):
        return self.name