# -*- coding:utf-8 -*-
'''
Created on 27.02.2019

@author: dedal
'''
import sys
import pyglet
from pyglet.window import key
from pyglet.window import mouse
import json
import log
from pymemcache.client.base import PooledClient as mem_Client
import os
import gettext
import time
os.nice(5)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))


def DebugOptions():
    return BASE_DIR == '/home/dedal/Colibri/SMIB/2_1'


DEBUG = DebugOptions()


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value.decode()
    if flags == 2:
        return json.loads(value)
    print("Unknown serialization format")


# if DEBUG is True:
#     CLIENT = mem_Client(('192.168.1.11', 11211), serializer=json_serializer, deserializer=json_deserializer)
#     LOGO_NAME = 'colibri-logo.png'
# else:
CLIENT = mem_Client(('127.0.0.1', 11211), serializer=json_serializer, deserializer=json_deserializer)

locale_folder = BASE_DIR + '/locale'
gettext.install('messages', locale_folder, names=['ugettext'], codeset='utf-8')
# gettext.install('messages', locale_folder, unicode=True, names=['ugettext'], codeset='utf-8')
if DEBUG is False:
    LANG = None
    while LANG == None:
        LANG = CLIENT.get('USE_LANGUAGE')
        time.sleep(2)
    lang = gettext.translation('messages', 'locale', fallback=True, languages=[LANG])
else:
    lang = gettext.translation('messages', 'locale', fallback=True, languages=['bg'])
lang.install()

# if DEBUG is False:
#     LOGO_NAME = None
#     while LOGO_NAME == None:
#         LOGO_NAME = CLIENT.get('LOGO_NAME')
#     # if LOGO_NAME == 'BREAK':
#     #     sys.exit()
# else:
LOGO_NAME = 'colibri-logo.png'
USE_ANIME = None
ANIME_NIM = None
MY_RANGE = None
if DEBUG is False:
    while USE_ANIME == None:
        USE_ANIME = CLIENT.get('use_anime')
        time.sleep(2)
    while ANIME_NIM == None:
        ANIME_NIM = CLIENT.get('anime_num')
        time.sleep(2)
    while MY_RANGE == None:
        MY_RANGE = CLIENT.get('anime_range')
        time.sleep(2)

# else:
#     USE_ANIME = False
#     ANIME_NIM = '1'
#     MY_RANGE = [0,0]

skin = CLIENT.get('skin')
if skin == 1:
    from yellow_skin import *
elif skin == 2:
    from blue_skin import *
else:
    from blue_skin import *

pyglet.app.run()
