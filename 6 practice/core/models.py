from django.db import models
from django.contrib.auth.models import AbstractUser
from core.enums import Role
# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = [(role.value, role.name) for role in Role]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES) 

class Instructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='instructor_profile')
    class Meta:
        permissions = [
            ('can_add_courses', 'Can add course'),
        ]
    
    def __str__(self) -> str:
        return self.user.username

class CourseManager(models.Manager):
    def get_course_by_instructor(self, instructor):
        return self.filter(instructor=instructor)

class Course(models.Model):
    name = models.CharField(max_length = 100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    objects = CourseManager()

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='student_profile')
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.user.username

class AssignmentManager(models.Manager):
    def get_by_course(self, course):
        return self.filter(course=course)
    
    def get_sorted_by_date(self):
        return self.get_queryset().order_by('due_date')

    def get_course_by_completeness(self, done):
        return self.filter(done=done)

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    done = models.BooleanField()
    objects = AssignmentManager()

    def __str__(self) -> str:
        return self.title + f"({self.course})"


class GradeManager(models.Manager):
    def get_grade_by_student(self, student):
        return self.filter(student=student)
    
    def get_grade_by_course(self, course):
        assigments = Assignment.objects.filter(course=course)
        return self.filter(assigment__in=assigments)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=5)
    objects = GradeManager()

class AnnouncementsManager(models.Manager):
    def get_sorted_by_date(self):
        return self.get_queryset().order_by('date_posted')

    def get_announcement_by_course(self, course):
        return self.filter(course=course)

class Announcements(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField()
    objects = AnnouncementsManager()

    def __str__(self) -> str:
        return self.title
