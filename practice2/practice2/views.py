from django.shortcuts import render

def student_list(request):
    students = ['Yerzhigit', 'Mynzhan', 'Zhainar', 'Ramazan']
    return render(request, 'student_list.html', {'students': students})