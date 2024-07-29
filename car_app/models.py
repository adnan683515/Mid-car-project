from django.db import models
from brand_app.models import Brand
from django.contrib.auth.models import User
# Create your models here.
class car(models.Model):
    Title = models.CharField(max_length=300)
    price = models.CharField(max_length=20)
    Description = models.TextField(max_length=1000)
    quantity = models.IntegerField(blank=True,null=True)
    image = models.ImageField(upload_to = 'uploads/', null = True , blank = True)
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True,null=True)
    
    
    def __str__(self):
        return self.Title
    
class Buy(models.Model):
    buy_user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(car,on_delete=models.CASCADE)
    

class comment(models.Model):
    car = models.ForeignKey(car,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comments by{self.name}'
    
    

    
    
    
    
    
    