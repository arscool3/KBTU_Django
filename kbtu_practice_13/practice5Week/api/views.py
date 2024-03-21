from django.shortcuts import render


def cars_list(request):
    cars = ['Lamborghini', 'Ferrari', 'Toyota', 'Mazda']
    return render(request, 'cars_list.html', {'cars': cars})
