# Generated by Django 3.2 on 2021-10-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppAdmin', '0007_entrenamiento_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrenamiento',
            name='content',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='entrenamiento',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
