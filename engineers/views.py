# engineers/views.py
from django.shortcuts import render, get_object_or_404
from .models import Engineer, EngineerDepartment
from departments.models import Department

def engineer_list(request):
    engineers = Engineer.objects.all()  # دریافت تمام مهندسین
    return render(request, 'engineers/engineer_list.html', {'engineers': engineers})

def engineer_detail(request, phone):
    engineer = get_object_or_404(Engineer, phone=phone)
    # استفاده از EngineerDepartment برای پیدا کردن دپارتمان‌های مرتبط با مهندس
    departments = EngineerDepartment.objects.filter(engineer=engineer).select_related('department')
    return render(request, 'engineers/engineer_detail.html', {'engineer': engineer, 'departments': [ed.department for ed in departments]})

