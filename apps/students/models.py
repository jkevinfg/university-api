from django.db import models
from apps.degrees.models import Degree


# Create your models here.
class Student(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    last_name_f = models.CharField(max_length=35)
    last_name_m = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    date_of_birth = models.DateField()
    genders = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    gender = models.CharField(max_length=1, choices=genders, default='F')
    degree = models.ForeignKey(Degree, null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def full_name(self):
        return f"{self.name} {self.last_name_m} {self.last_name_f}"
