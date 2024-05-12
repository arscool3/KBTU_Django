

# Create your views here.
from django.http import HttpResponse


def main(request):
    return HttpResponse("This is main view")

def basic(request):
    return HttpResponse("This is basic view")

def test(request):
    return HttpResponse("This is test view")