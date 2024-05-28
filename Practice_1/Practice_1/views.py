from django.http import HttpResponse

def Home_view(request):
    return HttpResponse("Welcome to Home view!")


def About_view(request):
    return HttpResponse("Welcome to About view!")


def Profile_view(request):
    return HttpResponse("Welcome to Profile view!")