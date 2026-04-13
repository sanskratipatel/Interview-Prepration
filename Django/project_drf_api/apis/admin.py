from django.contrib import admin
from .models import Students ,Employess,Comments ,Blog 
# Register your models here.

admin.site.register(Students) 
admin.site.register(Employess)  
admin.site.register(Blog) 
admin.site.register(Comments)