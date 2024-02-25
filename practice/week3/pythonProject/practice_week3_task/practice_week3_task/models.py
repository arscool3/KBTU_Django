from dataclasses import dataclass
import datetime
from django.db import models


# Relationship
# Student <-> Lesson (Many to many)
# Lesson <-> Teacher (Many to One)


class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.field1} {self.field2}"



