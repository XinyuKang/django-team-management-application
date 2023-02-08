from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('specific', views.specific, name='specific'),
    path('showEmployeeForm', views.showEmployeeForm, name="showEmployeeForm"),
    path('createEmployee', views.createEmployee, name="createEmployee")
]