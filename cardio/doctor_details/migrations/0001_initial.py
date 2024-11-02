# Generated by Django 5.0.3 on 2024-03-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('health_condition', models.TextField(max_length=100)),
            ],
        ),
    ]
