from django import forms
from django.core.exceptions import RequestDataTooBig
from django.db.models.base import Model
from django.forms.widgets import CheckboxInput
from django.forms import ModelForm
from .models import Evaluation

class EvaluationForm(forms.Form):
    name = forms.CharField(label="Nombres")
    lastname = forms.CharField(label="Apellidos")
    phone = forms.CharField(label="Celular")
    birth = forms.DateField(label="Fecha de Nacimiento")
    height = forms.DecimalField(label="Talla")
    weight = forms.DecimalField(label="Peso")
    experience = forms.CharField(label="Experiencia")
    objective = forms.CharField(label="Objetivo")
    