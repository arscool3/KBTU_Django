from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
stud_list = [
    "Arman Armanov",
    "Serik Alpysbaev",
    "Dana Kerimbaykyzy",
    "Anton Vladislavov",
]
def index(request):
    return render(request, "index.html", {"stud_list": stud_list})