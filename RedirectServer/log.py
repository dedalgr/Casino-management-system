'''
Created on 30.04.2019

@author: dedal
'''
import libs.log
import logging
import conf
from multiprocessing import log_to_stderr

logging.basicConfig(level=logging.DEBUG,format=' [%(levelname)s:%(processName)s] %(message)s')
log_formatter = logging.Formatter(' [%(levelname)s:%(processName)s] %(message)s')

file_handler = libs.log.MySysLogHandler(ident='RedirectServer')

file_handler.setFormatter(log_formatter)
file_handler.setLevel(conf.LOG_LEVEL)

mostrecent = libs.log.MostRecentHandler(max_records=conf.MAX_LOG)
mostrecent.setLevel(logging.DEBUG)
rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)
rootLogger.addHandler(mostrecent)

def get_log(level=conf.LOG_LEVEL):
    global file_handler
    log = log_to_stderr(level)
    file_handler.setFormatter(log_formatter)
    log.addHandler(file_handler)
    log.setLevel(level)
    return log

# stdout_logger = log_to_stderr(conf.LOG_LEVEL)
#
# stdout_logger.addHandler(file_handler)
#
# stderr_logger = log_to_stderr(conf.LOG_LEVEL)
# stderr_logger.addHandler(file_handler)

if conf.DB_DEBUG == True:
    db_logger = logging.getLogger('sqlalchemy')
    db_logger.setLevel(conf.LOG_LEVEL)
    db_logger.addHandler(file_handler)

