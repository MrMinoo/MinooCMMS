# departments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.department_list, name='department_list'),  # تعریف مسیر department_list
]
