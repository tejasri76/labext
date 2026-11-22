from django.shortcuts import render

# Create your views here.

def home(request):
    name='tejasri'
    context={
        'name':name,
        'roll_no':'A3'
    }

    return render(request,'home.html',context)
def user_login(request):
    
    return render(request,'login.html')
def user_register(request):
    return render(request,'register.html')