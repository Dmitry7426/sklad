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

# for items in computer.Win32_Printer():
#     slovar[items.Caption] = items.PortName
#
#
# slovar2['Принтера'] = slovar
#
#
# print(slovar2)
i = 0
arr = {}
for soft in computer.Win32_Product():
    i += 1
    # slovar[f'Наименование ПО {i}'] = soft.Caption
    # arr[soft.Caption] = soft.
    # arr.update({
    #                 f'ПО {i}': {
    #                 f'{soft.Caption}': soft.Caption
    #                 }
    #         })
    print(soft)
