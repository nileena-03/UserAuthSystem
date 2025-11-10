from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        messages.success(request,"User registered succesfully!")
        return redirect('login')
    return render(request,'register.html')

def loginUser(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')