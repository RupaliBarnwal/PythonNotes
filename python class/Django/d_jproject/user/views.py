from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views
from .forms import *
# Create your views here.
def index(request):
    return render(request,"nav.html")
    #it will go to the path you have defined in settings.py file and will find the page and return it
    #return HttpResponse("User app")

def home(request):
    return HttpResponse("Welcome to my user app home")

def myhome(request):
    return render(request,"faltu.html")

def login(request):
    form = Login()
    return render(request,"login.html",{'form':form})

def afterlogin(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid(): #validation
            email = form.cleaned_data['email']
            passwd = form.cleaned_data['password']
            return HttpResponse(f"{email}:{passwd}")
        else:
            error = "Invalid Form"
            form = Login()
            return render(request,"login.html",{'form':form,"error":error})
    else:
        return redirect("/user/login")
    
def signup(request):
    form = Signup()
    return render(request,"signup.html",{'form':form})
