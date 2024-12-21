# -*- coding:utf-8 -*-
'''
Created on 18.11.2018 г.

@author: dedal
'''
import os
import log
import multiprocessing
from multiprocessing import Process
LOG = log.get_log(log.LOG_CHANEL_LEVEL['system'])
import client
import time
import threading
import shelve

# import logging
from inspect import signature
from functools import wraps
from multiprocessing.managers import SyncManager
from multiprocessing import managers


# logger = logging.getLogger(__name__)
orig_AutoProxy = managers.AutoProxy


@wraps(managers.AutoProxy)
def AutoProxy(*args, incref=True, manager_owned=False, **kwargs):
    # Create the autoproxy without the manager_owned flag, then
    # update the flag on the generated instance. If the manager_owned flag
    # is set, `incref` is disabled, so set it to False here for the same
    # result.
    autoproxy_incref = False if manager_owned else incref
    proxy = orig_AutoProxy(*args, incref=autoproxy_incref, **kwargs)
    proxy._owned_by_manager = manager_owned
    return proxy


def apply():
    if "manager_owned" in signature(managers.AutoProxy).parameters:
        return

    # logger.debug("Patching multiprocessing.managers.AutoProxy to add manager_owned")
    managers.AutoProxy = AutoProxy

    # re-register any types already registered to SyncManager without a custom
    # proxy type, as otherwise these would all be using the old unpatched AutoProxy
    SyncManager = managers.SyncManager
    registry = managers.SyncManager._registry
    for typeid, (callable, exposed, method_to_typeid, proxytype) in registry.items():
        if proxytype is not orig_AutoProxy:
            continue
        create_method = hasattr(managers.SyncManager, typeid)
        SyncManager.register(
            typeid,
            callable=callable,
            exposed=exposed,
            method_to_typeid=method_to_typeid,
            create_method=create_method,
        )

apply()

def get_date_time(ip, port, log, timeout, udp_buffer, crypt=None):
    for i in range(3):
        data = client.send('get_date_times',
                        ip=ip,
                        port=port,
                        log=log,
                        timeout=timeout,
                        udp_buffer=udp_buffer,
                        crypt=crypt)
        if data != None and data is not False:
            break
    if data != None and data is not False:
        try:
            dates = data['dates']
            dates = dates.replace('.', '-')
            times = data['times']
            cmd = 'sudo date -s %s' % (dates)
            os.system(cmd)
            cmd = 'sudo date -s %s' % (times)
            # log.error('set rtc: %s %s' % (dates, times))
            os.system(cmd)
            return True
        except TypeError as e:
            log.warning(e, exc_info=True)
            return None
    else:
        log.error('no rtc server: ip %s, port %s' % (ip, port))

    return None

class SysManager(SyncManager):
    pass

from queue import PriorityQueue
import conf
import crypt
import db
import libs.cr
import watchdog
import server

def ssh_port():
    cmd = 'sudo grep Port /etc/ssh/sshd_config'
    data = os.popen(cmd).read()
    data = data.replace('Port ', '')
    try:
        data = int(data)
    except ValueError:
        try:
            cmd = 'sudo grep "\<Port\>" /etc/ssh/sshd_config'
            data = os.popen(cmd).read()[:-1]
            data = data.replace('Port ', '')
            data = int(data)
        except ValueError:
            return None
    return data

my_ssh_port = ssh_port()
CONF = conf.Conf()
# SysManager.register("Conf", conf.Conf)
if CONF.get('DB', 'eeprom', 'bool') is True:
    SysManager.register("RealDB", db.EEPROM_DB)
else:
    SysManager.register("RealDB", db.RealDB)
SysManager.register("MemDB", db.MemDB)
SysManager.register("PriorityQueue", PriorityQueue)
# SysManager.register('SEND', client.Send)
manager = SysManager()
manager.start()


COMUNICATION_IV_JUMP = CONF.get('COMUNICATION', 'iv_jump', 'bool')
my_key = crypt.vector_generator(iv_jump=COMUNICATION_IV_JUMP)
IP_TABLESS = [
    'sudo iptables -F',
    'sudo iptables -A INPUT -p icmp -j ACCEPT', # Позволява пинг използва се за проверка от SMIB
    'sudo iptables -A INPUT -s 127.0.0.1/24 --j ACCEPT', # Отваря всички локални портове
    'sudo iptables -I INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT', # Позволява използването на интерне
    'sudo iptables -A INPUT -p tcp --dport %s -j ACCEPT'  % (my_ssh_port), # Позволява връзка към SSH, Иска ключ
    'sudo iptables -A INPUT -s NEW_SVN_IP -j ACCEPT', # Отваря всички портове за мен
    # 'sudo iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT', # Отваря всичло за локална мрежа
    'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (CONF.get('SELF_SERVER', 'port', 'int')), # Отваря всичло за 30593
    'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (CONF.get('SYSTEM', 'visual_port', 'int')),
    'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (5025),
    #'sudo iptables -A INPUT -p udp --dport %s -j ACCEPT' % (UDP_VISUAL_PORT), # Отваря всичло за 30593
    'sudo iptables -A INPUT -i lo -p all -j ACCEPT',
    'sudo iptables -A INPUT -j DROP'
]

print('USE IPTABLES')
for i in IP_TABLESS:
    print('SET ROW', i)
    os.system(i)
# DB_CRYPT = libs.cr.Crypt(crypt.DB, crypt.IV, CONF.get('DB', 'iv_jump', 'bool'), False)
COMUNICATION_IV_JUMP = CONF.get('COMUNICATION', 'iv_jump', 'bool')
if COMUNICATION_IV_JUMP is False:
    COMUNICATION_CRYPT = libs.cr.Crypt(crypt.COMUNICATION, crypt.IV, COMUNICATION_IV_JUMP)
else:
    COMUNICATION_CRYPT = libs.cr.CryptFernet(my_key)

# if CONF.get('DB', 'crypt', 'bool') is False:
#     DB_CRYPT = None

# if CONF.get('COMUNICATION', 'crypt', 'bool') is False:
#     COMUNICATION_CRYPT = None
if CONF.get('DB', 'eeprom', 'bool') is False:
    DB = manager.RealDB(path=conf.DB, my_crypt=None, use_json=True)
else:
    DB = manager.RealDB(types=CONF.get('DB', 'eeprom_types', 'str'), device=CONF.get('DB', 'eeprom_device', 'int'), adress=CONF.get('DB', 'eeprom_adress', 'int'))
# DB = None
MEM_DB = manager.MemDB(DB)
# raise KeyError('c')
if CONF.get('RTC', 'use', 'bool') is True:
    get_date_time(ip=CONF.get('RTC', 'ip', 'str'), port=CONF.get('RTC', 'port', 'int'), log=LOG, crypt=COMUNICATION_CRYPT, udp_buffer=CONF.get('COMUNICATION', 'buffer', 'int'), timeout=CONF.get('COMUNICATION', 'timeout', 'int'))
server.DB = MEM_DB
# SEND = manager.SEND()
#print client.send('client_want_bonus', ip='192.168.1.104', my_name='192.168.1.90', mony=5, cust_id=4, port=CONF.get('RTC', 'port', 'int'), log=LOG, crypt=COMUNICATION_CRYPT, udp_buffer=CONF.get('COMUNICATION', 'buffer', 'int'), timeout=CONF.get('COMUNICATION', 'timeout', 'int'))
def run():

    watchdog_proc = watchdog.Watchdog(conf=CONF, mem_db=MEM_DB, db=DB, crypt=COMUNICATION_CRYPT)
    # watchdog_proc.daemon = True
    watchdog_proc.start()

    server.PIPE = {'watchdog':watchdog_proc.pipe_server_send_watchdog, 'sas':watchdog_proc.pipe_server_send_sas}
    # if conf.COMUNICATION_IV_JUMP is True:
    #     crypts = libs.cr.Crypt(crypt.COMUNICATION, crypt.IV, True, False)
    #     holder = shelve.open(conf.HOLDER, 'w')
    #     key = crypts.decrypt(holder['rand_key'])
    #     holder['rand_key'] = crypts.encrypt(key)
    #     holder.sync()
    #     holder.close()
    # my_server_look = Process(target=server.run_server_look, name='REALTIME', kwargs={
    #     'handler': server.LookHandler,
    #     'crypt': COMUNICATION_CRYPT,
    #     'buffer': CONF.get('COMUNICATION', 'buffer', 'int'),
    #     'timeout': CONF.get('COMUNICATION', 'timeout', 'int'),
    #     'port': 5025,
    #     "ip": CONF.get('SELF_SERVER', 'ip', 'str'),
    #     'in_thread': conf.IN_THREAD,
    #     'logging': log.get_log(log.LOG_CHANEL_LEVEL['server'])
    # })
    # # my_server.daemon = True
    # my_server_look.start()

    my_server = Process(target=server.run_server, name='SOCKET', kwargs={
                                'handler':server.Handler,
                                'crypt':COMUNICATION_CRYPT,
                                'buffer':CONF.get('COMUNICATION', 'buffer', 'int'),
                                'timeout':CONF.get('COMUNICATION', 'timeout', 'int'),
                                'port':CONF.get('SELF_SERVER', 'port', 'int'),
                                "ip":CONF.get('SELF_SERVER', 'ip', 'str'),
                                'in_thread':conf.IN_THREAD,
                                'logging':log.get_log(log.LOG_CHANEL_LEVEL['server'])
    })
    # my_server.daemon = True
    my_server.start()
    # raise Exception, my_server
    # watchdog.my_server = my_server
    watchdog_proc.join()
    try:
        my_server.terminate()
        # my_server_look.terminate()
    except:
        pass
    os.system('sudo service colibri restart')

    # return 0

