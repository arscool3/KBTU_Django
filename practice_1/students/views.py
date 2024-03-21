from django.shortcuts import render


def student_list(request):
    students = [
        'Oralbay Nurzhan',
        'Arslan Yersain',
        'Ivanov Ivan',
        'Aliev Ali',
    ]
    context = {'students': students}
    return render(request, 'students/student_list.html', context)
