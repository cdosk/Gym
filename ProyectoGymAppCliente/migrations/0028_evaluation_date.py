# Generated by Django 3.2 on 2021-11-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppCliente', '0027_auto_20211118_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
