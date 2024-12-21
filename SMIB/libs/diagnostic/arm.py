# -*- coding:utf-8 -*-
'''
Created on 8.09.2018 г.

@author: dedal
'''

import os
import time
import subprocess
if __name__ == '__main__':
    from exception import *
else:
    from .exception import *  # @UnusedWildImport


# MAX_TEMP = 65
# MIN_VOLTAGE = 4
# MIN_AMPER = 1.0

class OlimexMicro():
    @staticmethod
    def temp():

        # cmd = 'sudo cat /sys/devices/platform/sunxi-i2c.0/i2c-0/0-0034/temp1_input'
        data = open('/sys/class/thermal/thermal_zone0/temp').read()
        # data = os.popen(cmd).read()
        data = float(data) / 1000
        #         if data >= MAX_TEMP:
        #             raise HideTemp, str(data + ' C')
        return data

    @staticmethod
    def voltage():
        # cmd = 'sudo cat /sys/bus/i2c/devices/0-0034/axp20-supplyer.28/power_supply/ac/voltage_now'
        data = open('/sys/class/power_supply/axp20x-usb/voltage_min').read()
        # data = os.popen(cmd).read()
        data = float(data) / 1000000
        #         if data <= MIN_VOLTAGE:
        #             raise LowVolage, str(data + ' V')
        return data

    @staticmethod
    def network(ip, count=3):
        succees = []
        error = []
        for i in range(count):  # @UnusedVariable
            cmd = 'sudo ping -c 1 %s' % (ip)
            response = subprocess.call(cmd.split())
            time.sleep(2)
            if response == 0:
                succees.append(response)
            else:
                error.append(response)

        if len(succees) == count:
            return True
        else:
            try:
                error = (float(len(error)) / float(count)) * 100
            except ZeroDivisionError:
                return True
            else:
                if error >= 40:
                    return False
        return error

    @staticmethod
    def amper():
        # cmd = 'sudo cat /sys/bus/i2c/devices/0-0034/axp20-supplyer.28/power_supply/ac/current_now'
        data = open('cat /sys/class/power_supply/axp20x-usb/current_max').read()
        # data = os.popen(cmd).read()
        data = float(data) / 100000
        #         if data <= MIN_AMPER:
        #             raise LowAmper, str(data + ' A')
        return data

    @staticmethod
    def get_real_ip():
        import requests
        return requests.get('https://checkip.amazonaws.com').text.strip()

# print (OlimexMicro.network('192.168.1.1'))
