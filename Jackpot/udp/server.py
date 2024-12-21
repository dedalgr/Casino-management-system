# -*- coding:utf-8 -*-
import events  # @UnresolvedImport
import security  # @UnresolvedImport
import cr  # @UnresolvedImport
import time
import random
from multiprocessing import Process
from multiprocessing import Pipe
import threading
# from multiprocessing import Queue
from queue import PriorityQueue
from queue import Empty
import conf  # @UnresolvedImport
import db  # @UnresolvedImport
from exception import log
from . import client
import games

DB_PROC = db.db_proc.DBSync()
DB_PROC.start()

DB = db.db.MemDB()
if conf.IV_JUMP is False:
    CRYPT = cr.Crypt(cr.COMUNICATION, cr.IV, conf.IV_JUMP)
else:
    CRYPT = cr.CryptFernet(cr.key)
import sock.udp_socket.server as server

server.LOG_SERVER = log.stderr_logger
if conf.ERR_LOG_COUNT == 1:
    server.LOG_SERVER.setLevel(server.logging.ERROR)
elif conf.ERR_LOG_COUNT == 2:
    server.LOG_SERVER.setLevel(server.logging.WARNING)
elif conf.ERR_LOG_COUNT == 3:
    server.LOG_SERVER.setLevel(server.logging.INFO)
elif conf.ERR_LOG_COUNT == 4:
    server.LOG_SERVER.setLevel(server.logging.DEBUG)
Q = PriorityQueue()

class Prioritize:

    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

LOCK = threading.Lock()

class CHKDBSYNC(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._break = False

    def abort(self):
        self._break = True

    def run(self):
        global DB_PROC
        while True:
            time.sleep(120)
            if self._break:
                return
            if DB_PROC.is_alive() == False:
                DB_PROC = db.db_proc.DBSync()
                DB_PROC.start()
            # else:
            #     raise KeyError(DB_PROC.last_loop, time.time())
            #     if DB_PROC.last_loop > time.time():
            #         DB_PROC.terminate()
            #         DB_PROC = db.db_proc.DBSync()
            #         DB_PROC.start()

class Handler(server.EchoRequestHandler):
    def handle(self):
        try:
            global Q
            if conf.IN_THREAD == True:
                LOCK.acquire()
            # self.handle_timeout()
            data = self.get_data()

            if data != None and data != False and data != self:
                casino_name = DB.get_key('casino_name')
                # raise KeyError(data[0], "ACTIV")
                # data[1]['real_ip'] = self.client_address[0]
                self.log.debug('SERVER REQUEST %s', data)
                if data[0] == 'ALIFE':
                    kwargs = data[1]
                    try:
                        if casino_name['ip']:
                            DB.mem_cach2.set('ALIFE', True)
                    except:
                        pass
                    data = events.GLOBAL_EVENT[data[0]](**kwargs)
                elif data[0] == 'ALIFE_VISUAL' or data[0] == 'chk_alife':
                    kwargs = data[1]
                    data = events.GLOBAL_EVENT[data[0]](**kwargs)
                else:
                    db_key = DB.get_key('work')
                    if db_key['can_work'] == True:
                        if data[0] == 'add_bet':
                            Q.put(Prioritize(1,data))
                            data = True
                            self.send_data(data)
                            self.log.debug('SERVER REQUEST %s', True)
                            return True
                        else:

                            if data[0] in events.GLOBAL_EVENT:
                                try:
                                    kwargs = data[1]
                                    data = events.GLOBAL_EVENT[data[0]](**kwargs)
                                except IndexError:
                                    data = events.GLOBAL_EVENT[data[0]]()
                            else:
                                try:
                                    kwargs = data[1]
                                    data = events.ee(data[0], **kwargs)
                                except IndexError:
                                    data = events.ee(data[0])

                    else:
                        DB.set_lock()
                        if data[0] == "ACTIV":
                            key = data[1]
                            try:
                                chk = security.mk_uuid.activate_code(key['key'], key['base'])
                            except ValueError:
                                chk = False, None
                            except TypeError:
                                chk = False, None
                            if chk[0] != True:
                                data = security.mk_uuid.base_code(db_key['error'])
                            else:
                                data = True
                                DB.set_key_to('work', 'can_work', chk[0])
                                DB.set_key_to('work', 'work_to', chk[1])
                                DB.delete_lock()
                                visual = DB.get_key('visual')

                                if casino_name['ip']:
                                    try:
                                        DB.mem_cach2.set('DOWN', {'evt': 'SET_DB', 'time':time.time()})
                                    except:
                                        pass
                                else:
                                    DB.mem_cach.set('DOWN', {'evt': 'SET_DB', 'time':time.time()})

                                for item in visual:
                                    for i in range(3):
                                        client.send(ip=item, evt='SET_DB', timeout=conf.UDP_VISUAL_TIMEOUT,
                                             port=conf.UDP_VISUAL_PORT)

                        elif data[0] == 'run_linux_cmd':
                            if data[0] in events.GLOBAL_EVENT:
                                try:
                                    kwargs = data[1]
                                    data = events.GLOBAL_EVENT[data[0]](**kwargs)
                                except IndexError:
                                    data = events.GLOBAL_EVENT[data[0]]()
                            else:
                                try:
                                    kwargs = data[1]
                                    data = events.ee(data[0], **kwargs)
                                except IndexError:
                                    data = events.ee(data[0])
                        else:
                            if data[0] == 'LOGIN':
                                data = 'ACTIV', security.mk_uuid.base_code(db_key['error'])
                            else:
                                return
                        # DB.set_key('stop_rotation', True)
                self.log.debug('SERVER RESPONSE %s', data)
                self.send_data(data)

        except Exception as e:
            # DB.set_key('stop_rotation', False)
            self.log.error(e, exc_info=True)
        if conf.IN_THREAD == True:
            try:
                LOCK.release()
            except:
                pass
        return True


def add_bet_proc(pipe):
    while True:
        data = Q.get()
        data = data.item
        server.LOG_SERVER.info('ADD_BET REQUEST %s', data)
        # while DB.check_for_lock():
        #     server.LOG_SERVER.info('LOCK: %s', DB.check_for_lock())
        try:

            kwargs = data[1]
            data = events.ee(data[0], **kwargs)
            server.LOG_SERVER.info('ADD_BET RESPONSE %s', data)
            if len(Q.queue) > conf.Q_COUNT:
                server.LOG_SERVER.info('clean server q')
                while True:
                    try:
                        Q.get_nowait()
                    except Empty:
                        break
        except Exception as e:
            server.LOG_SERVER.error(e, exc_info=True)
            # DB.delete_lock()


def start_add_bet_proc():
    global Q
    # import games
    # games.create_proc()
    server = threading.Thread(target=add_bet_proc, args=(Q,))
    server.daemon = True
    server.start()


def start_chk():
    while True:
        time.sleep(random.randint(3600, 18000))
        try:
            security.init.Start_CHK()
            security.init.naem()
        except Exception as e:
            server.LOG_SERVER.error(e, exc_info=True)


def start_chk_prok():
    server = threading.Thread(target=start_chk)
    server.start()


def send_to_visual():
    add_bet_old = None
    casino_name = DB.get_key('casino_name')
    for i in range(3):
        time.sleep(3)
        if add_bet_old:
            break
        if casino_name['ip']:
            add_bet_old = DB.mem_cach2.get('ADD_BET')
            down_old = DB.mem_cach2.get('DOWN')
        else:
            add_bet_old = DB.mem_cach.get('ADD_BET')
            down_old = DB.mem_cach.get('DOWN')

    add_bet_new = {}
    down_new = {}
    while True:
        try:
            if casino_name['ip']:
                add_bet_new = DB.mem_cach2.get('ADD_BET')
                down_new = DB.mem_cach2.get('DOWN')
            else:
                add_bet_new = DB.mem_cach.get('ADD_BET')
                down_new = DB.mem_cach.get('DOWN')
            if down_new != down_old:
                visual = DB.get_key('visual')
                for item in visual:
                    for i in range(3):
                        client.visual_send(ip=item, **down_new)
            # if add_bet_new == None and add_bet_old == None:
            #     time.sleep(10)
            #     server.LOG_SERVER.debug('add_bet_new %s, add_bet_old: %s' % (add_bet_new, add_bet_old))
            elif add_bet_new != add_bet_old:
                data = DB.get_key('group')
                data = data[add_bet_new['grup']]
                visual = DB.get_key('visual')
                for i in visual:
                    if add_bet_new['grup'] == visual[i]['group']:
                        games.send_to_visual_direct(ip=i, **add_bet_new)
        except Exception as e:
            log.stderr_logger.critical(e, exc_info=True)
        down_old = down_new
        add_bet_old = add_bet_new


def run_visual_proc():
    visual_proc = threading.Thread(target=send_to_visual)
    visual_proc.start()

chk_db_sync = CHKDBSYNC()
chk_db_sync.start()
# if __name__ == '__main__':
#     start_add_bet_proc()
