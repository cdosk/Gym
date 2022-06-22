from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from ProyectoGymApp.models import Trainer
from .models import Suplementation, Receta
import os

from ProyectoGymAppAdmin.forms import ClaseForm
from .models import Entrenamiento, Suplementation, Alimentacion, Clase


def inicioadmin(request):

    return render(request, "ProyectoGymAppAdmin/inicioadmin.html")


def clases(request):
    form = ClaseForm()
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            clase = Clase()
            trainer_id = form.cleaned_data['trainer']
            trainer = Trainer.objects.get(id=trainer_id)
            clase.name = form.cleaned_data['name']
            clase.trainer_id = trainer
            clase.days_of_week = form.cleaned_data['days_of_week']
            clase.startTime = form.cleaned_data['startTime']
            clase.endTime = form.cleaned_data['endTime']
            clase.capacity = form.cleaned_data['capacity']
            clase.save()
            messages.success(request, "Clase guardada")
    context = {
        "form": form
    }
    return render(request, "ProyectoGymAppAdmin/clases.html", context)


def suplementacion(request):

    if request.method == "POST":
        prod = Suplementation()
        prod.nameproducsupl = request.POST.get('name_supl')
        prod.description = request.POST.get('description_supl')
        prod.description_cons = request.POST.get('description_supl_cons')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, 'Producto agregado')
        return redirect('/')

    return render(request, "ProyectoGymAppAdmin/suplementacion.html")


def alimentacion(request):

    if request.method == "POST":
        inf = Alimentacion()
        inf.alimento = request.POST.get('name_ali')
        inf.categoria = request.POST.get('cat_ali')
        inf.cantidad = request.POST.get('can_ali')
        inf.calorias = request.POST.get('en_ali')

        inf.save()
        messages.success(request, 'Alimento agregado')
    return render(request, "ProyectoGymAppAdmin/alimentacion.html")


def entrenamiento(request):
    if request.method == "POST":
        articulo = Entrenamiento()
        articulo.title = request.POST.get('title')
        articulo.author = request.POST.get('author')
        articulo.content = request.POST.get('content')
        if len(request.FILES) != 0:
            articulo.image = request.FILES['image']
        articulo.save()
        messages.success(request, 'Artículo agregado')
    return render(request, "ProyectoGymAppAdmin/entrenamiento.html")

def recetas(request):

        if request.method == "POST":
                rct = Receta()
                rct.title = request.POST.get('title')
                rct.ingredients = request.POST.get('ingredients')
                rct.preparation = request.POST.get('preparation')

                if len(request.FILES) != 0:
                        rct.image = request.FILES['image']
                
                rct.save()
                messages.success(request, 'Receta Agregada')

        return render (request, "ProyectoGymAppAdmin/recetas.html")

def mostrarrecetas(request):

        datareceta = Receta.objects.all()

        return render(request, "ProyectoGymAppAdmin/mostrarreceta.html", {"datareceta":datareceta})

def editoreceta(request, pk):
        
        ereceta = Receta.objects.get(id=pk)
        context = {'ereceta':ereceta}

        if request.method == "POST":
                if len(request.FILES) != 0:
                        if len(ereceta.image) > 0:
                                os.remove(ereceta.image.path)
                        ereceta.image = request.FILES['image']
                ereceta.title = request.POST.get('title')
                ereceta.ingredients = request.POST.get('ingredients')
                ereceta.preparation = request.POST.get('preparation')                
                ereceta.save()
                return redirect('Mostrarrecetas')

        return render(request, "ProyectoGymAppAdmin/editarreceta.html", context)

def deletereceta(request, pk):
        ereceta = Receta.objects.get(id=pk)
        if len(ereceta.image) > 0:
                os.remove(ereceta.image.path)
        ereceta.delete()
        
        return redirect('Mostrarrecetas')