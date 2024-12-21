# -*- coding:utf-8 -*-
'''
Created on 9.09.2018 г.

@author: dedal
'''
import datetime
import time
import pytz


class BG():

    def __init__(self, tz='Europe/Sofia'):
        self.week_day = [u'Понеделник', u'Вторник', u'Сряда', u'Четвъртък', u'Петък', u'Събота', u'Неделя']
        self.tz = tz

    def times(self):
        return time.time()

    def now(self):
        return self.add_tz()

    def date_to_str(self, date=None, formats='%d.%m.%Y'):
        if date == None:
            date = self.add_tz()
        else:
            date = self.add_tz(date)
        return datetime.datetime.strftime(date, formats)

    def str_to_date(self, date=None, formats='%d.%m.%Y'):
        date = datetime.datetime.strptime(date, formats)
        date.timetz()
        # if date == None:
        #     date = self.add_tz()
        # else:
        #     date = self.add_tz(my_date)
        # date = self.add_tz(my_date)
        return date

    def go_back_from_date(self, back=1, date=None):
        if date == None:
            date = self.add_tz()
        return date - datetime.timedelta(days=back)

    def go_up_from_date(self, up=1, date=None):
        if date == None:
            date = self.add_tz()
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
        if name == False:
            return datetime.date.weekday(date)
        else:
            return self.week_day[datetime.date.weekday(date)]

    def add_tz(self, date=datetime.datetime.utcnow()):
        date = date.replace(tzinfo=pytz.UTC)
        if self.tz != None:
            return date.astimezone(pytz.timezone(self.tz))
        else:
            return date


if __name__ == '__main__':
    date_now = datetime.datetime.now()
    sm_day = datetime.date.weekday(date_now)
    rtc = BG(None)
    bonus_on_day = [0, 1, 3, 5, 6]
    a = rtc.date_to_str(datetime.datetime.utcnow(), '%d.%m.%Y %H:%M:%S')
    b = rtc.str_to_date(a, '%d.%m.%Y %H:%M:%S')
    print(a, b)