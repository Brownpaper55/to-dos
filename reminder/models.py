from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

 #Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique= True)
    email = models.EmailField(unique= True)
    password = models.CharField(max_length=15, unique=True)

class Task(models.Model):
    Title = models.CharField(max_length= 20, blank = True)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    Task_body = models.TextField(max_length = 600)
    time = models.DateTimeField()
    Done = models.BooleanField(default = False)
   
    def __str__(self):
        return self.Title