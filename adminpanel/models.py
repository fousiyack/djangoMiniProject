from django.db import models



    



class AdminLogin(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=50)    

class Adminregister(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)