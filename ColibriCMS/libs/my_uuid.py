# -*- coding:utf-8 -*-
'''
Created on 14.05.2017 г.

@author: dedal
'''

import uuid
# import crcmod
import os
import time
# import random
import datetime

if os.name == 'posix':
    import smbus


# from conf import *
# POLY = 0x104c11db7
# CONST = 0xfe7830a5

# def crc(data, poly):
#     crc32 = crcmod.Crc(poly, initCrc=0, xorOut=0xFFFFFFFFFFFFFFFF)
#     crc32.update(data)
#     return crc32.hexdigest()

class EEPROMError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class BadSoftCRC(Exception):
    pass


def read_db_n():
    if os.name == 'posix':
        var = os.popen('df -h | grep -w /').read()
        var = var.split()
        cmd = 'udevadm info --query=all --name=%s | grep ID_SERIAL=' % (var[0])
        data = os.popen(cmd).read()
        data = data.replace('E: ID_SERIAL=', '')
        return data[2:-1]
    else:
        var = os.popen('vol').read()
        var = var.split()
        return var[-1]


def hw_uuid():
    '''
    Генерира уникален номер на база серийния номер на процесора.
    Използва getserial
    :return: Уникален идентификатор на компютъра
    '''
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, read_db_n()))


def mk_soft_id():
    '''
    Генерира уникален номер на софтуера
    :return: Уникален номер на софтуера
    '''
    return str(uuid.uuid4())


def chk_hw_uuid(machine_uuid):
    '''
    Проверява дали компютъра е купен от нас.
    В монмента не се използва при smib модула.
    :param machine_uuid: Взима уникалния номер на машината.
    Използва getserial и сравнява.
    :return: True или False
    '''
    return machine_uuid == str(uuid.uuid5(uuid.NAMESPACE_DNS, read_db_n()))


if __name__ == '__main__':
    print(hw_uuid())
