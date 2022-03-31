from hashlib import new
from http.client import HTTPResponse
from pickle import FALSE
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponse
from basic.models import foodItems
from basic.models import customer
from basic.models import registration
from basic.forms import login
from basic.models import foodForm
from RestaurantManagementSystem import settings


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
    form_=foodForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
         new.image = request.FILES.get('image')
    if form_.is_valid():
        print("na")
        form_.save()
    else:
        print("na!!")
    context['form']=form_
    return render(request,"Form.html",context)

# def addFoodDB(request):
#     form=foodForm(request.POST)
    
#     print(form)
#     if form.is_valid():
#         print("na")
#         form.save()
#     else:
#         print("na!!")
#     return render(request,"Form.html")

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
           cust=customer.objects.get(pk=request.POST['phoneNo'])
           if cust.password==request.POST['password']:
               request.session['name'] =cust.uname
               cart={1:"None"}
               request.session['cart'] = cart
               return render(request,"index.html",context)
           else:
               return render(request,"Form.html",context)
    else:
        form_=login()
        print(form_)
        context['form']=form_
        print("ha")
        return render(request,"Form.html",context)

def order_(request):
    foodItem=foodItems.objects.all()
    context={}
    context["food"]=foodItem
    return render(request,"OrderPage.html",context)

def menu(request):
    dests = foodItems.objects.all()
    flag=[False,False,False]
    for d in dests:
        flag[d.ide]=False

    # print(flag[d.ide])
    request.session['flag']=flag
    return render(request,'menu.html',{'dests':dests,'media_url':settings.MEDIA_URL,'flags':flag})

def cart(request):
    id=request.GET['id']
    print("hello")
    flag=request.session['flag']
    flag[id]=True
    request.session['flag']=flag
    print(flag) 
    cart_=request.session.get('cart')
    print(cart_)
    cart_[str(id)]=1
    request.session['cart']=cart_
    dests = foodItems.objects.all()
    return render(request,'menu.html',{'dests':dests,'media_url':settings.MEDIA_URL,'flags':flag})
    