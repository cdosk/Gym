# Generated by Django 3.2 on 2021-09-29 17:51

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=django.db.models.fields.FilePathField),
        ),
        migrations.AlterField(
            model_name='sportproduct',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sportproduct',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]