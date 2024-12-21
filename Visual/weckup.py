# -*- coding:utf-8 -*-
'''
Created on 03.05.2019

@author: dedal
'''
import time
from libs.sock.udp_socket import client
import config
import log

def wekup():
    while True:            
        try:
            my_client = client.Client(ip='127.0.0.1',
            port=config.SELF_PORT,
            timeout=2, 
            udp_buffer=config.UDP_BUFFER,
            crypt=config.CRYPT)
            data = my_client.send(True)
            # print data
            if data == True:
                break
        except Exception as e:
            time.sleep(1)
            log.stderr_logger.error(e, exc_info=True)
          


