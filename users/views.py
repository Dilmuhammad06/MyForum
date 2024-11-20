from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'login.html',{"form":form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('auth:login')
        return render(request,'login.html',{"form":form})

def logoutView(request):
    logout(request)
    return redirect('auth:login')