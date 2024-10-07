# maintenance/urls.py یا repair/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('repairs/', views.repair_list, name='repair_list'),
    path('recent-services/', views.recent_service_list, name='recent_service_list'),  # تعریف مسیر recent_service_list

]
