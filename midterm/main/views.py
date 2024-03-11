from django.shortcuts import render

#GET emdpoints

from rest_framework import generics
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer, ContactInfoSerializer


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseStudentsView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Student.objects.filter(courses__id=course_id)

class ContactInfoView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = ContactInfoSerializer

    def get_object(self):
        return self.queryset.get(id=self.kwargs['student_id']).contactinfo


# POST endpoints
    
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Course, Guardian, School
from .serializers import StudentSerializer, CourseSerializer, ContactInfoSerializer, GuardianSerializer,SchoolSerializer

class CreateStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateCourseView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CreateContactInfoView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = ContactInfoSerializer

class CreateGuardianView(generics.CreateAPIView):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer

class CreateSchoolView(generics.CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
