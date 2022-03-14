# import email
from django import forms
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.forms import ModelForm,widgets
from multiselectfield import MultiSelectField

class customer(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    password=models.CharField(max_length=10) 
    phoneNo=models.IntegerField(primary_key=True) 
    email=models.EmailField(max_length=30)

class registration(forms.ModelForm):
    class Meta:
        model = customer
        fields = "__all__"
        widget={
            'fname' : forms.TextInput(attrs={'class':'form-control'}),
            'lname': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'phoneNo': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }

class worker(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    phone_no=models.IntegerField()
    email=models.EmailField(max_length=30)
    post=models.CharField(max_length=10)


class foodItems(models.Model):
    CustomizationChoice=(
        ('Cheese','Cheese'),
        ('Butter','Butter'),
        ('Onion toppings','Onion toppings'),
        ('mayonnaise','mayonnaise'),
        ('spicy','spicy'),
        ('extra chilly spicy','extra chilly spicy')
    )
    typeChoice=(
        ('Veg','Veg'),
        ('Non-veg','Non-veg'),
    )
    name=models.CharField(max_length=50) 
    type=models.CharField(max_length=20,choices=typeChoice,blank=False,default='Veg') 
    price=models.IntegerField() 
    customization=MultiSelectField(choices=CustomizationChoice,blank=False)
    description=models.CharField(max_length=30)
    image=models.ImageField(upload_to='uploadedImages')

class foodForm(forms.ModelForm):
    class Meta:
        model = foodItems
        fields = "__all__"
        widget={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'customization': forms.CheckboxSelectMultiple,
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }

class feedback(models.Model):
    cid = models.ForeignKey (customer, on_delete=models.CASCADE)
    foodid = models.ForeignKey(foodItems, on_delete=models.CASCADE)
    ratings = models.IntegerField()
    
class orders(models.Model):
    cid=models.ForeignKey(customer, on_delete=models.CASCADE)
    noOfFood=models.IntegerField() 
    totalCost=models.IntegerField() 
    date=models.DateTimeField(auto_now_add = True)
    address=models.TextField()
    paymentStatus=models.BooleanField()

class tableReservation(models.Model):
    cid=models.ForeignKey(customer, on_delete=models.CASCADE)
    totalTables=models.IntegerField()
    cost = models.IntegerField()
    date = models.DateTimeField()
    paymentStatus = models.BooleanField()

class orderood(models.Model):
    CustomizationChoice=(
        ('Cheese','Cheese'),
        ('Butter','Butter'),
        ('Onion toppings','Onion toppings'),
        ('mayonnaise','mayonnaise'),
        ('spicy','spicy'),
        ('extra chilly spicy','extra chilly spicy')
    )
    oid=models.ForeignKey(orders, on_delete=models.CASCADE)
    foodid=models.ForeignKey(customer, on_delete=models.CASCADE)
    quantity=models.IntegerField() 
    pricePerItem=models.IntegerField() 
    custmizations=models.CharField(max_length=60,choices=CustomizationChoice)
    totalPrice=models.IntegerField() 

class table(models.Model):
    noOfTables = models.IntegerField()
    availableTables = models.IntegerField()
    bookedTables = models.IntegerField()

class dealsAndOffers(models.Model):
    offerCode = models.CharField(max_length=8)
    foodid = models.ForeignKey(foodItems, on_delete=models.CASCADE)
    discount = models.CharField(max_length=5)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

class mannualOrder(models.Model):
    customerFname = models.CharField(max_length=100)
    customerLname = models.CharField(max_length=100)
    foodid = models.ForeignKey(foodItems, on_delete=models.CASCADE)
    quantity = models.IntegerField()

