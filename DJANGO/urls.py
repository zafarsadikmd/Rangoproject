"""
URL configuration for DJANGO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RANGO.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="Home"),
    path('index.html',index,name="Home"),
    path('restaurant.html',restaurant,name="restaurant"),
    path('ngo.html',ngo,name="ngo"),
    path('volunteer.html',volunteer,name="volunteer"),
    path('donate.html',donate,name="donate"),
    path('aboutus.html',aboutus,name="aboutus"),
    path('contactus.html',contactus,name="contactus"),
    path('login.html',login,name="login"),
    path('register.html',register,name="register")

]
