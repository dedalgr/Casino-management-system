#-*- coding:utf-8 -*-
'''
Created on 12.09.2018 г.

@author: dedal
'''
import logging
from logging.handlers import SysLogHandler, RotatingFileHandler, SocketHandler

try:
    from collections import deque
except ImportError:
    # pre 2.5
    class deque(list):
        def popleft(self):
            elem = self.pop(0)
            return elem

try:
    reversed
except NameError:
    # pre 2.4
    def reversed(items):
        return items[::-1]


class MostRecentHandler(logging.Handler):
    'A Handler which keeps the most recent logging records in memory.'

    def __init__(self, max_records=2000):
        logging.Handler.__init__(self)
        self.logrecordstotal = 0
        self.max_records = max_records
        try:
            self.db = deque([], max_records)
        except TypeError:
            # pre 2.6
            self.db = deque([])

    def emit(self, record):
        self.logrecordstotal += 1
        try:
            self.db.append(record)
            # pre 2.6
            while len(self.db) > self.max_records:
                self.db.popleft()
        except Exception:
            self.handleError(record)

class StreamToLogger(object):
    """
       Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass

class MySysLogHandler(SysLogHandler):
    def __init__(self, ident):
        self.ident = ident
        SysLogHandler.__init__(self, address='/dev/log')

    def emit(self, record):
        priority = self.encodePriority(self.facility, self.mapPriority(record.levelname))
        record.ident = self.ident
        super(MySysLogHandler, self).emit(record)

class MySocketLogHandler(SocketHandler):
    def __init__(self, adress, port, ident='' ):
        self.ident = ident
        SocketHandler.__init__(self, adress, port)
        self.timeout = 5

    def emit(self, record):
        # priority = self.encodePriority(self.facility, self.mapPriority(record.levelname))
        record.ident = self.ident
        super(MySocketLogHandler, self).emit(record)
        self.close()


class MyRotatingFileHandler(RotatingFileHandler):

    def __init__(self, log_name, maxBytes, backupCount):
        RotatingFileHandler.__init__(self, log_name, mode='a',
                            maxBytes=maxBytes,
                            backupCount=backupCount,
                            encoding=None,
                            delay=0)

    # def emit(self, record):
    #     priority = self.encodePriority(self.facility, self.mapPriority(record.levelname))
    #     super(MyRotatingFileHandler, self).emit(record)