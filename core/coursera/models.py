from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='instructor_profile_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    prerequisite = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    instructor = models.OneToOneField(Instructor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.name


class EnrollmentQuerySet(models.QuerySet):
    def get_enrollments_of_student(self, student_id: int):
        return self.filter(student_id=student_id)

    def get_enrollments_of_course(self, course_id: int):
        return self.filter(course_id=course_id)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    objects = EnrollmentQuerySet.as_manager()

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ReviewQuerySet(models.QuerySet):
    def get_reviews(self, course_id: int):
        return self.filter(course_id=course_id)


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    rating = models.IntegerField(choices=RATING_CHOICES)
    text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    objects = ReviewQuerySet.as_manager()

    def __str__(self):
        return f"{self.student.name}'s review on {self.course.title}"
