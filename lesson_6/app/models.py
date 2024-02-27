from datetime import date

from django.db import models



class User(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Teacher(User):
    years_of_experience = models.IntegerField()


class LessonQuerySet(models.QuerySet):
    def get_today_lessons_by_teacher(self, name: str):
        return self.filter(teacher__name=name, date=date.today())

class Lesson(models.Model):
    title = models.CharField(max_length=10)
    date = models.DateField()
    duration = models.IntegerField()
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    students = models.ManyToManyField('Student', related_name='lessons')
    objects = LessonQuerySet.as_manager()

    def __str__(self):
        return f"{self.title} {self.teacher.name}"


class StudentQuerySet(models.QuerySet):
    def get_only_arslan(self):
        return self.filter(name='Arslan')

    def get_students_only_from_course_3(self):
        return self.filter(course='3')

class Student(User):
    course = models.CharField(max_length=30)
    objects = StudentQuerySet.as_manager()


# Student <-> Lesson Many to Many
# Teacher <-> Lesson One to Many

# python3 manage.py makemigrations
# python3 manage.py migrate

# python3 manage.py createsuperuser\