#-*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

from . import conf
from . import log
from . import my_uuid
from . import udp
from . import rfid
from . import smib
from . import rtc
import pytz
import sys
from . import db
import os
from . import sendmail
import datetime
from . import xls_file
from . import helps
from . import subversion
import json
from . import rfid_update
from . import rsa
import time
from . import ocr

# from sshtunnel import SSHTunnelForwarder

# class Tunel(threading.Thread):
#     def __init__(self, server="62.73.85.249", port=44554):
#         threading.Thread.__init__(self)
#         port_list =  [4434, 6454, 7464, 8474, 9484, 5434, 5444, 5454, 5464, 5474, 5484, 5434, 5444, 5454, 5464, 5474, 5484]
#         my_port = conf.CONF.get('SYSTEM', 'db_tunnel_port', 'int')
#         if conf.PGADMIN == True:
#             my_port = port_list[0]
#             conf.CONF.update_option('SYSTEM', db_tunnel_port=0)
#         else:
#             if my_port >= 16:
#                 my_port = port_list[0]
#                 conf.CONF.update_option('SYSTEM', db_tunnel_port=0)
#             else:
#                 my_port += 1
#                 conf.CONF.update_option('SYSTEM', db_tunnel_port=my_port)
#                 my_port = port_list[my_port]
#         self.my_port = my_port
#         self._abort = 0
#
#         self.server = SSHTunnelForwarder((server, port),
#                                     ssh_username="mistralcms",
#                                     ssh_pkey='db_tunnel.pem',
#                                     remote_bind_address=('127.0.0.1', 5432),
#                                     local_bind_address=('127.0.0.1', self.my_port),
#                                     compression=False
#                                     )
#         self.alive = False
#
#     def abort(self):
#         self.server.stop()
#         self._abort = 1
#         count = 0
#         while self.server.tunnel_is_up != {}:
#             count += 1
#             time.sleep(1)
#             if count >= 3:
#                 break
#
#         # if self.server.is_alive() == True:
#         #     return True
#
#     def run(self):
#         self.server.start()
#         self.alive = self.server.tunnel_is_up
#         while True:
#             if self._abort:
#                 if self.server.tunnel_is_up == {}:
#                     self.alive = self.server.tunnel_is_up
#                     break
#             # time.sleep(1)
#
#
# def load_db_tunnel(server="62.73.85.249", port=44554):
#     my_server = Tunel(server, port)
#     my_server.start()
#     count = 0
#     while my_server.alive == {}:
#         count += 1
#         time.sleep(1)
#         if count >= 10:
#             break
#     # time.sleep(15)
#
#     return my_server
#
# class NoDBConnection(Exception):
#     pass
# MY_PORT = 5432
CONNECTION_ERROR = False
DEVISE_ERROR = False

# if conf.DINAMIC_IP == True:
#     if conf.SERVER == '127.0.0.1' or conf.SERVER == '192.168.1.6':
#         alife = udp.send('get_uuid', ip=conf.SERVER, timeout=2)
#         timeout = 2
#         for i in range(2):
#             timeout += 3
#             if alife == None:
#                 alife = udp.send('get_uuid', ip=conf.SERVER, timeout=timeout)
#             else:
#                 break
#         # raise Exception, alife
#         # print alife
#         if alife != None:
#             try:
#                 conf.CONF.add_option('SERVER_UUID', **alife)
#             except:
#                 conf.CONF.update_option('SERVER_UUID', **alife)
#         else:
#             CONNECTION_ERROR = True
#             # conf.SERVER = alife[alife.keys(0)]
#     elif conf.SERVER != '127.0.0.1' or conf.SERVER != '192.168.1.6':
#         my_uuid = conf.CONF.get('SERVER_UUID')
#         for i in my_uuid:
#             if conf.CONF.get('SERVER_UUID', i, 'str') == conf.SERVER:
#                 alife = None
#

if __package__ != 'gui_libs':
    alife = udp.send('server_alive', ip=conf.SERVER)
else:
    alife = True
if alife == None:
    alife = udp.send('server_alive', ip=conf.SERVER)
# print alife
# raise Exception, conf.SERVER
if alife == None:
    DEVISE_ERROR = True
    CONNECTION_ERROR = True
else:
    if __package__ != 'gui_libs':
        if conf.DB_IPTABLES == False:
            if DEVISE_ERROR == False or DEVISE_ERROR == True:
                for i in range(3):
                    response = udp.send('chk_pos', ip=conf.SERVER, pos_id=conf.ID)
                    if response != None:
                        DEVISE_ERROR = response
                        break
                    time.sleep(2)
        else:
            if conf.DB_IPTABLES == True:
                if DEVISE_ERROR == False or DEVISE_ERROR == 'INSTALL':
                    for i in range(3):
                        port = udp.send('db_iptables', ip=conf.SERVER, pos_id=conf.ID)
                        if port != None:
                            break
                        time.sleep(2)
                else:
                    port = False
                if port == None:
                    conf.DB_SERVER = '127.0.0.1'
                    CONNECTION_ERROR = True
                elif port == 'INSTALL':
                    DEVISE_ERROR = port
                elif port == False:
                    conf.DB_SERVER = '127.0.0.1'
                    CONNECTION_ERROR = True

if CONNECTION_ERROR == False:
    try:
        from . import models
        DB = models.DBCtrl()
    except Exception as e:
        log.stderr_logger.critical(e, exc_info=True)
        CONNECTION_ERROR = True


def restart_program(user=None, user_clean=False):
    if user_clean == True:
        try:
            if user == None:
                user = DB.get_all_where(models.User, login=True)
                for obj in user:
                    obj.login = False
                    DB.add_object_to_session(obj)
            else:
                user.login = False
                DB.add_object_to_session(user)
            DB.commit()
        except Exception as e:
            print(e)
    try:
        conf.PARNET.OnClose(None)
    except Exception as e:
        print(e)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    sys.exit(0)


def chk_time():
    start_times = DB.get_one_where(models.DayReport, day_report=True, order='id', descs=True)
    if start_times == None:
        return True
    now = models.TZ.now()
    # print models.TZ.set_tz_info(start_times.pub_time), now
    if models.TZ.set_tz_info(start_times.pub_time) > now:
        return models.TZ.date_to_str(start_times.pub_time, '%d.%m.%Y %H:%M:%S')
    else:
        return True


def chk_license(name=None):
    if name != None:
        ln = DB.get_one_where(models.LN, name=name)
        if ln == None:
            return 'NO'
        else:
            values = json.loads(ln.value)
            if models.TZ.str_to_date(values['end_time'], '%d.%m.%Y') < models.TZ.now():
                return 'END'
            elif models.TZ.str_to_date(values['end_time'], '%d.%m.%Y') < models.TZ.now() + datetime.timedelta(days=10):
                return 'END_TIME'
            elif ln.name != values['name']:
                return 'BAD NAME'
            else:
                return True
    else:
        all_ln = {}
        all_name = []
        ln = DB.get_all(models.LN)
        for i in ln:
            all_name.append(i.name)
            values = json.loads(i.value)
            if models.TZ.str_to_date(values['end_time'], '%d.%m.%Y') < models.TZ.now():
                all_ln[i.name] = 'END'
            elif models.TZ.str_to_date(values['end_time'], '%d.%m.%Y') < models.TZ.now() + datetime.timedelta(days=10):
                all_ln[i.name] = 'END_TIME'
            elif i.name != values['name']:
                all_ln[i.name] = 'BAD NAME'
            else:
                all_ln[i.name] = True
        if 'base' not in all_name:
            all_ln['base'] = 'NO'
        if 'keysystem' not in all_name:
            all_ln['keysystem'] = 'NO'
        if 'bonus_cart' not in all_name:
            all_ln['bonus_cart'] = 'NO'
        if 'client' not in all_name:
            all_ln['client'] = 'NO'
        if 'jackpot' not in all_name:
            all_ln['jackpot'] = 'NO'
        return all_ln

        # return False


def tail(fname, lines):
    """Read last N lines from file fname."""
    f = open(fname, 'r')
    BUFSIZ = 1024
    f.seek(0, os.SEEK_END)
    fsize = f.tell()
    block = -1
    data = ""
    exit = False
    while not exit:
        step = (block * BUFSIZ)
        if abs(step) >= fsize:
            f.seek(0)
            exit = True
        else:
            f.seek(step, os.SEEK_END)
        data = f.read().strip()
        if data.count('\n') >= lines:
            break
        else:
            block -= 1
    return data.splitlines()[-lines:]


def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True


__all__ = [
    # 'Session',
    'conf',
    'udp',
    'rfid',
    'smib',
    'models',
    'db',
    'sendmail',
    'xls_file',
    'helps',
    'subversion'
]

if __name__ == '__main__':
    pass
