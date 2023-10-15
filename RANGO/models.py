from django.db import models

# Create your models here.
class Register(models.Model):
    Restaurantname=models.CharField(max_length=150)
    EmailId=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    Username=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    contact=models.CharField(max_length=12)
    def __str__(self):
        return self.Restaurantname


class Login_details(models.Model):
    Restaurantname=models.CharField(max_length=200)
    Username=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    


    
     