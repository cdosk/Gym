# Generated by Django 3.2 on 2021-09-29 18:39

import ProyectoGymApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymApp', '0003_alter_sportproduct_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=ProyectoGymApp.models.filepath),
        ),
    ]