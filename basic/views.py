from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponse
from RestaurantManagementSystem.basic.models import customer
from basic.models import registration
from basic.forms import login

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
    context={}
    form_=registration(request.POST or None)
    if form_.is_valid():
        print("na")
        form_.save()
    else:
        print("na!!")
    context['form']=form_
    print("ha")
    return render(request,"Form.html",context)

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