from django.db import models

class Evaluation(models.Model):

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    birth = models.DateField()
    height = models.DecimalField(max_digits=10, decimal_places=4)
    weight = models.DecimalField(max_digits=10, decimal_places=4)
    experience = models.CharField(max_length=50)
    objective = models.CharField(max_length=50)
