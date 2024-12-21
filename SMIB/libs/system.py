#-*- coding:utf-8 -*-
'''
Created on 12.09.2018 г.

@author: dedal
'''
import os

def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

def get_ip(**kwargs):
    f = os.popen('sudo ifconfig | grep "192.168" | cut -d" " -f10')
    your_ip = f.read()
    if your_ip[:-1] == '192.168.2.11':
        return '192.168.1.11'
    return your_ip[:-1]