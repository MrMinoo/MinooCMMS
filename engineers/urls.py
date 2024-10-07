# engineers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('engineers/', views.engineer_list, name='engineer_list'),  # تعریف مسیر engineer_list
]
