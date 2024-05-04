# models.py
from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=100)

    def method1(self):
        pass

    def method2(self):
        pass

class Department(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
