# Generated by Django 3.2 on 2021-09-30 00:23

import ProyectoGymApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymApp', '0004_alter_sportproduct_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=9)),
                ('days', models.FloatField(verbose_name=50)),
                ('turn', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=ProyectoGymApp.models.filepath)),
            ],
        ),
    ]