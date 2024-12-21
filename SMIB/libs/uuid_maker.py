# -*- coding:utf-8 -*-
'''
Created on 27.04.2018 г.

@author: dedal
'''
import smbus
import os
import crcmod
import uuid
import random

# ROOT_PATH = os.getcwd()
POLY = 0x104c11db7


class EEPROMError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class NoCPUSerial(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class BadSoftCRC(Exception):
    pass


def read_emmc_n():
    cmd = 'sudo udevadm info --query=all --name=%s | grep ID_SERIAL=' % ('/dev/mmcblk0p1')
    data = os.popen(cmd).read()
    data = data.replace('E: ID_SERIAL=', '')
    return data[2:-1]


def read_cpu_n():
    cmd = "cat /proc/cpuinfo | grep 'Serial'"
    data = os.popen(cmd).read()[:-1]
    data = data.replace(' ', '')
    data = data.replace('Serial', '')
    data = data.replace(' ', '')

    if data != '00000000':
        return data
    else:
        raise NoCPUSerial('NO CPU SERIAL')


def set_eeprom_data(bus=1, col=0x51, row=0x02, buf=[]):
    bus = smbus.SMBus(bus)
    bus.write_i2c_block_data(col, row, buf)
    return True


def read_eeprom_data(bus=1, col=0X51, row=0x02, read_len=7):
    try:
        bus = smbus.SMBus(bus)
        buf = bus.read_i2c_block_data(col, row, read_len)
        var = ''
        for i in buf:
            var += hex(i)
    except:
        raise EEPROMError('NO EEPROM BUS')
    return var.replace('0x', '')


def hw_uuid():
    '''
    Генерира уникален номер на база серийния номер на процесора.
    Използва getserial
    :return: Уникален идентификатор на компютъра
    '''
    #try:
    #    return str(uuid.uuid5(uuid.NAMESPACE_DNS, read_cpu_n()))
    #except NoCPUSerial:
    #    try:
    #        return str(uuid.uuid5(uuid.NAMESPACE_DNS, read_eeprom_data()))
    #    except EEPROMError:
    #        pass
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, 'no_hw_smib' + read_emmc_n()))


def get_namespase_dns():
    return uuid.NAMESPACE_DNS


def mk_soft_id():
    '''
    Генерира уникален номер на софтуера
    :return: Уникален номер на софтуера
    '''
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, read_emmc_n()))


def crc(data, poly):
    crc32 = crcmod.Crc(poly, initCrc=0, xorOut=0xFFFFFFFFFFFFFFFF)
    # raise KeyError(type(data))
    crc32.update(data)
    return crc32.hexdigest()


def get_files(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):  # @UnusedVariable
        for filename in files:
            filepath = os.path.join(root, filename)
            if filepath[-3:] == '.db':
                pass
            elif filepath[-5:] == '.conf':
                pass
            elif filepath[-4:] == '.log':
                pass
            elif 'gui_client' in filepath:
                pass
            elif '.svn' in filepath:
                pass
            else:
                file_paths.append(filepath)
    return file_paths


def mk_crc(path=None, string=False):
    if path == None:
        path = os.getcwd()
    files = get_files(path)
    math_crc = ''
    for i in files:
        # print (i)
        # if i[-3:] != '.db' and i[-5:] != '.conf' and i[-4:] != '.log' and 'gui_client' not in i:
        math_crc = math_crc + crc(open(i, 'rb').read(), POLY)
    math_crc = crc(math_crc.encode('utf-8'), POLY)
    if string == True:
        return math_crc
    return int(math_crc, 16)


def chk_crc(crc_to_chk, path, string=False, poly=POLY):
    new_crc = mk_crc(path, string, poly)
    if crc_to_chk == new_crc:
        return True
    else:
        return False

