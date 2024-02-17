from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

month_text = {
    'january' : '1',
    'february' : '2',
    'march' : '3',
    'april' : '4',
    'may' : '5',
    'june' : '6',
    'july' : '7',
    'august' : '8',
    'september' : '9',
    'october' : '10',
    'november' : '11',
    'december' : '12',
}

def monthly_challenges_by_number(request, month):
    months = list(month_text.keys())
    redirect_month = months[int(month) - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/ jan
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        text = month_text[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("ERROR!!")



    return HttpResponse(text)