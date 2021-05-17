from django.db import models

# Create your models here.

class user_data(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
