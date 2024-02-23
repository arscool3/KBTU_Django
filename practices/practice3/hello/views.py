from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

class Student:
    def __init__(self,id_,fname,lname):
        self.id = id_
        self.fname = fname
        self.lname = lname

def test(request):
    students = [Student(0,'dUke','nUkEM'),Student(1,'JC','DentOn'),Student(2,'GoRdOn','fReEmAn')]
    template = loader.get_template("test.html")
    return HttpResponse(template.render({'students':students},request))