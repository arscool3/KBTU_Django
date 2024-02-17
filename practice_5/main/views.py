from django.shortcuts import render

# Create your views here.
student_list = [
    'Beket',
    'Riza',
    'Bakha'
]

teachers = [
    'Arslan',
    'Bobur',
    'Yelibay'
]

def view(request):
    return render(request, 'main.html', {
            'student_list': student_list,
            'teachers': teachers
    })