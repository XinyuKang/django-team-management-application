from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Member
# Create your views here.


def index(request):
    members = Member.objects.all()
    return render(request, 'team_management/index.html', {'members': members})

# class MemberList(ListView):
#     model = Member

def showMember(request):
    return render(request, "team_management/show.html")


def editMember(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, "team_management/edit.html", {'member': member})


def createMember(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        role = request.POST.get("role")
        phone_number = request.POST.get("phone_number")

        member = Member()
        member.lastname = lastname
        member.firstname = firstname
        member.email = email
        member.phone_number = phone_number
        member.role = role
        member.save()
        return redirect('index')
    return redirect('index')


def edit(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == "POST":
        if request.POST.get('action') == "delete":
            member.delete()
            return redirect('index')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        role = request.POST.get('role')

        member.firstname = firstname
        member.lastname = lastname
        member.email = email
        member.phone_number = phone_number
        member.role = role
        member.save()
        
        return redirect('index')
