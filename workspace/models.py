from turtle import update
from django.db import models

# Create your models here.
class Workspace(models.Model):

    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return  self.name