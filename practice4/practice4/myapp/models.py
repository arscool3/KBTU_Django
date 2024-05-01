from django.db import models


class UserBase(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

class TeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('exp')
    



class Teacher(UserBase):
    exp = models.IntegerField()
    

    def __str__(self):
        return self.name
    
    objects = TeacherManager()



class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Student(UserBase):
    grade = models.CharField(max_length=2)
    courses = models.ManyToManyField('Course')
    def __str__(self):
        return self.name








    