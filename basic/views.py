import datetime
from hashlib import new
from http.client import HTTPResponse
from pickle import FALSE
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponse
from basic.models import foodItems, orderood, orders, tableReservation
from basic.models import customer
from basic.models import registration
from basic.forms import login
from basic.models import foodForm
from RestaurantManagementSystem import settings


# Create your views here.

def home(request):
    return render(request,'index.html')

def index(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        link="profile"
        name=cust.fname+cust.lname
    return render(request,'index.html',{'name':name,'link':link})
    

def booking(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname
        link="profile"
    return render(request,'booking.html',{'name':name,'link':link})

def contact(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname
        link="profile"
    return render(request,'contact.html',{'name':name,'link':link})

def menu(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname
        link="profile" 
    return render(request,'menu.html',{'name':name,'link':link})

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
    context['heading']="Add Food Items To The Menu"
    context['button']="Add Food"
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
    context['heading']="Register Yourself"
    context['button']="Register Yourself"
    print("ha")
    return render(request,"Form.html",context)

def login_(request):
    context={}
    context['heading']="Login Yourself"
    context['button']="Login Yourself"
    if request.method=='POST':
        form_=login(request.POST)
        if form_.is_valid():
           if request.POST['phoneNo']=="111" and request.POST['password']=="000":
               cust=customer.objects.get(pk=request.POST['phoneNo'])
               request.session['name'] =cust.uname
               request.session['id'] = cust.phoneNo
               cart={}
               request.session['cart'] = cart
               return render(request,"index.html",context)
           cust=customer.objects.get(pk=request.POST['phoneNo'])
           if cust.password==request.POST['password']:
               request.session['name'] =cust.uname
               request.session['id'] =cust.phoneNo
               cart={}
               request.session['cart'] = cart
               return render(request,"index.html",context)
           else:
               return render(request,"Form.html",context)
    else:
        form_=login()
        print(form_)
        context['form']=form_
        context['heading']="LogIn To Website"
        print("ha")
        return render(request,"Form.html",context)

def order_(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname
        link="profile" 
    foodItem=foodItems.objects.all()
    context={}
    context["food"]=foodItem
    context["name"]=name
    context["link"]=link
    return render(request,"OrderPage.html",context)

def menu(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname
        link="profile" 
    dests = foodItems.objects.all()
    flag=[False]*100
    for d in dests:
        flag[d.ide]=False

    # print(flag[d.ide])
    request.session['flag']=flag
    return render(request,'menu.html',{'dests':dests,'media_url':settings.MEDIA_URL,'flags':flag,'name':name,'link':link})

def cartView(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname
        link="profile"
    price=0
    cart=request.session['cart']
    print(cart)
    cartObj=[]
    for i in cart:
        objGet=foodItems.objects.get(pk=i)
        price+=int(objGet.price)*int(cart[i])
        cartObj.append({'obj':objGet,'qua':cart[i]})
    return render(request,'viewCart.html',{'cart':cartObj,'amount':price,'name':name,'link':link})

def cart(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname
        link="profile" 
    id=request.GET['id']
    print("hello")
    flag=request.session['flag']
    # flag[id]=True
    request.session['flag']=flag
    print(flag) 
    cart_=request.session.get('cart')
    print(cart_)
    cart_[str(id)]=1
    request.session['cart']=cart_
    dests = foodItems.objects.all()
    return render(request,'menu.html',{'dests':dests,'media_url':settings.MEDIA_URL,'flags':flag,'name':name,'link':link})
    
def plus(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname
        link="profile"  
    cart=request.session['cart']
    price=0
    # print(cart)
    pid=request.GET['id']
    cartObj=[]
    for i in cart:
        objGet=foodItems.objects.get(pk=i)
        price+=int(objGet.price)*int(cart[i])
        if pid==i:
            price+=objGet.price
            cart[i]+=1
        cartObj.append({'obj':objGet,'qua':cart[i]})
    request.session['cart']=cart
    return render(request,'viewCart.html',{'cart':cartObj,'amount':price,'name':name,'link':link})

def minus(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname 
        link="profile"
    price=0
    cart=request.session['cart']
    # print(cart)
    pid=request.GET['id']
    cartObj=[]
    for i in cart:
        objGet=foodItems.objects.get(pk=i)
        price+=int(objGet.price)*int(cart[i])
        if pid==i:
            price-=objGet.price
            cart[i]-=1
        if cart[i]!=0:
            cartObj.append({'obj':objGet,'qua':cart[i]})
        # else:
        #     cart.pop(i)
    request.session['cart']=cart
    return render(request,'viewCart.html',{'cart':cartObj,'amount':price,'name':name,'link':link})

def checkout(request):
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname 
        link="profile" 
    price=request.GET['price']
    return render(request,'Payment.html',{'amount':price,'name':name,'link':link})

def emptyCart(request):
    c={}
    name="Login"
    link="login"
    if(request.session['id']):
        cust=customer.objects.get(pk=request.session['id'])
        name=cust.fname+cust.lname 
        link="profile" 
    request.session['cart']=c
    return render(request,'viewCart.html',{'amount':0,'name':name,'link':link})

def orderDone(request):

    amount=0
    cart=request.session['cart']
    cid=request.session['id']
    cust=customer.objects.get(pk=cid)
    name=cust.fname+" "+cust.lname
    link="profile"
    # print(cart)
    cartObj=[]
    for i in cart:
        objGet=foodItems.objects.get(pk=i)
        amount+=int(objGet.price)*int(cart[i])
        cartObj.append({'obj':objGet,'qua':cart[i]})
    details={}
    details['street']=request.POST['street']
    details['city']=request.POST['city']
    details['state']=request.POST['state']
    details['nameOnBill']=cust.fname+" "+cust.lname
    details['pincode']=request.POST['pincode']
    details['date']=datetime.datetime.now().time()
   
    orderObj=orders()
    orderObj.cid=cust
    orderObj.address=details['street']+details['city']+details['state']
    orderObj.date=datetime.datetime.now().time()
    orderObj.noOfFood=len(cart)
    orderObj.paymentStatus=True
    orderObj.totalCost=amount
    orderObj.save()
    details['orderId']=orderObj.pk

    for i in cart:
        objGet=foodItems.objects.get(pk=i)
        orderfood=orderood()
        orderfood.oid=orderObj
        orderfood.name=objGet.name
        orderfood.foodid=objGet
        orderfood.quantity= cart[i]
        orderfood.pricePerItem=objGet.price
        orderfood.totalPrice= cart[i]*objGet.price
        orderfood.save()
    c={}
    request.session['cart']=c
    return render(request,'orderDone.html',{'obj':details,'cart':cartObj,'amount':amount,'name':name,'link':link})


def profile(request):
    cid=request.session['id']
    cust=customer.objects.get(pk=cid)
    name=cust.fname+" "+cust.lname
    link="profile"
    return render(request,'profile.html',{'name':name,'cust':cust,'link':link})

def updateProfile(request):
    cid=request.session['id']
    cust=customer.objects.get(pk=cid)
    cust.fname=request.POST['fname']
    cust.lname=request.POST['lname']
    cust.uname=request.POST['uname']
    cust.password=request.POST['password']
    cust.email=request.POST['email']
    cust.save()
    name=cust.fname+cust.lname
    link="profile"
    return render(request,'profile.html',{'name':name,'cust':cust,'link':link})

def viewOrder(request):
    cid=request.session['id']
    cust=customer.objects.get(pk=cid)
    name=cust.fname+cust.lname
    link="profile"
    order=orders.objects.filter(cid=cust.phoneNo)
    orderfood=[]
    for o in order:
        print(o.pk)
        food=orderood.objects.filter(oid=o.pk)
        print(food)
        orderfood.append({"orderObj":o,"food_":food})
    return render(request,'viewOrder.html',{'name':name,'cust':cust,'link':link,'order':order,'orderfood':orderfood})

def adminHome_(request):
    cat1 = foodItems.objects.filter(category=1)
    cat2 = foodItems.objects.filter(category=2)
    cat3 = foodItems.objects.filter(category=3)
    return render(request,'adminHome.html',{'cat1':cat1,'cat2':cat2,'cat3':cat3})

def updateItem(request):
    obj=foodItems.objects.get(ide=request.GET['fid'])
    return render(request,'updateFood.html',{'obj':obj})

def updateFood(request):
    id=request.POST['id']
    food=foodItems.objects.get(pk=id)
    food.name=request.POST['name']
    food.category=request.POST['category']
    food.type=request.POST['type']
    food.price=request.POST['price']
    food.description=request.POST['description']
    food.save()
    cat1 = foodItems.objects.filter(category=1)
    cat2 = foodItems.objects.filter(category=2)
    cat3 = foodItems.objects.filter(category=3)
    return render(request,'adminHome.html',{'cat1':cat1,'cat2':cat2,'cat3':cat3})


def removeItem(request):
    id=request.GET['fid']
    foodItems.objects.get(pk=id).delete()
    cat1 = foodItems.objects.filter(category=1)
    cat2 = foodItems.objects.filter(category=2)
    cat3 = foodItems.objects.filter(category=3)
    return render(request,'adminHome.html',{'cat1':cat1,'cat2':cat2,'cat3':cat3})

def bookTable(request):
    # context={}
    # form_=registration(request.POST or None)
    # if form_.is_valid():
    #     print("na")
    #     form_.save()
    # else:
    #     print("na!!")
    # context['form']=form_
    # print("ha")
    # return render(request,"Form.html",context)
    # name = request.POST['name']
    # email = request.POST['email']
    # mobile = request.POST['mobile']
    # date = request.POST['date']
    # time = request.POST['time']
    # no_of_tables = request.POST['no_of_table']
    bt = tableReservation()
    bt.name = request.POST['name']
    bt.email = request.POST['email']
    bt.mobile = request.POST['mobile']
    bt.date = request.POST['date']
    bt.time = request.POST['time']
    bt.no_of_tabels = request.POST['no_of_tabels']
    bt.id = request.POST['id']
    bt.save()
    return render(request,"index.html")