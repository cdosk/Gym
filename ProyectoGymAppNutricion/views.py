from django.shortcuts import render

# Create your views here.
def lunes(request):

    return render(request, "ProyectoGymAppNutricion/lunes.html")

def martes(request):

    return render(request, "ProyectoGymAppNutricion/martes.html")

def miercoles(request):

    return render(request, "ProyectoGymAppNutricion/miercoles.html")

def jueves(request):

    return render(request, "ProyectoGymAppNutricion/jueves.html")

def viernes(request):

    return render(request, "ProyectoGymAppNutricion/viernes.html")

def sabado(request):

    return render(request, "ProyectoGymAppNutricion/sabado.html")

def domingo(request):

    return render(request, "ProyectoGymAppNutricion/domingo.html")

