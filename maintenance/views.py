# maintenance/views.py یا repair/views.py
from django.shortcuts import render
from .models import PeriodicService

def repair_list(request):
    # کد مربوط به نمایش لیست تعمیرات
    return render(request, 'maintenance/repair_list.html')

def recent_service_list(request):
    recent_services = PeriodicService.objects.order_by('-service_date')
    return render(request, 'maintenance/recent_service_list.html', {'recent_services': recent_services})