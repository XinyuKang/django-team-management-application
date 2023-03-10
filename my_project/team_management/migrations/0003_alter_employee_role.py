# Generated by Django 4.1.6 on 2023-02-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("team_management", "0002_rename_first_name_employee_firstname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="role",
            field=models.CharField(
                choices=[
                    ("REGULAR", "Regular - Can't delete members"),
                    ("ADMIN", "Admin - Can delete members"),
                ],
                default="REGULAR",
                max_length=200,
            ),
        ),
    ]
