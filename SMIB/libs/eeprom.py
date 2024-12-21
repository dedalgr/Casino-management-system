from eeprom import CBOR_EEPROM
import datetime  # @UnusedImport
import threading
import json

class CBOR():
    def __init__(self, types="24c01", device=1, adress=0x50):
        self.types = types
        self.device = device
        self.adress = adress
        self.lock = threading.Lock()
        self.eeprom = CBOR_EEPROM(self.types, self.device, self.adress)

    def open(self):
        return self.eeprom.open()

    def close(self):
        return True

    def sync(self):
        return True

    def acquire(self, in_loop=True):
        return self.lock.acquire(in_loop)

    def release(self):
        if self.isLock() == True:
            return self.lock.release()
        return True

    def isLock(self):
        return self.lock.locked()

    def get(self, key):
        return self.eeprom.get(key)

    def set(self, key, data={}):
        self.eeprom.put(key, data)
        return self.update_keys(key)

    def dell(self, key):
        tmp = self.eeprom.get('keys')
        tmp2 = []
        for i in tmp:
            if i != key:
                tmp2.append(self.eeprom.get(i))
        del tmp['key']
        self.erese()
        for i in tmp:
            self.eeprom.put(tmp2[i])
        self.eeprom.put('keys', tmp)
        return True

    def erese(self):
        self.eeprom.erase_file()
        return True

    def keys(self):
        tmp = self.eeprom.get('keys')
        if not tmp:
            self.eeprom.put('keys', [])
            return []
        return self.eeprom.get('keys')

    def update_keys(self, key_name):
        tmp = self.eeprom.get('keys')
        if not tmp:
            self.eeprom.put('keys', [])
            tmp = []
        if key_name not in tmp:
            tmp.append(key_name)
            self.eeprom.put('keys', tmp)
        return True

