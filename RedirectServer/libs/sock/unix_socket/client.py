'''
Created on 19.02.2019

@author: dedal
'''
import socket
import sys
import json
import logging
from multiprocessing import log_to_stderr

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',  
 )
LOG = log_to_stderr()
LOG.setLevel(logging.DEBUG)

class UnixSocket(Exception):
    pass

class Client():
    
    def __init__(self, address='/tmp/colibri.sock', tcp_buffer=4096, log=LOG):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.address = address
        self.buffer = tcp_buffer
        self.log = log
    
    def connect(self):
        try:
            self.sock.connect(self.address)
        except socket.error as e:
            self.log.critical(e, exc_info=True)
            raise UnixSocket(e)
        
    def send(self, event, **kwargs):
        try:
            message = [event, kwargs]
            message = json.dumps(message)
            self.sock.sendall(message)
         
            amount_received = 0
            amount_expected = len(message)
            data = None
            while amount_received < amount_expected:
                data = self.sock.recv(self.buffer)
                amount_received += len(data)
        except Exception as e:
            self.log.critical(e, exc_info=True)
        finally:
            self.sock.close()
        return data