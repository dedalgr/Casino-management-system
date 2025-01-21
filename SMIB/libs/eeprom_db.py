from . import eeprom
import datetime  # @UnusedImport
import threading
import json
import zlib
from .eeprom import CBOR_EEPROM

class CBOR():
    def __init__(self, types="24c2048", device=1, adress=80, my_keys={}, count=1):
        self.types = types
        self.device = device
        self.adress = adress
        self.lock = threading.Lock()
        self.my_keys = my_keys
        self.count = count
        self.eeprom = CBOR_EEPROM(self.types, self.device, self.adress)
        # self.eeprom._chunk_size = 1790

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
        data = self.eeprom.get(self.my_keys[key])
        return json.loads(zlib.decompress(data))

    def set(self, key, data={}):
        if key not in self.my_keys:
            self.count += 1
            self.my_keys[key] = self.count
        self.eeprom.put(self.my_keys[key], zlib.compress(json.dumps(data).encode('utf-8')))
        return True

    def dell(self, key):
        tmp2 = {}
        for i in self.my_keys:
            if i != key:
                tmp2[i] = self.eeprom.get(self.my_keys[i])
        del self.my_keys[key]
        self.erese()
        for i in self.my_keys:
            self.eeprom.put(self.my_keys[i], tmp2[i])
        # self.eeprom.put('keys', tmp)
        return True

    def erese(self):
        self.eeprom.erase_file()
        return True

    def keys(self):
        # tmp = self.eeprom.get('keys')
        # if not tmp:
        #     self.eeprom.put('keys', {})
        #     return []
        return list(self.my_keys.keys())

    # def update_keys(self, key_name):
    #     tmp = self.eeprom.get('keys')
    #     if not tmp:
    #         self.eeprom.put('keys', {})
    #         tmp = {}
    #     if key_name not in tmp:
    #         count += 1
    #         tmp[key_name] = count
    #
    #         self.eeprom.put('count', count)
    #         self.eeprom.put('keys', tmp)
    #     return True

if __name__ == '__main__':
    import eeprom
    eprom = eeprom.CBOR_EEPROM('24c2048', 1, 80)
    eprom.write(b'\xff' * 2048, addr=0)
    data = b'U\xaaLO\x06\x12\x00\x00J\x00U \x10\x00\x00\xff\x1e\x000289048272BE\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xa3\x1a\x0e\x87'
    eprom.write(data, addr=0)



