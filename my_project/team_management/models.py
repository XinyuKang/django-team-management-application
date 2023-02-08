from django.db import models
from phone_field import PhoneField

# Create your models here.

class Employee(models.Model):
    # id, first name, last name, email, phone number, role: regular vs admin
    id = models.AutoField(primary_key=True) # make the id unique
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    role = models.CharField(max_length=300)  # TODO change this to a selection
    salary = models.IntegerField(null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
