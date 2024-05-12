from django.shortcuts import render


students = ['Dima', 'Zoldaz', 'Camila', 'Lena', 'Ayazhan', 'Gleb']


def view(request):
    return render(request, 'Pr2App/index.html', {'students': students})