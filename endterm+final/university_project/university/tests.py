from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Department, Course, Student, Professor
from .tasks import update_course_description

class DepartmentViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name="Computer Science")
        self.course = Course.objects.create(title="Algorithms", department=self.department)
        self.student = Student.objects.create(name="John Doe")

    def test_get_courses(self):
        url = reverse('department-courses', kwargs={'pk': self.department.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Algorithms")

class CourseViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name="Computer Science")
        self.course = Course.objects.create(title="Algorithms", department=self.department)
        self.student = Student.objects.create(name="John Doe")

    def test_enroll_student(self):
        url = reverse('course-enroll-student', kwargs={'pk': self.course.pk})
        response = self.client.post(url, {'student_id': self.student.pk}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Student enrolled successfully')
        self.assertTrue(self.course.students.filter(pk=self.student.pk).exists())

class StudentViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = Student.objects.create(name="John Doe")
        self.department = Department.objects.create(name="Computer Science")
        self.course = Course.objects.create(title="Algorithms", department=self.department)
        self.course.students.add(self.student)

    def test_enrolled_courses(self):
        url = reverse('student-enrolled-courses', kwargs={'pk': self.student.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Algorithms")

class ProfessorViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.professor = Professor.objects.create(name="Dr. Smith")
        self.department = Department.objects.create(name="Computer Science")
        self.course = Course.objects.create(title="Algorithms", professor=self.professor, department=self.department)

    def test_courses_taught(self):
        url = reverse('professor-courses-taught', kwargs={'pk': self.professor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Algorithms")

class CeleryTasksTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title="Algorithms", description="Old description")

    def test_update_course_description(self):
        new_description = "New description"
        update_course_description(self.course.pk, new_description)
        self.course.refresh_from_db()
        self.assertEqual(self.course.description, new_description)

