from django.shortcuts import render

from django.http import HttpResponse


def index(request):

    students = ['Gey', 'Madi', 'Charlie', 'Greg']
    
    # Pass the students list to the template through the context
    context = {'students': students}
    return render(request, 'practice2/students_list.html', context)
