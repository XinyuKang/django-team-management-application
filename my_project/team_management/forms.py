from django import forms
from django.forms import ModelForm
from .models import Member
from phone_field import PhoneField

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        