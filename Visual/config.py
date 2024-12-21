# -*- coding:utf-8 -*-
import libs.config
import os
import sys
from libs.cr import *
import libs.rsa

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
def debug():
    # return False
    return BASE_DIR == '/home/dedal/Colibri/Visual'


sys.path.append(os.path.abspath(os.path.join(os.path.abspath('.'))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
DEBUG = debug()
VERSION = '2_1'
IN_THREAD = False
CONF_FILE = 'visual.conf'
LOG_FILE = 'visual.log'
ROOT_PATH = os.getcwd()

KEY = '''vc3Qtq+Qf0k7PJSwDlJKw44HpS/+jU6+dFMRxCuy6g5Hw235NLAS5YAa1c/FPboGNCfUGnW/shvpQIEfGuTYpgHgXH3M9s47jTvs9tRsof/bhH1Lrk+cZrKfLp8vaGvNTiiMYGz1Uyv2tyylkGUA5tY1c4MA/v7O3eZnk1OeLvVVqqLxr5cxOf45jKCX+hxV2skR9H2qAYXMTiwmjwVRMjlvbyMyCxxS3DeUvdoFibCcw12f/D1nbIa6sHFXNY9U9/gp4m9+Xt5xyw6SRotllTQxX2zoBfAnYXftL3VHSAcStPiYyd2EocUd738Fvj1u'''
RAND_KEY = '''KRJGxB0HYzmWFxoZxYwnMxDz9ZRu6dA50hC-SwVelKsV9_i2nbJOEGVCeN8rhRXsF3nNtxz7m5KDUMnAUBGhcov4l5uC66PgGIgQjPXOhXITsliUbH51J4eR050VPSURyF492TYXfC_BeQIR4qyGozWhfl2vULIkng48vvLSGF2v2g9tsk417I9RFbs-DV4fGPFpNqFnKXeXysUN4el_vknSPyiSrhJ1aM6x1zD3TeDqqpbdybhUIF8-05L0u4k06csbz5xkOaKeDkm98aVIfoB81-BpQljkzNc1Ou6D8J5TvSaWF13JAGKJlj9fCbrRE4ieU_oLC-9QbC0F2Vfzaj7f5lZUh47w6PmgqGUJdgQrGxugx4nsZwXKqO26qjmt4n1faqjqk36nZruXGhMBltqVQ5SEJFfzC7lXpjlPuwXuJ0qbLuMoHnQ3sI8R3ViqMfs0Q0UkdXqu-VlzQM0mEQ=='''

PRIVATE_KEY = '''-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----'''

RSA = libs.rsa.RSAKey()
RSA.load_key(PRIVATE_KEY)

def vector_generator(**kwargs):
    global COMUNICATION
    global IV
    global DB
    global EMPTY1
    global EMPTY2
    # holder = shelve.open(holder, 'r')
    key = KEY
    key2 = RAND_KEY
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

class ConfFile(libs.config.ConfFile):

    def __init__(self, conf_file):
        try:
            libs.config.ConfFile.__init__(self, conf_file)
            self.option_update()
        except libs.config.NotConfigFile:
            libs.config.ConfFile.__init__(self, conf_file, make_new=True)
            self.new()

    def option_update(self):
        try:
            self.get('SYSTEM', 'visual_micro', 'bool')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', visual_micro=True)
        try:
            self.get('LOG', 'file_handler', 'bool')
        except libs.config.NoOptionError:
            self.add_option('LOG', file_handler=False)

        try:
            self.get('SYSTEM', 'field_active', 'bool')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', field_active=False)
        try:
            self.get('BACKGROUND', 'anime', 'int')
        except libs.config.NoSectionError:
            self.add_section('BACKGROUND')
            self.add_option('BACKGROUND', anime=1)
        try:
            self.get('SYSTEM', 'name', 'str')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', name='')

        try:
            self.get('FIELD', 'field_active', 'bool')
        except libs.config.NoSectionError:
            self.add_section('FIELD')
            self.add_option('FIELD', field_active=False)
            self.add_option('FIELD', color_name=False)

        try:
            self.get('FONT', 'name', 'int')
        except libs.config.NoSectionError:
            self.add_section('FONT')
            self.add_option('FONT', name=1)

        try:
            self.get('SYSTEM', 'pygame', 'bool')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', pygame=True)

    def new(self):
        self.add_section('SYSTEM')
        self.add_option('SYSTEM', version='2.1')
        self.add_option('SYSTEM', rev='0')
        self.add_option('SYSTEM', name='')
        self.add_option('SYSTEM', ip='None')
        self.add_option('SYSTEM', tz='Europe/Sofia')
        self.add_option('SYSTEM', mony='BGN')
        self.add_option('SYSTEM', sum_runner_rnage=False)
        self.add_option('SYSTEM', chk_alige_interval=60)
        self.add_option('SYSTEM', visual_micro=True)
        self.add_option('SYSTEM', pygame=True)


        self.add_section('LOG')
        self.add_option('LOG', log_level='WARNING')
        self.add_option('LOG', file_handler=False)

        self.add_section('UDP')
        self.add_option('UDP', udp_timeout=10)
        self.add_option('UDP', udp_port=2552)
        self.add_option('UDP', jp_server_ip='192.168.1.5')
        self.add_option('UDP', jp_server_port=2522)
        self.add_option('UDP', iv_jump=False)
        self.add_option('UDP', buffer=4096)

        self.add_section('Q')
        self.add_option('Q', q_timeout=15)
        self.add_option('Q', q_max_count=100)

        self.add_section('BACKGROUND')
        self.add_option('BACKGROUND', anime=1)

        self.add_section('FIELD')
        self.add_option('FIELD', field_active=True)
        self.add_option('FIELD', color_name=False)

        self.add_section('FONT')
        self.add_option('FONT', name=1)

CONF = ConfFile(CONF_FILE)

IP = CONF.get('SYSTEM', 'ip', 'str')
PYGAME = CONF.get('SYSTEM', 'pygame', 'bool')
TZ = CONF.get('SYSTEM', 'tz', 'str')
MONY = CONF.get('SYSTEM', 'mony', 'str')
SUM_RUNNER = CONF.get('SYSTEM', 'sum_runner_rnage', 'bool')
ALIFE_INTERVAL = CONF.get('SYSTEM', 'chk_alige_interval', 'int')
VISUAL_MICRO = CONF.get('SYSTEM', 'visual_micro', 'bool')

LOG_LEVEL = CONF.get('LOG', 'log_level', 'str')
FILE_HANDLER = CONF.get('LOG', 'file_handler', 'bool')

IV_JUMP = CONF.get('UDP', 'iv_jump', 'bool')
key = vector_generator(iv_jump=IV_JUMP)
if IV_JUMP is False:
    CRYPT = Crypt(COMUNICATION, IV, IV_JUMP)
else:
    CRYPT = CryptFernet(key)

UDP_TIMEOUT = CONF.get('UDP', 'udp_timeout', 'int')
SELF_PORT = CONF.get('UDP', 'udp_port', 'int')
JP_IP = CONF.get('UDP', 'jp_server_ip', 'str')
JP_PORT = CONF.get('UDP', 'jp_server_port', 'int')
UDP_BUFFER = CONF.get('UDP', 'buffer', 'int')

Q_TIMEOUT = CONF.get('Q', 'q_timeout', 'int')
Q_MAX_COUNT = CONF.get('Q', 'q_max_count', 'int')
BACKGROUND_ANIME = CONF.get('BACKGROUND', 'anime', 'int')
FIELF_ACTIVE = CONF.get('FIELD', 'field_active', 'bool')
FIELF_COLOR_NAME = CONF.get('FIELD', 'color_name', 'bool')

FONT = CONF.get('FONT', 'name', 'int')