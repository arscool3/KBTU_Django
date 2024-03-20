from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    return HttpResponse('This is main view')
def view2(request):
    return HttpResponse("This is basic view")
def view3(request):
    return HttpResponse("Test view")


