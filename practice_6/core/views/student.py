from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from serializers import StudentSerializer
from core.models import *
from core.forms import *


@api_view(['GET'])
@login_required(login_url='login')
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return render(request, 'index.html', {
            'iterable_name': 'Student',
            'iterable': students
        })
