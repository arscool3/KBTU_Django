from django.shortcuts import render


def view(request):
    Students = [
        {'name': 'Aizere', 'age': 19, 'sex': 'Female'},
        {'name': 'Arystan', 'age': 22, 'sex': 'Male'},
        {'name': 'Khafa', 'age': 23, 'sex': 'Male'},
    ]

    return render(request, 'index.html', {'students': Students})
