import datetime
from dataclasses import dataclass
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



class Student(Person):
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    lessons = models.ManyToManyField('Lesson')


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title


class Teacher(Person):
    pass

