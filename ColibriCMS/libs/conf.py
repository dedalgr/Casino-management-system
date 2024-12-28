#-*- coding:utf-8 -*-
'''
Created on 14.05.2017 г.

@author: dedal
'''
from configparser import ConfigParser
import wx
import os
from subprocess import Popen, PIPE
import socket
import sys
# print (__package__)
if not __package__:
    import my_uuid
    import config
else:
    from . import my_uuid
    from . import config
from threading import Lock
PARENT = None
VERSION = '2_1'
ROOT_PATH = ''
LOCALE_PATH = ROOT_PATH + 'locale/'
IMG_FOLDER = ROOT_PATH + 'img/'
TEMPLATES = ROOT_PATH + 'template/'
# UDP_IV_JUMP = True
# HOLDER = ROOT_PATH + 'holder'
CONF_FILE = ROOT_PATH + 'colibri.conf'
LOG_PATH = ROOT_PATH + 'colibri.log'
DB_LOG_PATH = ROOT_PATH + 'db_colibri.log'
NEW_ORDER= True
BASE_DIR = os.path.dirname(os.path.abspath(LOCALE_PATH))
DOCS = BASE_DIR + '/docs/'
LOCK = Lock()
UNITEST = False

KEY = '''vc3Qtq+Qf0k7PJSwDlJKw44HpS/+jU6+dFMRxCuy6g5Hw235NLAS5YAa1c/FPboGNCfUGnW/shvpQIEfGuTYpgHgXH3M9s47jTvs9tRsof/bhH1Lrk+cZrKfLp8vaGvNTiiMYGz1Uyv2tyylkGUA5tY1c4MA/v7O3eZnk1OeLvVVqqLxr5cxOf45jKCX+hxV2skR9H2qAYXMTiwmjwVRMjlvbyMyCxxS3DeUvdoFibCcw12f/D1nbIa6sHFXNY9U9/gp4m9+Xt5xyw6SRotllTQxX2zoBfAnYXftL3VHSAcStPiYyd2EocUd738Fvj1u'''
RAND_KEY = '''KRJGxB0HYzmWFxoZxYwnMxDz9ZRu6dA50hC-SwVelKsV9_i2nbJOEGVCeN8rhRXsF3nNtxz7m5KDUMnAUBGhcov4l5uC66PgGIgQjPXOhXITsliUbH51J4eR050VPSURyF492TYXfC_BeQIR4qyGozWhfl2vULIkng48vvLSGF2v2g9tsk417I9RFbs-DV4fGPFpNqFnKXeXysUN4el_vknSPyiSrhJ1aM6x1zD3TeDqqpbdybhUIF8-05L0u4k06csbz5xkOaKeDkm98aVIfoB81-BpQljkzNc1Ou6D8J5TvSaWF13JAGKJlj9fCbrRE4ieU_oLC-9QbC0F2Vfzaj7f5lZUh47w6PmgqGUJdgQrGxugx4nsZwXKqO26qjmt4n1faqjqk36nZruXGhMBltqVQ5SEJFfzC7lXpjlPuwXuJ0qbLuMoHnQ3sI8R3ViqMfs0Q0UkdXqu-VlzQM0mEQ=='''

PRIVATE_KEY = '''-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----'''

# if os.name != 'posix':
#     PRINT_FOLDER = r'c:\windows\temp'
# else:
#     PRINT_FOLDER = '/tmp/'

def doc_debug():
    return BASE_DIR == '/home/dedal/Colibri/ColibriCMS/2_1'

DOCS_DEBUG = doc_debug()
#=========================================================================
# Клас за предупреждения в конфигурационния файл
#=========================================================================

def root_cmd(cmd, passwd='vavilon'):
    sudo_password = passwd
    command = '%s' % (cmd)
    command = command.split()
    p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE,
          universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]
    return True

# class ConfWarning(ConfigParser.Error):
#     '''
#         Warning exception!
#         Използва се за повдигане на предупреждение.
#         Приема съобщение.
#         msg = съобщение
#     '''
#
#     pass

#=========================================================================
# Клас за грешки в конфиг файла
#=========================================================================


# class ConfError(ConfigParser.Error):
#     '''Error exception!'''
#
#     pass
#
# class NotConfigFile(Exception):
#     pass

#=========================================================================
# Клас за обработка на конф файл
#=========================================================================


class ConfFile(config.ConfFile):
    '''
    Работа с конфигурационен файл!

    Функции:
        __init__(confName)
        update_option(section, **option)
        add_section(section)
        add_option(section, **option)
        get(section, option = None, return_type = None)
        add_comment(section, comment)

    '''

    def __init__(self, conf_file=CONF_FILE):
        try:
            config.ConfFile.__init__(self, conf_file, False)
            self.option_update()
        except config.NotConfigFile:
            config.ConfFile.__init__(self, conf_file, True)
            self.new()


    def option_update(self):
        # try:
        #     self.get('DB')
        # except:
        #     self.add_section('DB')
        #     self.add_option('DB', connect_timeout=30)
        #     self.add_option('DB', tcp_user_timeout=30)
            # self.add_option('DB', echo_pool=False)
            # self.add_option('DB', pool_reset_on_return=True)
        try:
            self.get('OCR')
        except:
            self.add_section('OCR')
            self.add_option('OCR', worker_port='/dev/rfid')
            self.add_option('OCR', use=False)
        try:
            self.get('OCR', 'desko', 'bool')
        except:
            self.add_option('OCR', desko=False)
        try:
            self.get('KEYSYSTEM', 'change_on_order', 'bool')
        except config.NoOptionError:
            self.add_option('KEYSYSTEM', change_on_order=False)
        try:
            self.get('PRINTER', 'printer_on_server_pos', 'bool')
        except config.NoOptionError:
            self.add_option('PRINTER', printer_on_server_pos=False)
        try:
            self.get('PRINTER', 'print_direct_pos', 'bool')
        except config.NoOptionError:
            self.add_option('PRINTER', print_direct_pos=False)
        try:
            self.get('UDP', 'tcp', 'bool')
        except config.NoOptionError:
            self.add_option('UDP', tcp=False)
        try:
            self.get('UDP', 'iv_jump', 'bool')
        except config.NoOptionError:
            self.add_option('UDP', iv_jump=False)
        try:
            self.get('PRINTER', 'mony_back_on_pos', 'bool')
        except config.NoOptionError:
            self.add_option('PRINTER', mony_back_on_pos=False)
        try:
            self.get('UDP', 'db_port', 'int')
        except config.NoOptionError:
            self.add_option('UDP', db_port=5432)
        try:
            self.get('OCR', 'ocr_timeout', 'int')
        except config.NoOptionError:
            self.add_option('OCR', ocr_timeout=1)
        try:
            self.get('OCR', 'lock', 'bool')
        except config.NoOptionError:
            self.add_option('OCR', lock=False)

    def new(self):
        self.add_section('SYSTEM')
        self.add_option('SYSTEM', debug=False)
        # self.add_option('SYSTEM', user_name=False)
        # CONF.add_option('SYSTEM', pgadmin=False)
        self.add_option('SYSTEM', db_debug=False)
        self.add_option('SYSTEM', fulscreen=False)
        # self.add_option('SYSTEM', bill_out_default=False)
        # self.add_option('SYSTEM', use_dinamic_ip=False)
        # CONF.add_option('SYSTEM', hold_bonus_cart=True)
        self.add_option('SYSTEM', db_iptables=True)
        # CONF.add_option('SYSTEM', db_tunnel_port=0)

        self.add_option('SYSTEM', use_rtc=False)
        self.add_option('SYSTEM', rtc='127.0.0.1')
        # CONF.add_option('SYSTEM', rtc_port=30593)
        # self.add_option('SYSTEM', bill_block=False)
        self.add_option('SYSTEM', rev='0')

        self.add_section('SERVER')
        self.add_option('SERVER', use_server='127.0.0.1')
        self.add_option('SERVER', localhost='127.0.0.1')

        self.add_section('JPSERVER')
        self.add_option('JPSERVER', ip='192.168.1.5')
        self.add_option('JPSERVER', port=2522)

        #     CONF.add_section('JP_ALL_SERVER')
        #     CONF.add_option('JP_ALL_SERVER', localhost='192.1368.1.5')

        self.add_section('UDP')
        self.add_option('UDP', port=30593)
        self.add_option('UDP', buffer=4096)
        # CONF.add_option('UDP', protocol='UDP')
        self.add_option('UDP', timeout=12)
        self.add_option('UDP', tcp=False)
        # CONF.add_option('UDP', rtansfer_server=True)
        # CONF.add_option('UDP', rtansfer_server_ip='127.0.0.1')
        # CONF.add_option('UDP', rtansfer_server_port=30593)
        self.add_option('UDP', iv_jump=False)
        self.add_option('UDP', db_port=5432)

        self.add_section('RFID')
        # self.add_comment('RFID', 'Използва се от rfid модула.')
        self.add_option('RFID', worker_port='/dev/rfid')
        #     CONF.add_option('RFID', cust_port='/dev/ttyACM1')
        self.add_option('RFID', baudrate=115200)
        # self.add_option('RFID', use_cust_port=True)
        self.add_option('RFID', use_work_port=True)
        #     CONF.add_option('RFID', key_system=True)
        self.add_option('RFID', scan_time=500)
        self.add_option('RFID', timeout=1)
        self.add_option('RFID', login=False)

        self.add_section('LANGUAGE')
        self.add_option('LANGUAGE', use_lang='en')
        self.add_option('LANGUAGE', bg='Български')
        self.add_option('LANGUAGE', en='English')
        self.add_option('LANGUAGE', ro='Românesc')

        self.add_section('KEYBORD')
        self.add_option('KEYBORD', virtual=False)

        self.add_section('PRINTER')
        self.add_option('PRINTER', default_printer='')
        self.add_option('PRINTER', pos_printer_use=False)
        self.add_option('PRINTER', default_pos_printer='')
        self.add_option('PRINTER', pos_printer_x=72)
        if os.name == 'posix':
            self.add_option('PRINTER', pos_printer_y=115)
        else:
            self.add_option('PRINTER', pos_printer_y=128)
        self.add_option('PRINTER', print_direct=False)
        self.add_option('PRINTER', pdf_soft='atril')
        self.add_option('PRINTER', printer_on_server=False)
        self.add_option('PRINTER', printer_on_server_pos=False)
        self.add_option('PRINTER', print_direct_pos=False)
        self.add_option('PRINTER', mony_back_on_pos=False)

        self.add_section('KEYSYSTEM')
        self.add_option('KEYSYSTEM', jump=False)
        self.add_option('KEYSYSTEM', change_on_order=False)

        self.add_section('OCR')
        self.add_option('OCR', worker_port='/dev/ocr')
        self.add_option('OCR', use=False)
        self.add_option('OCR', desko=False)
        self.add_option('OCR', ocr_timeout=1)
        self.add_option('OCR', lock=False)

        # self.add_section('DB')
        # self.add_option('DB', connect_timeout=30)
        # self.add_option('DB', tcp_user_timeout=30)
        # self.add_option('KEYSYSTEM', use_block=False)
        # self.add_option('KEYSYSTEM', randum_block=False)
        # self.add_option('KEYSYSTEM', block=9)

        # self.add_section('MAIL')
        # self.add_option('MAIL', auto=False)
        # self.add_option('MAIL', subject='')
        # self.add_option('MAIL', boss='')
        # self.add_option('MAIL', service='')

        # self.add_section('SERVER_UUID')
    def reload_conf(self):
        global REV
        REV = self.get('SYSTEM', 'rev', 'str')
        global UDP_PORT
        UDP_PORT = self.get('UDP', 'port', 'int')
        global UDP_BUFFER
        UDP_BUFFER = self.get('UDP', 'buffer', 'int')
        global UDP_TIMEOUT
        UDP_TIMEOUT = self.get('UDP', 'timeout', 'int')
        # global ALL_SERVER
        # ALL_SERVER = CONF.get('SERVER')
        # del ALL_SERVER['use_server']
        # global SERVER
        # SERVER = CONF.get('SERVER', 'use_server', 'str')
        # global CASINO_NAME
        # for i in ALL_SERVER:
        #     if ALL_SERVER[i] == SERVER:
        #
        #         CASINO_NAME = i
        global DB_IPTABLES
        DB_IPTABLES = self.get('SYSTEM', 'db_iptables', 'bool')
        # global DB_SERVER
        # DB_SERVER = SERVER
        global USE_RTC

        USE_RTC = self.get('SYSTEM', 'use_rtc', 'bool')
        # global FULSCREEAN
        # FULSCREEAN = CONF.get('SYSTEM', 'fulscreen', 'bool')
        # global DEBUG
        # DEBUG = CONF.get('SYSTEM', 'debug', 'bool')
        # global DB_DEBUG
        # DB_DEBUG = CONF.get('SYSTEM', 'db_debug', 'bool')
        # global ALL_POS_REGISTER
        # try:
        #     ALL_POS_REGISTER = CONF.get('SYSTEM', 'pos_register', 'bool')
        # except:
        #     ALL_POS_REGISTER = False
        global RFID_WORK_PORT
        RFID_WORK_PORT = self.get('RFID', 'worker_port', 'str')
        global RFID_BAUD
        RFID_BAUD = self.get('RFID', 'baudrate', 'int')
        global RFID_USE_WORK
        RFID_USE_WORK = self.get('RFID', 'use_work_port', 'bool')
        global RFID_SCAN_TIME
        RFID_SCAN_TIME = self.get('RFID', 'scan_time', 'int')
        global RFID_TIMEOUT
        RFID_TIMEOUT = self.get('RFID', 'timeout', 'int')
        global RFID_LOGIN
        RFID_LOGIN = self.get('RFID', 'login', 'bool')

        global OCR_PORT
        global OCR_USE
        global OCR_DESKO
        global OCR_TIMEOUT
        OCR_USE = self.get('OCR', 'use', 'bool')
        OCR_PORT = self.get('OCR', 'worker_port', 'str')
        OCR_DESKO = self.get('OCR', 'desko', 'bool')
        OCR_TIMEOUT = self.get('OCR', 'ocr_timeout', 'int')

        # global USE_LANGUAGE
        # USE_LANGUAGE = CONF.get('LANGUAGE', 'use_lang', 'str')
        # global ALL_LANGUAGE
        # ALL_LANGUAGE = CONF.get('LANGUAGE')
        # del ALL_LANGUAGE['use_lang']
        # global USE_VIRTUAL_KEYBORD
        # USE_VIRTUAL_KEYBORD = CONF.get('KEYBORD', 'virtual', 'bool')
        # global JPSERVERIP
        # JPSERVERIP = CONF.get('JPSERVER', 'ip', 'str')
        # global JPSERVERPORT
        # JPSERVERPORT = CONF.get('JPSERVER', 'port', 'int')
        # global EDITDOWN
        # try:
        #     EDITDOWN = CONF.get('JPSERVER', 'edit_down', 'bool')
        # except:
        #     EDITDOWN = False
        # global DOWNSELECT
        # try:
        #     DOWNSELECT = CONF.get('JPSERVER', 'down_select', 'bool')
        # except:
        #     DOWNSELECT = False
        # global EDITVAL
        # try:
        #     EDITVAL = CONF.get('JPSERVER', 'edit_val', 'bool')
        # except:
        #     EDITVAL = False
        global CHANGE_KS_ON_ORDER
        CHANGE_KS_ON_ORDER = self.get('KEYSYSTEM', 'change_on_order', 'bool')

        global PRINTER_DEFAULT
        PRINTER_DEFAULT = self.get('PRINTER', 'default_printer', 'str')
        global PRINT_DIRECT
        PRINT_DIRECT = self.get('PRINTER', 'print_direct', 'bool')
        global PDF_PROGRAM
        PDF_PROGRAM = self.get('PRINTER', 'pdf_soft', 'str')
        global PRINT_ON_SERVER
        PRINT_ON_SERVER = self.get('PRINTER', 'printer_on_server', 'bool')
        global PRINT_ON_SERVER_POS
        PRINT_ON_SERVER_POS = self.get('PRINTER', 'printer_on_server_pos', 'bool')
        global PRINT_DIRECT_POS
        PRINT_DIRECT_POS = self.get('PRINTER', 'print_direct_pos', 'bool')
        global POS_PRINTER_USE
        POS_PRINTER_USE = self.get('PRINTER', 'pos_printer_use', 'bool')
        global DEFAULT_POS_PRINTER
        DEFAULT_POS_PRINTER = self.get('PRINTER', 'default_pos_printer', 'str')
        global POS_PRINTER_SIZE
        POS_PRINTER_SIZE = (self.get('PRINTER', 'pos_printer_x', 'int'), self.get('PRINTER', 'pos_printer_y', 'int'))
        global KS_JUMP
        KS_JUMP = self.get('KEYSYSTEM', 'jump', 'bool')
        global TCP
        TCP = self.get('UDP', 'tcp', 'bool')
        global MONYBACK_ON_POS
        MONYBACK_ON_POS = self.get('PRINTER', 'mony_back_on_pos', 'bool')
        # global USER_NAME_ON_DAY_ORDER
        # USER_NAME_ON_DAY_ORDER = CONF.get('SYSTEM', 'user_name', 'bool')

#=========================================================================
# Копиране на конфигурацията от една работна станция на друга
#=========================================================================
def dump(conf_file):
    pass


def load(conf_file):
    pass


#=========================================================================
# Инициализация на конфиг файла
#=========================================================================

# try:
    # Опитва се да отвори файла
CONF = ConfFile(CONF_FILE)
# except config.NotConfigFile:  # Липсва конфигурационен файл
#     #-------------------------------------------------------------------------
#     open(CONF_FILE, 'a').close()
#     CONF = ConfFile(CONF_FILE)

# def update_conf():
#     global CONF
#     try:
#         CONF.add_option('MAIL', service='')
#     except ConfWarning:
#         pass
#     try:
#         CONF.add_section('JPSERVER')
#         CONF.add_option('JPSERVER', ip='192.168.1.5')
#         CONF.add_option('JPSERVER', port=2522)
#     except ConfWarning:
#         pass
#     try:
#         CONF.add_option('PRINTER', pos_printer_use=False)
#         CONF.add_option('PRINTER', default_pos_printer='')
#         CONF.add_option('PRINTER', pos_printer_x=72)
#         CONF.add_option('PRINTER', pos_printer_y=115)
#     except ConfWarning:
#         pass
#     try:
#         CONF.add_option('PRINTER', printer_on_server=False)
#     except ConfWarning:
#         pass
#
#     try:
#         CONF.add_option('SYSTEM', rev='0')
#     except ConfWarning:
#         pass
#     try:
#         CONF.add_option('SYSTEM', db_iptables=False)
#     except ConfWarning:
#         pass
#     # try:
#     #     CONF.add_option('SYSTEM', db_tunnel_port=0)
#     # except ConfWarning:
#     #     pass
#     # try:
#     #     CONF.add_option('SYSTEM', pgadmin=False)
#     # except ConfWarning:
#     #     pass

# update_conf()

#=========================================================================
# Създаване на глобални променливи
#=========================================================================
#------------------------------------------------------------------------------
# PGADMIN = CONF.get('SYSTEM', 'pgadmin', 'bool')
# USER_NAME_ON_DAY_ORDER = CONF.get('SYSTEM', 'user_name', 'bool')
OCR_USE = CONF.get('OCR', 'use', 'bool')
OCR_DESKO = CONF.get('OCR', 'desko', 'bool')
OCR_PORT = CONF.get('OCR', 'worker_port', 'str')
OCR_LOCK = CONF.get('OCR', 'lock', 'bool')

OCR_TIMEOUT = CONF.get('OCR', 'ocr_timeout', 'int')
REV = CONF.get('SYSTEM', 'rev', 'str')
UDP_PORT = CONF.get('UDP', 'port', 'int')
UDP_BUFFER = CONF.get('UDP', 'buffer', 'int')
UDP_TIMEOUT = CONF.get('UDP', 'timeout', 'int')
# UDP_TRANSFER_SERVER = CONF.get('UDP', 'rtansfer_server', 'bool')
# UDP_TRANSFER_SERVER_IP = CONF.get('UDP', 'rtansfer_server_ip', 'str')
# UDP_TRANSFER_SERVER_PORT = CONF.get('UDP', 'rtansfer_server_port', 'int')


ALL_SERVER = CONF.get('SERVER')
del ALL_SERVER['use_server']
# SERVER = CONF.get('SERVER', 'use_server', 'str')
try:
    socket.inet_pton(socket.AF_INET, CONF.get('SERVER', 'use_server', 'str'))
    SERVER = CONF.get('SERVER', 'use_server', 'str')
except:
    try:
        SERVER = socket.gethostbyname(CONF.get('SERVER', 'use_server', 'str'))
        socket.inet_pton(socket.AF_INET, CONF.get('SERVER', 'use_server', 'str'))
    except:
        SERVER = CONF.get('SERVER', 'use_server', 'str')
# BILL_OUT_DEFOUT = CONF.get('SYSTEM', 'bill_out_default', 'bool')
for i in ALL_SERVER:
    if ALL_SERVER[i] == SERVER:
        CASINO_NAME = i

DB_IPTABLES= CONF.get('SYSTEM', 'db_iptables', 'bool')
DB_NAME = 'mistralcms'
DB_USER = 'root'
DB_PASS = '123456'
# DB_CONNECTION_TIMEOUT = CONF.get('DB', 'connect_timeout', 'int')
# DB_TCP_CONNECTION_TIMEOUT = CONF.get('DB', 'tcp_user_timeout', 'int')
# if SERVER == '127.0.0.1':
DB_SERVER = SERVER
DB_PORT = CONF.get('UDP', 'db_port', 'int')
# DB_TUNNEL = False
# elif '192.168.1.' in SERVER:
#     DB_SERVER = SERVER
#     DB_PORT = 5432
#     DB_TUNNEL = False
# else:
#     if DB_TUNNEL is False:
#         DB_SERVER = SERVER
#         DB_PORT = 5432
#     else:
#         DB_SERVER = '127.0.0.1'
#         DB_PORT = 54434

#------------------------------------------------------------------------------
# VERSION = CONF.get('SYSTEM', 'version', 'str')
# ROOT_PATH = CONF.get('SYSTEM', 'root_path', 'str')
# DB_VERSION = CONF.get('SYSTEM', 'db_version', 'str')
# LOCALE_PATH = CONF.get('SYSTEM', 'locale_path', 'str')
# IMG_FOLDER = CONF.get('SYSTEM', 'img_folder', 'str')
# TEMPLATES = CONF.get('SYSTEM', 'doc_template', 'str')
# if TYPES == 'DEV' or TYPES == 'GUI':
#     ID = CONF.get('SYSTEM', 'soft_id', 'str')
# elif TYPES == 'EMBEDED':
ID = my_uuid.hw_uuid()
# ERR_LOG = CONF.get('SYSTEM', 'err_log', 'str')
USE_RTC = CONF.get('SYSTEM', 'use_rtc', 'bool')
# RTC =  CONF.get('SYSTEM', 'rtc', 'str')
# RTC_PORT = CONF.get('SYSTEM', 'rtc_port', 'int')
FULSCREEAN = CONF.get('SYSTEM', 'fulscreen', 'bool')
DEBUG = CONF.get('SYSTEM', 'debug', 'bool')
DB_DEBUG = CONF.get('SYSTEM', 'db_debug', 'bool')
# BLOCK_BILL_ON_ORDER = CONF.get('SYSTEM', 'bill_block', 'bool')
# PLATFORM = CONF.get('SYSTEM', 'platform', 'str')
try:
    ALL_POS_REGISTER = CONF.get('SYSTEM', 'pos_register', 'bool')
except:
    ALL_POS_REGISTER = False
#--------------------------key_system = True----------------------------------------------------
RFID_WORK_PORT = CONF.get('RFID', 'worker_port', 'str')
# RFID_CUST_PORT = CONF.get('RFID', 'cust_port', 'str')
RFID_BAUD = CONF.get('RFID', 'baudrate', 'int')
# RFID_USE_CUST = CONF.get('RFID', 'use_cust_port', 'bool')
RFID_USE_WORK = CONF.get('RFID', 'use_work_port', 'bool')
# RFID_KEY_SYSTEM = CONF.get('RFID', 'key_system', 'bool')
RFID_SCAN_TIME = CONF.get('RFID', 'scan_time', 'int')
RFID_TIMEOUT = CONF.get('RFID', 'timeout', 'int')
RFID_LOGIN = CONF.get('RFID', 'login', 'bool')

#------------------------------------------------------------------------------
USE_LANGUAGE = CONF.get('LANGUAGE', 'use_lang', 'str')
ALL_LANGUAGE = CONF.get('LANGUAGE')
del ALL_LANGUAGE['use_lang']

#------------------------------------------------------------------------------
USE_VIRTUAL_KEYBORD = CONF.get('KEYBORD', 'virtual', 'bool')

#------------------------------------------------------------------------------
# FLOR = CONF.get('FLOR', 'use', 'bool')
JPSERVERIP = CONF.get('JPSERVER', 'ip', 'str')
JPSERVERPORT = CONF.get('JPSERVER', 'port', 'int')

try:
    EDITDOWN = CONF.get('JPSERVER', 'edit_down', 'bool')
except:
    EDITDOWN = False
try:
    DOWNSELECT = CONF.get('JPSERVER', 'down_select', 'bool')
except:
    DOWNSELECT = False

try:
    EDITVAL = CONF.get('JPSERVER', 'edit_val', 'bool')
except:
    EDITVAL = False

PRINTER_DEFAULT = CONF.get('PRINTER', 'default_printer', 'str')
PRINT_DIRECT = CONF.get('PRINTER', 'print_direct', 'bool')
PDF_PROGRAM = CONF.get('PRINTER', 'pdf_soft', 'str')
PRINT_ON_SERVER = CONF.get('PRINTER', 'printer_on_server', 'bool')
MONYBACK_ON_POS = CONF.get('PRINTER', 'mony_back_on_pos', 'bool')

PRINT_ON_SERVER_POS = CONF.get('PRINTER', 'printer_on_server_pos', 'bool')
PRINT_DIRECT_POS = CONF.get('PRINTER', 'print_direct_pos', 'bool')

POS_PRINTER_USE = CONF.get('PRINTER', 'pos_printer_use', 'bool')
DEFAULT_POS_PRINTER = CONF.get('PRINTER', 'default_pos_printer', 'str')
POS_PRINTER_SIZE = (CONF.get('PRINTER', 'pos_printer_x', 'int'), CONF.get('PRINTER', 'pos_printer_y', 'int'))

KS_JUMP = CONF.get('KEYSYSTEM', 'jump', 'bool')
TCP = CONF.get('UDP', 'tcp', 'bool')

CHANGE_KS_ON_ORDER = CONF.get('KEYSYSTEM', 'change_on_order', 'bool')
# KS_USE_BLOCK = CONF.get('KEYSYSTEM', 'use_block', 'bool')
# KS_RANDUM_BLOCK = CONF.get('KEYSYSTEM', 'randum_block', 'bool')
# KS_BLOCK = CONF.get('KEYSYSTEM', 'block', 'int')
# DINAMIC_IP = CONF.get('SYSTEM', 'use_dinamic_ip', 'bool')
UDP_IV_JUMP = CONF.get('UDP', 'iv_jump', 'bool')

if __name__ == '__main__':
    pass
