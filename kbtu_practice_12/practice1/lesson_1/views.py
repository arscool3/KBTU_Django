from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return HttpResponse("This is main page")

def more(request):
    return HttpResponse("This is more page")

def test(request):
    return HttpResponse("This is test page")