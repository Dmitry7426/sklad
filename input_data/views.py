import pythoncom
from django.core.files.storage import default_storage, FileSystemStorage
from wmi import WMI
import re
import subprocess
import json
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import EquipmentsForm, FormList, BrandsForm, TabForm, UserForm, UserDeleteForm, \
    EquipmentAddForm, EquipmentsLinkUsers, UnitForm, PositionForm, ConfigComputer, UploadFileForm
from .models import *



def index(request):
    return render(request, 'index.html')


def form_in(request):
    form = EquipmentsForm()
    if request.method == 'POST':
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


def st2(request):
    return render(request, 'formsinput.html')


# Функция заполения моделей, брендов, типа оборудования
def form_tabs(request):
    form = TabForm()
    if request.method == 'POST':
        if request.POST.get('forms') == 'equipments':
            form = BrandsForm(request.POST)
            if form.is_valid():
                t = request.POST.get('name')
                try:
                    types = TypesEquipments.objects.create(TypesEq=t)
                    types.save()
                    return HttpResponse(
                        f'<br><h1>{t} успешно добавлен в справочник!</h1></h1><br><br></h2><a href="/input_data/form_tabs"> '
                        f'Повторить ввод</a><br><br><a href="/">Вернуться на главную</a>')
                except IntegrityError:
                    return HttpResponse(
                        f'<br><h1>{t} уже есть в справочнике! </h1><br><br></h2><a href="/input_data/form_tabs"> '
                        f'Повторить ввод</a><br><br><a href="/">Вернуться на главную</a>')
        if request.POST.get('forms') == 'brands':
            form = BrandsForm(request.POST)
            if form.is_valid():
                t = request.POST.get('name')
                try:
                    types = Brands.objects.create(BrandName=t)
                    types.save()
                    return HttpResponse(
                        f'<br><h1>{t} успешно добавлен в справочник!</h1></h1><br><br></h2><a href="/input_data/form_tabs"> '
                        f'Повторить ввод</a><br><br><a href="/">Вернуться на главную</a>')
                except IntegrityError:
                    return HttpResponse(
                        f'<br><h1>{t} уже есть в справочнике! </h1><br><br></h2><a href="/input_data/form_tabs"> '
                        f'Повторить ввод</a><br><br><a href="/">Вернуться на главную</a>')
        if request.POST.get('forms') == 'models':
            form = BrandsForm(request.POST)
            if form.is_valid():
                t = request.POST.get('name')
                try:
                    types = Models.objects.create(ModelName=t)
                    types.save()
                    return HttpResponse(
                        f'<br><h1>{t} успешно добавлен в справочник!</h1></h1><br><br></h2><a href="/input_data/form_tabs"> '
                        f'Повторить ввод</a><br><br><a href="/">Вернуться на главную</a>')
                except IntegrityError:
                    return HttpResponse(
                        f'<br><h1>{t} уже есть в справочнике! </h1><br><br></h2><a href="/input_data/form_tabs"> '
                        f'Повторить ввод</a><br><br><a href="/">Вернуться на главную</a>')
    return render(request, 'form_tabs.html', {'form': form})


# функция добавления пользователя в справочник (с должностью и подразделением)
def form_users(request):
    form = UserForm()
    unit = Unit.objects.all()
    pos = Position.objects.all()
    if request.method == 'POST':
        arr = []
        for item in request.POST:
            arr.append(request.POST.get(item))
        arr = arr[1:]
        print(arr)
        print(request.POST.get('position'))
        print(request.POST.get('unit'))

        if func_re(arr):
            Users.objects.create(UserName=arr[0], MidlName=arr[1], SurName=arr[2],
                                 Position=Position.objects.get(PositionName=request.POST.get('position')),
                                 Unit=Unit.objects.get(UnitName=request.POST.get('unit'))).save()
            messages.info(request, 'Информация записана в базу данных!')
            return render(request, 'form_users.html', {'form': form, 'unit': unit, 'pos': pos})
        else:
            messages.info(request, 'Данные введены не корректные либо не допустимые символы!!')
            return render(request, 'form_users.html', {'form': form, 'unit': unit, 'pos': pos})
    return render(request, 'form_users.html', {'form': form, 'unit': unit, 'pos': pos})


# функция удаления пользователя из справочника Users
def form_delete_user(request):
    form = UserDeleteForm()
    if Users.objects.all():
        allobj = Users.objects.all()
        name = []
        for i in allobj:
            name.append(i.SurName + ', ' + i.UserName + ', ' + i.MidlName + ', ' + i.Position.PositionName + ', '
                        + i.Unit.UnitName)
        if request.method == 'POST':
            if request.POST.get('select'):
                lst = request.POST.get('select')
                lst = lst.split(', ')
                if len(lst) == 4:
                    for i in Position.objects.filter(PositionName=lst[3]):
                        id_pos = i.id
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
    return render(request, 'form_equipments_all.html', {'form': form, 'invnum': invnum,
                                                        'models': models, 'user': user})


# функция регистрации нового оборудования
def form_add_equipment(request):
    form = EquipmentAddForm()
    typeeq = TypesEquipments.objects.all()
    brands = Brands.objects.all()
    models = Models.objects.all()
    num = InvNum.objects.all()
    if request.method == 'POST':
        print(request.POST.get('inv'))
        if func_invnum(request.POST.get('inv')):
            print('Запись в базу произведена')
            InvNum.objects.create(InvNumber=request.POST.get('inv'),
                                  typ=TypesEquipments.objects.get(TypesEq=request.POST.get('typeeq')),
                                  brand=Brands.objects.get(BrandName=request.POST.get('brand')),
                                  model=Models.objects.get(ModelName=request.POST.get('model')),
                                  netname=request.POST.get('netname')).save()
            messages.info(request, 'Информация успешно внесена в базу данных')
            return render(request, 'form_equp_add.html', {'form': form, 'typeeq': typeeq,
                                                          'brands': brands, 'models': models})
        else:
            print('Ошибка- либо номер есть либо введен не верно')
            messages.info(request, 'Такой инвентарный номер уже есть, либо номер введен не корректно! '
                                   'Проверьте и введите заново.')
            return render(request, 'form_equp_add.html', {'form': form, 'typeeq': typeeq,
                                                          'brands': brands, 'models': models})
    return render(request, 'form_equp_add.html', {'form': form, 'typeeq': typeeq,
                                                  'brands': brands, 'models': models})


# функция вывода всей информации о технике и ее пользователях
def get_all_equipments(request):
    get_all = Equipments.objects.all()
    form = EquipmentsLinkUsers()
    if request.method == 'POST':
        types = request.POST.get('types')
        names = request.POST.get('name')
        w = request.POST.get('typeeq')
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
    return render(request, 'get_all_equipments.html', {'form': form, 'data': get_all})


# форма ввода подразделения
def form_units(request):
    form = UnitForm()
    if request.method == 'POST':
        try:
            Unit.objects.create(UnitName=(request.POST.get('name'))).save()
            return HttpResponse(
                f'<br><h1>Запись успешно добавлена!</h1></h1><br><br></h2><a href="/input_data/add_unit"> '
                f'Добавить еще</a><br><br><a href="/">Вернуться на главную</a>')
        except IntegrityError:
            return HttpResponse(f'<br><h1>Такая запись уже есть!</h1></h1><br><br></h2><a href="/input_data/add_unit"> '
                                f'Повторить ввод</a><br><br><a href="/">Вернуться на главную</a>')
    return render(request, 'form_unit.html', {'form': form})


# форма ввода должности
def form_position(request):
    form = PositionForm()
    if request.method == 'POST':
        try:
            Position.objects.create(PositionName=(request.POST.get('name'))).save()
            return HttpResponse(
                f'<br><h1>Запись успешно добавлена!</h1></h1><br><br></h2><a href="/input_data/add_position"> '
                f'Добавить еще</a><br><br><a href="/">Вернуться на главную</a>')
        except IntegrityError:
            return HttpResponse(
                f'<br><h1>Такая запись уже есть!</h1></h1><br><br></h2><a href="/input_data/add_position"> '
                f'Повторить ввод</a><br><br><a href="/">Вернуться на главную</a>')
    return render(request, 'form_pos.html', {'form': form})


# функция заполения конфигурации ПК
def config_computer_manual(request):
    form = ConfigComputer()
    inv = InvNum.objects.all()
    if request.method == 'POST':
        arr = []
        for items in request.POST:
            arr.append(request.POST.get(items))
        arr = arr[1:]
        Hardware.objects.create(InvNumber=InvNum.objects.get(InvNumber=''.join(arr[0])), OperateSystem=arr[1],
                                Activate=arr[2], CurrentUser=arr[3], IPAddress=arr[4], MAC=arr[5],
                                SystemName=arr[6], LANSpeed=arr[7], HDD=arr[8], Mboard=arr[9], ProcessorName=arr[10],
                                Soccet=arr[11], OZU=arr[12], PrinterTypeConnect=arr[13], InstalledSoft=arr[14])
    return render(request, 'form_config_comp.html', {'form': form, 'inv': inv})


# функция заполнения конфигурации скриптом
def config_computer_auto(request):
    form = ConfigComputer()
    inv = InvNum.objects.all()
    hard = Hardware.objects.all()
    addr = request.META["REMOTE_ADDR"]
    if request.method == 'POST':
        if request.POST.get == 'onclick':
            print('OnClick')
        else:
            print(request.META["REMOTE_ADDR"])
            try:
                with open(f'//winwsus/inv21/inv_new/{addr}.json', 'r') as file:
                    dt = json.load(file)
                    arr = []
                    soft = []
                    for key, value in dt.items():
                        for k, v in value.items():
                            arr.append(k)
                            arr.append(v)
                    for name_po, brand in dt['Программное обеспечение'].items():
                        soft.append(name_po)
                    if request.method == 'POST':
                        for item in hard:
                            tmp = []
                            tmp.append(item.InvNumber.InvNumber)
                        inv_n = []
                        inv_n.append(request.POST.get('invent'))
                        for items in request.POST:
                            a1 = []
                            a1.append(items)
                        if ''.join(a1) == 'getnum':
                            if Hardware.objects.filter(InvNumber=InvNum.objects.get(InvNumber=''.join(inv_n))):
                                return HttpResponse(
                                    '<h2>Такая запись есть!</h2><h3><a href="/input_data/conf_auto">Вернуться назад</h3>')
                            else:
                                Hardware.objects.create(
                                    InvNumber=InvNum.objects.get(InvNumber=''.join(inv_n)), OperateSystem=arr[3],
                                    Activate=arr[5], CurrentUser=(str(arr[7]).split('\\'))[1], IPAddress=arr[13],
                                    MAC=arr[11], SystemName=arr[1], LANSpeed=arr[15],
                                    HDD=dt['Конфигурация ПК']['Модель HDD'], Mboard=(arr[17] + '; ' + arr[19]),
                                    ProcessorName=arr[21], Soccet=arr[23], OZU=arr[25],
                                    PrinterTypeConnect=arr[33], InstalledSoft=str(soft))
                return render(request, 'form_config_comp_auto.html', {'form': form, 'inv': inv, 'dt': dt,
                                                                      'form_put': arr, 'soft': soft})
            except:
                return HttpResponse(
                    '<h1>Информации о данном ПК не найдено!</h1><br><br><a href="/">Вернуться на главную</a>')
    return render(request, 'form_config_comp_auto.html', {'form': form, 'inv': inv})


def config_computer_file(request):
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':

        folder = 'media'
        if form.is_valid():
            file = request.FILES['file']

            fs = FileSystemStorage(location=folder)  # defaults to   MEDIA_ROOT
            filename = fs.save(file.name, file)
            file_url = fs.url(filename)
            print('Файл сохранен')
            print(file_url)
            print(filename)
            print(fs)
            with open(f'.{file_url}', 'r', encoding='UTF-8') as fl:
                f = fl.read()
                print(f)

            return render(request, 'upload.html', {'form': form})

    return render(request, 'upload.html', {'form': form})


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


# функция проверки инвентарного номера на дубликат и корректность ввода
def func_invnum(a):
    print(a)
    if InvNum.objects.filter(InvNumber=a):  # проверка наличия номера в бд
        return False
    else:
        tmp = a.lower()
        tmp = re.sub(r'м', 'm', tmp)
        if re.match(r'^m0{2}0\d{5}$', tmp) or re.match(r'^\d{6}$', tmp):
            return True
        else:
            return False


# функция запроса системной информации - тесты
def get_config_ps(addr):
    pythoncom.CoInitialize()
    computer = WMI(addr)
    print(addr)
    slovar = {}
    arr = {}
    act = subprocess.Popen("powershell.exe -ExecutionPolicy ByPass -File act.ps1", stdout=subprocess.PIPE)
    p = act.communicate()
    w = str(p)
    w = re.findall(r'\d+', w)
    if '1' in w:
        acivations = 'Да'
    else:
        acivations = 'Нет'
    arr['Активация системы'] = acivations
    slovar['Статус активации'] = arr
    arr = {}
    arr['Сетевое имя'] = computer.Win32_ComputerSystem()[0].Name
    slovar['Имя ПК'] = arr
    arr = {}
    i = 0
    for netspeed in computer.Win32_NetworkAdapter():
        if netspeed.NetConnectionStatus == 2:
            speed = round(int(netspeed.Speed) / 1000 / 1000)
    for net in computer.Win32_NetworkAdapterConfiguration():
        if net.IPAddress:
            i += 1
            ip = net.IPAddress[0]
    arr[f'Сетевой адаптер'] = net.Description
    arr['MAC адрес'] = net.MACAddress
    arr['IP адрес'] = ip
    arr['Скорость соединения'] = speed
    slovar['Сеть'] = arr
    arr = {}
    arr['Имя'] = computer.Win32_ComputerSystem()[0].UserName
    slovar['Текущий пользователь'] = arr
    arr = {}
    arr['Наименование'] = computer.Win32_OperatingSystem()[0].Caption
    slovar['Установленная система'] = arr
    arr = {}
    arr['Производитель MBoard'] = computer.Win32_BaseBoard()[0].Manufacturer
    arr['Модель MBoard'] = computer.Win32_BaseBoard()[0].Product
    arr['Процессор'] = computer.Win32_Processor()[0].Name
    arr['Соккет'] = computer.Win32_Processor()[0].SocketDesignation
    arr['ОЗУ'] = round(int(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1024 / 1024)
    # slovar['Кофигурация ПК'] = arr
    for hdd in computer.Win32_DiskDrive():
        hdd_size = int(int(hdd.Size) / 1024 / 1024 / 1024)
        if hdd.Caption:
            arr['Модель HDD'] = hdd.Model
            arr['Обьем'] = int(int(hdd.Size) / 1024 / 1024 / 1024)
    slovar['Конфигурация ПК'] = arr
    for video in computer.Win32_videoController():
        arr = {}
        i += 1
        arr[video.VideoProcessor] = video.Description
    slovar['Видео'] = arr
    arr = {}
    for items in computer.Win32_Printer():
        if items.Default:
            arr[items.Name] = items.PortName
    slovar['Принтера'] = arr
    with open('result.json', 'w') as file:
        json.dump(slovar, file)
    print('Файл готов')


