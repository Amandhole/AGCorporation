from django.shortcuts import render

# Create your views here.
def Admin_Login(request):
    return render(request,'admin_login.html')

def Blog_Dashboard(request):
    return render(request,'dashboard.html')    

def Saas_Dashboard(request):
    return render(request,'dashboard_saas.html')


def Crypto_Dashboard(request):
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