from django.db import models

# Create your models here.
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    position = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(Employee, related_name='projects')


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)


class Report(models.Model):
    text = models.TextField()
    employee = models.ForeignKey(Employee, related_name='reports', on_delete=models.CASCADE)
    date = models.DateField()


class Salary(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(Employee, related_name='salaries', on_delete=models.CASCADE)
    date = models.DateField()
