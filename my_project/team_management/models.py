from django.db import models
from phone_field import PhoneField
from django.core.validators import EmailValidator

# Create your models here.

role_choices = (
        ("REGULAR", "Regular - Can't delete members"),
        ("ADMIN", "Admin - Can delete members")
    )
    
class Member(models.Model):
    # id, first name, last name, email, phone number, role: regular vs admin
    id = models.AutoField(primary_key=True) # make the id unique
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=200, blank=False, unique=True,validators=[EmailValidator])

    role = models.CharField(max_length=200, choices=role_choices, default="REGULAR")
    phone_number = PhoneField(blank=False, unique=True)
