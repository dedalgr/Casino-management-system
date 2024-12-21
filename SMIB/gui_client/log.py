#-*- coding:utf-8 -*-

import logging
import sys
from logging.handlers import SysLogHandler, RotatingFileHandler
# Създава лог файл
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
    
logging.basicConfig(level=logging.DEBUG,format=' [%(levelname)s:%(name)s] %(message)s' )
log_formatter = logging.Formatter(' [%(levelname)s:%(processName)s] %(message)s')
# my_handler = RotatingFileHandler('/home/olimex/gui_client.log',
#                                         maxBytes=5242880,
#                                         backupCount=7)
my_handler = SysLogHandler(address='/dev/log')

my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.DEBUG)

# Пренасочва целия лог към файл
stdout_logger = logging.getLogger('CLIENT STDOUT')
stdout_logger.setLevel(logging.INFO)
sl = StreamToLogger(stdout_logger, logging.WARNING)
sys.stdout = sl
stdout_logger.addHandler(my_handler)

stderr_logger = logging.getLogger('CLIENT STDERR')
stderr_logger.setLevel(logging.DEBUG)
sl = StreamToLogger(stderr_logger, logging.DEBUG)
sys.stderr = sl



