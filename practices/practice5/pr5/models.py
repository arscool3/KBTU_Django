from django.db import models

class Person(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + self.lname

    class Meta:
        abstract = True

class Lesson(models.Model):
    title = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)

    def __str__(self):
        return title

class Faculty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return name

class StudentQuerySet(models.QuerySet):
    def freshmen(self):
        return self.filter(year=1)
    def sophomores(self):
        return self.filter(year=2)
    def juniors(self):
        return self.filter(year=3)
    def seniors(self):
        return self.filter(year=4)

class StudentManager(models.Manager):
    def get_queryset(self):
        return StudentQuerySet(self.model, using=self._db)
    def freshmen(self):
        return self.get_queryset().freshmen()
    def sophomores(self):
        return self.get_queryset().sophomores()
    def juniors(self):
        return self.get_queryset().juniors()
    def seniors(self):
        return self.get_queryset().seniors()

class TeacherQuerySet(models.QuerySet):
    def filter_by_faculty(self,faculty):
        return self.filter(faculty=faculty)
    def high_ranking(self):
        return self.filter(salary__gte=1000000)

class TeacherManager(models.Manager):
    def get_queryset(self):
        return TeacherQuerySet(self.model, using=self._db)
    def filter_by_faculty(self,faculty):
        return self.get_queryset().filter_by_faculty(faculty)
    def high_ranking(self):
        return self.get_queryset().high_ranking()

class Student(Person):
    year = models.IntegerField()
    faculty = models.ForeignKey('Faculty',on_delete=models.CASCADE)
    lessons = models.ManyToManyField('Lesson')
    objects = StudentManager()

class Teacher(Person):
    salary = models.IntegerField()
    faculty = models.ForeignKey('Faculty',on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson',on_delete=models.CASCADE)
    objects = TeacherManager()