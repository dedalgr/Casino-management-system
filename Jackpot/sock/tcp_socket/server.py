# -*- coding:utf-8 -*-
'''
Created on 7.09.2018 г.

@author: dedal
'''
import socketserver as SocketServer
import logging
from multiprocessing import log_to_stderr
import threading
import socket
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
)
LOG_SERVER = log_to_stderr()
LOG_SERVER.setLevel(logging.DEBUG)

CRYPT = None
SERVER_IN_THREADING = False
BUFFER = 10
PORT = 2522
SERVER_USE_JSON = True
TIMEOUT = 10
IP = '127.0.0.1'
RSA = False

# if SERVER_USE_JSON == False:
try:
    import _pickle as pickle  # @UnusedImport
except:
    import pickle  # @Reimport @UnusedImport
# else:
import json
import time

REQUEST = {}

class BadSignature(Exception):
    pass


class EchoRequestHandler(SocketServer.BaseRequestHandler):

    def sig(self, msg):
        return self.RSA.get_signature(msg)

    def verify(self, msg):
        data = json.loads(msg)
        if self.RSA.verify(data[0], data[1]) is True:
            return data[0]
        else:
            raise BadSignature(data)

    def crypt_decrypt(self, data):
        # LOG_SERVER.error('SERVER DECRYPT: %s', data )
        if CRYPT != None and self.RSA is False:
            # if RSA == False:
            #     data = CRYPT.decrypt(data)
            # else:
            data = CRYPT.decrypt(data)
            # LOG_SERVER.error('SERVER DECRYPT: %s', data )
        elif CRYPT != None and self.RSA is not False:
            data = CRYPT.decrypt(data)
            data = self.verify(data)

        try:
            if SERVER_USE_JSON == False:
                data = pickle.loads(data)
            else:
                data = json.loads(data)
        except Exception as e:
            raise e(data)
        return data

    def crypt_encrypt(self, data):
        if CRYPT != None:
            if SERVER_USE_JSON == False:
                if self.RSA == False:
                    data = CRYPT.encrypt(pickle.dumps(data))
                else:
                    signature = self.sig(pickle.dumps(data))
                    data = pickle.dumps([data, signature])
                    data = CRYPT.encrypt(pickle.dumps(data))
            else:
                if self.RSA == False:
                    data = CRYPT.encrypt(json.dumps(data))
                else:
                    data = json.dumps(data)
                    signature = self.sig(data)
                    data = json.dumps([data, signature])
                    data = CRYPT.encrypt(data)
        else:
            if SERVER_USE_JSON == False:
                data = pickle.dumps(data)
            else:
                data = json.dumps(data)
        return data

    def get_data(self):
        self.time = time.time()
        data = b''
        # var = b''
        while True:
            var = self.request.recv(BUFFER)
            data += var
            if data[-4:] == b'EXIT':
                break
            if time.time() > self.time + (TIMEOUT / 2):
                raise socket.timeout(data)
        data = data.replace(b'EXIT', b'')
        # if data == b'':
        #     data = None
        data = self.crypt_decrypt(data)
        self.log.debug('GET DATA: %s', data)
        return data

    def send_data(self, data):
        data = self.crypt_encrypt(data) + b'EXIT'
        # data = self.crypt_encrypt(data)
        self.request.sendall(data)
        return True

    # def send_data(self, msg):
    #     self.log.debug('SEND DATA: %s', msg)
    #     self.request.sendall(self.crypt_encrypt(msg) + 'EXIT')
    #     # self.request.sendall()
    #     return True

    # def handle_timeout(self):
    #     pass

    # def finish(self):
    #     self.request.close()

    def handle(self):  # @UndefinedVariable @ReservedAssignment
        data = self.get_data()
        data = 'b' * 10000
        self.send_data(data)
        return True


class ThreadedServer(SocketServer.ThreadingTCPServer, SocketServer.TCPServer):
    pass


def run_server(handler=EchoRequestHandler, **kwargs):  # @UndefinedVariable
    '''
    Стартита TCP сървър като демон.
    Използва _tcp.EchoRequestHandler
    :param port:  Порт на лоцалния TCP сървър. Взима се от conf
    :param args: Ne se podawat argumenti
    :return: Не връща резултат. Стартира безкраен демон.
    '''
    global LOG_SERVER
    global CRYPT
    global SERVER_USE_JSON
    global TIMEOUT
    global BUFFER
    global SERVER_IN_THREADING
    global PORT
    global IP
    global RSA

    if 'crypt' in kwargs:
        CRYPT = kwargs['crypt']

    if 'use_json' in kwargs:
        SERVER_USE_JSON = kwargs['use_json']

    if 'timeout' in kwargs:
        TIMEOUT = kwargs['timeout']

    if 'buffer' in kwargs:
        BUFFER = kwargs['buffer']

    if 'in_thread' in kwargs:
        SERVER_IN_THREADING = kwargs['in_thread']

    if 'port' in kwargs:
        PORT = kwargs['port']

    if 'ip' in kwargs:
        IP = kwargs['ip']

    address = (IP, PORT)  # let the kernel give us a port


    if SERVER_IN_THREADING == True:
        server = ThreadedServer(address, handler)
    else:
        server = SocketServer.TCPServer(address, handler)

    # server._handle_request_noblock()
    server.allow_reuse_address = True
    server.allow_reuse = True
    #     server.timeout = TIMEOUTSocketServer
    # server._handle_request_noblock = True
    server.timeout = TIMEOUT
    if 'logging' in kwargs:
        handler.log = kwargs['logging']
    else:
        handler.log = LOG_SERVER
    if 'rsa' in kwargs:
        handler.RSA = kwargs['rsa']
    else:
        handler.RSA = RSA
    handler.log.info('SERVER PROC STARTING!')
    handler.log.info('BIND: %s', address)
    handler.log.info('IN THREAD: %s', SERVER_IN_THREADING)
    handler.log.info('CRYPT: %s', CRYPT)
    handler.log.info('BUFFER: %s', BUFFER)
    handler.log.info('RSA: %s', handler.RSA)
    handler.log.info('%s started at %s' % (server.__class__.__name__, server.server_address))
    # t = threading.Thread(target=server.serve_forever())
    # t.start()
    return server.serve_forever()


if __name__ == '__main__':
    run_server()
