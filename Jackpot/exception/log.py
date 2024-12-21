#-*- coding:utf-8 -*-

import logging
import sys
from logging.handlers import SysLogHandler, RotatingFileHandler
import conf

from multiprocessing import log_to_stderr

if conf.ERR_LOG_COUNT == 1:
    level = logging.ERROR
elif conf.ERR_LOG_COUNT == 2:
    level = logging.WARNING
elif conf.ERR_LOG_COUNT == 3:
    level = logging.INFO
elif conf.ERR_LOG_COUNT == 4:
    level = logging.DEBUG

class StreamToLogger(object):
    """
       Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, log_level=level):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass
    
logging.basicConfig(level=logging.DEBUG,format=' %(levelname)s:%(name)s:%(message)s',  )
log_formatter = logging.Formatter(' [%(levelname)s:%(processName)s] %(message)s')
if conf.ERR_USE_FILE == False:
    file_handler = SysLogHandler(address='/dev/log')
else:
    file_handler = RotatingFileHandler(conf.ERR_LOG, mode='a', maxBytes=5*1024*1024,
                                 backupCount=conf.ERR_LOG_COUNT, encoding=None, delay=0)
file_handler.setFormatter(log_formatter)

stdout_logger = logging.getLogger('STDOUT')
sl = StreamToLogger(stdout_logger, level)

sys.stdout = sl
stdout_logger.addHandler(file_handler)
stdout_logger.setLevel(level=level)

stderr_logger = logging.getLogger('STDERR')

sl = StreamToLogger(stderr_logger, level)
sys.stderr = sl
stderr_logger.addHandler(file_handler)
stderr_logger.setLevel(level=level)