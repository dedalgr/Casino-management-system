# -*- coding:utf-8 -*-
'''
Created on 12.10.2018 г.

@author: dedal
'''

import sys
import socket
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
)

FILE_TRANSFER_CLIENT_LOG = logging.getLogger('FILE TRANSFER CLIENT')
FILE_TRANSFER_CLIENT_LOG.setLevel(logging.DEBUG)


def get_file(host, file_name, log, port=5565, write_in='/tmp/'):
    log.info('Try to get file: %s', file_name)
    log.info('Port: %s', port)
    log.info('Host: %s', host)
    skClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skClient.connect((host, port))
    while True:
        skClient.send(file_name)
        sData = skClient.recv(1024)
        fDownloadFile = open(write_in + file_name, "wb")
        if sData == '1':
            fDownloadFile.close()
            os.system('rm %s ' % (write_in + file_name))
            log.warning('Not found: %s', file_name)

            break
        while sData:
            fDownloadFile.write(sData)
            sData = skClient.recv(1024)
        log.info("Download Completed")
        break
    fDownloadFile.close()
    skClient.close()


if __name__ == '__main__':
    get_file('127.0.0.1', 5565, 'server.py', FILE_TRANSFER_CLIENT_LOG)