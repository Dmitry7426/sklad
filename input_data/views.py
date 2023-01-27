import re

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import EquipmentsForm, FormList, BrandsForm, ModelsForm, TabForm, UserForm, UserDeleteForm, \
    EquipmentsAllForm
from .models import *
from django import forms

def index(request):
    return render(request, 'index.html')

def form_in(request):
    form = EquipmentsForm()
    if request.method == 'POST':
        # w1 = request.form.get('n1')
        form = EquipmentsForm(request.POST)
        if form.is_valid():
            t = request.POST.get('Typ')
            types = TypesEquipments.objects.create(TypesEq=t)
            types.save()
            return HttpResponse(f'<h2>{t} успешно добавлен в справочник!</h2><a href="/input_data/form_in"> '
                                    f'Добавить еще!</a><br><br><a href="/">Вернуться на главную</a>')
        else:
            form = EquipmentsForm()
            messages.info(request, 'Не допустимое наименование')
            return render(request, 'form_index.html', {'form': form})
    else:
        return render(request, 'form_index.html', {'form': form})

def test(request):
    a = 'drgdsghfdghbfgdbd'
    return HttpResponse(a)

def st2(request):
    return render(request, 'formsinput.html')

# Функция заполения моделей, брендов и типа оборудования
def form_tabs(request):
    form = TabForm()
    if request.method == 'POST':
        if request.POST.get('forms') == 'equipments':
            form = EquipmentsForm(request.POST)
            if form.is_valid():
                t = request.POST.get('name')
                types = TypesEquipments.objects.create(TypesEq=t)
                types.save()
                return HttpResponse(f'<h2>{t} успешно добавлен в справочник!</h2><a href="/input_data/form_tabs"> '
                                    f'Добавить еще!</a><br><br><a href="/">Вернуться на главную</a>')
            else:
                form = EquipmentsForm()
                messages.info(request, 'Не допустимое наименование')
                return render(request, 'form_tabs.html', {'form': form})

        if request.POST.get('forms') == 'brands':
            form = BrandsForm(request.POST)
            if form.is_valid():
                t = request.POST.get('name')
                types = Brands.objects.create(BrandName=t)
                types.save()
                return HttpResponse(f'<h2>{t} успешно добавлен в справочник!</h2><a href="/input_data/form_tabs"> '
                                    f'Добавить еще!</a><br><br><a href="/">Вернуться на главную</a>')
            else:
                form = BrandsForm()
                messages.info(request, 'Не допустимое наименование')
                return render(request, 'form_tabs.html', {'form': form})

        if request.POST.get('forms') == 'models':
            form = ModelsForm(request.POST)
            if form.is_valid():
                t = request.POST.get('name')
                types = Models.objects.create(ModelName=t)
                types.save()
                return HttpResponse(f'<h2>{t} успешно добавлен в справочник!</h2><a href="/input_data/form_tabs"> '
                                    f'Добавить еще!</a><br><br><a href="/">Вернуться на главную</a>')
            else:
                form = ModelsForm()
                messages.info(request, 'Не допустимое наименование')
                return render(request, 'form_tabs.html', {'form': form})
    return render(request, 'form_tabs.html', {'form': form})

# функция добавления пользователя в справочник (с должностью и подразделением)
def form_users(request):
    form = UserForm()
    if request.method == 'POST':
        UserName = request.POST.get('UserName')
        MidlName = request.POST.get('MidlName')
        SurName = request.POST.get('SurName')
        Positions = Position.objects.create(PositionName=request.POST.get('Position'))
        Units = Unit.objects.create(UnitName=request.POST.get('Units'))
        types = Users.objects.create(UserName=UserName, MidlName=MidlName, SurName=SurName, Position=Positions, Unit=Units)
        types.save()
        messages.info(request, 'Запись добавлена!')
        return render(request, 'form_users.html', {'form': form})

    return render(request, 'form_users.html', {'form': form})

# функция удаления пользователя из справочника Users
def form_delete_user(request):
    form = UserDeleteForm()
    if Users.objects.all():
        allobj = Users.objects.all()
        name = []
        for i in allobj:
            name.append(i.UserName + ', ' + i.MidlName + ', ' + i.SurName + ', ' + i.Position.PositionName)
        if request.method == 'POST':
            if request.POST.get('select'):
                lst = request.POST.get('select')
                # print(lst)
                lst = lst.split(', ')
                # print(lst)
                if len(lst) == 4:
                    for i in Position.objects.filter(PositionName=lst[3]):
                        id_pos = i.id
                    # print(id_pos)
                    Users.objects.filter(UserName=lst[0], MidlName=lst[1], SurName=lst[2], Position=id_pos).delete()
                    messages.info(request, 'Запись успешно удалена!!')
                    return HttpResponseRedirect('/input_data/delete_user')
                return render(request, 'form_del_users.html', {'form': form, 'name': name})
            else:
                messages.info(request, 'Вы ни чего выбрали!')
    else:
        return render(request, 'form_del_users.html', {'form': form})
    return render(request, 'form_del_users.html', {'form': form, 'name': name})



# функция добавления записей о принадлежности оборудования

def form_equipments(request):
    form = EquipmentsAllForm()
    invnum = InvNum.objects.all()
    typeeq = TypesEquipments.objects.all()
    for i in invnum:
        print(i.InvNumber)
    for i in typeeq:
        print(i.TypesEq)
    if request.method == 'POST':
        inv = request.POST.get('inv')
        typ = request.POST.get('typeeq')
        # inv = Equipments.objects.create(InvNum=request.POST.get('inv'))
        print(inv, ' - ', typ)
        return render(request, 'form_equipments_all.html', {'form': form, 'invnum': invnum, 'typeeq': typeeq})
    return render(request, 'form_equipments_all.html', {'form': form, 'invnum': invnum, 'typeeq': typeeq})

    # Positions = Position.objects.create(PositionName=request.POST.get('Position'))



# тестовая форма работы со списком
def form_list(request):
    allobj = Users.objects.all()
    name = []
    for i in allobj:
        name.append(i.UserName + ' ' + i.MidlName + ' ' + i.SurName)
    form = FormList()
    if request.method == 'POST':
        lst = request.POST.get('select', 'select2')
        lst = lst.split(' ')
        Users.objects.filter(UserName=lst[0], MidlName=lst[1], SurName=lst[2]).delete()
    return render(request, 'form_list.html', {'form': form, 'name': name})




