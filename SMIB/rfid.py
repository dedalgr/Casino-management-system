# -*- coding:utf-8 -*-
'''
Created on 19.02.2019

@author: dedal
'''
from libs import rfid
from multiprocessing import Process
import log
import time  # @UnusedImport
import serial.tools.list_ports
import os
import sys
from subprocess import Popen, PIPE
import fcntl

class Rfid_RC522(Process):
    def __init__(self, **kwargs):
        Process.__init__(self, name='RFID')
        self.log = log.get_log(log.LOG_CHANEL_LEVEL['rfid'])
        self.db = kwargs['db']
        self.conf = kwargs['conf']
        # realise = os.popen('lsb_release -sr').read()
        # if '10' in realise:
        self.port = '/dev/spidev1.0'
        # else:
        #     self.port = '/dev/spidev1.0'
        self.scan_time = self.conf.get('RFID', 'scan_time', 'int')
        self.timeout = self.scan_time*0.001
        self.rfid = rfid.RFID_RC522()
        self.id = False
        self.pipe = kwargs['pipe']
        self.work_mod = self.db.get('WORKING_MODULE')
        self.multi_key = self.conf.get('KEYSYSTEM', 'multi_key', 'bool')
        self.all_bonus = self.db.get('BONUSCART')
        # self.open()
        # self.is_open = self.isOpen()
        self.send_to_keysystem_response = False
        self.bonus_cart_response = False

    def send_to_keysystem(self):
        # self.log.debug('send to keysystem: mod %s: ' % (self.multi_key))
        if self.multi_key is False:
            self.all_keys = self.db.get('KEYSYSTEM')
        else:
            self.all_keys = self.db.get('MULTI_KEYSYSTEM')
        if self.multi_key is False:
            if self.id == self.all_keys['credit_id']:
                self.pipe['keysystem'].send(1)
                return True
            elif self.id == self.all_keys['report_id']:
                self.pipe['keysystem'].send(2)
                return True
        else:
            if self.id in self.all_keys['credit_id']:
                self.pipe['keysystem'].send(1)
                return True
            elif self.id in self.all_keys['report_id']:
                self.pipe['keysystem'].send(2)
                return True
        return False

    def send_to_bonus(self):
        self.all_bonus = self.db.get('BONUSCART')
        # self.log.debug('send to bonus: %s', self.id)
        if self.id in self.all_bonus:
            self.pipe['bonus'].send(self.id)
            return True
        return False

    def run(self):
        send_to_keysystem = False
        bonus_cart = False
        while True:
            try:
                self.work_mod = self.db.get('WORKING_MODULE')
                # for i in range(2):
                send_to_keysystem = False
                bonus_cart = False
                self.id = self.rfid.get_id()
                # if self.id is not False:
                #     break
                # self.id = self.rfid.get_id()
                self.log.debug('RFID ID: %s', self.id)
                if self.id is not False:
                    if self.work_mod['keysystem'] is True:
                        send_to_keysystem = self.send_to_keysystem()
                    else:
                        send_to_keysystem = False
                    if self.work_mod['bonus_cart'] is True and send_to_keysystem is False:
                        bonus_cart = self.send_to_bonus()
                    else:
                        bonus_cart = False
                    self.log.info('KEYSYSTEM: %s BONUS: %s' % (send_to_keysystem, bonus_cart))
                    if self.work_mod['client_cart'] is True and send_to_keysystem is False and bonus_cart is False:
                        self.pipe['client'].send(self.id)
                else:
                    time.sleep(self.timeout)
                    send_to_keysystem = False
                    bonus_cart = False
                    self.id = False
            except Exception as e:
                send_to_keysystem = False
                bonus_cart = False
                self.id = False
                # time.sleep(0.5)
                self.log.critical(e, exc_info=True)
            # time.sleep(0.05)

class Rfid(Process):
    def __init__(self, **kwargs):
        Process.__init__(self, name='RFID')
        self.log = log.get_log(log.LOG_CHANEL_LEVEL['rfid'])
        self.db = kwargs['db']
        self.conf = kwargs['conf']
        self.port = '/dev/rfid'
        # scan_time = self.conf.get('RFID', 'scan_time', 'str')
        self.baudrate = self.conf.get('RFID', 'speed', 'int')
        self.timeout=self.conf.get('RFID', 'rfid_timeout', 'float')
        try:
            self.rfid = rfid.RFID(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
        except:
            self.rfid = None
        self.id = False
        self.pipe = kwargs['pipe']
        self.work_mod = self.db.get('WORKING_MODULE')
        self.multi_key = self.conf.get('KEYSYSTEM', 'multi_key', 'bool')
        self.all_bonus = self.db.get('BONUSCART')
        # self.open()
        # self.is_open = self.isOpen()
        self.send_to_keysystem_response = False
        self.bonus_cart_response = False
        self.usbdevfs_reset= 21780

    def reset_reader(self):
        try:
            self.log.error("resetting rfid driver: Olimex")
            lsusb_out = os.popen("lsusb | grep -i Olimex").read().split()
            bus = lsusb_out[1]
            # print lsusb_out
            device = lsusb_out[3][:-1]
            f = open("sudo /dev/bus/usb/%s/%s" % (bus, device), 'w', os.O_WRONLY)
            fcntl.ioctl(f, self.usbdevfs_reset, 0)
            return True
        except IndexError as e:
            self.log.warning(e, exc_info=True)
            return False
        except Exception as e:
            self.log.critical(e, exc_info=True)
            return False

    def send_to_keysystem(self):
        # self.log.debug('send to keysystem: mod %s: ' % (self.multi_key))
        if self.multi_key is False:
            self.all_keys = self.db.get('KEYSYSTEM')
        else:
            self.all_keys = self.db.get('MULTI_KEYSYSTEM')
        if self.multi_key is False:
            if self.id == self.all_keys['credit_id']:
                self.pipe['keysystem'].send(1)
                return True
            elif self.id == self.all_keys['report_id']:
                self.pipe['keysystem'].send(2)
                return True
        else:
            if self.id in self.all_keys['credit_id']:
                self.pipe['keysystem'].send(1)
                return True
            elif self.id in self.all_keys['report_id']:
                self.pipe['keysystem'].send(2)
                return True
        return False

    def chk_for_port(self):
        ports = serial.tools.list_ports.comports()
        tmp = []
        try:
            for i in ports:
                tmp.append(i[0])
        except Exception as e:
            self.log.critical(e, exc_info=True)
            raise e
        if '/dev/ttyACM0' in tmp:
            port = '/dev/ttyACM0'
            baudrate = self.conf.get('RFID', 'speed', 'int')
            timeout = self.conf.get('RFID', 'rfid_timeout', 'float')
            self.rfid = rfid.RFID(port=port, baudrate=baudrate, timeout=timeout)
            # self.open()
            return True
        elif '/dev/ttyACM1' in tmp:
            port = '/dev/ttyACM1'
            baudrate = self.conf.get('RFID', 'speed', 'int')
            timeout = self.conf.get('RFID', 'rfid_timeout', 'float')
            self.rfid = rfid.RFID(port=port, baudrate=baudrate, timeout=timeout)
            # self.open()
            return True
        elif '/dev/ttyACM2' in tmp:
            port = '/dev/ttyACM2'
            baudrate = self.conf.get('RFID', 'speed', 'int')
            timeout = self.conf.get('RFID', 'rfid_timeout', 'float')
            self.rfid = rfid.RFID(port=port, baudrate=baudrate, timeout=timeout)
            # self.open()
            return True
        elif '/dev/ttyACM3' in tmp:
            port = '/dev/ttyACM3'
            baudrate = self.conf.get('RFID', 'speed', 'int')
            timeout = self.conf.get('RFID', 'rfid_timeout', 'float')
            self.rfid = rfid.RFID(port=port, baudrate=baudrate, timeout=timeout)
            # self.open()
            return True
        else:
            self.log.warning('no rfid port')
        return False

    def send_to_bonus(self):
        self.all_bonus = self.db.get('BONUSCART')
        # self.log.debug('send to bonus: %s', self.id)
        if self.id in self.all_bonus:
            self.pipe['bonus'].send(self.id)
            return True
        return False

    def run(self):
        send_to_keysystem = False
        bonus_cart = False
        # scan_time_conf = False
        # try:
        #     if self.rfid.isOpen() is False:
        #         self.rfid.open()
        #
        # except rfid.RFIDOpenError as e:
        #
        # except Exception as e:
        #     self.log.error(e, exc_info=True)
        while True:
            try:
                if self.rfid == None:
                    self.rfid = rfid.RFID(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
                if self.rfid.isOpen() is False:
                    self.rfid.open()
                    # if self.isOpen() is False:
                    #     self.log.warning('rfid port not open')
                    #     if self.chk_for_port() is False:
                    #         self.log.error('rfid port try to reload')
                    #         try:
                    #             self.reset_reader()
                    #             os.system('sudo udevadm trigger')
                    #             time.sleep(10)
                    #         except Exception as e:
                    #             self.log.critical(e, exc_info=True)
                    #     else:
                    #         time.sleep(2)
                    #         self.open()
                    send_to_keysystem = False
                    bonus_cart = False
                    self.id = False
                else:
                    # if scan_time_conf is False:
                    #     self.rfid.scan_time(self.conf.get('RFID', 'scan_time', 'int'))
                    #     scan_time_conf = True
                    self.work_mod = self.db.get('WORKING_MODULE')
                    send_to_keysystem = False
                    bonus_cart = False
                    self.id = self.rfid.get_id()
                        # if self.id != False and self.id != None:
                        #     break
                    self.log.debug('RFID ID: %s', self.id)
                    if self.id is not False:
                        if self.work_mod['keysystem'] is True:
                            send_to_keysystem = self.send_to_keysystem()
                        else:
                            send_to_keysystem = False
                        if self.work_mod['bonus_cart'] is True and send_to_keysystem is False:
                            bonus_cart = self.send_to_bonus()
                        else:
                            bonus_cart = False
                        self.log.info('KEYSYSTEM: %s BONUS: %s' % (send_to_keysystem, bonus_cart))
                        if self.work_mod['client_cart'] is True and send_to_keysystem is False and bonus_cart is False:
                            self.pipe['client'].send(self.id)
                    else:
                        send_to_keysystem = False
                        bonus_cart = False
                        self.id = False
            except rfid.RFIDOpenError as e:
                self.log.error(e, exc_info=True)
                bonus_cart = False
                send_to_keysystem = False
                self.id = False
                try:
                    self.rfid.close()
                except Exception as e:
                    self.log.warning(e, exc_info=True)
                time.sleep(1)
                # try:
                #     if self.chk_for_port() is False:
                #         self.log.error('rfid port try to reload')
                #         # try:
                #         #     self.reset_reader()
                #         #     os.system('sudo udevadm trigger')
                #         #     time.sleep(10)
                #         # except Exception as e:
                #         #     self.log.critical(e, exc_info=True)
                # except Exception as e:
                #     pass
                # try:
                #     self.chk_for_port()
                # except Exception as e:
                #     self.log.critical(e, exc_info=True)
            except rfid.RFIDReadError as e:
                self.log.warning(e, exc_info=True)
                bonus_cart = False
                send_to_keysystem = False
                self.id = False
                # try:
                #     self.rfid.close()
                # except Exception as e:
                #     self.log.critical(e, exc_info=True)
                # time.sleep(2)
            except Exception as e:
                self.log.critical(e, exc_info=True)
                bonus_cart = False
                send_to_keysystem = False
                self.id = False
                try:
                    self.rfid.close()
                except Exception as e:
                    self.log.error(e, exc_info=True)
                time.sleep(0.5)
