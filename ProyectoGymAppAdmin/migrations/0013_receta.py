# Generated by Django 3.2 on 2021-10-20 21:49

import ProyectoGymAppAdmin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppAdmin', '0012_remove_clase_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('ingredients', models.CharField(max_length=1000)),
                ('preparation', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to=ProyectoGymAppAdmin.models.filepath)),
            ],
        ),
    ]
