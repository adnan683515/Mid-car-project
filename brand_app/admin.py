from django.contrib import admin
from brand_app.models import Brand
# Register your models here.

class model_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Brand_name',)}
    list_display = ['Brand_name','slug']
    
admin.site.register(Brand,model_admin)