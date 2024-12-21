#-*- coding:utf-8 -*-
'''
Created on 27.01.2019 г.

@author: dedal
'''
import conf
import base64
import libs.cr
import threading

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
            crypts = libs.cr.Crypt(COMUNICATION, IV, True, False)
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
