from django.db import models

# Create your models here.


class Trainer(models.Model):
    GENDER = [('M', 'Masculino'), ('F', 'Femenino')]
    name = models.CharField(("Name"), max_length=50)
    surname = models.CharField(("Apellidos"), max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER)
    mobileNumber = models.IntegerField()


class Class(models.Model):
    name = models.CharField(("hola"), max_length=100)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)


class ClassSchedule(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    repeat = models.BooleanField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)


class Day(models.Model):
    LUNES = 'L'
    MARTES = 'M'
    MIERCOLES = 'K'
    JUEVES = 'J'
    VIERNES = 'V'
    SABADO = 'S'
    DOMINGO = 'D'
    DAYS_OF_WEEK = [
        (LUNES, 'Lunes'),
        (MARTES, 'Martes'),
        (MIERCOLES, 'Miercoles'),
        (JUEVES, 'Jueves'),
        (VIERNES, 'Viernes'),
        (SABADO, 'Sábado'),
        (DOMINGO, 'Domingo')
    ]
    day_of_week = models.CharField(max_length=1, choices=DAYS_OF_WEEK)


class ClassSchedule_Day(models.Model):
    classSchedule_id = models.ForeignKey(
        ClassSchedule, on_delete=models.CASCADE)
    day_id = models.ForeignKey(Day, on_delete=models.CASCADE)
    startTime = models.TimeField()
    endTime = models.TimeField()


class ClientClass(models.Model):
    capacity = models.IntegerField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
