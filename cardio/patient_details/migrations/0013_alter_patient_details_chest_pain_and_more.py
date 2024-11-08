# Generated by Django 5.0.3 on 2024-04-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_details', '0012_patient_details_user_id_alter_patient_details_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_details',
            name='chest_pain',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='hyper_tension_bp',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='palpitation',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='surgery',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='0', max_length=100),
        ),
    ]
