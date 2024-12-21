# -*- coding:utf-8 -*-
'''
Created on 12.10.2018 г.

@author: dedal
'''
import sys
import socket
import os
import threading
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
)

FILE_TRANSFER_SERVER_LOG = logging.getLogger('FILE TRANSFER SERVER')
FILE_TRANSFER_SERVER_LOG.setLevel(logging.DEBUG)


class Server(threading.Thread):

    def __init__(self, host, port=5565, folder_for_file='', listen=10, log=FILE_TRANSFER_SERVER_LOG):
        if folder_for_file[:-1] != '/':
            folder_for_file = folder_for_file + '/'
        self.folder_for_file = folder_for_file
        self.log = log
        self._abort = 0
        self.skServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.skServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.skServer.bind((host, port))
        self.skServer.listen(listen)
        threading.Thread.__init__(self)
        self.log.info("Port: %s", port)
        self.log.info("Host: %s", host)
        self.log.info("Listen: %s", listen)
        self.log.info("Folder to list file: %s", folder_for_file)

    def abort(self):
        self._abort = 1

    def get_file(self):
        self.log.info("Waithing request!")
        while True:
            try:
                if self._abort:
                    break
                Content, Address = self.skServer.accept()
                self.log.info("Request from: %s", Address)
                sFileName = Content.recv(1024)
                bFileFound = 0
                for file_find in os.listdir(self.folder_for_file):
                    if file_find == sFileName:
                        bFileFound = 1
                        break
                if bFileFound == 0:
                    self.log.error("File Not Found: %s", sFileName)
                    Content.send('1')

                else:
                    self.log.info("File Found: %s", sFileName)
                    fUploadFile = open(self.folder_for_file + sFileName, "rb")
                    sRead = fUploadFile.read(1024)
                    while sRead:
                        Content.send(sRead)
                        sRead = fUploadFile.read(1024)
                    self.log.info("Sending Completed")
                    #                     print
                    break
            except Exception as e:
                Content.send('1')
                self.log.error(e, exc_info=True)

    def run(self):
        while True:
            self.get_file()
