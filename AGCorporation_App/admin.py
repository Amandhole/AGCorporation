from django.contrib import admin
from .models import *
# Register your models here.
class User_Details_Class(admin.ModelAdmin):
	list_display = ('id', 'First_Name','Last_Name','Username','Password','User_Type','Created_Datetime')
admin.site.register(User_Details, User_Details_Class)