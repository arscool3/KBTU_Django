import dataclasses

from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import City, Customer, Seller, Item, Orders

@dataclasses.dataclass
class Student:
    name: str
    age: int
    course: int


students = [
    Student(name='Anar', age=18, course=2),
    Student(name='Dauren', age=19, course=2),
    Student(name='Daniyar', age=20, course=3),
]


def view(request):
    return render(request, 'index.html', {'students': students})

def view2(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        course = request.POST.get("course")
        students.append(Student(name = name, age = age, course = course))
        print('i am here')
    studentform = StudentForm()
    return render(request, 'index2.html', {'form': studentform})


def view3(request):
    Seller_list = Seller.objects
    if city_name := request.GET.get('city'):
        Seller_list = Seller_list.filter(city__name=city_name)
    Seller_list = Seller_list.all()
    print('Seller_list', Seller_list)
    return render(request, 'index3.html', {"iterable": Seller_list, "object": "Sellers"})

def view4(request):
    Item_list = Item.objects
    if item_id := request.GET.get('item_id'):
        Item_list = Item_list.filter(item__id=item_id)
    Item_list = Item_list.all()
    print('Item_list', Item_list)
    return render(request, 'index3.html', {"iterable": Item_list, "object": "Sellers"})

def view5(request):
    Item_list = Customer.objects.all().filter_name_starting_with_D()
    print('Item_list', Item_list)
    return render(request, 'index3.html', {"iterable": Item_list, "object": "Sellers"})
