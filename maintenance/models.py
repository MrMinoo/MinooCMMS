from django.db import models
from equipments.models import Equipment
from engineers.models import Engineer

class PeriodicService(models.Model):
    description = models.CharField(max_length=45, null=True, blank=True)
    service_date = models.DateField(null=True, blank=True, default=models.DateField())
    next_date = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=50, decimal_places=0, null=True, blank=True)
    engineer = models.ForeignKey(Engineer, on_delete=models.SET_NULL, null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipment.name} - {self.service_date}"

class Maintenance(models.Model):
    STATUS_CHOICES = [
        ('Repaired', 'Repaired'),
        ('Under Repair', 'Under Repair'),
        ('Needs Part', 'Needs Part'),
        ('Not Repairable', 'Not Repairable'),
    ]

    description = models.CharField(max_length=45, null=True, blank=True)
    date = models.DateField(null=True, blank=True, default=models.DateField())
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Repaired')
    cost = models.DecimalField(max_digits=50, decimal_places=0, null=True, blank=True)
    engineer = models.ForeignKey(Engineer, on_delete=models.SET_NULL, null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    periodic_service = models.ForeignKey(PeriodicService, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.equipment.name} - {self.status}"
