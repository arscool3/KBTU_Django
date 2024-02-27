from django.shortcuts import render

from django.http import HttpResponse
from pr_lesson_6.api.models import *


def get_users(request):
    users = CustomUser.objects.all()
    return render(request, 'index.html', {'users': users})
