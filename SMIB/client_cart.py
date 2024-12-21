# -*- coding:utf-8 -*-
'''
Created on 27.02.2019

@author: dedal
'''
import os
from multiprocessing import Process
import log
# import json
# from pymemcache.client.base import PooledClient as mem_Client
import client
import time
from libs import system
import libs
import random
import threading
import datetime


# TODO: Четене на лична карта и попълване на информацията автоматично
# TODO: Клиентската карта е блокирана ако не се чекира личната карта по ЕГН или номер на лична карта
# TODO: Петия сандък да отваря опция за нов сандък с умножени стойности, да се заложи максимално отваряне на нов сандък
# TODO: Да се интегрира киоск. Трябва протокол за комуникация.
# TODO: Показване на активните бомби на визуализацията
# TODO: Мистериите да падат при играещи определен брой машини. Да падат в краен случай и при една играеща
# TODO: Да се смени изцяло визуализацията
# TODO: Валичноста на личната карта да стане дата на раждане и да ваци специален бонус за рожден ден
# FIXME: При аут от AFT да позволява аут ако има направен бонус?
# TODO: Да се измисли NFC и Мобилно приложение.


class ClientCart(Process):
    def __init__(self, **kwargs):
        Process.__init__(self, name='ClientCart')
        self.rtc = libs.rtc.date_format.BG(None)
        self.log = log.get_log(log.LOG_CHANEL_LEVEL['client_cart'])
        # self.current_credit_in_in = False
        self.conf = kwargs['conf']
        self.db = kwargs['db']
        self.db.set('PLAYER_DAY_ORDER', False)
        self.db.set('PLAYER_IN_NRA', False)
        # self.day_finish = False
        self.send = kwargs['send']
        self.buffer = self.conf.get('COMUNICATION', 'buffer', 'int')
        self.pipe = kwargs['pipe']
        # self.check_bonus_time = 2
        # self.games_played = 0
        self.lock_emf_if_no_cust = self.conf.get('PLAYER', 'lock_emg_if_no_cust', 'bool')
        self.lock_bill_if_no_cust = self.conf.get('PLAYER', 'lock_bill_if_no_cust', 'bool')
        self.refresh_player = False
        #         self.unix_client = unix_client.Client(address='/tmp/colibri.sock', tcp_buffer=self.buffer, log=self.log)
        self.tcp_timeout = self.conf.get('COMUNICATION', 'timeout', 'int')
        self.tcp_ip = self.conf.get('DB_SERVER', 'ip', 'str')
        self.tcp_port = self.conf.get('DB_SERVER', 'port', 'int')
        self.rfid_timeout = self.conf.get('PLAYER', 'player_timeout', 'float')
        self.logo_name = self.conf.get('PLAYER', 'logo_name', 'str')
        USE_LANGUAGE = self.conf.get('SYSTEM', 'lang', 'str')
        DISPLAY_SIZE = self.conf.get('PLAYER', 'display_size', 'int')
        self.sas_timeout = self.conf.get('PLAYER', 'sas_timeout', 'int')
        self.bonus_on_credit = self.conf.get('PLAYER', 'bonus_on_credit', 'int')
        anime_use = self.conf.get('PLAYER', 'anime_use', 'bool')
        anime_num = str(self.conf.get('PLAYER', 'anime_num', 'int'))
        skin = self.conf.get('PLAYER', 'skin', 'int')
        use_sas_aft = self.conf.get('SAS', 'aft', 'bool')

        if anime_num == '1':
            my_range = (8, 94)
        elif anime_num == '2':
            my_range = (0, 46)
        elif anime_num == '3':
            my_range = (0, 193)
        elif anime_num == '4':
            my_range = (0, 290)
        elif anime_num == '5':
            my_range = (0, 119)
        elif anime_num == '6':
            my_range = (0, 199)
        elif anime_num == '7':
            my_range = (0, 148)
        elif anime_num == '8':
            my_range = (0, 2)
        else:
            my_range = (8, 94)
            anime_num = 1
            anime_use = False

        self.down_bonus_count = 1
        self.cart = False
        self.use_touch = self.conf.get('PLAYER', 'use_touch', 'bool')
        # self.server = mem_Client(('127.0.0.1', 11211), serializer=json_serializer, deserializer=json_deserializer)
        self.server = libs.db.mem_db.MemDB()

        self.logo_name = self.conf.get('PLAYER', 'logo_name', 'str')
        self.use_aft = self.conf.get('KEYSYSTEM', 'aft', 'bool')
        self.sas_aft = self.conf.get('SAS', 'aft', 'bool')
        if self.sas_aft is False:
            self.use_aft = False
        self.bonus_warning_use = False
        self.player_get_bonus_now = False
        if self.db.get('RESET_PLAYER') is True:
            self.player = False
            self.db.set('RESET_PLAYER', False)
            self.db.set('PLAYER', self.player)
        else:
            self.player = self.db.get('PLAYER')
        self.db.set('CART_CHANGE', False)
            # if self.player is not False:
            #     self.del_player()
        if self.sas_aft is False:
            self.server.set('SHOW_OUT_BUTTON', False)
        else:
            self.server.set('SHOW_OUT_BUTTON', self.use_aft)
        self.server.set('MAKE_IN_OUT', False)
        self.crypt = kwargs['crypt']
        self.server.set('skin', skin)
        self.server.set('use_sas_aft', use_sas_aft)
        self.server.set('HALT', False)
        self.server.set('use_anime', anime_use)
        self.server.set('anime_num', anime_num)
        self.server.set('anime_range', my_range)
        self.server.set('PLAYER', self.player)
        self.server.set('PLAYER_BONUS_INIT', [])
        self.server.set('PLAYER_GET_BONUS', [])
        self.server.set('PLAYER_WON_BONUS', None)
        self.server.set('LOGO_NAME', self.logo_name)
        self.server.set('PLAYER_PLAY_BONUS_MONY', None)
        self.server.set('PLAYER_BONUS_WARNING', None)
        self.server.set('PLAYER_BONUS_REVERT', [0, 0])
        self.server.set('DISPLAY_SIZE', DISPLAY_SIZE)
        self.server.set('USE_LANGUAGE', USE_LANGUAGE)
        self.server.set('SHOW_MONYBACK_PAY', self.conf.get('PLAYER', 'show_monybeck_pay', 'bool'))
        self.server.set('MONY_BACK_PAY', False)

        self.player_bonus_warning_time = None

        # try:
        #     self.LOCK.release()
        # except ValueError:
        #     pass

        self.my_name = system.get_ip()

        if self.lock_emf_if_no_cust is True:
            self.pipe['sas'].send(['sas.get_single_meter', {'command': 'halt'}])
            if self.pipe['sas'].poll(self.sas_timeout):
                aft_data = self.pipe['sas'].recv()
        elif self.lock_bill_if_no_cust == True:
            self.pipe['sas'].send(['sas.get_single_meter', {'command': 'halt bill'}])
            if self.pipe['sas'].poll(self.sas_timeout):
                aft_data = self.pipe['sas'].recv()

    def halt(self):
        os.system('sudo halt')

    def mony_back_pay(self):
        my_mony = None
        while my_mony == None:
            my_mony = self.send_data('get_user_mony_back', id=self.player['id'])
        if my_mony < self.player['mony_back_pay']:
            del_user = None
            while del_user == None:
                del_user = self.send_data('del_monuback_user', id=self.player['id'])
            self.server.set('MONY_BACK_PAY', False)
            return
        if self.db.get('CUST_NO_AUT_BEFOR'):
            self.server.set('MONY_BACK_PAY', False)
            del_user = None
            while del_user == None:
                del_user = self.send_data('del_monuback_user', id=self.player['id'])
            return False
        if my_mony <= 0:
            self.server.set('MONY_BACK_PAY', False)
            del_user = None
            while del_user == None:
                del_user = self.send_data('del_monuback_user', id=self.player['id'])
            return False

        init_time = time.time() + (self.sas_timeout - 2)
        waith_to_play = time.time() + int(self.sas_timeout / 2)
        self.pipe['sas'].send(['sas.cust_monyback_pay',
                               {
                                   'mony': my_mony,
                                   'tax': '00',
                                   'request_time': init_time,
                                   'waith_to_play': waith_to_play,
                               }])
        if self.pipe['sas'].poll(self.sas_timeout):
            response_from_sas = self.pipe['sas'].recv()
            self.log.info('mony_back_pay: mony: %s, sas response: %s' % (my_mony, response_from_sas))
            if response_from_sas is True:
                self.get_player_meter()
                clear_bonus = None
                while clear_bonus == None:
                    clear_bonus = self.send_data('mony_back_clear', id=self.player['id'], mony=my_mony)
                self.player['total_mony_back'] = self.player['total_mony_back'] - my_mony
                self.server.set('PLAYER', self.player)
        self.server.set('MONY_BACK_PAY', False)
        return True

    def send_data(self, evt, **kwargs):

        # unlock = False
        my_init_time = time.time()
        kwargs['ip'] = self.tcp_ip
        kwargs['port'] = self.tcp_port
        # kwargs['log'] = self.log
        kwargs['timeout'] = self.tcp_timeout
        kwargs['udp_buffer'] = self.buffer
        # kwargs['crypt'] = self.crypt
        kwargs['my_name'] = self.my_name
        kwargs['my_init_time'] = my_init_time
        kwargs['evt'] = evt
        while True:
            while self.send.poll():
                self.send.recv()
            data = None
            # my_init_time = time.time()
            # kwargs['my_init_time'] = my_init_time
            kwargs['send_time'] = time.time()
            try:
                self.send.send(kwargs)
                data = None
                if self.send.poll(self.tcp_timeout+3):
                    data = self.send.recv()
                if data != None:
                    if data[1] != kwargs:
                        data = None
                    else:
                        data = data[0]
                        break
            except Exception as e:
                self.log.error('evt %s, data: %s' % (evt, kwargs))
                self.log.error(e, exc_info=True)
                data = None
            self.clean_rfid_poll()
            if data == None:
                time.sleep(1)
        # self.clean_rfid_poll()
        return data
        # return None

    def make_range(self, x2=False):
        tmp = []
        for b in self.player['bonus_row']:
            for i in range(self.player['bonus_row'][b]):
                if x2 == False:
                    tmp.append(float(b))
                else:
                    tmp.append(float(b)*2)
        if len(tmp) < 5:
            tmp = tmp * 5
        return tmp

    def make_random(self, new=False, x2=False):
        # activ_bonus = self.send_data('activ_bonus', cust_id=self.player['id'], grup=self.player['grup'])
        # if activ_bonus:
        #     tmp = [activ_bonus['mony']]*5
        # else:
        tmp = self.make_range(x2=x2)
        random.shuffle(tmp)
        if new is False:
            return random.sample(tmp, 5)
        else:
            tmp = random.sample(tmp, 4)
            tmp.append('x2')
            random.shuffle(tmp)
            return tmp

    def old_rfid_poll_clean(self):
        while True:
            if self.pipe['rfid'].poll():
                self.pipe['rfid'].recv()
            else:
                break

    def get_player_from_server(self):
        self.refresh_player = True
        data = self.db.get('SAS_METER')
        if data == None or data is False:
            self.player = False
            self.server.set('PLAYER', self.player)
            self.db.set('PLAYER', self.player)
            # self.log.error('NO COUNTERS FOR PLAYER')
            return
        elif None in data.values():
            self.player = False
            self.server.set('PLAYER', self.player)
            self.db.set('PLAYER', self.player)
            # self.log.error('NO COUNTERS FOR PLAYER')
            return
        self.player = self.send_data('get_client', cart_id=self.cart)
        # self.old_in_for_hold = 0
        # self.old_out_for_hold = 0
        # self.old_won_for_hold = 0
        # self.old_bet_for_hold = 0
        if self.player is None:
            self.player = False
            self.server.set('PLAYER', self.player)
            self.db.set('PLAYER', self.player)
        elif self.player is False:
            self.db.set('PLAYER', self.player)
            self.server.set('PLAYER', self.player)
            # time.sleep(1)
        elif self.player is True:
            self.player = False
            self.server.set('PLAYER', self.player)
            self.db.set('PLAYER', self.player)
        elif 'cart_id' not in self.player:
            self.player = False
            self.server.set('PLAYER', self.player)
            self.db.set('PLAYER', self.player)
        else:
            for i in range(3):
                if self.send_data('i_get_player', cart_id=self.cart) is True:
                    break

            self.down_bonus_count = self.player['down_bonus_count']
            # self.player['activ_bonus'] = self.send_data('activ_bonus', cust_id=self.player['id'])
            self.player['cart'] = self.cart
            self.db.set('PLAYER', self.player)
            self.server.set('PLAYER', self.player)
            if self.server.get('PLAYER_PLAY_BONUS_MONY') != self.player['id']:
                self.server.set('PLAYER_PLAY_BONUS_MONY', None)
            reserve = self.db.get('RESERVE')
            # raise KeyError, reserve
            if reserve != None:
                # raise KeyError, reserve
                if self.player['id'] == reserve['player_id'] and self.player['in_nra'] is False:
                    self.pipe['sas'].send(['sas.get_single_meter', {'command': 'start'}])
                    if self.pipe['sas'].poll(self.sas_timeout):
                        self.pipe['sas'].recv()
                        self.db.set('RESERVE', None)

            if self.lock_emf_if_no_cust is True and reserve == None and self.player['in_nra'] is False:
                aft_data = False
                while aft_data is not True:
                    self.pipe['sas'].send(['sas.get_single_meter', {'command': 'start'}])
                    if self.pipe['sas'].poll(self.sas_timeout):
                        aft_data = self.pipe['sas'].recv()
            elif self.lock_bill_if_no_cust is True and self.player['in_nra'] is False:
                aft_data = False
                while aft_data is not True:
                    self.pipe['sas'].send(['sas.get_single_meter', {'command': 'start bill'}])
                    if self.pipe['sas'].poll(self.sas_timeout):
                        aft_data = self.pipe['sas'].recv()

            if 'bonus_warning_use' in self.player:
                self.bonus_warning_use = self.player['bonus_warning_use']

            # self.db.set('PLAYER_IN_NRA', self.player['in_nra'])
            # self.server.set('PLAYER_IN_NRA', self.player['in_nra'])
            # self.log.error(self.player['in_nra'])
            if self.player['in_nra'] is True:
                self.pipe['sas'].send(['sas.get_single_meter', {'command': 'halt'}])
                if self.pipe['sas'].poll(self.sas_timeout):
                    self.pipe['sas'].recv()

    def get_player_meter(self):
        data = self.db.get('SAS_METER')
        if data == None or data == False:
            return
        elif data != None  and data is not False and 'bet' in data:
            if None in data.values():
                for i in data.keys():
                    data[i] = None
                return
            if 'old_meter' not in self.player:
                if None not in data.values():
                    self.player['old_meter'] = data
                # if self.use_aft is True and 'old_meter' in self.player:
                #     # self.player['old_meter'] = data
                #     if self.player['curent_mony'] > 0:
                #         mony = self.send_data('get_player_mony', player_id=self.player['id'])
                #         if mony > 0:
                #             clean_mony = self.send_data('clean_current_mony', player_id=self.player['id'])
                #             if clean_mony is True:
                #                 init_time = time.time() + (self.sas_timeout - 2)
                #
                #                 while True:
                #                     self.pipe['sas'].send(['sas.add_in_to_emg',
                #                                            {'mony': self.player['curent_mony'], 'amount': 1,
                #                                             'init_time': init_time, 'request_time': init_time}])
                #                     if self.pipe['sas'].poll(self.sas_timeout):
                #                         aft_response = self.pipe['sas'].recv()
                #                         # raise KeyError, aft_response
                #                     if aft_response == None or aft_response is False:
                #                         self.pipe['sas'].send(['sas.clean_transaction_poll', {}])
                #                         aft_response = None
                #                     elif aft_response['Transfer status'] == 'Full transfer successful':
                #                         server_response = self.send_data('aft_in', cust_id=self.player['id'],
                #                                                          mony=self.player['curent_mony'])
                #                         while server_response is not True:
                #                             server_response = self.send_data('aft_in',
                #                                                              cust_id=self.player['id'],
                #                                                              mony=self.player['curent_mony'])
                #                         self.player['old_meter']['in'] += self.player['curent_mony']
                #                         self.player['curent_mony'] = 0
                #                         break
                #                     else:
                #                         aft_response = None
                #         else:
                #             self.log.warning('current player mony: %s', mony)
                #             self.player['curent_mony'] = mony
            if self.player['old_meter']['bet'] > data['bet']:
                data['bet'] = 999999.99
                self.player['new_meter'] = data
                self.set_player_to_server()
                return
            elif self.player['old_meter']['in'] > data['in']:
                data['in'] = 999999.99
                self.player['new_meter'] = data
                self.set_player_to_server()
                return
            elif self.player['old_meter']['out'] > data['out']:
                data['out'] = 999999.99
                self.player['new_meter'] = data
                self.set_player_to_server()
                return
            elif self.player['old_meter']['won'] > data['won']:
                data['won'] = 999999.99
                self.player['new_meter'] = data
                self.set_player_to_server()
                return
            else:
                self.player['new_meter'] = data
            self.server.set('PLAYER', self.player)
            self.log.debug('credit %s, bonus_on_credit %s' % (self.player['new_meter']['curent credit'], self.bonus_on_credit))
            self.db.set('PLAYER', self.player)
            if self.db.get('PLAYER_IN_NRA') == False:
                self.db.set('PLAYER_IN_NRA', self.player['in_nra'])
                self.server.set('PLAYER_IN_NRA', self.player['in_nra'])
            if self.server.get('MAKE_IN_OUT'):
                if self.player['new_meter']['curent credit'] > 0:
                    data = self.out_from_emg()
                elif self.player['curent_mony'] > 0:
                    data = self.get_in_to_emg()
                else:
                    data = self.out_from_emg()
                # if data:
                self.server.set('MAKE_IN_OUT', False)
            elif self.server.get('MONY_BACK_PAY'):
                self.mony_back_pay()
            if self.bonus_warning_use is True:
                self.bonus_warning_f()

    def bonus_warning_f(self):
        self.log.debug('bonus_warning_use in self.player: %s', self.player)
        self.log.debug('self.player[bonus_warning_use] %s', self.player['bonus_warning_use'])
        self.log.debug('self.bonus_warning_use %s', self.bonus_warning_use)
        # if 'bonus_warning_use' in self.player:
        # raise KeyError, self.player['bonus_warning_initial']
        if self.bonus_warning_use is True and self.player['bonus_warning_initial'] is True:
            ins = round((self.player['new_meter']['in'] - self.player['old_meter']['in']), 2)
            # bet += self.player['old_meter']['curent credit']
            self.log.debug('in %s', ins)
            out = round(self.player['new_meter']['out'] - self.player['old_meter']['out'], 2)
            self.log.debug('out %s', out)
            total = round(ins - out, 2)
            total += self.player['full_total']
            self.log.info('total %s', total)
            self.log.info(' total >= self.player[bonus_warning_mony] %s',
                           total >= self.player['bonus_warning_mony'])
            if total >= self.player['bonus_warning_mony'] and self.player['new_meter']['curent credit'] <= self.bonus_on_credit:
                response = self.send_data('chk_for_bonus_warning', player_id=self.player['id'])
                # if response == None:
                #     response = self.send_data('chk_for_bonus_warning', player_id=self.player['id'])
                if response is True:
                    #
                    self.log.info('response %s', response)
                    self.bonus_warning_use = False
                    self.server.set('PLAYER_BONUS_WARNING', True)
                    self.player_bonus_warning_time = time.time()
                    self.player['bonus_warning_initial'] = False
                else:
                    self.bonus_warning_use = False
                    self.player_bonus_warning_time = None

    def set_player_to_server(self):

        while True:
            if 'old_meter' in self.player and 'new_meter' in self.player:
                if None not in self.player['new_meter'].values():
                    data = self.send_data('set_client', player=self.player)
                else:
                    data = False
                if data is True:
                    # self.player = False
                    # self.server.set('PLAYER', self.player)
                    # self.db.set('PLAYER', self.player)
                    break
                else:
                    self.log.info('set client response %s', str(data))
                    self.get_player_meter()
            else:
                self.get_player_meter()
        self.player = False
        # if end_date is not False:
        #     self.day_finish = True
        self.server.set('PLAYER', self.player)
        self.db.set('PLAYER', self.player)
        self.server.set('PLAYER_BONUS_INIT', [])
        self.server.set('PLAYER_GET_BONUS', [])
        self.server.set('PLAYER_WON_BONUS', None)
        self.server.set('PLAYER_BONUS_WARNING', None)
        # self.server.set('PLAYER_BONUS_REVERT', [0, 0])
        self.player_bonus_warning_time = None
        self.player_get_bonus_now = False
        self.down_bonus_count = 1

    def get_in_to_emg(self):
        aft_data = None

        if self.use_aft is not True:
            return True
        if self.sas_aft is False:
            return True
        if self.db.get('RESERVE') is not None:
            return True
        if self.db.get('CUST_NO_AUT_BEFOR'):
            return

        mony = self.send_data('get_player_mony', player_id=self.player['id'])
        if mony <= 0:
            return True
        clean_mony = None
        while True:
            clean_mony = self.send_data('clean_current_mony', player_id=self.player['id'], out=False, mony=mony)
            if clean_mony:
                break
        self.clean_sas_poll()
        waith_to_play = time.time() + ((self.sas_timeout - 2) / 2)
        init_time = time.time() + (self.sas_timeout - 2)
        self.pipe['sas'].send(
                ['sas.add_in_to_emg', {'init_time': init_time, 'request_time': init_time, 'mony':mony, 'waith_to_play':waith_to_play}])
        if self.pipe['sas'].poll(self.sas_timeout):
            aft_data = self.pipe['sas'].recv()
            self.log.info('aft data %s', aft_data)
            if not aft_data:
                self.log.warning('get_in_from_emg %s', aft_data)
            elif aft_data['Transfer status'] == 'Full transfer successful' or aft_data['Transfer status'] == 'Transfer pending (not complete)':
                self.log.info('get_in_from_emg %s', aft_data)
                self.log.info('%s', self.player)
                self.player['curent_mony'] = 0
                return True
            else:
                self.log.warning('get_in_from_emg %s', aft_data)
        data = None
        while not data:
            data = self.send_data('revert_current_mony', my_id=clean_mony[1])
        self.player['curent_mony'] = mony
        # self.server.set('MAKE_IN_OUT', False)
        # clean_mony = self.send_data('revert_current_mony', player_id=self.player['id'], out=False, mony=mony)
        return False

    def out_from_emg(self):
        aft_data = None

        if self.use_aft is not True:
            return True
        if self.sas_aft is False:
            return True
        if 'new_meter' not in self.player:
            return True
        # self.log.error('client mod %s', self.db.get('CUST_NO_AUT_BEFOR'))
        # data = self.db.get('CUST_NO_AUT_BEFOR')
        # if self.db.get('CUST_NO_AUT_BEFOR'):
        #     return
        crupie_bonus_hold = self.send_data('get_croupie_bonus_hold')
        self.clean_sas_poll()
        init_time = time.time() + (self.sas_timeout - 2)
        waith_to_play = time.time() + ((self.sas_timeout - 2) / 2)
        self.pipe['sas'].send(
            ['sas.get_out_from_emg',
             {'forbiden': True, 'init_time': init_time, 'request_time': init_time, 'waith_to_play': waith_to_play, 'croupie_bonus_hold':crupie_bonus_hold}])
        if self.pipe['sas'].poll(self.sas_timeout):
            aft_data = self.pipe['sas'].recv()
            self.log.info('aft data %s', aft_data)
            if aft_data == 'NO OUT':
                return True
            if aft_data is False:
                self.log.warning('get_out_from_emg %s', aft_data)
                return False
            elif aft_data == None:
                self.log.warning('get_out_from_emg %s', aft_data)
                return False
            elif aft_data['Transfer status'] == 'Full transfer successful' or aft_data[
                'Transfer status'] == 'Transfer pending (not complete)':
                self.log.info('get_out_from_emg %s', aft_data)
                self.log.info('%s', self.player)
                clean_mony = None
                while True:
                    clean_mony = self.send_data('clean_current_mony', player_id=self.player['id'], out=True,
                                                mony=round(float(aft_data['Cashable amount']), 2))
                    if clean_mony:
                        break
                self.player['curent_mony'] = clean_mony[0]
                return True
            elif aft_data['Transfer status'] == 'Gaming machine unable to perform transfers at this time (door open, tilt, disabled, cashout in progress, etc.)':
                self.clean_sas_poll()
                init_time = time.time() + (self.sas_timeout - 2)
                waith_to_play = time.time() + ((self.sas_timeout - 2) / 2)
                self.pipe['sas'].send(
                    ['sas.get_single_meter',
                     {'forbiden': True, 'init_time': init_time, 'request_time': init_time,
                      'command': 'player_reset_hand_pay', 'waith_to_play':waith_to_play}])
                if self.pipe['sas'].poll(self.sas_timeout):
                    data = self.pipe['sas'].recv()
                    self.log.info('player_reset_hand_pay %s', data)
                    if not data:
                        return False
                    elif data > 0:
                        clean_mony = None
                        while True:
                            clean_mony = self.send_data('clean_current_mony', player_id=self.player['id'], out=True,
                                                        mony=round(float(data), 2))
                            if clean_mony:
                                break
                        self.player['curent_mony'] = clean_mony[0]
                        return True
            else:
                self.log.warning('get_out_from_emg %s', aft_data)
            return False

    def clean_sas_poll(self):
        while self.pipe['sas'].poll():
            self.pipe['sas'].recv()

    def clean_rfid_poll(self):
        while self.pipe['rfid'].poll():
            self.pipe['rfid'].recv()

    def set_bonus(self, mony):
        self.get_player_meter()
        response_from_sas = False
        set_first_request = True
        # self.clean_rfid_poll()
        # sas_timeout = 30
        # bill_stop = False
        if self.player['bonus_waith_for_in'] is True:
            # if self.player['new_meter']['curent credit'] >= mony:
            # hold_mony = mony * 2 * self.player['no_out_befor']
            if self.player['bonus_waith_for_in_mony'] <= 0:
                hold_mony = mony * 2 * self.player['no_out_befor'] + (self.player['new_meter']['curent credit'] - mony)
            else:
                hold_mony = (mony + self.player['bonus_waith_for_in_mony']) * self.player['no_out_befor'] + (self.player['new_meter']['curent credit']-self.player['bonus_waith_for_in_mony'])
        else:
            hold_mony = mony * self.player['no_out_befor'] + self.player['new_meter']['curent credit']
        if self.player['no_out_befor'] <= 1 or self.sas_aft is False:
            hold_mony = None
            # show_out = None
        # if self.player['no_out_befor'] > 1:
        #     self.pipe['sas'].send(['sas.get_single_meter', {'command': 'disable bill', 'request_time': time.time() + (self.sas_timeout - 2)}])
        #     if self.pipe['sas'].poll(self.sas_timeout):
        #         tmp = self.pipe['sas'].recv()
        #         self.log.info('halt bill if set_bonus: %s', tmp)
        # bill_stop = True
        if self.player['bonus_hold'] is True:
            hold_bonus = {
                'cust_id': self.player['id'],
                'mony': mony,
                'bonus': mony,
                'bonus_waith_for_in': self.player['bonus_waith_for_in']
            }
            # if bill_stop is False:
            #     if self.player['bonus_hold'] is True:
            #         self.pipe['sas'].send(['sas.get_single_meter', {'command': 'disable bill',
            #                                                         'request_time': time.time() + (
            #                                                                     self.sas_timeout - 2)}])
            #         if self.pipe['sas'].poll(self.sas_timeout):
            #             tmp = self.pipe['sas'].recv()
            #             self.log.warning('halt bill if wait_for_in: %s', tmp)
        else:
            hold_bonus = None
        block_out = None
        if self.player['bonus_revert_by_bet'] is True and self.player['no_out_befor'] > 1 and self.sas_aft is True:
            block_out = {'bonus_revert_by_bet': self.player['bonus_revert_by_bet'], 'mony': mony,
                                    'no_out_befor': hold_mony, 'in':self.player['bonus_waith_for_in'], 'old_credit':self.player['new_meter']['curent credit']}
            # if self.pipe['sas'].poll(self.sas_timeout):
            #     self.pipe['sas'].recv()
            self.log.info('%s', [hold_mony, self.player['new_meter']['bet']])
            # self.server.set('PLAYER_BONUS_REVERT', [hold_mony, self.player['new_meter']['bet']])
        elif self.player['bonus_revert_by_bet'] is False and self.player['no_out_befor'] > 1 and self.sas_aft is True:
            if self.player['bonus_waith_for_in'] is True:
                block_out = {'bonus_revert_by_bet': self.player['bonus_revert_by_bet'],
                                        'mony': mony, 'no_out_befor': hold_mony, 'in':self.player['bonus_waith_for_in'], 'old_credit':self.player['new_meter']['curent credit']}
                # if self.pipe['sas'].poll(self.sas_timeout):
                #     self.pipe['sas'].recv()
                # self.server.set('PLAYER_BONUS_REVERT', hold_mony)
            else:
                block_out = {'bonus_revert_by_bet': self.player['bonus_revert_by_bet'],
                                        'mony': mony, 'no_out_befor': hold_mony, 'in':self.player['bonus_waith_for_in'], 'old_credit':self.player['new_meter']['curent credit']}
                # if self.pipe['sas'].poll(self.sas_timeout):
                #     self.pipe['sas'].recv()
                # self.server.set('PLAYER_BONUS_REVERT',
                #                 hold_mony + self.player['new_meter']['curent credit'])
        else:
            block_out = None
        self.server.set('PLAYER_PLAY_BONUS_MONY', self.player['id'])
        self.clean_sas_poll()
        set = True
        while True:
            self.clean_rfid_poll()
            self.server.set('MAKE_IN_OUT', False)
            if self.player['bonus_one_per_day'] is True:
                last_bonus = self.send_data('open_in_other_device_bonus', cust_id=self.player['id'], grup=self.player['grup'])
                if last_bonus != None:
                    if last_bonus is True:
                        self.player['activ_bonus'] = False
                        self.server.set('PLAYER_BONUS_INIT', [])
                        self.server.set('PLAYER_GET_BONUS', [])
                        self.server.set('PLAYER_WON_BONUS', None)
                        self.server.set('PLAYER_BONUS_REVERT', [0, 0])
                        self.player_get_bonus_now = False
                        return False
                else:
                    last_bonus = False
            if set_first_request is True and last_bonus is False:
                set_first_request = False
                if self.player['bonus_one_per_day'] is True:
                    if last_bonus == None:
                        pass
                    else:
                        init_time = time.time() + (self.sas_timeout - 2)
                        waith_to_play = time.time() + int(self.sas_timeout / 2)
                        self.pipe['sas'].send(['sas.client_bonus',
                                               {'no_out_befor': hold_mony,
                                                'mony': mony,
                                                'bonus_revert_by_bet': self.player['bonus_revert_by_bet'],
                                                'tax': '00',
                                                'request_time': init_time,
                                                'bonus_waith_for_in': self.player['bonus_waith_for_in'],
                                                'restricted': self.player['restricted_bonus'],
                                                'out': self.player['new_meter']['out'],
                                                'waith_to_play':waith_to_play,
                                                'hold_bonus':hold_bonus,
                                                'block_out':block_out,
                                                'set': set,
                                                }])
                else:
                    init_time = time.time() + (self.sas_timeout - 2)
                    waith_to_play = time.time() + int(self.sas_timeout / 2)
                    self.pipe['sas'].send(['sas.client_bonus',
                                           {'no_out_befor': hold_mony,
                                            'mony': mony,
                                            'bonus_revert_by_bet': self.player['bonus_revert_by_bet'],
                                            'tax': '00',
                                            'request_time': init_time,
                                            'bonus_waith_for_in': self.player['bonus_waith_for_in'],
                                            'restricted': self.player['restricted_bonus'],
                                            'out': self.player['new_meter']['out'],
                                            'waith_to_play': waith_to_play,
                                            'hold_bonus': hold_bonus,
                                            'block_out': block_out,
                                            'set': set,
                                            }])
            if self.pipe['sas'].poll(self.sas_timeout):
                response_from_sas = self.pipe['sas'].recv()
                self.log.info('mony: %s, sas response: %s' % (mony, response_from_sas))
                if response_from_sas is True:
                    # if self.player['bonus_hold'] is True:
                    #     self.player['bonus_hold'] = hold_mony
                    # self.old_in_for_hold = self.player['new_meter']['in']
                    # self.old_out_for_hold = self.player['new_meter']['out']
                    # self.old_bet_for_hold = self.player['new_meter']['bet']
                    # self.old_won_for_hold = self.player['new_meter']['won']


                    # self.get_player_meter()
                    # self.log.error('%s, %s, %s' % (self.player['bonus_revert_by_bet'] is True, self.player['no_out_befor'] > 1, self.sas_aft is True))
                    self.get_player_meter()
                    if self.player['bonus_revert_by_bet'] is True and self.player['no_out_befor'] > 1 and self.sas_aft is True:
                        # self.pipe['sas'].send(['no_out_befor',
                        #                        {'bonus_revert_by_bet': self.player['bonus_revert_by_bet'], 'mony': mony,
                        #                         'no_out_befor': hold_mony}])
                        # if self.pipe['sas'].poll(self.sas_timeout):
                        #     self.pipe['sas'].recv()
                        # self.log.info('%s', [hold_mony, self.player['new_meter']['bet']])
                        self.server.set('PLAYER_BONUS_REVERT', [hold_mony, self.player['new_meter']['bet']])
                    elif self.player['bonus_revert_by_bet'] is False and self.player['no_out_befor'] > 1 and self.sas_aft is True:
                            self.server.set('PLAYER_BONUS_REVERT', hold_mony)
                    else:
                        self.server.set('PLAYER_BONUS_REVERT', hold_mony)
                    if self.player['bonus_one_per_day'] is False:
                        self.player['full_total'] -= mony
                    # if self.player['bonus_waith_for_in'] is True and self.player['bonus_hold'] is True:
                    if self.player['no_out_befor'] > 1:
                        self.stop_bill()
                    return True
                elif response_from_sas == 'CONTINUE':
                    set = False

                elif response_from_sas == 'BREAK':
                    self.player['activ_bonus'] = False
                    self.server.set('PLAYER_BONUS_INIT', [])
                    self.server.set('PLAYER_GET_BONUS', [])
                    self.server.set('PLAYER_WON_BONUS', None)
                    self.server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.player_get_bonus_now = True
                    self.server.set('PLAYER_PLAY_BONUS_MONY', None)
                    # self.clean_rfid_poll()
                    return False
                elif response_from_sas == 'ERROR':
                    # self.player['activ_bonus'] = False
                    self.server.set('PLAYER_BONUS_INIT', [])
                    self.server.set('PLAYER_GET_BONUS', [])
                    # self.server.set('PLAYER_WON_BONUS', None)
                    self.server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.server.set('PLAYER_PLAY_BONUS_MONY', None)
                    # self.clean_rfid_poll()
                    return False
                else:
                    self.log.info('try again')
                    if self.player['bonus_one_per_day'] is True:
                        last_bonus = self.send_data('open_in_other_device_bonus', cust_id=self.player['id'], grup=self.player['grup'])
                        if last_bonus == None:
                            pass

                        elif last_bonus is True:
                            self.player['activ_bonus'] = False
                            self.server.set('PLAYER_BONUS_INIT', [])
                            self.server.set('PLAYER_GET_BONUS', [])
                            self.server.set('PLAYER_WON_BONUS', None)
                            self.server.set('PLAYER_BONUS_REVERT', [0, 0])
                            self.player_get_bonus_now = False
                            # self.clean_rfid_poll()
                            return False
                        else:
                            init_time = time.time() + (self.sas_timeout - 2)
                            waith_to_play = time.time() + int(self.sas_timeout / 2)
                            self.pipe['sas'].send(['sas.client_bonus',
                                                   {'no_out_befor': hold_mony,
                                                    'mony': mony,
                                                    'bonus_revert_by_bet': self.player['bonus_revert_by_bet'],
                                                    'tax': '00',
                                                    'request_time': init_time,
                                                    'bonus_waith_for_in': self.player['bonus_waith_for_in'],
                                                    'restricted': self.player['restricted_bonus'],
                                                    'out': self.player['new_meter']['out'],
                                                    'waith_to_play': waith_to_play,
                                                    'hold_bonus': hold_bonus,
                                                    'block_out': block_out,
                                                    'set': set,
                                                    }])
                    else:
                        init_time = time.time() + (self.sas_timeout - 2)
                        waith_to_play = time.time() + int(self.sas_timeout / 2)
                        last_bonus = self.send_data('open_in_other_device_bonus', cust_id=self.player['id'],
                                                    grup=self.player['grup'])
                        if last_bonus == None:
                            pass

                        elif last_bonus is True:
                            self.player['activ_bonus'] = False
                            self.server.set('PLAYER_BONUS_INIT', [])
                            self.server.set('PLAYER_GET_BONUS', [])
                            self.server.set('PLAYER_WON_BONUS', None)
                            self.server.set('PLAYER_BONUS_REVERT', [0, 0])
                            self.player_get_bonus_now = False
                            # self.clean_rfid_poll()
                            return False
                        else:
                            self.pipe['sas'].send(['sas.client_bonus',
                                               {'no_out_befor': hold_mony,
                                                'mony': mony,
                                                'bonus_revert_by_bet': self.player['bonus_revert_by_bet'],
                                                'tax': '00',
                                                'request_time': init_time,
                                                'bonus_waith_for_in': self.player['bonus_waith_for_in'],
                                                'restricted': self.player['restricted_bonus'],
                                                'out': self.player['new_meter']['out'],
                                                'waith_to_play': waith_to_play,
                                                'hold_bonus': hold_bonus,
                                                'block_out': block_out,
                                                'set':set,
                                                }])
        return False

    def update_bonus(self, id):
        response_bonus_want = self.send_data('activ_bonus_update', bonus_id=id, aft=self.use_aft,
                                             clean_all=self.player['bonus_one_per_day'])
        while response_bonus_want is not True:
            response_bonus_want = self.send_data('activ_bonus_update', bonus_id=id, aft=self.use_aft,
                                                 clean_all=self.player['bonus_one_per_day'])
        self.player['activ_bonus'] = None
        return True

    def chk_for_bonus(self):
        my_time = datetime.datetime.now()
        if my_time.year <= 2010:
            self.log.critical('DATETIME ERROR: %s', my_time.year)
            return False

        if self.player['new_meter']['curent credit'] <= self.bonus_on_credit and self.refresh_player is False:
            self.refresh_player = True
            ins = round(
                (self.player['new_meter']['in'] - self.player['old_meter']['in']) + self.player['old_meter'][
                    'curent credit'], 2)
            out = round(self.player['new_meter']['out'] - self.player['old_meter']['out'], 2)
            total = ins - out
            data = self.send_data('get_client', reset_group=total, **self.player)
            data['new_meter'] = self.player['new_meter']
            data['old_meter'] = self.player['old_meter']
            data['come_on_emg_time'] = self.player['come_on_emg_time']
            self.player = data
            self.player['cart'] = self.cart
            if not self.player['bonus_use']:
                return False
        elif self.player['new_meter']['curent credit'] > self.bonus_on_credit:
            self.refresh_player = False
        if self.player['bonus_use'] is False:
            return False

        if 'new_meter' in self.player and 'old_meter' in self.player:
            if None not in self.player['new_meter'].values() and None not in self.player['old_meter'].values():
                if self.player['bonus_on_day'] is not True:
                    self.player_get_bonus_now = True
                    return False
                elif self.player['bonus_direct'] is True:
                    if self.player['bonus_one_per_day'] is True:
                        last_bonus = self.player['last_bonus']
                        if last_bonus is True:
                            self.player_get_bonus_now = True
                            return False
                        else:
                            # if self.player['bonus_one_per_day'] is True:
                            last_bonus = self.send_data('last_bonus', cust_id=self.player['id'],
                                                        grup=self.player['grup'])
                            if last_bonus == None:
                                return False
                            if last_bonus is True:
                                self.player_get_bonus_now = True
                                self.player['last_bonus'] = True
                                return False
                            return True
                elif self.player['bonus_by_in'] is True:
                    if 'one_day_back_total' in self.player:
                        if self.player['one_day_back_total'] is True or self.player['mount_total'] is True:

                            # last_bonus = self.player['last_bonus']
                            if self.player['last_bonus'] is True:
                                self.log.info('player have bonus')
                                self.player_get_bonus_now = True
                                return False
                            else:
                                last_bonus = self.send_data('last_bonus', cust_id=self.player['id'],
                                                            grup=self.player['grup'])
                                if last_bonus is True:
                                    self.log.info('player have bonus')
                                    self.player_get_bonus_now = True
                                    self.player['last_bonus'] = True
                                    return False
                                if last_bonus == None:
                                    return False
                            if self.player['full_total'] >= self.player['bonus_on_mony']:
                                return True
                            else:
                                self.log.info('player bad old total %s' % (str(self.player['full_total'])))
                                self.player_get_bonus_now = True
                                return False
                    # if 'mount_total' in self.player
                    ins = round(
                        (self.player['new_meter']['in'] - self.player['old_meter']['in']) + self.player['old_meter'][
                            'curent credit'], 2)
                    out = round(self.player['new_meter']['out'] - self.player['old_meter']['out'], 2)
                    # if won == None :
                    won = round(self.player['new_meter']['won'] - self.player['old_meter']['won'], 2)
                    bet = round(self.player['new_meter']['bet'] - self.player['old_meter']['bet'], 2)
                    total = round(ins - out, 2)
                    if self.player['new_meter']['curent credit'] > self.bonus_on_credit:
                        self.log.info('credit %s > bonus_on_credit %s' % (
                            self.player['new_meter']['curent credit'], self.bonus_on_credit))
                        return False
                    if won > bet:
                        self.log.info('won > bet won: %s bet: %s ' % (won, bet))
                        return False

                    if round(bet - won, 2) != round(total - self.player['new_meter']['curent credit'], 2):
                        self.log.info('bet: %s-won %s != total %s ' % (
                            bet, won, total - self.player['new_meter']['curent credit']))
                        return False

                    total += self.player['full_total']
                    if round(total / self.down_bonus_count, 2) < self.player['bonus_on_mony']:
                        self.log.info('full_total %s < bonus_on_mony %s' % (total, self.player['bonus_on_mony']))
                        return False

                    else:
                        if self.player['bonus_one_per_day'] is True:
                            last_bonus = self.player['last_bonus']
                            if last_bonus is True:
                                self.log.info('player have bonus')
                                self.player_get_bonus_now = True
                                return False
                            else:
                                self.log.info('total for bonus: %s curent credit: %s' % (
                                    round(total / self.down_bonus_count, 2), self.player['new_meter']['curent credit']))
                                self.player_get_bonus_now = True
                                # if self.player['bonus_one_per_day'] is True:
                                last_bonus = self.send_data('last_bonus', cust_id=self.player['id'],
                                                            grup=self.player['grup'])
                                if last_bonus == None:
                                    return False
                                if last_bonus is True:
                                    self.player_get_bonus_now = True
                                    self.player['last_bonus'] = True
                                    return False
                                self.get_player_meter()
                                won = round(self.player['new_meter']['won'] - self.player['old_meter']['won'], 2)
                                bet = round(self.player['new_meter']['bet'] - self.player['old_meter']['bet'], 2)
                                if won > bet:
                                    return False
                                elif self.player['new_meter']['curent credit'] > self.bonus_on_credit:
                                    return False
                                return True
                        elif self.player['bonus_one_per_day'] is False:
                            if round(total / self.down_bonus_count, 2) >= self.bonus_on_credit:
                                last_bonus = self.send_data('last_bonus', cust_id=self.player['id'], count=True)
                                self.down_bonus_count += 1
                                self.log.info('total for bonus: %s curent credit: %s count: %s' % (
                                    round(total / self.down_bonus_count, 2), self.player['new_meter']['curent credit'],
                                    self.down_bonus_count))
                                return True
                            return False
                else:
                    bet = self.player['new_meter']['bet'] - self.player['old_meter']['bet']
                    if bet / self.down_bonus_count >= self.player['bonus_on_mony']:
                        if self.player['bonus_one_per_day'] is True:
                            last_bonus = self.player['last_bonus']
                            if last_bonus is True:
                                self.log.info('player have bonus')
                                self.player_get_bonus_now = True
                                return False
                            else:
                                last_bonus = self.send_data('last_bonus', cust_id=self.player['id'],
                                                            grup=self.player['grup'])
                                if last_bonus == None:
                                    return False
                                if last_bonus is True:
                                    self.player_get_bonus_now = True
                                    self.player['last_bonus'] = True
                                    return False
                        else:
                            self.log.info('bet for bonus: bet %s, count %s bonus_mony %s' % (
                                bet, self.down_bonus_count, self.player['bonus_on_mony']))
                            if bet / self.down_bonus_count >= self.player['bonus_on_mony']:
                                self.down_bonus_count += 1
                                return True
                        return False
                return False

        return False

    def start_bill(self):
        # if self.player['bonus_hold'] is True:
        self.pipe['sas'].send(['sas.get_single_meter', {'command': 'enable bill', 'request_time': time.time() + (self.sas_timeout - 2)}])
        if self.pipe['sas'].poll(self.sas_timeout):
            tmp = self.pipe['sas'].recv()
            self.log.info('start bill if wait_for_in: %s', tmp)

    def stop_bill(self):
        self.pipe['sas'].send(['sas.get_single_meter', {'command': 'disable bill', 'request_time': time.time() + (self.sas_timeout - 2)}])
        if self.pipe['sas'].poll(self.sas_timeout):
            tmp = self.pipe['sas'].recv()
            self.log.info('halt bill if wait_for_in: %s', tmp)
    def wait_for_in(self, mony, old_in=None):
        if self.player['bonus_waith_for_in'] is True:
            old_in = None
            while True:
                data = self.db.get('SAS_METER')
                try:
                    if old_in == None:

                        if data != None:
                            # if my_data['games played']+1 > self.player['new_meter']['games played']:
                            # raise KeyError, (my_data['games played'], self.player['new_meter']['games played'])
                            old_in = data['in']
                            # else:
                            #     old_in = self.player['new_meter']['in']
                except Exception as e:
                    old_in = None
                    self.log.warning(e, exc_info=True)

                # self.clean_rfid_poll()
                cart = self.get_cart()
                # self.log.error('%s', cart)
                if cart is False:
                    self.server.set('PLAYER_BONUS_INIT', [])
                    self.server.set('PLAYER_GET_BONUS', [])
                    self.server.set('PLAYER_WON_BONUS', None)
                    # self.server.set('PLAYER_BONUS_REVERT', [0, 0])
                    # self.start_bill()
                    return 'ERROR'
                elif cart != self.player['cart']:
                    self.server.set('PLAYER_BONUS_INIT', [])
                    self.server.set('PLAYER_GET_BONUS', [])
                    self.server.set('PLAYER_WON_BONUS', None)
                    # self.server.set('PLAYER_BONUS_REVERT', [0, 0])
                    # self.start_bill()
                    return 'ERROR'
                # data = self.db.get('SAS_METER')
                if data is not None and old_in is not None:
                    if None not in data.values():
                        self.log.info('bonus_waith_for_in in: %s, mony:%s credit:%s' % (data['in'] - old_in, mony, data['curent credit']))
                        if data['in'] - old_in >= mony and data['curent credit'] >= mony:
                            self.player['new_meter'] = data
                            time.sleep(1)
                            return True
            else:
                # self.start_bill()
                return False
        else:
            # self.start_bill()
            return True
        # self.start_bill()
        return False

    def get_cart(self):
        self.clean_rfid_poll()
        if self.pipe['rfid'].poll(self.rfid_timeout):
            self.cart = self.pipe['rfid'].recv()
            self.log.debug('%s', self.cart)
            # return self.cart
        else:
            self.cart = False
        return self.cart

    def del_player(self):
        if self.db.get('PLAYER_IN_NRA') is True:
            return
        if self.db.get('CUST_NO_AUT_BEFOR'):
            return
        self.server.set('PLAYER_IN_NRA', self.db.get('PLAYER_IN_NRA'))
        # else:
        #     self.server.set('PLAYER_IN_NRA', self.db.get('PLAYER_IN_NRA'))
        # FIXME: Да не премахва клиента без кешаут
        self.get_player_meter()
        if self.player['new_meter']['curent credit'] > self.bonus_on_credit:
            return False
        # else:
        #     # if self.player['bonus_hold'] is not False and self.player['bonus_hold'] is not True:
        #     self.bonus_hold_check(check=False)
        self.set_player_to_server()
        if self.lock_emf_if_no_cust is True:
            # self.db.set('PLAYER_IN_NRA', False)
            self.pipe['sas'].send(['sas.get_single_meter', {'command': 'halt'}])
            if self.pipe['sas'].poll(self.sas_timeout):
                self.pipe['sas'].recv()
        elif self.lock_bill_if_no_cust is True:
            aft_data = False
            while aft_data is not True:
                self.pipe['sas'].send(['sas.get_single_meter', {'command': 'halt bill'}])
                if self.pipe['sas'].poll(self.sas_timeout):
                    aft_data = self.pipe['sas'].recv()

        # else:
        #     self.db.set('PLAYER_IN_NRA', False)
        #     if self.player['in_nra'] is True:
        #         self.pipe['sas'].send(['sas.get_single_meter', {'command': 'start', 'request_time': time.time()}])
        #         if self.pipe['sas'].poll(self.sas_timeout):
        #             self.pipe['sas'].recv()

        # self.old_in_for_hold = 0
        # self.old_out_for_hold = 0
        self.refresh_player = False
        self.db.set('PLAYER_DAY_ORDER', False)
        # self.server.set('MAKE_IN_OUT', False)
        return True

    def run(self):
        while True:
            try:
                if self.server.get('HALT') is True:
                    self.halt()
                    return
                self.get_cart()

                reserve = self.db.get('RESERVE')
                if reserve != None:
                    # raise KeyError, reserve
                    if datetime.datetime.now() >= self.rtc.str_to_date(reserve['datetime'], '%d.%m.%Y %H:%M'):
                        self.pipe['sas'].send(['sas.get_single_meter', {'command': 'start'}])
                        if self.pipe['sas'].poll(self.sas_timeout):
                            self.pipe['sas'].recv()
                            self.db.set('RESERVE', None)

                if self.cart is not False and self.player == None:
                    self.get_player_from_server()
                elif self.cart is not False and self.player is False:
                    self.get_player_from_server()
                elif self.cart is False and self.player is not False:
                    self.log.info('rfid get False')
                    self.del_player()
                    # if self.del_player() is False:
                    #     self.cart = self.player['cart']

                if self.cart is not False and self.player is not False:
                    if self.player['forbiden'] is True:
                        self.log.warning('user is forbiden')
                        self.player = False
                    elif self.player is not False and self.cart != self.player['cart']:
                        self.log.warning(
                            'client cart is diffrent: client: %s from rfid: %s' % (self.player['cart'], self.cart))
                        # self.del_player()
                        # if self.del_player() is False:
                        #     self.cart = self.player['cart']
                    # elif self.db.get('PLAYER_DAY_ORDER') is not False and self.player is not False:
                    #     self.del_player(end_date=self.db.get('PLAYER_DAY_ORDER'))
                    #     self.db.set('PLAYER_DAY_ORDER', False)

                    else:
                        if self.player_bonus_warning_time != None:
                            if self.player_bonus_warning_time + 120 < time.time():
                                self.player_bonus_warning_time = None
                                self.server.set('PLAYER_BONUS_WARNING', None)
                        self.get_player_meter()

                        if 'old_meter' in self.player and 'new_meter' in self.player:
                            # FIXME: Зануляване при дневен отчет
                            # self.server.set('PLAYER_IN_NRA', self.db.get('PLAYER_IN_NRA'))
                            if None not in self.player['old_meter'].values() and None not in self.player['new_meter'].values():
                                # if self.db.get('PLAYER_DAY_ORDER') is not False and self.player and self.cart:
                                #     self.log.info('day reset player: %s', self.db.get('PLAYER_DAY_ORDER'))
                                #     full_total = self.player['new_meter']['curent credit']
                                #     self.player['new_meter']['curent credit'] = 0
                                #     self.send_data('set_client', player=self.player,
                                #                    end_date=self.db.get('PLAYER_DAY_ORDER'), del_cart=True)
                                #     # full_total = self.player['new_meter']['curent credit']
                                #     # self.player['new_meter']['curent credit'] = 0
                                #     # self.send_data('set_client', player=self.player, del_cart=True)
                                #     self.player = self.send_data('get_client', cart_id=self.cart, del_cart=True)
                                #     # self.cart = self.get_cart()
                                #     # if self.cart is False:
                                #     # #     # self.clean_rfid_poll()
                                #     #     self.cart = self.get_cart()
                                #     #     return False
                                #     self.player['cart'] = self.cart
                                #     self.get_player_meter()
                                #     self.player['full_total'] -= full_total
                                #     self.player['old_meter']['curent credit'] = 0
                                #     self.log.info('clean day')
                                if self.player['bonus_use'] is True and self.player['activ_bonus'] is not False and self.player['activ_bonus'] != None:
                                    self.server.set('PLAYER_PLAY_BONUS_MONY', None)
                                    # if self.player['no_out_befor'] > 1:
                                    #     self.stop_bill()
                                    if self.player['activ_bonus']['mony'] <= 0:
                                        var = self.make_random()
                                        self.player['activ_bonus']['mony'] = random.sample(var, 1)[0]
                                        response = self.send_data('activ_bonus_update_mony',
                                                                  bonus_id=self.player['activ_bonus']['id'],
                                                                  mony=self.player['activ_bonus']['mony'])

                                        if not response:
                                            self.log.error('%s', response, exc_info=True)

                                    self.server.set('PLAYER_WON_BONUS', self.player['activ_bonus']['mony'])
                                    bonus_get = self.server.get('PLAYER_GET_BONUS')
                                    # self.games_played = self.player['new meter']['games played']
                                    while bonus_get == []:
                                        cart = self.get_cart()
                                        bonus_get = self.server.get('PLAYER_GET_BONUS')
                                        #

                                        # self.log.error('%s', cart)
                                        if cart is False or cart != self.player['cart']:
                                            # self.clean_rfid_poll()
                                            cart = self.get_cart()
                                            if cart is False or cart != self.player['cart']:
                                                bonus_get = [False, self.player['activ_bonus']['mony']]
                                                self.log.warning('no client but have won %s',
                                                                 self.player['activ_bonus']['mony'])
                                                self.player['activ_bonus'] = False
                                                self.server.set('PLAYER_WON_BONUS', None)
                                            # self.player_get_bonus_now = False
                                            # break
                                        self.log.debug('get_bonus %s', bonus_get)
                                        # bonus_get = self.server.get('PLAYER_GET_BONUS')

                                    if bonus_get[0] is False:
                                        self.player['activ_bonus'] = None
                                        self.server.set('PLAYER_GET_BONUS', [])
                                        if self.player['bonus_one_per_day'] is True:
                                            self.player_get_bonus_now = True
                                    else:
                                        if self.player['bonus_waith_for_in_mony'] <= 0:
                                            var_wait_for_in = self.wait_for_in(self.player['activ_bonus']['mony'])
                                        else:
                                            var_wait_for_in = self.wait_for_in(self.player['bonus_waith_for_in_mony'])
                                        if var_wait_for_in is True:
                                            if self.set_bonus(mony=self.player['activ_bonus']['mony']) is True:
                                                self.update_bonus(self.player['activ_bonus']['id'])
                                                self.server.set('PLAYER_GET_BONUS', [])
                                                self.player['activ_bonus'] = None
                                                if self.player['bonus_one_per_day'] is True:
                                                    self.player_get_bonus_now = True
                                                    # self.old_rfid_poll_clean()
                                        elif var_wait_for_in == 'ERROR':
                                            self.del_player()
                                            # if self.del_player() is False:
                                            #     self.cart = self.player['cart']

                                # elif self.player['bonus_use'] is True and self.player['activ_bonus'] is not False and self.player['activ_bonus'] != None and self.use_touch is False:
                                #     self.server.set('PLAYER_PLAY_BONUS_MONY', None)
                                #     if self.player['activ_bonus']['mony'] <= 0:
                                #         var = self.make_random()
                                #         self.player['activ_bonus']['mony'] = random.sample(var, 1)[0]
                                #         response = None
                                #         while response is not True:
                                #             response = self.send_data('activ_bonus_update_mony',
                                #                                       bonus_id=self.player['activ_bonus']['id'],
                                #                                       mony=self.player['activ_bonus']['mony'])
                                #
                                #             if not response:
                                #                 self.log.error('%s', response, exc_info=True)
                                #
                                #         if self.set_bonus(mony=self.player['activ_bonus']['mony']) is True:
                                #             self.update_bonus(self.player['activ_bonus']['id'])
                                #     else:
                                #         if self.set_bonus(mony=self.player['activ_bonus']['mony']) is True:
                                #             self.update_bonus(self.player['activ_bonus']['id'])
                                #     if self.player['bonus_one_per_day'] is True:
                                #         self.player_get_bonus_now = True
                                #     self.player['activ_bonus'] = None
                                # # if self.player is False or self.player == None:
                                # #     pass
                                else:
                                    i_get_bonus = self.chk_for_bonus()
                                    self.log.debug('check for bonus: %s', i_get_bonus)
                                    # if i_get_bonus is True and self.use_touch is False:
                                    #     self.server.set('PLAYER_PLAY_BONUS_MONY', None)
                                    #     var = self.make_random()
                                    #     var = random.sample(var, 1)[0]
                                    #     response = self.send_data('client_want_bonus',
                                    #                               cust_id=self.player['id'],
                                    #                               mony=var,
                                    #                               from_in=self.player['restricted_bonus'],
                                    #                               from_redirect=self.player['from_redirect'],
                                    #                               goup=self.player['grup'])
                                    #     while response == None:
                                    #         response = self.send_data('client_want_bonus',
                                    #                                   cust_id=self.player['id'],
                                    #                                   mony=var,
                                    #                                   from_in=self.player['restricted_bonus'],
                                    #                                   from_redirect=self.player['from_redirect'],
                                    #                                   goup=self.player['grup'])
                                    #     if self.set_bonus(mony=var) is True:
                                    #         # if self.use_touch is False:
                                    #         #     data = None
                                    #         #     while data is not True:
                                    #         #         data = self.send_data(evt='aft_bonus', mony=var)
                                    #         self.update_bonus(response)
                                    #         self.player['activ_bonus'] = None
                                    #         if self.player['bonus_one_per_day'] is True:
                                    #             self.player_get_bonus_now = True


                                    if i_get_bonus is True and self.player['bonus_use'] is True:
                                        # if self.player['no_out_befor'] > 1:
                                        #     self.stop_bill()
                                        # self.pipe['sas'].send(['sas.get_single_meter',
                                        #                        {'command': 'disable bill',
                                        #                         'request_time': time.time() + (self.sas_timeout - 2)}])
                                        # if self.pipe['sas'].poll(self.sas_timeout):
                                        #     tmp = self.pipe['sas'].recv()
                                        #     self.log.info('stop bill if wait_for_in: %s', tmp)
                                        self.server.set('PLAYER_PLAY_BONUS_MONY', None)
                                        self.server.set('PLAYER_BONUS_INIT', self.make_random())
                                        bonus_get = []
                                        # self.games_played = self.player['new meter']['games played']
                                        while bonus_get == []:
                                            cart = self.get_cart()
                                            if cart is False or cart != self.player['cart']:
                                                # self.clean_rfid_poll()
                                                cart = self.get_cart()
                                            bonus_get = self.server.get('PLAYER_GET_BONUS')
                                            if cart is False or cart != self.player['cart']:
                                                won = None
                                                if bonus_get == []:
                                                    for i in range(4):
                                                        if won:
                                                            break
                                                        time.sleep(1)
                                                        bonus_get = self.server.get('PLAYER_GET_BONUS')
                                                        if bonus_get != []:
                                                            won = None
                                                            break
                                                        won = self.server.get('PLAYER_WON_BONUS')
                                                if won:
                                                    bonus_get = [False, won]
                                                    self.server.set('PLAYER_GET_BONUS', [False, won])
                                                else:
                                                    pass
                                                self.player['activ_bonus'] = False
                                                self.server.set('PLAYER_WON_BONUS', None)
                                                # else:
                                                self.log.warning('no cart but have won %s', won)
                                                # break
                                        self.log.debug('get_bonus %s', bonus_get)
                                        if bonus_get != []:
                                            if bonus_get[0] is True:
                                                response = None
                                                response = self.send_data('client_want_bonus',
                                                                          cust_id=self.player['id'],
                                                                          mony=bonus_get[1],
                                                                          from_in=self.player['restricted_bonus'],
                                                                          from_redirect=self.player['from_redirect'],
                                                                          goup=self.player['grup'],
                                                                          bonus_one_per_day=self.player['bonus_one_per_day'])
                                                self.log.debug('%s', response)
                                                while response == None:
                                                    response = self.send_data('client_want_bonus',
                                                                              cust_id=self.player['id'],
                                                                              mony=bonus_get[1],
                                                                              from_in=self.player['restricted_bonus'],
                                                                              from_redirect=self.player['from_redirect'],
                                                                              goup=self.player['grup'],
                                                                              bonus_one_per_day=self.player['bonus_one_per_day'])
                                                if response is not False:
                                                    if self.player['bonus_waith_for_in_mony'] <= 0:
                                                        var_wait_for_in = self.wait_for_in(bonus_get[1])
                                                    else:
                                                        var_wait_for_in = self.wait_for_in(self.player['bonus_waith_for_in_mony'])
                                                else:
                                                    var_wait_for_in = False
                                                if var_wait_for_in is True:
                                                    if self.set_bonus(mony=bonus_get[1]) is True:
                                                        # if self.use_touch is False:
                                                        #     data = None
                                                        #     while data is not True:
                                                        #         data = self.send_data(evt='aft_bonus',mony=bonus_get[1])
                                                        self.update_bonus(response)
                                                        self.server.set('PLAYER_GET_BONUS', [])
                                                        self.player['activ_bonus'] = False
                                                        if self.player['bonus_one_per_day'] is True:
                                                            self.player_get_bonus_now = True
                                                elif var_wait_for_in == 'ERROR':
                                                    bonus_get = []
                                                    self.player['activ_bonus'] = False
                                                    self.server.set('PLAYER_GET_BONUS', [])
                                                else:
                                                    self.server.set('PLAYER_GET_BONUS', [])
                                                    self.player['activ_bonus'] = False
                                            elif bonus_get[0] is False:
                                                self.server.set('PLAYER_GET_BONUS', [])
                                                self.player['activ_bonus'] = None
                                                if self.player['bonus_one_per_day'] is True:
                                                    self.player_get_bonus_now = True
                                                response = None
                                                response = self.send_data('client_want_bonus',
                                                                          cust_id=self.player['id'],
                                                                          mony=bonus_get[1],
                                                                          from_in=self.player['restricted_bonus'],
                                                                          from_redirect=self.player['from_redirect'],
                                                                          goup=self.player['grup'],
                                                                          bonus_one_per_day=self.player['bonus_one_per_day'])
                                                while response == None:
                                                    response = self.send_data('client_want_bonus',
                                                                              cust_id=self.player['id'],
                                                                              mony=bonus_get[1],
                                                                              from_in=self.player['restricted_bonus'],
                                                                              from_redirect=self.player['from_redirect'],
                                                                              goup=self.player['grup'],
                                                                              bonus_one_per_day=self.player['bonus_one_per_day'])

            except Exception as e:
                time.sleep(0.5)
                try:
                    # self.clean_rfid_poll()
                    self.clean_sas_poll()
                except:
                    pass
                self.log.error('player: %s', self.player)
                self.log.critical(e, exc_info=True)
