from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Student(Person):
    age = models.IntegerField()
