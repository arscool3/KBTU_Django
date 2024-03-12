from django.shortcuts import render
from .models import Manager, Department, Employee, Project

def manager_list(request):
    managers = Manager.objects.all()
    return render(request, 'manager_list.html', {'managers': managers})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})
