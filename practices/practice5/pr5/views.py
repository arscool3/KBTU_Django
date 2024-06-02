from django.shortcuts import render

from .models import *

def index(request):
    return render(request,"index.html")

def teacher(request):
    if request.method == "GET":
        ts = Teacher.objects.all()
        return render(request,"entity.html",{"type":"teacher","liste":ts})
    elif request.method == "POST":
        r = request.POST
        fname = r["fname"]
        lname = r["lname"]
        age = r["age"]
        salary = r["salary"]
        lesson = r["lesson"]
        faculty = r["faculty"]
        t = Teacher(fname=fname,lname=lname,age=age,salary=salary,lesson=lesson,faculty=faculty)
        t.save()

def student(request):
    if request.method == "GET":
        ss = Student.objects.all()
        return render(request,"entity.html",{"type":"student","liste":ss})
    elif request.method == "POST":
        r = request.POST
        fname = r["fname"]
        lname = r["lname"]
        age = r["age"]
        year = r["year"]
        faculty = r["faculty"]
        lesson = r["lesson"]
        s = Student(fname=fname,lname=lname,age=age,year=year,faculty=faculty)
        s.save()
        s.lessons.add(Lesson.objects.get(title=lesson))
        s.save()

def faculty(request):
    if request.method == "GET":
        fs = Faculty.objects.all()
        return render(request,"entity.html",{"type":"faculty","liste":fs})
    elif request.method == "POST":
        r = request.POST
        name = r["name"]
        f = Faculty(name=name)
        f.save()

def lesson(request):
    if request.method == "GET":
        ls = Lesson.objects.all()
        return render(request,"entity.html",{"type":"lesson","liste":ls})
    elif request.method == "POST":
        r = request.POST
        title = r["title"]
        semester = r["semester"]
        l = Lesson(title=title,semester=semester)
        l.save()