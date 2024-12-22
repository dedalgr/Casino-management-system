# -*- coding:utf-8 -*-
'''
Created on 18.02.2019

@author: dedal
'''
# from multiprocessing import Process
from multiprocessing import Pipe, Lock
# from io import StringIO
from subprocess import Popen, PIPE
import log
import time
import datetime
from libs import diagnostic
from libs import system
import libs.cr
import libs.rfid
import os
import subprocess
import conf
import rfid
import keysystem
import bonus
import jpserver
# import sas
import random
import client
# import sys
from libs import uuid_maker
from libs import subversion
import proto_sas as sas
import client_cart
import threading
from multiprocessing import Process
# from pymemcache.client.base import PooledClient as mem_Client
from multiprocessing import Queue


class Watchdog(Process):

    def __init__(self, **kwargs):
        Process.__init__(self, name='Watchdog')
        # self.daemon = True
        # self.my_server = None
        self.pub = conf.PUB_KEY_SVN
        # self.mem_cache_server = mem_Client(('127.0.0.1', 11211), serializer=client_cart.json_serializer, deserializer=client_cart.json_deserializer)
        # self.mem_cache_server.set('CHANGE_KEY_NAME', None)
        # self.mem_cache_server.set('CHANGE_KEY', {})
        self.ERROR = False
        # client.client.LOG_CLIENT.setLevel(log.LOG_CHANEL_LEVEL['system'])
        self.conf = kwargs['conf']
        self.mem_db = kwargs['mem_db']
        self.go_to_reboot = False
        self.db = kwargs['db']
        self.crypt = kwargs['crypt']
        self.load_time = time.time()
        self.cpu_cernel_stop = None
        # self.LOCK = Lock()
        # self.send = kwargs['send']
        # self.go_to_reboot = False
        self.reboot_if_error = self.conf.get('WATCHDOG', 'reboot_if_error', 'bool')
        self.check_interval = self.conf.get('WATCHDOG', 'check_interval', 'int')
        self.critical_power_a = self.conf.get('WATCHDOG', 'critical_power_a', 'float')
        self.critical_power_v = self.conf.get('WATCHDOG', 'critical_power_v', 'float')
        self.warning_temp = self.conf.get('WATCHDOG', 'warnt_temp', 'float')
        self.critical_temp = self.conf.get('WATCHDOG', 'critical_temp', 'float')
        self.working_mod = self.db.get('WORKING_MODULE')
        self.tcp_buffer = self.conf.get('COMUNICATION', 'buffer', 'int')
        self.tcp_timeout = self.conf.get('COMUNICATION', 'timeout', 'int')
        self.db_server_port = self.conf.get('DB_SERVER', 'port', 'int')
        self.db_server_ip = self.conf.get('DB_SERVER', 'ip', 'str')
        self.proc_chk_now = self.conf.get('WATCHDOG', 'proc_chk', 'bool')
        self.net_chk_now = self.conf.get('WATCHDOG', 'net_chk', 'bool')
        self.sys_chk_now = self.conf.get('WATCHDOG', 'sys_chk', 'bool')
        self.sas_tester = None
        # self.proto_sas = self.conf.get('SYSTEM', 'proto_sas', 'bool')
        # if self.proto_sas is True:
        #     global sas
        #
        #     sas = proto_sas
        # if self.conf.get('WATCHDOG', 'revision', 'int') == 0:
        #    self.conf.update_option('WATCHDOG', revision=self.svn_info())
        self.rev = self.conf.get('WATCHDOG', 'revision', 'int')
        self.check_working_time = time.time() + random.randint(86400, 172800)
        self.my_name = system.get_ip()
        self.all_proc = {}
        self.no_sync_db = False
        self.pipe_server_send_watchdog, self.pipe_server_recv_watchdog = Pipe()

        self.pipe_rfid_send_keysystem, self.pipe_rfid_recv_keysystem = Pipe()

        self.pipe_rfid_send_bonus, self.pipe_rfid_recv_bonus = Pipe()
        self.pipe_bonus_send_sas, self.pipe_bonus_recv_sas = Pipe()

        self.pipe_sas_send_jackpot, self.pipe_sas_recv_jackpot = Pipe()

        self.pipe_server_send_sas, self.pipe_server_recv_sas = Pipe()

        self.pipe_rfid_send_client, self.pipe_rfid_recv_client = Pipe()
        self.pipe_client_send_sas, self.pipe_client_recv_sas = Pipe()

        self.pipe_udp_client_cart_send, self.pipe_udp_client_cart_recv = Pipe()

        self.pipe_udp_bonus_cart_send, self.pipe_udp_bonus_cart_recv = Pipe()

        self.pipe_udp_sas_send, self.pipe_udp_sas_recv = Pipe()

        self.mem_db.set('SAS_METER', None)
        self.mem_db.set('SAS_METER_IN_COUNT', None)
        self.init = {}
        self.init['sw_id'] = self.sw_id()
        self.init['crc'] = self.crc_maker()
        self.init['hw_id'] = self.sw_id() #self.hw_id()
        self.init['version'] = conf.VERSION
        self.init['ip'] = system.get_ip()
        self.init['rev'] = self.rev
        self.mem_db.set('RESERVE', None)
        # self.log.error('test')

    def sas_tester_connect(self, **kwargs):
        if not self.sas_tester:
            try:
                if self.conf.get('SAS', 'usb', 'bool') is True:
                    port = '/dev/ia'
                    self.sas_tester = libs.proto_sas.SAS_USB(port=port, timeout=2, log=self.log,
                                           aft_check_last_transaction=self.conf.get('SAS', 'aft_check_last_transaction', 'bool'), sas_dump=False,
                                           denom=self.conf.get('SAS', 'coef', 'float'), get_aft_transaction_from_EMG=self.conf.get('SAS', 'last_aft_transaction_from_emg', 'bool'))
                else:
                    # realise = os.popen('lsb_release -a | grep Description:').read()
                    # if 'buster' in realise:
                    port = '/dev/ttyS4'
                    # else:
                    #     self.port = '/dev/ttyS1'
                    self.sas_tester = libs.proto_sas.Sas(port=port, timeout=2, log=self.log,
                                                  aft_check_last_transaction=self.conf.get('SAS', 'aft_check_last_transaction',
                                                                                         'bool'), sas_dump=False,
                                                  denom=self.conf.get('SAS', 'coef', 'float'), get_aft_transaction_from_EMG=self.conf.get('SAS', 'last_aft_transaction_from_emg', 'bool'))
            except:
                return 'Port error'
        if self.sas_tester.is_open() == False:
            self.sas_tester.open()
        response = None
        for i in range(3):
            response = self.sas_tester.connection.read(1)
            if response:
                self.sas_tester.close()
                break
        data = []
        if not response:
            return 'No SAS Connection'
        else:
            self.sas_tester.adress = int(libs.proto_sas.binascii.hexlify(response))
            self.sas_tester.mashin_n = response.hex()
            data = ['adress recognised ' + str(self.sas_tester.mashin_n)]
        response = self.sas_tester.gaming_machine_ID()
        if not response:
            return 'addenomination not recognised'
        else:
            data.append('addenomination recognised ' + str(response))
        self.sas_tester.transaction = self.sas_tester.AFT_get_last_transaction()
        if self.sas_tester.transaction:
            data.append('last EMG AFT transaction ' + str(self.sas_tester.transaction))
        else:
            data.append('last EMG AFT transaction not recognised')
        return data

    def sas_tester_gpoll(self, **kwargs):
        if not self.sas_tester:
            return 'Connect to EMG'
        return self.sas_tester.events_poll()

    def sas_tester_run(self, **kwargs):
        if self.sas_tester is None:
            return 'Connect to EMG'
        event = {
            'shutdown': self.sas_tester.shutdown,
            'startup': self.sas_tester.startup,
            'enable_bill_acceptor': self.sas_tester.enable_bill_acceptor,
            'disable_bill_acceptor':self.sas_tester.disable_bill_acceptor,
            'en_dis_game':self.sas_tester.en_dis_game,
            'enter_maintenance_mode':self.sas_tester.enter_maintenance_mode,
            'exit_maintanance_mode':self.sas_tester.exit_maintanance_mode,
            'en_dis_rt_event_reporting':self.sas_tester.en_dis_rt_event_reporting,
            'send_meters_10_15':self.sas_tester.send_meters_10_15,
            'total_cancelled_credits':self.sas_tester.total_cancelled_credits,
            'total_bet_meter':self.sas_tester.total_bet_meter,
            'total_win_meter':self.sas_tester.total_win_meter,
            'total_in_meter':self.sas_tester.total_in_meter,
            'total_jackpot_meter':self.sas_tester.total_jackpot_meter,
            'games_played_meter':self.sas_tester.games_played_meter,
            'games_won_meter':self.sas_tester.games_won_meter,
            'games_lost_meter':self.sas_tester.games_lost_meter,
            'games_powerup_door_opened':self.sas_tester.games_powerup_door_opened,
            'meters_11_15':self.sas_tester.meters_11_15,
            'current_credits':self.sas_tester.current_credits,
            'handpay_info':self.sas_tester.handpay_info,
            'meters':self.sas_tester.meters,
            'total_bill_meters':self.sas_tester.total_bill_meters,
            'total_dollar_value_of_bills_meter':self.sas_tester.total_dollar_value_of_bills_meter,
            'true_coin_in':self.sas_tester.true_coin_in,
            'true_coin_out':self.sas_tester.true_coin_out,
            'total_hand_paid_cancelled_credit':self.sas_tester.total_hand_paid_cancelled_credit,
            'delay_game':self.sas_tester.delay_game,
            'last_accepted_bill_info':self.sas_tester.last_accepted_bill_info,
            'number_of_bills_currently_in_stacker':self.sas_tester.number_of_bills_currently_in_stacker,
            'total_credit_amount_of_all_bills_in_stacker':self.sas_tester.total_credit_amount_of_all_bills_in_stacker,
            'total_number_of_games_impimented':self.sas_tester.total_number_of_games_impimented,
            'game_meters':self.sas_tester.game_meters,
            'game_configuration':self.sas_tester.game_configuration,
            'selected_game_number':self.sas_tester.selected_game_number,
            'pending_cashout_info':self.sas_tester.pending_cashout_info,
            'AFT_jp':self.sas_tester.AFT_jp,
            'AFT_change_transaction':self.sas_tester.AFT_change_transaction,
            'AFT_out':self.sas_tester.AFT_out,
            'AFT_cashout_enable':self.sas_tester.AFT_cashout_enable,
            'AFT_won':self.sas_tester.AFT_won,
            'AFT_in':self.sas_tester.AFT_in,
            'AFT_game_lock_and_status_request':self.sas_tester.AFT_game_lock_and_status_request,
            'AFT_clean_transaction_poll':self.sas_tester.AFT_clean_transaction_poll,
            'AFT_get_last_transaction':self.sas_tester.AFT_get_last_transaction,
            'AFT_register':self.sas_tester.AFT_register,
            'AFT_unregister':self.sas_tester.AFT_unregister,
            'AFT_cansel_request':self.sas_tester.AFT_cansel_request,
            'current_date_time':self.sas_tester.current_date_time,
            'recieve_date_time':self.sas_tester.recieve_date_time,
            'initiate_legacy_bonus_pay':self.sas_tester.initiate_legacy_bonus_pay,
            'remote_handpay_reset':self.sas_tester.remote_handpay_reset,
            'legacy_bonus_meters':self.sas_tester.legacy_bonus_meters

        }

        cmd = kwargs['cmd']
        del kwargs['cmd']
        try:
            if kwargs == {}:
                response = event[cmd]()
            else:
                response = event[cmd](**kwargs)
        except Exception as e:
            response = None
            self.log.error(e, exc_info=True)
        # response = eval(cmd)

        if not response:
            return os.popen('journalctl --unit=colibri -n 1').read()
        self.db.set('AFT_TRANSACTION', self.sas_tester.transaction)
        emg_security = self.sas_tester.legacy_bonus_meters()
        self.db.set('SAS_SECURITY', emg_security)
        return response

    def start_udp_client(self):
        self.udp_send = client.Send(pipe=[self.pipe_udp_client_cart_recv, self.pipe_udp_bonus_cart_recv, self.pipe_udp_sas_recv], crypt=self.crypt)
        self.udp_send.start()

    def start_all(self, **kwargs):
        try:
            if self.working_mod['sas'] is True:
                self.sas_start()
        except Exception as e:
            # self.ERROR = True
            self.log.critical(e, exc_info=True)
        try:
            if self.working_mod['jackpot'] is True:
                self.jackpot_start()
        except Exception as e:
            # self.ERROR = True
            self.log.critical(e, exc_info=True)
        try:
            if self.working_mod['rfid'] is True:
                self.rfid_start()
        except Exception as e:
            # self.ERROR = True
            self.log.critical(e, exc_info=True)
        try:
            if self.working_mod['keysystem'] is True:
                self.keysystem_start()
        except Exception as e:
            # self.ERROR = True
            self.log.critical(e, exc_info=True)
        try:
            if self.working_mod['bonus_cart'] is True:
                self.bonus_start()
        except Exception as e:
            # self.ERROR = True
            self.log.critical(e, exc_info=True)
        try:
            if self.working_mod['client_cart'] is True:
                self.client_cart_start()
        except Exception as e:
            # self.ERROR = True
            self.log.critical(e, exc_info=True)

        return True

    # def change_db_key(self, name, data, **kwargs):
    def reset_nerwork(self, new_ip):
        time.sleep(2)
        # cmd = 'sudo service connman status'
        # tmp = os.popen(cmd).read()
        # if 'enable' in tmp:
        #     os.system("connmanctl config ethernet_02c504417187_cable --ipv4 manual %s 255.255.255.0 192.168.1.1" % (new_ip))
        # else:
        os.system('sudo ifconfig eth0 down')
        os.system('sudo ifconfig eth0 %s' % (new_ip))
        os.system('sudo ifconfig eth0 up')
        self.kill_all()
        self.my_name = system.get_ip()
        self.start_all()

    def change_ip(self, **kwargs):
        try:
            if 'sas_config' in kwargs:
                if kwargs['sas_config']:
                    self.conf.update_option('SAS', **kwargs['sas_config'])
        except Exception as e:
            self.log.error(e, exc_info=True)

        os.system('sudo mount -o remount rw /')
        # self.change_pass()
        cmd = "sudo sed -i 's/%s/%s/g' /etc/network/interfaces" % (self.my_name, kwargs['new_ip'])
        os.system(cmd)
        t = threading.Thread(target=self.reset_nerwork, args=(kwargs['new_ip'],))
        t.start()
        # b = threading.Thread(target=self.resize_var, args=(240, ))
        # b.start()
        return True

    def restart_all_proc(self, **kwargs):
        self.kill_all()
        self.start_all()
        return True

    def crc_maker(self, **kwargs):
        return uuid_maker.mk_crc(path=os.getcwd(), string=True)

    def emmc_id(self, **kwargs):
        return uuid_maker.read_emmc_n()

    def read_eeprom_data(self, **kwargs):
        return uuid_maker.read_eeprom_data()

    def set_eeprom_data(self, **kwargs):
        return uuid_maker.set_eeprom_data(buf=kwargs['buf'])

    def cpu_id(self, **kwargs):
        return uuid_maker.read_cpu_n()

    def hw_id(self, **kwargs):
        return uuid_maker.hw_uuid()

    def sw_id(self, **kwargs):
        return uuid_maker.mk_soft_id()

    def alive(self, **kwargs):
        return self.rev

    def status(self, **kwargs):
        return self.mem_db.get('STATUS')

    def pip_install(self, **kwargs):
        os.system('sudo mount -o remount rw /')
        os.system('sudo mount -o remount rw /var')
        os.system('sudo pip install %s' % (kwargs['mod']))
        # self.send_event(msg='pip install mod: %s' % (str(kwargs)))
        return True

    def apt_install(self, **kwargs):
        os.system('sudo mount -o remount rw /')
        os.system('sudo mount -o remount rw /var')
        os.system('sudo apt-get install %s' % (kwargs['mod']))
        # self.send_event(msg='apt install mod: %s' % (str(kwargs)))
        return True

    def reboot(self, **kwargs):
        # if self.sas.hold_bonus != None:
        #     data = self.db.get('BONUS_ERROR')
        #     data.append([self.sas.hold_bonus['bonus_id'], True, self.sas.meter['curent credit']])
        #     self.db.set('BONUS_ERROR', data)
        # self.hard_go_to_reboot = True

        if 'time' in kwargs:
            if kwargs['time'] < 1:
                kwargs['time'] = 1
            cmd = 'sudo shutdown -r %s' % (kwargs['time'])
        else:
            cmd = 'sudo shutdown -r  1'
        os.system(cmd)
        return True

    def soft_reboot(self, **kwargs):
        self.go_to_reboot = True
        # if self.sas.hold_bonus != None:
        #     data = self.db.get('BONUS_ERROR')
        #     data.append([self.sas.hold_bonus['bonus_id'], True, self.sas.meter['curent credit']])
        #     self.db.set('BONUS_ERROR', data)
        return True

    def set_time(self, **kwargs):
        cmd = 'date --set %s' % (kwargs['dates'])
        os.system(cmd)
        cmd = 'date --set %s' % (kwargs['times'])
        os.system(cmd)
        # self.send_event(msg='time set')
        return True

    def who(self, **kwargs):

        return self.init

    # def get_log(self, **kwargs):
    #     return None
    #     if 'level' not in kwargs:
    #         if self.conf.get('LOGGING_FILE', 'sys_log', 'bool') is True:
    #             # cmd = "sudo tail -n 200 /var/log/syslog | grep SMIB"
    #             cmd = '''sudo sed -n "/^$(LANG=C date --date='2 hours ago' '+%b %d %H:')\\|^$(LANG=C date --date='1 hours ago' '+%b %d %H:')/p" /var/log/syslog | grep SMIB'''
    #         else:
    #             cmd = "sudo tail -n 200 %s" % (conf.LOG_FILE)
    #     else:
    #         if self.conf.get('LOGGING_FILE', 'sys_log', 'bool') is True:
    #             cmd = "sudo tail -n 200 /var/log/syslog | grep %s" % (kwargs['level'])
    #         else:
    #             cmd = "sudo tail -n 200 %s | grep %s" % (conf.LOG_FILE, kwargs['level'])
    #     return os.popen(cmd).read()

    def get_conf(self, **kwargs):
        return self.conf.get(kwargs['section'])

    # def day_order_reset_player(self, **kwargs):
        # if self.mem_db.get('PLAYER') is not False:
        #     self.mem_db.set('PLAYER_DAY_ORDER', kwargs['end_date'])
        # return True

    def conf_update(self, **kwargs):
        section = kwargs['section']
        del kwargs['section']
        del kwargs['request_time']
        # self.send_event(msg='conf update')
        return self.conf.update_option(section, **kwargs)

    def conf_del(self, **kwargs):
        os.system('sudo rm %s' % (conf.CONF_FILE))
        return True

    def sys_cmd(self, **kwargs):
        return os.popen(kwargs['cmd']).read()

    def ks_reset(self, **kwargs):
        multi_keysystem = {
            'credit_id': [],
            'report_id': [],
            'admin_id': [],
            'owner_id': []
        }
        keysystem = {
            'credit_id': '',
            'report_id': '',
            'admin_id': '',
            'owner_id': ''
        }
        self.mem_db.set('MULTI_KEYSYSTEM', multi_keysystem)
        self.mem_db.set('KEYSYSTEM', keysystem)
        return True

    def keysystem_change(self, **kwargs):
        if self.conf.get('KEYSYSTEM', 'multi_key', 'bool') is True:
            all_keys = self.mem_db.get('MULTI_KEYSYSTEM')
            max_len = self.conf.get('KEYSYSTEM', 'multi_key_len', 'int')
            if 'credit_id' in kwargs:
                if len(all_keys['credit_id']) >= max_len:
                    del all_keys['credit_id'][0]
                all_keys['credit_id'].append(kwargs['credit_id'])
            if 'report_id' in kwargs:
                if len(all_keys['report_id']) >= max_len:
                    del all_keys['report_id'][0]
                all_keys['report_id'].append(kwargs['report_id'])
            return self.mem_db.set('MULTI_KEYSYSTEM', all_keys)
        else:
            all_keys = self.mem_db.get('KEYSYSTEM')
            if 'credit_id' in kwargs:
                all_keys['credit_id'] = kwargs['credit_id']
            if 'report_id' in kwargs:
                all_keys['report_id'] = kwargs['report_id']
            return self.mem_db.set('KEYSYSTEM', all_keys)

    def svn_info(self, **kwargs):
        if 'url' not in kwargs:
            url = 'svn://NEW_SVN_IP/home/svn/SMIB_BIN/%s/' % (conf.VERSION)
        else:
            url = kwargs['url']

        if 'my_dir' not in kwargs:
            my_dir = os.getcwd()
        else:
            my_dir = kwargs['my_dir']
        if 'user' in kwargs:
            user = kwargs['user']
        else:
            user = 'smib'
        if 'passwd' in kwargs:
            passwd = kwargs['passwd']
        else:
            passwd = 'smib_update'
        connect = subversion.SubVersion(folder=my_dir, user=user, passwd=passwd, url=url)
        return connect.info()

    def svn_update(self, **kwargs):
        if 'url' not in kwargs:
            url = 'svn://7NEW_SVN_IP/home/svn/SMIB_BIN/%s/' % (conf.VERSION)
        else:
            url = kwargs['url']

        if 'my_dir' not in kwargs:
            my_dir = os.getcwd()
        else:
            my_dir = kwargs['my_dir']
        if 'user' in kwargs:
            user = kwargs['user']
        else:
            user = 'smib'
        if 'passwd' in kwargs:
            passwd = kwargs['passwd']
        else:
            passwd = 'smib_update'
        connect = subversion.SubVersion(folder=my_dir, user=user, passwd=passwd, url=url)
        connect.checkout()
        if 'rev' in kwargs:
            connect.update(rev=kwargs['rev'])
            rev = kwargs['rev']
            self.conf.update_option('WATCHDOG', revision=kwargs['rev'])
        else:
            rev = connect.update()
            self.conf.update_option('WATCHDOG', revision=rev)
        try:
            b = threading.Thread(target=self.update_in_server, kwargs={'rev':rev})
            b.start()
        except Exception:
            pass

        if 'soft_reboot' in kwargs:
            if kwargs['soft_reboot'] is True:
                self.soft_reboot()

        return rev

    # def svn_update(self, **kwargs):
    #     a = threading.Thread(target=self._svn_update)
    #     a.start()
    #     return True
    # def svn_update(self, **kwargs):
    #     if 'url' not in kwargs:
    #         url = 'svn://NEW_SVN_IP/home/svn/SMIB_BIN/%s/' % (conf.VERSION)
    #     else:
    #         url = kwargs['url']
    #
    #     if 'my_dir' not in kwargs:
    #         my_dir = os.getcwd()
    #     else:
    #         my_dir = kwargs['my_dir']
    #     if 'user' in kwargs:
    #         user = kwargs['user']
    #     else:
    #         user = 'smib'
    #     if 'passwd' in kwargs:
    #         passwd = kwargs['passwd']
    #     else:
    #         passwd = 'smib_update'
    #     connect = subversion.SubVersion(folder=my_dir, user=user, passwd=passwd, url=url)
    #     connect.checkout()
    #     rev = connect.update()
    #     self.conf.update_option('WATCHDOG', revision=rev)
    #     return rev

    def svn_checkout(self, **kwargs):
        os.system('sudo rm -r .svn')
        if 'url' not in kwargs:
            url = 'svn://NEW_SVN_IP/home/svn/SMIB_BIN/%s/' % (conf.VERSION)
        else:
            url = kwargs['url']

        if 'my_dir' not in kwargs:
            my_dir = os.getcwd()
        else:
            my_dir = kwargs['my_dir']
        if 'user' in kwargs:
            user = kwargs['user']
        else:
            user = 'smib'
        if 'passwd' in kwargs:
            passwd = kwargs['passwd']
        else:
            passwd = 'smib_update'
        connect = subversion.SubVersion(folder=my_dir, user=user, passwd=passwd, url=url)
        rev = connect.checkout()
        self.conf_update('WATCHDOG', revision=rev)
        try:
            b = threading.Thread(target=self.update_in_server, kwargs={'rev':rev})
            b.start()
        except Exception:
            pass
        return rev

    # def status(self, **kwargs):
    #     return os.popen('sudo service colibri status').read()

    def db_keys(self, **kwargs):
        return self.mem_db.keys()

    def db_get(self, **kwargs):
        tmp = {}
        if 'key' not in kwargs:
            for i in self.db_keys():
                tmp[i] = self.mem_db.get(i)
        else:
            tmp[kwargs['key']] = self.mem_db.get(kwargs['key'])
        return tmp

    def db_set(self, **kwargs):
        for i in kwargs['db'].keys():
            self.mem_db.set(i, kwargs['db'][i])
        # self.send_event(msg='db change')
        return True

    def db_get_key(self, **kwargs):
        return self.mem_db.get(kwargs['key'])

    def db_set_key(self, **kwargs):
        key = kwargs['key']
        data = kwargs['data']
        # self.send_event(msg='db key change %s' % (str(kwargs)))
        return self.mem_db.set(key, data)

    def db_del(self, **kwargs):
        self.stop_db_sync()
        if self.conf.get('DB', 'eeprom', 'bool') == False:
            os.system('sudo rm %s' % (conf.DB))
        else:
            self.db.erese()
        return True

    def relay_test(self, **kwargs):
        cmd = 'sudo modio2tool -B 1 -s 1'
        tmp = os.popen(cmd).read()
        if 'error' in tmp:
            return False
        time.sleep(0.2)
        cmd = 'sudo modio2tool -B 1 -c 1'
        tmp = os.popen(cmd).read()
        if 'error' in tmp:
            return False
        time.sleep(0.2)
        cmd = 'sudo modio2tool -B 1 -s 2'
        tmp = os.popen(cmd).read()
        if 'error' in tmp:
            return False
        time.sleep(0.2)
        cmd = 'sudo modio2tool -B 1 -c 2'
        tmp = os.popen(cmd).read()
        if 'error' in tmp:
            return False
        return True

    def relay_status(self, **kwargs):
        # if 'keysystem' in self.all_proc:
        cmd = 'sudo modio2tool -B 1 -H'
        tmp = os.popen(cmd).read()
        if 'ID: 0x0\n' == tmp:
            return False
        return True

    def diagnostic(self, **kwargs):
        cmd = 'sudo service colibri status'
        tmp = os.popen('sudo uptime').read() + '\n' + os.popen(cmd).read()
        return tmp

    def security_reload(self, **kwargs):
        if self.working_mod['rfid'] is True:
            self.rfid_start()
        request_time = time.time() + self.tcp_timeout - 4
        # self.pipe_server_send_sas.send(['sas.get_single_meter', {'command':'start'}])
        self.pipe_server_send_sas.send(['sas.sas_security_unlock', {'request_time':request_time}])

        if self.pipe_server_send_sas.poll(self.tcp_timeout - 3):
            return self.pipe_server_send_sas.recv()
        # self.send_event(msg='RELOAD SECURITY')
        return None

    def bonus_add(self, **kwargs):
        bonus = self.mem_db.get('BONUSCART')  # @UnusedVariable
        bonus = kwargs['bonus']
        data = self.mem_db.set('BONUSCART', bonus)
        # self.send_event(msg='ADD BONUS')
        return data

    def set_jacpot_procent(self, **kwargs):
        pr = kwargs['pr']
        # self.send_event(msg='change jackpot % %s' % (pr))
        return self.mem_db.set('JACKPOT', pr)

    def disable_game_from_jackpot(self, **kwargs):
        # print self.all_proc['sas'].my_game
        if self.all_proc['sas'].my_game == None:
            return None
        all_disable = self.mem_db.get('DISABLE_GAME_JP')
        all_disable.append(self.all_proc['sas'].my_game)
        # self.send_event(msg='disable game from jackpot')
        return self.mem_db.set('DISABLE_GAME_JP', all_disable)

    def reserve_emg(self, **kwargs):
        self.mem_db.set('RESERVE', kwargs)
        # raise KeyError, self.mem_db.set('RESERVE', kwargs)
        return True

    def del_emg_reserve(self, **kwargs):
        self.mem_db.set('RESERVE', None)
        return True

    def enable_game_from_jackpot(self, **kwargs):

        if self.all_proc['sas'].my_game == None:
            return None
        all_disable = self.mem_db.get('DISABLE_GAME_JP')
        del all_disable[all_disable.index(self.all_proc['sas'].my_game)]
        # self.send_event(msg='enable game from jackpot')
        return self.mem_db.set('DISABLE_GAME_JP', all_disable)

    def chk_alife(self, **kwargs):
        return True

    def rev_and_player(self, **kwargs):
        # data = []
        try:
            tmp = self.mem_db.get('PLAYER')['name']
        except TypeError:
            tmp = False
        return [self.rev, tmp]
    def get_player(self, **kwargs):
        try:
            return self.mem_db.get('PLAYER')['name']
        except TypeError:
            return False

    def stop_db_sync(self, **kwargs):
        self.sync_db()
        self.no_sync_db = True
        self.db.close()
        self.mem_db.close()
        return True

    def get_namespase_dns(self, **kwargs):
        return libs.uuid_maker.get_namespase_dns()

    # def send_event(self, **kwargs):
    #     data = client.send(evt='write_log',
    #                        ip=self.db_server_ip,
    #                        port=self.db_server_port,
    #                        log=self.log,
    #                        timeout=self.tcp_timeout,
    #                        udp_buffer=self.tcp_buffer,
    #                        crypt=self.crypt,
    #                        my_name=self.my_name,
    #                        **kwargs)
    #     return data

    def client_cart_start(self, **kwargs):
        name = 'client_cart'
        if self.working_mod['rfid'] is False:
            self.working_mod['rfid'] = True
            self.mem_db.set('WORKING_MODULE', self.working_mod)
            if 'rfid' not in self.all_proc:
                # if self.all_proc['rfid'].is_alive() is False:
                self.rfid_start()
                # else:
                #     self.rfid_start()
        if 'client_cart' not in self.all_proc:
            self.working_mod[name] = True
            self.mem_db.set('WORKING_MODULE', self.working_mod)
            self.client_cart = client_cart.ClientCart(conf=self.conf, db=self.mem_db, crypt=self.crypt,
                                                      pipe={'rfid': self.pipe_rfid_recv_client,
                                                            'sas': self.pipe_client_send_sas}, send=self.pipe_udp_client_cart_send)
            self.all_proc['client_cart'] = self.client_cart
            self.client_cart.start()

        return True

    def client_cart_stop(self, **kwargs):
        if 'client_cart' in self.all_proc:
            self.client_cart.terminate()
            self.client_cart.join()
            del self.all_proc['client_cart']
        self.working_mod['client_cart'] = False
        self.mem_db.set('WORKING_MODULE', self.working_mod)
        #         self.send_event(msg='client proc stop')
        return True

    def rfid_scan_time(self, **kwargs):
        self.rfid_stop()
        rc522 = kwargs['rc255']
        if rc522 is False:
            port = '/dev/rfid'
        else:
            a = os.popen('ls /dev/spidev1.0').read()
            if a:
                port = '/dev/spidev1.0'
            else:
                port = '/dev/spidev0.0'
        if rc522 is False:
            # port = self.conf.get('RFID', 'rfid_port', 'str')
            baudrate = self.conf.get('RFID', 'speed', 'int')
            self.conf.update_option(section='RFID', rfid_timeout=kwargs['my_timeout'], scan_time=kwargs['scan_time'], rc522=rc522)
            my_rfid = libs.rfid.RFID(port=port, baudrate=baudrate, timeout=1)
            # my_rfid.chk_for_port()
            data = False
            for i in range(3):
                if my_rfid.isOpen() is False:
                    my_rfid.open()
                data = my_rfid.scan_time(times=kwargs['scan_time'])
                if data == 'OK':
                    data = True
                    break
            my_rfid.close()
        else:
            self.conf.update_option(section='RFID', rfid_timeout=kwargs['my_timeout'], scan_time=kwargs['scan_time'], rc522=rc522)
            data = True
        self.rfid_start()
        return data

    def _run_linux_cmd(self, **kwargs):
        os.popen(kwargs['cmd'])

    def run_linux_cmd(self, **kwargs):
        if 'show_response' not in kwargs:
            return os.popen(kwargs['cmd']).read()
        elif kwargs['show_response'] is True:
            return os.popen(kwargs['cmd']).read()
        else:
            t = threading.Thread(target=self._run_linux_cmd, kwargs=kwargs)
            t.start()
            return True

    def backup_conf(self, **kwargs):
        os.system('cp /home/colibri/colibri/smib.conf /home/colibri/colibri/smib.conf~')
        return True

    def restory_conf(self, **kwargs):
        os.system('cp /home/colibri/colibri/smib.conf~ /home/colibri/colibri/smib.conf')
        return True

    def event(self, evt, **kwargs):
        all_event = {
            'backup_conf':self.backup_conf,
            'restory_conf':self.restory_conf,
            'run_linux_cmd': self.run_linux_cmd,
            'rfid_scan_time': self.rfid_scan_time,
            'hw_id': self.hw_id,
            'sw_id': self.sw_id,
            'cpu_id': self.cpu_id,
            'emmc_id': self.emmc_id,
            'crc': self.crc_maker,
            'alive': self.alive,
            'ALIFE': self.alive,
            'status': self.status,
            'rfid_start': self.rfid_start,
            'rfid_stop': self.rfid_stop,
            'sas_start': self.sas_start,
            'sas_stop': self.sas_stop,
            'keysystem_start': self.keysystem_start,
            'keysystem_stop': self.keysystem_stop,
            'bonus_start': self.bonus_start,
            'bonus_stop': self.bonus_stop,
            'jackpot_start': self.jackpot_start,
            'jackpot_stop': self.jackpot_stop,
            'check_for_work': self.check_for_work,
            'sync_db': self.sync_db,
            # 'stop_kernel': self.stop_kernel,
            'set_nice': self.set_nice,
            'kill_all': self.kill_all,
            'is_work': self.isWork,
            'pip_install': self.pip_install,
            'apt_install': self.apt_install,
            'reboot': self.reboot,
            'set_time': self.set_time,
            'who': self.who,
            # 'get_log': self.get_log,
            'get_conf': self.get_conf,
            'conf_update': self.conf_update,
            'conf_del': self.conf_del,
            'sys_cmd': self.sys_cmd,
            'keysystem_change': self.keysystem_change,
            'ks_reset':self.ks_reset,
            'svn_update': self.svn_update,
            'db_keys': self.db_keys,
            'db_get': self.db_get,
            'db_set': self.db_set,
            'db_del': self.db_del,
            'client_cart_stop': self.client_cart_stop,
            'client_cart_start': self.client_cart_start,
            'relay_test': self.relay_test,
            'relay_status': self.relay_status,
            'diagnostic': self.diagnostic,
            'all_proc': self.all_proc_keys,
            'security_reload': self.security_reload,
            'bonus_add': self.bonus_add,
            'set_jacpot_procent': self.set_jacpot_procent,
            'disable_game_from_jackpot': self.disable_game_from_jackpot,
            'enable_game_from_jackpot': self.enable_game_from_jackpot,
            'get_player': self.get_player,
            'db_get_key': self.db_get_key,
            'db_set_key': self.db_set_key,
            'stop_db_sync': self.stop_db_sync,
            'change_ip': self.change_ip,
            'start_all': self.start_all,
            'svn_checkout': self.svn_checkout,
            'empty_log': self.empty_log,
            'upload_file': self.upload_file,
            'soft_reboot': self.soft_reboot,
            'read_eeprom_data': self.read_eeprom_data,
            'set_eeprom_data': self.set_eeprom_data,
            'get_namespase_dns': self.get_namespase_dns,
            'svn_info': self.svn_info,
            'change_pass': self.change_pass,
            'get_bonus_error': self.get_bonus_error,
            'del_bonus_error': self.del_bonus_error,
            'reset_player': self.reset_player,
            'reserve_emg': self.reserve_emg,
            'del_emg_reserve':self.del_emg_reserve,
            'smib_reset':self.smib_reset,
            'smib_if_jump':self.smib_if_jump,
            'block_nra': self.block_nra,
            # 'day_order_reset_player':self.day_order_reset_player,
            'real_time_look':self.real_time_look,
            'chk_alife':self.chk_alife,
            'rev_and_player':self.rev_and_player,
            'send_chk_jp_down': self.send_chk_jp_down,
            'sas_tester_connect':self.sas_tester_connect,
            'sas_tester_gpoll':self.sas_tester_gpoll,
            'sas_tester_run':self.sas_tester_run,
        }
        try:
            evt = all_event[evt](**kwargs)
            return evt
        except TypeError as e:
            self.log.warning(e, exc_info=True)
            return all_event[evt]

    def send_chk_jp_down(self, **kwargs):
        time.sleep(3)
        data = self.mem_db.get('chk_jp_down')
        self.log.warning('jpdown chk %s %s ' % (data, time.time() - 60))
        if data == False:
            return False
        elif data >= time.time() - 60:
            return True
        return False

    def block_nra(self, **kwargs):
        self.mem_db.set('PLAYER_IN_NRA', True)
        return True

    def smib_if_jump(self, **kwargs):
        self.conf.update_option('COMUNICATION', iv_jump=kwargs['iv_jump'])
        return self.soft_reboot()

    def smib_reset(self, **kwargs):
        self.change_ip(new_ip='192.168.1.9')
        self.db_del()
        self.conf_del()
        return True

    # def active_proto_sas(self, **kwargs):
    #     self.conf.update_option('SYSTEM', proto_sas=kwargs['active'])
    #     self.proto_sas = kwargs['active']
    #     # global sas
    #     # if self.proto_sas is True:
    #
    #     import proto_sas
    #     sas = proto_sas
    #     # else:
    #     #     # global sas
    #     #     # import sas as my_sas
    #     #     sas = my_sas
    #     self.sas_stop()
    #     self.sas_start()
    #     return True
    # def send_data(self, evt, timeout=10, **kwargs):
    #     data = None
    #     # self.LOCK.acquire()
    #     # if unlock is True:
    #         # unlock = True
    #     try:
    #         data = client.send(evt=evt,
    #                                    ip=self.conf.get('DB_SERVER', 'ip', 'str'),
    #                                    port=self.conf.get('DB_SERVER', 'port', 'int'),
    #                                    log=self.log,
    #                                    timeout=timeout,
    #                                    udp_buffer=self.conf.get('COMUNICATION', 'buffer', 'int'),
    #                                    crypt=self.crypt,
    #                                    **kwargs)
    #     except Exception as e:
    #         self.log.error('evt %s, data: %s' % (evt, kwargs))
    #         data = None
    #     # try:
    #     # try:
    #     #     self.LOCK.release()
    #     # except ValueError:
    #     #     pass
    #     # except ValueError:
    #     #     self.log.error('LOCK not release')
    #
    #     # if unlock is True:
    #     #     try:
    #     #         self.LOCK.release()
    #     #     except ValueError:
    #     #         self.log.error('LOCK not release')
    #     return data

    def reset_player(self, **kwargs):
        self.client_cart_stop()
        # self.db.set('RESET_PLAYER', True)
        player = self.mem_db.set('PLAYER', False)
        # try:
        #     for i in range(3):
        #         # self.send_data('clean_all_bonus', cust_id=player['id'], timout=0)
        #         self.send_data(evt='server_reset_player', timeout=4)
        # except Exception as e:
        #     self.log.error(e, exc_info=True)
        self.mem_db.set('RESET_PLAYER', True)
        # self.sync_db()
        # for i in range(3):
        # for i in range(3):

        return self.client_cart_start()

    def get_bonus_error(self, **kwargs):
        return self.mem_db.get('BONUS_ERROR')

    def real_time_look(self, **kwargs):
        count = self.mem_db.get('SAS_METER_IN_COUNT')
        if count != None and count is not False:
            player =  self.mem_db.get('PLAYER')
            if player:
                count['player'] = player['name']
            else:
                count['player'] = player
        return count

    def del_bonus_error(self, **kwargs):
        bonus_error = []
        self.mem_db.set('BONUS_ERROR', bonus_error)
        return True

    def change_pass(self, **kwargs):
        # command = 'encfsctl autopasswd %s' % ('/home/colibri/.colibri')
        # cat /proc/cpuinfo | grep Serial
        old_passwd = libs.system.get_ip()
        os.system('printf "%s\n | sudo cryptsetup luksRemoveKey colibri.img' % (old_passwd))
        # if 'new_passwd' not in kwargs:
        #     new_passwd = os.popen("udevadm info --query=all --name=/dev/mmcblk0p1 | grep ID_SERIAL").read()[:-1]
        # else:
        #     new_passwd = kwargs['new_passwd']
        # command = command.split()
        # p = Popen([] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
        # sudo_prompt = p.communicate(old_passwd + '\n' + new_passwd + '\n')[1]
        return True

    def upload_file(self, **kwargs):
        a = open(kwargs['name'], 'a')
        a.write(kwargs['data']).close()
        if 'mv' in kwargs:
            os.system('sudo mv %s %s' % (kwargs['name'], kwargs['mv']))
            if 'owner' in kwargs:
                os.system('sudo chown %s %s' % (kwargs['owner'], kwargs['mv']))
        elif 'owner' in kwargs:
            os.system('sudo chown %s %s' % (kwargs['owner'], kwargs['name']))
        return True

    def empty_log(self, **kwargs):
        # return True
        all_file = uuid_maker.get_files('/var/log/')
        cmd = 'sudo sh -c "cat /dev/null > %s'
        rm = 'sudo rm %s'
        for i in all_file:
            if i[-2:] == '.gz':
                os.system(rm % (i))
            else:
                os.system(cmd % (i))
        return True

    def all_proc_keys(self, **kwargs):
        return self.all_proc.keys()

    def set_nice(self, **kwargs):
        os.nice(kwargs['nice'])
        return True

    def update_in_server(self, **kwargs):
        try:
            crypt = libs.cr.Fernet('use_system10')
            # crypt.load_key(self.pub)
            data = client.send('smib_update',
                               ip='NEW_SVN_IP',
                               port=45454,
                               log=client.client.LOG_CLIENT,
                               timeout=10,
                               udp_buffer=4096,
                               crypt=crypt,
                               hw_id=self.hw_id(),
                               sw_id=self.sw_id(),
                               revision=kwargs['rev'],
                               smib_ip=system.get_ip(),
                               version=conf.VERSION,
                               crc=self.init['crc'],
                               )
        except Exception as e:
            return None

    def check_for_work(self, **kwargs):
        try:
            crypt = libs.cr.Fernet('use_system10')
            # crypt.load_key(self.pub)

            data = client.send('chk_dev',
                               ip='NEW_SVN_IP',
                               port=45454,
                               log=client.client.LOG_CLIENT,
                               timeout=10,
                               udp_buffer=4096,
                               crypt=crypt,
                               hw_id=self.hw_id(),
                               sw_id=self.sw_id(),
                               version=conf.VERSION,
                               smib_ip=system.get_ip(),
                               crc=self.init['crc'],
                               rev=self.init['rev'],
                               )
            if data == None:
                return True
            elif data[0] == 'change_pass':
                return self.change_pass(data[1]['passwd'])
            elif data[0] == 'stop' or data == 'BAD RSA SIGNATURE':
                self.log.critical('smib can`t work')
                for i in self.working_mod:
                    self.working_mod[i] = False
                self.mem_db.set('WORKING_MODULE', self.working_mod)
                self.kill_all()
                self.sync_db()
                os.system('sudo mount -o remount rw /')
                os.system('sudo mount -o remount rw /var')
                os.system('sudo systemctl disable colibri')
                self.change_pass(new_passwd=data[1]['new_passwd'])
                client.send('smib_disabled',
                            ip='NEW_SVN_IP',
                            port=45454,
                            log=client.client.LOG_CLIENT,
                            timeout=10,
                            udp_buffer=4096,
                            crypt=crypt,
                            hw_id=self.init['hw_id'],
                            sw_id=self.init['sw_id'],
                            crc=self.init['crc'],
                            version=conf.VERSION,
                            smib_ip=self.init['ip'],
                            rev=self.init['rev'],
                            )
                self.reboot()
        except Exception as e:
            return None
        return True

    def sync_db(self, **kwargs):
        # sync = False
        try:
            for i in self.db.keys():
                real = self.db.get(i)
                mem = self.mem_db.get(i)
                if real != mem:
                    # sync = True
                    self.db.set(i, mem)
                    self.log.info('sync db now')
            # if sync is True:
                    self.db.sync()
        except Exception as e:
            # self.no_sync_db = True
            if self.reboot_if_error is True:
                self.reboot(time=1)
            self.log.critical(e, exc_info=True)
            return False

        return True

    # def stop_kernel(self, **kwargs):
    #     cmd = 'sudo echo %s | sudo tee /sys/devices/system/cpu/cpu%s/online'
    #     if kwargs['stop'] is True:
    #         cmd = cmd % (0, kwargs['kernel'])
    #     else:
    #         cmd = cmd % (1, kwargs['kernel'])
    #     subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     return True

    def temp_chk(self, **kwargs):
        my_temp = diagnostic.arm.OlimexMicro().temp()
        # if self.cpu_cernel_stop == None:
        #     pass
        # elif self.cpu_cernel_stop == 1:
        #     self.stop_kernel(kernel=0, stop=False)
        #     self.cpu_cernel_stop = 2
        #     self.stop_kernel(kernel=1, stop=True)
        # elif self.cpu_cernel_stop == 2:
        #     self.stop_kernel(kernel=1, stop=False)
        #     self.cpu_cernel_stop = None

        if my_temp >= self.warning_temp and my_temp < self.critical_temp:
            # self.send_event(msg='warning temp: %s' % (my_temp))
            self.log.warning('temp %s', my_temp)
        elif my_temp >= self.critical_temp and self.cpu_cernel_stop == None:
            # self.send_event(msg='critical temp: %s' % (my_temp))
            # os.nice(10)
            self.log.critical('temp %s', my_temp)
            # self.cpu_cernel_stop = 1
            # self.stop_kernel(kernel=0, stop=True)
        # else:
        #     if self.cpu_cernel_stop != None:
        #         self.cpu_cernel_stop = None
                # self.stop_kernel(kernel=0, stop=False)
                # self.stop_kernel(kernel=1, stop=False)
        return my_temp

    def voltage_chk(self, **kwargs):
        V = diagnostic.arm.OlimexMicro().voltage()
        if V < self.critical_power_v:
            self.log.critical('power voltage %s', V)
            # self.send_event(msg='critical V: %s' % (V))
            # os.nice(10)
        return V

    def amperage_chk(self, **kwargs):
        A = diagnostic.arm.OlimexMicro().amper()
        if A < self.critical_power_a:
            self.log.critical('power amperage %s', A)
            # self.send_event(msg='critical A: %s' % (A))
            # os.nice(10)
        return A

    def network_chk(self, **kwargs):
        data = diagnostic.arm.OlimexMicro().network(self.conf.get('DB_SERVER', 'ip', 'str'), count=3)
        if data is False:
            data = diagnostic.arm.OlimexMicro().network(self.conf.get('JP_SERVER', 'ip', 'str'), count=3)
            if data is False:
                if data is False:
                    self.log.critical('no network connection')
                    if self.reboot_if_error is True:
                        self.log.warning('reboot smib')
                        self.kill_all()
                        self.sync_db()
                        self.reboot(time=1)
                    else:
                        self.log.warning('smib ifupdown')
                        os.system('sudo systemctl restart NetworkManager.service')
                        # os.system('sudo ifconfig eth0 up')
        return data

    def isWork(self, **kwargs):
        if kwargs['name'] in self.all_proc:
            return self.all_proc[kwargs['name']].is_alive()
        return False

    def kill_all(self, **kwargs):
        for i in self.all_proc:
            if self.isWork(name=i) is True:
                self.all_proc[i].terminate()
                self.all_proc[i].join()
        self.all_proc = {}
        return True

    def proc_check(self, **kwargs):
        t = threading.Thread(target=self._proc_check)
        t.start()

    def _proc_check(self, **kwargs):
        # reboot_service = False
        if self.udp_send.is_alive() is False:
            self.start_udp_client()
        for i in self.all_proc.keys():
            if self.isWork(name=i) is False:
                self.log.error('proc not work %s', i)
                if self.reboot_if_error is True:
                    self.log.warning('reboot smib')
                    self.soft_reboot()
                else:
                    self.log.warning('reload proc %s', i)
                    try:
                        self.all_proc[i].terminate()
                    except:
                        pass
                    del self.all_proc[i]
                    if i == 'rfid' or i == u'rfid':
                        self.rfid_start()
                    if i == 'keysystem' or i == u'keysystem':
                        # if self.conf.get('KEYSYSTEM', 'aft', 'bool') is False:
                        self.keysystem_start()
                    if i == 'bonus' or i == u'bonus':
                        self.bonus_start()
                    if i == 'sas' or i == u'sas':
                        self.sas_start()
                    if i == 'jackpot' or i == u'jackpot':
                        self.jackpot_start()
                    if i == 'client_cart' or i == u'client_cart':
                        self.client_cart_start()
        return True

    def rfid_start(self, **kwargs):
        name = 'rfid'
        if 'rfid' not in self.all_proc:
            rc522 = self.conf.get('RFID', 'rc522', 'bool')
            try:
                if rc522 == False:
                    self.rfid = rfid.Rfid(db=self.mem_db, conf=self.conf, pipe={'client': self.pipe_rfid_send_client,
                                                                                'keysystem': self.pipe_rfid_send_keysystem,
                                                                                'bonus': self.pipe_rfid_send_bonus})
                    self.all_proc[name] = self.rfid
                    self.rfid.start()
                    self.working_mod['rfid'] = True
                else:
                    self.rfid = rfid.Rfid_RC522(db=self.mem_db, conf=self.conf, pipe={'client': self.pipe_rfid_send_client,
                                                                                'keysystem': self.pipe_rfid_send_keysystem,
                                                                                'bonus': self.pipe_rfid_send_bonus})
                    self.all_proc[name] = self.rfid
                    self.rfid.start()
                    self.working_mod['rfid'] = True
            except Exception as e:
                self.log.error(e, exc_info=True)
                self.working_mod['rfid'] = False
            self.mem_db.set('WORKING_MODULE', self.working_mod)
        # self.send_event(msg='rfid proc start')
        return True

    def rfid_stop(self, **kwargs):
        if 'rfid' in self.all_proc:
            self.rfid.terminate()
            self.rfid.join()
            del self.all_proc['rfid']
        self.working_mod['rfid'] = False
        self.mem_db.set('WORKING_MODULE', self.working_mod)
        return True

    def keysystem_start(self, **kwargs):
        name = 'keysystem'
        try:
            if self.working_mod['rfid'] is False:
                self.working_mod['rfid'] = True
                self.mem_db.set('WORKING_MODULE', self.working_mod)
                if 'rfid' not in self.all_proc:
                    # if self.all_proc['rfid'].is_alive() is False:
                    self.rfid_start()
                    # else:
                    #     self.rfid_start()
            if 'keysystem' not in self.all_proc:
                self.keysystem = keysystem.KeySystem(db=self.mem_db, conf=self.conf,
                                                     pipe={'rfid': self.pipe_rfid_recv_keysystem})
                self.all_proc[name] = self.keysystem
                self.keysystem.start()
                self.working_mod['keysystem'] = True
                self.mem_db.set('WORKING_MODULE', self.working_mod)
        except Exception as e:
            self.log.error(e, exc_info=True)
            # self.send_event(msg='keysystem proc start')
        return True

    def keysystem_stop(self, **kwargs):
        if 'keysystem' in self.all_proc:
            self.keysystem.terminate()
            self.keysystem.join()
            del self.all_proc['keysystem']
        self.working_mod['keysystem'] = False
        self.mem_db.set('WORKING_MODULE', self.working_mod)
        #         self.send_event(msg='keysystem proc stop')
        return True

    def bonus_start(self, **kwargs):
        name = 'bonus'
        try:
            if self.working_mod['rfid'] is False:
                self.working_mod['rfid'] = True
                self.mem_db.set('WORKING_MODULE', self.working_mod)
                if 'rfid' not in self.all_proc:
                    # if self.all_proc['rfid'].is_alive() is False:
                    self.rfid_start()
                    # else:
                    #     self.rfid_start()
            if 'bonus' not in self.all_proc:
                self.bonus = bonus.Bonus(db=self.mem_db, conf=self.conf, crypt=self.crypt,
                                         pipe={'sas': self.pipe_bonus_send_sas, 'rfid': self.pipe_rfid_recv_bonus}, send=self.pipe_udp_bonus_cart_send)
                self.all_proc[name] = self.bonus
                self.bonus.start()
                self.working_mod['bonus_cart'] = True
                self.mem_db.set('WORKING_MODULE', self.working_mod)
        except Exception as e:
            self.log.error(e, exc_info=True)
        # self.send_event(msg='bonus proc start')
        return True

    def bonus_stop(self, **kwargs):
        if 'bonus' in self.all_proc:
            self.bonus.terminate()
            self.bonus.join()
            del self.all_proc['bonus']
        self.working_mod['bonus_cart'] = False
        self.mem_db.set('WORKING_MODULE', self.working_mod)
        #         self.send_event(msg='bonus proc stop')
        return True

    def jackpot_start(self, **kwargs):
        name = 'jackpot'
        try:
            if 'jackpot' not in self.all_proc:
                self.jackpot = jpserver.JPServer(db=self.mem_db, conf=self.conf, crypt=self.crypt,
                                                 pipe={'sas': self.pipe_sas_recv_jackpot})
                self.all_proc[name] = self.jackpot
                self.jackpot.start()
                self.working_mod['jackpot'] = True
                self.mem_db.set('WORKING_MODULE', self.working_mod)
        except Exception as e:
            self.log.error(e, exc_info=True)
        # self.send_event(msg='jackpot proc start')
        return True

    def jackpot_stop(self, **kwargs):
        if 'jackpot' in self.all_proc:
            self.jackpot.terminate()
            self.jackpot.join()
            del self.all_proc['jackpot']
        self.working_mod['jackpot'] = False
        self.mem_db.set('WORKING_MODULE', self.working_mod)
        #         print self.send_event(msg='jackpot proc stop')
        return True

    def sas_start(self, disconnect=False, **kwargs):
        name = 'sas'
        try:
            if disconnect == True and self.sas_tester:
                self.sas_tester.close()
                self.sas_tester = None
        except Exception as e:
            self.log.error(e, exc_info=True)
        try:
            if 'sas' not in self.all_proc:
                # if self.proto_sas is False:
                self.sas = sas.Sas(db=self.mem_db, conf=self.conf, crypt=self.crypt,
                                       pipe={'jp': self.pipe_sas_send_jackpot, 3: self.pipe_bonus_recv_sas,
                                             2: self.pipe_server_recv_sas, 1: self.pipe_client_recv_sas}, send=self.pipe_udp_sas_send)
                # else:
                #     self.sas = proto_sas.Sas(db=self.mem_db, conf=self.conf, crypt=self.crypt,
                #                        pipe={'jp': self.pipe_sas_send_jackpot, 'bonus': self.pipe_bonus_recv_sas,
                #                              'server': self.pipe_server_recv_sas, 'client': self.pipe_client_recv_sas},
                #                        lock=self.LOCK)
                self.all_proc[name] = self.sas
                self.sas.start()
                self.working_mod['sas'] = True
                self.mem_db.set('WORKING_MODULE', self.working_mod)
        except Exception as e:
            self.log.error(e, exc_info=True)
        # self.send_event(msg='sas proc start')
        return True

    def sas_stop(self, **kwargs):
        if 'sas' in self.all_proc:
            self.sas.terminate()
            self.sas.join()
            del self.all_proc['sas']
        self.working_mod['sas'] = False
        self.mem_db.set('WORKING_MODULE', self.working_mod)
        #         self.send_event(msg='sas proc stop')
        return True

    def chk_system(self):
        # self.network_chk()
        self.temp_chk()
        self.voltage_chk()
        self.amperage_chk()

    def sync_time_from_ntp(self):
        os.popen('sudo service ntp restart')

    def run(self):
        self.load_time = time.time()
        db_sync_time = time.time() + 30
        # self.change_pass()
        self.log = log.get_log(log.LOG_CHANEL_LEVEL['watchdog'])
        self.start_udp_client()
        self.start_all()
        while True:
            try:
                if self.go_to_reboot is True:
                    self.log.debug('reboot now: %s', self.go_to_reboot)
                    self.kill_all()
                    self.stop_db_sync()
                    self.go_to_reboot = False
                    os.system('sudo service colibri restart')
                # elif self.hard_go_to_reboot is True:
                #     self.hard_go_to_reboot = False
                #     self.kill_all()
                #     self.stop_db_sync()
                #     # self.reboot()
                #     os.system('sudo service colibri stop')
                else:
                    if self.load_time + self.check_interval <= time.time():
                        dates_on_smib = datetime.datetime.now()
                        if dates_on_smib.year < 2021:
                            self.sync_time_from_ntp()
                        # os.system('sudo ifconfig eth0 up')
                        self.load_time = time.time()
                        if self.proc_chk_now is True:
                            self.proc_check()
                        if self.sys_chk_now is True:
                            t = threading.Thread(target=self.chk_system)
                            t.start()
                        if self.net_chk_now is True:
                            b = threading.Thread(target=self.network_chk)
                            b.start()
                    if self.check_working_time < time.time():
                        c = threading.Thread(target=self.check_for_work)
                        c.start()
                        self.check_working_time = time.time() + random.randint(86400, 172800)
                    # if self.udp_send.is_alive() is False:
                    #     self.start_udp_client()
                    while self.pipe_server_recv_watchdog.poll(0.2):
                        data = self.pipe_server_recv_watchdog.recv()
                        if self.ERROR is False:
                            try:
                                data = self.event(evt=data[0], **data[1])
                            except Exception as e:
                                self.log.error(e, exc_info=True)
                                data = None
                        elif self.ERROR is True and data[0] == 'svn_update':
                            data = self.event(evt=data[0], **data[1])
                        elif self.ERROR is True and data[0] == 'soft_reboot':
                            data = self.event(evt=data[0], **data[1])
                        elif self.ERROR is True and data[0] == 'reboot':
                            data = self.event(evt=data[0], **data[1])

                        else:
                            data = None
                        self.pipe_server_recv_watchdog.send(data)
                        # while self.pipe_server_recv_watchdog.poll():
                        #     self.pipe_server_recv_watchdog.recv()
                    # self.log.debug('no_sync_db: %s', self.no_sync_db)
                    if not self.no_sync_db and db_sync_time <= time.time():
                        db_sync_time = time.time() + 30
                        self.sync_db()
                        if self.udp_send.is_alive() == False:
                            self.start_udp_client()
                        else:
                            pass
            except Exception as e:
                self.log.critical(e, exc_info=True)
                if self.reboot_if_error is True:
                    self.kill_all()
                    self.stop_db_sync()
                    self.soft_reboot()
                    # os.system('sudo service colibri restart')

# if __name__ == '__main__':
#     pub = conf.PUB_KEY_SVN
#     crypt = libs.rsa.RSAKey()
