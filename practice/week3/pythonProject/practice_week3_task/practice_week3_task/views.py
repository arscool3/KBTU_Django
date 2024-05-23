from django.shortcuts import render, redirect
from .forms import MyForm
from .models import Product, Order

def students_list(request):
    students = ['Ali Zhumataev', 'Ali Madiyar', 'Zhilkibaev Ernar', 'Mauletkhan Nurbek']
    return render(request, 'students_list.html', {'students': students})


def teachers_list(request):
    teachers = ['Bobur','Ali','Askar', 'Baisak', 'Pacman']
    return render(request, 'teachers_list.html', {'teachers': teachers})


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_template.html')
    else:
        form = MyForm()

    return render(request, 'my_template.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


