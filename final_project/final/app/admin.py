from django.contrib import admin
from .models import Company, Employee, Project, Task, Report, Salary

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Report)
admin.site.register(Salary)
