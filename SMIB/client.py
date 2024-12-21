'''
Created on 18.02.2019

@author: dedal
'''
import libs.sock.udp_socket.client as client
from libs.sock.udp_socket.client import BadCript
from multiprocessing import Process, Lock
from queue import Empty
import log
import time
import os

LOCK = Lock()

def send(evt, ip, port, log, timeout, udp_buffer, crypt, **kwargs):
    response = None
    # global LOCK
    # lock = LOCK.acquire(timeout=1)
    # if lock is True:
    try:
        my_client = client.Client(ip=ip, port=port, log=log, timeout=timeout, udp_buffer=udp_buffer, crypt=crypt)
        response = my_client.send(evt, **kwargs)
        my_client.close()
    except BadCript:
        log.critical('BAD RSA SIGNATURE')
        response = None
    except Exception as e:
        response = None
        log.error('ip: %s port:%s evt: %s kwargs: %s' %  (ip, port, evt, kwargs))
        log.error(e, exc_info=True)
            # return None
    finally:
        try:
            my_client.close()
        except:
            pass
    # try:
    #     LOCK.release()
    # except ValueError:
    #     pass
    # except Exception as e:
    #     log.error(e, exc_info=True)
    return response

class Send(Process):

    def __init__(self, pipe, crypt):
        Process.__init__(self)
        self.pipe = pipe
        # self.daemon = True
        self.crypt = crypt

        # self.log = log.get_log(log.LOG_CHANEL_LEVEL['client_cart'])

    def send(self, evt, ip, port, timeout, udp_buffer, **kwargs):
        response = None
        try:
            my_client = client.Client(ip=ip, port=port, log=self.log, timeout=timeout, udp_buffer=udp_buffer, crypt=self.crypt)
            response = my_client.send(evt, **kwargs)
            # my_client.close()
        except BadCript:
            response = None
            self.log.error('BAD RSA SIGNATURE')
        except Exception as e:
            response = None

            self.log.error(e, exc_info=True)
            # return None
        finally:
            try:
                my_client.close()
            except:
                pass
        if response == None and timeout > 0:
            time.sleep(2)
            self.log.error('ip: %s port:%s evt: %s kwargs: %s' % (ip, port, evt, kwargs))
        time.sleep(0.2)
        return response

    def run(self):
        self.log = log.get_log(log.LOG_CHANEL_LEVEL['server'])
        ERROR = 0
        while True:
            for i in self.pipe:
                if i.poll(0.2):
                    get_from = None
                    try:
                        get_from = i.recv()
                        if get_from['timeout'] <= 0:
                            get_from['no_response'] = True
                            self.send(**get_from)
                            data = True
                            # i.send(True)
                        elif get_from['timeout']-4 <= 2:
                            data = self.send(**get_from)
                        elif get_from['send_time'] + (get_from['timeout']-3) >= time.time():
                            data = self.send(**get_from)
                        if data == None:
                            data = None
                            # i.send(None)
                            for b in self.pipe:
                                while b.poll():
                                    b.recv()
                                    # b.send(None)
                        else:
                            i.send([data, get_from])
                    except Exception as e:
                        self.log.error(e, exc_info=True)
                        data = None
                        # i.send(None)
                        for b in self.pipe:
                            while b.poll():
                                b.recv()
                                # b.send(None)



