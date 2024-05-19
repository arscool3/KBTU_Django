from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Employee, Project, Task, Report, Salary
from .serializers import CompanySerializer, EmployeeSerializer, ProjectSerializer, TaskSerializer, ReportSerializer, SalarySerializer
from .permissions import IsAuthenticatedForGETRequests, IsAdminForOtherRequests
from .tasks import update_task_status

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedForGETRequests, IsAdminForOtherRequests]

    def perform_update(self, serializer):
        serializer.save()
        update_task_status.delay(serializer.instance.id, 'Updated Status')

    @action(detail=True, methods=['post'], permission_classes=[IsAdminForOtherRequests])
    def change_status(self, request, pk=None):
        task = self.get_object()
        new_status = request.data.get('status')
        update_task_status.delay(task.id, new_status)
        return Response({'status': 'Task status update scheduled'}, status=status.HTTP_200_OK)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedForGETRequests, IsAdminForOtherRequests]

    @action(detail=True, methods=['post'], permission_classes=[IsAdminForOtherRequests])
    def activate(self, request, pk=None):
        company = self.get_object()
        company.is_active = True
        company.save()
        return Response({'status': 'Company activated'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminForOtherRequests])
    def deactivate(self, request, pk=None):
        company = self.get_object()
        company.is_active = False
        company.save()
        return Response({'status': 'Company deactivated'}, status=status.HTTP_200_OK)


def company_info_view(request):
    companies = Company.objects.all()
    return render(request, 'app/company_info.html', {'companies': companies})

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedForGETRequests, IsAdminForOtherRequests]

    @action(detail=True, methods=['post'], permission_classes=[IsAdminForOtherRequests])
    def promote(self, request, pk=None):
        employee = self.get_object()
        employee.position = 'Senior ' + employee.position
        employee.save()
        return Response({'status': 'Employee promoted'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminForOtherRequests])
    def demote(self, request, pk=None):
        employee = self.get_object()
        if 'Senior ' in employee.position:
            employee.position = employee.position.replace('Senior ', '', 1)
            employee.save()
            return Response({'status': 'Employee demoted'}, status=status.HTTP_200_OK)
        return Response({'status': 'Cannot demote'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def get_salary(self, request, pk=None):
        employee = self.get_object()
        salaries = employee.salaries.all()
        serializer = SalarySerializer(salaries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedForGETRequests, IsAdminForOtherRequests]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedForGETRequests, IsAdminForOtherRequests]

    # def perform_update(self, serializer):
    #     serializer.save()
    #     update_task_status.delay(serializer.instance.id, 'Updated Status')

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticatedForGETRequests, IsAdminForOtherRequests]


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsAuthenticatedForGETRequests, IsAdminForOtherRequests]

