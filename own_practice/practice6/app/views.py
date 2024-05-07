from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Course, Lesson, Enrollment, Instructor, Quiz
from .serializers import CourseSerializer, LessonSerializer
from django.shortcuts import get_object_or_404


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instructor = Instructor.objects.get(user=self.request.user)
        serializer.save(instructor=instructor)


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class EnrollmentFormAPIView(generics.CreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        serializer.save(user=self.request.user, course=course)


class CreateLessonAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        serializer.save(course=course)


class TakeQuizAPIView(generics.RetrieveUpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]