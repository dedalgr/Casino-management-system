# -*- coding:utf-8 -*-
'''
Created on 27.04.2018 г.

@author: dedal
'''

import serial
import time
import os
from . import mfrc522

class NoSerial(Exception):
    pass

class BadSerialVersion(Exception):
    pass

class RFIDReadError(serial.SerialException):
    pass

class RFIDNoUSBReset(Exception):
    pass

class RFIDOpenError(Exception):
    pass

class RFIDCommandError(Exception):
    pass

class RFIDWriteError(Exception):
    pass

class RFIDFlushError(Exception):
    pass

class RFID_RC522():
    def __init__(self, scan_time=0.2, **kwargs):
        self.scan_time = scan_time
        self.rfid = mfrc522.SimpleMFRC522()

    def get_id(self):
        data = None
        for i in range(3):
            data = self.rfid.read_id()
            if data:
                break
            time.sleep(self.scan_time)
        if data:
            return data
        return False

    def get_block(self, n=4):
        data = 'NONE'
        for i in range(3):
            data = os.popen('%s -d %s -r %s -n 5 -y %s' % (self.app_name, self.port, n, self.scan_time)).read()
            data = data[:-1]
            data = data.replace(' ', '')
            data = data.upper()
            if data != 'NONE':
                try:
                    if len(data) != 16:
                        raise ValueError(data)
                    int(data, 16)
                except Exception as e:
                    pass
                else:
                    return data
        if data == 'NONE':
            return False
        raise RFIDReadError(data)

    def write(self, n=4, data=None):
        data = data.upper()
        if data == None:
            raise RFIDWriteError
        new_data = os.popen('%s -d %s -w %s --data "%s"' % (self.app_name, self.port, n, data)).read()
        new_data = new_data[:-1]
        new_data = new_data.replace(' ', '')
        new_data = new_data.upper()
        try:
            int(new_data, 16)
        except Exception as e:
            raise e
        if new_data != data:
            raise RFIDWriteError(new_data)
        return True


class RFID():
    def __init__(self, port, baudrate=115200, timeout=False):

        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        if timeout != False:
            self.ser.timeout = timeout
            #         self.usb_reset_tag = usb_reset_tag

    def open(self):
        try:
            self.ser.open()
        except serial.serialutil.SerialException as e:
            raise RFIDOpenError(e)

    def read(self, size):
        data = False
        try:
            self.flushInput()
            # self.flushOutput()
        except Exception as e:
            raise RFIDFlushError(e)
        # else:
        data = self.ser.read(size)
        return data

    def write(self, block, value):
        try:
            self.flushOutput()
        except Exception as e:
            raise RFIDWriteError(e)
        command = 'ew' + str(block) + ',' + str(value) + '\r'
        for i in range(5):  # @UnusedVariable
            self.ser.write(command.encode())
            self.read(40)
        return True

    def run_command(self, command):
        # self.ser.flushInput()
        try:
            # self.ser.flushInput()
            self.flushInput()
            self.flushOutput()
            command = command + '\r'
            # for i in range(5):  # @UnusedVariable
            self.ser.write(command.encode())
            # self.ser.write('\n')

        except Exception as e:
            raise RFIDCommandError(e)
        return self.read(20)

    def scan_time(self, times=500):
        for i in range(2):
            try:
                # self.ser.flushInput()
                # self.flushInput()
                # self.flushOutput()
                command = 'mt%s' % (times)
                # command = command + '\r'
                #             for i in range(5):  # @UnusedVariable
                data = self.run_command(command)
                data = data.decode()
                if data.split()[1] == 'OK':
                    return data.split()[1]
            except Exception as e:
                raise RFIDCommandError(e)

        return False

    def _read_block(self, from_block, to_block=None):
        if to_block == None:
            command = 'er' + str(from_block) + '\r'
        else:
            command = 'er' + str(from_block) + ',' + str(to_block) + '\r'
        # for i in range(5):  # @UnusedVariable
        self.run_command(command)
        self.read(20)
        return True

    def get_id(self):
        for i in range(2):
            data = self.read(12)
            if data:
                try:
                    if int(data[3:-1], 16) > 0:
                        return data[3:-1].decode()
                    else:
                        pass
                except ValueError as e:
                    pass
        return False


    def conf_block(self, block):
        if block != None:
            self._read_block(block)
            #         self.close()

    def get_block(self):
        data = self.read(79).decode()
        if not data[3:-1]:
            return False
        data = data[27:-5]
        var = ''
        for i in data:
            if i != '20':
                var = var + i
        return var

    def close(self):
        self.ser.close()

    def isOpen(self):
        return self.ser.isOpen()

    def flushInput(self):
        self.ser.flushInput()
        return True

    def flushOutput(self):
        self.ser.flushOutput()
        return True


if __name__ == '__main__':
    cart = RFID('/dev/ttyACM0', timeout=1 )
    cart.open()
    print (cart.scan_time(500))
    count = 1
    while True:
        print(cart.get_id(), count)
        count += 1
        # os.system('sudo udevadm trigger')
        # time.sleep(10)
