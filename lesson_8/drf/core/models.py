from django.db import models


class Weather(models.Model):
    temp = models.IntegerField()
    description = models.CharField(max_length=100)