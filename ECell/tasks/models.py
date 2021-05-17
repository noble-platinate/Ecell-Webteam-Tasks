from django.db import models

# Create your models here.

class todolist(models.Model):
    task_info=models.CharField(max_length=100)
    status=models.BooleanField()
    task_number=models.IntegerField()
