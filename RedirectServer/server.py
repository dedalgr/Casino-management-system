'''
Created on 12.03.2019

@author: dedal
'''
from libs.sock.udp_socket import server as server
from libs.sock.tcp_socket import server as tcp_server
from multiprocessing import Pipe
import conf
import client
import time
import event
import subprocess
# import chk_proc
EVENT = None
# EVENT2 = None
# Q = None
# Q2 = None
import threading
LOCK = threading.Lock()
LOCK2 = threading.Lock()
SERVER_SEND, SERVER_RESPONSE = Pipe()
SERVER2_SEND, SERVER2_RESPONSE = Pipe()

class SMIBHandler(server.EchoRequestHandler):
    def handle(self):
        no_response = False
        response = None
        try:
            # self.handle_timeout()
            if conf.IN_THREAD == True:
                LOCK.acquire()
            data = self.get_data()
            if data != None and data != False and data != self:
                if 'no_response' in data[1]:
                    no_response = data[1]['no_response']
                self.log.info('%s %s' % (self.client_address, str(data)))
                if data[0] in EVENT.event:
                    data.append(time.time())
                    while SERVER_SEND.poll() is True:
                        SERVER_SEND.recv()

                    SERVER_SEND.send(data)
                    if SERVER_SEND.poll(conf.TIMEOUT_2-5) is True:
                        response = SERVER_SEND.recv()
                        if response == None:
                            pass
                        elif response[1] == data:
                            response = response[0]
                        else:
                            response = None
                    else:
                        response = None
        except Exception as e:
            self.log.critical(e, exc_info=True)
            self.log.error('IP %s', self.client_address)
            response = None
        self.log.info('i send data 40593: %s', response)
        if no_response == False and response is not None:
            try:
                # time.sleep(0.2)
                self.send_data(response)
            except Exception as e:
                self.log.error('Try to send data: %s', response)
                self.log.error(e, exc_info=True)
        if conf.IN_THREAD == True:
            try:
                LOCK.release()
            except:
                pass
        return True

class UDPHandler(server.EchoRequestHandler):
    def handle(self):
        no_response = False
        response = None
        lock = False
        try:
            # self.handle_timeout()

            data = self.get_data()
            if data != None and data != False and data != self:
                if 'no_response' in data[1]:
                    no_response = data[1]['no_response']
                if data[0] == 'db_iptables':
                    pass
                elif data[0] == 'server_alive':
                    pass
                elif data[0] == 'get_tz':
                    pass
                elif data[0] == 'get_all_user':
                    pass
                elif data[0] == 'set_pos':
                    pass
                else:
                    if conf.IPTASBLES == True:
                        if self.client_address[0] not in conf.OPEN_IP:
                            self.log.error('%s %s' % (self.client_address, str(data)))
                            return
                        elif conf.OPEN_IP[self.client_address[0]] != 'True':
                            self.log.error('%s %s' % (self.client_address, str(data)))
                            return
                self.log.info('%s %s' % (self.client_address, str(data)))
                if data[0] in EVENT.event:
                    if conf.IN_THREAD == True:
                        LOCK2.acquire()
                        lock = True
                    # if conf.IN_THREAD == True:
                    #     if LOCK.acquire(conf.TIMEOUT_2-4) == False:
                    #         self.send_data(None)
                    #         return
                    #     lock = True
                    if data[0] == 'db_iptables':
                        data[1]['unblock_ip'] = {self.client_address[0]: True}
                    data.append(time.time())
                    while SERVER2_SEND.poll() is True:
                        SERVER2_SEND.recv()
                    SERVER2_SEND.send(data)
                    # data = None
                    if SERVER2_SEND.poll(conf.TIMEOUT_2 - 5) is True:
                        response = SERVER2_SEND.recv()
                        if response == None:
                            pass
                        elif response[1] == data:
                            response = response[0]
                        else:
                            response = None
                    else:
                        response = None
                    if data[0] == 'db_iptables':
                        conf.OPEN_IP = conf.CONF.get('OPEN_IP')
                else:
                    # print data
                    if 'smib_ip' in data[1]:
                        ip = data[1]['smib_ip']
                        del data[1]['smib_ip']
                    # else:
                    #     lock = True
                    #     LOCK.acquire()
                    if 'smib_port' in data[1]:
                        port = data[1]['smib_port']
                        del data[1]['smib_port']
                    else:
                        port = conf.PORT
                    if 'smib_timeout' in data[1]:
                        timeout = data[1]['smib_timeout']
                        del data[1]['smib_timeout']
                    else:
                        timeout = conf.TIMEOUT_2
                        # ip = conf.IP
                    # try:
                    if data[0] != 'DOWN_ON' and data[0] != 'SET_DB_KEY' and data[0] != 'GET_DB_KEY':
                        if timeout > 0:
                            var = client.send(evt='chk_alife', ip=ip, port=port, timeout=4, log=self.log)
                            # if data[0] == 'ALIFE':
                            #     response = var
                            if var is not None:
                                response = client.send(evt=data[0], ip=ip, port=port, timeout=timeout - 4,
                                                       log=self.log, **data[1])
                            else:
                                response = None
                        else:
                            response = client.send(evt=data[0], ip=ip, port=port, timeout=timeout,
                                                   log=self.log, **data[1])
                            no_response = True
                    elif data[0] == 'DOWN_ON' or data[0] == b'DOWN_ON':
                        response = client.send(evt=data[0], ip=ip, port=port, timeout=40,
                                               log=self.log, **data[1])
                        if response == None:
                            response = 'CHECK'
                    else:
                        if timeout > 0:
                            response = client.send(evt=data[0], ip=ip, port=port, timeout=timeout - 4,
                                                   log=self.log, **data[1])
                        else:
                            client.send(evt=data[0], ip=ip, port=port, timeout=timeout,
                                        log=self.log, **data[1])
                            no_response = True
                    # except Exception as e:
                    #     self.log.critical(e, exc_info=True)
                    #     self.log.critical('%s', response)
                    #     data = None
        except Exception as e:
            self.log.critical(e, exc_info=True)
            self.log.error('IP %s', self.client_address)
            response = None
        self.log.info('i send response 30593 UDP: %s', response)
        if no_response == False:
            try:
                # time.sleep(0.2)
                self.send_data(response)
            except Exception as e:
                self.log.error('Try to send response: %s', response)
                self.log.error(e, exc_info=True)
        if conf.IN_THREAD == True and lock is True:
            try:
                LOCK2.release()
            except:
                pass
        return True
        # self.request.close()
        # if lock == True:
        #     LOCK.release()

class TCPHandler(tcp_server.EchoRequestHandler):
    def handle(self):
        self.request.settimeout(conf.TIMEOUT_2)
        no_response = False
        response = None
        lock = False
        # self.log.error('%s', threading.current_thread())
        try:
            # self.handle_timeout()
            data = self.get_data()
            if data != None and data != False and data != self:
                if 'no_response' in data[1]:
                    no_response = data[1]['no_response']
                if data[0] == 'db_iptables':
                    pass
                elif data[0] == 'server_alive':
                    pass
                elif data[0] == 'get_tz':
                    pass
                elif data[0] == 'get_all_user':
                    pass
                elif data[0] == 'set_pos':
                    pass
                else:
                    if conf.IPTASBLES == True:
                        if self.client_address[0] not in conf.OPEN_IP:
                            self.log.error('%s %s' % (self.client_address, str(data)))
                            return
                        elif conf.OPEN_IP[self.client_address[0]] != 'True':
                            self.log.error('%s %s' % (self.client_address, str(data)))
                            return
                self.log.info('%s %s' % (self.client_address, str(data)))
                if data[0] in EVENT.event:
                    if conf.IN_THREAD == True:
                        lock = True
                        LOCK2.acquire()
                    # if conf.IN_THREAD == True:
                    #     if LOCK.acquire(conf.TIMEOUT_2-4) == False:
                    #         self.send_data(None)
                    #         return
                    #     lock = True
                    if data[0] == 'db_iptables':
                        data[1]['unblock_ip'] = {self.client_address[0]: True}
                    data.append(time.time())
                    while SERVER2_SEND.poll() is True:
                        SERVER2_SEND.recv()
                    SERVER2_SEND.send(data)
                    # data = None
                    if SERVER2_SEND.poll(conf.TIMEOUT_2 - 5) is True:
                        response = SERVER2_SEND.recv()
                        if response == None:
                            pass
                        elif response[1] == data:
                            response = response[0]
                        else:
                            response = None
                    else:
                        response = None
                    if data[0] == 'db_iptables':
                        conf.OPEN_IP = conf.CONF.get('OPEN_IP')
                else:
                    # print data
                    if 'smib_ip' in data[1]:
                        ip = data[1]['smib_ip']
                        del data[1]['smib_ip']
                    # else:
                    #     lock = True
                    #     LOCK.acquire()
                    if 'smib_port' in data[1]:
                        port = data[1]['smib_port']
                        del data[1]['smib_port']
                    else:
                        port = conf.PORT
                    if 'smib_timeout' in data[1]:
                        timeout = data[1]['smib_timeout']
                        del data[1]['smib_timeout']
                    else:
                        timeout = conf.TIMEOUT_2
                        # ip = conf.IP
                    # try:
                    if data[0] != 'DOWN_ON' and data[0] != 'SET_DB_KEY' and data[0] != 'GET_DB_KEY':
                        if timeout > 0:
                            # cmd = 'sudo ping -c 1 %s' % (ip)
                            # var = subprocess.call(cmd.split())
                            var = client.send(evt='chk_alife', ip=ip, port=port, timeout=4, log=self.log)
                            # if data[0] == 'ALIFE':
                            #     response = var
                            if var is not None:
                                response = client.send(evt=data[0], ip=ip, port=port, timeout=timeout - 4,
                                                       log=self.log, **data[1])
                            else:
                                response = None
                        else:
                            client.send(evt=data[0], ip=ip, port=port, timeout=timeout,
                                                   log=self.log, **data[1])
                            no_response = True
                    else:
                        if timeout > 0:
                            response = client.send(evt=data[0], ip=ip, port=port, timeout=timeout - 4,
                                                   log=self.log, **data[1])
                        else:
                            client.send(evt=data[0], ip=ip, port=port, timeout=timeout,
                                            log=self.log, **data[1])
                            no_response = True
                    # except Exception as e:
                    #     self.log.critical(e, exc_info=True)
                    #     self.log.critical('%s', response)
                    #     data = None
        except Exception as e:
            self.log.critical(e, exc_info=True)
            self.log.error('IP %s', self.client_address)
            response = None
        self.log.info('i send response 30593 TCP: %s', response)
        if no_response == False:
            try:
                # time.sleep(0.2)
                self.send_data(response)
            except Exception as e:
                self.log.error('Try to send response: %s', response)
                self.log.error(e, exc_info=True)

        if conf.IN_THREAD == True and lock is True:
            try:
                LOCK2.release()
            except:
                pass
        self.request.close()
        return True
        # self.request.close()
        # if lock == True:
        #     LOCK.release()

if __name__ == '__main__':
    pass