# Generated by Django 3.2 on 2021-09-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymApp', '0002_auto_20210929_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportproduct',
            name='price',
            field=models.FloatField(),
        ),
    ]
