# -*- coding:utf-8 -*-
from libs.sock.udp_socket import client
import config
import log

def send(evt, *args, **kwargs):
    '''
    Изпраща информация към TCP сървър.
    _tcp.Client
    :param evt: Име на функция на отдалечения сървър.
    :param kwargs: Аргументи ако има
    :return: Връща отговора на функцията. Ако е неуспешно None
    '''
    try:
        my_client = client.Client(ip=config.JP_IP, log=log.stdout_logger,  port=config.JP_PORT, timeout=config.UDP_TIMEOUT, udp_buffer=config.UDP_BUFFER, crypt=config.CRYPT)
        response = my_client.send(evt, **kwargs)
        my_client.close()
    except Exception as e:
        client.LOG_CLIENT.warning(e, exc_info=True)
        return None
    finally:
        try:
            my_client.close()
        except:
            pass
    if response == None:
        client.LOG_CLIENT.warning('SEND_TO_SERVER: evt %s, kwargs %s' % (evt, kwargs))
    return response