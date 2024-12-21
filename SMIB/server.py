#-*- coding:utf-8 -*-
'''
Created on 27.01.2019 г.

@author: dedal
'''
import libs.sock.udp_socket.server as server
import time
import threading
import conf
IN_THREAD = False
PIPE= {}
DB = None
LOCK = threading.Lock()
class Handler(server.EchoRequestHandler):

    def old_poll_clean(self):
        for i in PIPE:
            if PIPE[i].poll():
                PIPE[i].recv()
                
    def handle(self):
        global PIPE
        no_response = False
        # self.handle_timeout()
        try:
            data = self.get_data()
            if data != None and data is not False and data != self:
                self.log.debug('get data: %s', data)
                if IN_THREAD is True:
                    LOCK.acquire()
                request_time = time.time() + (server.TIMEOUT-6)
                if 'no_response' in data[1]:
                    no_response = data[1]['no_response']
                    del data[1]['no_response']
                data[1]['request_time'] = request_time
                if data[0][0:4] == 'sas.':
                    if data[0] == 'sas.meter':
                        data = DB.get('SAS_METER')
                    elif data[0] == 'sas.mether_count':
                        data = DB.get('SAS_METER_IN_COUNT')
                    else:
                        while PIPE['sas'].poll():
                            PIPE['sas'].recv()
                        # if data[0] == 'sas.jp_down':
                        #     jp = True
                        # else:
                        #     jp = False
                        PIPE['sas'].send(data)
                        server.LOG_SERVER.info('%s', data)
                        data = None
                        if PIPE['sas'].poll(server.TIMEOUT-2):
                            data = PIPE['sas'].recv()
                        # if data == None and jp == True:
                        #     data = False
                else:
                    if data[0] == 'real_time_look':
                        count = DB.get('SAS_METER_IN_COUNT')
                        if count != None and count is not False:
                            player = DB.get('PLAYER')
                            if player:
                                count['player'] = player['name']
                            else:
                                count['player'] = player
                        data = count
                    else:
                        while PIPE['watchdog'].poll():
                            PIPE['watchdog'].recv()
                        PIPE['watchdog'].send(data)
                        data = None
                        if PIPE['watchdog'].poll(server.TIMEOUT - 2):
                            data = PIPE['watchdog'].recv()
                self.log.debug('send data: %s', data)
                if no_response is False:
                    self.send_data(data)
        except Exception as e:
            self.log.error(e, exc_info=True)
        if conf.IN_THREAD == True:
            try:
                LOCK.release()
            except:
                pass
        return True


class LookHandler(server.EchoRequestHandler):

    def handle(self):
        global PIPE
        no_response = False
        # self.handle_timeout()
        try:
            data = self.get_data()
            if data != None and data is not False and data != self:
                self.log.debug('get data: %s', data)
                if data[0] == 'real_time_look':
                    data = None
                    count = DB.get('SAS_METER_IN_COUNT')
                    if count != None and count is not False:
                        player = DB.get('PLAYER')
                        if player:
                            count['player'] = player['name']
                        else:
                            count['player'] = player
                    data = count
                elif data[0] == 'chk_alife':
                    data = True
                else:
                    data = None
                self.log.debug('send data: %s', data)
                self.send_data(data)
        except Exception as e:
            self.log.error(e, exc_info=True)
        return True

def run_server(handler=Handler, **kwargs):  # @UndefinedVariable
    '''
    Стартита TCP сървър като демон.
    Използва _tcp.EchoRequestHandler
    :param port:  Порт на лоцалния TCP сървър. Взима се от conf
    :param args: Ne se podawat argumenti
    :return: Не връща резултат. Стартира безкраен демон.
    '''
    if 'crypt' in kwargs:
        server.CRYPT = kwargs['crypt']

    if 'use_json' in kwargs:
        server.SERVER_USE_JSON = kwargs['use_json']

    if 'timeout' in kwargs:
        server.TIMEOUT = kwargs['timeout']

    if 'buffer' in kwargs:
        server.BUFFER = kwargs['buffer']

    if 'in_thread' in kwargs:
        server.SERVER_IN_THREADING = kwargs['in_thread']

    if 'port' in kwargs:
        server.PORT = kwargs['port']

    if 'ip' in kwargs:
        server.IP = kwargs['ip']

    address = (server.IP, server.PORT)  # let the kernel give us a port


    if server.SERVER_IN_THREADING is True:
        my_server = server.ThreadedServer(address, handler)
    else:
        my_server = server.SocketServer.UDPServer(address, handler)
    if 'logging' in kwargs:
        handler.log = kwargs['logging']
    else:
        handler.log = server.LOG_SERVER
    if 'rsa' in kwargs:
        handler.RSA = kwargs['rsa']
    else:
        handler.RSA = server.RSA
    handler.log.info('SERVER PROC STARTING!')
    handler.log.info('BIND: %s', address)
    handler.log.info('IN THREAD: %s', server.SERVER_IN_THREADING)
    handler.log.info('CRYPT: %s', server.CRYPT)
    handler.log.info('RSA: %s', handler.RSA)
    handler.log.info('BUFFER: %s', server.BUFFER)

    # my_server._handle_request_noblock()
    my_server.allow_reuse_address = True
    my_server.allow_reuse = True
    # server._handle_request_noblock = True
    my_server.timeout = server.TIMEOUT
    handler.log.info('start server')
    # t = threading.Thread(target=my_server.serve_forever)
    # t.start()
    my_server.serve_forever()

def run_server_look(handler=LookHandler, **kwargs):  # @UndefinedVariable
    '''
    Стартита TCP сървър като демон.
    Използва _tcp.EchoRequestHandler
    :param port:  Порт на лоцалния TCP сървър. Взима се от conf
    :param args: Ne se podawat argumenti
    :return: Не връща резултат. Стартира безкраен демон.
    '''
    if 'crypt' in kwargs:
        server.CRYPT = kwargs['crypt']

    if 'use_json' in kwargs:
        server.SERVER_USE_JSON = kwargs['use_json']

    if 'timeout' in kwargs:
        server.TIMEOUT = kwargs['timeout']

    if 'buffer' in kwargs:
        server.BUFFER = kwargs['buffer']

    if 'in_thread' in kwargs:
        server.SERVER_IN_THREADING = kwargs['in_thread']

    if 'port' in kwargs:
        server.PORT = kwargs['port']

    if 'ip' in kwargs:
        server.IP = kwargs['ip']

    address = (server.IP, server.PORT)  # let the kernel give us a port


    if server.SERVER_IN_THREADING is True:
        my_server = server.ThreadedServer(address, handler)
    else:
        my_server = server.SocketServer.UDPServer(address, handler)
    if 'logging' in kwargs:
        handler.log = kwargs['logging']
    else:
        handler.log = server.LOG_SERVER
    if 'rsa' in kwargs:
        handler.RSA = kwargs['rsa']
    else:
        handler.RSA = server.RSA
    handler.log.info('SERVER PROC STARTING!')
    handler.log.info('BIND: %s', address)
    handler.log.info('IN THREAD: %s', server.SERVER_IN_THREADING)
    handler.log.info('CRYPT: %s', server.CRYPT)
    handler.log.info('RSA: %s', handler.RSA)
    handler.log.info('BUFFER: %s', server.BUFFER)

    # my_server._handle_request_noblock()
    my_server.allow_reuse_address = True
    my_server.allow_reuse = True
    # server._handle_request_noblock = True
    my_server.timeout = server.TIMEOUT
    handler.log.info('start server')
    # t = threading.Thread(target=my_server.serve_forever)
    # t.start()
    my_server.serve_forever()