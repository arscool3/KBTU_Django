from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TestForm
from .models import Member

def test(request):
    if request.method=="POST":
        form = TestForm(request.POST)
        if form.is_valid():
            m = Member(fname=form.cleaned_data["fname"],lname=form.cleaned_data["lname"],age=form.cleaned_data["age"])
            m.save()
            #print(m)
            return HttpResponseRedirect("../")
    else:
        form = TestForm()
    return render(request,"form.html",{"form":form})

def people(request):
    people = list(Member.objects.all().values())
    return render(request,"index.html",{"people":people})

def dudes(request, fn):
    dudes = list(Member.objects.filter(fname=fn))
    if len(dudes) == 0:
        return render(request,"dude_not_found.html")
    elif len(dudes) == 1:
        return render(request,"dude.html",{"dude":dudes[0]})
    else:
        return render(request,"dudes.html",{"dudes":dudes})