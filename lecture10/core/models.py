from django.db import models

class WeatherData(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.recorded_at}"

