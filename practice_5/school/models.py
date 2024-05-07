from django.db import models
from datetime import datetime, timedelta


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        abstract = True



class StudentQuerySet(models.QuerySet):
    def enrolled_in_course(self, course_id):
        return self.filter(enrollment__course_id=course_id)

    def enrolled_since(self, date):
        return self.filter(enrollment__date_joined__gte=date)


class Student(Person):
    enrollment_date = models.DateField()
    objects = StudentQuerySet.as_manager()


class Teacher(Person):
    hire_date = models.DateField()


class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Enrollment')

    class CourseQuerySet(models.QuerySet):
        def with_teacher(self, teacher_name):
            return self.filter(teacher__last_name=teacher_name)

        def without_students(self):
            return self.annotate(num_students=models.Count('students')).filter(num_students=0)

    objects = CourseQuerySet.as_manager()


class CourseQuerySet(models.QuerySet):
    def with_teacher(self, teacher_name):
        return self.filter(teacher__last_name=teacher_name)

    def without_students(self):
        return self.annotate(num_students=models.Count('students')).filter(num_students=0)

    def recent_courses(self):
        return self.filter(start_date__gte=datetime.now() - timedelta(days=30))

    def old_courses(self):
        return self.filter(start_date__lte=datetime.now() - timedelta(days=365))

    def active_courses(self):
        return self.filter(is_active=True)

    def full_courses(self, limit):
        return self.annotate(num_students=models.Count('students')).filter(num_students__gte=limit)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_joined = models.DateField()

    class Meta:
        unique_together = ('student', 'course')
