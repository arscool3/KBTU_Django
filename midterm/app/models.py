from django.db import models


class FitnessUser(models.Model):
    username = models.CharField(max_length=32)
    fullname = models.CharField(max_length=64)

    objects = models.Manager()

    def __str__(self):
        return self.username


class ActivityManager(models.Manager):
    def count_calories_per_day(self, user, date):
        all_per_day = self.filter(end_datetime__date=date).filter(user=user).all()
        all_calories = 0
        for activity in all_per_day:
            all_calories += activity.burnt_calories
        return all_calories


class Activity(models.Model):
    activity_name = models.CharField(max_length=32)
    burnt_calories = models.IntegerField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    user = models.ForeignKey(FitnessUser, on_delete=models.CASCADE)

    objects = ActivityManager()

    def __str__(self):
        return str(self.user.__str__()) + "'s " + str(self.activity_name)


class DietManager(models.Manager):
    def count_calories_per_day(self, user, date):
        all_per_day = self.filter(registered_datetime__date=date).filter(user=user).all()
        all_calories = 0
        for diet in all_per_day:
            all_calories += diet.calorie_content
        return all_calories


class Diet(models.Model):
    food_name = models.CharField(max_length=32)
    calorie_content = models.IntegerField()
    registered_datetime = models.DateTimeField()
    user = models.ForeignKey(FitnessUser, on_delete=models.CASCADE)

    objects = DietManager()

    def __str__(self):
        return str(self.user.__str__()) + "'s " + str(self.food_name)


class HealthMetrics(models.Model):
    BLOOD_TYPES_CHOICES = {
        "A+": "A positive",
        "A-": "A negative",
        "B+": "B positive",
        "B-": "B negative",
        "AB+": "AB positive",
        "AB-": "AB negative",
        "O+": "O positive",
        "O-": "O negative",
    }
    SEXES_CHOICES = {
        "M": "male",
        "F": "female",
    }
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=1, choices=SEXES_CHOICES, blank=True)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES_CHOICES, blank=True)
    user = models.OneToOneField(FitnessUser, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return str(self.user.__str__()) + "'s health metrics"


class Goal(models.Model):
    steps = models.IntegerField(null=True)
    burnt_calories = models.IntegerField(null=True)
    eaten_calories = models.IntegerField(null=True)
    sleep_time = models.IntegerField(null=True)
    user = models.OneToOneField(FitnessUser, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return str(self.user.__str__()) + "'s goals"


class ProgressManager(models.Manager):
    def update_calories(self, user, date):
        current_user_progress, created = CurrentProgress.objects.filter(user=user).get_or_create(date=date)
        print(current_user_progress)
        current_user_progress.eaten_calories = Diet.objects.count_calories_per_day(user, date)
        current_user_progress.burnt_calories = Activity.objects.count_calories_per_day(user, date)
        current_user_progress.save()

class CurrentProgress(models.Model):
    steps = models.IntegerField(null=True)
    burnt_calories = models.IntegerField(null=True)
    eaten_calories = models.IntegerField(null=True)
    sleep_time = models.IntegerField(null=True)
    date = models.DateField(unique=True)
    user = models.ForeignKey(FitnessUser, on_delete=models.CASCADE)

    objects = ProgressManager()

    def __str__(self):
        return str(self.user.__str__()) + "'s current progress"
