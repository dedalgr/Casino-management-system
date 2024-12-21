#-*- coding:utf-8 -*-
'''
Created on 26.03.2017 г.

@author: dedal
'''

import security  # @UnresolvedImport
import db.db  # @UnresolvedImport
import udp.client  # @UnresolvedImport
import rtc  # @UnresolvedImport
import conf  # @UnresolvedImport
import cr  # @UnresolvedImport
import os

DB = db.db.MemDB()
SEND = udp.client.send

def run_linux_cmd(**kwargs):
    if kwargs['cmd'] == 'REINIT':
        return CHANGE_INIT_DATA(crc=True, init_time=True, soft_uuid=True, hw_uuid=True)
    elif kwargs['cmd'] == 'RTC_write':
        return rtc.Write_RTC()
    elif kwargs['cmd'] == 'RTC_read':
        return rtc.Read_RTC()
    elif kwargs['cmd'] == 'RTC_sync':
        return rtc.Sync_RTC()
    else:
        return os.popen(kwargs['cmd']).read()

def CHANGE_INIT_DATA(**kwargs):
    init = DB.get_key('INIT')
    if 'crc' in kwargs:
        init['crc']  = security.mk_uuid.mk_crc()
    if 'init_time'  in kwargs:
        try:
            rtc.Write_RTC(bus=conf.RTC_Bus, init_write=True)
        except:
            pass
#         init['time'] = time.time()
    if 'soft_uuid'  in kwargs:
        init['soft_uuid'] = security.mk_uuid.mk_soft_id()
    if 'hw_uuid'  in kwargs:
        init['hw_uuid'] = security.mk_uuid.hw_uuid()
    if 'version'  in kwargs:
        init['version'] = kwargs['version']
    DB.set_key('INIT', init)
    DB.close()
    return True

def BASE_KEY(**kwargs):
    return security.mk_uuid.base_code(kwargs['err'])

def ACTIV(**kwargs):
    try:
        chk = security.mk_uuid.activate_code(kwargs['key'], kwargs['base'])
    except ValueError:
        chk = False, None
    except TypeError:
        chk = False, None
    if chk[0] == False:
        return security.mk_uuid.base_code(4)
    else:
        CHANGE_INIT_DATA(crc=True, init_time=True)
        DB.set_key_to('work', 'work', chk[0])  #
        DB.set_key_to('work', 'work_to', chk[1])  #
        DB.set_key_to('work', 'error', 4)  #
        DB.close()
        return CHANGE_INIT_DATA()

def GET_REAL_CRC(**kwargs):
    return security.mk_uuid.mk_crc()

def GET_CRC(**kwargs):
    return int(security.mk_uuid.crc(cr.crc_key, conf.POLY), 16)

def CHK_CRC(**kwargs):
    return security.mk_uuid.chk_crc(DB.get_key('INIT')['crc'])

def SET_NAME(**kwargs):
    DB.set_key('casino_name', {'name':kwargs['name']})  #
    visual = DB.get_key('visual')
    DB.close()
    for item in visual:
        udp.client.send(ip=item, evt='SET_NAME', name={'name':kwargs['name']})
