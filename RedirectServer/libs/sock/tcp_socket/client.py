# -*- coding:utf-8 -*-
'''
Created on 7.09.2018 г.

@author: dedal
'''
import socket
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
)

BUFFER = 1024
TIMEOUT = 10
CLINET_USE_JSON = True
LOG_CLIENT = logging.getLogger('UDP CLIENT')
LOG_CLIENT.setLevel(logging.DEBUG)


class BadSignature(Exception):
    pass


# if CLINET_USE_JSON == False:
try:
    import _pickle as pickle  # @UnusedImport
except ImportError:
    import pickle  # @Reimport @UnusedImport

import json  # @Reimport @UnusedImport


class Client():

    def __init__(self, ip, port, timeout=TIMEOUT, udp_buffer=BUFFER, log=LOG_CLIENT, use_json=CLINET_USE_JSON,
                 crypt=None, rsa=False):
        self.udp_buffer = udp_buffer
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(timeout)  # @UndefinedVariable
        self.ip = ip
        self.port = port
        self.crypt = crypt
        self.rsa = rsa
        self.log = log
        self.use_json = use_json
        self.log.debug('SEND TO: %s', str((ip, port)))
        self.s.connect((ip, port))

    def sig(self, msg):
        return self.rsa.get_signature(msg)

    def verify(self, msg):
        data = json.loads(msg)
        if self.rsa.verify(data[0], data[1]) is True:
            return data[0]
        else:
            raise BadSignature(data)

    def crypt_encrypt(self, evt):

        if self.use_json == False:
            data = pickle.dumps(evt)
        else:
            data = json.dumps(evt)
        self.log.debug('SEND DATA: %s', data)
        if self.crypt != None and self.rsa is False:
            data = self.crypt.encrypt(data)
        elif self.crypt != None and self.rsa is not False:
            data = json.dumps([data, self.sig(data)])
            data = self.crypt.encrypt(data)
        return data

    def crypt_decrypt(self, data):
        if self.crypt != None and self.rsa == False:
            data = self.crypt.decrypt(data)
        elif self.crypt != None and self.rsa is not False:
            data = self.crypt.decrypt(data)
            data = self.verify(data)
        if self.use_json == False:
            data = pickle.loads(data)
        else:
            data = json.loads(data)
        return data

    def sendto(self, evt):
        data = self.crypt_encrypt(evt) + b'EXIT'
        # data = self.crypt_encrypt(evt)
        self.s.sendall(data)
        # self.s.send()
        return True

    def getfrom(self):
        try:
            self.time = time.time()
            data = self.s.recv(self.udp_buffer)
            while 1:
                if data[-4:] == b'EXIT':
                    break
                var = self.s.recv(self.udp_buffer)
                data += var
                if time.time() > self.time + (TIMEOUT / 2):
                    raise socket.timeout(data)

                # if var == '':
                #     raise socket.timeout
            data = data.replace(b'EXIT', b'')
            data = self.crypt_decrypt(data)
            return data
        # try:
        #     self.log.debug('GET DATA: %s', data)
        #     return self.crypt_decrypt(data)
        except socket.error as e:
            self.log.error(e, exc_info=True)
        except Exception as e:
            self.log.error(e, exc_info=True)
        return None

    def send(self, evt, **kwargs):
        self.sendto(evt=[evt, kwargs])
        response = self.getfrom()
        return response

    def close(self):
        self.s.close()
        return True


def send(evt, ip, port, timeout=TIMEOUT, udp_buffer=BUFFER, crypt=None, rsa=False, *args, **kwargs):
    '''
    Изпраща информация към TCP сървър.
    _tcp.Client
    :param evt: Име на функция на отдалечения сървър.
    :param kwargs: Аргументи ако има
    :return: Връща отговора на функцията. Ако е неуспешно None
    '''

    try:
        client = Client(ip=ip, port=port, timeout=timeout, udp_buffer=udp_buffer, crypt=crypt, rsa=rsa)
        response = client.send(evt, **kwargs)
        client.close()
    except Exception as e:
        LOG_CLIENT.error(e, exc_info=True)
        return None
    #     finally:
    #         client.close()
    return response


if __name__ == '__main__':
    count = 1
    err = 0
    print(time.time())
    for i in range(100):
        print(send('test', ip='127.0.0.1', port=2522))
    print(time.time())
#         print a
#         time.sleep(1)