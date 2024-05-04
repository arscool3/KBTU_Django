from django.db import models

# Create your models here.
# WRITE DJANGO APPLICATION
# AT LEAST YOU NEED TO DEVELOP
# 2 Django Managers with 2 method each
# 4 Django Models with 2-3 relationship
# VIEWS for GET this objects
# AND Django form for creating this instances
class Base(models.Model):
    name = models.CharField(max_length=20, default="")
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class UniversityManager(models.QuerySet):
    def get_univs(self):
        return self.all()

    def get_budget(self):
        return self.order_by('budget')
    
    def get_lang(self):
        return self.filter(language='English')

class University(Base):
    numberOfStudents = models.IntegerField()
    budget = models.FloatField()
    language = models.CharField(max_length=30)
    objects = UniversityManager().as_manager()

class studentManager(models.QuerySet):
    def get_dorms(self):
        return self.filter(needs_dorm='True')
    def get_gpa(self):
        return self.order_by('gpa')
    
class Student(Base):
    age = models.IntegerField()
    needs_dorm = models.BooleanField(default = False)
    gpa = models.FloatField()
    course_year = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    objects = studentManager().as_manager()

class Teacher(Base):
    age = models.IntegerField()
    salary = models.FloatField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class Course(Base):
    credits = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, related_name="lessons")
    students = models.ManyToManyField("Student",related_name="lessons")