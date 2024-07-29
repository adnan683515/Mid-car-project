from django.contrib import admin
from car_app import models
# Register your models here.
admin.site.register(models.car)
admin.site.register(models.Buy)
admin.site.register(models.comment)