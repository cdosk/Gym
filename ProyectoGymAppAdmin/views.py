from django.shortcuts import render

def inicio(request):

        return render(request, "ProyectoGymAppAdmin/inicio.html")

def horarios(request):

        return render(request, "ProyectoGymAppAdmin/horarios.html")

def tienda(request):

        return render(request, "ProyectoGymAppAdmin/tienda.html")


# Create your views here.
