# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False,)
    is_teacher = models.BooleanField('teacher status', default=False,)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    Mobile = models.CharField(max_length=15)
    Address = models.CharField(max_length=500)

    def __str__(self):
        return self.Mobile





#course details:
class Course(models.Model):
    user = models.ForeignKey(Profile, unique=True,on_delete=models.CASCADE,primary_key=True)
    Institute_Name = models.CharField(max_length=100)
    Faculty_Name = models.CharField(max_length=100)
    New_Batche = models.DateField()
    Duration = models.CharField(max_length=100)
    Class_Timings = models.TimeField()
    Free_Demo_Video = models.URLField(validators=[URLValidator()])

    def __str__(self):
        return self.Institute_Name

# if student attend demo register form

class DemoStudents(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Mobile_Number = models.CharField(max_length=12)
    Course = models.CharField(max_length=12)
    Location = models.CharField(max_length=12)


