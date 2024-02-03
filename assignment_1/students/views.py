from django.shortcuts import render

def student_list(request):
    students = [
        'Khalel Sanzhar',
        'Manas Khairullin',
        'Orynbasarov Ansar',
        'Aliturliev Batyrbek',
    ]
    context = {'students': students}
    return render(request, 'students/student_list.html', context)
