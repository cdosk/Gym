# Generated by Django 3.2 on 2021-09-29 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppCliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='email',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='experience',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='height',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='objective',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='weight',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
