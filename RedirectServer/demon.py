'''
Created on 12.03.2019

@author: dedal
'''

import conf
# import shelve
try:
    conf.passwd_change()
except Exception as e:
    print(e)

import log
stdout_logger = log.get_log()
import server
import time
import os
import libs.rtc
from  multiprocessing import Process
import threading
from multiprocessing.managers import SyncManager
import libs
import get_loging
import chk_proc
import models
import  ban_proc
import datetime
import crypts
# import not_static_ip

# def doc_server():
#     cmd = 'sudo mkdocs serve --dev-addr=0.0.0.0:801'
#     os.system(cmd)
class SysManager(SyncManager):
    pass

from queue import PriorityQueue

class MyPriorityQueue(PriorityQueue):

    def get_attribute(self, name):
        return getattr(self, name)

    def set_attribute(self, name, data):
        return setattr(self, name, data)


SysManager.register("PriorityQueue", MyPriorityQueue)
SysManager.register('DB', models.DBCtrl)
SysManager.register('MEM_DB', libs.db.mem_db.DictDB)
manager = SysManager()
manager.start()
MEM_DB = manager.MEM_DB()
MEM_DB.set('real_time_look_get_data', {})

if conf.LOG_SERVER == True:
    # get_loging.LOCK = server.LOCK

    try:
        get_log = Process(target=get_loging.main)
        # get_log.daemon = True
        get_log.start()
    except Exception as e:
        stdout_logger.error(e, exc_info=True)
else:
    get_log = None

if conf.IPTASBLES == True and ban_proc.my_ssh_port != None:
    stdout_logger.info('USE IPTABLES')
    for i in ban_proc.IP_TABLESS:
        stdout_logger.info('SET ROW %s', i)
        os.system(i)
    cmd_tcp = 'sudo iptables -A INPUT -p tcp -s %s' + ' --dport %s -j ACCEPT' % (conf.DB_PORT)
    cmd_tcp_drop = 'sudo iptables -A INPUT -s %s -j DROP'
    for i in conf.OPEN_IP:
        if len(conf.OPEN_IP) > 0:
            if conf.OPEN_IP[i] == 'True':
                os.system('sudo iptables -D INPUT -j DROP')
                info = cmd_tcp % (i)
                stdout_logger.info('SET ROW %s', info)
                os.system(cmd_tcp % (i))
                os.system('sudo iptables -A INPUT -j DROP')
            if i == 'NEW_SVN_IP':
                pass
            elif i == '127.0.0.1':
                pass
            elif conf.OPEN_IP[i] == 'False':
                os.system('sudo iptables -D INPUT -j DROP')
                info = cmd_tcp_drop % (i)
                stdout_logger.info('SET ROW %s', info)
                os.system(cmd_tcp_drop % (i))
                os.system('sudo iptables -A INPUT -j DROP')
    # print os.popen('sudo iptables -L').read()
elif conf.BAN_PROC == True:
    ban = ban_proc.BanProc(log=log.get_log())
    # ban.daemon = True
    ban.start()

# if conf.DOC_SERVER == True:
#     doc_server_proc = Process(target=doc_server)
#     doc_server_proc.start()

def sync_time_from_ntp():
    stdout_logger.info('time sync proc')
    sleep = 2
    while True:
        time.sleep(sleep)
        dates = datetime.datetime.now()
        if dates.year < 2021:
            os.popen('sudo service ntp restart')
        time.sleep(60)
        new_dates = datetime.datetime.now()
        if new_dates.year >= 2021:
            break
        else:
            set_date_cmd = 'sudo date -s %s-%s-%s' % (dates.year, dates.month, dates.day)
            os.system(set_date_cmd)
            set_date_cmd = 'sudo date -s %s:%s' % (dates.hour, dates.minute)
            os.system(set_date_cmd)
            sleep = 120


if conf.RTC == True:
    try:
        date = server.client.send(evt='GET_DATE_TIME', ip='192.168.1.5', port=2522, timeout=conf.TIMEOUT)
        if date != None:
            os.system('sudo date -s %s' % date['dates'])
            os.system('sudo date -s %s' % date['times'])
        else:
            raise IOError
    except IOError:
        stdout_logger.error('no rtc mod')
else:
    sync_time_in_shedult = Process(target=sync_time_from_ntp, name='SyncTime')
    # sync_time_in_shedult.daemon = True
    sync_time_in_shedult.start()

# server.server.LOG_SERVER = log.get_log()
# server.DB = manager.DB()
# Q = manager.PriorityQueue()
# Q2 = manager.PriorityQueue()
# server.Q = Q
# server.Q2 = Q2
chk = chk_proc.Chk(log=log.get_log())
# chk.daemon = True
chk.start()
# DB = models.DBCtrl(my_session=True)
# rev = DB.get_one_where(models.Config, name='MinGuiRev')
# if rev == None:
#     my_rev = DB.make_obj(models.Config)
#     my_rev.name = 'MinGuiRev'
#     my_rev.value = conf.MinGuiRev
#     DB.add_object_to_session(my_rev)
#     DB.commit()
# elif int(rev.value) < int(conf.MinGuiRev):
#     rev.value = conf.MinGuiRev
#     DB.add_object_to_session(rev)
#     DB.commit()

server.EVENT = server.event.Evant()


if conf.TCP == False:
    my_server = Process(target=server.server.run_server, name='UDP_30593', kwargs={'handler':server.UDPHandler,
                            'crypt' : conf.CRYPT2,
                            'buffer':conf.BUFFER,
                            'timeout':conf.TIMEOUT_2,
                            'port':conf.PORT,
                            'ip':conf.IP,
                            'logging':log.get_log(),
                            'in_thread':conf.IN_THREAD,
                            'rsa':conf.RSA
    })
else:
    my_server = Process(target=server.tcp_server.run_server, name='TCP_30593',
                        kwargs={'handler': server.TCPHandler,
                                'crypt': conf.CRYPT2,
                                'buffer': conf.BUFFER,
                                'timeout': conf.TIMEOUT_2,
                                'port': conf.PORT,
                                'ip': conf.IP,
                                'logging': log.get_log(),
                                'in_thread': conf.IN_THREAD,
                                'rsa':conf.RSA
                                })
try:
    my_server.start()
except Exception as e:
    stdout_logger.error(e, exc_info=True)
# my_server.daemon = True

my_server_2 = Process(target=server.server.run_server, name='SMIB_UDP_40593', kwargs={'handler':server.SMIBHandler,
                        'crypt' : conf.CRYPT,
                        'buffer':conf.BUFFER,
                        'timeout':conf.TIMEOUT - 3,
                        'port':conf.PORT_2,
                        'ip':conf.IP,
                        'logging':log.get_log(),
                        'in_thread':conf.IN_THREAD,
})
# my_server_2.daemon = True
my_server_2.start()
CHANGE_KEY = True
sleep_time = 10
time.sleep(sleep_time)
EVENT = server.event.Evant(pipe=[server.SERVER_RESPONSE, server.SERVER2_RESPONSE], mem_db=MEM_DB)
# real_time = Process(target=server.event.real_time_look_get, args=[MEM_DB, log.get_log()])
# real_time.start()
EVENT.start()

# stop_log = False
while True:
    time.sleep(sleep_time)
    if EVENT.is_alive() == False:
        break
    # if real_time.is_alive() == False:
    #     real_time = Process(target=server.event.real_time_look_get, args=[MEM_DB, log.get_log()])
    #     real_time.start()
    if conf.TCP == False:
        if my_server.is_alive() == False or my_server_2.is_alive() == False or EVENT.is_alive() == False:
            stdout_logger.critical('REBOOT REDIRECT SYSTEM')
            stdout_logger.error('%s, %s, %s' % (my_server.is_alive() == False, my_server_2.is_alive() == False, EVENT.is_alive() == False))
            break
    else:
        if my_server_2.is_alive() == False or EVENT.is_alive() == False:
            stdout_logger.critical('REBOOT REDIRECT SYSTEM')
            break
        if my_server.is_alive() == False:
            try:
                my_server.terminate()
                my_server.join()
            except:
                pass
            my_server = Process(target=server.tcp_server.run_server, name='TCP_30593',
                                kwargs={'handler': server.TCPHandler,
                                        'crypt': conf.CRYPT2,
                                        'buffer': conf.BUFFER,
                                        'timeout': conf.TIMEOUT_2,
                                        'port': conf.PORT,
                                        'ip': conf.IP,
                                        'logging': log.get_log(),
                                        'in_thread': conf.IN_THREAD,
                                        'rsa':conf.RSA,
                                        })
            try:
                my_server.start()
            except:
                stdout_logger.info('TCP SERVER NOT START')
    if chk.is_alive() == False:
        stdout_logger.info('REDIRECT REBOOT CHK: not work')
        try:
            chk.terminate()
            chk.join()
        except:
            pass
        chk = chk_proc.Chk(log=log.get_log())
        # chk.daemon = True
        chk.start()
    if conf.LOG_SERVER == True:
        if get_log.is_alive() == False:
            # get_loging.LOCK = server.LOCK
            try:
                get_log.terminate()
                get_log.join()
            except:
                pass
            try:
                get_log = Process(target=get_loging.main)
                # get_log.daemon = True
                get_log.start()
            except:
                stdout_logger.info('LOGGING SERVER NOT START')
        # else:
        #     try:
        #         mem = os.popen('cat /proc/meminfo | grep MemFree:').read()
        #         mem = mem.split()
        #         if int(mem[1]) > 80856:
        #             stop_log = True
        #             get_log.terminate()
        #             # time.sleep(60)
        #         else:
        #             stop_log = False
        #     except:
        #         pass
    if conf.BAN_PROC == True:
        if ban.is_alive() == False:
            stdout_logger.info('REDIRECT REBOOT BAN: not work')
            try:
                ban.terminate()
                ban.join()
            except:
                pass
            ban = ban_proc.BanProc()
            # ban.daemon = True
            ban.start()
        if len(ban.my_file) > conf.MAX_DB_LOG_ROW:
            stdout_logger.info('REDIRECT REBOOT BAN: max log file')
            ban.terminate()
            ban.join()
            ban = ban_proc.BanProc()
            # ban.daemon = True
            ban.start()

    if my_server.is_alive() == True and my_server_2.is_alive() == True and EVENT.is_alive() == True:
        # if CHANGE_KEY == True and conf.COMUNICATION_IV_JUMP is True:
        #     CHANGE_KEY = False
        #     crypts = libs.cr.Crypt(crypts.COMUNICATION, crypts.IV, True, False)
        #     holder = shelve.open(conf.HOLDER, 'w')
        #     key = crypts.decrypt(holder['rand_key'])
        #     key = crypts.encrypt(key)
        #     holder['rand_key'] = key
        #     holder.sync()
        #     holder.close()
        sleep_time = 30

if conf.LOG_SERVER == True:
    if get_log.is_alive() == True:
        get_log.terminate()
        get_log.join()
# if real_time.is_alive() == True:
#     real_time.terminate()
#     real_time.join()
if my_server.is_alive() == True:
    my_server.terminate()
    my_server.join()
if my_server_2.is_alive() == True:
    my_server_2.terminate()
    my_server_2.join()
if EVENT.is_alive() == True:
    EVENT.terminate()
    EVENT.join()

stdout_logger.critical('REDIRECT GO DOWN')
os.system('sudo service colibri restart')
