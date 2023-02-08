from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Employee
# Create your views here.


def index(request):
    employees = Employee.objects.all()
    return render(request, 'team_management/index.html', {'employees': employees})


def specific(request):
    list1 = [1, 2, 3, 4]
    return HttpResponse(list1)


def showEmployeeForm(request):
    return render(request, "team_management/employeeForm.html")


def editEmployee(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, "team_management/edit.html", {'employee': employee})


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


def edit(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        if request.POST.get('action') == "delete":
            employee.delete()
            return redirect('index')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        employee.firstname = firstname
        employee.lastname = lastname
        employee.email = email
        employee.save()
        
        return redirect('index')
