from marshmallow import *
from wmi import WMI
import re
import subprocess
import json

computer = WMI()
slovar = {}
slovar2 = {}
arr = []
arrCapt =[]
arrPort = []
arrPort2 = []
i = 0

# def json_add():
#     for items in computer.Win32_Printer():
#         if items.Default:
#             slovar[items.Caption] = items.PortName
#             print(items.Default)
#     slovar2['Принтера'] = slovar
#     data = json.dumps(slovar2)
#     return data
#
# # чтение json
# item = json.loads(json_add())
# for key, value in item['Принтера'].items():
#     print(key, value)

# for video in computer.Win32_videoController():
#     i += 1
#     print(video)
#     slovar2[video.VideoProcessor] = video.Description
# slovar['Видео'] = slovar2
#
# print(slovar)

# i = 0
# arr = {}1
# for soft in computer.Win32_Product():
#     i += 1
#     # slovar[f'Наименование ПО {i}'] = soft.Caption
#     # arr[soft.Caption] = soft.
#     # arr.update({
#     #                 f'ПО {i}': {
#     #                 f'{soft.Caption}': soft.Caption
#     #                 }
#     #         })
#     print(soft)

# with open('result.json', 'r') as fs:
#     data = json.load(fs)
#     print(data['Сеть']['IP адрес'])
#     # for key, value in data.items():
#     #     print(key, value)
# e = computer.Win32_Processor().SocketDesignation
#
# for items in e:
#     print(items)

def get_os():
    slovar = {}
    slovar['Установленная ОС'] = computer.Win32_OperatingSystem()[0].Caption
    data = json.dumps(slovar)
    return json.dumps(slovar)


a = json.loads(get_os())
print(a)