from django.shortcuts import render

def my_view(request):
    context = {
        'my_list': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    }
    return render(request, 'index.html', context)