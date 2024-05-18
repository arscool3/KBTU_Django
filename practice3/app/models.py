from dataclasses import dataclass

from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    engine_volume = models.FloatField()
    horse_powers = models.IntegerField()

    def __str__(self):
        return self.brand.__str__() + " " + self.model.__str__()
