# Generated by Django 4.2.7 on 2023-11-08 12:01

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_employee_created_at_employee_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile',
            field=models.ImageField(default='employees/employee.png', null=True, upload_to=main_app.models.unique_img_name),
        ),
    ]
