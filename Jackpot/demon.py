# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.abspath('.'))))
import time
import conf
from multiprocessing import Process
# os.system('umount /dev/mmcblk1p1')
# os.system('mkdir %s' % (conf.DB_PATH))
# os.system('mount /dev/mmcblk1p1 /mnt/sdcart/')
import db
import security
import exception
import exception.log
# if conf.ERR_USE_FILE == True:
#     import exception.log  # @UnusedImport
print('USE IPTABLES')
for i in conf.IP_TABLESS:
    print('SET ROW', i)
    os.system(i)


hard_db = db.db.SQLite()
try:
    hard_db.get_key('INIT')
    global_ip = hard_db.get_key('casino_name')
    if 'ip' not in global_ip:
        global_ip['ip'] = ''
        hard_db.set_key('casino_name', global_ip)
        hard_db.sync()
        # hard_db.close()
except KeyError:
    hard_db.set_key('INIT', {
        'crc': security.mk_uuid.mk_crc(),
        'init_time': time.time(),
        'version': '1.0.1',
        'soft_uuid': security.mk_uuid.mk_soft_id(),
        'hw_uuid': security.mk_uuid.hw_uuid()
    }
                    )
    hard_db.set_key('work', {})
    hard_db.set_key_to('work', 'can_work', False)
    hard_db.set_key_to('work', 'error', exception.EXCEPTION_MSG['INIT'])
    hard_db.set_key_to('work', 'work_to', None)
    hard_db.set_key('users', {})
    hard_db.set_key_to('users', 'root', {'name': 'root', 'passwd': '123456'})
    hard_db.set_key_to('users', 'MistralCMS', {'name': 'MistralCMS', 'passwd': 'use_system10'})
    hard_db.set_key('smib', {})
    hard_db.set_key('visual', {})
    hard_db.set_key('group', {})
    # hard_db.set_key('log', {})
    hard_db.set_key('casino_name', {'name': '', 'ip':''})
    # hard_db.set_key('sleiv', {})
    hard_db.set_key('down_stop', {})
    hard_db.set_key('go_down', {})
    # hard_db.set_key('backup_log_stop', False)
    hard_db.sync()

global_ip = hard_db.get_key('casino_name')
hard_db.close()
log = db.db.SQLite(name='log.db')
log.close()

import security.init
import udp
import rtc
import datetime

os.system('mkdir backup')

DB = db.db.MemDB(True)
# DB.set_key('stop_rotation', False)

def sync_time_from_ntp():
    print('time sync proc')
    sleep = 60
    while True:
        # time.sleep(sleep)
        dates = datetime.datetime.now()
        if dates.year < 2021:
            os.popen('sudo service ntp restart')
        else:
            break
        time.sleep(sleep)
        new_dates = datetime.datetime.now()
        if new_dates.year >= 2021:
            break
        else:
            set_date_cmd = 'sudo date -s %s-%s-%s' % (dates.year, dates.month, dates.day)
            os.system(set_date_cmd)
            set_date_cmd = 'sudo date -s %s:%s' % (dates.hour, dates.minute)
            os.system(set_date_cmd)
            sleep = 120
try:
    rtc.Sync_RTC()
except:
    sync_time_in_shedult = Process(target=sync_time_from_ntp)
    sync_time_in_shedult.start()
    # DB.set_key_to('work', 'work_to', None)
    # DB.set_key_to('work', 'work_to', None)
    # DB.set_key_to('work', 'error', exception.EXCEPTION_MSG['NO RTC'])

# smib = DB.get_key('smib')
# for item in smib:
#         for i in range(3):
#             udp.client.send(ip=item, evt='JP_Q_CLEAN', timeout=conf.UDP_VISUAL_TIMEOUT)

visual = DB.get_key('visual')
for item in visual:
    data = udp.client.visual_send(ip=item, evt='SET_DB', port=conf.UDP_VISUAL_PORT, timeout=5)

# db.db_proc.db_sync_proc()



# db.db_proc.db_backup_proc()
if conf.NOT_CHK_ON_START == False:
    try:
        security.init.Start_CHK()
    except Exception as e:
        udp.server.LOG_SERVER.error(e, exc_info=True)
    udp.server.start_chk_prok()


# import games
# if DB.get_key('casino_name')['ip']:
#     tunel_server = db.db.Tunel(server=DB.get_key('casino_name')['ip'], port=44554)
#     tunel_server.start()
# casino_name = DB.get_key('casino_name')
# try:
#     addf_bet_key = DB.mem_cach2.get('ADD_BET')
# except:
#     addf_bet_key = DB.mem_cach.get('ADD_BET')
# if not addf_bet_key:

if global_ip['ip']:
    tunel_server = db.db.Tunel(server=global_ip['ip'], port=55555, level=exception.log.level, log=exception.log.stdout_logger)
    tunel_server.start()
    for i in range(3):
        try:
            DB.mem_cach2.set('DOWN', {'evt': 'SET_DB', 'time':time.time()})
            break
        except:
            time.sleep(5)
else:
    DB.mem_cach.set('DOWN', {'evt': 'SET_DB', 'time':time.time()})
# try:
#     DB.mem_cach2.delete('lock')
# except:Tunel
DB.delete_lock()
down_stop = DB.get_key('down_stop')
for i in down_stop.keys():
    down_stop[i] = False
DB.set_key('down_stop', down_stop)
udp.server.start_add_bet_proc()
udp.server.run_visual_proc()
my_server = udp.server.server.run_server(
    handler=udp.server.Handler,
    crypt=udp.server.CRYPT,
    buffer=conf.UDP_BUFFER,
    timeout=conf.UDP_TIMEOUT,
    port=conf.UDP_JP_PORT,
    ip='0.0.0.0',
    in_thread=conf.IN_THREAD,
    logging=exception.log.stderr_logger
)

try:
    DB.tunel_server.close()
    DB.tunel_server.terminate()
except:
    pass

try:
    udp.server.chk_db_sync.abort()
    udp.server.DB_PROC.terminate()
    udp.server.DB_PROC.join()
    tunel_server.close()
    tunel_server.terminate()
except:
    pass

