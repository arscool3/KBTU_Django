from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Company, Employee, Project, Task, Report, Salary
from .serializers import CompanySerializer, EmployeeSerializer, ProjectSerializer, TaskSerializer, ReportSerializer, SalarySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

def company_info_view(request):
    companies = Company.objects.all()
    return render(request, 'app/company_info.html', {'companies': companies})

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=['post'])
    def promote(self, request, pk=None):
        employee = self.get_object()
        employee.position = 'Senior ' + employee.position
        employee.save()
        return Response({'status': 'Employee promoted'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_salary(self, request, pk=None):
        employee = self.get_object()
        salaries = employee.salaries.all()
        serializer = SalarySerializer(salaries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_update(self, serializer):
        serializer.save()
        update_task_status.delay(serializer.instance.id, 'Updated Status')

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
from django.shortcuts import render

# Create your views here.
