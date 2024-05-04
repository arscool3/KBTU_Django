from django.db import models

class StipendiaStudentManager(models.Manager):
    def get_students_by_stipendia(self):
        return self.filter(has_stipendia=True)
    
    def get_students_by_nonstipendia(self):
        return self.filter(has_stipendia=False)

class FacultyManager(models.Manager):
    def get_students_of_fit(self, faculty):
        return self.filter(faculty=faculty)
        
    def get_students_of_bs(self, faculty):
        return self.filter(faculty=faculty)


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    has_stipendia = models.BooleanField(default=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    objects = models.Manager()

    stipendiaManager = StipendiaStudentManager()  
    facultyManager = FacultyManager()

    def __str__(self):
        return self.name