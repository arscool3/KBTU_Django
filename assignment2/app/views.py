from django.shortcuts import render
value = 5

def view(request):
    global value
    value **= 3
    return render(request, 'index.html', {'value': value})