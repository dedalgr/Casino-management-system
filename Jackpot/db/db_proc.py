#-*- coding:utf-8 -*-
from multiprocessing import Process
from threading import Thread
import conf  # @UnresolvedImport
from .db import MemDB, SQLite
import exception  # @UnresolvedImport
import time
import socket
from pymemcache.exceptions import MemcacheUnexpectedCloseError

class DBSync(Process):
    def __init__(self):
        Process.__init__(self)
        self.last_loop = time.time()


    def run(self):
        cach = MemDB()
        db = SQLite()
        time_start = time.time()


        while True:
            try:
                sync = False
                time.sleep(2)
                try:
                    sync = False
                    self.last_loop = time.time() + 240
                    for i in cach.keys():
                        if i != 'backup_log_stop':
                            data = cach.get_key(i)
                            if data != db.get_key(i):
                                if i == 'group':
                                    if cach.get_key('casino_name')['ip']:
                                        to_del = []
                                        for b in data:
                                            if data[b]['global_mistery'] is True:
                                                to_del.append(b)
                                        for c in to_del:
                                            del data[c]

                                db.set_key(i, data)
                                if not cach.get_key('REBOOT'):
                                    sync = True
                                else:
                                    sync = False
                    if sync == True:
                        db.sync()
                    cach.close()
                except socket.error:
                    pass
                except MemcacheUnexpectedCloseError:
                    pass
                except Exception as e:
                    exception.log.stderr_logger.error(e, exc_info=True)
                    try:
                        db.close()
                    except:
                        pass
                    try:
                        db = SQLite()
                    except Exception as e:
                        exception.log.stderr_logger.critical(e, exc_info=True)

                if time_start + 86400 < time.time():
                    time_start = time.time()
                    try:
                        db.db._backup('backup')
                        if cach.get_key('backup_log_stop') is False:
                            log = SQLite('log.db')
                            log.db._backup('backup')
                            log.close()
                    except Exception as e:
                        exception.log.stderr_logger.critical(e, exc_info=True)
            except Exception as e:
                exception.log.stderr_logger.critical(e, exc_info=True)
                time.sleep(10)


            
# def db_backup():
#     cach = MemDB()
#     # bk_db = SQLite(path = 'backup/')
#     while True:
#         time.sleep(3600)
#         if cach.get_key('REBOOT') == False:
#             try:
#                 print 'backup'
#                 log = SQLite('log.db')
#                 log.db._backup('backup')
#                 log.close()
#                 jp = SQLite()
#                 jp.db._backup('backup')
#                 jp.close()
#             except Exception as e:
#                 try:
#                     log.close()
#                     jp.close()
#                 except:
#                     pass
#                 print e
#                 raise exception.DBError, 'BAD BACKUP DB'
#             cach.close()
#         else:
#             cach.close()
#             time.sleep(60)
#
# def db_backup_proc():
#     server = Process(target=db_backup)
#     server.daemon = True
#     server.start()

# def db_sync_proc():
#     server = Process(target=sync_db)
#     # server.daemon = True
#     server.start()