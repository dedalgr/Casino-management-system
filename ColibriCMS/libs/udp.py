'''
Created on 11.03.2019

@author: dedal
'''
if not __package__:
    import conf
    import cr
    import log
    import rsa
    import sock
    if conf.TCP == True:
        from sock.tcp_socket import client
    else:
        from sock.udp_socket import client
else:
    from . import conf
    from . import cr
    from . import log
    from . import rsa
    if conf.TCP == True:
        from .sock.tcp_socket import client
    else:
        from .sock.udp_socket import client

RSA = rsa.RSAKey()
RSA.load_key(conf.PRIVATE_KEY)
if conf.UDP_IV_JUMP is False:
    CRYPT = cr.Crypt(cr.EMPTY2, cr.IV, False)
else:
    CRYPT = cr.CryptFernet(cr.key)

def send(evt, ip, port=conf.UDP_PORT, timeout=conf.UDP_TIMEOUT, rsa=RSA, crypt=CRYPT, **kwargs):
    response = None
    try:
        smib_ip = ip
        ip = conf.SERVER
        kwargs['smib_ip'] =  smib_ip
        kwargs['smib_port'] = port
        port = conf.UDP_PORT
        my_client = client.Client(ip=ip, port=port, timeout=timeout, log=log.stderr_logger, udp_buffer=conf.UDP_BUFFER, crypt=crypt, rsa=rsa)
        my_client.log.setLevel(log.logging.WARNING)
        response = my_client.send(evt, **kwargs)
        if response == None:
            client.LOG_CLIENT.warning('ip: %s evt: %s kwargs: %s response: %s' % (ip, evt, kwargs, response))
    except Exception as e:
        response = None
        client.LOG_CLIENT.error('ip: %s evt: %s kwargs: %s' %  (ip, evt, kwargs))
        # return None
    finally:
        try:
            my_client.close()
        except:
            pass
    return response
