import re

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import EquipmentsForm, FormList, BrandsForm, ModelsForm, TabForm, UserForm, UserDeleteForm, \
    EquipmentAddForm, EquipmentsLinkUsers
from .models import *


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

# Функция заполения моделей, брендов, типа оборудования
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
        arr = []
        for item in request.POST:
            arr.append(request.POST.get(item))
        arr = arr[1:]
        if func_re(arr):
            Users.objects.create(UserName=arr[0], MidlName=arr[1], SurName=arr[2],
                                 Position=Position.objects.create(PositionName=arr[3]),
                                 Unit=Unit.objects.create(UnitName=arr[4])).save()
            messages.info(request, 'Информация записана в базу данных!')
            return render(request, 'form_users.html', {'form': form})
        else:
            messages.info(request, 'Данные введены не корректные либо не допустимые символы!!')
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
    form = EquipmentsLinkUsers()
    invnum = InvNum.objects.all()
    user = Users.objects.all()
    for i in invnum:
        print(i.InvNumber, i.typ.TypesEq, i.model.ModelName, i.brand.BrandName)
    for i in user:
        print(i.UserName, i.MidlName, i.SurName, i.Unit.UnitName, i.Position.PositionName)

    if request.method == 'POST':
        Equipments.objects.create(Number=InvNum.objects.get(InvNumber=request.POST.get('inv')),
                                  User=Users.objects.get(SurName=request.POST.get('user'))).save()


        return render(request, 'form_equipments_all.html', {'form': form, 'invnum': invnum,
                                                            'models': models, 'user': user})
    #     inv = request.POST.get('inv')
    #     typ = request.POST.get('typeeq')
    #     brnd = request.POST.get('brand')
    #     mdl = request.POST.get('model')
    #     usr = request.POST.get('users')
    #
    #     # inv = Equipments.objects.create(InvNum=request.POST.get('inv'))
    #     print(inv, ' - ', typ, brnd, mdl, usr)
    #     return render(request, 'form_equipments_all.html', {'form': form, 'invnum': invnum, 'typeeq': typeeq,
    #                                                         'brands': brands, 'models': models, 'user': user})
    return render(request, 'form_equipments_all.html', {'form': form, 'invnum': invnum,
                                                         'models': models, 'user': user})

    # Positions = Position.objects.create(PositionName=request.POST.get('Position'))

# функция регистрации нового оборудования
def form_add_equipment(request):
    form = EquipmentAddForm()
    typeeq = TypesEquipments.objects.all()
    brands = Brands.objects.all()
    models = Models.objects.all()
    num = InvNum.objects.all()

    if request.method == 'POST':
        if InvNum.objects.filter(InvNumber=request.POST.get('inv')):
            print('yes')

            messages.info(request, 'Такой инвентарный номер уже есть! Проверьте и введите заново.')
            return render(request, 'form_equp_add.html', {'form': form, 'typeeq': typeeq,
                                                              'brands': brands, 'models': models})

        else:
            InvNum.objects.create(InvNumber=request.POST.get('inv'),
                                    typ=TypesEquipments.objects.get(TypesEq=request.POST.get('typeeq')),
                                    brand=Brands.objects.get(BrandName=request.POST.get('brand')),
                                    model=Models.objects.get(ModelName=request.POST.get('model')),
                                    netname=request.POST.get('netname')).save()

            return render(request, 'form_equp_add.html', {'form': form, 'typeeq': typeeq,
                                                              'brands': brands, 'models': models})

    return render(request, 'form_equp_add.html', {'form': form, 'typeeq': typeeq,
                                                        'brands': brands, 'models': models})

# функция вывода всей информации о технике и ее пользователях
def get_all_equipments(request):
    # get_all = Equipments.objects.all().order_by('User__Unit__UnitName')
    get_all = Equipments.objects.all()
    form = EquipmentsLinkUsers()
    if request.method == 'POST':
        types = request.POST.get('types')
        names = request.POST.get('name')
        w = request.POST.get('typeeq')
        print(w)
        # print(types, names)
        if request.POST.get('types'):
            get_all = Equipments.objects.all().order_by('Number__typ__TypesEq')
            return render(request, 'get_all_equipments.html', {'data': get_all, 'form': form})
        elif request.POST.get('name'):
            get_all = Equipments.objects.all().order_by('Number__brand__BrandName')
            return render(request, 'get_all_equipments.html', {'data': get_all, 'form': form})
        elif request.POST.get('user'):
            get_all = Equipments.objects.all().order_by('User__SurName')
            return render(request, 'get_all_equipments.html', {'data': get_all, 'form': form})
        elif request.POST.get('unit'):
            get_all = Equipments.objects.all().order_by('User__Unit__UnitName')
            return render(request, 'get_all_equipments.html', {'data': get_all, 'form': form})



        # else:
        #     get_all = Equipments.objects.all()
        #     return render(request, 'get_all_equipments.html', {'data': get_all, 'form': form})

    # for i in get_all:
    #     print(i.Number.InvNumber, i.Number.typ.TypesEq, i.Number.brand.BrandName, i.Number.model.ModelName, i.Number.netname)
        # print(i.User.SurName, i.User.UserName, i.User.MidlName, i.User.Position.PositionName, i.User.Unit.UnitName)
        # print(i.Number.netname)
    return render(request, 'get_all_equipments.html', {'form': form, 'data': get_all})

# функция выбора техники по параметрам
# выбор по подразделениям
def get_units(request):
    pass

# выбор по человеку
def get_user(request):
    pass

# выбор по бренду
def get_brand(request):
    pass

# выбор по конкретному типу
def get_type(request):
    pass

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

# функция проверки полей на ввод только латиницей
def func_re(a):
    r = []
    for i in a:
        res = bool(re.findall(r'[a-zA-Z]', i))
        r.append(res)

    if True in r:
        return False
    else:
        return True

