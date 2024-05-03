from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import *
from .serializers import *
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from midterm.settings import LOGIN_REDIRECT_URL, LOGIN_URL

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

User = get_user_model()

@api_view(['GET'])
def index(request):
    return render(request, "index.html", {'user':request.user.username})

@api_view(['GET'])
@login_required(login_url=LOGIN_URL)
def profile(request):
    certs = [val for val in Cert.objects.all() if val in request.user.certs.all()]
    return render(request, "profile.html", {'user':request.user,'certs':certs})

#@permission_required('core.add_course', login_url=LOGIN_URL)
class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'

    @action(detail=True, methods=["get"],url_path='courses', url_name='courses')
    def getcourse(self, request, id: int):
        c = Course.objects.get(id=id)
        lessons = Lesson.objects.filter(course=c)
        return render(request, "course.html", {'user':request.user,'course':c,'lessons':lessons})

    @action(detail=True, methods=["get"],url_path='course', url_name='course')
    def getcourses(self, request):
        cs = Course.objects.all()
        return render(request, "courses.html", {'user':request.user,'cs':cs})

    @action(detail=True, methods=["get","post"],url_path='course/new', url_name='course/new')
    def newcourse(self, request):
        if request.method == "POST":
            title = request.POST["title"]
            descr = request.POST["descr"]
            cert_title= request.POST["cert_title"]
            cert_descr = request.POST["cert_descr"]
            newce = Cert(title=cert_title,descr=cert_descr)
            try:
                newce.save()
            except:
                return Response({"message" : "Something went wrong."})
            newco = Course(title=title,descr=descr,cert=newce)
            try:
                newco.save()
                return redirect('/courses/')
            except:
                return Response({"message" : "Something went wrong."})
        else:
            form = CourseForm()
            return render(request, 'form.html', {'form':form,'entity':'New Course'})

"""@api_view(['GET'])
@login_required(login_url=LOGIN_URL)
def courses(request):
    cs = Course.objects.all()
    return render(request, "courses.html", {'user':request.user,'cs':cs})

@api_view(['GET'])
@login_required(login_url=LOGIN_URL)
def course(request, id):
    c = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course=c)
    return render(request, "course.html", {'user':request.user,'course':c,'lessons':lessons})

@api_view(['GET','POST'])
@permission_required('core.add_course', login_url=LOGIN_URL)
def newcourse(request):
    if request.method == "POST":
        title = request.POST["title"]
        descr = request.POST["descr"]
        cert_title= request.POST["cert_title"]
        cert_descr = request.POST["cert_descr"]
        newce = Cert(title=cert_title,descr=cert_descr)
        try:
            newce.save()
        except:
            return Response({"message" : "Something went wrong."})
        newco = Course(title=title,descr=descr,cert=newce)
        try:
            newco.save()
            return redirect('/courses/')
        except:
            return Response({"message" : "Something went wrong."})
    else:
        form = CourseForm()
        return render(request, 'form.html', {'form':form,'entity':'New Course'})"""

@api_view(['GET'])
@login_required(login_url=LOGIN_URL)
def lesson(request,id):
    l = Lesson.objects.get(id=id)
    q = l.quiz
    questions = Question.objects.filter(quiz=q.id)
    return render(request, "lesson.html", {'user':request.user,'lesson':l,'quiz':q,'questions':questions})

@api_view(['GET','POST'])
@permission_required('core.add_lesson', login_url=LOGIN_URL)
def newlesson(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        c= request.POST["course"]
        course = Course.objects.get(id=c)
        quiz_title = request.POST["quiz_title"]
        newq = Quiz(title=quiz_title)
        try:
            newq.save()
        except:
            return Response({"message" : "Something went wrong."})
        newl = Lesson(title=title,text=text,course=course,quiz=newq)
        try:
            newl.save()
            return redirect('/courses/'+str(c))
        except:
            return Response({"message" : "Something went wrong."})
    else:
        form = LessonForm()
        return render(request, 'form.html', {'form':form,'entity':'New Lesson'})

@api_view(['GET','POST'])
@permission_required('core.add_question', login_url=LOGIN_URL)
def newquestion(request,id):
    q = Quiz.objects.get(id=id)
    if request.method == "POST":
        title = request.POST["title"]
        answer0 = request.POST["answer0"]
        answer1 = request.POST["answer1"]
        answer2 = request.POST["answer2"]
        answer3 = request.POST["answer3"]
        correct = request.POST["correct"]
        newq = Question(title=title,answer0=answer0,answer1=answer1,answer2=answer2,answer3=answer3,correct=correct,quiz=q)
        try:
            newq.save()
            return redirect('/')
        except:
            return Response({"message" : "Something went wrong."})
    else:
        form = QuestionForm()
        return render(request, 'form.html', {'form':form,'entity':'New Question for the "' + q.title + '" quiz:'})

@api_view(['GET','POST'])
@login_required(login_url=LOGIN_URL)
def answer(request,id):
    if request.method == "POST":
        q = Quiz.objects.get(id=id)
        request.user.passedq.add(q)
        l = Lesson.objects.get(quiz=id)
        ls = Lesson.objects.filter(course=l.course)
        getCert = True
        for a in ls:
            b = Quiz.objects.get(id=a.quiz.id)
            if b not in request.user.passedq.all():
                getCert = False
                break
        if getCert:
            c = Course.objects.get(id=l.course.id)
            ce = c.cert
            request.user.certs.add(ce)
    return redirect('/')

@api_view(['GET','POST'])
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({"message" : "Something went wrong."})
        login(request, user)
        return redirect(LOGIN_REDIRECT_URL)
    else:
        form = LoginForm()
        return render(request, 'form.html', {'form':form,'entity':'Log in'})

@api_view(['GET'])
@login_required(login_url=LOGIN_URL)     
def signout(request):
    logout(request)
    return redirect('/')
            
@api_view(['GET','POST'])
def signup(request):
    if request.method=="POST":
        org = request.POST['org']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
            org = Org.objects.get(id=org),
            first_name=first_name, 
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        try:
            newuser.save()
            newuser.user_permissions.remove(Permission.objects.get(name='Can add log entry'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change log entry'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete log entry'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can view log entry'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can add group'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change group'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete group'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can add permission'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change permission'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete permission'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can add content type'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change content type'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete content type'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can view content type'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can add cert'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change cert'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete cert'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can add course'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change course'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete course'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can add lesson'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change lesson'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete lesson'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can add quiz'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change quiz'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete quiz'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can add question'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change question'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete question'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete user'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can add org'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can change org'))
            newuser.user_permissions.remove(Permission.objects.get(name='Can delete org'))
            newuser.save()
            return redirect('/')
        except:
            return Response({"message" : "Something went wrong."})
    else:
        form = UserForm()
        return render(request, 'form.html', {'form':form,'entity':'Sign up'})

@api_view(['GET'])
@login_required(login_url=LOGIN_URL)
def org(request,id):
    o = Org.objects.get(id=id)
    users = User.objects.filter(org=o)
    return render(request, "org.html", {'user':request.user,'organization':o,'users':users})

@api_view(['GET','POST'])
@permission_required('core.add_org', login_url=LOGIN_URL)
def neworg(request):
    if request.method=="POST":
        title = request.POST['title']
        descr = request.POST['descr']
        neworg = Org(title=title,descr=descr)
        try:
            neworg.save()
            return redirect('/')
        except:
            return Response({"message" : "Something went wrong."})
    else:
        form = OrgForm()
        return render(request, 'form.html', {'form':form,'entity':'New Organization'})