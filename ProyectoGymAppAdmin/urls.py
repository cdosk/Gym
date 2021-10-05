from django.urls import path

from ProyectoGymAppAdmin import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('horarios',views.horarios, name="Horarios"),
    path('tienda',views.tienda, name="Tienda"),
]