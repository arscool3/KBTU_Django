from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Home view")


def about_view(request):
    return HttpResponse("About view")


def settings_view(request):
    return HttpResponse("Settings view")