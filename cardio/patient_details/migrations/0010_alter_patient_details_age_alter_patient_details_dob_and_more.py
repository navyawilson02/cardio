# Generated by Django 5.0.3 on 2024-04-07 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0009_alter_patient_details_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_details',
            name='age',
            field=models.CharField(default='phone no.', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='dob',
            field=models.CharField(default='date', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='height',
            field=models.CharField(default='phone no.', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='phone_number',
            field=models.CharField(default='phone no.', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='weight',
            field=models.CharField(default='phone no.', max_length=100),
        ),
    ]
