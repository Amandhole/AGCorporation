
from django.urls import path
from AGCorporation_App.views import *


urlpatterns = [
    path('',Admin_Login,name='Admin_Login'),
    path('Blog_Dashboard',Blog_Dashboard,name='Blog_Dashboard'),
    path('Chats',Chats,name='Chats'),
    path('Filemanager',Filemanager,name='Filemanager'),
    path('Register',Register,name='Register'),
    path('Forget_Password',Forget_Password,name='Forget_Password'),
    path('Confirm_Email',Confirm_Email,name='Confirm_Email'),
    path('Email_Verification',Email_Verification,name='Email_Verification'),
    path('Two_Step_Verification',Two_Step_Verification,name='Two_Step_Verification'),
    path('Basic_Table',Basic_Table,name='Basic_Table'),
    path('Forms_Layout',Forms_Layout,name='Forms_Layout'),
    path('Advance_Forms',Advance_Forms,name='Advance_Forms'),
    path('Form_Upload',Form_Upload,name='Form_Upload'),
    path('Form_Wizard',Form_Wizard,name='Form_Wizard'),
    path('Form_Mask',Form_Mask,name='Form_Mask'),
    path('Saas_Dashboard',Saas_Dashboard,name='Saas_Dashboard'),
    path('Crypto_Dashboard',Crypto_Dashboard,name='Crypto_Dashboard'),
    # path('Data_Table',Data_Table,name='Data_Table'),
    path('Horizontal_Menu',Horizontal_Menu,name='Horizontal_Menu')
]