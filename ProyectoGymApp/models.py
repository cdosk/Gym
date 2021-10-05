from django.db import models
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
    image = models.ImageField(upload_to = filepath, null=True, blank=True)

class Trainer(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    days = models.CharField(max_length=50)
    turn = models.CharField(max_length=50)
    image = models.ImageField(upload_to = filepath, null=True, blank=True)