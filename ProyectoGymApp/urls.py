from django.urls import path
from ProyectoGymApp import views
from ProyectoGymAppCliente import views as viewscli

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('entrenadores',views.entrenadores, name="Entrenadores"),
    path('comunidad',views.comunidad, name="Comunidad"),
    path('tienda',views.tienda, name="Tienda"),
    path('registrar',views.registrar, name="Registrar"),
    path('registroclientes',viewscli.registroclientes, name="Registroclientes"),
    path('login',views.login, name="Login"),
    path('logout',views.logout, name="Logout"),
]