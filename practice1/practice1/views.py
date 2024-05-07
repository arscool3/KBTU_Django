from django.http import HttpResponse


def first_view(request):
    return HttpResponse("1 view")


def second_view(request):
    return HttpResponse("2 view")


def third_view(request):
    return HttpResponse("3 view")
