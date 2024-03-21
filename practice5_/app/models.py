from django.db import models

class Base(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class CorporationQuerySet(models.QuerySet):
    def get_corporation_by_field(self, name: str, field: str):
        return self.filter(name=name, field=field)

class Corporation(Base):
    field = models.CharField(max_length=100)  
    staff_number = models.IntegerField(blank=True, null=True)
    objects = CorporationQuerySet.as_manager()

class DepartmentQuerySet(models.QuerySet):
    def get_departments_in_corporation(self, corporation):
        return self.filter(corporation=corporation)

class Department(Base):
    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE)
    staff_number = models.IntegerField(blank=True, null=True)
    objects = DepartmentQuerySet.as_manager()

class EmployeeQuerySet(models.QuerySet):
    def get_employee_by_salary(self, salary):
        return self.filter(salary=salary)

    def get_employee_by_age(self, age):
        return self.filter(age=age)

class Employee(Base):
    position = models.CharField(max_length=100) 
    salary = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    objects = EmployeeQuerySet.as_manager()

class ProjectQuerySet(models.QuerySet):
    def get_successful_projects(self):
        return self.filter(is_successful=True)

    def get_highest_budget_project(self):
        return self.order_by('-budget').first()

class Project(Base):
    budget = models.IntegerField(blank=True, null=True)
    is_successful = models.BooleanField(default=False)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    objects = ProjectQuerySet.as_manager()
