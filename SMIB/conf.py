# -*- coding:utf-8 -*-
'''
Created on 27.01.2019 г.

@author: dedal
'''

import libs.config
from logging.handlers import DEFAULT_TCP_LOGGING_PORT
import os
from subprocess import Popen, PIPE
import libs
import time

VERSION = '2_1'
# HOLDER = 'holder.so'
CONF_FILE = 'smib.conf'
DB = 'smib.db'
LOG_FILE = 'smib.log'
# COMUNICATION_IV_JUMP = True
IN_THREAD = False
KEY = '''vc3Qtq+Qf0k7PJSwDlJKw44HpS/+jU6+dFMRxCuy6g5Hw235NLAS5YAa1c/FPboGNCfUGnW/shvpQIEfGuTYpgHgXH3M9s47jTvs9tRsof/bhH1Lrk+cZrKfLp8vaGvNTiiMYGz1Uyv2tyylkGUA5tY1c4MA/v7O3eZnk1OeLvVVqqLxr5cxOf45jKCX+hxV2skR9H2qAYXMTiwmjwVRMjlvbyMyCxxS3DeUvdoFibCcw12f/D1nbIa6sHFXNY9U9/gp4m9+Xt5xyw6SRotllTQxX2zoBfAnYXftL3VHSAcStPiYyd2EocUd738Fvj1u'''
RAND_KEY = '''KRJGxB0HYzmWFxoZxYwnMxDz9ZRu6dA50hC-SwVelKsV9_i2nbJOEGVCeN8rhRXsF3nNtxz7m5KDUMnAUBGhcov4l5uC66PgGIgQjPXOhXITsliUbH51J4eR050VPSURyF492TYXfC_BeQIR4qyGozWhfl2vULIkng48vvLSGF2v2g9tsk417I9RFbs-DV4fGPFpNqFnKXeXysUN4el_vknSPyiSrhJ1aM6x1zD3TeDqqpbdybhUIF8-05L0u4k06csbz5xkOaKeDkm98aVIfoB81-BpQljkzNc1Ou6D8J5TvSaWF13JAGKJlj9fCbrRE4ieU_oLC-9QbC0F2Vfzaj7f5lZUh47w6PmgqGUJdgQrGxugx4nsZwXKqO26qjmt4n1faqjqk36nZruXGhMBltqVQ5SEJFfzC7lXpjlPuwXuJ0qbLuMoHnQ3sI8R3ViqMfs0Q0UkdXqu-VlzQM0mEQ=='''

PUB_KEY_SVN = '''-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----'''

class Conf(libs.config.ConfFile):
    def __init__(self, conf_file=CONF_FILE):
        try:
            libs.config.ConfFile.__init__(self, conf_file)
            self.option_update()
        except libs.config.NotConfigFile:
            libs.config.ConfFile.__init__(self, conf_file, make_new=True)
            self.new()

    def option_update(self):
        try:
            self.get('PLAYER', 'lock_bill_if_no_cust', 'bool')
        except libs.config.NoOptionError:
            self.add_option('PLAYER', lock_bill_if_no_cust=False)
        try:
            self.get('SAS', 'sas_dump', 'bool')
        except libs.config.NoOptionError:
            self.add_option('SAS', sas_dump=False)
        try:
            self.get('PLAYER', 'display_size', 'int')
        except libs.config.NoOptionError:
            self.add_option('PLAYER', display_size=4)
        try:
            self.get('PLAYER', 'show_monybeck_pay', 'bool')
        except libs.config.NoOptionError:
            self.add_option('PLAYER', show_monybeck_pay=False)
        tmp = self.get('SAS', 'coef', 'float')
        if tmp == 0:
            self.update_option('SAS', coef=0.01)
        try:
            self.get('SAS', 'aft_lock_time', 'int')
        except libs.config.NoOptionError:
            self.add_option('SAS', aft_lock_time=0)
        try:
            self.get('SAS', 'last_aft_transaction_from_emg', 'bool')
        except libs.config.NoOptionError:
            self.add_option('SAS', last_aft_transaction_from_emg=False)
        try:
            self.get('SAS', 'aft_check_last_transaction', 'bool')
        except libs.config.NoOptionError:
            self.add_option('SAS', aft_check_last_transaction=False)
        try:
            self.get('DB', 'eeprom', 'bool')
        except libs.config.NoOptionError:
            self.add_option('DB', eeprom=False)
            self.add_option('DB', eeprom_types='24c512')
            self.add_option('DB', eeprom_device=1)
            self.add_option('DB', eeprom_adress=80)
        # if self.get('SAS', 'emg_type', 'int') == 0:
        #     self.update_option('SAS', emg_type=1)

    def new(self):
        libs.config.ConfFile.__init__(self, CONF_FILE, make_new=True)
        # ===========================================================================
        # СИСТЕМНИ НАСТРОЙКИ
        # ===========================================================================
        self.add_section('SYSTEM')
        self.add_option('SYSTEM', version=VERSION)
        self.add_option('SYSTEM', lang='en')
        self.add_option('SYSTEM', block_bonus_by_bet=False)
        self.add_option('SYSTEM', visual_port=2552)
        # self.add_option('SYSTEM', proto_sas=True)
        # self.add_option('SYSTEM', update_unix=False)

        self.add_section('WATCHDOG')
        self.add_option('WATCHDOG', reboot_if_error=False)
        self.add_option('WATCHDOG', check_interval=60)
        self.add_option('WATCHDOG', warnt_temp=70.0)
        self.add_option('WATCHDOG', critical_temp=90.0)
        self.add_option('WATCHDOG', critical_power_a=1.5)
        self.add_option('WATCHDOG', critical_power_v=4.0)
        self.add_option('WATCHDOG', revision=0)
        self.add_option('WATCHDOG', proc_chk=False)
        self.add_option('WATCHDOG', net_chk=False)
        self.add_option('WATCHDOG', sys_chk=False)
        # ===========================================================================
        # КОМУНИКАЦИЯ
        # ===========================================================================
        self.add_section('COMUNICATION')
        self.add_option('COMUNICATION', timeout=10)
        self.add_option('COMUNICATION', buffer=4096)
        # self.add_option('COMUNICATION', crypt=True)
        self.add_option('COMUNICATION', iv_jump=False)

        # ===========================================================================
        # СЪРВЪР
        # ===========================================================================
        self.add_section('SELF_SERVER')
        self.add_option('SELF_SERVER', ip='0.0.0.0')
        self.add_option('SELF_SERVER', port=30593)
        self.add_option('SELF_SERVER', threading=False)

        # ===========================================================================
        # RTC
        # ===========================================================================
        self.add_section('RTC')
        self.add_option('RTC', use=True)
        self.add_option('RTC', ip='192.168.1.6')
        self.add_option('RTC', port=40593)

        # ===========================================================================
        # ДЖАКПОТ СЪРВЪР
        # ===========================================================================
        self.add_section('JP_SERVER')
        self.add_option('JP_SERVER', ip='192.168.1.5')
        self.add_option('JP_SERVER', port=2522)
        self.add_option('JP_SERVER', block_if_lost=False)
        self.add_option('JP_SERVER', block_count=20)
        self.add_option('JP_SERVER', down_if_credti=1)
        self.add_option('JP_SERVER', down_by_aft=False)

        # ===========================================================================
        # DB СЪРВЪР
        # ===========================================================================
        self.add_section('DB_SERVER')
        self.add_option('DB_SERVER', ip='192.168.1.6')
        self.add_option('DB_SERVER', port=40593)

        # ===========================================================================
        # ЛОГ СЪРВЪР
        # ===========================================================================
        self.add_section('LOGGING_SERVER')
        self.add_option('LOGGING_SERVER', use=True)
        self.add_option('LOGGING_SERVER', server_ip='192.168.1.6')
        self.add_option('LOGGING_SERVER', port=DEFAULT_TCP_LOGGING_PORT)
        self.add_option('LOGGING_SERVER', level='WARNING')

        # ===========================================================================
        # DB
        # ===========================================================================
        self.add_section('DB')
        self.add_option('DB', crypt=True)
        self.add_option('DB', iv_jump=False)
        self.add_option('DB', mem_type='DICT')
        self.add_option('DB', eeprom=True)
        self.add_option('DB', eeprom_types='24c512')
        self.add_option('DB', eeprom_device=1)
        self.add_option('DB', eeprom_adress=80)

        # ===========================================================================
        # RFID
        # ===========================================================================
        self.add_section('RFID')
        # self.add_option('RFID', rfid_port='/dev/rfid')
        self.add_option('RFID', speed=115200)
        self.add_option('RFID', rfid_timeout=1)
        self.add_option('RFID', scan_time=500)
        self.add_option('RFID', rc522=True)


        # ===========================================================================
        # KEYSYSTEM
        # ===========================================================================
        self.add_section('KEYSYSTEM')
        self.add_option('KEYSYSTEM', multi_key=False)
        self.add_option('KEYSYSTEM', multi_key_len=5)
        self.add_option('KEYSYSTEM', relay_timeout=1)
        self.add_option('KEYSYSTEM', aft=True)
        self.add_option('KEYSYSTEM', credit=1)
        self.add_option('KEYSYSTEM', report=2)
        #         self.add_option('RELAY', hold=False)

        # =======================================================================
        # BONUS
        # =======================================================================
        self.add_section('BONUS')
        self.add_option('BONUS', sas_timeout=30)
        self.add_option('BONUS', out=1)
        self.add_option('BONUS', pipe_clean=10)
        # self.add_option('BONUS', forbiden_out_befor=2)

        # =======================================================================
        # PLAYER
        # =======================================================================
        self.add_section('PLAYER')
        self.add_option('PLAYER', sas_timeout=30)
        self.add_option('PLAYER', player_timeout=4)
        self.add_option('PLAYER', bonus_on_credit=1)
        self.add_option('PLAYER', use_touch=True)
        self.add_option('PLAYER', lock_emg_if_no_cust=False)
        self.add_option('PLAYER', logo_name='colibri-logo.png')
        self.add_option('PLAYER', anime_use=True)
        self.add_option('PLAYER', anime_num=1)
        self.add_option('PLAYER', skin=2)
        self.add_option('PLAYER', lock_bill_if_no_cust=False)
        self.add_option('PLAYER', display_size=4)
        self.add_option('PLAYER', show_monybeck_pay=False)

        # self.add_option('PLAYER', forbiden_out_befor=2)
        # ===========================================================================
        # LOGGING FILE
        # ===========================================================================
        self.add_section('LOGGING_FILE')
        self.add_option('LOGGING_FILE', use=True)
        self.add_option('LOGGING_FILE', sys_log=True)
        self.add_option('LOGGING_FILE', level='DEBUG')
        self.add_option('LOGGING_FILE', count=7)
        self.add_option('LOGGING_FILE', size=2097152)

        # ===========================================================================
        # LOG LEVEL
        # ===========================================================================
        self.add_section('LOGGING_LEVEL')
        self.add_option('LOGGING_LEVEL', system='WARNING')
        self.add_option('LOGGING_LEVEL', server='WARNING')
        self.add_option('LOGGING_LEVEL', watchdog='WARNING')
        self.add_option('LOGGING_LEVEL', rfid='WARNING')
        self.add_option('LOGGING_LEVEL', keysystem='WARNING')
        self.add_option('LOGGING_LEVEL', bonus='WARNING')
        self.add_option('LOGGING_LEVEL', jpserver='WARNING')
        self.add_option('LOGGING_LEVEL', sas='WARNING')
        self.add_option('LOGGING_LEVEL', client_cart='WARNING')

        # ===========================================================================
        # SAS
        # ===========================================================================
        self.add_section('SAS')
        self.add_option('SAS', sas_n='00')
        self.add_option('SAS', aft=True)
        # self.add_option('SAS', aft_won=True)
        self.add_option('SAS', sync_time=False)
        self.add_option('SAS', usb=False)
        self.add_option('SAS', sas_timeout=2)
        self.add_option('SAS', security=False)
        self.add_option('SAS', pay_jp_by_hand=False)
        self.add_option('SAS', check_for_game=True)
        self.add_option('SAS', mail_send=True)
        self.add_option('SAS', mail_send_on_won=1000)
        self.add_option('SAS', delay_rill=False)
        self.add_option('SAS', sleep_on_down=False)
        self.add_option('SAS', sleep_time=0.04)
        self.add_option('SAS', stop_autoplay=False)
        self.add_option('SAS', stop_autoplay_on_won=100)
        self.add_option('SAS', stop_autoplay_fix_after_time=60)
        self.add_option('SAS', coef=0.01)
        self.add_option('SAS', aft_lock_time=0)
        # self.add_option('SAS', coef_use=False)
        self.add_option('SAS', use_gpoll=True)
        self.add_option('SAS', gpoll_timeout=1)
        self.add_option('SAS', aft_check_last_transaction=True)
        # self.add_option('SAS', impera=False)
        self.add_option('SAS', set_jp_mether_to_out=True)
        self.add_option('SAS', emg_type=0)
        self.add_option('SAS', sas_dump=False)
        self.add_option('SAS', last_aft_transaction_from_emg=False)
        self.change_pass()
        try:
            self.fix_eeprom()
        except:
            pass
        # self.resize_var()

    def fix_eeprom(self):
        # pass
        a = os.popen('journalctl -g Olimex').read()
        if 'LIME' in a:
            from pyA20 import i2c
            eeprom_address = 0x50
            i2c.init("/dev/i2c-1")
            i2c.open(eeprom_address)
            i2c.write([0x00, 0xFF])
            i2c.close()
            os.system('sudo reboot')

    def read_db_n(self):
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

    def change_pass(self, **kwargs):

        # command = 'encfsctl autopasswd %s' % ('/home/colibri/.colibri')
        old_passwd = libs.system.get_ip()
        if 'new_passwd' not in kwargs:
            new_passwd = self.read_db_n()
        else:
            new_passwd = kwargs['new_passwd']
        # command = command.split()
        # p = Popen([] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
        # sudo_prompt = p.communicate(old_passwd + '\n' + new_passwd + '\n')[1]

        cmd = 'printf "%s\n%s\n%s\n" | sudo cryptsetup luksAddKey /home/colibri/colibri.img' % (old_passwd, new_passwd, new_passwd)
        os.system(cmd)
        cmd = 'udevadm info --query=all --name=%s | grep ID_SERIAL=' % ('/dev/mmcblk1p1')
        data = os.popen(cmd).read()
        if data:
            cmd = 'printf "%s\n%s\n%s\n" | sudo cryptsetup luksAddKey /home/colibri/colibri.img' % (old_passwd, data, data)
            os.system(cmd)

        os.system('printf "%s\n" | sudo cryptsetup luksRemoveKey /home/colibri/colibri.img' % (old_passwd))
        return True

    def resize_var(self):
        os.system('sudo mount -o remount rw /')
        os.system('sudo mount -o remount rw /var')
        # os.system('sudo apt-get clean')
        os.system('sudo rm /etc/init.d/resize_sd')
        os.system('sudo sh /root/resize_sd.sh /dev/mmcblk0 2')

if __name__ == '__main__':
    conf = Conf()
