from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import RegisterForm, Login


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


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/login')


def testauth(request):
    a = 'drgdsghfdghbfgdbd'
    return HttpResponse(a)


