from django.contrib import admin
from .models import Students
from django.contrib import admin
# Register your models here.

@admin.register(Students)
class StudentAdminClass(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'email' , 'password')
