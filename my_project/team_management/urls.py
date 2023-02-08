from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('specific', views.specific, name='specific'),
    path('showEmployeeForm', views.showEmployeeForm, name="showEmployeeForm"),
    path('createEmployee', views.createEmployee, name="createEmployee"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('editEmployee/<int:id>/', views.editEmployee, name="editEmployee"),
]