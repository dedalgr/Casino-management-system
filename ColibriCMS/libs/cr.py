#-*- coding:utf-8 -*-
'''
Created on 20.02.2018 г.

@author: dedal
'''
from Cryptodome import Random
from Cryptodome.Cipher import AES
# import shelve
import os
import base64
if not __package__:
    import conf
else:
    from . import conf
import zlib
from cryptography.fernet import Fernet

COMUNICATION= None
IV = None
EMPTY1 = None
DB = None
EMPTY2 = None
Q1 = None

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
            for i in key2:
                if count == 3:
                    key3 += chr(i)
                count += 1
                if count > 3:
                    count = 0
            key3 = str(key3[0:44])
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


key = vector_generator(iv_jump=conf.UDP_IV_JUMP)
