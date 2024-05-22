from django.shortcuts import render
from django.http import HttpResponse


numbers = [
    1, 3, 5, 7, 8,
]


def test(request):
    result = numbers[0]+ numbers[1]
    return HttpResponse(f"result = {result }")

def to_str(request):
    str = ""
    for i in numbers:
        str+= str
    return HttpResponse(f" string result is{str} ")

def first_item(request):
    return HttpResponse(f"frist item is {numbers[0]}")