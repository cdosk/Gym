# Generated by Django 3.2 on 2021-10-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGymApp', '0010_nutricionist_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutricionist',
            name='picture',
            field=models.ImageField(default='https://icons-for-free.com/iconfiles/png/512/profile+profile+page+user+icon-1320186864367220794.png', upload_to='profile-pictures/nutricionistas'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='picture',
            field=models.ImageField(default='https://icons-for-free.com/iconfiles/png/512/profile+profile+page+user+icon-1320186864367220794.png', upload_to='profile-pictures/entrenadores'),
        ),
    ]
