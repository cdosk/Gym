from django.urls import path

from ProyectoGymAppCliente import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('evaluacion',views.evaluacion, name="Evaluacion"),
]