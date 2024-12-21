#-*- coding:utf-8 -*-
'''
Created on 22.02.2019

@author: dedal
'''
from multiprocessing import Process
import log
import client
from libs import system
import time

class JPServer(Process):
    def __init__(self, **kwargs):
        Process.__init__(self, name='JPServer')
        # self.daemon = True
        self.log=log.get_log(log.LOG_CHANEL_LEVEL['jpserver'])
        self.db = kwargs['db']
        self.crypt = kwargs['crypt']
        self.conf = kwargs['conf']
        self.pipe = kwargs['pipe']
        self.tcp_buffer = self.conf.get('COMUNICATION', 'buffer', 'int')
        self.block_if_lost = self.conf.get('JP_SERVER', 'block_if_lost', 'bool')
        self.block_count = self.conf.get('JP_SERVER', 'block_count', 'int')
        self.tcp_timeout = self.conf.get('COMUNICATION', 'timeout', 'int')+2
        self.tcp_ip = self.conf.get('JP_SERVER', 'ip', 'str')
        self.tcp_port = self.conf.get('JP_SERVER', 'port', 'int')
        self.db_server_port = self.conf.get('DB_SERVER', 'port', 'int')
        self.db_server_ip = self.conf.get('DB_SERVER', 'ip', 'str')
        self.pr = self.db.get('JACKPOT')
        self.ip = system.get_ip()

    def old_poll_clean(self):
        for i in self.pipe:
            if self.pipe[i].poll():
                self.pipe[i].recv()

    def send_data(self, evt='add_bet', **kwargs):
        player = self.db.get('PLAYER')
        if player is not False and player != None :
            player = player['id']
        response = client.send(evt,
                    ip=self.tcp_ip,
                    port=self.tcp_port,
                    log=self.log,
                    timeout=self.tcp_timeout,
                    udp_buffer=self.tcp_buffer,
                    crypt=self.crypt,
                    player=player,
                    **kwargs)
        return response

    def send_exception(self, **kwargs):
        try:
            for i in range(3):  # @UnusedVariable
                data = client.send('write_log',
                        ip=self.db_server_ip,
                        port=self.db_server_port,
                        log=self.log,
                        timeout=self.tcp_timeout+3,
                        udp_buffer=self.tcp_buffer,
                        crypt=self.crypt,
                        my_name=self.ip,
                        **kwargs)
                if data != None:
                    break
                time.sleep(2)
        except Exception as e:
            self.log.error(e, exc_info=True)
            return None
        return data

    def run(self):
        block_count = self.block_count
        while True:
            data = self.pipe['sas'].recv()
            self.log.debug('%s', data)
            try:
                self.pr = self.db.get('JACKPOT')
                if data == None:
                    pass
                elif data is False:
                    pass
                elif None in data.values():
                    pass
                # elif data is True:
                #     pass
                elif data['old_bet'] >= data['new_bet']:
                    self.log.warning('%s', data)
                else:
                    bet = round(data['new_bet'] - data['old_bet'], 2)
                    if self.pr < 0.2:
                        self.pr = 0.2
                    bet = round(bet*self.pr, 2)
                    self.log.info('%s', bet)

                    response = self.send_data(bet=bet, smib_ip=self.ip)
                    if not response:
                        block_count -= 1
                        while self.pipe['sas'].poll():
                            self.pipe['sas'].recv()
                        self.log.warning('jpserver not response')
                    else:
                        block_count = self.block_count

                    if self.block_if_lost is True:
                        if block_count < 0:
                            # self.log.error('block emg, lost server')
                            self.pipe['sas'].send(['sas.get_single_meter', {'command':'halt'}])
                            # self.db.set('STATUS', 'JP SERVER LOST')
                            self.log.error('no connection with jackpot server: HALT')
                            while True:
                                time.sleep(5)
                                while self.pipe['sas'].poll():
                                    self.pipe['sas'].recv()
                                response = self.send_data(evt='ALIFE')
                                if response is True:
                                    self.log.info('start emg, server alive')
                                    while True:
                                        data = None
                                        while self.pipe['sas'].poll():
                                            self.pipe['sas'].recv()
                                        self.pipe['sas'].send(['sas.get_single_meter', {'command': 'start'}])
                                        # while self.pipe['sas'].poll():
                                        data = self.pipe['sas'].recv()
                                        if data is True:
                                            break

                                    self.log.error('connection with jackpot server: START EMG')
                                    # self.db.set('STATUS', 'OK')
                                    block_count = self.block_count
                                    break
            except Exception as e:
                self.log.critical(e, exc_info=True)
                time.sleep(0.5)

