# Generated by Django 5.0.3 on 2024-04-07 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0010_alter_patient_details_age_alter_patient_details_dob_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_details',
            name='user_id',
        ),
    ]
