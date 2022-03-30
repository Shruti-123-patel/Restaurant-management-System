from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.http.response import HttpResponse
from basic.models import customer
from basic.models import registration
# from basic.forms import login
from basic.models import foodForm





# Create your views here.

def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def feature(request):
    return render(request,'feature.html')

def menu(request):
    return render(request,'menu.html')

def single(request):
    return render(request,'single.html')

def team(request):
    return render(request,'team.html')

def addFood(request):
    context={}
    form=foodForm
    context['form']=form
    print("ha")
    return render(request,"Form.html",context)

def addFoodDB(request):
    form=foodForm(request.POST)
    
    print(form)
    if form.is_valid():
        print("na")
        form.save()
    else:
        print("na!!")
    return render(request,"Form.html")

def register(request):

    if(request.method=="POST"):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if(User.objects.filter(username=username).exists()):
                messages.success(request,'User Name is not available.')
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.success(request,'Email id is already taken.') 
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User Created.')
        else:
            messages.success(request,'Password not matching.') 
            return redirect('register')
        return redirect('/')

    else:
        return render(request,"Form.html")

def login_(request):
    context={}
    if request.method=='POST':
        form_=login(request.POST)
        if form_.is_valid():
           cust=customer.objects.get(pk=request.POST['email'])
           if cust.password==request.POST['password']:
               return render(request,"index.html",context)
           else:
               return render(request,"Form.html",context)
    else:
        form_=login()
        print(form_)
        context['form']=form_
        print("ha")
        return render(request,"Form.html",context)