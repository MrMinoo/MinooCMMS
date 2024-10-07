from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=45, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.name
