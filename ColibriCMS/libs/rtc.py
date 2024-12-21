#-*- coding:utf-8 -*-
'''
Created on 30.06.2017 г.

@author: dedal
'''
import time
import os
if not __package__:
    import udp
    import conf
    import log
else:
    from . import udp
    from . import conf
    from . import log
import datetime
import pytz

def set_date_time(dates, times):
    response = udp.send('SET_DATE_TIME', ip=conf.JPSERVERIP, port=conf.JPSERVERIP, dates=dates, times=times)
    return response

def get_date_time(passwd=None):

    # if conf.UDP_TRANSFER_SERVER is True:
    dates = udp.send('get_date_times', ip=conf.SERVER)
    # else:
    #     dates = udp.send('GET_DATE_TIME', ip=conf.RTC, port=conf.RTC_PORT)
    if dates == None:
        
#         log_file = open(conf.ERR_LOG, 'a')
        log.stderr_logger.warning('\nRTC ERROR\n')
#         log_file.close()
        return False
    else:
        set_rtc(dates['dates'], dates['times'], passwd)
        # if os.name == 'posix':
        #     cmd = 'sudo date -s %s' % (dates['dates'])
        #     os.system(cmd)
        #     cmd = 'sudo date -s %s' % (dates['times'])
        #     os.system(cmd)
        # elif os.name == 'win32':
        #     dates = datetime.datetime.strptime(dates['dates'] + ' ' + dates['times'], '%Y.%m.%d %H:%M:%S')
        #     import pywin32  # @UnresolvedImport
        #     pywin32.SetSystemTime(dates.tm_year, dates.tm_mon , dates.tm_mday , dates.tm_hour , dates.tm_min)
        return True

def set_rtc(dates, times, passwd=None):
    if os.name == 'posix':
        # from . import conf
        cmd = 'sudo date -s %s' % (dates)
        if passwd:
            conf.root_cmd(cmd, passwd)
            cmd = 'sudo date -s %s' % (times)
            time.sleep(2)
            conf.root_cmd(cmd, passwd)
        else:
            os.system('sudo date -s %s' % (dates))
            time.sleep(2)
            os.system('sudo date -s %s' % (times))

    elif os.name == 'win32':
        import pywin32
        # import datetime
        dates = dates + ' ' + times
        dates = datetime.datetime.strptime(dates, "%Y-%m-%d %H:%M")
        pywin32.SetSystemTime(dates.year, dates.mon , dates.day , dates.hour , dates.minute)
    return True
    

class TZFormat():

    def __init__(self, tz='Europe/Sofia'):
        self.week_day = [u'Понеделник', u'Вторник', u'Сряда', u'Четвъртък', u'Петък', u'Събота', u'Неделя']
        self.tz = pytz.timezone(tz)

    def times(self):
        return time.time()

    # def now(self):
    #     return self.add_tz()

    def date_to_str(self, date=None, formats='%d.%m.%Y'):
        if date == None:
            date = self.now()
        else:
            date = self.add_tz(date)
        return datetime.datetime.strftime(date, formats)

    def str_to_date(self, date=None, formats='%d.%m.%Y'):
        date = datetime.datetime.strptime(date, formats)
        date = self.add_tz(date)
        # if date == None:
        #     date = self.add_tz()
        # else:
        #     date = self.add_tz(my_date)
        # date = self.add_tz(my_date)
        return date

    def go_back_from_date(self,  date=None, back=1):

        if date == None:
            date = self.now()
        else:
            date = self.add_tz(date)
        return date - datetime.timedelta(days=back)

    def go_up_from_date(self, date=None, up=1):
        # print date, type(date)
        if date == None:
            date = self.now()
        else:
            date = self.add_tz(date)
        return date + datetime.timedelta(days=up)

    def time_to_date(self, times=time.time()):
        date = time.gmtime(times)
        date = datetime.datetime(*date[:6])
        return self.add_tz(date)

    def date_to_time(self, date):
        date = date.replace(tzinfo=pytz.UTC)
        return time.mktime(date.timetuple()) + date.microsecond / 1E6

    def get_week_day(self, date=None, name=False):
        if date == None:
            date = self.add_tz()
        if name is False:
            return datetime.date.weekday(date)
        else:
            return self.week_day[datetime.date.weekday(date)]

    def add_tz(self, date=datetime.datetime.utcnow()):
        date = date.replace(tzinfo=self.tz)
        # date = date.astimezone(pytz.UTC)
        if self.tz != None:
            return date.astimezone(self.tz)
        else:
            return date

    def now(self):
        if self.tz != None:
            date = datetime.datetime.utcnow()
            date = date.replace(tzinfo=pytz.UTC)
            return date.astimezone(self.tz)
        else:
            date = datetime.datetime.now()
            return date

    def set_tz_info(self, date):
        # date.replace(tzinfo=self.tz)
        return self.tz.localize(date)

    def go_to_first(self, date):
        date = date.replace(day=1)
        return date


class DateStr():
    
    @staticmethod
    def date_to_str(date, formats = '%d.%m.%Y'):
        return datetime.datetime.strftime(date, formats)
    
    @staticmethod
    def str_to_date(date, formats='%d.%m.%Y'):
        return datetime.datetime.strptime(date, formats)
    
    @staticmethod
    def go_to_first(date):
        date = date.replace(day=1)
        return date
    
    @staticmethod
    def go_back_from_now(back):
        return datetime.datetime.now() - datetime.timedelta(days=back)
    
    @staticmethod
    def go_back_from_date(date, back):
        return date - datetime.timedelta(days=back)
    
    @staticmethod
    def go_up_from_date(date, up):
        return date + datetime.timedelta(days=up)
    
if __name__ == '__main__':
    RTC = TZFormat('')

