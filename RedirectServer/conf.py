'''
Created on 12.03.2019

@author: dedal
'''
import crypts
import os
import libs.cr
import logging
import libs.config
import libs
import time
from subprocess import Popen, PIPE
COMUNICATION_IV_JUMP = True
# IN_THREAD = True
CONF_FILE = 'redirect.conf'

VERSION = '2_1'
# MinGuiRev = '0'
# HOLDER = 'holder'
PUB = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCCfEodyqZBKEkvAO+f3AZBPGq4
zK7nR1brgQEjBoYzBzUKJzWqZhUHHPWCuOdjtOv5F4DQUYIIAU54pu0SqIyRQlJO
aQerphkz60kU+rZKSDD+dyogHCDO1yHDY/9TZk+Fg7782BQycYoyNQvKDlJBeOKp
mjLmFFcYUoCQMvJ2HwIDAQAB
-----END PUBLIC KEY-----
'''

KEY = '''vc3Qtq+Qf0k7PJSwDlJKw44HpS/+jU6+dFMRxCuy6g5Hw235NLAS5YAa1c/FPboGNCfUGnW/shvpQIEfGuTYpgHgXH3M9s47jTvs9tRsof/bhH1Lrk+cZrKfLp8vaGvNTiiMYGz1Uyv2tyylkGUA5tY1c4MA/v7O3eZnk1OeLvVVqqLxr5cxOf45jKCX+hxV2skR9H2qAYXMTiwmjwVRMjlvbyMyCxxS3DeUvdoFibCcw12f/D1nbIa6sHFXNY9U9/gp4m9+Xt5xyw6SRotllTQxX2zoBfAnYXftL3VHSAcStPiYyd2EocUd738Fvj1u'''
RAND_KEY = '''KRJGxB0HYzmWFxoZxYwnMxDz9ZRu6dA50hC-SwVelKsV9_i2nbJOEGVCeN8rhRXsF3nNtxz7m5KDUMnAUBGhcov4l5uC66PgGIgQjPXOhXITsliUbH51J4eR050VPSURyF492TYXfC_BeQIR4qyGozWhfl2vULIkng48vvLSGF2v2g9tsk417I9RFbs-DV4fGPFpNqFnKXeXysUN4el_vknSPyiSrhJ1aM6x1zD3TeDqqpbdybhUIF8-05L0u4k06csbz5xkOaKeDkm98aVIfoB81-BpQljkzNc1Ou6D8J5TvSaWF13JAGKJlj9fCbrRE4ieU_oLC-9QbC0F2Vfzaj7f5lZUh47w6PmgqGUJdgQrGxugx4nsZwXKqO26qjmt4n1faqjqk36nZruXGhMBltqVQ5SEJFfzC7lXpjlPuwXuJ0qbLuMoHnQ3sI8R3ViqMfs0Q0UkdXqu-VlzQM0mEQ=='''

PRIVATE_KEY = '''-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----'''

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

def debug():
    return BASE_DIR == '/home/dedal/Colibri/RedirectServer'

DEBUG = debug()

def read_db_n():
    if os.name == 'posix':
        var = os.popen('df -h | grep -w /').read()
        var = var.split()
        cmd = 'udevadm info --query=all --name=%s | grep ID_SERIAL=' % (var[0])
        data = os.popen(cmd).read()
        # data = data.replace('E: ID_SERIAL=', '')
        return data[:-1]
    else:
        var = os.popen('vol').read()
        var = var.split()
        return var[-1]


def passwd_change():

    # command = 'encfsctl autopasswd %s' % ('/home/colibri/.colibri')
    # cat /proc/cpuinfo | grep Serial
    old_passwd = libs.system.get_ip()
    new_passwd = read_db_n()
    cmd = 'printf "%s\n%s\n%s\n" | sudo cryptsetup luksAddKey /home/colibri/colibri.img' % (old_passwd, new_passwd, new_passwd)
    os.system(cmd)
    cmd = 'udevadm info --query=all --name=%s | grep ID_SERIAL=' % ('/dev/mmcblk1p1')
    data = os.popen(cmd).read()
    if data:
        cmd = 'printf "%s\n%s\n%s\n" | sudo cryptsetup luksAddKey /home/colibri/colibri.img' % (old_passwd, data, data)
        os.system(cmd)
    os.system('printf "%s\n" | sudo cryptsetup luksRemoveKey /home/colibri/colibri.img' % (old_passwd))
    # command = command.split()
    # p = Popen([] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
    # sudo_prompt = p.communicate(old_passwd + '\n' + new_passwd + '\n')[1]
    return True


class Conf(libs.config.ConfFile):
    def __init__(self, conf_file):
        try:
            libs.config.ConfFile.__init__(self, conf_file)
            self.option_update()
        except libs.config.NotConfigFile:
            libs.config.ConfFile.__init__(self, conf_file, make_new=True)
            self.new()

    def option_update(self):
        try:
            self.get('OCR')
        except Exception:
            self.add_section('OCR')
            self.add_option('OCR', unlock=False)
        try:
            self.get('NRA')
        except Exception:
            self.add_section('NRA')
            self.add_option('NRA', debug=False)
        try:
            self.get('SYSTEM', 'old_rev', 'int')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', old_rev=0)

        try:
            self.get('SYSTEM', 'rev', 'int')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', rev=0)

        try:
            self.get('SYSTEM', 'max_log', 'int')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', max_log=2000)

        try:
            self.get('SYSTEM', 'backup_path', 'str')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', backup_path='/home/colibri/db_backup')
        try:
            self.get('SYSTEM', 'iv_jump', 'bool')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', iv_jump=False)
        try:
            self.get('SYSTEM', 'db_port', 'int')
        except libs.config.NoOptionError:
            self.add_option('SYSTEM', db_port=5432)

    def new(self):
        self.add_section('SYSTEM')
        self.add_option('SYSTEM', port=30593)
        self.add_option('SYSTEM', port_2=40593)
        self.add_option('SYSTEM', buffer=4096)
        self.add_option('SYSTEM', timeout=12)
        self.add_option('SYSTEM', timeout_2=12)
        self.add_option('SYSTEM', tcp=False)
        self.add_option('SYSTEM', backup_path='/home/colibri/db_backup')
        self.add_option('SYSTEM', ip='0.0.0.0')
        self.add_option('SYSTEM', db_ip='127.0.0.1')
        self.add_option('SYSTEM', db_debug=False)
        self.add_option('SYSTEM', db_timeout=10)
        self.add_option('SYSTEM', in_thread=False)
        self.add_option('SYSTEM', log_server=True)
        self.add_option('SYSTEM', max_log=2000)
        self.add_option('SYSTEM', log_level='WARNING')
        self.add_option('SYSTEM', rtc=False)
        self.add_option('SYSTEM', rtc_bus=2)
        self.add_option('SYSTEM', rtc_bug=False)
        self.add_option('SYSTEM', db_port=5432)
        # self.add_option('SYSTEM', gmail=True)
        self.add_option('SYSTEM', mail_on_won='')
        self.add_option('SYSTEM', mail_on_won_subject='')
        self.add_option('SYSTEM', tz='Europe/Sofia')
        self.add_option('SYSTEM', old_rev=0)
        self.add_option('SYSTEM', rev=0)
        self.add_option('SYSTEM', iv_jump=False)

        self.add_section('BAN')
        self.add_option('BAN', ban_proc_run=False)
        self.add_option('BAN', iptables=False)
        self.add_option('BAN', db_log='/var/log/postgresql/postgresql-13-main.log')
        self.add_option('BAN', check_time=120)
        self.add_option('BAN', max_wrong_db_login=5)
        self.add_option('BAN', max_db_log_row=50000)

        self.add_section('NRA')
        self.add_option('NRA', debug=False)

        self.add_section('OCR')
        self.add_option('OCR', unlock=False)

        self.add_section('PRINTER')
        self.add_option('PRINTER', default='')
        self.add_option('PRINTER', default_pos='')
        self.add_section('OPEN_IP')


CONF = Conf(CONF_FILE)
DB_PORT = CONF.get('SYSTEM', 'db_port', 'int')
OPEN_IP = CONF.get('OPEN_IP')
IPTASBLES = CONF.get('BAN', 'iptables', 'bool')
TZ = CONF.get('SYSTEM', 'tz', 'str')
MAX_LOG = CONF.get('SYSTEM', 'max_log', 'int')
IN_THREAD = CONF.get('SYSTEM', 'in_thread', 'bool')
BAN_PROC = CONF.get('BAN', 'ban_proc_run', 'bool')
BAN_DB_LOG = CONF.get('BAN', 'db_log', 'str')
BAN_CHK = CONF.get('BAN', 'check_time', 'int')
BAN_MAX_DB_WRONG_LOGIN = CONF.get('BAN', 'max_wrong_db_login', 'int')
MAX_DB_LOG_ROW = CONF.get('BAN', 'max_db_log_row', 'int')
# DOC_SERVER = CONF.get('SYSTEM', 'doc_server', 'bool')
MAIL_ON_WON = CONF.get('SYSTEM', 'mail_on_won', 'str')
MAIL_ON_WON_SUBJECT = CONF.get('SYSTEM', 'mail_on_won_subject', 'str')

PORT = CONF.get('SYSTEM', 'port', 'int')
PORT_2 = CONF.get('SYSTEM', 'port_2', 'int')
BUFFER = CONF.get('SYSTEM', 'buffer', 'int')
TIMEOUT = CONF.get('SYSTEM', 'timeout', 'int')
TIMEOUT_2 = CONF.get('SYSTEM', 'timeout_2', 'int')

IP = CONF.get('SYSTEM', 'ip', 'str')
DB_IP = CONF.get('SYSTEM', 'db_ip', 'str')
# PROTOCOL = 'TCP'

DB_USER = 'root'
DB_PASS = '123456'
DB_NAME = 'mistralcms'
DB_DEBUG = CONF.get('SYSTEM', 'db_debug', 'bool')
DB_TIMEOUT = CONF.get('SYSTEM', 'db_timeout', 'int')
COMUNICATION_IV_JUMP = CONF.get('SYSTEM', 'iv_jump', 'bool')
key = crypts.vector_generator(iv_jump=COMUNICATION_IV_JUMP)
if COMUNICATION_IV_JUMP is False:
    CRYPT = libs.cr.Crypt(key=crypts.COMUNICATION, iv=crypts.IV, iv_jump=False)
    CRYPT2 = libs.cr.Crypt(key=crypts.EMPTY2, iv=crypts.IV, iv_jump=False)
else:
    CRYPT = libs.cr.CryptFernet(key=key)
    CRYPT2 = libs.cr.CryptFernet(key=key)
RSA = libs.rsa.RSAKey()
RSA.load_key(PRIVATE_KEY)


LOG_SERVER = CONF.get('SYSTEM', 'log_server', 'bool')
# SEND_GMAIL = CONF.get('SYSTEM', 'gmail', 'bool')
log_level = CONF.get('SYSTEM', 'log_level', 'str')
if log_level == 'INFO':
    LOG_LEVEL = logging.INFO
elif log_level == 'DEBUG':
    LOG_LEVEL = logging.DEBUG
elif log_level == 'WARNING':
    LOG_LEVEL = logging.WARNING
elif log_level == 'ERROR':
    LOG_LEVEL = logging.ERROR
elif log_level == 'CRITICAL':
    LOG_LEVEL = logging.CRITICAL
else:
    LOG_LEVEL = logging.WARNING
RTC = CONF.get('SYSTEM', 'rtc', 'bool')
RTC_BUG = CONF.get('SYSTEM', 'rtc_bug', 'bool')
RTC_BUS = CONF.get('SYSTEM', 'rtc_bus', 'int')
DEFAULT_PRINTER = CONF.get('PRINTER', 'default', 'str')
DEFAULT_PRINTER_POS = CONF.get('PRINTER', 'default_pos', 'str')
TCP = CONF.get('SYSTEM', 'tcp', 'bool')
REV = CONF.get('SYSTEM', 'rev', 'int')
OLD_REV = CONF.get('SYSTEM', 'old_rev', 'int')
DB_BACKUP_PART = CONF.get('SYSTEM', 'backup_path', 'str')
NRA_DEBUG = CONF.get('NRA', 'debug', 'bool')
OCR_UNLOCK = CONF.get('OCR', 'unlock', 'bool')
#DINAMIC_IP = CONF.get('SYSTEM', 'use_dinamic_ip', 'bool')