# Generated by Django 3.2 on 2021-10-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppAdmin', '0005_entrenamiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrenamiento',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
