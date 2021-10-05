from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from .forms import CreateUserForm
from .models import SportProduct, Trainer
from ProyectoGymAppCliente.models import Evaluation

# Create your views here.

def inicio(request):

        return render(request, "ProyectoGymApp/inicio.html")

def entrenadores(request):

        if request.method == "POST":
                trainer = Trainer()
                trainer.name = request.POST.get('name')
                trainer.lastname = request.POST.get('lastname')
                trainer.occupation = request.POST.get('occupation')
                trainer.phone = request.POST.get('phone')
                trainer.days = request.POST.get('days')
                trainer.turn = request.POST.get('turn')
                if len(request.FILES) != 0:
                        trainer.image = request.FILES['image']
                trainer.save()
                messages.success(request, 'Agregado correctamente')
                
        return render(request, "ProyectoGymApp/entrenadores.html")

def comunidad(request):

        return render(request, "ProyectoGymApp/comunidad.html")   

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

        context = {'form' : form}
        return render(request, "ProyectoGymApp/registrar.html", context)

def login(request):
        
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username = username, password = password)

                if user is not None:
                        auth_login(request, user)
                        return redirect('Evaluacion')
                else:
                        messages.info(request, 'Username o Password incorrecto')

        context = {}

        return render(request, "ProyectoGymApp/login.html", context)

def registroclientes(request):

        clientdata = Evaluation.objects.all()

        return render(request, "ProyectoGymApp/registroclientes.html", {"clientdata":clientdata})   
