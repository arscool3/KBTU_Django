import datetime
from dataclasses import dataclass

from django.db import models


# Relationships
# Student <-> Lesson (Many to Many)
# Lesson <-> Teacher (Many to One) done

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

# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py dbshell

# Migrations for 'core':
#   core/migrations/0001_initial.py
#     - Create model Lesson
#     - Create model Teacher
#     - Create model Student
#     - Add field teacher to lesson
