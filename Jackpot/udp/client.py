#-*- coding:utf-8 -*-
import socket
import cr  # @UnresolvedImport
import json
import conf  # @UnresolvedImport
import time
from exception import log
if conf.IV_JUMP is False:
    CRYPT = cr.Crypt(cr.COMUNICATION, cr.IV, conf.IV_JUMP)
else:
    CRYPT = cr.CryptFernet(cr.key)
from sock.udp_socket import client
# from sock.tcp_socket import client as tcp_client

def send(evt, ip, port, timeout=conf.UDP_TIMEOUT, udp_buffer=conf.UDP_BUFFER, crypt=CRYPT, *args, **kwargs):
    '''
    Изпраща информация към TCP сървър.
    _tcp.Client
    :param evt: Име на функция на отдалечения сървър.
    :param kwargs: Аргументи ако има
    :return: Връща отговора на функцията. Ако е неуспешно None
    '''
#     print 'clint send evt', evt, ip, port
    try:
        my_client = client.Client(ip=ip, port=port, timeout=timeout, log=log.stdout_logger, udp_buffer=udp_buffer, crypt=crypt)
        my_client.log.setLevel(client.logging.ERROR)
        response = my_client.send(evt, **kwargs)
        my_client.close()
    except Exception as e:
        client.LOG_CLIENT.warning(e, exc_info=True)
        response = None
    finally:
        try:
            my_client.close()
        except:
            pass
    return response

def visual_send(evt, ip, port=conf.UDP_VISUAL_PORT, timeout=conf.UDP_TIMEOUT, udp_buffer=conf.UDP_BUFFER, crypt=CRYPT, *args, **kwargs):
    '''
    Изпраща информация към TCP сървър.
    _tcp.Client
    :param evt: Име на функция на отдалечения сървър.
    :param kwargs: Аргументи ако има
    :return: Връща отговора на функцията. Ако е неуспешно None
    '''
#     print 'clint send evt', evt, ip, port
    try:
        my_client = client.Client(ip=ip, port=port, timeout=timeout, log=log.stdout_logger, udp_buffer=udp_buffer, crypt=crypt)
        my_client.log.setLevel(client.logging.ERROR)
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
    return response

