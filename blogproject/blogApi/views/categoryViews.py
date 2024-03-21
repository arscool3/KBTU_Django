from django.shortcuts import render, redirect
from blogApi.models.category import Category
from django.contrib.auth import decorators
@decorators.login_required(login_url='login')
def get(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories':categories})
@decorators.login_required(login_url='login')
def post(request):
    if request.method =='POST':
        categories = Category()
        categories.name = request.POST.get('name')
        categories.description = request.POST.get('description')
        categories.save()
    return redirect('/categories')