'''
Created on 12.03.2019

@author: dedal
'''
import conf
from libs.sock.udp_socket import client
import log

client.LOG_CLIENT.setLevel(conf.LOG_LEVEL)

def send(evt, ip, port=conf.PORT, timeout = conf.TIMEOUT, log=log.get_log(), **kwargs):
    response = None
    try:
        my_client = client.Client(ip=ip, port=port, timeout=timeout, log=log, udp_buffer=conf.BUFFER, crypt=conf.CRYPT)
        my_client.log.setLevel(conf.LOG_LEVEL)
        response = my_client.send(evt, **kwargs)
        my_client.close()
    except Exception as e:
        response = None
        # client.LOG_CLIENT.error('ip: %s port: %s evt: %s kwargs: %s' %  (ip, port, evt, kwargs))
        client.LOG_CLIENT.warning(e, exc_info=True)
        client.LOG_CLIENT.warning('ip: %s port: %s evt: %s kwargs: %s' % (ip, port, evt, kwargs))
        # return None
    finally:
        try:
            my_client.close()
        except:
            pass
    if response == None:
        client.LOG_CLIENT.warning('RESPONE None: ip: %s port: %s evt: %s kwargs: %s' % (ip, port, evt, kwargs))
    return response
