# home/views.py
from django.shortcuts import render
from equipments.models import Equipment
from maintenance.models import PeriodicService, Repair
from departments.models import Department
from engineers.models import Engineer
from django.utils import timezone

def home(request):
    # دستگاه‌هایی که موعد سرویس دوره‌ای آن‌ها رسیده است
    due_services = Equipment.objects.filter(periodicservice__next_service_date__lte=timezone.now())

    # دستگاه‌هایی که در حال تعمیر هستند
    ongoing_repairs = Equipment.objects.filter(repair__status='ongoing')

    # لیست دپارتمان‌ها
    departments = Department.objects.all()

    # لیست مهندسین
    engineers = Engineer.objects.all()

    # دستگاه‌هایی که اخیراً سرویس یا تعمیر شده‌اند
    recently_serviced = Equipment.objects.filter(
        periodicservice__last_service_date__isnull=False
    ).order_by('-periodicservice__last_service_date')[:5]

    context = {
        'due_services': due_services,
        'ongoing_repairs': ongoing_repairs,
        'departments': departments,
        'engineers': engineers,
        'recently_serviced': recently_serviced,
    }
    return render(request, 'home/home.html', context)
