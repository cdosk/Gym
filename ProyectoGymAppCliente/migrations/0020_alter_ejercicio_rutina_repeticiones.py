# Generated by Django 3.2 on 2021-10-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppCliente', '0019_alter_ejercicio_rutina_repeticiones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercicio_rutina',
            name='repeticiones',
            field=models.IntegerField(default=100),
        ),
    ]
