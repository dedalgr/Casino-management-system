#-*- coding:utf-8 -*-
import uuid
import conf  # @UnresolvedImport
import os
import crcmod
import time
import datetime
import random
import rtc  # @UnresolvedImport
import smbus
import exception  # @UnresolvedImport

def read_emmc_n():
    if conf.DEBUG == True:
        return 'ffffff'
    cmd = 'sudo udevadm info --query=all --name=%s | grep ID_SERIAL' % ('/dev/mmcblk0p1')
    data = os.popen(cmd).read()
    data = data.replace('E: ID_SERIAL=', '')
    return data[2:-1]

def read_db_n():
    if conf.DEBUG == True:
        return 'ffffff'
    cmd = 'sudo udevadm info --query=all --name=%s | grep ID_SERIAL' % ('/dev/mmcblk0p1')
    data = os.popen(cmd).read()
    data = data.replace('E: ID_SERIAL=', '')
    return data[:-1]

def crc(data, poly):
    crc32 = crcmod.Crc(poly, initCrc=0, xorOut=0xFFFFFFFFFFFFFFFF)
    crc32.update(data)
    return crc32.hexdigest()


def hw_uuid():
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, read_emmc_n()))

def mk_soft_id():
    return str(uuid.uuid4())

def chk_hw_uuid(machine_uuid):
    return machine_uuid == str(uuid.uuid5(uuid.NAMESPACE_DNS, read_emmc_n()))

def get_files(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):  # @UnusedVariable
        for filename in files:
            filepath = os.path.join(root, filename)
            if filepath[-3:] == '.db':
                pass
            elif filepath[-5:] == '.conf':
                pass
            elif filepath[-4:] == '.log':
                pass
            elif 'backup' in filepath:
                pass
            elif '.svn' in filepath:
                pass
            else:
                file_paths.append(filepath)
    return file_paths

def chk_crc(soft_crc, path=None):
    if path == None:
        path = conf.ROOT_PATH  
    files = get_files(path)
    math_crc = ''
    if conf.NOT_CHK_ON_START == True:
        return True
    for i in files:
        # if i[-3:] != '.db' and i[-5:] != '.conf' and i[-4:] != '.log':
        math_crc = math_crc + crc(open(i, 'rb').read(), conf.POLY)
    math_crc = crc(math_crc.encode('utf-8'), conf.POLY)
    if soft_crc == int(math_crc, 16):
        return True
    else:
        return False

def mk_crc(path=None, string=False):
    if path == None:
        path = os.getcwd()
    files = get_files(path)
    math_crc = ''
    for i in files:
        # if i[-3:] != '.db' and i[-5:] !='.conf' and i[-4:] != '.log':
        math_crc = math_crc + crc(open(i, 'rb').read(), conf.POLY)
    math_crc = crc(math_crc.encode('utf-8'), conf.POLY)
    if string==True:
        return math_crc
    return int(math_crc, 16)

def base_code(error):
    version = conf.VERSION
    version = version.replace('_', '')
    version = version.replace('.', '')
    code = uuid.UUID(fields=(
        int(time.time()),
        int(version),  
        random.randint(0, 10000),
        error,
        random.randint(0, 100),
        mk_crc() + int(read_db_n(), 16),
    ))
    return str(code)



def activate_code(code, base):
    new_date = code[0:8]
    activ_type = int(code[19:21], 16)

    if activ_type == 1:
        date = int(new_date, 16) - (conf.CONST/2)  
        new_date = datetime.datetime.fromtimestamp(date)
        new_date = time.mktime(new_date.timetuple())
    else:
        new_date = int(time.time()) - (conf.CONST/2)  
    global crc
    base_key_crc = int(crc(base.encode('utf-8'), conf.POLY)[0:4], 16)
    base_key_crc_1 = int(crc(base.encode('utf-8'), conf.POLY)[6:], 16)
    version = int(code[9:13], 16)
    base_crc = int(code[14:18], 16)
    base_crc1 = int(code[21:23], 16)
    my_id =  int(code[24:], 16) - mk_crc()
    soft_crc = (int(code[24:], 16) - my_id)
    main_version = conf.VERSION
    main_version = main_version.replace('_', '')
    main_version = main_version.replace('.', '')
    if my_id != int(read_db_n(), 16):
        return False, None
    elif soft_crc != mk_crc():
        return False, None
    elif version != int(main_version):
        return False, None
    elif base_key_crc != base_crc:
        return False, None
    elif base_key_crc_1 != base_crc1:
        return False, None
    else:
        if conf.DEBUG == False:
            try:
                rtc.Write_RTC(bus=conf.RTC_Bus, init_write=True)
            except:
                print('DATA NOT WRITE ON PC')
                pass
                # return False, None
        if activ_type == 1:
            return True, new_date
        else:
            return True, None


