from django.db import models

class AirplaneManager(models.Manager):
    def get_active_airplanes(self):
        return self.filter(active=True)

    def get_inactive_airplanes(self):
        return self.filter(active=False)

class Airplane(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    objects = AirplaneManager()

    def __str__(self):
        return self.name

class ConsumerManager(models.Manager):
    def get_by_phone_number(self, phone_number):
        return self.filter(phone__contains=phone_number)

    def get_by_email(self, email):
        return self.filter(email__contains=email)

class Consumer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    objects = ConsumerManager()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    seat_number = models.CharField(max_length=10)
    departure_date = models.DateField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket {self.id} - {self.airplane.name} - {self.consumer.name}"