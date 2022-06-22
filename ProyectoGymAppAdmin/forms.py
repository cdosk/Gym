from django import forms
from django.db.models.fields import TimeField
from django.forms.widgets import CheckboxInput, TimeInput
from ProyectoGymApp.models import Trainer


class ClaseForm(forms.Form):
    trainers = Trainer.objects.all()
    TRAINERS = []
    for entrenador in trainers:
        TRAINERS.append((entrenador.pk, entrenador.name))
    name = forms.CharField(max_length=100)
    trainer = forms.ChoiceField(label="Entrenador", choices=TRAINERS)
    DAYS_OF_WEEK = [
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('K', 'Miercoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sábado'),
        ('D', 'Domingo'),
    ]
    days_of_week = forms.ChoiceField(
        choices=DAYS_OF_WEEK)
    startTime = forms.TimeField(
        label="Hora de inicio",
        widget=forms.TimeInput(attrs={'type': 'time'}),)
    endTime = forms.TimeField(
        label="Hora de fin",
        widget=forms.TimeInput(attrs={'type': 'time'}))
    capacity = forms.IntegerField(max_value=50)
