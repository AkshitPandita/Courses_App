from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User


@login_required(login_url='login')
def Home(request):
    return render(request,'index.html')

def About(request):
    return render(request,'welcome.html')

def Main(request):
    return render(request,'main.html')


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
            else:
                message = "Invalid username or password"
    else:
        form = LoginForm()
        message= None
    
    return render(request, 'login.html', {'form': form,'message': message})

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home') 
        else:
            message = "Invalid Username or EmailId" # Redirect to home page after successful registration
    else:
        form = RegisterForm()
        message = None
    
    return render(request, 'register.html', {'form': form, 'message': message})