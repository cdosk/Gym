from .models import Evaluation
from .forms import forms
from .forms import EvaluationForm
from django.contrib.auth.forms import forms
from django.shortcuts import render

def inicio(request):

        return render(request, "ProyectoGymAppCliente/inicio.html")

def evaluacion(request):

        form=EvaluationForm()

        if request.method =="POST":
                #print(request.POST['name','lastname','phone','email','height','weight','experience','objetive'])
                form = EvaluationForm(request.POST)

                if form.is_valid():
                        print("Evaluacion registrada")
                        #form.save()
                        evaluation = Evaluation()

                        evaluation.name = form.cleaned_data['name']
                        evaluation.lastname = form.cleaned_data['lastname']
                        evaluation.phone = form.cleaned_data['phone']
                        evaluation.birth = form.cleaned_data['birth']
                        evaluation.height = form.cleaned_data['height']
                        evaluation.weight = form.cleaned_data['weight']
                        evaluation.experience = form.cleaned_data['experience']
                        evaluation.objective = form.cleaned_data['objective']

                        evaluation.save()
                else:
                        print("Evaluacion no registrada, Intentalo de nuevo")
        return render(request, "ProyectoGymAppCliente/evaluacion.html",{'form':form})

def registroclientes(request):

        clientdata = Evaluation.objects.all()

        return render(request, "ProyectoGymApp/registroclientes.html", {"clientdata":clientdata})   

# Create your views here.
