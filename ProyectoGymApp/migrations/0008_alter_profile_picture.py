# Generated by Django 3.2 on 2021-10-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymApp', '0007_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='https://icons-for-free.com/iconfiles/png/512/profile+profile+page+user+icon-1320186864367220794.png', upload_to='ProyectoGymApp/static/img/profile-pictures'),
        ),
    ]
