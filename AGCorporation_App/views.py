from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
import traceback
from django.http import JsonResponse
import json
from .models import *
# Create your views here.
@csrf_exempt

##############Login Functionality for admin , staf , service
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    # user_types = Admin ,Staf,Service
    session_id = request.session.get('user_id')
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode('utf-8'))
            username = data['username']
            password = data['password']
            user_type =data['user_type']
            print(user_type)
            
            if user_type == "Admin" or user_type =='admin':
                if User_Details.objects.filter(Username=username, Password=password).exists():
                    admin_obj = User_Details.objects.get(Username=username, Password=password,User_Type=user_type)
                    request.session['user_id'] = str(admin_obj.id)
                    send_data = {"status": 1, "msg": "Admin Login succesfully"}
                else:
                    send_data = {"status": 0, "msg": "Invalid Credential"}


            elif user_type == "Staf":
                if User_Details.objects.filter(Username=username, Password=password).exists():
                    staf_obj = User_Details.objects.get(Username=username, Password=password,User_Type=user_type)
                    request.session['user_id'] = str(staf_obj.id)
                    send_data = {"status": 2, "msg": "Staf Login succesfully"}
                else:
                    send_data = {"status": 0, "msg": "Invalid Credential"}
            

            elif user_type == "Service":
                if User_Details.objects.filter(Username=username, Password=password).exists():
                    staf_obj = User_Details.objects.get(Username=username, Password=password,User_Type=user_type)
                    request.session['user_id'] = str(staf_obj.id)
                    send_data = {"status": 3, "msg": "Staf Login succesfully"}
                else:
                    send_data = {"status": 0, "msg": "Invalid Credential"}
        else:
            return render(request,'login.html')
    except:
        print(traceback.format_exc())
        send_data = {'status':0,'msg':'Request is not post','error':traceback.format_exc()}

    return JsonResponse(send_data)

    


def Admin_Dashboard(request):
    return render(request,'dashboard_crypto.html')

def Chats(request):
    return render(request,'chat.html')

def Filemanager(request):
    return render(request,'filemanager.html')

def Register(request):
    return render(request,'register.html')

def Forget_Password(request):
    return render(request,'forget_password.html')

 
def Confirm_Email(request):
    return render(request,'confirm_emal.html')   

def Email_Verification(request):
    return render(request,'email_verification.html')

def Two_Step_Verification(request):
    return render(request,'two_step_verification.html')

def Basic_Table(request):
    return render(request,'basic_table.html')


# def Data_Table(request):
#     return render(request,'data_table.html') ,

def Forms_Layout(request):
    return render(request,'form-layouts.html')   


def Advance_Forms(request):
    return render(request,'form-advanced.html')   

def Form_Upload(request):
    return render(request,'form-uploads.html')

def Form_Wizard(request):
    return render(request,'form_wizard.html')


def Form_Mask(request):
    return render(request,'form_mask.html')      

def Horizontal_Menu(request):
    return render(request,'horizontal_menu.html')