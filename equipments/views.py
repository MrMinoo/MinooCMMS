from django.shortcuts import render, get_object_or_404
from .models import Equipment

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipments/equipment_list.html', {'equipments': equipments})


def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'equipments/equipment_detail.html', {'equipment': equipment})
