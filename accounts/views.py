from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView

def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            messages.success(request,'please confirm this form','success')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'You are logged in successfully','success')
                return redirect('home')
            else:
                messages.error(request,'username or password is wrong','danger')
    else:
        form = LoginForm()
    return render(request,'login.html', {'form':form})


def LogoutView(request):
    logout(request)
    messages.success(request,'You are logged out successfully','success')
    return redirect('home')


class ProfileView():
    pass