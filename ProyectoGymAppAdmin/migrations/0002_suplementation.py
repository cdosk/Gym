# Generated by Django 3.2 on 2021-10-05 22:40

import ProyectoGymAppAdmin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suplementation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameproducsupl', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('description_cons', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to=ProyectoGymAppAdmin.models.filepath)),
            ],
        ),
    ]
