from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
    
        return self.name

class Student(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):

        return self.name

class ContactInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Contact info for {self.student.name}"

class Guardian(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - Guardian of {self.student.name}"