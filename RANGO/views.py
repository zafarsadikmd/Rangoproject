from django.shortcuts import render

from django.http import HttpResponse
from RANGO.models import Register
from RANGO.models import Login_details

def home(request):
    return render(request,"index.html")
    
def index(request):
    return render(request , "index.html")

def restaurant(request):
    return render(request,"restaurant.html")

def ngo(request):
    return render(request,"ngo.html")

def donate(request):
    return render(request,"donate.html")

def volunteer(request):
    return render(request,"volunteer.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")

def login(request):
    if request.method == "POST":
        Restaurantname = request.POST.get('Rname')
        Username =request.POST.get('Uname')
        Password =request.POST.get('Passw')
        LoggedIN=Login_details(Restaurantname=Restaurantname,Username=Username,Password=Password)
        Login_details.save()
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        Restaurantname =request.POST.get('Rname')
        EmailId =request.POST.get('Email')
        address =request.POST.get('address')
        Username =request.POST.get('Username')
        Password =request.POST.get('Password')
        contact =request.POST.get('Contact')
        Registered=Register( Restaurantname=Restaurantname, EmailId=EmailId, address=address, Username=Username, Password=Password, contact=contact)
        Registered.save()
    return render(request,"register.html")



