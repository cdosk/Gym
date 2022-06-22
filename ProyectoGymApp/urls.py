from os import name
from django.urls import path
from ProyectoGymApp import views
from ProyectoGymAppCliente import views as viewscli

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('entrenadores', views.entrenadores, name="Entrenadores"),
    path('oferta', views.oferta, name="Oferta"),
    path('tienda', views.tienda, name="Tienda"),
    path('registrar', views.registrar, name="Registrar"),
    path('registroclientes', viewscli.registroclientes, name="Registroclientes"),
    path('mostraroferta', views.mostrarofertas, name="Mostraroferta"),
    path('login', views.login, name="Login"),
    path('logout', views.logout, name="Logout"),
    path('editoferta/<int:pk>', views.editoferta, name="Editoferta"),
    path('deleteoferta/<int:pk>', views.deleteoferta, name="Deleteoferta"),
    path('profile', views.profileview, name='Perfil'),
    path('mostrar_plan/<int:pk_plan>', viewscli.mostrar_plan_entrenamiento,
         name="MostrarPlanEntrenamiento"),
    path('mostrar_plan_nutricional/<int:pk_plan>/<int:duracion_meses>/<str:initial_date>', viewscli.mostrar_plan_nutricional,
         name="MostrarPlanNutricional"),
]
