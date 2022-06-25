from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register(request):
  
    if request.method == "POST":
        password = request.POST['password1']
        middle_name = request.POST['middle_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']       
        user = CustomUser.objects.create(first_name=first_name, password=password,
                                middle_name=middle_name, last_name=last_name, email=email, is_active=True)
        user.set_password(password)
        user.save()
        user = authenticate(request, email=email, password=password)       
        if user is not None:
            login(request, user)
            return redirect('books')        
    return render(request, 'authentication/register.html')

# admin@tes.com

def log_in(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')      
        user = authenticate(request, email=email, password=password)       
        if user is not None:
            login(request, user)
            return redirect('books')
 
    return render(request,'authentication/login.html')

def log_out(request):
    logout(request)
    return redirect('books')