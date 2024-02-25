from django.http import HttpResponse


def index(request):
    return HttpResponse('LOL KEk ')

def other(request):
    return HttpResponse('Today Django Day')