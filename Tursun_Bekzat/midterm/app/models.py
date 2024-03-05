from django.db import models


class Base(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Faculty(Base):
    relevant = models.BooleanField(default=True)


class Speciality(Base):
    code = models.CharField(max_length=10)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Discipline(Base):
    credits = models.IntegerField()
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, default=1)


class Student(Base):
    id = models.CharField(max_length=9, primary_key=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    speciality = models.ForeignKey(Speciality, on_delete=models.PROTECT)
    disciplines = models.ManyToManyField(Discipline, blank=True)
    login = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disciplines = self.disciplines.none()


class Professor(Base):
    surname = models.CharField(max_length=30)
    disciplines = models.ManyToManyField(Discipline)
    login = models.CharField(max_length=150)
    password = models.CharField(max_length=128)


class Schedule(models.Model):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    DAY_CHOICES = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]

    time_slot = models.CharField(max_length=50)
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    discipline = models.CharField(max_length=100)


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title