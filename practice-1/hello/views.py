from django.http import HttpResponse


def index(request):
    return HttpResponse('This is the main view')

def basic(request):
    return HttpResponse('This is the basic view')

def test(request):
    return HttpResponse('This is the test view')