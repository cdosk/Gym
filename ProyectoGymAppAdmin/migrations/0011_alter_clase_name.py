# Generated by Django 3.2 on 2021-10-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppAdmin', '0010_auto_20211013_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
