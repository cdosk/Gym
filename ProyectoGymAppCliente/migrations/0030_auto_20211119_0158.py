# Generated by Django 3.2 on 2021-11-19 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppCliente', '0029_alter_comida_plan_nutricional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaingredientes',
            name='cantidadMaxGr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='listaingredientes',
            name='cantidadMinGr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='listaingredientes',
            name='cucharadas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listaingredientes',
            name='unidades',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opciones',
            name='cantidadMaxGr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='opciones',
            name='cantidadMinGr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='opciones',
            name='cucharadas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opciones',
            name='unidades',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
