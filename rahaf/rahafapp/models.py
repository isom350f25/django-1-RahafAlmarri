from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Class(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    students = models.ManyToManyField(User, related_name='classes')

    def __str__(self):
        return self.name