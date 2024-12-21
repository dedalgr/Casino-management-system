#-*- coding:utf-8 -*-
'''
Created on 9.09.2018 г.

@author: dedal
'''
import smbus
import os
import time
import datetime
import pytz

RTC_Bus = 2
RTC_TIME_ZONE = 'Europe/Sofia'
RTC_BUG_FIX = False

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def bug_fix(date_now, last_write, go_one_day_up):
    variation = 0
    if last_write[0] == date_now.year and date_now.month <=2 and date_now.day <= 28 and last_write[1] <= 2 and last_write[2] <= 28:
        variation = 0
    elif last_write[0] == date_now.year and last_write[1] >= 2 and date_now.month > 2:
        variation = 0
    elif last_write[0] < date_now.year:
        for i in range(date_now.year - last_write[0]):
            if is_leap_year(last_write[0]+i) == False:
                variation += 1
        if last_write[1] > 2 and variation > 0 and is_leap_year(date_now.year) == False:
            variation -= 1
        elif date_now.day <=28 and date_now.month <= 2 and variation > 0 and is_leap_year(date_now.year) == False:
            variation -= 1
    if go_one_day_up == True and variation > 0:
        variation -= 1
    return date_now - datetime.timedelta(days=variation)

def BCDtoInt(bcd):
    "BDC -> INT"
    a = bcd & 0x0F
    b = bcd >> 4
    return b*10 + a


def InttoBCD(Int):
    "INT -> BDC"
    a = Int % 10;
    b = Int / 10;    
    return (b << 4) + a;

def Read_RTC(bus=RTC_Bus, zone=RTC_TIME_ZONE): 
    "Read the date from MOD-RTC"
    bus = smbus.SMBus(bus)
    buf = bus.read_i2c_block_data(0x51, 0x02, 7)
    buf[0] &= 0x7F;
    buf[1] &= 0x7F;
    buf[2] &= 0x3F;
    buf[3] &= 0x3F;
    buf[4] &= 0x07;
    buf[5] &= 0x1F;
    buf[6] &= 0xFF;
    if RTC_BUG_FIX == True:
        go_one_day_up = False
        if BCDtoInt(buf[5]) == 2 and BCDtoInt(buf[3]) == 29 and is_leap_year(BCDtoInt(buf[6])+1900) == False:
            buf[5] = InttoBCD(3)
            buf[3] = InttoBCD(1)
            go_one_day_up = True

    date_now = "%d-%d-%d %d:%d:%d" % (BCDtoInt(buf[6])+1900, BCDtoInt(buf[5]), BCDtoInt(buf[3]),
                                  BCDtoInt(buf[2]), BCDtoInt(buf[1]),
                                  BCDtoInt(buf[0]))
    if RTC_BUG_FIX == True:
        buf2 = bus.read_i2c_block_data(0x51, 0x09, 3)
        buf2[0] &= 0xFF;
        buf2[1] &= 0x1F;
        buf2[2] &= 0x3F;
        date_now = datetime.datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S')
        last_write = [BCDtoInt(buf2[0])+1900, BCDtoInt(buf2[1]), BCDtoInt(buf2[2])]
        date_now = bug_fix(date_now, last_write, go_one_day_up)
    else:
        try:
            date_now = datetime.datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S')
        except ValueError as e:
            print('found rtc bug use  -b 1 option')
            print(e)
            return False
    date_now = date_now.replace(tzinfo=pytz.UTC)
    date_now = date_now.astimezone(pytz.timezone(zone))
    return datetime.datetime.strftime(date_now, '%Y-%m-%d %H:%M:%S')
    
#     else:
#         return "%d-%d-%d %d" % (BCDtoInt(buf[6])+1900, BCDtoInt(buf[5]), BCDtoInt(buf[3]),
#                                     BCDtoInt(buf[2]))

def Write_RTC(bus=RTC_Bus):
    "Write system clock to MOD-RTC"     
    bus = smbus.SMBus(bus)
    a = time.time()
    a = time.gmtime(a)
    buf = []
    buf.append(InttoBCD(a.tm_sec))
    buf.append(InttoBCD(a.tm_min))
    buf.append(InttoBCD(a.tm_hour))    
    buf.append(InttoBCD(a.tm_mday))
    if a.tm_wday + 1 == 7:
        buf.append(0)
    else:
        buf.append(InttoBCD(a.tm_wday + 1))    
    buf.append(InttoBCD(a.tm_mon))
    buf.append(InttoBCD(a.tm_year-1900))
    bus.write_i2c_block_data(0x51, 0x02, buf)   
    if RTC_BUG_FIX == True: 
        bus.write_i2c_block_data(0x51, 0x09, [InttoBCD(a.tm_year-1900), InttoBCD(a.tm_mon), InttoBCD(a.tm_mday)])
    return True



def Sync_RTC(bus=RTC_Bus):
    "Sync system clock with MOD-RTC"
    bus = smbus.SMBus(bus)     
    buf = bus.read_i2c_block_data(0x51, 0x02, 7) 
    buf[0] &= 0x7F;
    buf[1] &= 0x7F;
    buf[2] &= 0x3F;
    buf[3] &= 0x3F;
    buf[4] &= 0x07;
    buf[5] &= 0x1F;
    buf[6] &= 0xFF; 
    
    if RTC_BUG_FIX == True:
        go_one_day_up = False
        if BCDtoInt(buf[5]) == 2 and BCDtoInt(buf[3]) == 29 and is_leap_year(BCDtoInt(buf[6])+1900) == False:
            buf[5] = InttoBCD(3)
            buf[3] = InttoBCD(1)
            go_one_day_up = True

    date_now = "%d-%d-%d %d:%d:%d" % (BCDtoInt(buf[6])+1900, BCDtoInt(buf[5]), BCDtoInt(buf[3]),
                                  BCDtoInt(buf[2]), BCDtoInt(buf[1]),
                                  BCDtoInt(buf[0]))
    if RTC_BUG_FIX == True:
        buf2 = bus.read_i2c_block_data(0x51, 0x09, 3)
        buf2[0] &= 0xFF;
        buf2[1] &= 0x1F;
        buf2[2] &= 0x3F;
        go_one_day_up = False
        date_now = datetime.datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S')
        last_write = [BCDtoInt(buf2[0])+1900, BCDtoInt(buf2[1]), BCDtoInt(buf2[2])]
        date_now = bug_fix(date_now, last_write, go_one_day_up)
    else:
        try:
            date_now = datetime.datetime.strptime(date_now, '%Y-%m-%d %H:%M:%S')
        except ValueError as e:
            print('found rtc bug use  -b 1 option')
            print(e)
            return False
    date_now = date_now.replace(tzinfo=pytz.UTC)
    date_now = date_now.astimezone(pytz.timezone(RTC_TIME_ZONE))
    dates = '%s-%s-%s' % (date_now.year, date_now.month, date_now.day)
    times = '%s:%s:%s' % (date_now.hour, date_now.minute, date_now.second)
    cmd = 'date -s %s' % (dates)
    os.system(cmd)
    cmd = 'date -s %s' % (times)
    os.system(cmd) 
    return True