# -*- coding:utf-8 -*-
'''
Created on 7.09.2018 г.

@author: dedal
'''
import socketserver as SocketServer
import logging
from multiprocessing import log_to_stderr
import threading
import time
import socket
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
)
LOG_SERVER = log_to_stderr()
LOG_SERVER.setLevel(logging.DEBUG)

CRYPT = None
SERVER_IN_THREADING = False
BUFFER = 4096
PORT = 30593
SERVER_USE_JSON = True
TIMEOUT = 10
IP = '0.0.0.0'
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
        data = self.request[0]
        self.time = time.time()
        var = b''
        while True:
            data = data + var
            if data[-4:] == b'EXIT':
                break
            # if time.time() > self.time + (TIMEOUT/2):
            #     raise socket.timeout, data
            var = self.request[1].recv(BUFFER)

        data = data.replace(b'EXIT', b'')
        data = self.crypt_decrypt(data)
        return data

    def send_data(self, data):
        data = self.crypt_encrypt(data) + b'EXIT'
        start = 0
        end = BUFFER
        #         count = 1
        while True:
            if len(data[start:]) < BUFFER:
                self.request[1].sendto(data[start:], self.client_address)
                break
            else:
                self.request[1].sendto(data[start:end], self.client_address)
                time.sleep(0.1)
            # count += 1
            start = end
            end += BUFFER
            # if time.time() > self.time + (TIMEOUT):
            #     raise socket.timeout
        return True

    # def handle_timeout(self):
    #     pass

    #         request_time = time.time() + TIMEOUT
    #         for i in REQUEST:
    #             if i > request_time:
    #                 del REQUEST[i]
    # def finish(self):
    #     self.request.close()

    def handle(self):  # @UndefinedVariable @ReservedAssignment
        # self.handle_timeout()
        data = self.get_data()
        if data != self:
            data = {'b':5}
            self.send_data(data)
        return True


class EchoRequestHandlerInThread(EchoRequestHandler):
    pass


# class ThreadedServer(SocketServer.ThreadingUDPServer, SocketServer.UDPServer):
#     pass

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
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
        server = SocketServer.UDPServer(address, handler)

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
    # return server
