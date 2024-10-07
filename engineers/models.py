from django.db import models
from departments.models import Department

class Engineer(models.Model):
    full_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45, primary_key=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    departments = models.ManyToManyField(Department, through='EngineerDepartment')

    def __str__(self):
        return self.full_name

class EngineerDepartment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
