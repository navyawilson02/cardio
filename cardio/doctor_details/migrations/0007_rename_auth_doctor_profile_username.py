# Generated by Django 5.0.3 on 2024-04-04 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_details', '0006_alter_doctor_profile_auth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor_profile',
            old_name='auth',
            new_name='username',
        ),
    ]
