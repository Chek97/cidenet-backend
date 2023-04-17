from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    other_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=50)
    job_country = models.CharField(max_length=100)
    email = models.EmailField()