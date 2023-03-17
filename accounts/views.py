from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Product
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from . forms import ProductForm

def productList(request):
    product=Product.objects.all()
    return render(request,'products.html',{'products':product})

def newProduct(request):
     # form from forms.py
        if request.method=='POST':
            form=ProductForm(request.POST,request.FILES)
    #    if form.is_valid:
            #  product = Product.objects.create(
            #     name=form.cleaned_data['name'],
            #     price=form.cleaned_data['price'],
            #     stock=form.cleaned_data['stock'],
            #     image=form.cleaned_data['image']
            
            
            # )
            name = "car"
            price ="20000"
            stock = "500"
            image =""
            # product = Product.objects.create(
            #     name=name,
            #     stock=stock,
            #     price=price,
            #     image=image)
            form.save()
            return redirect('products.html')
        else:
         form=ProductForm()
        return render(request,'productsAdd.html',{'form':form})       

def register(request):
   
    if request.method=='POST':
    
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:  
           if User.objects.filter(username=username).exists(): 
               messages.info(request,'Username Taken')
               return redirect('register')
           elif User.objects.filter(email=email).exists(): 
               messages.info(request,'Email Taken')
               return redirect('register')
           else:
               user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
               user.save()
               messages.info(request,'User created')
               return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
         
    else:
        return render(request,'register.html')    
    
    

def login(request):   
  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('userHome')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:  
            
        return render(request,'login.html')   
    
    
    
    
    
    
    
def login1(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'userHome.html')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login1')
    else:
       return render(request,'login.html')
   
@never_cache
def userHome(request):
    if 'username' in request.session:
        return render(request,'userHome.html')
    return render(request,'login.html')


def logout(request):
    if 'username' in request.session:
        request.session.flush()
        auth.logout(request)
    return redirect('login')    




