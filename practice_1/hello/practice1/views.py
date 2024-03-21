from django.shortcuts import render
from django.http import HttpResponse


def viewshka1(request):
    return HttpResponse("View 1")


def viewshka2(request):
    return HttpResponse("View 2")


def viewshka3(request):
    return HttpResponse("View 3")
