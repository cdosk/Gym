# Generated by Django 3.2 on 2021-09-29 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=3)),
                ('weight', models.CharField(max_length=3)),
                ('experience', models.BooleanField()),
                ('objective', models.CharField(max_length=255)),
            ],
        ),
    ]