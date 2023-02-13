from wmi import WMI
import re
import subprocess
import json


computer = WMI()
slovar = {}
slovar2 = {}
i = 0


def get_activate():
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
    data = json.dumps(slovar)
    return data


def name_pc():
    arr = {}
    arr['Сетевое имя'] = computer.Win32_ComputerSystem()[0].Name
    slovar['Имя ПК'] = arr
    data = json.dumps(slovar)
    return data


def get_network():
    arr = {}
    i = 0
    for netspeed in computer.Win32_NetworkAdapter():
        if netspeed.NetConnectionStatus == 2:
            speed = round(int(netspeed.Speed) / 1000 / 1000)
    for net in computer.Win32_NetworkAdapterConfiguration():
        if net.IPAddress:
            i += 1
            ip = net.IPAddress
    arr[f'Сетевой адаптер'] = net.Description
    arr[f'MAC адрес'] = net.MACAddress
    arr[f'IP адрес'] = ip
    arr[f'Скорость соединения'] = speed
    slovar['Сеть'] = arr
    data = json.dumps(slovar)
    return data


def get_user():
    arr = {}
    arr['Имя'] = computer.Win32_ComputerSystem()[0].UserName
    slovar['Текущий пользователь'] = arr
    data = json.dumps(slovar)
    return data


def get_os():
    arr = {}
    arr['Наименование'] = computer.Win32_OperatingSystem()[0].Caption
    slovar['Установленная система'] = arr
    data = json.dumps(slovar)
    return data


def get_hardware():
    arr = {}
    i = 0
    arr['Производитель MBoard'] = computer.Win32_BaseBoard()[0].Manufacturer
    arr['Модель MBoard'] = computer.Win32_BaseBoard()[0].Product
    arr['Процессор'] = computer.Win32_Processor()[0].Name
    arr['Соккет'] = computer.Win32_Processor()[0].SocketDesignation
    arr['ОЗУ'] = round(int(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1024 / 1024)
    # slovar['Кофигурация ПК'] = arr
    for hdd in computer.Win32_DiskDrive():
        hdd_size = int(int(hdd.Size) / 1024 / 1024 / 1024)
        if hdd.Caption:
            i += 1
            arr[f'Модель HDD {i}'] = hdd.Model
            arr[f'Обьем {i}'] = int(int(hdd.Size) / 1024 / 1024 / 1024)
    slovar['Конфигурация ПК'] = arr
    for video in computer.Win32_videoController():
        arr = {}
        i += 1
        arr[video.VideoProcessor] = video.Description
    slovar['Видео'] = arr
    data = json.dumps(slovar)
    return data


def get_printer():
    i = 0
    arr = {}
    for items in computer.Win32_Printer():
        if items.Default:
            arr[items.Name] = items.PortName
    slovar['Принтера'] = arr
    data = json.dumps(slovar)
    return data


def get_soft():
    i = 0
    arr = {}
    for soft in computer.Win32_Product():
        i += 1
        arr[soft.Name] = soft.Vendor
    slovar['Программное обеспечение'] = arr
    data = json.dumps(slovar)
    return data


def file_output():
    with open(f'c:/getinfo/{computer.Win32_ComputerSystem()[0].Name}.txt', 'a',
              encoding='UTF-8') as file_out:
        for key, val in slovar.items():
            key = str(re.sub(r'[^a-zA-Zа-яА-Я ]', '', key))
            file_out.writelines(f'{key}: {val}; \n')


def json_output_file():
    i = 0
    for net in computer.Win32_NetworkAdapterConfiguration():
        if net.IPAddress:
            i += 1
            ip = net.IPAddress[0]
    with open(f'{ip}.json', 'w') as fp:
        json.dump(slovar, fp)
    print('Файл готов')


def json_read_file():
    file = input('Введите имя файла JSON: ')
    with open(file, 'r') as fp:
        data = json.load(fp)
    return data


def json_return():
    data = json.dumps(slovar)
    return data


#
name_pc()
get_os()
get_activate()
get_user()
get_network()
get_hardware()
get_printer()
get_soft()
# # get_info.file_output()
json_output_file()
# # data2 = get_info.json_read_file()
#
json_return()
