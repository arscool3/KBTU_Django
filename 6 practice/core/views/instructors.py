from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from core.models import *
from core.forms import *
from rest_framework.decorators import api_view

@api_view(['GET'])
@login_required(login_url='login')
def get_all_instructors(request):
    if request.method == 'GET':
        instructors = Instructor.objects.all()
        return render(request, 'index.html', {
            'iterable_name': 'Instructor',
            'iterable': instructors
        })

