from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.CharField(max_length=120)
    name=models.CharField(max_length=150)
    course=models.CharField(max_length=120)
    address=models.CharField(max_length=300)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=120)
    def __str__(self):
        return self.name