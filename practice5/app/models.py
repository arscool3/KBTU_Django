from django.db import models

class Base(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

class Corporation(Base):
    field = models.CharField(max_length=100)  # Adjust max_length according to your needs

class CEO(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-staff_count')  # Change to an existing field, or define 'area'
   

class Department(Base):
    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE)
    staff_count = models.IntegerField()
    objects = CEO()  # Default manager

class DepartmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-salary')  # Change to an existing field, or define 'area'

class Employee(Base):
    position = models.CharField(max_length=100)  # Adjust max_length according to your needs
    salary = models.IntegerField()
    age = models.IntegerField()
    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE, related_name='employees')  # Use 'Corporation' instead of 'corporation'
    objects = DepartmentManager()

class Project(Base):
    budget=models.IntegerField()
    is_successful=models.BooleanField(default=False)
    employee=models.ForeignKey(Employee,on_delete=models.PROTECT)
    objects=DepartmentManager()