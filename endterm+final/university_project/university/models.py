from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import *
from django.conf import settings


# class CustomUser(AbstractUser):
#     USER_TYPES = (
#         ('student', 'Student'),
#         ('professor', 'Professor'),
#     )
#     user_type = models.CharField(max_length=10, choices=USER_TYPES)


class Department(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название')
    code = models.CharField(
        max_length=20,
        verbose_name='Код')
    dean = models.OneToOneField('Professor', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='department_as_dean')
    image = models.ImageField(
        upload_to='department_images/',
        blank=True,
        null=True,
        validators=[validate_size, validate_extension]
    )

    def __str__(self):
        return self.name


class Professor(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя')
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='professors')
    email = models.EmailField(
        verbose_name='Email',
        null=True,
        blank=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    image = models.ImageField(
        upload_to='professor_images/',
        blank=True,
        null=True,
        validators=[validate_size, validate_extension]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название')
    code = models.CharField(
        max_length=20,
        verbose_name='Код')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    credits = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Кредиты')
    prerequisite_courses = models.ManyToManyField('self', symmetrical=False, related_name='courses_required',
                                                  blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return self.name


class Student(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя')
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия')
    courses = models.ManyToManyField(Course, related_name='students')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name='Адрес', null=True, blank=True)
    image = models.ImageField(
        upload_to='student_images/',
        blank=True,
        null=True,
        validators=[validate_size, validate_extension]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Schedule(models.Model):
    DAY_CHOICES = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    )
    day_of_week = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
        verbose_name='День недели')
    start_time = models.TimeField(verbose_name='Время начала')
    end_time = models.TimeField(verbose_name='Время окончания')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='schedules')

    def __str__(self):
        return f"{self.course} - {self.day_of_week} {self.start_time}-{self.end_time}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.FloatField(verbose_name='Оценка')
    semester = models.CharField(max_length=20, verbose_name='Семестр')
    academic_year = models.CharField(max_length=10, verbose_name='Учебный год')

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"
