# -*- coding:utf-8 -*-
'''
Created on 27.01.2023 г.

@author: dedal
'''

import serial
import os
import re
if os.name == 'posix':
    import fcntl
# if not __package__:
#     import log
# else:
#     from . import log
import datetime

class OCROpenError(Exception):
    pass

class EGNExceptions(Exception):
    pass

def IsEGNValid(egn):
        try:
            int(egn)
            if len(egn) != 10:
                return False
            else:
                mounth = int(str('%s%s' % (egn[2:3], egn[3:4])))
                if mounth >=40:
                    mounth = mounth - 40
                    year = int('20' + egn[0:1] + egn[1:2])
                else:
                    year = int('19' + egn[0:1] + egn[1:2])
                day = int(egn[4:5] + egn[5:6])
                # my_sity = int(egn[6:7] + egn[7:8]+egn[8:9])
                tmp = []
                for i in egn:
                    tmp.append(int(i))
                egn = tmp
                my_date = datetime.datetime.now()
                if mounth > 12 or mounth < 0:
                    return False
                if year < my_date.year - 100:
                    return False
                if my_date.year - 18 < year:
                    return 'LITLE'
                elif my_date.year - 18 == year:
                    if my_date.month < mounth:
                        return 'LITLE'
                    elif my_date.month == mounth:
                        if my_date.day <= day:
                            return 'LITLE'
                coef = [2,4,8,5,10,9,7,3,6]
                sum = 0.0
                for i in range(0, len(egn)):
                    if i < 9:
                        sum += egn[i] * coef[i]
                sum = sum % 11
                sum = int(sum)
                if sum == 10:
                    sum = 0
                if sum != egn[9]:
                    return False
                # burt_date = '%s.%s.%s' % (day, mounth, year)
                return True
        except Exception as e:
            e.args += (egn,)
            raise e
            # log.stderr_logger.error(e, exc_info=True)
        return False
            
class DeskoOCR():
    def __init__(self, port, timeout=0.5, lock=False):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.timeout = timeout
        # self.timeout = timeout
        self.ser.parity = serial.PARITY_EVEN
        self.ser.bytesize = serial.SEVENBITS
        self.lock = lock

    def open(self):
        try:
            self.ser.open()
            if self.lock is True and os.name == 'posix':
                fcntl.flock(self.ser.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except serial.serialutil.SerialException as e:
            raise OCROpenError(e)

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

    def get_ocr_data(self):
        # self.ser.read(1)
        data = ''
        try:
            data = self.ser.readall().decode()
            # while True:
            #     tmp = self.ser.read(1).decode()
            #     # if tmp:
            #     #     self.ser.timeout = 0.1
            #     # a = tmp
            #     # if a.encode('hex') == '0d':
            #     #     tmp = '\n'
            #     if not tmp:
            #         break
            #     data += tmp
            # self.ser.timeout = self.timeout
            if data == '':
                return False

            tmp = {}
            data = re.sub(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\>\|\:\-])', r'', data)
            data = data.replace("\'", '')
            data = data.replace('\"', '')
            data = data.replace('\*', '')
            data = data.replace('\x02', '')
            data = data.replace('\\n', '')
            data = data.replace('\\r', '')
            data = data.replace('\\x', '')
            data = data.replace("\\", '')
            data = data.split('<')
            tmp['VALID'] = datetime.datetime.strptime(data[15][9:15], '%y%m%d')
            # tmp2 = data[15][-10:]
            # tmp2 = datetime.datetime.strptime(tmp2[0:-4], '%y%m%d')
            if tmp['VALID'].year < 2000:
                tmp['VALID'] = tmp['VALID'].replace(year=tmp['VALID'].year+100)
            if tmp['VALID'] < datetime.datetime.now():
                return 'EXPIRED'
            tmp['VALID'] = datetime.datetime.strftime(tmp['VALID'], '%d.%m.%Y')
            tmp['LK'] = data[0][6:-1]
            tmp['EGN'] = data[15][-10:]
            tmp['country_code'] = data[15][-13:-10]
            tmp['name'] = data[18]
            tmp['father_name'] = data[19]
            tmp['surname'] = data[16][2:]
            # for i in tmp:
            #     if '"' in tmp[i]:
            #         tmp[i] = tmp[i].replace('"', '')
            #     if "'" in tmp[i]:
            #         tmp[i] = tmp[i].replace("'", '')
            #     if not tmp[i]:
            #         return False
            #     if '\\' in tmp[i]:
            #         return False
            #     if '*' in tmp[i]:
            #         return False
            #     if '\\n' in tmp[i]:
            #         return False
            chk_egn = IsEGNValid(tmp['EGN'])
            if chk_egn is False:
                raise EGNExceptions(tmp['EGN'])
            elif chk_egn is True:
                pass
            else:
                return chk_egn
            return tmp
        except Exception as e:
            # print (data)
            # log.stderr_logger.critical(e, exc_info=True)
            e.args += (data,)
            raise e
        return False

class OCR():
    def __init__(self, port, timeout=0.5, lock=False):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.timeout = timeout
        self.lock = lock
        # self.timeout = timeout

    def open(self):
        try:
            self.ser.open()
            if self.lock is True and os.name == 'posix':
                fcntl.flock(self.ser.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except serial.serialutil.SerialException as e:
            raise OCROpenError(e)

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

    def get_ocr_data(self):
        # self.ser.read(1)
        data = ''
        try:
            data = self.ser.readall().decode()
            # while True:
            #     tmp = self.ser.read(1).decode()
            #     # if tmp:
            #     #     self.ser.timeout = 0.1
            #     # a = tmp
            #     # if a == '\x02':
            #     #     tmp = '\n'
            #     if tmp == '':
            #         break
            #     data += tmp
            # self.ser.timeout = self.timeout
        # self.ser.timeout = 10

            if data == '':
                return False
            data = re.sub(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\>\|\:\-])', r'', data)
            data = data.replace("\'", '')
            data = data.replace('\"', '')
            data = data.replace('\*', '')
            data = data.replace('\x02', '')
            data = data.replace('\\n', '')
            data = data.replace('\\r', '')
            data = data.replace('\\x', '')
            data = data.replace("\\", '')
            data = data.split('<')
            tmp = {}
            tmp['VALID'] = datetime.datetime.strptime(data[15][9:15], '%y%m%d')
            # tmp2 = data[15][-10:]
            # tmp2 = datetime.datetime.strptime(tmp2[0:-4], '%y%m%d')
            if tmp['VALID'].year < 2000:
                tmp['VALID'] = tmp['VALID'].replace(year=tmp['VALID'].year + 100)
            if tmp['VALID'] < datetime.datetime.now():
                return 'EXPIRED'
            tmp['VALID'] = datetime.datetime.strftime(tmp['VALID'], '%d.%m.%Y')
            tmp['LK'] = data[0][5:-1]
            tmp['EGN'] = data[15][-10:]
            tmp['country_code'] = data[15][-13:-10]
            tmp['name'] = data[18]
            tmp['father_name'] = data[19]
            tmp['surname'] = data[16][2:]
            # for i in tmp:
            #     if '"' in tmp[i]:
            #         tmp[i] = tmp[i].replace('"', '')
            #     if "'" in tmp[i]:
            #         tmp[i] = tmp[i].replace("'", '')
            #     if not tmp[i]:
            #         return False
            #     if '\\' in tmp[i]:
            #         return False
            #     if '*' in tmp[i]:
            #         return False
            #     if '\\n' in tmp[i]:
            #         return False
            chk_egn = IsEGNValid(tmp['EGN'])
            if chk_egn is False:
                raise EGNExceptions(tmp['EGN'])
            elif chk_egn is True:
                pass
            else:
                return chk_egn
            return tmp
        except Exception as e:
            # print (data)
            # log.stderr_logger.critical(e, exc_info=True)
            e.args += (data,)
            raise e
        return False

if __name__ == '__main__':
    cart = DeskoOCR('/dev/ttyUSB0')
    cart.open()
    count = 1
    while 1:
        print(cart.get_ocr_data())

