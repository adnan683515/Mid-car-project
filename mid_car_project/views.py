from django.shortcuts import render,redirect
from brand_app import models
from car_app.models import car


def home(request,brand_name_slug = None):
    brand_data = models.Brand.objects.all()
    car_data = car.objects.all()
    
    if brand_name_slug is not None:
        brand = models.Brand.objects.get(slug = brand_name_slug)
        car_data = car.objects.filter(Brand=brand)
        
    return render(request,'home.html',{"data":brand_data,'car_data':car_data,})
   



