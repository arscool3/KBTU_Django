from django.http.response import JsonResponse
from django.shortcuts import render
from students import models


def student_list(request):
    students = models.Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
    # students_json = [s.to_json() for s in students]
    # return JsonResponse(students_json, safe=False)

