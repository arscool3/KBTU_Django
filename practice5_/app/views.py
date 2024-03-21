from django.shortcuts import render, redirect
from .forms import CorpForm, DepForm, EmpForm, ProForm
from .models import Corporation, Department, Employee, Project

def corporations_and_departments(request):
    corporations = Corporation.objects.all()
    departments = Department.objects.all()
    employees = Employee.objects.all()
    projects = Project.objects.all()
    corp_form = CorpForm(prefix='corp')
    dep_form = DepForm(prefix='dep')
    emp_form = EmpForm(prefix='emp')
    pro_form = ProForm(prefix='pro')

    if request.method == 'POST':
        corp_form = CorpForm(request.POST, prefix='corp')
        dep_form = DepForm(request.POST, prefix='dep')
        emp_form = EmpForm(request.POST, prefix='emp')
        pro_form = ProForm(request.POST, prefix='pro')

        if corp_form.is_valid():
            Corporation.objects.create(**corp_form.cleaned_data)
            corp_form = CorpForm() 
        elif dep_form.is_valid():
            Department.objects.create(**dep_form.cleaned_data)
            dep_form = DepForm()  
        elif emp_form.is_valid():
            Employee.objects.create(**emp_form.cleaned_data)
            emp_form = EmpForm()  
        elif pro_form.is_valid():
            Project.objects.create(**pro_form.cleaned_data)
            pro_form = ProForm()  

    return render(request, 'corp.html', {
        'corporations': corporations,
        'departments': departments,
        'employees': employees,
        'projects': projects,
        'corp_form': corp_form,
        'dep_form': dep_form,
        'emp_form': emp_form,
        'pro_form': pro_form,
        
    })

def get_employees_age(request):
    age = request.GET.get('age')
    employees = Employee.objects.get_employee_by_age(age) if age else Employee.objects.none()
    return render(request, 'employee.html', {'employees': employees})

def get_employees_salary(request):
    salary = request.GET.get('salary')
    employees = Employee.objects.get_employee_by_salary(salary) if salary else Employee.objects.none()
    return render(request, 'employee.html', {'employees': employees})


def get_projects(request):
    projects = Project.objects.get_successful_projects()
    return render(request, 'projects.html', {'projects': projects})


