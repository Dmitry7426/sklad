from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
            print('успех')
        return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
        data['form'] = form
        data['res'] = 'Ошибка'
        print('ошибка')
        return render(request, 'register.html', {'form': form})

def loginuser(request):
    uservalue = ''
    passwordvalue = ''

    form = Login(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context = {'form': form, 'error': 'Логин не верный'}
            return render(request, 'login.html', context)
        else:
            context = {'form': form, 'error': 'Логин или пароль не верный'}
            return render(request, 'login.html', context)
    else:
        context = {'form': form}
        return render(request, 'login.html', context)

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/')

def testauth(request):
    a = 'drgdsghfdghbfgdbd'
    return HttpResponse(a)


