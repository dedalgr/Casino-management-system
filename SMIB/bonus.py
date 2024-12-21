# -*- coding:utf-8 -*-
'''
Created on 21.02.2019

@author: dedal
'''
from multiprocessing import Process
import log
import time
import client
from libs import system
import threading
from queue import Queue


class Bonus(Process):
    def __init__(self, **kwargs):
        Process.__init__(self, name='Bonus')
        # self.daemon = True
        self.pipe = kwargs['pipe']
        self.db = kwargs['db']
        self.conf = kwargs['conf']
        self.crypt = kwargs['crypt']
        self.send = kwargs['send']
        self.log = log.get_log(log.LOG_CHANEL_LEVEL['bonus'])
        self.bonus = self.db.get('BONUSCART')
        self.bonus_error = self.db.get('BONUS_ERROR_LOG')
        self.sas_timeout = self.conf.get('BONUS', 'sas_timeout', 'int')
        self.tcp_buffer = self.conf.get('COMUNICATION', 'buffer', 'int')
        self.tcp_timeout = self.conf.get('COMUNICATION', 'timeout', 'int')
        self.tcp_ip = self.conf.get('DB_SERVER', 'ip', 'str')
        self.tcp_port = self.conf.get('DB_SERVER', 'port', 'int')
        self.pipe_clean = self.conf.get('BONUS', 'pipe_clean', 'int')
        self.crypt = kwargs['crypt']
        self.use_aft = self.conf.get('SAS', 'aft', 'bool')
        self.ip = system.get_ip()
        self.send_q = Queue()
        # try:
        #     self.LOCK.release()
        # except ValueError:
        #     pass

    def old_poll_clean(self):
        while self.pipe['sas'].poll():
            self.pipe['sas'].recv()

    def get_cart(self, cart_id, **kwargs):
        data = None
        while self.send.poll():
            self.send.recv()
        kwargs['send_time'] = time.time()
        kwargs['evt'] = 'get_bonus_cart_to_init'
        kwargs['ip'] = self.tcp_ip
        kwargs['port'] = self.tcp_port
        # kwargs['log'] = self.log
        kwargs['timeout'] = self.tcp_timeout
        kwargs['udp_buffer'] = self.tcp_buffer
        # kwargs['crypt'] = self.crypt
        kwargs['my_name'] = self.ip
        kwargs['cart_id'] = cart_id
        kwargs['send_time'] = time.time()
        try:
            data = None
            for i in range(2):
                self.send.send(kwargs)
                if self.send.poll(self.tcp_timeout + 3):
                    data = self.send.recv()
                    if data:
                        break
        except Exception as e:
            self.log.error(e, exc_info=True)
            data = None
        if not data:
            self.log.error('server not response on bonus get_cart')
        else:
            if data[1] != kwargs:
                self.log.warning('%s, %s' % (data[1], kwargs))
                data = None
            else:
                data = data[0]
        return data

    # def send_data(self, **kwargs):
    #     t = threading.Thread(target=self._send_data, kwargs=kwargs)
    #     t.start()

    def send_data(self, send_q, send, log, **kwargs):
        while True:
            kwargs = send_q.get()
            if 'myinit_time' not in kwargs:
                kwargs['myinit_time'] = time.time()

            bonus_init_time = time.time()
            my_init_time = time.time()
            kwargs['my_init_time'] = my_init_time
            kwargs['evt'] = 'bonus_init'
            kwargs['ip'] = self.tcp_ip
            kwargs['port'] = self.tcp_port
            kwargs['timeout'] = self.tcp_timeout
            kwargs['udp_buffer'] = self.tcp_buffer
            kwargs['my_name'] = self.ip
            kwargs['bonus_init_time'] = bonus_init_time
            kwargs['send_time'] = time.time()
            while True:
                while self.send.poll():
                    self.send.recv()
                data = None
                # if 'myinit_time' not in kwargs:
                #     kwargs['myinit_time'] = time.time()
                #
                # bonus_init_time = time.time()
                # kwargs['evt'] = 'bonus_init'
                # kwargs['ip'] = self.tcp_ip
                # kwargs['port'] = self.tcp_port
                # kwargs['timeout'] = self.tcp_timeout
                # kwargs['udp_buffer'] = self.tcp_buffer
                # kwargs['my_name'] = self.ip
                # kwargs['bonus_init_time'] = bonus_init_time
                # kwargs['send_time'] = time.time()
                try:
                    self.send.send(kwargs)
                    if self.send.poll(self.tcp_timeout+3):
                        data = self.send.recv()
                        if data:
                            if data[1] != kwargs:
                                data = None
                            else:
                                break
                    # self.LOCK.release()

                except Exception as e:
                    # self.LOCK.release()
                    log.error(e, exc_info=True)
                    # data = None
                # if data == None:
                #     time.sleep(2)

    def bonus_error_clean(self):
        error = self.db.get('BONUS_ERROR_LOG')
        self.db.set('BONUS_ERROR_LOG', [])
        self.bonus_error = []
        for i in range(len(error)):
            if error[i]['hold'] is False:
                if self.bonus[error[i]['bonus_id']]['model'] == 'x2_hold':
                    self.init_time = time.time() + self.sas_timeout
                    self.pipe['sas'].send(['sas.bonus_hold',
                                           {'bonus_id': error[i]['bonus_id'], 'mony': self.bonus[error[i]['bonus_id']]['mony'],
                                            'player': error[i]['player'], 'request_time': self.init_time, 'hold': True}])
                    self.pipe['sas'].recv()
                elif self.bonus[error[i]['bonus_id']]['model'] == 'static_hold':
                    self.init_time = time.time() + self.sas_timeout
                    self.pipe['sas'].send(['sas.bonus_hold',
                                           {'bonus_id': error[i]['bonus_id'],
                                            'mony': self.bonus[error[i]['bonus_id']]['mony'],
                                            'player': error[i]['player'], 'request_time': self.init_time, 'hold': True}])
                    self.pipe['sas'].recv()
                elif self.bonus[error[i]['bonus_id']]['model'] == '1x1_hold':
                    self.init_time = time.time() + self.sas_timeout
                    self.pipe['sas'].send(['sas.bonus_hold',
                                           {'bonus_id': error[i]['bonus_id'],
                                            'mony': self.bonus[error[i]['bonus_id']]['mony'],
                                            'player': error[i]['player'], 'request_time': self.init_time, 'hold': True}])
                    self.pipe['sas'].recv()
            self.log.error('clean not writet bons len %s', error[i])
            self.send_data(**error[i])
        return True

    def run_1x1(self):
        self.pipe['sas'].send(['sas.get_single_meter', {'command': 'curent credit'}])
        if self.pipe['sas'].poll(self.sas_timeout) is True:
            credit = self.pipe['sas'].recv()
            if credit != None and credit >= self.bonus[self.cart_id]['mony']:
                # self.old_poll_clean()
                self.init_time = time.time() + (self.sas_timeout-2)
                waith_to_play = time.time() + int(self.sas_timeout / 2)
                self.pipe['sas'].send(['sas.bonus', {'mony': self.bonus[self.cart_id]['mony'], 'tax': '00',
                                                     'request_time': self.init_time,
                                                     'model': self.bonus[self.cart_id]['model'],
                                                     'no_out_befor': self.bonus[self.cart_id]['mony']*2*self.bonus[self.cart_id]['no_out_befor'],
                                                     'waith_to_play':waith_to_play,
                                                     }])
                data = None
                # while True:
                if self.pipe['sas'].poll(self.sas_timeout):
                    data = self.pipe['sas'].recv()
                    self.log.debug('sas response: %s', data)
                    if data is True:
                        self.send_q.put({'bonus_id':self.cart_id, 'player':self.player_id, 'hold':False})
                        return True
                    else:
                        self.log.error('sas response run_1x1: %s', data)
                        return False

    def run_1x1_hold(self):
        self.pipe['sas'].send(['sas.get_single_meter', {'command': 'curent credit'}])
        if self.pipe['sas'].poll(self.sas_timeout) is True:
            credit = self.pipe['sas'].recv()
            if credit != None and credit >= self.bonus[self.cart_id]['mony']:
                # self.old_poll_clean()
                self.init_time = time.time() + (self.sas_timeout-2)
                waith_to_play = time.time() + int(self.sas_timeout / 2)
                self.pipe['sas'].send(['sas.bonus', {'mony': self.bonus[self.cart_id]['mony'], 'tax': '00',
                                                     'request_time': self.init_time,
                                                     'no_out_befor': self.bonus[self.cart_id]['mony']*2*self.bonus[self.cart_id]['no_out_befor'],
                                                     'waith_to_play':waith_to_play,
                                                     }])
                # data = None*self.bonus[self.cart_id]['no_out_befor']*self.bonus[self.cart_id]['no_out_befor']
                if self.pipe['sas'].poll(self.sas_timeout):
                    data = self.pipe['sas'].recv()
                    self.log.debug('sas response: %s', data)
                    if data is True:
                        self.init_time = time.time() + (self.sas_timeout-2)
                        self.pipe['sas'].send(['sas.bonus_hold', {'bonus_id': self.cart_id, 'mony': self.bonus[self.cart_id]['mony'],'player': self.player_id, 'request_time': self.init_time, 'hold':True}])
                        self.pipe['sas'].recv()
                        self.send_q.put({'bonus_id':self.cart_id, 'player':self.player_id, 'hold':False})
                        # self.send_data(bonus_id=self.cart_id, player=self.player_id, hold=False)
                        return True
                    else:
                        self.log.error('sas response run_1x1_hold: %s', data)
                        return False

    def run_1x2(self):
        # self.old_poll_clean()
        self.init_time = time.time() + (self.sas_timeout-2)
        waith_to_play = time.time() + int(self.sas_timeout / 2)
        self.pipe['sas'].send(['sas.bonus', {'mony': self.bonus[self.cart_id]['mony']*2, 'tax': '00',
                                             'request_time': self.init_time,
                                             'no_out_befor': self.bonus[self.cart_id]['mony']*2*self.bonus[self.cart_id]['no_out_befor'],
                                             'waith_to_play':waith_to_play
                                             }])
        data = None
        # while True:*self.bonus[self.cart_id]['no_out_befor']
        if self.pipe['sas'].poll(self.sas_timeout):
            data = self.pipe['sas'].recv()
            self.log.debug('sas response: %s', data)
            if data is True:
                self.send_q.put({'bonus_id': self.cart_id, 'player': self.player_id, 'hold': False})
                # self.send_data(bonus_id=self.cart_id, player=self.player_id, hold=False)
                return True
            else:
                self.log.error('sas response run_1x2: %s', data)
                return False

    def run_1x2_hold(self):
        # self.old_poll_clean()
        self.init_time = time.time() + (self.sas_timeout-2)
        waith_to_play = time.time() + int(self.sas_timeout / 2)
        self.pipe['sas'].send(['sas.bonus', {'mony': self.bonus[self.cart_id]['mony']*2, 'tax': '00',
                                             'request_time': self.init_time,
                                             'no_out_befor': self.bonus[self.cart_id]['mony']*2*self.bonus[self.cart_id]['no_out_befor'],
                                             'waith_to_play':waith_to_play,
                                             }])
        data = None
        # while True:
        if self.pipe['sas'].poll(self.sas_timeout):
            data = self.pipe['sas'].recv()
            self.log.debug('sas response: %s', data)
            if data is True:
                self.init_time = time.time() + (self.sas_timeout-2)
                self.pipe['sas'].send(['sas.bonus_hold',{'bonus_id': self.cart_id, 'mony': self.bonus[self.cart_id]['mony'],'player': self.player_id, 'request_time': self.init_time, 'hold':True}])
                self.pipe['sas'].recv()
                self.send_q.put({'bonus_id': self.cart_id, 'player': self.player_id, 'hold': False})
                # self.send_data(bonus_id=self.cart_id, player=self.player_id, hold=False)
                return True
            else:
                self.log.error('sas response run_1x2_hold: %s', data)
                return False

    def run_static(self):
        waith_to_play = time.time() + int(self.sas_timeout / 2)
        self.init_time = time.time() + (self.sas_timeout-2)
        self.pipe['sas'].send(['sas.bonus', {'mony': self.bonus[self.cart_id]['mony'], 'tax': '00',
                                             'request_time': self.init_time,
                                             'no_out_befor': self.bonus[self.cart_id]['mony']*self.bonus[self.cart_id]['no_out_befor'],
                                             'waith_to_play':waith_to_play
                                             }])
        data = None
        # while True:
        if self.pipe['sas'].poll(self.sas_timeout):
            data = self.pipe['sas'].recv()
            self.log.debug('sas response: %s', data)
            if data is True:
                self.send_q.put({'bonus_id': self.cart_id, 'player': self.player_id, 'hold': False})
                # self.send_data(bonus_id=self.cart_id, player=self.player_id, hold=False)
                return True
            else:
                self.log.error('sas response run_static: %s', data)
                return False

    def run_static_hold(self):
        # self.old_poll_clean()
        data = None
        self.init_time = time.time() + (self.sas_timeout-2)
        waith_to_play = time.time() + int(self.sas_timeout / 2)
        self.pipe['sas'].send(['sas.bonus', {'mony': self.bonus[self.cart_id]['mony'], 'tax': '00',
                                             'request_time': self.init_time,
                                             'no_out_befor': self.bonus[self.cart_id]['mony']*self.bonus[self.cart_id]['no_out_befor'],
                                             'waith_to_play':waith_to_play,
                                             }])

        # while True:
        if self.pipe['sas'].poll(self.sas_timeout):
            data = self.pipe['sas'].recv()
            self.log.debug('sas response: %s', data)
            if data is True:
                self.init_time = time.time() + (self.sas_timeout-2)
                self.pipe['sas'].send(['sas.bonus_hold', {'bonus_id': self.cart_id,'mony': self.bonus[self.cart_id]['mony'], 'player': self.player_id, 'request_time': self.init_time, 'hold':True}])
                self.pipe['sas'].recv()
                self.send_q.put({'bonus_id': self.cart_id, 'player': self.player_id, 'hold': False})
                # self.send_data(bonus_id=self.cart_id, player=self.player_id, hold=False)
                return True
            else:
                self.log.error('sas response run_static_hold: %s', data)
                return False

    def restricted(self, **kwargs):
        # self.old_poll_clean()
        self.init_time = time.time() + self.sas_timeout - 2
        waith_to_play = time.time() + int(self.sas_timeout / 2)
        self.pipe['sas'].send(['sas.bonus', {'mony': self.bonus[self.cart_id]['mony'], 'tax': '00',
                                                 'request_time': self.init_time,
                                                 'no_out_befor':1,
                                                 'restricted':True,
                                                 'waith_to_play':waith_to_play,
                                                 }])
        data = None
        # while True:
        if self.pipe['sas'].poll(self.sas_timeout):
            data = self.pipe['sas'].recv()
            self.log.debug('sas response: %s', data)
            if data is True:
                self.send_q.put({'bonus_id': self.cart_id, 'player': self.player_id, 'hold': False})
                # self.send_data(bonus_id=self.cart_id, player=self.player_id, hold=False)
                return True
            else:
                self.log.error('sas response run_static: %s', data)
                return False

    def set_my_bonus(self):
        self.old_poll_clean()
        data = None
        self.init_time = time.time() + (self.sas_timeout-2)
        if self.bonus[self.cart_id]['model'] == 'x2':
            data = self.run_1x2()
        elif self.bonus[self.cart_id]['model'] == 'static':
            data = self.run_static()
        elif self.bonus[self.cart_id]['model'] == '1x1':
            data = self.run_1x1()
        elif self.bonus[self.cart_id]['model'] == 'x2_hold':
            data = self.run_1x2_hold()
        elif self.bonus[self.cart_id]['model'] == 'static_hold':
            data = self.run_static_hold()
        elif self.bonus[self.cart_id]['model'] == '1x1_hold':
            data = self.run_1x1_hold()
        elif self.bonus[self.cart_id]['model'] == 'restricted':
            data = self.restricted()
        self.log.debug('response: %s', data)
        # self.old_poll_clean()
        return data

    def run(self):
        t = threading.Thread(target=self.send_data, args=[self.send_q, self.send, self.log])
        t.start()
        while True:


            # self.init_time = time.time() + self.sas_timeout
            try:
                self.cart_id = self.pipe['rfid'].recv()
                self.player_id = None
                self.bonus = self.get_cart(self.cart_id)
                self.log.debug('bonus %s', self.bonus)
                self.player = self.db.get('PLAYER')
                if self.bonus:
                    if self.bonus[self.cart_id]['must_have_cust'] is True or self.bonus[self.cart_id]['must_have_cust'] == 'True':
                        self.log.debug('bonus_cart player %s', self.player_id)
                        if self.player is False:
                            pass
                        elif self.player == None:
                            pass
                        else:
                            self.player_id = self.player['id']
                            self.set_my_bonus()
                    else:
                        if self.player is False:
                            pass
                        elif self.player == None:
                            pass
                        else:
                            self.player_id = self.player['id']
                        self.set_my_bonus()
            except Exception as e:
                self.log.critical(e, exc_info=True)
                time.sleep(0.1)

            while self.pipe['rfid'].poll(self.pipe_clean):
                self.log.debug('clean pipe')
                self.pipe['rfid'].recv()

            # else:
            #     self.pipe['rfid'].send(True)
