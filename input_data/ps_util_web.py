from wmi import WMI
import re
import subprocess
import json

computer = WMI()
slovar = {}
i = 0

class get_info:

    def get_activate():
        act = subprocess.Popen("powershell.exe -ExecutionPolicy ByPass -File act.ps1", stdout=subprocess.PIPE)
        p = act.communicate()
        w = str(p)
        w = re.findall(r'\d+', w)
        if '1' in w:
            acivations = 'Система активирована'
        else:
            acivations = 'Система не активирована'
        slovar['Статус активации'] = acivations

    def name_pc():
        slovar['Имя ПК'] = computer.Win32_ComputerSystem()[0].Name

    def get_network():
        i = 0
        for netspeed in computer.Win32_NetworkAdapter():
            if netspeed.NetConnectionStatus == 2:
                speed = round(int(netspeed.Speed) / 1000 / 1000)
        for net in computer.Win32_NetworkAdapterConfiguration():
            if net.IPAddress:
                i += 1
                ip = net.IPAddress[0]
        slovar[f'Сетевой адаптер'] = net.Description
        slovar['MAC адрес'] = net.MACAddress
        slovar['IP адрес'] = ip
        slovar['Скорость соединения'] = speed

    def get_user():
        slovar['Пользователь'] = computer.Win32_ComputerSystem()[0].UserName

    def get_os():
        slovar['Установленная ОС'] = computer.Win32_OperatingSystem()[0].Caption

    def get_hardware():
        i = 0
        slovar['Производитель'] = computer.Win32_BaseBoard()[0].Manufacturer
        slovar['Модель'] = computer.Win32_BaseBoard()[0].Product
        slovar['Процессор'] = computer.Win32_Processor()[0].Name
        slovar['Соккет'] = computer.Win32_Processor()[0].SocketDesignation
        slovar['ОЗУ'] = round(int(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1024 / 1024)
        for hdd in computer.Win32_DiskDrive():
            hdd_size = int(int(hdd.Size) / 1024 / 1024 / 1024)
            if hdd.Caption:
                # slovar['Производитель'] = hdd.Model
                # slovar['Емкость диска'] = hdd_size
                slovar.update({
                    f'Диск {i}': {
                        hdd.Model: f'{hdd_size} Gb' }
                })
        for video in computer.Win32_videoController():
            i += 1
            # slovar[f'Видео контроллер {i}'] = video.Description
            slovar.update({
                f'Видео-контроллер {i}': {
                    'наименование': video.Description
                }
            })

    def get_printer():
        i = 0
        caption = []
        port = []
        for items in computer.Win32_Printer():
            i += 1
            # slovar.update({f'Принтер наименование {i}': prn.Caption})
            # slovar.update({f'Порт {i}': prn.PortName})

            slovar.update({
                f'Принтер {i}': {
                f'{items.Caption}': f'{items.PortName}'


                }
                })

    def get_soft():
        i = 0
        for soft in computer.Win32_Product():
            i += 1
            # slovar[f'Наименование ПО {i}'] = soft.Caption
            slovar.update({
                    f'ПО {i}': {
                    f'{soft.Caption}': soft.Caption
                    }
            })

    def file_output():
        with open(f'c:/getinfo/{computer.Win32_ComputerSystem()[0].Name}.txt', 'a',
                  encoding='UTF-8') as file_out:
            for key, val in slovar.items():
                key = str(re.sub(r'[^a-zA-Zа-яА-Я ]', '', key))
                file_out.writelines(f'{key}: {val}; \n')

    def json_output():
        with open('result.json', 'w') as fp:
            json.dump(slovar, fp)

get_info.name_pc()
get_info.get_os()
get_info.get_activate()
get_info.get_user()
get_info.get_network()
get_info.get_hardware()
get_info.get_printer()
get_info.get_soft()
# get_info.file_output()

get_info.json_output()

