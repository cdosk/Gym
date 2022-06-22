import datetime
import os
from django.db.models.fields import IntegerField
from django.http import response
from .models import Ejercicio, Ejercicio_Rutina, Evaluation, Muscles, NutritionalPlanDate, PlanEntrenamiento, PlanNutricional, Rutina_PlanEntrenamiento, Gallery, Comida, SeguimientoNutricional
from .forms import forms
from .forms import EvaluationForm, EjercicioForm
from django.contrib.auth.forms import forms
from ProyectoGymAppAdmin.models import Entrenamiento, Suplementation, Alimentacion
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from ProyectoGymApp.models import Profile
from django.contrib import messages
from ProyectoGymApp import models as modelsg
from ProyectoGymAppAdmin import models as modelsadmin
from django.db.models import Max, IntegerField


def inicio(request):

    return render(request, "ProyectoGymAppCliente/inicio.html")


def evaluacion(request):

    form = EvaluationForm()
    current_user = get_object_or_404(User, pk=request.user.pk)

    if request.method == "POST":
        # print(request.POST['name','lastname','phone','email','height','weight','experience','objetive'])
        form = EvaluationForm(request.POST)

        if form.is_valid():
            evaluacion = Evaluation()
            evaluacion.profile = current_user.profile
            evaluacion.height = form.cleaned_data['height']
            evaluacion.weight = form.cleaned_data['weight']
            evaluacion.experience = form.cleaned_data['experience']
            evaluacion.objective = form.cleaned_data['objective']
            duracion = form.cleaned_data['duration']
            evaluacion.duration = duracion
            evaluacion.endDate = datetime.datetime.now().date() + \
                datetime.timedelta(days=duracion*30)
            evaluacion.save()
            return redirect(planes_recomendados, evaluacion.pk)
        else:
            print("Evaluacion no registrada, Intentalo de nuevo")

    context = {
        'form': form,
        'user': current_user,
    }
    return render(request, "ProyectoGymAppCliente/evaluacion.html", context)


def registroclientes(request):

    clientdata = Evaluation.objects.all()

    return render(request, "ProyectoGymApp/registroclientes.html", {"clientdata": clientdata})

# Create your views here.


def buscarejercicios(request):

    form = EjercicioForm()

    if request.method == "POST":
        form = EjercicioForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']
            muscles_involved = form.cleaned_data['muscles_involved']
            ejercicios = Ejercicio.objects.filter(
                category=category, muscles_involved=muscles_involved)
            return render(request, "ProyectoGymAppCliente/listar_ejercicios.html", {"ejercicios": ejercicios})

    return render(request, "ProyectoGymAppCliente/buscar_ejercicios.html", {"form": form})


def infosuplementacion(request):
    infsupl = Suplementation.objects.all()

    return render(request, "ProyectoGymAppCliente/infosuplementacion.html", {"infsupl": infsupl})


def informacion(request):
    inf = Alimentacion.objects.all()

    return render(request, "ProyectoGymAppCliente/informacion.html", {"inf": inf})


def articulos_entrenamiento(request):
    articulos = Entrenamiento.objects.all()
    return render(request, "ProyectoGymAppCliente/articulosEntrenamiento.html", {"articulos": articulos})


def articulo(request, pk):
    articulo = Entrenamiento.objects.get(id=pk)
    return render(request, "ProyectoGymAppCliente/articulo.html", {"articulo": articulo})


def planes_recomendados(request, pk_evaluacion):
    evaluacion = Evaluation.objects.get(pk=pk_evaluacion)
    planes_entrenamiento = PlanEntrenamiento.objects.filter(
        level=evaluacion.experience, objective=evaluacion.objective)

    if request.method == "POST":
        id_plan_entrenamiento = request.POST.get('planes_de_entrenamiento')
        plan_entrenamiento = PlanEntrenamiento.objects.get(
            id=id_plan_entrenamiento)
        evaluacion.training_plan = plan_entrenamiento
        evaluacion.save()
        return redirect('MostrarPlanEntrenamiento', id_plan_entrenamiento)

    context = {
        "planes_entrenamiento": planes_entrenamiento,
    }
    return render(request, "ProyectoGymAppCliente/escoger_plan_entrenamiento.html", context)


def mostrar_plan_entrenamiento(request, pk_plan):
    rutinas = Rutina_PlanEntrenamiento.objects.filter(
        plan_entrenamiento=pk_plan)
    plan = PlanEntrenamiento.objects.get(pk=pk_plan)

    days = [
        'Lunes',
        'Martes',
        'Miercoles',
        'Jueves',
        'Viernes',
        'Sábado',
        'Domingo'
    ]

    context = {
        "plan": plan,
        "rutinas": rutinas,
        "days": days,
        "semanas": range(1, 5),
    }
    return render(request, "ProyectoGymAppCliente/mostrar_plan_entrenamiento.html", context)


def mostrar_rutina(request, pk_plan, pk_rutina):
    rutina_ejercicios = Ejercicio_Rutina.objects.filter(rutina=pk_rutina)
    context = {
        "pk_plan": pk_plan,
        "rutina_ejercicios": rutina_ejercicios,
    }
    return render(request, "ProyectoGymAppCliente/mostrar_rutina.html", context)


def mostrarrecetas(request):

    datareceta = modelsadmin.Receta.objects.all()

    return render(request, "ProyectoGymAppCliente/mostrarrecetacliente.html", {"datareceta": datareceta})


def mostrarofertas(request):

    dataoferta = modelsg.Oferta.objects.all()

    return render(request, "ProyectoGymAppCliente/mostrarofertacliente.html", {"dataoferta": dataoferta})


def galeria(request):

    datagaleria = Gallery.objects.all()

    return render(request, "ProyectoGymAppCliente/galeria.html", {"datagaleria": datagaleria})


def uploadgaleria(request):

    if request.method == "POST":
        gall = Gallery()
        gall.title = request.POST.get('title')
        gall.description = request.POST.get('description')

        if len(request.FILES) != 0:
            gall.image = request.FILES['image']

        gall.save()
        messages.success(request, 'Foto Agregada')

    return render(request, "ProyectoGymAppCliente/uploadgaleria.html")


def editgaleria(request, pk):

    egallery = Gallery.objects.get(id=pk)
    context = {'egallery': egallery}

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(egallery.image) > 0:
                os.remove(egallery.image.path)
            egallery.image = request.FILES['image']
        egallery.title = request.POST.get('title')
        egallery.description = request.POST.get('description')
        egallery.save()
        return redirect('Galeria')

    return render(request, "ProyectoGymAppCliente/editgaleria.html", context)


def deletegaleria(request, pk):
    egallery = Gallery.objects.get(id=pk)
    if len(egallery.image) > 0:
        os.remove(egallery.image.path)
    egallery.delete()

    return redirect('Galeria')


def verificar(request):

    return render(request, "ProyectoGymAppCliente/verificar.html")


def mostrar_plan_nutricional(request, pk_plan, duracion_meses, initial_date):

    plan = PlanNutricional.objects.get(pk=pk_plan)
    initialDate = datetime.datetime.strptime(initial_date, '%Y-%m-%d').date()
    today = datetime.datetime.now().date()

    if not NutritionalPlanDate.objects.filter(planNutricional=pk_plan):
        for mes in range(1, duracion_meses+1):
            for day in range(30):
                if day == 0 and mes == 1:
                    date = initialDate
                else:
                    date = date + datetime.timedelta(days=1)

                planDate = NutritionalPlanDate()
                planDate.planNutricional = plan
                planDate.month = mes
                planDate.day = day+1
                planDate.date = date
                planDate.save()

    planDate = NutritionalPlanDate.objects.filter(planNutricional=pk_plan)

    days = [
        'Lunes',
        'Martes',
        'Miercoles',
        'Jueves',
        'Viernes',
        'Sábado',
        'Domingo'
    ]

    semanas = [
        {"nums": range(1, 8)},
        {"nums": range(8, 15)},
        {"nums": range(15, 22)},
        {"nums": range(22, 29)},
        {"nums": range(29, 31)},
    ]

    context = {
        "plan": plan,
        "plans_date": planDate,
        "days": days,
        "semanas": semanas,
        "meses": range(1, duracion_meses+1),
        "initial_date": initialDate,
        "today": today
    }

    return render(request, "ProyectoGymAppCliente/mostrar_plan_nutricional.html", context)


def mostrarPlannXdia(request, pk_plan, date):

    today = datetime.datetime.now().date()
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    comidas = Comida.objects.filter(plan_nutricional=pk_plan)

    ncomidas = comidas.order_by('-num_comida').first()

    if not SeguimientoNutricional.objects.filter(PlanNutricional=pk_plan, date=date):
        for comida in comidas:
            seguimiento = SeguimientoNutricional()
            seguimiento.PlanNutricional = comida.plan_nutricional
            seguimiento.comida = comida
            seguimiento.date = date
            seguimiento.save()

    seguimiento = SeguimientoNutricional.objects.filter(
        PlanNutricional=pk_plan, date=date)

    context = {
        "seguimiento": seguimiento,
        "num_comidas": range(1, ncomidas.num_comida+1),
        "comidas": comidas,
        "date": date,
        "today": today
    }

    return render(request, "ProyectoGymAppCliente/mostrar_plannXdia.html", context)
