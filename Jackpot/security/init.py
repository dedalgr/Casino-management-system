#-*- coding:utf-8 -*-
from . import mk_uuid

import os
import time
import rtc  # @UnresolvedImport
from db import db  # @UnresolvedImport
import exception  # @UnresolvedImport
import datetime

DB = db.MemDB()

def Start_CHK():
    init = DB.get_key('INIT')  
    # network = os.path.getmtime('/etc/network/interfaces')
    # network = time.gmtime(network)
    init_time = time.gmtime(init['init_time'])
    init_time = datetime.datetime(*init_time[:6])
    work_to = DB.get_key('work')  
#     rclocal = os.path.getmtime('/etc/rc.local')
#     rclocal = time.gmtime(rclocal)
    #holder = os.path.getmtime('/var/local/holder.so')
    #holder = time.gmtime(holder)
    eeprom = None
    try:
        eeprom=rtc.Read_RTC()
        eeprom = "%d-%d-%d %d:%d:%d" % (eeprom.year, eeprom.month, eeprom.day, eeprom.hour, eeprom.minute, eeprom.second)
    except IOError:
        try:
            raise exception.EEPROMError('NO RTC')
        except exception.EEPROMError:
            pass
    except:
        try:
            raise exception.UncnownError('INIT')
        except exception.UncnownError:
            pass 
    else: 
        try:
            if eeprom == None:
                raise exception.EEPROMError('NO RTC')
            elif eeprom != "%d-%d-%d %d:%d:%d" % (init_time.year, init_time.month, init_time.day, init_time.hour, init_time.minute, init_time.second) or eeprom == '2065-25-45 45':
                raise exception.EEPROMError('BAD DATE TIME')
            elif mk_uuid.chk_hw_uuid(init['hw_uuid']) == False:
                raise exception.HWUUIDError('BAD HW UUID')
            elif mk_uuid.chk_crc(init['crc']) == False:
                raise exception.CRCError('BAD CRC')
            elif time.time() < init['init_time']:
                raise exception.DateTimeError('BAD INIT TIME')
            # elif network.tm_year > init_time.year:
            #     raise exception.LinuxError, 'BAD LINUX NETWORK TIME'
            # elif network.tm_year == init_time.year:
            #     if network.tm_mon > init_time.month:
            #         raise exception.LinuxError, 'BAD LINUX NETWORK TIME'
            #     elif network.tm_mon == init_time.month:
            #         if network.tm_mday > init_time.day + 1:
            #             raise exception.LinuxError, 'BAD LINUX NETWORK TIME'
#             elif rclocal.tm_year > init_time.year:
#                 raise exception.LinuxError, 'BAD LINUX RC LOCAL TIME' 
#             elif rclocal.tm_year == init_time.year:
#                 if rclocal.tm_mon > init_time.month:
#                     raise exception.LinuxError, 'BAD LINUX RC LOCAL TIME'  
#                 elif rclocal.tm_mon == init_time.month:
#                     if rclocal.tm_mday > init_time.day + 1:
#                         raise exception.LinuxError, 'BAD LINUX RC LOCAL TIME' 
            elif work_to['work_to'] != None:
                naem()
                
        except exception.Server_Block_Except:
            DB.close()
            return False
        else:
            DB.close()
            return True

def naem():
    work = DB.get_key('work')  
    init = DB.get_key('INIT')  
    DB.close()
    try:
        if init['init_time'] > time.time():
            raise exception.DateTimeError('BAD INIT TIME')
        if work['work_to'] != None:  
            if work['work_to'] < time.time():
                raise exception.LicenseError('LICENSE OUT OF DATE')
    except exception.Server_Block_Except:
        return False
    return True
