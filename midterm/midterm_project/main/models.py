from django.db import models

class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    instructor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.instructor_name

    class Meta:
        db_table = 'instructor'
        verbose_name = 'instructor'

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    membership_type = models.CharField(max_length=50)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'member'

class Gym(models.Model):
    gym_id = models.AutoField(primary_key=True)
    gym_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    instructor = models.OneToOneField(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.gym_name

    class Meta:
        db_table = 'gym'

class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='memberships')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'membership'

class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='equipment')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'equipment'

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='workouts')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'workout'
