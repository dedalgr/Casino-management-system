# -*- coding:utf-8 -*-
'''
Created on 19.11.2018 г.

@author: dedal
'''

import libs.db.exception
from libs.db.file_db import SQLite
from libs.db.exception import NoSQLiteDB, EmptyDB
from libs.db.mem_db import DictDB
import os
# try:
from libs.eeprom import CBOR
# except ImportError:
#     os.system('sudo mount -o remount rw /')
#     os.system('sudo mount -o remount rw /var')
#     os.system('sudo pip install eeprom')
#     cmd = "sudo sed -i 's/%s/%s/g' /usr/local/lib/python3.9/dist-packages/eeprom/eeprom.py" % ('addr=0', 'addr=31')
#     os.system(cmd)
#     cmd = "sudo sed -i 's/%s/%s/g' /usr/local/lib/python3.9/dist-packages/eeprom/cbor_eeprom.py" % ('for x in range(0, self._size, self._chunk_size):', 'for x in range(31, self._size, self._chunk_size):')
#     os.system(cmd)
#     os.system('sudo reboot')
# os.system('sudo chmod 777 /sys/bus/i2c/devices/1-0050/eeprom')

class NewDB():

    def new(self):
        game_disable = []
        working_module = {
            'keysystem': False,
            'rfid': True,
            'jackpot': True,
            'sas': True,
            'bonus_cart': True,
            'client_cart': True
        }
        keysystem = {
            'credit_id': '',
            'report_id': '',
            'admin_id': '',
            'owner_id': ''
        }
        #         else:
        multi_keysystem = {
            'credit_id': [],
            'report_id': [],
            'admin_id': [],
            'owner_id': []
        }
        bonus_cart = {
        }

        bonus_error_log = []
        # bonus_error = []
        player_bonus_hold = []
        reserve_for = []

        self.set('JACKPOT', 1)
        self.set('GAME_DISABLE', game_disable)
        self.set('DISABLE_GAME_JP', [])
        self.set('WORKING_MODULE', working_module)
        self.set('KEYSYSTEM', keysystem)
        self.set('MULTI_KEYSYSTEM', multi_keysystem)
        self.set('BONUSCART', bonus_cart)
        self.set('OUT_COMPENSATION', 0)
        self.set('SAS_SECURITY', None)
        self.set('BONUS_ERROR_LOG', bonus_error_log)
        self.set('PLAYER', False)
        self.set('PLAYER_BINUS_HOLD_ERROR', player_bonus_hold)
        self.set('PLAYER_ERROR', [])
        self.set('PLAYER_RESERVE', reserve_for)
        self.set('PLAYER_BONUS_REVERT', [0, 0])
        self.set('AFT_TRANSACTION', 0)
        self.sync()

    def update(self):
        try:
            aft_transaction = self.get('AFT_TRANSACTION')
            if not aft_transaction:
                self.set('AFT_TRANSACTION', 1)
                self.sync()
        except:
            self.set('AFT_TRANSACTION', 1)
            self.sync()

class EEPROM_DB(CBOR, NewDB):
    def __init__(self, types="24c01", device=1, adress=0x50):
        CBOR.__init__(self, types=types, device=device, adress=adress)
        if not self.keys():
            self.erese()
            self.new()
        else:
            self.update()

    def load(self):
        self.open()

    def update(self):
        pass

class RealDB(SQLite, NewDB):
    def __init__(self, path, my_crypt=None, use_json=True):
        self.my_crypt = my_crypt
        self.json = use_json
        self.path = path
        data = None
        # try:
        #     db = Berkeley(name=self.path, crypt=self.my_crypt, use_json=self.json)
        #     data = {}
        #     for i in db.keys():
        #         data[i] = db.get(i)
        #     db.close()
        #     os.system('rm %s' % (self.path))
        # except:
        #     pass
        # self.my_crypt = None
        try:
            SQLite.__init__(self, name=self.path, crypt=None, use_json=self.json)
            self.open()
        except EmptyDB:
            open(self.path, 'a').close()
            SQLite.__init__(self, name=self.path, crypt=None, use_json=self.json)
            self.open()
            self.new_table()
            self.new()
        if data != None:
            for i in data:
                self.set(i, data[i])
        self.update()

    def load(self):
        SQLite.__init__(self, name=self.path, crypt=None, use_json=self.json)


class MemDB(DictDB):
    def __init__(self, dump_db):
        DictDB.__init__(self, dump_db=dump_db)
        self.set('STATUS', 'OK')
        # self.set('PLAYER_RESET', False)


if __name__ == '__main__':
    db = RealDB('test.db')
    print(db.get('GAME_DISABLE'))
