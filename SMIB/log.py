import logging
from logging.handlers import SysLogHandler, RotatingFileHandler, SocketHandler
from multiprocessing import log_to_stderr
import conf
import libs.system
import libs.log

IP = libs.system.get_ip()
CONF = conf.Conf()

# ===============================================================================
# HANDLER FORMAT
# ===============================================================================
if CONF.get('LOGGING_FILE', 'sys_log', 'bool') is True:
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s: [%(levelname)s:%(name)s] %(message)s')
    log_formatter = logging.Formatter(' %(asctime)s: [%(levelname)s:%(processName)s] %(message)s')
else:
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s: [%(levelname)s:%(name)s] %(message)s')
    log_formatter = logging.Formatter(' %(asctime)s: [%(levelname)s:%(name)s] %(message)s')
log_net_formatter = logging.Formatter(' %(ident)s %(asctime)s:%(levelname)s:%(name)s:%(message)s')
# ===============================================================================
# CHANEL LEVEL
# ===============================================================================
LOG_CHANEL_LEVEL = CONF.get('LOGGING_LEVEL')
for i in LOG_CHANEL_LEVEL:
    if LOG_CHANEL_LEVEL[i] == 'DEBUG':
        LOG_CHANEL_LEVEL[i] = logging.DEBUG
    elif LOG_CHANEL_LEVEL[i] == 'INFO':
        LOG_CHANEL_LEVEL[i] = logging.INFO
    elif LOG_CHANEL_LEVEL[i] == 'WARNING':
        LOG_CHANEL_LEVEL[i] = logging.WARNING
    elif LOG_CHANEL_LEVEL[i] == 'ERROR':
        LOG_CHANEL_LEVEL[i] = logging.ERROR
    elif LOG_CHANEL_LEVEL[i] == 'CRITICAL':
        LOG_CHANEL_LEVEL[i] = logging.WARNING
    else:
        LOG_CHANEL_LEVEL[i] = logging.ERROR

# ===============================================================================
# FILE HANDLER
# ===============================================================================

if CONF.get('LOGGING_FILE', 'use', 'bool') is True:
    if CONF.get('LOGGING_FILE', 'sys_log', 'bool') is True:
        file_handler = libs.log.MySysLogHandler(ident='SMIB')
        # file_handler.setFormatter(log_formatter)
    else:
        file_handler = libs.log.MyRotatingFileHandler(conf.LOG_FILE,
                                        maxBytes=CONF.get('LOGGING_FILE', 'size', 'int'),
                                        backupCount=CONF.get('LOGGING_FILE', 'count', 'int'),)
    file_handler.setFormatter(log_formatter)
    level = CONF.get('LOGGING_FILE', 'level', 'str')
    if level == 'WARNING':
        file_handler.setLevel(logging.WARNING)
    elif level == 'INFO':
        file_handler.setLevel(logging.INFO)
    elif level == 'ERROR':
        file_handler.setLevel(logging.ERROR)
    elif level == 'CRITICAL':
        file_handler.setLevel(logging.CRITICAL)
    elif level == 'DEBUG':
        file_handler.setLevel(logging.DEBUG)
    else:
        file_handler.setLevel(logging.ERROR)
else:
    file_handler = None
# ===============================================================================
# SERVER HANDLER
# ===============================================================================
if CONF.get('LOGGING_SERVER', 'use', 'bool') is True:
    socketh_handler = libs.log.MySocketLogHandler(
        CONF.get('LOGGING_SERVER', 'server_ip', 'str'),
        CONF.get('LOGGING_SERVER', 'port', 'int'),
        IP
    )
    socketh_handler.setFormatter(log_net_formatter)
    level = CONF.get('LOGGING_SERVER', 'level', 'str')
    if level == 'WARNING':
        socketh_handler.setLevel(logging.WARNING)
    elif level == 'INFO':
        socketh_handler.setLevel(logging.INFO)
    elif level == 'ERROR':
        socketh_handler.setLevel(logging.ERROR)
    elif level == 'CRITICAL':
        socketh_handler.setLevel(logging.CRITICAL)
    elif level == 'DEBUG':
        socketh_handler.setLevel(logging.DEBUG)
    else:
        socketh_handler.setLevel(logging.ERROR)

else:
    socketh_handler = None


def get_log(level):
    global socketh_handler
    global file_handler
    log = log_to_stderr(level)
    if CONF.get('LOGGING_SERVER', 'use', 'bool') is True:
        socketh_handler.setFormatter(log_net_formatter)
        log.addHandler(socketh_handler)
    if CONF.get('LOGGING_FILE', 'use', 'bool') is True:
        file_handler.setFormatter(log_formatter)
        log.addHandler(file_handler)
    log.setLevel(level)
    return log

if __name__ == '__main__':
    l = get_log(logging.INFO)
    l.warning('test')
