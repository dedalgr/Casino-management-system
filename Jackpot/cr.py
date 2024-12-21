#-*- coding:utf-8 -*-
'''
Created on 18.02.2018 г.
@author: dedal
Ключ за криптиране!
'''
from Cryptodome import Random
from Cryptodome.Cipher import AES
import os
# import shelve
import base64
import zlib
from cryptography.fernet import Fernet
import conf

crc_key = '''-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----'''

COMUNICATION= None
IV = None
EMPTY1 = None
DB = None
EMPTY2 = None

class NoKey(Exception):
    pass


def vector_generator(**kwargs):
    global COMUNICATION
    global IV
    global DB
    global EMPTY1
    global EMPTY2
    # holder = shelve.open(holder, 'r')
    key = conf.KEY
    key2 = conf.RAND_KEY
    # holder.close()
    key = base64.b64decode(key)
    COMUNICATION = key[0:8]+key[150:158]+key[64:72]
    EMPTY1 = key[64:96]
    EMPTY2 = key[128:160]
    DB = key[192:224]
    IV = key[224:256]
    if 'iv_jump' in kwargs:
        if kwargs['iv_jump'] == True:
            crypts = Crypt(COMUNICATION, IV, True, False)
            key2 = crypts.decrypt(key2)
            count = 0
            key3 = ''
            # raise KeyError(bytes.(key2[0]))
            for i in key2:
                # raise KeyError(i, chr(i))
                if count == 3:
                    key3 += chr(i)
                count += 1
                if count > 3:
                    count = 0
            key3 = key3[0:44]
            # raise KeyError(len(key3))
            return key3
    return True

class CryptFernet():
    def __init__(self, key, **kwargs):
        self.key = key
        self.fernet = Fernet(self.key)

    def encrypt(self, my_message):
        my_message = zlib.compress(my_message.encode('utf8'))
        return self.fernet.encrypt(my_message)

    def decrypt(self, my_message):
        my_message = self.fernet.decrypt(my_message)
        return zlib.decompress(my_message)


class Crypt():
    def __init__(self, key, iv, iv_jump=False, compress=True):
        self.key = key
        self.iv = iv
        self.bs = 16
        self.iv_jump = iv_jump
        self.compress = compress

    def encrypt(self, my_message):
        if self.compress:
            my_message = zlib.compress(my_message.encode('utf8'))
        if self.iv_jump == False:
            obj = AES.new(self.key, AES.MODE_CFB, self.iv)
        else:
            Random.atfork()
            raw = self._pad(my_message)
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return base64.urlsafe_b64encode(iv + cipher.encrypt(raw))
        return obj.encrypt(my_message)

    def decrypt(self, my_message):
        if self.iv_jump == False:
            obj2 = AES.new(self.key, AES.MODE_CFB, self.iv)
        else:
            enc = base64.urlsafe_b64decode(my_message.encode('utf-8'))
            iv = enc[:self.bs]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            my_message = self._unpad(cipher.decrypt(enc[self.bs:]))
            if self.compress:
                return zlib.decompress(my_message)
            else:
                return my_message
        # my_message = bytes.hex(my_message)
        my_message = obj2.decrypt(my_message)
        # raise KeyError(zlib.decompress(my_message))
        if self.compress:
            return zlib.decompress(my_message)
        return my_message

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    @staticmethod
    def vector_maker():
        return Random.new().read(AES.block_size)

    @staticmethod
    def key_maker(key_len=32):
        return os.urandom(key_len)

    # @staticmethod
    # def write_key_to_shelve(keys, path):
    #     holder = shelve.open(path, 'c')
    #     holder['key'] = keys
    #     holder.close()
    #     return True

    @staticmethod
    def new_key(add_iv=True):
        return base64.b64encode(
            Crypt.key_maker() + Crypt.key_maker() +
            Crypt.key_maker() + Crypt.key_maker() +
            Crypt.key_maker() + Crypt.key_maker() +
            Crypt.key_maker() + Crypt.vector_maker()
        )

key = vector_generator(iv_jump=True)
