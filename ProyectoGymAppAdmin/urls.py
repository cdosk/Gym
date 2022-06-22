from django.urls import path

from ProyectoGymAppAdmin import views

urlpatterns = [
    path('', views.inicioadmin, name="InicioAdmin"),
    path('clases', views.clases, name="Clases"),
    path('suplementacion', views.suplementacion, name="Suplementacion"),
    path('alimentacion', views.alimentacion, name="Alimentacion"),
    path('entrenamiento', views.entrenamiento, name="Entrenamiento"),
    path('recetas', views.recetas, name="Recetas"),
    path('mostrarrecetas', views.mostrarrecetas, name="Mostrarrecetas"),
    path('editarreceta/<int:pk>', views.editoreceta, name="Editarreceta"),
    path('deletereceta/<int:pk>', views.deletereceta, name="Deletereceta")
]
