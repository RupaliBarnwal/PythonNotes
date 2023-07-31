from django.db import models

# Create your models here.
class UserAdd(models.Model):
    email = model.EmailField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=30)