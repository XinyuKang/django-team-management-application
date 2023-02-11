from django import forms
from django.forms import ModelForm
from .models import Member
from phone_field import PhoneField

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        


# role_choices = (
#         ("REGULAR", "Regular - Can't delete members"),
#         ("ADMIN", "Admin - Can delete members")
#     )

# class MemberForm(forms.Form):
#     # id = forms.AutoField(primary_key=True) # make the id unique
#     firstname = forms.CharField(max_length=100)
#     lastname = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=200)

#     # role = forms.CharField(widget=forms.Select(choices=role_choices))
#     # phone_number = PhoneField(widget=forms.TextInput(attrs={'placeholder': ('Phone')}), label=("Phone number"), required=True)

#     # class Meta:
#     #     model = Member
#     #     fields = "__all__"