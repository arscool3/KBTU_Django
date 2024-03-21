from django.http import HttpResponse


def main(request):
    return HttpResponse('This is the Main View')

def basic(request):
    return HttpResponse('This is the Basic View')

def test_view(request):
    return HttpResponse('Test View')