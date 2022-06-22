from django.contrib import admin
from ProyectoGymAppAdmin.models import Alimentacion, Entrenamiento
from ProyectoGymAppAdmin.views import Suplementation

admin.site.register(Suplementation)
admin.site.register(Alimentacion)
admin.site.register(Entrenamiento)
