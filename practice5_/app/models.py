from django.db import models

class Base(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        abstract = True
    def __str__(self):
        return self.name

class Corporation(Base):
    field = models.CharField(max_length=100)  
    staff_number = models.IntegerField(blank=True, null=True)


class Department(Base):
    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE)
    staff_number = models.IntegerField(blank=True, null=True)

class Employee(Base):
    position = models.CharField(max_length=100) 
    salary = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    Depratment = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

class Project(Base):
    budget=models.IntegerField(blank=True, null=True)
    is_successful=models.BooleanField(default=False)
    employee=models.ForeignKey(Employee,on_delete=models.PROTECT)
