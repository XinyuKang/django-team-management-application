# Generated by Django 4.1.6 on 2023-02-08 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("team_management", "0003_alter_employee_role"),
    ]

    operations = [
        migrations.RenameModel(old_name="Employee", new_name="Member",),
    ]