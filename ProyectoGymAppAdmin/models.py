from django.db import models
from ProyectoGymApp.models import Trainer
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.


class Clase(models.Model):
    name = models.CharField(max_length=100)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    DAYS_OF_WEEK = [
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('K', 'Miercoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sábado'),
        ('D', 'Domingo')
    ]
    days_of_week = models.CharField(
        max_length=1, choices=DAYS_OF_WEEK)
    startTime = models.TimeField()
    endTime = models.TimeField()
    capacity = models.IntegerField(default=0)
    inscritos = models.IntegerField(default=0)


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Suplementation(models.Model):
    nameproducsupl = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    description_cons = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)


class Entrenamiento(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.CharField(max_length=2000)
    author = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)

    def __str__(self):
        return self.title

class Alimentacion(models.Model):
    alimento = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    cantidad = models.FloatField()
    calorias = models.FloatField()

class Receta(models.Model):
    title = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=1000)
    preparation = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = filepath, null=True, blank=True)
