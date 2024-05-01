from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Teacher(Person):
    pass


class LessonManager(models.QuerySet):
    def get_pp1(self):
        return self.filter(name='pp1')

    def get_lessons_by_teacher(self, name: str):
        return self.filter(teacher__name=name)


class Lesson(models.Model):
    objects = LessonManager.as_manager()
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class StudentManager(models.QuerySet):
    def get_by_lessons(self, lesson: str):
        return self.filter(lessons__name=lesson)

    def get_by_name(self, name: str):
        return self.filter(name=name)


class Student(Person):
    lessons = models.ManyToManyField(Lesson)
    objects = StudentManager.as_manager()
