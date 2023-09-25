from django.urls import path
from . import views

urlpatterns = [
    ##department views
    path('index/', views.index),
    path('depart/list/', views.dep_list),
    path('depart/add/', views.dep_add),
    path('depart/delete/<int:dep_id>', views.dep_del),
    path('depart/edit/<int:dep_id>', views.dep_edit),
    ##application views
    path('app/list/', views.app_list),
    path('app/add/', views.app_add),
    path('app/delete/<int:app_id>', views.app_del),
    path('app/edit/<int:app_id>', views.app_edit),
    ##role views
    path('role/list/', views.role_list),
    path('role/add/', views.role_add),
    path('role/delete/<int:role_id>', views.role_del),
    path('role/edit/<int:role_id>', views.role_edit),
    ##employee views
    path('emp/list/', views.emp_list),
    path('emp/add/', views.emp_add),
    path('emp/delete/<int:emp_id>', views.emp_del),
    path('emp/edit/<int:emp_id>', views.emp_edit)
]
