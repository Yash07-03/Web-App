from django.db import models

# Create your models here.
class stud(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Course = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)


