# Generated by Django 5.1.1 on 2024-10-07 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('engineers', '0001_initial'),
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodicService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('service_date', models.DateField(blank=True, default=models.DateField(), null=True)),
                ('next_date', models.DateField(blank=True, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=0, max_digits=50, null=True)),
                ('engineer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='engineers.engineer')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('date', models.DateField(blank=True, default=models.DateField(), null=True)),
                ('status', models.CharField(choices=[('Repaired', 'Repaired'), ('Under Repair', 'Under Repair'), ('Needs Part', 'Needs Part'), ('Not Repairable', 'Not Repairable')], default='Repaired', max_length=20)),
                ('cost', models.DecimalField(blank=True, decimal_places=0, max_digits=50, null=True)),
                ('engineer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='engineers.engineer')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipments.equipment')),
                ('periodic_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maintenance.periodicservice')),
            ],
        ),
    ]
