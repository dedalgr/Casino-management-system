# -*- coding:utf-8 -*-
'''
Created on 28.02.2019

@author: dedal
'''
import client
import crypt
import time
import libs.cr
import logging
import threading
import multiprocessing
import libs.system
import conf
CONF = conf.Conf()
COMUNICATION_IV_JUMP = CONF.get('COMUNICATION', 'iv_jump', 'bool')
key = crypt.vector_generator(iv_jump=COMUNICATION_IV_JUMP)
if COMUNICATION_IV_JUMP is False:
    COMUNICATION_CRYPT = libs.cr.Crypt(crypt.COMUNICATION, crypt.IV, False)
else:
    COMUNICATION_CRYPT = libs.cr.CryptFernet(key)
IP = '127.0.0.1'
JP_PORT=2522
JP_IP='192.168.1.11'
MY_IP = '127.0.0.1'
PORT = 30593
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)
TIMEOUT = 12
BUFFER = 4096


class Test():
    def __init__(self, ip=MY_IP, buffer=BUFFER, port=PORT, log=LOG, timeout=TIMEOUT, crypt=COMUNICATION_CRYPT):
        self.ip = ip
        self.log = log
        self.buffer = buffer
        self.timeout = timeout
        self.crypt = crypt
        self.port = port

    def alive(self):
        return client.send('alive', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt)

    def hw_id(self):
        return client.send('hw_id', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt)

    def sw_id(self):
        return client.send('sw_id', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt)

    def emmc_id(self):
        return client.send('emmc_id', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt)

    def crc(self):
        return client.send('crc', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt)

    def status(self):
        return client.send('status', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt)

    def jp_down(self, mony=1, tax='00'):
        return client.send('sas.jp_down', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, min_bet=0, mony=mony, tax=tax)

    def get_meter(self):
        return client.send('sas.meter', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt)

    def set_legacy(self, mony=1, tax='00'):
        return client.send('sas.set_legacy_bonus', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, mony=mony, tax=tax)

    def client_bonus(self, mony=1, tax='02', **kwargs):
        return client.send('sas.client_bonus', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, mony=mony, tax=tax)

    def get_multi_meter(self, **kwargs):
        return client.send('sas.get_multi_meter', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def get_single_meter(self, **kwargs):
        return client.send('sas.get_single_meter', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def get_event(self, **kwargs):
        return client.send('sas.event', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def add_bet(self, bet=1.00):
        return client.send('add_bet', ip=JP_IP, port=JP_PORT, log=self.log, udp_buffer=self.buffer,
                           timeout=10,
                           crypt=self.crypt, bet=bet, smib_ip=self.ip)

    def server_alive(self, **kwargs):
        return client.send('server_alive', ip=IP, port=PORT, log=self.log, udp_buffer=self.buffer,
                           timeout=12,
                           crypt=self.crypt)

    def get_client(self, **kwargs):
        return client.send('get_client', ip=IP, port=self.port, log=self.log, udp_buffer=self.buffer,
                           timeout=12,
                           crypt=self.crypt, cart_id='B241E026', my_name=self.ip)

    def server_alive(self):
        # print IP, PORT, self.buffer
        return client.send('server_alive', ip=IP, port=PORT, log=self.log, udp_buffer=self.buffer,
                           timeout=12,
                           crypt=self.crypt)

    def get_rtc_dates(self):
        return client.send('GET_DATE_TIME', ip=IP, port=PORT, log=self.log, udp_buffer=self.buffer,
                           timeout=12,
                           crypt=self.crypt)

    def activ_bonus_update_mony(self):
        return client.send('activ_bonus_update_mony', bonus_id=28217, mony=20, my_name=self.ip, ip=IP, port=PORT, log=self.log, udp_buffer=self.buffer,
                           timeout=12,
                           crypt=self.crypt)

    def aft_in(self, **kwargs):
        return client.send('sas.add_in_to_emg', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)
    def aft_out(self, **kwargs):
        return client.send('sas.get_out_from_emg', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def aft_won(self, games=None, **kwargs):
        return client.send('sas.add_won_to_emg', ip=self.ip, port=self.port, log=self.log, timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def aft_clean_transaction(self, **kwargs):
        return client.send('sas.clean_transaction_poll', ip=self.ip, port=self.port, log=self.log,
                           timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def aft_get_last_transaction(self, **kwargs):
        return client.send('sas.get_last_transaction', ip=self.ip, port=self.port, log=self.log,
                           timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def aft_format_transaction_id(self, **kwargs):
        return client.send('sas.format_transaction_id', ip=self.ip, port=self.port, log=self.log,
                           timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def aft_register(self, **kwargs):
        return client.send('sas.aft_register', ip=self.ip, port=self.port, log=self.log,
                           timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def aft_lock(self, **kwargs):
        return client.send('sas.lock_emg', ip=self.ip, port=self.port, log=self.log,
                           timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def aft_clean(self, **kwargs):
        return client.send('sas.cansel_request', ip=self.ip, port=self.port, log=self.log,
                           timeout=self.timeout,
                           udp_buffer=self.buffer, crypt=self.crypt, **kwargs)

    def stop_proc(self, name):
        if name == 'sas':
            return client.send('sas_stop', ip=self.ip, port=self.port, log=self.log,
                        timeout=self.timeout,
                        udp_buffer=self.buffer, crypt=self.crypt)
        elif name == 'rfid':
            return client.send('rfid_stop', ip=self.ip, port=self.port, log=self.log,
                               timeout=self.timeout,
                               udp_buffer=self.buffer, crypt=self.crypt)
        elif name == 'client':
            return client.send('rfid_stop', ip=self.ip, port=self.port, log=self.log,
                               timeout=self.timeout,
                               udp_buffer=self.buffer, crypt=self.crypt)

    def error_log(self, msg, port=PORT):
        client.send('write_log', ip=self.ip, port=port, log=self.log, udp_buffer=self.buffer,
                    timeout=12,
                    crypt=self.crypt, my_name=self.ip, msg=msg)

if __name__ == '__main__':
    import time
    tmp = [
        Test(ip='192.168.1.11', port=PORT),
        Test(ip='192.168.1.12', port=PORT),
        Test(ip='192.168.1.14', port=PORT),
        Test(ip='192.168.1.15', port=PORT),
        Test(ip='192.168.1.16', port=PORT),
        Test(ip='192.168.1.17', port=PORT),
        Test(ip='192.168.1.18', port=PORT),
        Test(ip='192.168.1.19', port=PORT),
        Test(ip='192.168.1.20', port=PORT),
    ]

    def t(obj):
        count = 0
        while True:
            count += 1
            time.sleep(0.1)
            print(obj.ip, obj.add_bet(bet=1))
            if count >= 100000:
                time.sleep(3600)
    import multiprocessing

    thread = []
    for i in tmp:
        thread.append(multiprocessing.Process(target=t, kwargs={'obj':i}))
    for i in thread:
        i.start()