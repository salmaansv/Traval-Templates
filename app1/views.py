from django.shortcuts import render
from .models import place,self,myuser
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
def home(request):
    p=place.objects.all()
    t=self.objects.all()
    return render(request,'home.html',{'p':p,'t':t})

def register(request):
    if(request.method=="POST"):
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        place=request.POST['place']
        phone=request.POST['phone']
        s=myuser.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password,place=place,phone=phone)
        s.save()
        return home(request)
    return render(request,'register.html')

def user_login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,"Invalid user")

    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return user_login(request)