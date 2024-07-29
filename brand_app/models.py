from django.db import models

# Create your models here.
class Brand(models.Model):
    Brand_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True,blank=True,unique=True)
    
    
    def __str__(self):
        return self.Brand_name
    