# engineers/views.py
from django.shortcuts import render
from .models import Engineer

def engineer_list(request):
    engineers = Engineer.objects.all()
    for engineer in engineers:
        print(engineer.__dict__)  # چاپ اطلاعات دقیق هر مهندس
    return render(request, 'engineers/engineer_list.html', {'engineers': engineers})
