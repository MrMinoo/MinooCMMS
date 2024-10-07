# engineers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('engineers/', views.engineer_list, name='engineer_list'),  # تعریف مسیر engineer_list
    path('engineer/<str:phone>/', views.engineer_detail, name='engineer_detail'),  # استفاده از پارامتر phone
]

