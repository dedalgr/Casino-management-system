import logging
import serial
from serial.serialutil import SerialException
from xmodem import XMODEM
import time
logging.basicConfig(level=logging.DEBUG)

class UpdateRFID():
    def __init__(self, port='/dev/rfid', timeout=10, baudrate=19200):
        self.ser = serial.Serial(port, timeout=timeout, baudrate=baudrate)

    def is_open(self):
        return self.ser.isOpen()

    def open(self):
        if self.ser.isOpen() == False:
            self.ser.open()

    def close(self):
        self.ser.close()

    def flush(self):
        self.ser.flushInput()
        self.ser.flushOutput()

    def putc(self, data, timeout=1):
        return self.ser.write(data)

    def getc(self, size, timeout=1):
        return self.ser.read(size) or None

    def make_modem(self):
        self.modem = XMODEM(self.getc, self.putc)

    def load_image(self, name):
        self.file = open(name, 'rb')

    def read(self):
        self.ser.timeout = 1
        return self.ser.read(1)


    def update(self, img='MOD-RFID1356MIFARE-UPDATE-101.img'):
        self.open()
        self.make_modem()
        self.load_image(img)
        data = self.modem.send(self.file, quiet=True)
        self.close()
        self.file.close()
        return data

if __name__ == '__main__':
    data = input('img file (default:MOD-RFID1356MIFARE-UPDATE-101.img): ')
    if data == '':
        data = 'MOD-RFID1356MIFARE-UPDATE-101.img'
    while True:
        try:
            update = UpdateRFID(port='/dev/ttyACM0', timeout=0, baudrate=19200)
            break
        except SerialException:
            print('try to init port')
        except Exception as e:
            raise e
    while 1: 
        var = update.read()
        if var == b'C':
            break
    update.update(img=data)
    input('Press Enter to close!')
    # update.file.close()

