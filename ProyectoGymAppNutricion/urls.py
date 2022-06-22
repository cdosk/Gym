from django.urls import path

from ProyectoGymAppNutricion import views

urlpatterns = [
    path('lunes', views.lunes, name="Lunes"),
    path('martes', views.martes, name="Martes"),
    path('miercoles', views.miercoles, name="Miercoles"),
    path('jueves', views.jueves, name="Jueves"),
    path('viernes', views.viernes, name="Viernes"),
    path('sabado', views.sabado, name="Sabado"),
    path('domingo', views.domingo, name="Domingo"),


]
