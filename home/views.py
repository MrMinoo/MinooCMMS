from django.db.models import OuterRef, Subquery
from django.utils import timezone
from equipments.models import Equipment
from maintenance.models import PeriodicService
from departments.models import Department
from engineers.models import Engineer
from django.shortcuts import render

def home(request):
    # دستگاه‌هایی که موعد سرویس دوره‌ای آن‌ها رسیده است
    due_services = Equipment.objects.filter(
        id__in=Subquery(
            PeriodicService.objects.filter(
                equipment_id=OuterRef('id'),
                next_date__lte=timezone.now()
            ).values('equipment_id')
        )
    )

    # دستگاه‌هایی که در حال تعمیر هستند
    ongoing_repairs = Equipment.objects.filter(status='under_repair')

    # لیست دپارتمان‌ها
    departments = Department.objects.all()

    # لیست مهندسین
    engineers = Engineer.objects.all()

    # دستگاه‌هایی که اخیراً سرویس یا تعمیر شده‌اند
    recently_serviced = Equipment.objects.filter(
        periodicservice__service_date__isnull=False
    ).order_by('-periodicservice__service_date')[:5]

    context = {
        'due_services': due_services,
        'ongoing_repairs': ongoing_repairs,
        'departments': departments,
        'engineers': engineers,
        'recently_serviced': recently_serviced,
    }
    return render(request, 'home/home.html', context)
