from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Employee
# Create your views here.


def index(request):
    return HttpResponse("This is my first url")

def specific(request):
    list1 = [1,2,3,4]
    return HttpResponse(list1)

def showEmployeeForm(request):
    return render(request, "team_management/employeeForm.html")

def createEmployee(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        role = request.POST.get("role")
        salary = request.POST.get("salary")
        employee = Employee()
        employee.lastname = lastname
        employee.firstname = firstname
        employee.email = email
        employee.role = role
        employee.salary = salary
        employee.save()
        return redirect('index')
    return redirect('index')

