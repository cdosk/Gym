from django.db import models
from django.contrib.auth.models import User
import datetime
import os


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class SportProduct(models.Model):
    nameproduct = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.FloatField()
    brand = models.CharField(max_length=50)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)


class Oferta(models.Model):
    title = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    price = models.FloatField()
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)


class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        default='https://icons-for-free.com/iconfiles/png/512/profile+profile+page+user+icon-1320186864367220794.png',
        upload_to='profile-pictures',
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username


class Trainer(models.Model):
    GENDER = [('M', 'Masculino'), ('F', 'Femenino')]
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER)
    mobileNumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, null=True)
    picture = models.ImageField(
        default='https://icons-for-free.com/iconfiles/png/512/profile+profile+page+user+icon-1320186864367220794.png',
        upload_to='profile-pictures/entrenadores',
    )

    def __str__(self):
        return self.name


class Nutricionist(models.Model):
    GENDER = [('M', 'Masculino'), ('F', 'Femenino')]
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER)
    mobileNumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, null=True)
    picture = models.ImageField(
        default='https://icons-for-free.com/iconfiles/png/512/profile+profile+page+user+icon-1320186864367220794.png',
        upload_to='profile-pictures/nutricionistas',
    )

    def __str__(self):
        return self.name
