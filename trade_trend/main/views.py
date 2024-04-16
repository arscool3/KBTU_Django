from django.shortcuts import render


def get_index(request):
    return render(request, "index.html")