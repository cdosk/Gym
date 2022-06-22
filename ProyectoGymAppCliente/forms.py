from typing import ValuesView
from django import forms
from django.core.exceptions import RequestDataTooBig
from django.db.models import query
from django.db.models.base import Model
from django.forms.fields import MultipleChoiceField
from django.forms.models import ModelMultipleChoiceField
from django.forms.widgets import CheckboxInput, RadioSelect
from django.forms import ModelForm
from .models import Evaluation


class EvaluationForm(forms.Form):
    height = forms.DecimalField(
        max_value=2.0, decimal_places=2, label="Talla (metros): ")
    weight = forms.DecimalField(
        max_value=200.0, decimal_places=2, label="Peso (kg): ")

    EXP = (
        ('P', 'Principiante'),
        ('I', 'Intermedio'),
        ('A', 'Avanzado'),
    )

    OBJECTIVE = (
        ('H', 'Hipertrofia muscular'),
        ('QyB', 'Quemar grasa y bajar de peso'),
    )

    experience = forms.ChoiceField(label="Experiencia: ", choices=EXP)
    objective = forms.ChoiceField(label="Objetivo: ", choices=OBJECTIVE)
    duration = forms.IntegerField(
        label="Duración: ", max_value=12, min_value=1)


class EjercicioForm(forms.Form):

    CATEGORY = [
        ('E', 'Estiramientos'),
        ('PC', 'Peso corporal'),
        ('B', 'Barra'),
        ('M', 'Mancuernas'),
        ('P', 'Polea'),
        ('BE', 'Banda Elástica')
    ]

    MUSCLES = [
        (1, 'Triceps'),
        (2, 'Cuadriceps'),
        (3, 'Biceps'),
        (4, 'Trapecios'),
        (5, 'Deltoides'),
        (6, 'Antebrazos'),
        (7, 'Pectorales'),
        (8, 'Dorsales'),
        (9, 'Pantorrillas'),
        (10, 'Femorales'),
        (11, 'Gluteos'),
        (12, 'Abdominales'),
    ]

    category = forms.ChoiceField(
        choices=CATEGORY, widget=RadioSelect(attrs={'checked': True}), label='Categoria:')
    muscles_involved = forms.ChoiceField(
        choices=MUSCLES, label='Grupo muscular: ')
