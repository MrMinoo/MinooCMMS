# departments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.department_list, name='department_list'),  # department_list
    path('department/<int:pk>/', views.department_detail, name='department_detail'),  #department_detail
]
