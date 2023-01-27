from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import RegisterForm, Login
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):

    return render(request, 'index.html')

def register(request):
    data = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = 'Регистрация прошла успешно'
            messages.info(request, 'Пользователь зарегистрирован!')
            return HttpResponseRedirect('/login/')
        return render(request, 'register.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def loginuser(request):
    form = Login(request.POST)
    if request.method == 'POST':
        form = Login(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.info(request, 'Не верный логин или пароль')
                return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})





    # if request.method == 'POST':
    #     form = Login(request.POST)
    #     print('ПОСТ прошел')
    #     if form.is_valid():
    #         uservalue = form.cleaned_data.get("username")
    #         passwordvalue = form.cleaned_data.get("password")
    #
    #         user = authenticate(username=uservalue, password=passwordvalue)
    #         print('ФОрма валидна')
    #         if user is not None:
    #             login(request, user)
    #             context = {'form': form, 'error': 'Логин не верный'}
    #             print('Логин не верный')
    #             return render(request, 'login.html', context)
    #         else:
    #             context = {'form': form, 'error': 'Логин или пароль не верный'}
    #             print('логин или пароль не верный')
    #             return render(request, 'login.html', context)
    #
    #             if user.is_autenticated:
    #                 pass
    # else:
    #     form = Login()
    #
    #     return render(request, 'login.html', {'form': form})
    #     # return HttpResponseRedirect('/login/')



def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/login')

def testauth(request):
    a = 'drgdsghfdghbfgdbd'
    return HttpResponse(a)


