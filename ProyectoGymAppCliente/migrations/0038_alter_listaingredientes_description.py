# Generated by Django 3.2 on 2021-11-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppCliente', '0037_auto_20211124_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaingredientes',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
