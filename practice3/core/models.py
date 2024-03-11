import datetime
from dataclasses import dataclass

from django.db import models


# Relationships
# Student <-> Lesson (Many to Many)
# Lesson <-> Teacher (Many to One) done

# Student <-> Event(Many to Many)
# Event <-> Organiser (Many to one)

class Person(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



class Student(Person):
    age = models.IntegerField()
    balance = models.IntegerField()
    events = models.ManyToManyField('Event')


class Event(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.CharField(max_length=100)
    organizer = models.ForeignKey('Organizer', on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.title


class Organizer(Person):
    pass

# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py dbshell

# Migrations for 'core':
#   core/migrations/0001_initial.py
#     - Create model Lesson
#     - Create model Teacher
#     - Create model Student
#     - Add field teacher to lesson