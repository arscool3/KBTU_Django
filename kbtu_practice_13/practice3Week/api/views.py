from datetime import datetime

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def sayHello(request, name):
    return Response("Hello " + name);

@api_view(['GET'])
def getTime(request):
    return Response(datetime.now().date())

@api_view(['GET'])
def view1(request):
    return Response("main view");

@api_view(['GET'])
def view2(request):
    return Response("basic view");

@api_view(['GET'])
def view3(request):
    return Response("last view");