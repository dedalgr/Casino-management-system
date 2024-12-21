#-*- coding:utf-8 -*-
'''
Created on 4.03.2018 г.

@author: dedal
'''
import traceback
import conf  # @UnresolvedImport
import db  # @UnresolvedImport
from . import log
import os

# try:
#     os.system('cp jp.db backup/')
#     hard_db = db.db.Berkeley()
#     all_key = hard_db.keys()
#     data = {}
#     for i in all_key:
#         data[i] = hard_db.get_key(i)
#     os.system('rm jp.db')
#     hard_db = db.db.SQLite()
#     for i in data:
#         hard_db.set_key(i, data[i])
#     global_ip = hard_db.get_key('casino_name')
#     if 'ip' not in global_ip:
#         global_ip['ip'] = ''
#         hard_db.set_key('casino_name', global_ip)
#     hard_db.sync()
#     hard_db.close()
# except:
#     pass
# try:
#     os.system('cp log.db backup/')
#     hard_db = db.db.Berkeley('log.db')
#     try:
#         all_key = hard_db.get_key('log')
#         hard_db.close()
#         data = {}
#         for i in all_key:
#             for b in all_key[i]:
#                 if b not in data:
#                     data[b] = {}
#                 data[b][i] = all_key[i][b]
#     except KeyError:
#         pass
#
#     os.system('rm log.db')
#     hard_db = db.db.SQLite('log.db')
#     for i in data:
#         hard_db.set_key(i, data[i])
#     hard_db.sync()
#     hard_db.close()
# except Exception as e:
#     pass
DB = db.db.MemDB()

EXCEPTION_MSG = {
    'UNCNOWN':-1,
    'INIT':1,
    'BAD CRC': 2,
    'BAD LINUX':3,
    'LICENSE OUT OF DATE': 4,
    'BAD HW UUID':5,
    'WRONG VERSION': 6,
    'BAD DATE TIME': 7,
    'BAD DB': 8,
    'BAD INIT TIME': 9,
    'LOST CONNECTION': 0,
    'VISUAL NO GRUP': 10,
    'EEPROM DATA IS WRONG': 11,
    'NO EEPROM': 12,
    'NO RTC': 13,
    'BAD LINUX NETWORK TIME': 14,
    'BAD LINUX RC LOCAL TIME': 15,
    'BAD BACKUP DB': 16,
    'NO HW ID': 17,
    'HW IS NONE': 18,
    'BAD VISUAL CRC': 50,
    'LOST_GLOBAL_SERVER': 40,
}

ACTIV_TYPE = {'naem':True, 'buy': False}

class Inside_Except(Exception):
    def __init__(self, msg='No Message'):
        self.msg = msg
        # print '-' * 20
        if conf.ERR_MSG_LOG == False:
            print(traceback.print_stack())
        print('MESSAGE: %s' % (self.msg))
        # print '-' * 20
        
    def __str__(self):
        return repr(self.msg)
    
class Server_Block_Except(Exception):
    def __init__(self, msg='No Message'):
        self.msg = msg
        DB.set_key_to('work', 'can_work', False)  
        DB.set_key_to('work', 'error', EXCEPTION_MSG[self.msg])  
        DB.set_key_to('work', 'work_to', None)  
        # print '-' * 20
        if conf.ERR_MSG_LOG == False:
            print(traceback.print_stack())
        print('MESSAGE: %s' % (self.msg))
        # print '-' * 20
        
    def __str__(self):
        return repr(self.msg)
    

class UncnownError(Server_Block_Except):
    pass

class DBError(Server_Block_Except):
    pass

class EEPROMError(Server_Block_Except):
    pass

class HWUUIDError(Server_Block_Except):
    pass

class CRCError(Server_Block_Except):
    pass

class LinuxError(Server_Block_Except):
    pass

class LicenseError(Server_Block_Except):
    pass

class DateTimeError(Server_Block_Except):
    pass

class BadSecurity(Server_Block_Except):
    pass
