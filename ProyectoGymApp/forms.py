from django import forms
from django.db import models
from django.db.models.fields import CharField
from django.forms import ModelForm, fields
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms

from ProyectoGymApp.models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=20, label="Nombre: ")
    last_name = forms.CharField(max_length=20, label="Apellidos: ")
    email = forms.EmailField(max_length=50, label="Email: ")
    phone_number = forms.CharField(max_length=15, label='Cel:')
