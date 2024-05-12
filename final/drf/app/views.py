from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework import viewsets
from .models import Company, Employee, Project, Task, Report, Salary
from .serializers import CompanySerializer, EmployeeSerializer, ProjectSerializer, TaskSerializer, ReportSerializer, \
    SalarySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from .tasks import update_task_status


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]  # Требует аутентификации для всех операций

from django.shortcuts import render
from .models import Company

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'myapp/index.html', {'companies': companies})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def promote(self, request, pk=None):
        employee = self.get_object()
        employee.position = 'Senior ' + employee.position
        employee.save()
        return Response({'status': 'Employee promoted'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_salary(self, request, pk=None):
        """
        Custom action to retrieve the salary details of an employee.
        """
        employee = self.get_object()
        salaries = employee.salaries.all()
        serializer = SalarySerializer(salaries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]
    def perform_update(self, serializer):
        serializer.save()
        update_task_status.delay(serializer.instance.id, 'Updated Status')


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [permissions.IsAuthenticated]
