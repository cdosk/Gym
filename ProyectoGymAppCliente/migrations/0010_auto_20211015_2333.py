# Generated by Django 3.2 on 2021-10-15 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymAppCliente', '0009_auto_20211015_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanEntrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rutina_PlanEntrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_of_week', models.CharField(choices=[('L', 'Lunes'), ('M', 'Martes'), ('K', 'Miercoles'), ('J', 'Jueves'), ('V', 'Viernes'), ('S', 'Sábado'), ('D', 'Domingo')], max_length=1)),
                ('plan_entrenamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoGymAppCliente.planentrenamiento')),
                ('rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoGymAppCliente.rutina')),
            ],
        ),
        migrations.AddField(
            model_name='planentrenamiento',
            name='rutinas',
            field=models.ManyToManyField(through='ProyectoGymAppCliente.Rutina_PlanEntrenamiento', to='ProyectoGymAppCliente.Rutina'),
        ),
    ]
