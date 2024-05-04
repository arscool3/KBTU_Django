from django.db import models

class Test(models.Model):
    test = models.CharField(max_length=255)

    def __str__(self):
        return self.test
