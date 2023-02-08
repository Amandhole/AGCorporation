from django.db import models

# Create your models here.
class User_Details(models.Model):
    First_Name = models.CharField(max_length=50, null=True, blank=True)
    Last_Name = models.CharField(max_length=50, blank=True, null=True)
    Username = models.CharField(max_length=50, null=True,blank=True)
    Password = models.CharField(max_length=20, null=True,blank=True)
    User_Type = models.CharField(max_length=50  ,blank=True, null=True)
    Created_Datetime = models.DateTimeField(null=True, blank=True , auto_now=True)
    
    # def __str__(self):
    #     return self.First_Name