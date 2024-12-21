import _pickle as pickle
import logging
import logging.handlers
import socketserver as SocketServer
import struct
from datetime import datetime
import libs.rtc.date_format
import conf
# import log
# import json
import time
import socket
import threading
LAST_LOG = {}
TIME_TO_WRITE = 300
try:
    from collections import deque
except ImportError:
    # pre 2.5
    class deque(list):
        def popleft(self):
            elem = self.pop(0)
            return elem

try:
    reversed
except NameError:
    # pre 2.4
    def reversed(items):
        return items[::-1]
# from threading import Thread
# from Queue import Queue
# Q = Queue()
# LOG = log.get_log(logging.ERROR)
# DB =
# DB.connect()
# class WriteLog(Thread):
#     def __init__(self, q):
#         self.q = q
#         # global DB
#         self.db = libs.db.sql_db.PostgreSQL(dbname=conf.DB_NAME, user=conf.DB_USER, host=conf.DB_IP, passwd=conf.DB_PASS, port=conf.DB_PORT)
#
#         self.log = LOG
#         Thread.__init__(self)
#
#     def run(self):
#         while True:
#             data = self.q.get()
#             self.db.connect()
#             try:
#
#                 device = self.db.get_all(
#                     "select * from mashin where sas=True and enable=True and ip='%s'" % (data[0]))
#
#                 if device != []:
#                     start_date = datetime.fromtimestamp(time.time() - TIME_TO_WRITE)
#                     # end_date = datetime.fromtimestamp(record.created)
#                     start_date = datetime.strftime(start_date, '%Y-%m-%d %H:%M:%S')
#                     # end_date = datetime.strftime(end_date, '%d.%m.%Y %H:%M:%S')
#                     # raise KeyError, (start_date, end_date, record.filename, record.msg, record.levelname, record.processName)
#                     # obj = self.db.get_all_where(models.Log, device_id=device.id, asctime__gte=start_date, msg=record.msg, name=record.filename, level=record.levelname, proces_name=record.processName)
#                     try:
#                         data[1].msg = data[1].msg.replace("'", '"')
#                     except AttributeError:
#                         data[1].msg = ''
#                     try:
#                         data[1].exc_text = data[1].exc_text.replace("'", '"')
#                     except AttributeError:
#                         data[1].exc_text = ''
#                     # record.msg = record.msg.replace("'", '"')
#                     # LOG.error(record.exc_text)
#                     # LOG.error("""select * from system_log where device_id=%s and pub_time>'%s' and lineno='%s' and name='%s' and level='%s' and proces_name='%s' and msg_text='%s'""" %
#                     #     (device[0][0], start_date, str(record.lineno), record.filename, record.levelname,
#                     #      record.processName, record.msg))
#                     obj = self.db.get_all(
#                         """select * from system_log where device_id=%s and pub_time>'%s' and lineno='%s' and name='%s' and level='%s' and proces_name='%s' and msg_text='%s'""" %
#                         (device[0][0], start_date, str(data[1].lineno), data[1].filename, data[1].levelname,
#                          data[1].processName, data[1].msg))
#                     # LOG.debug('obj: %s', obj)
#                     if obj == []:
#                         # raise KeyError, obj
#                         cmd = """INSERT INTO system_log(asctime, level, name, proces_name, func_name, lineno, msg_text, device_id, text, pub_time) VALUES
#                         ('%s','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
#                             datetime.strftime(datetime.fromtimestamp(data[1].created), '%Y-%m-%d %H:%M:%S'),
#                             data[1].levelname,
#                             data[1].filename, data[1].processName, data[1].funcName, str(data[1].lineno),
#                             data[1].msg, device[0][0], data[1].exc_text,
#                             datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
#                         )
#
#                         self.db.set(cmd)
#                         self.db.commit()
#
#                         # self.db.dispose()
#             except Exception as e:
#                 self.log.error(e, exc_info=True)
#             try:
#                 self.db.close()
#             except Exception:
#                 pass
class MostRecentHandler(logging.Handler):
    'A Handler which keeps the most recent logging records in memory.'

    def __init__(self, max_records=2000):
        logging.Handler.__init__(self)
        self.logrecordstotal = 0
        self.max_records = max_records
        try:
            self.db = deque([], max_records)
        except TypeError:
            # pre 2.6
            self.db = deque([])

    def emit(self, record):
        self.logrecordstotal += 1
        try:
            self.db.append(record)
            # pre 2.6
            while len(self.db)>self.max_records:
                self.db.popleft()
        except Exception:
            self.handleError(record)

class LogRecordStreamHandler(SocketServer.StreamRequestHandler):
    'Handler for a streaming logging request'

    def handle(self):
        '''
        Handle multiple requests - each expected to be a 4-byte length,
        followed by the LogRecord in pickle format.
        '''
        while 1:
            chunk = self.connection.recv(4)
            if len(chunk) < 4:
                break
            slen = struct.unpack('>L', chunk)[0]
            chunk = self.connection.recv(slen)
            while len(chunk) < slen:
                chunk = chunk + self.connection.recv(slen - len(chunk))
            obj = self.unPickle(chunk)
            record = logging.makeLogRecord(obj)
            self.handleLogRecord([self.client_address[0], record])



    def unPickle(self, data):
        data = pickle.loads(data)
        data['name'] = self.client_address[0]
        return data

    def handleLogRecord(self, data):
        global LAST_LOG
        # if self.server.logname is not None:
        #     name = self.server.logname
        # else:
        #     name = data[0]
        try:

            tmp = [data[1].levelname,
                   data[1].filename, data[1].processName, data[1].funcName, str(data[1].lineno), data[1].msg, data[1].exc_text]
            tmp = pickle.dumps(tmp)
            for i in list(LAST_LOG.keys()):
                for b in list(LAST_LOG[i].keys()):
                    if LAST_LOG[i][b] <= time.time() - TIME_TO_WRITE:
                        # print ('del')
                        del LAST_LOG[i][b]
            # tmp = pickle.dumps(data[1])
            # time.sleep(0.2)
            # print (LAST_LOG)
            if data[0] in LAST_LOG:
                if tmp in LAST_LOG[data[0]]:
                    return True
                else:
                    LAST_LOG[data[0]][tmp] = time.time()
            else:
                LAST_LOG[data[0]] = {}
                LAST_LOG[data[0]][tmp] = time.time()
            # print LAST_LOG
            if len(LAST_LOG[data[0]]) > 20:
                LAST_LOG[data[0]] = {}
            logger = logging.getLogger(data[1].name)
            logger.handle(data[1])
            self.db.connect()
            device = self.db.get_all(
                "select * from mashin where sas=True and enable=True and ip='%s'" % (data[0]))

            if device != []:
                start_date = datetime.fromtimestamp(time.time() - TIME_TO_WRITE)
                # end_date = datetime.fromtimestamp(record.created)
                start_date = datetime.strftime(start_date, '%Y-%m-%d %H:%M:%S')
                # end_date = datetime.strftime(end_date, '%d.%m.%Y %H:%M:%S')
                # raise KeyError, (start_date, end_date, record.filename, record.msg, record.levelname, record.processName)
                # obj = self.db.get_all_where(models.Log, device_id=device.id, asctime__gte=start_date, msg=record.msg, name=record.filename, level=record.levelname, proces_name=record.processName)
                try:
                    data[1].msg = data[1].msg.replace("'", '"')
                except AttributeError:
                    data[1].msg = ''
                try:
                    data[1].exc_text = data[1].exc_text.replace("'", '"')
                except AttributeError:
                    data[1].exc_text = ''
                # record.msg = record.msg.replace("'", '"')
                # LOG.error(record.exc_text)
                # LOG.error("""select * from system_log where device_id=%s and pub_time>'%s' and lineno='%s' and name='%s' and level='%s' and proces_name='%s' and msg_text='%s'""" %
                #     (device[0][0], start_date, str(record.lineno), record.filename, record.levelname,
                #      record.processName, record.msg))
                # obj = self.db.get_all(
                #     """select * from system_log where device_id=%s and pub_time>'%s' and lineno='%s' and name='%s' and level='%s' and proces_name='%s'""" %
                #     (device[0][0], start_date, str(data[1].lineno), data[1].filename, data[1].levelname,
                #      data[1].processName))
                # LOG.debug('obj: %s', obj)
                # if obj != []:
                #     return True
                cmd = """INSERT INTO system_log(asctime, level, name, proces_name, func_name, lineno, msg_text, device_id, text, pub_time) VALUES 
                                ('%s','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                        datetime.strftime(datetime.fromtimestamp(data[1].created), '%Y-%m-%d %H:%M:%S'),
                        data[1].levelname,
                        data[1].filename, data[1].processName, data[1].funcName, str(data[1].lineno),
                        data[1].msg, device[0][0], data[1].exc_text,
                        datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
                    )

                self.db.set(cmd)
                self.db.commit()
                self.db.close()
        except Exception as e:
            print(e)
        try:
            self.db.close()
        except Exception:
            pass
        return True
        # global Q
        # Q.put([self.client_address[0] ,record])


class LoggingReceiver(SocketServer.TCPServer):
    'Simple TCP socket-based logging receiver'

    logname = None

    def __init__(self, host='0.0.0.0',
                 port=None,
                 handler=LogRecordStreamHandler):
        if port is None:
            port = logging.handlers.DEFAULT_TCP_LOGGING_PORT
        handler.db = libs.db.sql_db.PostgreSQL(dbname=conf.DB_NAME, user=conf.DB_USER, host=conf.DB_IP,
                                            passwd=conf.DB_PASS,
                                            port=conf.DB_PORT)
        SocketServer.TCPServer.__init__(self, (host, port), handler)

def main():
    # global Q
    # t = WriteLog(Q)
    # t.start()
    mostrecent = MostRecentHandler()
    rootLogger = logging.getLogger('')
    rootLogger.setLevel(logging.DEBUG)
    rootLogger.addHandler(mostrecent)
    recv = LoggingReceiver()
    # thr_recv = Thread(target=recv.serve_forever)
    # thr_recv.daemon = True
    recv.allow_reuse_address = True
    print('%s started at %s' % (recv.__class__.__name__, recv.server_address))
    # thr_recv = threading.Thread(target=recv.serve_forever)
    # thr_recv.daemon = True
    # print '%s started at %s' % (recv.__class__.__name__, recv.server_address)
    # thr_recv.start()
    return recv.serve_forever()

if __name__ == "__main__":
    main()
    # start_date = datetime.fromtimestamp(time.time() - TIME_TO_WRITE)
    # # end_date = datetime.fromtimestamp(record.created)
    # start_date = datetime.strftime(start_date, '%Y-%m-%d %H:%M:%S')
    # print start_date
    # db = libs.db.sql_db.PostgreSQL(dbname=conf.DB_NAME, user=conf.DB_USER, host='62.176.117.216', passwd=conf.DB_PASS,
    #                                port=conf.DB_PORT)
    # db.connect()
    # obj =db.get_all(
    #     """select * from system_log where device_id=%s and pub_time>'%s' and lineno='%s' and name='%s' and level='%s' and proces_name='%s' and msg_text='%s'""" %
    #     (26,
    #      '2021-10-11 19:40:37',
    #      258,
    #      'process.py',
    #      'ERROR',
    #      'SAS',
    #      'client_bonus: sas response {"Transfer type": "Transfer bonus coin out win amount from host to gaming machine", "Cashable amount": 0.0, "Length": 17, "Asset number": "01000000", "Transfer status": "Not a valid transfer function (unsupported type, amount, index, etc.)", "Transaction ID": "2020202020202020202020202020203f5f", "Receipt status": "No receipt requested or receipt not printed", "Transaction ID length": "11", "Restricted amount": 0.0, "Nonrestricted amount": 0.0, "Transfer flags": "01"}'))
