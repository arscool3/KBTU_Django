from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .tasks import update_course_description
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import CustomUserSerializer


# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    # Custom action to get courses offered by a department
    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        department = self.get_object()
        courses = Course.objects.filter(department=department)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    # Custom action to enroll a student in a course
    @action(detail=True, methods=['post'])
    def enroll_student(self, request, pk=None):
        course = self.get_object()
        student_id = request.data.get('student_id')
        student = Student.objects.get(id=student_id)
        course.students.add(student)
        return Response({'message': 'Student enrolled successfully'})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    # Custom action to get courses enrolled by a student
    @action(detail=True, methods=['get'])
    def enrolled_courses(self, request, pk=None):
        student = self.get_object()
        courses = student.courses.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]

    # Custom action to get courses taught by a professor
    @action(detail=True, methods=['get'])
    def courses_taught(self, request, pk=None):
        professor = self.get_object()
        courses = Course.objects.filter(professor=professor)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


def update_course(request, course_id):
    if request.method == 'POST':
        new_description = request.POST.get('new_description', '')
        update_course_description.send(course_id, new_description)
        return render(request, 'success_template.html', {'message': 'Description update task has been scheduled.'})
    else:
        return render(request, 'update_course_template.html')


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]


# CustomUser = get_user_model()


# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = CustomUserSerializer


# class ObtainTokenPairView(generics.GenericAPIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         try:
#             user = CustomUser.objects.get(username=username)
#             if user.check_password(password):
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                 })
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
#         except CustomUser.DoesNotExist:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
