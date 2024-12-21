#-*- coding:utf-8 -*-

import logging
import sys
if not __package__:
    import conf
else:
    from . import conf
from logging.handlers import RotatingFileHandler
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

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
#    filename=ERR_LOG,
#    filemode='a'
 )

log_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
my_handler = RotatingFileHandler(conf.LOG_PATH, mode='a', maxBytes=5*1024*1024,
                                 backupCount=10, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.WARNING)

# socketh = logging.handlers.SocketHandler(sysobj.LOG_HOST, sysobj.LOG_PORT)

# Пренасочва целия лог към файл
stdout_logger = logging.getLogger('STDOUT:CMS')
sl = StreamToLogger(stdout_logger, logging.WARNING)
sys.stdout = sl
stdout_logger.addHandler(my_handler)

stderr_logger = logging.getLogger('STDERR:CMS')
sl = StreamToLogger(stderr_logger, logging.WARNING)
sys.stderr = sl
stderr_logger.addHandler(my_handler)


# db_handler = RotatingFileHandler(conf.DB_LOG_PATH, mode='a', maxBytes=5*1024*1024,
#                                  backupCount=10, encoding=None, delay=0)
# db_handler.setFormatter(log_formatter)
# db_handler.setLevel(logging.DEBUG)
if conf.DB_DEBUG is True:
    db_logger = logging.getLogger('sqlalchemy')
    db_logger.setLevel(logging.WARNING)
    db_logger.addHandler(my_handler)

