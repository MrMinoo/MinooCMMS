# departments/views.py
from django.shortcuts import render, get_object_or_404
from .models import Department
from engineers.models import EngineerDepartment

def department_list(request):
    departments = Department.objects.all()  # دریافت تمام دپارتمان‌ها
    return render(request, 'departments/department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    # استفاده از EngineerDepartment برای پیدا کردن مهندسین مرتبط با دپارتمان
    engineers = EngineerDepartment.objects.filter(department=department).select_related('engineer')
    return render(request, 'departments/department_detail.html', {'department': department, 'engineers': [ed.engineer for ed in engineers]})
