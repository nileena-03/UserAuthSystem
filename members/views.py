from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'register.html')

def loginUser(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')