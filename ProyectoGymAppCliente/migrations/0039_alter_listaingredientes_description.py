# Generated by Django 3.2 on 2021-11-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppCliente', '0038_alter_listaingredientes_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaingredientes',
            name='description',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]