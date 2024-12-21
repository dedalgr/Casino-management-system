'''
Created on 19.02.2019

@author: dedal
'''
import socket
import sys
import os
import json
import logging
from multiprocessing import log_to_stderr

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',  
 )
LOG = log_to_stderr()
LOG.setLevel(logging.DEBUG)

class SocetExist(Exception):
    pass

class UnixSocket():
    def __init__(self, address='/tmp/colibri.sock', tcp_buffer=4096):
        self.address = address
        self.buffer = tcp_buffer
        self.log = LOG
        try:
            os.unlink(self.address)
        except OSError as e:
            if os.path.exists(self.address):
                self.log.critical(e, exc_info=True)
                raise SocetExist(e)
         
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.bind(self.address)
        self.sock.listen(1)
    
    def run(self):
        while True:
            connection, client_address = self.sock.accept()
            try:
                while True:
                    data = connection.recv(self.buffer)
                    if data:
                        data = json.loads(data)
                        data = True
                        connection.sendall(json.dumps(data))
                    else:
                        break
            except Exception as e:
                self.log.critical(e, exc_info=True)
            finally:
                connection.close()