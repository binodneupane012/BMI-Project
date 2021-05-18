from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Suggestion(models.Model):
    BMI = (
        ("overweight","OVERWEIGHT"),
        ("obsessed","OBSESSED"),
        ("undeweight","UNDERWEIGHT"),
        ("normalweight","NORMALWEIGHT")
    )
    suggestion = models.CharField(max_length=255, choices=BMI)
    message = models.TextField()

    def __str__(self):
        return self.suggestion


class BMIMeasurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def bmi(self):
        return self.weight/self.height**2
