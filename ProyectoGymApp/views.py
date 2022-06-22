from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.contrib.auth.models import User

from ProyectoGymAppCliente.views import evaluacion
from .forms import CreateUserForm, ProfileForm
from .models import Profile, SportProduct, Oferta
from ProyectoGymAppCliente.models import Evaluation, PlanNutricional, PlanEntrenamiento
from ProyectoGymApp.models import Trainer, Nutricionist
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Max
import os


# Create your views here.


def inicio(request):
    if request.method == "POST":

        subject = request.POST["affair"]
        message = request.POST["message"] + " " + request.POST["email"] + \
            " " + request.POST["fullname"] + " " + request.POST["phone"]
        email_from = settings.EMAIL_HOST_USER
        recepient_list = ["72763597@continental.edu.pe"]
        send_mail(subject, message, email_from, recepient_list)

        return render(request, "ProyectoGymApp/gracias.html")

    return render(request, "ProyectoGymApp/inicio.html")


def entrenadores(request):
    entrenadores = Trainer.objects.all()
    nutricionistas = Nutricionist.objects.all()
    context = {
        "entrenadores": entrenadores,
        "nutricionistas": nutricionistas
    }
    return render(request, "ProyectoGymApp/entrenadores.html", context)


def oferta(request):

    if request.method == "POST":
        of = Oferta()
        of.title = request.POST.get('title')
        of.startDate = request.POST.get('startDate')
        of.endDate = request.POST.get('endDate')
        of.price = request.POST.get('price')
        of.description = request.POST.get('description')

        if len(request.FILES) != 0:
            of.image = request.FILES['image']

        of.save()
        messages.success(request, 'Oferta Agregada')

    return render(request, "ProyectoGymApp/oferta.html")


def tienda(request):
    if request.method == "POST":
        prod = SportProduct()
        prod.nameproduct = request.POST.get('name')
        prod.category = request.POST.get('category')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')
        prod.brand = request.POST.get('brand')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, 'Producto agregado')

    return render(request, "ProyectoGymApp/tienda.html")


def registrar(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta creada, BIENVENIDO ' + user)

            return redirect('Login')

    context = {'form': form}
    return render(request, "ProyectoGymApp/registrar.html", context)


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('Evaluacion')
        else:
            messages.info(request, 'Username o Password incorrecto')

    context = {}

    return render(request, "ProyectoGymApp/login.html", context)


def registroclientes(request):

    clientdata = Evaluation.objects.all()

    return render(request, "ProyectoGymApp/registroclientes.html", {"clientdata": clientdata})


def mostrarofertas(request):

    dataoferta = Oferta.objects.all()

    return render(request, "ProyectoGymApp/mostraroferta.html", {"dataoferta": dataoferta})


def editoferta(request, pk):

    eoferta = Oferta.objects.get(id=pk)
    context = {'eoferta': eoferta}

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(eoferta.image) > 0:
                os.remove(eoferta.image.path)
            eoferta.image = request.FILES['image']
        eoferta.title = request.POST.get('title')
        eoferta.startDate = request.POST.get('startDate')
        eoferta.endDate = request.POST.get('endDate')
        eoferta.price = request.POST.get('price')
        eoferta.description = request.POST.get('description')
        eoferta.save()
        return redirect('Mostraroferta')

    return render(request, "ProyectoGymApp/editoferta.html", context)


def deleteoferta(request, pk):
    eoferta = Oferta.objects.get(id=pk)
    if len(eoferta.image) > 0:
        os.remove(eoferta.image.path)
    eoferta.delete()
    messages.success(request, "Oferta Eliminado")

    return redirect('Mostraroferta')


def profileview(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    perfil = Profile.objects.get(user=current_user.pk)
    evaluacion = Evaluation.objects.filter(
        profile=perfil).aggregate(Max('date'))
    evaluacion = Evaluation.objects.get(date=evaluacion['date__max'])
    form = ProfileForm()

    if request.method == "POST":
        current_user.first_name = request.POST.get('first_name')
        current_user.last_name = request.POST.get('last_name')
        current_user.email = request.POST.get('email')
        current_user.profile.phone_number = request.POST.get('phone_number')
        current_user.save()
        messages.success(request, "GUARDADO")

    context = {
        "form": form,
        "user": current_user,
        "evaluacion": evaluacion,
        "initialdate": str(evaluacion.date.date())
    }

    return render(request, "ProyectoGymApp/profile.html", context)
