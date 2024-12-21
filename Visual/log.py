#-*- coding:utf-8 -*-

import logging
import sys
# from conf import *
from libs.log import SysLogHandler, MyRotatingFileHandler
import config
LOG_LEVEL = config.LOG_LEVEL

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

if LOG_LEVEL == 'DEBUG':
    LOG_LEVEL = logging.DEBUG
elif LOG_LEVEL == 'INFO':
    LOG_LEVEL = logging.INFO
elif LOG_LEVEL == 'WARNING':
    LOG_LEVEL = logging.WARNING
elif LOG_LEVEL == 'ERROR':
    LOG_LEVEL = logging.ERROR
elif LOG_LEVEL == 'CRITICAL':
    LOG_LEVEL = logging.CRITICAL
else:
    LOG_LEVEL = logging.INFO


logging.basicConfig(level=logging.DEBUG,format='%(levelname)s:%(name)s:%(message)s',  )
log_formatter = logging.Formatter('VISUAL: [%(levelname)s:%(processName)s] %(message)s')
if config.FILE_HANDLER is False:
    file_handler = SysLogHandler(address='/dev/log')
else:
    file_handler = MyRotatingFileHandler(config.LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(LOG_LEVEL)
stdout_logger = logging.getLogger('STDOUT')
sl = StreamToLogger(stdout_logger, LOG_LEVEL)
sys.stdout = sl
stdout_logger.addHandler(file_handler)
stdout_logger.setLevel(LOG_LEVEL)

stderr_logger = logging.getLogger('STDERR')
sl = StreamToLogger(stderr_logger, LOG_LEVEL)
sys.stderr = sl
stderr_logger.addHandler(file_handler)
stderr_logger.setLevel(LOG_LEVEL)