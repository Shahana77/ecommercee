from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST['firstName']
        secnd_name=request.POST['secondName']

        email=request.POST['email']
        password=request.POST['password']
        conf_password=request.POST['confirmpassword']
        if password == conf_password:
            if User.objects.filter(username=first_name).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=first_name,last_name=secnd_name,email=email,password=password)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


