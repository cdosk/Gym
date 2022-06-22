from django.urls import path

from ProyectoGymAppCliente import views
from ProyectoGymAppAdmin import views as viewsadmin
from ProyectoGymAppAdmin.models import Entrenamiento

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('evaluacion', views.evaluacion, name="Evaluacion"),
    path('ejercicios', views.buscarejercicios, name="Ejercicios"),
    path('infosuplementacion', views.infosuplementacion, name="InfoSuplementacion"),
    path('informacion', views.informacion, name="Informacion"),
    path('artentrenamiento', views.articulos_entrenamiento,
         name="ArticulosEntrenamiento"),
    path('articulo/<int:pk>', views.articulo, name="Articulo"),
    path('planes_recomendados/<int:pk_evaluacion>',
         views.planes_recomendados, name="PlanesRecomendados"),
    path('mostrar_plan/<int:pk_plan>', views.mostrar_plan_entrenamiento,
         name="MostrarPlanEntrenamiento"),
    path('mostrar_rutina/<int:pk_plan>/<int:pk_rutina>',
         views.mostrar_rutina, name="MostrarRutina"),
    path('galeria', views.galeria, name="Galeria"),
    path('uploadgaleria', views.uploadgaleria, name="Uploadgaleria"),
    path('editgaleria/<int:pk>', views.editgaleria, name="Editgaleria"),
    path('deletegaleria/<int:pk>', views.deletegaleria, name="Deletegaleria"),
    path('mostrarrecetacliente', views.mostrarrecetas,
         name="Mostrarrecetascliente"),
    path('mostrarofertacliente', views.mostrarofertas,
         name="Mostrarofertascliente"),

    path('verificar', views.verificar, name="Verificar"),
    path('mostrar_plan_nutricional/<int:pk_plan>/<int:duracion_meses>/<str:initial_date>', views.mostrar_plan_nutricional,
         name="MostrarPlanNutricional"),
    path('mostrarplannxdia/<int:pk_plan>/<str:date>',
         views.mostrarPlannXdia, name="MostrarPlanNutricionalXdia")
]
