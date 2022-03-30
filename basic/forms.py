from django import forms

class login(forms.Form):
    phoneNo = forms.CharField(label='Your Registered Phone no', max_length=40)
    password=forms.CharField(widget = forms.PasswordInput(),label='Password', max_length=10)
