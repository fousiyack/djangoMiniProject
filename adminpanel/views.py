from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import UpdateForm
from django.views.decorators.cache import cache_control
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.cache import never_cache


def adminlogin(request):
    if 'username' in request.session:
        return redirect('adminHome')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
           if user.is_superuser: 
             request.session['username']=username
             auth.login(request,user)
             return redirect('adminHome')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('adminLogin')
    else:    
        messages.info(request,'You are not admin')
        return render(request,'adminlogin.html')   

@never_cache
def adminHome(request):
  if request.user.is_superuser:
    if 'username'in request.session:
        users=User.objects.all()
        dict_obj ={
        'users':users 
        }
        return render(request,'adminHome.html',dict_obj)   
  return redirect('adminLogin')


# @user_passes_test(lambda u: u.username.is_super_user)
def delete_data(request,id):
  
      if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('adminHome')
    


def update_data(request,id):
    if request.method == 'POST':
        editData =User.objects.get(pk=id)
        newData = UpdateForm(request.POST,instance=editData)
        if newData.is_valid():
          newData.save()
          return redirect('adminHome')
    else:
        editData = User.objects.get(pk=id)
        newData = UpdateForm(instance=editData)
    return render(request,'updatedata.html',{'form':newData,'id':id})

def createUser(request):
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
               return redirect('createUser')
           elif User.objects.filter(email=email).exists(): 
               messages.info(request,'Email Taken')
               return redirect('createUser')
           else:
               user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
               user.save()
               return redirect('adminHome')
        else:
            messages.info(request,'Password not matching')
            return redirect('createUser')
         
     else:
        return render(request,'createUser.html')  

def adminLogout(request):
    if 'username' in request.session:
        request.session.flush()
    auth.logout(request)
    return redirect('adminLogin')



def search_data(request): 
    searched=request.GET['search']
    # searchnames=User.objects.filter(username__icontains=searched)
    searchnames=User.objects.filter(username__icontains=searched)
    return render(request,'adminHome.html',{'users':searchnames})

