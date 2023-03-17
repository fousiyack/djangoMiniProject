from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2500)
class Offers(models.Model):
    code=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    discount=models.FloatField()    
    
# Create your models here.
class register(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
class Login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=50)    


