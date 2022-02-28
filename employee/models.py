from pyexpat import model
from django.db import models
from workspace.models import Workspace
# Create your models here.

class Employee(models.Model):

    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    salary = models.IntegerField()
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name