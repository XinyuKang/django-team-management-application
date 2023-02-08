from django.db import models
from phone_field import PhoneField

# Create your models here.

role_choices = (
        ("REGULAR", "Regular - Can't delete members"),
        ("ADMIN", "Admin - Can delete members")
    )
    
class Member(models.Model):
    # id, first name, last name, email, phone number, role: regular vs admin
    id = models.AutoField(primary_key=True) # make the id unique
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    role = models.CharField(max_length=200, choices=role_choices, default="REGULAR")
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
