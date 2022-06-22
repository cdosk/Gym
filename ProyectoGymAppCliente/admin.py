from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Evaluation)
admin.site.register(PlanEntrenamiento)
admin.site.register(Rutina)
admin.site.register(Rutina_PlanEntrenamiento)
admin.site.register(Ejercicio_Rutina)
admin.site.register(Food)
admin.site.register(Opciones)
admin.site.register(PlanNutricional)
admin.site.register(Comida)
admin.site.register(ListaIngredientes)


@admin.register(Ejercicio)
class Ejercicio(admin.ModelAdmin):
    list_display = ('name', 'video')
