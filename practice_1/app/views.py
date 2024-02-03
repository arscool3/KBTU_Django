from django.shortcuts import render

students = [
    'Nursultan',
    'Yersultan',
    'Aliar',
    'Bolat',
    'Temirlan',
]


def index(request):
    return render(request, 'index.html', {
        'students': students
    })
