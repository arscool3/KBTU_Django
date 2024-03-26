from django.db import models
from django.contrib.auth.models import AbstractUser

class Entity(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class Org(Entity):
    descr = models.CharField(max_length=255)

class Quiz(Entity):
    pass

class Question(Entity):
    quiz = models.ForeignKey('Quiz',on_delete=models.CASCADE)
    correct = models.IntegerField()
    answer0 = models.CharField(max_length=50)
    answer1 = models.CharField(max_length=50)
    answer2 = models.CharField(max_length=50)
    answer3 = models.CharField(max_length=50)

class Cert(Entity):
    descr = models.CharField(max_length=255)

class Course(Entity):
    cert = models.OneToOneField('Cert',on_delete=models.CASCADE)
    descr = models.CharField(max_length=255)

class Lesson(Entity):
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    quiz = models.OneToOneField('Quiz',on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)

class User(AbstractUser):
    org = models.ForeignKey('Org',on_delete=models.CASCADE, null=True)
    certs = models.ManyToManyField('Cert')
    passedq = models.ManyToManyField('Quiz')
