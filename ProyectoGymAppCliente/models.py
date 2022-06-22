from io import open_code
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import DateField
from ProyectoGymApp.models import Profile
import datetime
import os


class Ejercicio(models.Model):

    DIFFICULTY = (
        ('P', 'Principiante'),
        ('I', 'Intermedio'),
        ('A', 'Avanzado'),
    )

    CATEGORY = (
        ('E', 'Estiramientos'),
        ('PC', 'Peso corporal'),
        ('B', 'Barra'),
        ('M', 'Mancuernas'),
        ('P', 'Polea'),
        ('BE', 'Banda Elástica')
    )

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY)
    category = models.CharField(max_length=2, choices=CATEGORY)
    video = models.URLField()
    muscles_involved = models.ManyToManyField('Muscles')

    def __str__(self):
        return self.name


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Muscles(models.Model):

    name = models.CharField(max_length=50, unique=True)
    img = models.URLField(null=True)

    def __str__(self):
        return self.name


class Rutina(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    ejercicios = models.ManyToManyField(Ejercicio, through='Ejercicio_Rutina')

    def __str__(self):
        return self.name


class Ejercicio_Rutina(models.Model):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    sets = models.IntegerField()
    sets_adicionales = models.IntegerField(
        verbose_name="Sets Adicionales", default=0)
    repeticiones = models.IntegerField(
        verbose_name="Repeticiones/Pasos", default=0)
    rep_adicionales = models.IntegerField(
        verbose_name="Repeticiones Adicionales", default=0)
    fallo = models.BooleanField(default=False)

    def __str__(self):
        return "{}. {}".format(self.rutina.name, self.ejercicio.name)


class PlanEntrenamiento(models.Model):

    LEVEL = [
        ('P', 'Principiante'),
        ('I', 'Intermedio'),
        ('A', 'Avanzado'),
    ]

    OBJECTIVE = [
        ('H', 'Hipertrofia muscular'),
        ('QyB', 'Quemar grasa y bajar de peso'),
    ]

    name = models.CharField(max_length=100, unique=True)
    img = models.URLField(null=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    rutinas = models.ManyToManyField(
        Rutina, through='Rutina_PlanEntrenamiento')
    level = models.CharField(max_length=1, choices=LEVEL, default='P')
    objective = models.CharField(max_length=5, choices=OBJECTIVE, null=True)

    def __str__(self):
        return self.name


class Rutina_PlanEntrenamiento(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=CASCADE)
    plan_entrenamiento = models.ForeignKey(
        PlanEntrenamiento, on_delete=CASCADE)
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
    week = models.IntegerField(null=True)
    month = models.IntegerField(null=True)

    def __str__(self):
        return "{} - {} {} / Semana {} / Mes {}".format(
            self.plan_entrenamiento.name, self.rutina.name, self.get_days_of_week_display(), self.week, self.month)


class Food(models.Model):
    name = models.CharField(max_length=100, unique=True)
    caloriasXgr = models.IntegerField(null=True)
    ulrPhoto = models.URLField(null=True)

    def __str__(self):
        return self.name


class PlanNutricional(models.Model):
    OBJECTIVE = [
        ('H', 'Hipertrofia muscular'),
        ('QyB', 'Quemar grasa y bajar de peso'),
    ]
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=300, null=True)
    objective = models.CharField(max_length=5, choices=OBJECTIVE, null=True)

    def __str__(self):
        return self.name


class NutritionalPlanDate(models.Model):
    planNutricional = models.ForeignKey(PlanNutricional, on_delete=CASCADE)
    month = models.IntegerField()
    day = models.IntegerField()
    date = models.DateField()


class ListaIngredientes(models.Model):
    plan_nutricional = models.ManyToManyField(
        PlanNutricional, through='Comida')
    food = models.ManyToManyField(Food, through='Opciones')
    description = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return "{}".format(self.description)


class Comida(models.Model):

    COMIDA = [
        (1, 'Comida 1'),
        (2, 'Comida 2'),
        (3, 'Comida 3'),
        (4, 'Comida 4'),
        (5, 'Comida 5'),
        (6, 'Comida 6'),
        (7, 'Comida 7'),
        (8, 'Comida 8'),
    ]

    plan_nutricional = models.ForeignKey(PlanNutricional, on_delete=CASCADE)
    lista_ingredientes = models.ForeignKey(
        ListaIngredientes, on_delete=CASCADE, null=True)
    num_comida = models.IntegerField(choices=COMIDA)
    num_lista = models.IntegerField(null=True)

    def __str__(self):
        return "{} / Comida {} - {}) {}".format(self.plan_nutricional.name, self.num_comida, self.num_lista, self.lista_ingredientes)


class Opciones(models.Model):
    lista_ingredientes = models.ForeignKey(
        ListaIngredientes, on_delete=CASCADE)

    food = models.ForeignKey(Food, on_delete=CASCADE)

    def __str__(self):
        return "{} - Opciones ({})".format(self.lista_ingredientes, self.food.name)


class SeguimientoNutricional(models.Model):
    PlanNutricional = models.ForeignKey(PlanNutricional, on_delete=CASCADE)
    comida = models.ForeignKey(Comida, on_delete=CASCADE, null=True)
    date = models.DateField()
    completado = models.BooleanField(default=False)


class Evaluation(models.Model):
    EXP = (
        ('P', 'Principiante'),
        ('I', 'Intermedio'),
        ('A', 'Avanzado'),
    )

    OBJECTIVE = (
        ('H', 'Hipertrofia muscular'),
        ('QyB', 'Quemar grasa y bajar de peso'),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.CharField(max_length=1, choices=EXP)
    objective = models.CharField(max_length=5, choices=OBJECTIVE)
    training_plan = models.ForeignKey(
        PlanEntrenamiento, on_delete=CASCADE, null=True)
    nutritional_plan = models.OneToOneField(
        PlanNutricional, on_delete=CASCADE, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    duration = models.IntegerField(default=3)
    endDate = models.DateField(null=True, blank=True)


class Gallery(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
