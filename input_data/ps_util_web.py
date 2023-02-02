from wmi import WMI
import re
import subprocess
import json

computer = WMI()
slovar = {}
slovar2 = {}
i = 0


def test():
    w = {'testsssss': 'ggfdd'}
    return json.dumps(w)

def get_activate():
    act = subprocess.Popen("powershell.exe -ExecutionPolicy ByPass -File act.ps1", stdout=subprocess.PIPE)
    p = act.communicate()
    w = str(p)
    w = re.findall(r'\d+', w)
    if '1' in w:
        acivations = 'Да'
    else:
        acivations = 'Нет'
    slovar['Статус активации'] = acivations
    data = json.dumps(slovar)
    return data

def name_pc():
    slovar['Имя ПК'] = computer.Win32_ComputerSystem()[0].Name
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
            ip = net.IPAddress[0]
    arr[f'Сетевой адаптер'] = net.Description
    arr['MAC адрес'] = net.MACAddress
    arr['IP адрес'] = ip
    arr['Скорость соединения'] = speed
    slovar['Сеть'] = arr
    data = json.dumps(slovar)
    return data

def get_user():

    slovar['Пользователь'] = computer.Win32_ComputerSystem()[0].UserName
    data = json.dumps(slovar)
    return data

def get_os():

    slovar['Установленная ОС'] = computer.Win32_OperatingSystem()[0].Caption
    data = json.dumps(slovar)
    return data

def get_hardware():
    arr = {}
    i = 0
    slovar['Производитель'] = computer.Win32_BaseBoard()[0].Manufacturer
    slovar['Модель'] = computer.Win32_BaseBoard()[0].Product
    slovar['Процессор'] = computer.Win32_Processor()[0].Name
    slovar['Соккет'] = computer.Win32_Processor()[0].SocketDesignation
    slovar['ОЗУ'] = round(int(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1024 / 1024)
    for hdd in computer.Win32_DiskDrive():
        hdd_size = int(int(hdd.Size) / 1024 / 1024 / 1024)
        if hdd.Caption:
            arr['Модель'] = hdd.Model
            arr['Обьем'] = int(int(hdd.Size) / 1024 / 1024 / 1024)

    slovar['HDD'] = arr
            # slovar['Производитель'] = hdd.Model
            # slovar['Емкость диска'] = hdd_size
            # slovar.update({
            #     f'Диск {i}': {
            #         hdd.Model: f'{hdd_size} Gb' }
            # })
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
    with open('result.json', 'w') as fp:
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

name_pc()
get_os()
get_activate()
get_user()
get_network()
get_hardware()
get_printer()
get_soft()
# get_info.file_output()
json_output_file()
# data2 = get_info.json_read_file()

json_return()

# data2 = json.loads(get_info.json_return())
#
# print(data2['Установленная ОС'])
# print(data2['Статус активации'])
# print(data2['Пользователь'])
# print(data2['Сеть']['IP адрес'])
# print(data2['Сеть']['MAC адрес'])
# print(data2['Имя ПК'])
# print(data2['Сеть']['Скорость соединения'])
# for key, value in data2['HDD'].items():
#     print(key)
# print(data2['Производитель'] + '; ' + data2['Модель'])
# print(data2['Процессор'])
# print(data2['Соккет'])
# print(data2['ОЗУ'])
# print(data2['Принтера'])





# for key, value in data2.items():
#     print(key, value)
# data2 = json.load(get_info.json_return())
#
#
# print(data2)



