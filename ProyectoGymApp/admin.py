from django.contrib import admin
from .models import Nutricionist, Profile, SportProduct, Trainer

# Register your models here.
admin.site.register(SportProduct)
admin.site.register(Profile)
admin.site.register(Trainer)
admin.site.register(Nutricionist)
