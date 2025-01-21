# -*- coding:utf-8 -*-
'''
Created on 1.05.2021

@author: dedal
'''
from multiprocessing import Process
import log
import time
import datetime
import client
from libs import system
import threading
# import json
import libs
from libs import proto_sas as sas
from queue import Queue
import random
import os

class Sas(Process):
    def __init__(self, **kwargs):
        Process.__init__(self, name='SAS')
        self.Q = Queue()
        self.game_started = False
        self.conf = kwargs['conf']
        self.date_jump_mounth = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        self.date_jump_day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
                              '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
        self.send_q = Queue()
        self.sas_sleep = self.conf.get('SAS', 'sleep_time', 'float')
        # self.impera = self.conf.get('SAS', 'impera', 'bool')
        self.db = kwargs['db']
        self.SEND = kwargs['send']
        self.log = log.get_log(log.LOG_CHANEL_LEVEL['sas'])
        self.pipe = kwargs['pipe']
        self.crypt = kwargs['crypt']
        self.stop_autoplay = self.conf.get('SAS', 'stop_autoplay', 'bool')
        # self.aft_won = self.conf.get('SAS', 'aft_won', 'bool')
        self.stop_autoplay_now = False
        self.stop_autoplay_on_won = self.conf.get('SAS', 'stop_autoplay_on_won', 'int')
        self.stop_autoplay_old_won = None
        self.stop_autoplay_time = range(200, 300, 100)
        self.stop_autoplay_fix_after_time = None
        self.stop_autoplay_fix_after_time_from_conf = self.conf.get('SAS', 'stop_autoplay_fix_after_time', 'int')
        self.user_stop_bill = False
        self.disable_all_games = True
        self.ip = system.get_ip()
        self.timeout = self.conf.get('SAS', 'sas_timeout', 'float')
        gpoll_timeout = self.conf.get('SAS', 'gpoll_timeout', 'float')
        self.emg_type = self.conf.get('SAS', 'emg_type', 'int')
        self.bonus_old_in = None
        self.bonus_is_down = False
        self.db.set('chk_jp_down', False)

        # if self.emg_type == 6:
        #     self.aft_won = False
        # else:
        #     self.aft_won = True
        # if self.emg_type == 7:
        #     self.impera = True
        # else:
        #     self.impera = False
        # self.aft_my_key = self.conf.get('SAS', 'aft_key', 'str')
        self.use_security = self.conf.get('SAS', 'security', 'bool')
        # self.clean_aft_tranzaction = self.conf.get('SAS', 'clean_aft_tranzaction', 'bool')
        self.pay_by_hand = self.conf.get('SAS', 'pay_jp_by_hand', 'bool')
        self.disable_game_from_jp = self.db.get('DISABLE_GAME_JP')
        self.db_security = self.db.get('SAS_SECURITY')
        self.check_for_game = self.conf.get('SAS', 'check_for_game', 'bool')
        self.coef_my_denom = self.conf.get('SAS', 'coef', 'float')
        self.set_jp_mether_to_out = self.conf.get('SAS', 'set_jp_mether_to_out', 'bool')
        self.bonus_clear_transaction_pool = False
        # self.coef_use = self.conf.get('SAS', 'coef_use', 'bool')
        self.aft_check_last_transaction = self.conf.get('SAS', 'aft_check_last_transaction', 'bool')
        self.last_aft_transaction_from_emg = self.conf.get('SAS', 'last_aft_transaction_from_emg', 'bool')
        self.emg_security = None
        self.sync_datetime = self.conf.get('SAS', 'sync_time', 'bool')
        self.old_bet = None
        self.bonus_revert_old_bet = None
        self.old_in = None
        self.working_mod = self.db.get('WORKING_MODULE')
        self.bonus_for_hold = None
        # self.player_bonus_for_hold = None
        self.no_bonus_out_befor = None
        self.no_cust_bonus_out_befor = None
        self.db.set('CUST_NO_AUT_BEFOR', self.no_cust_bonus_out_befor)
        self.hold_mony = self.conf.get('BONUS', 'out', 'float')
        self.cust_hold_mony = self.conf.get('PLAYER', 'bonus_on_credit', 'float')
        self.block_bonus_by_bet = self.conf.get('SYSTEM', 'block_bonus_by_bet', 'bool')
        self.tcp_buffer = self.conf.get('COMUNICATION', 'buffer', 'int')
        self.tcp_timeout = self.conf.get('COMUNICATION', 'timeout', 'int')
        self.bonus_ip = self.conf.get('DB_SERVER', 'ip', 'str')
        self.bonus_port = self.conf.get('DB_SERVER', 'port', 'int')
        self.jp_down_if_credit = self.conf.get('JP_SERVER', 'down_if_credti', 'float')
        self.jp_down_by_aft = self.conf.get('JP_SERVER', 'down_by_aft', 'bool')
        self.jp_clean_transaction_poll = False
        self.ks_use_aft = self.conf.get('KEYSYSTEM', 'aft', 'bool')
        # self.block_keysystem_for_security = False
        self.ip = system.get_ip()
        self.use_aft = self.conf.get('SAS', 'aft', 'bool')
        self.init_security_time = time.time() - 30
        self.init_time = time.time()
        self.smib_reload_securiy = False
        if self.check_for_game is True:
            self.my_game = None
        else:
            self.my_game = 1
        self.notifiti_if_won = self.conf.get('SAS', 'mail_send', 'bool')
        self.notifity_if_won_mony = self.conf.get('SAS', 'mail_send_on_won', 'int')
        self.old_won = None
        self.aft_register_initial = False
        self.slee_on_down = self.conf.get('SAS', 'sleep_on_down', 'bool')
        self.sas_dump = self.conf.get('SAS', 'sas_dump', 'bool')
        self.sas_n = self.conf.get('SAS', 'sas_n', 'str')
        sas.GPOLL_TIMEOUT = gpoll_timeout
        # sas.SLEEP_IF_FORMAT_TRANSACTION = self.slee_on_down
        try:
            if self.conf.get('SAS', 'usb', 'bool') is True:
                self.port = '/dev/ia'
                self.sas = sas.SAS_USB(port=self.port, timeout=self.timeout, log=self.log,
                                       aft_check_last_transaction=self.aft_check_last_transaction, sas_dump=self.sas_dump, denom=self.coef_my_denom,
                                       lock_time=self.conf.get('SAS', 'aft_lock_time', 'int'),
                                       get_aft_transaction_from_EMG=self.last_aft_transaction_from_emg)
            else:
                # realise = os.popen('lsb_release -a | grep Description:').read()
                # if 'buster' in realise:
                self.port = '/dev/ttyS4'
                # else:
                #     self.port = '/dev/ttyS1'
                self.sas = sas.Sas(port=self.port, timeout=self.timeout, log=self.log,
                                   aft_check_last_transaction=self.aft_check_last_transaction, sas_dump=self.sas_dump, denom=self.coef_my_denom,
                                   lock_time=self.conf.get('SAS', 'aft_lock_time', 'int'),
                                   get_aft_transaction_from_EMG=self.last_aft_transaction_from_emg)
        except Exception as e:
            self.log.critical(e, exc_info=True)
            self.sas = None
        if self.sas_n != '00':
            self.sas.mashin_n = self.sas_n
            self.sas.adress = int(self.sas_n)
        # self.sas.log = self.log
        self.meter = {'games played': None, 'bet': None, 'bill': None, 'won': None, 'in': None, 'out': None,
                      'curent credit': None, 'jp': None}
        self.db.set('SAS_METER', self.meter)
        self.db.set('SAS_METER_IN_COUNT', None)
        self.use_gpoll = self.conf.get('SAS', 'use_gpoll', 'bool')
        self.event = None
        self.error = 0
        self.old_out = 0
        self.counter_time = time.time()
        self.rill_hold = True
        self.rill_hold_time = None
        self.delay_rill = self.conf.get('SAS', 'delay_rill', 'bool')
        # self.bonus_error = self.db.get('BONUS_ERROR_LOG')
        # self.hold_player_bonus_error = self.db.get('PLAYER_BINUS_HOLD_ERROR')
        self.bonus_initial = 0
        self.player_bonus_initial = 0
        self.revert_player_bonus_by_bet = False
        # if self.hold_player_bonus_error == []:
        self.cust_bonus_for_hold = None
        self.all_event = {
            'sas.get_single_meter': self.get_single_meter,
            'sas.get_multi_meter': self.get_multi_meter,
            'sas.coef': self.sas.gaming_machine_ID,
            'sas.denom': self.return_denom,
            'sas.get_mashin_n': self.return_machin_n,
            'sas.get_date_time': self.sas.current_date_time,
            'sas.game_disable_denomination': self.game_disable_denomination,
            'sas.sas_version': self.sas.SAS_version_gaming_machine_serial_ID,
            'sas.delay_game': self.sas.delay_game,
            'sas.set_date_time': self.sas.recieve_date_time,
            'sas.set_legacy_bonus': self.set_legacy_bonus,
            # 'sas.multi_cmd': self.lpoll.multi_cmd,
            'sas.event': self.sas.events_poll,
            # 'sas.meter': self.meter,
            # 'sas.bet': self.meter['bet'],
            # 'sas.won': self.meter['won'],
            # 'sas.in': self.meter['in'],
            # 'sas.out': self.meter['out'],
            # 'sas.bill': self.meter['bill'],
            'sas.enable_game_from_jackpot': self.enable_game_from_jackpot,
            'sas.disable_game_from_jackpot': self.disable_game_from_jackpot,
            'sas.jp_down': self.jp_down,
            'sas.bonus': self.bonus_init,
            'sas.bonus_hold': self.bonus_hold,
            'sas.sas_security_unlock': self.sas_security_unlock,
            'sas.sync_time': self.sync_time_now,
            'sas.mether_count': self.mether_count,
            'sas.client_bonus': self.client_bonus,
            'sas.lock_emg': self.sas.shutdown,
            'sas.register': self.sas.AFT_register,
            'sas.get_last_transaction': self.sas.AFT_get_last_transaction,
            'sas.clean_transaction_poll': self.sas.AFT_clean_transaction_poll,
            'sas.add_in_to_emg': self.add_in_to_emg,
            'sas.get_out_from_emg': self.get_out_from_emg,
            'sas.add_won_to_emg': self.add_won_to_emg,
            # 'sas.add_jp_to_emg': self.add_jp_to_emg,
            'sas.order': self.order,
            'sas.stop_alarm': self.stop_alarm,
            'sas.start_alarm': self.start_alarm,
            'sas.format_transaction_id': self.sas.AFT_format_transaction,
            'sas.aft_register': self.sas.AFT_register,
            'sas.cansel_request': self.sas.AFT_cansel_request,
            'sas.player_hold': self.player_hold,
            'no_out_befor': self.no_out_befor,
            'sas.cust_monyback_pay':self.cust_monyback_pay,
            # 'sas.send_chk_jp_down':self.send_chk_jp_down,
        }
        # else:
        #     self.cust_bonus_for_hold = self.hold_player_bonus_error[0]
        self.mem_server = libs.db.mem_db.MemDB()
        # try:
        #     self.LOCK.release()
        # except ValueError:
        #     pass

    def cust_monyback_pay(self, **kwargs):
        try:
            waith_to_play = kwargs['waith_to_play']
            tax = kwargs['tax']
            mony = kwargs['mony']
            request_time = kwargs['request_time']
            self.log.info('mony: %s, tax: %s' % (mony, tax))
            del kwargs['request_time']
            if self.slee_on_down is True:
                time.sleep(self.sas_sleep)
            if self.use_aft is False:
                if waith_to_play > time.time():
                    if self.check_for_game is True:
                        data = self.sas.initiate_legacy_bonus_pay(mony=mony, tax=tax)
                    else:
                        data = self.sas.initiate_legacy_bonus_pay(mony=mony, tax=tax, games=1)
                else:
                    return False
                if data is True:
                    if self.use_security is True:
                        self.smib_reload_securiy = True
                        self.init_security_time = time.time() + 30
                    return True
                else:
                    self.log.warning('monyback_pay: sas response %s', data)
                    return False
            else:
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                if waith_to_play > time.time():
                    try:
                        if self.check_for_game is True:
                            data = self.sas.AFT_won(mony=mony, amount=1)
                        else:
                            data = self.sas.AFT_won(mony=mony, amount=1, games=1)
                    except Exception as e:
                        data = None
                        self.log.warning(e, exc_info=True)
                else:
                    return False
                if data == 'NoGame':
                    self.log.warning('NO GAME SELECTED: %s', data)
                    return False
                data = None
                while request_time > time.time():
                    if data == None or data is False:
                        time.sleep(self.sas_sleep)
                        try:
                            data = self.clean_transaction_poll()
                        except sas.BadCRC as e:
                            data = None
                            self.log.info(e, exc_info=True)
                        except sas.BadTransactionID as e:
                            data = None
                            self.log.error(e, exc_info=True)
                        except Exception as e:
                            data = None
                            self.log.error(e, exc_info=True)
                    else:
                        if data['Transfer status'] == 'Full transfer successful':
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.log.info('monyback_pay: %s', data)
                            return True
                        elif data['Transfer status'] == 'Transfer pending (not complete)':
                            if self.emg_type == 7 or self.emg_type == 8:
                                self.bonus_clear_transaction_pool = True
                                if self.slee_on_down is True:
                                    time.sleep(self.sas_sleep)
                                self.log.info('monyback_pay: %s', data)
                                return True
                            time.sleep(self.sas_sleep)
                            self.log.info('monyback_pay: sas response %s', data)
                            data = None
                        else:
                            self.log.error('monyback_pay: sas response %s', data)
                            return False
                self.log.warning('monyback_pay: sas timeout')
                return False
        except Exception as e:
            self.log.error(e, exc_info=True)
            return None

    def return_machin_n(self, **kwargs):
        return self.sas.mashin_n

    def return_denom(self, **kwargs):
        return self.sas.denom

    def get_single_meter(self, **kwargs):
        data = None
        for i in range(2):
            try:
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                if kwargs['command'] == 'curent credit':
                    data = self.sas.current_credits()
                elif kwargs['command'] == 'out':
                    data = self.sas.total_cancelled_credits()
                elif kwargs['command'] == 'out credit':
                    data = self.sas.total_cancelled_credits(denom=False)
                elif kwargs['command'] == 'true out':
                    data = self.sas.true_coin_out(denom=False)
                elif kwargs['command'] == 'true out credit':
                    data = self.sas.true_coin_out(denom=True)
                elif kwargs['command'] == 'bill':
                    data = self.sas.total_dollar_value_of_bills_meter()
                elif kwargs['command'] == 'bet':
                    data = self.sas.total_bet_meter()
                elif kwargs['command'] == 'won':
                    data = self.sas.total_win_meter()
                elif kwargs['command'] == 'in':
                    data = self.sas.total_in_meter(denom=False)
                elif kwargs['command'] == 'in credit':
                    data = self.sas.total_in_meter(denom=True)
                elif kwargs['command'] == 'true in':
                    data = self.sas.true_coin_in(False)
                elif kwargs['command'] == 'true in credit':
                    data = self.sas.true_coin_in(True)
                elif kwargs['command'] == 'jp':
                    data = self.sas.total_jackpot_meter()
                elif kwargs['command'] == 'games played':
                    data = self.sas.games_played_meter()
                elif kwargs['command'] == 'game won':
                    data = self.sas.games_won_meter()
                elif kwargs['command'] == 'game lost':
                    data = self.sas.games_lost_meter()
                elif kwargs['command'] == 'game implement':
                    data = self.sas.total_number_of_games_impimented()
                elif kwargs['command'] == 'selected game':
                    data = self.sas.selected_game_number()
                # elif kwargs['command'] == 'denomination':
                #     {'command': 'B3', 'size': 5, 'denom': False},
                elif kwargs['command'] == 'halt':
                    data = self.sas.shutdown()
                elif kwargs['command'] == 'start':
                    data = self.sas.startup()
                elif kwargs['command'] == 'halt bill':
                    self.user_stop_bill = True
                    data = self.sas.disable_bill_acceptor()
                elif kwargs['command'] == 'start bill':
                    self.user_stop_bill = False
                    data = self.sas.enable_bill_acceptor()
                    # self.log.error('data %s', data)
                elif kwargs['command'] == 'halt autoplay':
                    data = self.sas.stop_autorebet()
                elif kwargs['command'] == 'start autoplay':
                    data = self.sas.stop_autorebet()
                elif kwargs['command'] == 'reset hand pay':
                    data = self.sas.remote_handpay_reset()
                elif kwargs['command'] == 'stop alarm':
                    data = self.sas.enter_maintenance_mode()
                elif kwargs['command'] == 'start alarm':
                    data = self.sas.exit_maintanance_mode()
                elif kwargs['command'] == 'disable bill':
                    data = self.sas.disable_bill_acceptor()
                elif kwargs['command'] == 'player_reset_hand_pay':
                    data = self.player_reset_hand_pay(**kwargs)
                elif kwargs['command'] == 'enable bill':
                    # self.log.error('user_stop_bill %s', self.user_stop_bill)
                    if self.user_stop_bill is True:
                        data = True
                    else:
                        data = self.sas.enable_bill_acceptor()
                if data == None:
                    pass
                elif data is False:
                    pass
                else:
                    break
            except Exception as e:
                self.log.error(e, exc_info=True)
                data = None
        return data

    def player_reset_hand_pay(self, **kwargs):
        if kwargs['forbiden'] == False:
            self.sas.remote_handpay_reset()
            return True
        else:
            try:
                if kwargs['waith_to_play'] > time.time() and self.no_bonus_out_befor == None and self.no_cust_bonus_out_befor == None:
                    data_old = self.sas.send_meters_10_15(True)
                    if data_old == None:
                        self.mem_server.set('MAKE_IN_OUT', False)
                        return False
                    self.sas.remote_handpay_reset()
                    while kwargs['request_time'] > time.time():
                        data_new = self.sas.send_meters_10_15(True)
                        if data_new:
                            if data_new['total_cancelled_credits_meter'] > data_old['total_cancelled_credits_meter']:
                                self.mem_server.set('MAKE_IN_OUT', False)
                                return data_new['total_cancelled_credits_meter'] - data_old[
                                    'total_cancelled_credits_meter']
                else:
                    self.mem_server.set('MAKE_IN_OUT', False)
                return False
            except Exception as e:
                self.log.warning(e, exc_info=True)
                return False
        return False

    def get_multi_meter(self, **kwargs):
        data = None
        for i in range(2):
            try:
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                if kwargs['command'] == '19':
                    data = self.sas.meters_11_15(False)
                elif kwargs['command'] == '0F':
                    data = self.sas.send_meters_10_15(False)
                elif kwargs['command'] == '1C':
                    data = self.sas.meters(False)
                elif kwargs['command'] == '19 credit':
                    data = self.sas.meters_11_15(True)
                elif kwargs['command'] == '0F credit':
                    data = self.sas.send_meters_10_15(True)
                elif kwargs['command'] == '1C credit':
                    data = self.sas.meters(True)
                elif kwargs['command'] == 'bill':
                    data = self.sas.total_bill_meters()
                elif kwargs['command'] == 'meter for game':
                    data = self.sas.game_meters()
                elif kwargs['command'] == 'game conf':
                    data = self.sas.game_configuration()
                elif kwargs['command'] == 'bonus win':
                    data = False
                elif kwargs['command'] == 'legacy bonus':
                    data = self.sas.legacy_bonus_meters()
                if data == None:
                    pass
                elif data is False:
                    pass
                else:
                    break
            except Exception as e:
                self.log.error(e, exc_info=True)
                data = None
        return data

    def clear_meter(self, **kwargs):
        # if self.slee_on_down is True:
        #     time.sleep(self.sas_sleep)
        meter = {'games played': None, 'bet': None, 'bill': None, 'won': None, 'in': None, 'out': None,
                 'curent credit': None, 'jp': None}
        # try:
        #     all_meter = self.sas.send_meters_10_15(True)
        # except sas.BadCRC:
        all_meter = None
        if all_meter == None:
            for i in range(3):
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                try:
                    all_meter = self.sas.send_meters_10_15(True)
                except sas.BadCRC:
                    all_meter = None
                except Exception as e:
                    all_meter = None
                    self.log.warning(e, exc_info=True)
                if all_meter != None:
                    break
        if all_meter != None:
            if self.set_jp_mether_to_out is True:
                meter['out'] = all_meter['total_cancelled_credits_meter'] + all_meter['total_jackpot_meter']
            else:
                meter['out'] = all_meter['total_cancelled_credits_meter']
            meter['bet'] = all_meter['total_in_meter']
            meter['won'] = all_meter['total_out_meter']
            meter['in'] = all_meter['total_droup_meter']
            meter['jp'] = all_meter['total_jackpot_meter']
            meter['games played'] = all_meter['games_played_meter']
        else:
            for i in meter.keys():
                meter[i] = None
        if meter['in'] != self.meter['in']:
            meter['bill'] = None
            if meter['bill'] == None:
                for i in range(3):
                    if self.slee_on_down is True:
                        time.sleep(self.sas_sleep)
                    try:
                        meter['bill'] = self.sas.total_dollar_value_of_bills_meter()
                    except sas.BadCRC:
                        meter['bill'] = None
                    except Exception as e:
                        meter['bill'] = None
                        self.log.warning(e, exc_info=True)
                    if meter['bill'] != None:
                        break
        else:
            meter['bill'] = self.meter['bill']

        if meter['in'] != self.meter['in'] or meter['out'] != self.meter['out'] or meter['bet'] != self.meter['bet'] or \
                meter['won'] != self.meter['won'] or meter['jp'] != self.meter['jp']:
            meter['curent credit'] = None
            if meter['curent credit'] == None:
                for i in range(3):
                    if self.slee_on_down is True:
                        time.sleep(self.sas_sleep)
                    try:
                        meter['curent credit'] = self.sas.current_credits(True)
                    except sas.BadCRC:
                        meter['curent credit'] = None
                    except Exception as e:
                        meter['curent credit'] = None
                        self.log.warning(e, exc_info=True)
                    if meter['curent credit'] != None:
                        break
        else:
            meter['curent credit'] = self.meter['curent credit']

        self.log.debug('METHER: %s', meter)
        self.db.set('SAS_METER', meter)
        self.db.set('CUST_NO_AUT_BEFOR', self.no_cust_bonus_out_befor)
        if meter != None and self.meter is not None:
            if None not in meter.values() and None not in self.meter.values():
                self.write_in_out(meter)
        self.meter = meter
        if self.meter == None:
            self.db.set('SAS_METER_IN_COUNT', None)
        elif None in self.meter.values():
            self.db.set('SAS_METER_IN_COUNT', None)
        else:
            self.db.set('SAS_METER_IN_COUNT', self.mether_count())
        return self.meter

    def write_in_out(self, meter):
        if meter['in'] != self.meter['in'] or meter['out'] != self.meter['out']:
            if meter['in'] < self.meter['in']:
                return
            if meter['out'] < self.meter['out']:
                return
            if meter['bill'] < self.meter['bill']:
                return
            player = self.db.get('PLAYER')
            if player == None:
                pass
            elif player is False:
                pass
            else:
                player = player['id']

            ins = meter['in'] - self.meter['in']
            out = meter['out'] - self.meter['out']
            # if meter['bill'] is not None:
            bill = meter['bill'] - self.meter['bill']
            # else:
            # bill = 0
            self.send_exception(evt='write_in_out', ins=ins, bill=bill, out=out, player=player)

    def _send_to_server(self, q, send, log, **kwargs):
        while True:
            try:
                data_to_send = q.get()
                if 'timeout' not in data_to_send:
                    data_to_send['timeout'] = self.tcp_timeout
                data = None
                while send.poll():
                    send.recv()
                my_init_time = time.time()
                data_to_send['my_init_time'] = my_init_time
                while data == None:
                    data_to_send['send_time'] = time.time()
                    try:
                        send.send(data_to_send)
                        if data_to_send['timeout'] <= 0:
                            break
                        if send.poll(data_to_send['timeout']+3):
                            data = send.recv()
                        if data != None:
                            if data[1] != data_to_send:
                                data = None
                            else:
                                data = data[0]
                                break
                    except Exception as e:
                        self.log.error(e, exc_info=True)
                    if data == None:
                        time.sleep(2)
            except Exception as e:
                log.error(e, exc_info=True)

    def mether_count(self, **kwargs):
        if None in self.meter.values():
            return None
        else:
            return {'bet': int(round(self.meter['bet'] / self.sas.denom, 2)),
                    'bill': int(self.meter['bill']),
                    'won': int(round(self.meter['won'] / self.sas.denom, 2)),
                    'in': int(round(self.meter['in'] / self.sas.denom, 2)),
                    'out': int(round(self.meter['out'] / self.sas.denom, 2)),
                    'jp': int(round(self.meter['jp'] / self.sas.denom, 2)),
                    'curent credit': self.meter['curent credit'],
                    'games played': self.meter['games played']}

    def old_poll_clean(self):
        for i in self.pipe:
            if self.pipe[i].poll():
                self.pipe[i].recv()

    def security_get(self, **kwargs):
        self.emg_security = self.sas.legacy_bonus_meters()
        self.log.info('%s', str(self.emg_security))
        if self.emg_security != None or self.emg_security is not False:
            return self.emg_security
        return False

    def securite_check(self, **kwargs):
        self.emg_security = self.sas.legacy_bonus_meters()
        if self.slee_on_down is True:
            time.sleep(self.sas_sleep)
        data = None
        if self.use_aft is True:
            data = self.sas.AFT_get_last_transaction()
            for i in range(3):
                if data:
                    if data == int('2020202020202020202020202020202021', 16):
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                    else:
                        break
                else:
                    if self.slee_on_down is True:
                        time.sleep(self.sas_sleep)
                    data = self.sas.AFT_get_last_transaction()
            if data:
                if self.db.get('AFT_TRANSACTION') != data:
                    self.log.error('lock emg new AFT: %s \nold: %s' % (data, self.db.get('AFT_TRANSACTION')))
                    # self.block_keysystem_for_security = True
                    self.sas.shutdown()
                    self.db.set('STATUS', 'EMG SECURITY LOCK')
                    # self.send_exception('write_log',
                    #                     msg='EMG SECURITY LOCK AFT TRANSACTION: new: %s,\n old:%s' % (self.sas.transaction, self.db.get('AFT_TRANSACTION')))
                    return False
        if self.emg_security != None and self.db_security != None:
            if self.emg_security != self.db_security:
                self.log.error('lock emg new: %s \nold: %s' % (self.emg_security, self.db_security))
                # self.block_keysystem_for_security = True
                self.sas.shutdown()
                self.db.set('STATUS', 'EMG SECURITY LOCK')
                # self.send_exception('write_log',
                #                     msg='EMG SECURITY LOCK: old: %s,\n new:%s' % (self.db_security, self.emg_security))
                return False
        return True

    def security_reload(self, **kwargs):
        self.emg_security = self.sas.legacy_bonus_meters()
        self.db.set('AFT_TRANSACTION', self.sas.transaction)
        self.log.info('new: %s \nold: %s' % (self.emg_security, self.db_security))
        if self.emg_security != None and self.emg_security is not False:
            if self.emg_security != self.db_security:
                self.db_security = self.emg_security
                self.smib_reload_securiy = False
                self.db.set('SAS_SECURITY', self.db_security)
                return True
            elif self.emg_security == self.db_security:
                    self.log.error('security_reload timeout new: %s \nold: %s' % (self.emg_security, self.db_security))
                    self.smib_reload_securiy = False
                    return True
        if self.smib_reload_securiy is False and self.emg_security != None:
            self.db_security = self.emg_security
            self.db.set('SAS_SECURITY', self.db_security)
            return True
        return False

    def sas_security_unlock(self, **kwargs):
        self.stop_autoplay_now = False
        self.sas.startup()
        self.smib_reload_securiy = True
        # self.smib_reload_securiy = True
        self.init_security_time = time.time() + 30
        data = None
        if self.use_aft is True:
            data = self.sas.AFT_get_last_transaction()
            for i in range(3):
                if data:
                    if data == int('2020202020202020202020202020202021', 16):
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        data = self.sas.AFT_get_last_transaction()
                    else:
                        break
                else:
                    if self.slee_on_down is True:
                        time.sleep(self.sas_sleep)
                    data = self.sas.AFT_get_last_transaction()
                time.sleep(self.sas_sleep)
            self.log.info('AFT TRANSACTION: old %s, new %s' % (self.sas.transaction, data))
            self.sas.transaction = data
            self.db.set('AFT_TRANSACTION', self.sas.transaction)
        data = self.security_reload()
        self.db.set('STATUS', 'OK')
        if self.db.get('PLAYER_IN_NRA') is True:
            self.db.set('PLAYER_IN_NRA', False)
        self.send_exception('write_log', msg='security unlock')
        return data

    def sync_time_now(self):
        current_date = datetime.datetime.now()
        if datetime.datetime.strftime(current_date, '%Y') == '2010':
            self.sync_datetime = False
            return True
        my_date = datetime.datetime.strftime(current_date, '%m.%d.%Y')
        my_time = datetime.datetime.strftime(current_date, '%H:%M')
        self.sas.recieve_date_time(dates=my_date, times=my_time)
        self.sync_datetime = False
        return True

    def send_exception(self, evt, **kwargs):
        kwargs['evt'] = evt
        kwargs['send_time'] = time.time()
        kwargs['ip'] = self.bonus_ip
        kwargs['port'] = self.bonus_port
        kwargs['timeout'] = self.tcp_timeout
        kwargs['udp_buffer'] = self.tcp_buffer
        kwargs['my_name'] = self.ip
        self.send_q.put(kwargs)
        # try:
        #     self.SEND.send(kwargs)
        # except Exception as e:
        #     self.log.error(e, exc_info=True)
        return True

    # def send_player_hold_data(self, **kwargs):
    #     t = threading.Thread(target=self._send_player_hold_data, kwargs=kwargs)
    #     t.start()

    def send_player_hold_data(self, **kwargs):
        hold_init_time = time.time()
        kwargs['evt'] = 'hold_client_cart_bonus'
        kwargs['ip'] = self.bonus_ip
        kwargs['port'] = self.bonus_port
        kwargs['timeout'] = self.tcp_timeout
        kwargs['udp_buffer'] = self.tcp_buffer
        kwargs['hold_init_time'] = hold_init_time
        kwargs['send_time'] = time.time()
        kwargs['my_name'] = self.ip
        self.send_q.put(kwargs)
        # while True:
        #     kwargs['send_time'] = time.time()
        #     try:
        #         self.SEND.send(kwargs)
        #         data = self.SEND.recv()
        #         if data is True:
        #             break
        #     except Exception as e:
        #         self.log.error(e, exc_info=True)
        #     time.sleep(1)
        # while self.SEND.poll():
        #     self.SEND.recv()
        # return data

    # def send_honus_hold_data(self, **kwargs):
    #     t = threading.Thread(target=self._send_honus_hold_data, kwargs=kwargs)
    #     t.start()

    def send_honus_hold_data(self, **kwargs):
        if 'myinit_time' not in kwargs:
            kwargs['myinit_time'] = time.time()
        bonus_init_time = time.time()
        kwargs['bonus_init_time'] = bonus_init_time
        kwargs['evt'] = 'bonus_init'
        kwargs['send_time'] = time.time()
        kwargs['ip'] = self.bonus_ip
        kwargs['port'] = self.bonus_port
        kwargs['timeout'] = self.tcp_timeout
        kwargs['udp_buffer'] = self.tcp_buffer
        kwargs['my_name'] = self.ip
        self.send_q.put(kwargs)
        # data = None
        # while True:
        #     try:
        #         kwargs['send_time'] = time.time()
        #         self.SEND.send(kwargs)
        #         data = self.SEND.recv()
        #         if data is True:
        #             break
        #     except Exception as e:
        #         self.log.error(e, exc_info=True)
        #     time.sleep(1)
        # while self.SEND.poll():
        #     self.SEND.recv()
        # return data

    def order(self, **kwargs):
        tmp = {}
        if self.slee_on_down is True:
            time.sleep(self.sas_sleep)
        if kwargs['bill_block'] is True:
            try:
                self.user_stop_bill = True
                tmp['bill_block'] = self.sas.disable_bill_acceptor()
                if tmp['bill_block'] == None:
                    tmp['bill_block'] = False
                # try:
                #     if self.slee_on_down is True:
                #         time.sleep(self.sas_sleep)
                #     self.sas.enter_maintenance_mode()
                # except Exception:
                #     pass
            except Exception:
                tmp['bill_block'] = False
        else:
            tmp['bill_block'] = True

        # if self.slee_on_down is True:
        #     time.sleep(self.sas_sleep)
        # try:
        #     var = self.sas.send_meters_10_15(False)
        # except sas.BadCRC:
        var = None
        # if var == None:
        for i in range(2):
            if self.slee_on_down is True:
                time.sleep(self.sas_sleep)
            try:
                var = self.sas.send_meters_10_15(False)
            except sas.BadCRC:
                var = None
            if var != None:
                break
        if var == None:
            return None
        if self.set_jp_mether_to_out is True:
            tmp['out'] = var['total_cancelled_credits_meter'] + var['total_jackpot_meter']
        else:
            tmp['out'] = var['total_cancelled_credits_meter']
        tmp['bet'] = var['total_in_meter']
        tmp['won'] = var['total_out_meter']
        tmp['in'] = var['total_droup_meter']
        tmp['jp'] = var['total_jackpot_meter']
        tmp['games played'] = var['games_played_meter']

        # if self.slee_on_down is True:
        #     time.sleep(self.sas_sleep)
        # try:
        #     tmp['bill'] = self.sas.total_dollar_value_of_bills_meter()
        # except sas.BadCRC:
        tmp['bill'] = None
        # if tmp['bill']  == None:
        for i in range(2):
            if self.slee_on_down is True:
                time.sleep(self.sas_sleep)
            try:
                tmp['bill'] = self.sas.total_dollar_value_of_bills_meter()
            except sas.BadCRC:
                tmp['bill'] = None
            if tmp['bill'] != None:
                break
        if None in tmp.values():
            return None
        else:
            return tmp

    def jp_down(self, **kwargs):
        if self.jp_down_by_aft is False or self.use_aft is False:
            return self._jp_down(**kwargs)
        else:
            return self._jp_aft_down(**kwargs)

    def _jp_aft_down(self, **kwargs):
        min_bet = kwargs['min_bet']
        del kwargs['min_bet']
        tax = kwargs['tax']
        mony = kwargs['mony']
        request_time = kwargs['request_time']
        self.jp_clean_transaction_poll = False
        if self.slee_on_down is True:
            time.sleep(self.sas_sleep)
        self.meter['bet'] = self.sas.total_bet_meter()
        self.old_bet = self.meter['bet']
        if self.old_bet == None:
            self.log.warning('jp_down old_bet: %s', self.old_bet)
            return False
        self.db.set('chk_jp_down', False)
        while request_time >= time.time():
            self.smib_reload_securiy = True
            self.init_security_time = time.time() + 30
            if self.slee_on_down is True:
                time.sleep(self.sas_sleep)
                # self.meter['bet'] = self.sas.total_bet_meter()
            try:
                bet = self.sas.send_meters_10_15(True)
            except Exception as e:
                bet = None
            try:
                if bet != None:
                    self.meter['bet'] = bet['total_in_meter']
                else:
                    self.meter['bet'] = None

                if self.meter['bet'] != None and self.old_bet != None:
                    if self.meter['curent credit'] < self.jp_down_if_credit:
                        self.log.warning('jp_by_aft: no credit %s ', self.meter['curent credit'])
                        return False
                    # self.meter['curent credit'] = self.meter['curent credit'] - round(self.meter['bet'] - self.old_bet, 2)
                    self.log.info('old_bet: %s, new_bet: %s' % (self.old_bet, self.meter['bet']))
                    if self.meter['bet'] > self.old_bet:
                        if round(self.meter['bet'] - self.old_bet, 2) >= min_bet:
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            try:
                                if self.check_for_game is True:
                                    if self.pay_by_hand is True:
                                        data = self.sas.AFT_jp(mony, lock_timeout=0)
                                    else:
                                        data = self.sas.AFT_won(mony, lock_timeout=0)
                                else:
                                    if self.pay_by_hand is True:
                                        data = self.sas.AFT_jp(mony, games=1, lock_timeout=0)
                                    else:
                                        data = self.sas.AFT_won(mony, games=1, lock_timeout=0)
                            except Exception as e:
                                self.log.critical(e, exc_info=True)
                                return False
                            self.log.info('down %s, mony %s, bet %s min_bet %s' % (
                            data, mony, round(self.meter['bet'] - self.old_bet, 2), min_bet))
                            if data == None or data is False:
                                self.log.error('jp_by_aft: %s', data)
                                return False
                            elif data == 'NoGame':
                                self.log.warning('jp_by_aft: %s', data)
                                return False
                            elif data['Transfer status'] == 'Full transfer successful':
                                self.jp_clean_transaction_poll = True
                                self.db.set('chk_jp_down', time.time())
                                return True
                            elif data['Transfer status'] == 'Transfer pending (not complete)':
                                self.jp_clean_transaction_poll = True
                                self.db.set('chk_jp_down', time.time())
                                return True
                            else:
                                self.log.warning('jp_by_aft: sas response %s ', data)
                                return False
                        else:
                            self.log.warning('jp_by_aft bo bet: bet %s min_bet %s ' % (
                                round(self.meter['bet'] - self.old_bet, 2), min_bet))
                            return False
                if self.meter['bet'] is not None:
                    self.old_bet = self.meter['bet']
            except Exception as e:
                self.log.error(e, exc_info=True)
                return False
        self.log.warning('jp_by_aft: time out')
        return False

    def _jp_down(self, **kwargs):
        self.db.set('chk_jp_down', False)
        min_bet = kwargs['min_bet']
        del kwargs['min_bet']
        tax = kwargs['tax']
        mony = kwargs['mony']
        request_time = kwargs['request_time']
        if self.slee_on_down is True:
            time.sleep(self.sas_sleep)
        self.meter['bet'] = self.sas.total_bet_meter()
        if self.old_bet == None:
            self.log.warning('jp_down old_bet: %s', self.old_bet)
            return False
        if self.meter['bet'] is not None:
            self.old_bet = self.meter['bet']
        # self.stop_autoplay_now = True
        if self.pay_by_hand is True:
            while request_time > time.time():
                self.smib_reload_securiy = True
                self.init_security_time = time.time() + 30
                if self.meter['curent credit'] < self.jp_down_if_credit:
                    return False
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                try:
                    bet = self.sas.send_meters_10_15(True)
                except Exception as e:
                    bet = None
                try:
                    if bet != None:
                        self.meter['bet'] = bet['total_in_meter']
                    else:
                        self.meter['bet'] = None
                    self.log.info('old_bet: %s, new_bet: %s' % (self.old_bet, self.meter['bet']))
                    if self.meter['bet'] != None and self.old_bet != None:
                        bet = round(self.meter['bet'] - self.old_bet, 2)
                        # self.meter['curent credit'] = self.meter['curent credit'] - bet
                        if bet >= min_bet:
                            self.old_bet = self.meter['bet']
                            self.db.set('chk_jp_down', time.time())
                            return True

                    if self.meter['bet'] is not None:
                        self.old_bet = self.meter['bet']
                except Exception as e:
                    self.log.error(e, exc_info=True)
                    return False
        else:
            while request_time >= time.time():
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                # self.meter['bet'] = self.sas.total_bet_meter()
                try:
                    bet = self.sas.send_meters_10_15(True)
                except Exception as e:
                    bet = None
                try:
                    if bet != None:
                        self.meter['bet'] = bet['total_in_meter']
                    else:
                        self.meter['bet'] = None

                    if self.meter['bet'] != None and self.old_bet != None:
                        if self.meter['curent credit'] < self.jp_down_if_credit:
                            self.log.warning('jp_down: no credit %s ', self.meter['curent credit'])
                            return False
                        # self.meter['curent credit'] = self.meter['curent credit'] - round(self.meter['bet'] - self.old_bet, 2)
                        self.log.info('old_bet: %s, new_bet: %s' % (self.old_bet, self.meter['bet']))
                        if self.meter['bet'] > self.old_bet:
                            if round(self.meter['bet'] - self.old_bet, 2) >= min_bet:
                                if self.slee_on_down is True:
                                    time.sleep(self.sas_sleep)
                                if self.check_for_game is True:
                                    data = self.sas.initiate_legacy_bonus_pay(mony=mony, tax=tax)
                                else:
                                    data = self.sas.initiate_legacy_bonus_pay(mony=mony, tax=tax, games=1)
                                self.log.info('down %s, mony %s, bet %s min_bet %s' % (
                                data, mony, round(self.meter['bet'] - self.old_bet, 2), min_bet))
                                if data is True:
                                    if self.use_security is True:
                                        self.smib_reload_securiy = True
                                        self.init_security_time = time.time() + 30
                                    self.db.set('chk_jp_down', time.time())
                                    return True
                                else:
                                    self.log.warning('jp_down: sas response %s ', data)
                                    return False
                            else:
                                self.log.warning('jp_down bo bet: bet %s min_bet %s ' % (
                                    round(self.meter['bet'] - self.old_bet, 2), min_bet))
                                return False
                        if self.meter['bet'] is not None:
                            self.old_bet = self.meter['bet']
                except Exception as e:
                    self.log.error(e, exc_info=True)
                    return False

        self.log.warning('jp_down: time out')
        return False

    def set_legacy_bonus(self, **kwargs):
        data = self.sas.initiate_legacy_bonus_pay(mony=kwargs['mony'], tax=kwargs['tax'])
        if self.use_security is True and data is True:
            self.smib_reload_securiy = True
            self.init_security_time = time.time() + 30
        return data

    def no_out_befor(self, **kwargs):
        # self.clear_meter()
        # for i in range(3):
        if None in self.meter.values():
            self.log.error('no_out_befor mether %s', self.meter)
            # return True
            #     break
            # time.sleep(self.sas_sleep)
            # self.clear_meter() # FIXME: Ако няма инфо ще бъгне
        if self.emg_type == 4:
            self.no_cust_bonus_out_befor = None
            return True
        self.bonus_revert_old_bet = self.meter['bet']
        # if self.meter['curent credit'] <= self.cust_hold_mony:
        #     credit = 0
        # else:
        credit = self.meter['curent credit']
        self.bonus_is_down = self.meter['won']
        # credit = self.no_cust_bonus_out_befor[3] + won - bet
        if kwargs['no_out_befor'] > kwargs['mony']:
            self.no_cust_bonus_out_befor = [kwargs['no_out_befor'],
                                            self.meter['bet'],
                                            self.meter['won'] + kwargs['mony'],
                                            credit + kwargs['mony']]
        else:
            self.no_cust_bonus_out_befor = None
        self.revert_player_bonus_by_bet = kwargs['bonus_revert_by_bet']
        self.player_bonus_initial = kwargs['no_out_befor']
        self.log.info('no_out_befor: %s', self.no_cust_bonus_out_befor)
        self.bonus_initial = kwargs['mony']
        self.old_out = self.meter['out']
        if 'in' in kwargs:
            if kwargs['in'] is True:
                self.old_in = self.meter['in'] + kwargs['mony']
            else:
                self.old_in = self.meter['in']
        else:
            self.old_in = self.meter['in']
            # raise KeyError, self.player_bonus_initial
        return True

    def client_bonus(self, **kwargs):
        try:
            # if self.cust_bonus_for_hold != None:
            #     self.log.error('CUST BONUS INIT RETURN False, HOLD NOT NONE')
            #     return False
            # self.log.error('run client_bonus')
            # self.stop_autoplay_now = True
            tax = kwargs['tax']
            mony = kwargs['mony']
            bonus_waith_for_in = kwargs['bonus_waith_for_in']
            for i in range(3):
                if self.meter != None:
                    if None not in self.meter.values():
                        break
                self.clear_meter()
            # self.log.error('get mether client_bonus')
            request_time = kwargs['request_time']
            waith_to_play = kwargs['waith_to_play']
            del kwargs['request_time']
            del kwargs['waith_to_play']
            if self.slee_on_down is True:
                time.sleep(self.sas_sleep)
            self.meter['bet'] = self.sas.total_bet_meter()
            self.old_bet = self.meter['bet']
            out = kwargs['out']
            # self.log.error('get bet client_bonus')
            if self.use_aft is False:
                while waith_to_play > time.time():
                    self.smib_reload_securiy = True
                    self.init_security_time = time.time() + 30
                    if self.slee_on_down is True:
                        time.sleep(self.sas_sleep)
                    bet = self.sas.send_meters_10_15(True)
                    if bet != None:
                        self.meter['bet'] = bet['total_in_meter']
                    else:
                        self.meter['bet'] = None
                    self.log.info('old_bet: %s, new_bet: %s' % (self.old_bet, self.meter['bet']))
                    if self.meter['bet'] != None and self.old_bet != None:
                        if self.meter['bet'] > self.old_bet:
                            break
                    elif self.old_bet == None and self.meter['bet'] != None:
                        self.old_bet = self.meter['bet']
                    elif self.meter['bet'] == None and self.old_bet != None:
                        self.meter['bet'] = self.old_bet
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                data = 'NOT_PLAY'
                if self.meter['bet'] != None and self.old_bet != None:
                    if self.meter['bet'] > self.old_bet:
                        if self.check_for_game is True and waith_to_play >= time.time():
                            data = self.sas.initiate_legacy_bonus_pay(mony=mony, tax=tax)
                        else:
                            data = self.sas.initiate_legacy_bonus_pay(mony=mony, tax=tax, games=1)

                if data is True:
                    self.smib_reload_securiy = True
                    self.init_security_time = time.time() + 30
                    evt = 'A legacy bonus pay awarded and/or a multiplied jackpot occurred'
                    if evt == 'A legacy bonus pay awarded and/or a multiplied jackpot occurred':
                        self.log.info('add client bonus: sas response %s', data)
                        if self.use_security is True:
                            self.smib_reload_securiy = True
                            self.init_security_time = time.time() + 30
                        self.player_bonus_initial = mony
                        if kwargs['block_out']:
                            self.no_out_befor(**kwargs['block_out'])
                        if kwargs['hold_bonus']:
                            self.player_hold(**kwargs['hold_bonus'])
                        return True
                elif data == 'NOT_PLAY':
                    # self.old_bet = self.meter['bet']
                    self.log.warning('client_bonus PLAY: time out')
                    return False
                else:
                    self.log.warning('add client bonus: sas response %s', data)
                    return False
            else:
                my_out = None
                for i in range(3):
                    if my_out == None:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        try:
                            self.clear_meter()
                            my_out = self.meter['out']
                            # my_out = all_meter = self.sas.send_meters_10_15(True)
                        except Exception as e:
                            my_out = None
                            self.log.error(e, exc_info=True)
                    else:
                        break
                # self.log.error('get in client_bonus')
                if my_out != None:
                    if bonus_waith_for_in is True and my_out - out >= self.cust_hold_mony:
                        # time.sleep(4)
                        self.log.warning('NO CREDIT FOR BONUS')
                        return 'BREAK'
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                if waith_to_play > time.time() and kwargs['set'] is True:
                    try:
                        if kwargs['restricted'] is False:
                            if self.check_for_game is True:
                                data = self.sas.AFT_won(mony=mony, amount=1)
                            else:
                                data = self.sas.AFT_won(mony=mony, amount=1, games=1)
                        else:
                            data = self.sas.AFT_in(mony=mony, amount=2)
                    except Exception as e:
                        data = None
                        self.log.warning(e, exc_info=True)
                else:
                    return False
                if data == 'NoGame':
                    # time.sleep(4)
                    self.log.warning('NO GAME SELECTED: %s', data)
                    return False
                data = None
                while request_time > time.time():
                    self.smib_reload_securiy = True
                    self.init_security_time = time.time() + 30
                    if data == None or data is False:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        try:
                            data = self.clean_transaction_poll()
                        except sas.BadCRC as e:
                            data = None
                            self.log.info(e, exc_info=True)
                        except sas.BadTransactionID as e:
                            data = None
                            self.log.error(e, exc_info=True)
                        except Exception as e:
                            data = None
                            self.log.error(e, exc_info=True)
                    else:
                        if data['Transfer status'] == 'Full transfer successful':
                            self.old_in = self.meter['in']
                            self.log.info('client_bonus: sas response %s', data)
                            if kwargs['block_out']:
                                self.no_out_befor(**kwargs['block_out'])
                                self.bonus_old_in = self.meter['in']
                            if kwargs['hold_bonus']:
                                self.player_hold(**kwargs['hold_bonus'])
                            return True
                        elif data['Transfer status'] == 'Transfer pending (not complete)':
                            if self.emg_type == 7 or self.emg_type == 8:
                                self.bonus_clear_transaction_pool = True
                                self.old_in = self.meter['in']
                                self.log.info('client_bonus: sas response %s', data)
                                if kwargs['block_out']:
                                    self.no_out_befor(**kwargs['block_out'])
                                if kwargs['hold_bonus']:
                                    self.player_hold(**kwargs['hold_bonus'])
                                return True
                            data = None
                        # elif data['Transfer status'] == 'Gaming machine unable to perform transfers at this time (door open, tilt, disabled, cashout in progress, etc.)':
                        #     if self.mem_server.get('MAKE_IN_OUT'):
                        #         self.mem_server.set('MAKE_IN_OUT', False)
                        #         self.sas.remote_handpay_reset()
                        #     return False

                        else:
                            self.log.error('client_bonus: sas response %s', data)
                            return False
                self.log.warning('client_bonus time out: sas response %s', data)
                if data:
                    try:
                        if data['Transfer status'] == 'Transfer pending (not complete)':
                            return 'CONTINUE'
                    except:
                        return False
                # if self.clean_aft_tranzaction is True:
                return False
                # else:
                #     return True

            # else:
            self.old_bet = self.meter['bet']
            self.log.warning('client_bonus: time out')
            return False
        except Exception as e:
            self.log.error(e, exc_info=True)
            return None

    def player_hold(self, **kwargs):
        # self.clear_meter()
        # self.meter['bet'],
        # self.meter['won'] + kwargs['mony'],
        # self.meter['curent credit'] + kwargs['mony']
        self.cust_bonus_for_hold = kwargs
        self.cust_bonus_for_hold['won'] = self.meter['won']
        self.cust_bonus_for_hold['bet'] = self.meter['bet']
        # if kwargs['bonus_waith_for_in'] is False:
        self.cust_bonus_for_hold['curent credit'] = self.meter['curent credit'] + kwargs['mony']
        # else:
        #     self.cust_bonus_for_hold['curent credit'] = self.meter['curent credit'] + kwargs['mony']*2

        self.log.info('player_hold: %s', self.cust_bonus_for_hold)
        # self.hold_player_bonus_error.append(kwargs)
        # self.db.set('PLAYER_BINUS_HOLD_ERROR', self.hold_player_bonus_error)
        return True

    def bonus_init(self, restricted=False, **kwargs):
        try:
            waith_to_play = kwargs['waith_to_play']
            tax = kwargs['tax']
            mony = kwargs['mony']
            request_time = kwargs['request_time']
            self.log.info('mony: %s, tax: %s' % (mony, tax))
            del kwargs['request_time']
            if self.slee_on_down is True:
                time.sleep(self.sas_sleep)
            if self.use_aft is False:
                if waith_to_play > time.time():
                    self.smib_reload_securiy = True
                    self.init_security_time = time.time() + 30
                    if self.check_for_game is True:
                        data = self.sas.initiate_legacy_bonus_pay(mony=mony, tax=tax)
                    else:
                        data = self.sas.initiate_legacy_bonus_pay(mony=mony, tax=tax, games=1)
                else:
                    return False
                if data is True:
                    # while request_time > time.time():
                    # evt = 'A legacy bonus pay awarded and/or a multiplied jackpot occurred'
                    # if evt == 'A legacy bonus pay awarded and/or a multiplied jackpot occurred':
                    if self.use_security is True:
                        self.smib_reload_securiy = True
                        self.init_security_time = time.time() + 30
                    self.bonus_initial = mony
                    return data
                else:
                    self.log.warning('bonus_init: sas response %s', data)
                    return False
            else:
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                if waith_to_play > time.time():
                    try:
                        if restricted is False:
                            if self.check_for_game is True:
                                data = self.sas.AFT_won(mony=mony, amount=1)
                            else:
                                data = self.sas.AFT_won(mony=mony, amount=1, games=1)
                        else:
                            data = self.sas.AFT_in(mony=mony, amount=2)
                    except Exception as e:
                        data = None
                        self.log.warning(e, exc_info=True)
                else:
                    return False
                if data == 'NoGame':
                    # time.sleep(4)
                    self.log.warning('NO GAME SELECTED: %s', data)
                    return False
                self.smib_reload_securiy = True
                self.init_security_time = time.time() + 30
                data = None
                while request_time > time.time():
                    self.smib_reload_securiy = True
                    self.init_security_time = time.time() + 30
                    if data == None or data is False:
                        time.sleep(self.sas_sleep)
                        try:
                            data = self.clean_transaction_poll()
                        except sas.BadCRC as e:
                            data = None
                            self.log.info(e, exc_info=True)
                        except sas.BadTransactionID as e:
                            data = None
                            self.log.error(e, exc_info=True)
                        except Exception as e:
                            data = None
                            self.log.error(e, exc_info=True)
                    else:
                        if data['Transfer status'] == 'Full transfer successful':
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            # try:
                            #     self.clear_meter()
                            # except Exception as e:
                            #     self.log.error(e, exc_info=True)
                            self.log.info('bonus_init: %s', data)
                            self.old_in = self.meter['in']
                            self.log.info('bonus_init: %s', data)
                            if kwargs['no_out_befor'] > kwargs['mony'] and self.emg_type != 4:
                                # while self.meter['curent credit'] == 0:
                                #     try:
                                #         self.clear_meter()
                                #     except Exception as e:
                                #         self.log.error(e, exc_info=True)
                                self.bonus_is_down = self.meter['won']
                                self.no_bonus_out_befor = [kwargs['no_out_befor'],
                                                           self.meter['bet'],
                                                           self.meter['won'] + kwargs['mony'],
                                                           self.meter['curent credit'] + kwargs['mony']]
                                # else:
                                #     self.no_bonus_out_befor = [kwargs['no_out_befor'],
                                #                                self.meter['bet'],
                                #                                self.meter['won']+kwargs['mony'],
                                #                                self.meter['curent credit']+kwargs['mony'] ]
                                self.bonus_revert_old_bet = self.meter['bet']
                            else:
                                self.no_bonus_out_befor = None
                            self.log.info('%s', self.no_bonus_out_befor)
                            self.bonus_initial = mony
                            self.old_out = self.meter['out']

                            return True
                        elif data['Transfer status'] == 'Transfer pending (not complete)':
                            if self.emg_type == 7 or self.emg_type == 8:
                                self.bonus_clear_transaction_pool = True
                                if self.slee_on_down is True:
                                    time.sleep(self.sas_sleep)
                                self.log.info('bonus_init: %s', data)
                                self.old_in = self.meter['in']
                                self.log.info('bonus_init: %s', data)
                                self.no_bonus_out_befor = [kwargs['no_out_befor'],
                                                               self.meter['bet'],
                                                               self.meter['won'] + kwargs['mony'],
                                                               self.meter['curent credit'] + kwargs['mony']]
                                self.bonus_revert_old_bet = self.meter['bet']
                                self.log.info('%s', self.no_bonus_out_befor)
                                self.bonus_initial = mony
                                self.old_out = self.meter['out']
                                return True
                            time.sleep(self.sas_sleep)
                            # self.log.info('bonus_init: sas response %s', data)
                            data = None
                        else:
                            self.log.error('bonus_init: sas response %s', data)
                            return False
                self.log.warning('bonus_init: sas timeout')
                return False
        except Exception as e:
            self.log.error(e, exc_info=True)
            return None

    def bonus_hold(self, **kwargs):
        # self.bonus_error.append(kwargs)
        # self.db.set('BONUS_ERROR_LOG', self.bonus_error)
        self.clear_meter()
        self.bonus_for_hold = kwargs
        self.bonus_for_hold['won'] = self.meter['won']
        self.bonus_for_hold['bet'] = self.meter['bet']
        self.bonus_for_hold['curent credit'] = self.meter['curent credit']
        return True

    def event_run(self, evt, **kwargs):

        try:
            evt = self.all_event[evt](**kwargs)
            return evt
        except TypeError as e:
            self.log.debug(e, exc_info=True)
            self.log.warning('%s %s', str(evt), str(kwargs))
        except Exception as e:
            self.log.warning('%s %s', str(evt), str(kwargs))
            try:
                raise e
            except:
                pass
            return self.all_event[evt]

    def stop_alarm(self, **kwargs):
        return self.sas.enter_maintenance_mode()

    def start_alarm(self, **kwargs):
        return self.sas.exit_maintanance_mode()

    def game_disable_denomination(self, **kwargs):
        disable_game = self.db.get('GAME_DISABLE')
        game = self.sas.en_dis_game(en_dis=kwargs['disable'])
        if kwargs['disable'] is True:
            if game != None:
                try:
                    disable_game.index(game)
                except ValueError:
                    disable_game.append(game)
        else:
            try:
                del disable_game[disable_game.index(game)]
            except ValueError:
                pass
        self.db.set('GAME_DISABLE', disable_game)
        return True

    def disable_game_from_jackpot(self, **kwargs):
        # print self.all_proc['sas'].my_game
        if self.my_game == None:
            return None
        all_disable = self.db.get('DISABLE_GAME_JP')
        all_disable.append(self.my_game)
        # self.send_event(msg='disable game from jackpot')
        self.db.set('DISABLE_GAME_JP', all_disable)
        self.disable_game_from_jp = self.db.get('DISABLE_GAME_JP')
        return True

    def enable_game_from_jackpot(self, **kwargs):

        if self.my_game == None:
            return None
        all_disable = self.db.get('DISABLE_GAME_JP')
        del all_disable[all_disable.index(self.my_game)]
        self.db.set('DISABLE_GAME_JP', all_disable)
        self.disable_game_from_jp = self.db.get('DISABLE_GAME_JP')
        return True

    def add_won_to_emg(self, **kwargs):
        self.sas.AFT_won(**kwargs)
        self.smib_reload_securiy = True
        self.init_security_time = time.time() + 30
        return self.clean_transaction_poll()

    def add_in_to_emg(self, **kwargs):
        if self.slee_on_down is True:
            time.sleep(self.sas_sleep)
        data_old = self.sas.send_meters_10_15(True)
        if data_old == None:
            return
        waith_to_play = kwargs['waith_to_play']
        if waith_to_play > time.time():
            try:
                response = self.sas.AFT_in(**kwargs)
                self.log.info('%s', response)
                self.smib_reload_securiy = True
                self.init_security_time = time.time() + 30
            except Exception as e:
                response = None
                self.log.error(e, exc_info=True)
            if response:
                if response['Transfer status'] == 'Gaming machine unable to perform transfers at this time (door open, tilt, disabled, cashout in progress, etc.)':
                    self.sas.AFT_clean_transaction_poll()
                    return False
        else:
            return False
        # if not response:
        #     try:
        #         response = self.clean_transaction_poll()
        #     except Exception as e:
        #         self.log.error(e, exc_info=True)
        #     return False
        response = False
        while kwargs['request_time'] > time.time():
            if self.slee_on_down is True:
                time.sleep(self.sas_sleep)
            if not response:
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                try:
                    response = self.clean_transaction_poll()
                except sas.BadCRC as e:
                    response = None
                    self.log.info(e, exc_info=True)
                except sas.BadTransactionID as e:
                    response = None
                    self.log.error(e, exc_info=True)
                except Exception as e:
                    response = None
                    self.log.error(e, exc_info=True)
            else:
                if not response:
                    pass
                elif response['Transfer status'] == 'Full transfer successful':
                    time.sleep(self.sas_sleep)
                    data_new = self.sas.send_meters_10_15(True)
                    if data_new == None:
                        response = None
                    elif data_new['total_droup_meter'] > data_old['total_droup_meter']:
                        return response
                    else:
                        response = None
                elif response['Transfer status'] == 'Transfer pending (not complete)':
                    response = None
                    # self.bonus_clear_transaction_pool = True
                    # return response
                # elif response['Transfer status'] == 'Transfer pending (not complete)':
                #     time.sleep(self.sas_sleep)
                #     response = False
                else:
                    self.log.error('transfer response %s', response)
                    if self.emg_type != 1:
                        time.sleep(4)
                    return False
        return response

    def clean_transaction_poll(self, **kwargs):
        return self.sas.AFT_clean_transaction_poll(register=False, **kwargs)

    def block_out(self, mony, cust=False, out=None):
        # self.clear_meter()
        self.player_bonus_initial = mony
        if self.block_bonus_by_bet is False:
            return self.block_out_by_credit(mony, cust, out)
        else:
            return self.block_out_by_bet(mony, cust, out)

    def block_out_by_bet(self, mony, cust=False, out=None):
        if cust is False:
            hold_mony = self.hold_mony

        else:
            hold_mony = self.cust_hold_mony
        bonus_back = False
        if self.revert_player_bonus_by_bet is False:
            if cust is False:
                won = self.meter['won'] - self.no_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_bonus_out_befor[1]
                my_credit = round(self.no_bonus_out_befor[3] + won - bet, 2)
            else:
                won = self.meter['won'] - self.no_cust_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_cust_bonus_out_befor[1]
                my_credit = round(self.no_cust_bonus_out_befor[3] + won - bet, 2)

            credit = out - self.old_out
            self.old_out = out
            self.log.info(
                'block_out_by_bet_debug my_credit: %s credit: %s, mony: %s mony hold: %s won: %s bet: %s cust %s' % (
                    my_credit, credit, round(mony, 2), hold_mony, won, bet, cust))
            if credit >= hold_mony:
                if my_credit < round(mony, 2) or credit < round(mony, 2):
                    if self.emg_type == 7 or self.emg_type == 9:
                        time.sleep(4)
                    self.log.error('block_out_by_credit my_credit: %s, credit: %s mony: %s mony hold: %s cust: %s' % (
                        my_credit, credit, round(mony, 2), hold_mony, cust))
                    try:
                        self.sas.AFT_in(round(credit, 2))
                    except Exception as e:
                        self.log.error(e, exc_info=True)
                    reset_time = time.time()
                    while True:
                        time.sleep(self.sas_sleep)
                        self.smib_reload_securiy = True
                        self.init_security_time = time.time() + 30
                        try:
                            data = self.clean_transaction_poll()
                        except sas.BadCRC as e:
                            data = None
                            self.log.info(e, exc_info=True)
                        except sas.BadTransactionID as e:
                            data = None
                            self.log.error(e, exc_info=True)
                            # self.send_exception('write_log', msg=u'BAD AFT TRANSACTION')
                            # return bonus_back
                        except Exception as e:
                            data = None
                            self.log.error(e, exc_info=True)
                        if data is False or data == None:
                            pass
                        elif data['Transfer status'] == 'Full transfer successful':

                            self.old_in += credit
                            self.old_out = out
                            if cust is False:
                                self.bonus_initial = credit
                            else:
                                self.player_bonus_initial = credit
                                a = self.mem_server.get('PLAYER_BONUS_REVERT')
                                if a:
                                    if type(a) is not list:
                                        a -= credit
                                        self.mem_server.set('PLAYER_BONUS_REVERT', a)
                            bonus_back = True
                            self.send_exception('write_log', msg=u'BONUS BACK BY AFT %s' % (round(mony, 2)))
                            break
                        elif data['Transfer status'] == 'Transfer pending (not complete)':
                            pass
                        else:
                            self.log.warning('BLOCK AFT OUT ERROR 1: %s, %s' % (round(credit, 2), data))
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.sas.shutdown()
                            return
                        if reset_time + 60 <= time.time():
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.log.warning('BLOCK AFT OUT TIMEOUT 2: %s, %s' % (round(credit, 2), data))
                            self.sas.shutdown()
                            return
                else:
                    if cust is False:
                        self.no_bonus_out_befor = None
                        self.old_in = self.meter['in']
                    else:
                        self.no_cust_bonus_out_befor = None
                        self.old_in = self.meter['in']
            else:
                if cust is False:
                    self.no_bonus_out_befor = None
                else:
                    self.no_cust_bonus_out_befor = None
        else:
            if cust is False:
                won = self.meter['won'] - self.no_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_bonus_out_befor[1]
                my_credit = self.no_bonus_out_befor[3] + won - bet
            else:

                won = self.meter['won'] - self.no_cust_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_cust_bonus_out_befor[1]
                my_credit = self.no_cust_bonus_out_befor[3] + won - bet

            credit = out - self.old_out
            self.old_out = out
            if my_credit >= hold_mony:
                if self.meter['bet'] - self.bonus_revert_old_bet < mony:
                    if self.emg_type == 7 or self.emg_type == 9:
                        time.sleep(4)
                    elif self.slee_on_down is True:
                        time.sleep(self.sas_sleep)
                    self.log.error('block_out_by_credit my_credit: %s, credit: %s mony: %s mony hold: %s cust: %s' % (
                        my_credit, credit, round(mony, 2), hold_mony, cust))
                    try:
                        data = self.sas.AFT_in(round(credit, 2))
                    except Exception as e:
                        self.log.error(e, exc_info=True)
                    reset_time = time.time()
                    while True:
                        self.smib_reload_securiy = True
                        self.init_security_time = time.time() + 30
                        time.sleep(self.sas_sleep)
                        try:
                            data = self.clean_transaction_poll()
                        except sas.BadCRC as e:
                            data = None
                            self.log.info(e, exc_info=True)
                        except sas.BadTransactionID as e:
                            data = None
                            self.log.error(e, exc_info=True)
                            # self.send_exception('write_log', msg=u'BAD AFT TRANSACTION')
                            # return bonus_back
                        except Exception as e:
                            data = None
                            self.log.error(e, exc_info=True)
                        if data is False or data == None:
                            pass
                        elif data['Transfer status'] == 'Full transfer successful':
                            if cust is False:
                                self.bonus_initial = credit
                            else:
                                self.player_bonus_initial = credit
                            self.old_in += credit
                            self.old_out = out
                            bonus_back = True
                            self.send_exception('write_log', msg=u'BONUS BACK BY AFT %s' % (round(mony, 2)))
                            break
                        elif data['Transfer status'] == 'Transfer pending (not complete)':
                            pass
                        else:
                            self.log.warning('BLOCK AFT OUT ERROR 3: %s, %s' % (round(credit, 2), data))
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.sas.shutdown()
                            return
                        if reset_time + 60 <= time.time():
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.log.warning(u'BLOCK AFT OUT TIMEOUT 4: %s, %s' % (round(credit, 2), data))
                            self.sas.shutdown()
                            return
                else:
                    if cust is False:
                        self.no_bonus_out_befor = None
                        self.old_in = self.meter['in']
                    else:
                        # self.get_single_meter(command='enable bill')
                        self.no_cust_bonus_out_befor = None
                        self.old_in = self.meter['in']
                        self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
            else:
                if cust is False:
                    self.no_bonus_out_befor = None
                else:
                    # self.get_single_meter(command='enable bill')
                    self.no_cust_bonus_out_befor = None
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
        return bonus_back

    def block_out_by_credit(self, mony, cust=False, out=None):
        if cust is False:
            hold_mony = self.hold_mony
        else:
            hold_mony = self.cust_hold_mony
        bonus_back = False
        if self.revert_player_bonus_by_bet is False:
            if cust is False:
                won = self.meter['won'] - self.no_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_bonus_out_befor[1]
                my_credit = round(self.no_bonus_out_befor[3] + won - bet, 2)
                self.log.info('BLOCK OUT credit: %s no_bonus_out_befor: %s' % (my_credit, self.no_bonus_out_befor[0]))
            else:
                won = self.meter['won'] - self.no_cust_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_cust_bonus_out_befor[1]
                my_credit = round(self.no_cust_bonus_out_befor[3] + won - bet, 2)
                self.log.info(
                    'BLOCK OUT credit: %s no_cust_bonus_out_befor: %s' % (my_credit, self.no_cust_bonus_out_befor[0]))

            credit = out - self.old_out
            self.log.info('block_out_by_credit debug my_credit: %s, credit: %s mony: %s mony hold: %s cust: %s' % (
                my_credit, credit, round(mony, 2), hold_mony, cust))

            if credit > hold_mony:
                if my_credit < round(mony, 2) or credit < round(mony, 2):
                    if self.emg_type == 7:
                        time.sleep(4)
                    self.log.error('block_out_by_credit my_credit: %s, credit: %s mony: %s mony hold: %s cust: %s' % (
                        my_credit, credit, round(mony, 2), hold_mony, cust))
                    try:
                        self.sas.AFT_in(round(credit, 2))
                    except Exception as e:
                        self.log.error(e, exc_info=True)
                    reset_time = time.time()
                    while True:
                        time.sleep(self.sas_sleep)
                        self.smib_reload_securiy = True
                        self.init_security_time = time.time() + 30
                        try:
                            data = self.clean_transaction_poll()
                        except sas.BadCRC as e:
                            data = None
                            self.log.info(e, exc_info=True)
                        except sas.BadTransactionID as e:
                            data = None
                            self.log.error(e, exc_info=True)
                            # self.send_exception('write_log', msg=u'BAD AFT TRANSACTION')
                            # return bonus_back
                        except Exception as e:
                            data = None
                            self.log.error(e, exc_info=True)
                        if data is False or data == None:
                            pass
                        elif data['Transfer status'] == 'Full transfer successful':
                            self.old_in += credit
                            if cust is False:
                                self.bonus_initial = credit
                            else:
                                self.player_bonus_initial = credit
                            bonus_back = True
                            self.send_exception('write_log', msg=u'BONUS BACK BY AFT %s' % (round(mony, 2)))
                            self.old_out = out
                            a = self.mem_server.get('PLAYER_BONUS_REVERT')
                            if a:
                                if type(a) is not list:
                                    a -= credit
                                    self.mem_server.set('PLAYER_BONUS_REVERT', a)
                            break
                        elif data['Transfer status'] == 'Transfer pending (not complete)':
                            pass
                        else:
                            self.log.warning('BLOCK AFT OUT ERROR 5: %s, %s' % (round(credit, 2), data))
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.sas.shutdown()
                            return
                        if reset_time + 60 <= time.time():
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.log.warning('BLOCK AFT OUT TIMEOUT 6: %s, %s' % (round(credit, 2), data))
                            self.sas.shutdown()
                            return
                else:
                    if cust is False:
                        self.no_bonus_out_befor = None
                        self.old_in = self.meter['in']
                    else:
                        # self.get_single_meter(command='enable bill')
                        self.no_cust_bonus_out_befor = None
                        self.old_in = self.meter['in']
            else:
                if cust is False:
                    self.no_bonus_out_befor = None
                else:
                    # self.get_single_meter(command='enable bill')
                    self.no_cust_bonus_out_befor = None
        else:
            if cust is False:
                won = self.meter['won'] - self.no_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_bonus_out_befor[1]
                my_credit = self.no_bonus_out_befor[3] + won - bet
            else:
                won = self.meter['won'] - self.no_cust_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_cust_bonus_out_befor[1]
                my_credit = self.no_cust_bonus_out_befor[3] + won - bet
            credit = out - self.old_out
            self.old_out = out
            if my_credit >= hold_mony:
                if self.meter['bet'] - self.bonus_revert_old_bet < mony:
                    if self.emg_type == 7:
                        time.sleep(4)
                    elif self.slee_on_down is True:
                        time.sleep(self.sas_sleep)
                    self.log.error(
                        'block_out_by_credit my_credit: %s, credit: %s mony: %s mony hold: %s cust: %s' % (
                            my_credit, credit, round(mony, 2), hold_mony, cust))
                    try:
                        data = self.sas.AFT_in(round(credit, 2))
                    except Exception as e:
                        self.log.error(e, exc_info=True)
                    reset_time = time.time()
                    while True:
                        self.smib_reload_securiy = True
                        self.init_security_time = time.time() + 30
                        time.sleep(self.sas_sleep)
                        try:
                            data = self.clean_transaction_poll()
                        except sas.BadCRC as e:
                            data = None
                            self.log.info(e, exc_info=True)
                        except sas.BadTransactionID as e:
                            data = None
                            self.log.error(e, exc_info=True)
                            # self.send_exception('write_log', msg=u'BAD AFT TRANSACTION')
                            # return bonus_back
                        except Exception as e:
                            data = None
                            self.log.error(e, exc_info=True)
                        if data is False or data == None:
                            pass
                        elif data['Transfer status'] == 'Full transfer successful':
                            if cust is False:
                                self.bonus_initial = credit
                            else:
                                self.player_bonus_initial = credit
                            self.old_in += credit
                            self.old_out = out
                            bonus_back = True
                            self.send_exception('write_log', msg=u'BONUS BACK BY AFT')
                            break
                        elif data['Transfer status'] == 'Transfer pending (not complete)':
                            pass
                        else:
                            self.log.warning('BLOCK AFT OUT ERROR 7 : %s, %s' % (round(credit, 2), data))
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.sas.shutdown()
                            return
                        if reset_time + 60 <= time.time():
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.log.warning('BLOCK AFT OUT TIMEOUT 8: %s, %s' % (round(credit, 2), data))
                            self.sas.shutdown()
                            return
                else:
                    if cust is False:
                        self.no_bonus_out_befor = None
                        self.old_in = self.meter['in']
                    else:
                        # self.get_single_meter(command='enable bill')
                        self.no_cust_bonus_out_befor = None
                        self.old_in = self.meter['in']
                        self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
            else:
                if cust is False:
                    self.no_bonus_out_befor = None
                else:
                    # self.get_single_meter(command='enable bill')
                    self.no_cust_bonus_out_befor = None
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
        return bonus_back

    def get_out_from_emg(self, forbiden=True, croupie_bonus_hold='False', **kwargs):
        try:
            self.clear_meter()
            self.check_bonus_to_clean(reset=True)
            if forbiden is False:
                self.no_bonus_out_befor = None
                self.no_cust_bonus_out_befor = None
                self.player_bonus_initial = 0
                self.bonus_initial = 0
                self.cust_bonus_for_hold = None
                self.bonus_for_hold = None
                if self.slee_on_down is True:
                    time.sleep(self.sas_sleep)
                response1 = self.sas.AFT_out()
                self.log.info('%s', response1)
                self.smib_reload_securiy = True
                self.init_security_time = time.time() + 30
                response = False
                # except sas.BadTransactionID:
                #     response = self.sas.AFT_clean_transaction_poll()
                if response1:
                    for i in range(3):
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        try:
                            response = self.clean_transaction_poll()
                            if response:
                                if response['Transfer status'] == 'Full transfer successful' or response[
                                    'Transfer status'] == 'Transfer pending (not complete)':
                                    break
                            else:
                                return False
                        except Exception as e:
                            self.log.error(e, exc_info=True)
                return response1

            else:
                self.clear_meter()
                self.check_bonus_to_clean(reset=True)
                data_old = self.sas.send_meters_10_15(True)
                if data_old == None:
                    self.mem_server.set('MAKE_IN_OUT', False)
                    return
                if self.no_bonus_out_befor == None and self.no_cust_bonus_out_befor == None:
                    if self.meter['curent credit'] <= 0:
                        self.mem_server.set('MAKE_IN_OUT', False)
                        return False
                    # try:
                    if self.slee_on_down is True:
                        time.sleep(self.sas_sleep)
                    waith_to_play = kwargs['waith_to_play']
                    if waith_to_play >= time.time():
                        if self.cust_bonus_for_hold != None and self.no_cust_bonus_out_befor == None:
                            if self.meter['curent credit'] - self.cust_bonus_for_hold['bonus'] <= 0:
                                self.mem_server.set('MAKE_IN_OUT', False)
                                return False
                        if self.bonus_for_hold != None and self.no_bonus_out_befor == None:
                            if self.meter['curent credit'] - self.bonus_for_hold['bonus'] <= 0:
                                self.mem_server.set('MAKE_IN_OUT', False)
                                return False
                        try:
                            response = self.sas.AFT_out()
                            self.log.info('%s', response)
                            self.smib_reload_securiy = True
                            self.init_security_time = time.time() + 30
                            if response['Transfer status'] == 'Gaming machine unable to perform transfers at this time (door open, tilt, disabled, cashout in progress, etc.)':
                                self.sas.AFT_clean_transaction_poll()
                                return response
                        except Exception as e:
                            self.log.error(e, exc_info=True)
                            # try:
                            #     response = self.clean_transaction_poll()
                            # except Exception as e:
                            #     self.log.error(e, exc_info=True)
                            # return False
                    else:
                        self.mem_server.set('MAKE_IN_OUT', False)
                        return False
                    # if not response:
                    #     # self.mem_server.set('MAKE_IN_OUT', False)
                    #     return False
                    response = False
                    while kwargs['request_time'] > time.time():
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        if not response:
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            try:
                                response = self.sas.AFT_clean_transaction_poll()
                            except sas.BadCRC as e:
                                response = None
                                self.log.info(e, exc_info=True)
                            except sas.BadTransactionID as e:
                                response = None
                                self.log.error(e, exc_info=True)
                            except Exception as e:
                                response = None
                                self.log.error(e, exc_info=True)
                        # else:
                        if not response:
                            pass
                        elif response['Transfer status'] == 'Full transfer successful':
                            time.sleep(self.sas_sleep)
                            data_new = self.sas.send_meters_10_15(True)
                            if data_new == None:
                                response = None
                            elif data_new['total_cancelled_credits_meter'] > data_old['total_cancelled_credits_meter']:
                                if self.bonus_for_hold != None and self.no_bonus_out_befor == None:
                                    won = self.meter['won'] - self.bonus_for_hold['won']
                                    bet = self.meter['bet'] - self.bonus_for_hold['bet']
                                    credit = round(float(response['Cashable amount']), 2)
                                    if credit > self.hold_mony:
                                        self.bonus_for_hold['credit'] = credit
                                        self.send_honus_hold_data(**self.bonus_for_hold)
                                        if croupie_bonus_hold == 'True':
                                            response['Cashable amount'] -= self.bonus_for_hold['bonus']
                                    self.bonus_for_hold = None
                                # self.log.info('for hold %s, \n out %s credit %s' % (
                                # self.cust_bonus_for_hold, self.no_cust_bonus_out_befor, my_old_credit))
                                if self.cust_bonus_for_hold != None and self.no_cust_bonus_out_befor == None:
                                    won = self.meter['won'] - self.cust_bonus_for_hold['won']
                                    bet = self.meter['bet'] - self.cust_bonus_for_hold['bet']
                                    credit = round(float(response['Cashable amount']), 2)
                                    self.log.warning('credit %s, cust_hold_mony %s' % (credit, self.cust_hold_mony))
                                    if credit > self.cust_hold_mony:
                                        self.cust_bonus_for_hold['credit'] = credit
                                        self.send_player_hold_data(**self.cust_bonus_for_hold)
                                        if croupie_bonus_hold == 'True':
                                            response['Cashable amount'] -= self.cust_bonus_for_hold['bonus']
                                    self.cust_bonus_for_hold = None
                                self.smib_reload_securiy = True
                                self.init_security_time = time.time() + 30
                                return response
                            else:
                                response = None
                        elif response['Transfer status'] == 'Transfer pending (not complete)':
                            response = None
                        else:
                            self.log.error('transfer response %s', response)
                            if self.emg_type != 1:
                                time.sleep(4)
                            # self.mem_server.set('MAKE_IN_OUT', False)
                            return response
                    # self.mem_server.set('MAKE_IN_OUT', False)
                    self.log.error('aft_out_from_emg timeout %s', response)
                    return False
                elif self.no_bonus_out_befor != None:
                    bet = self.meter['bet']
                    won = self.meter['won']
                    self.log.error(
                        'block_out no_cust_bonus_out_befor: %s, mony: %s, won: %s bet: %s' % (
                        self.no_cust_bonus_out_befor, self.meter['curent credit'], won, bet))
                    self.mem_server.set('MAKE_IN_OUT', False)
                    return 'NO OUT'
                elif self.no_cust_bonus_out_befor != None:
                    bet = self.meter['bet']
                    won = self.meter['won']
                    self.log.error(
                        'block_out no_cust_bonus_out_befor: %s, mony: %s, won: %s bet: %s' % (self.no_cust_bonus_out_befor, self.meter['curent credit'],won, bet))
                    self.mem_server.set('MAKE_IN_OUT', False)
                    return 'NO OUT'
                elif self.bonus_for_hold != None:
                    bet = self.meter['bet']
                    won = self.meter['won']
                    self.log.error(
                        'block_out bonus_for_hold: %s, mony: %s, won: %s bet: %s' % (
                        self.bonus_for_hold, self.meter['curent credit'], won, bet))
                    self.mem_server.set('MAKE_IN_OUT', False)
                    return 'NO OUT'
            # else:
            #     return False
        except Exception as e:
            self.log.error(e, exc_info=True)
        return False

    def send_mail(self, **kwargs):
        try:
            kwargs['send_time'] = time.time()
            kwargs['ip'] = self.bonus_ip
            kwargs['port'] = self.bonus_port
            kwargs['timeout'] = self.tcp_timeout
            kwargs['udp_buffer'] = self.tcp_buffer
            kwargs['evt'] = 'send_mail_won'
            kwargs['my_name'] = self.ip
            # if 'cash_out' not in kwargs:
            # kwargs['cash_out'] = False
            self.send_q.put(kwargs)
            # self.SEND.send(kwargs)
            # else:
            #     # kwargs['cash_out'] = True
            #     self.SEND.send(kwargs)
        except Exception as e:
            self.log.error(e, exc_info=True)
        return True

    def check_bonus_to_clean(self, reset=False):
        # return
        if None in self.meter.values():
            return False
        if self.meter['curent credit'] != None:
            if self.meter['curent credit'] <= self.cust_hold_mony:
                self.db.set('CART_CHANGE', False)
        if self.block_bonus_by_bet is False:
            return self.check_bonus_to_clean_by_credit(reset)
        else:
            return self.check_bonus_to_clean_by_bet(reset)

    def check_bonus_to_clean_by_bet(self, reset=False):
        if self.use_aft is False:
            self.bonus_initial = 0
            self.player_bonus_initial = 0
        if self.no_bonus_out_befor != None:
            self.log.debug('no_bonus_out_befor %s', str(self.no_bonus_out_befor))
            won = self.meter['won'] - self.no_bonus_out_befor[2]
            bet = self.meter['bet'] - self.no_bonus_out_befor[1]
            if self.bonus_initial != 0 and self.bonus_is_down != self.meter['won']:
                self.bonus_initial = 0
            elif self.no_bonus_out_befor[3] + won - bet <= self.hold_mony and self.bonus_initial == 0:
                # self.log.error('1 %s' % (self.no_bonus_out_befor))
                self.no_bonus_out_befor = None
                self.bonus_initial = 0
            elif self.no_bonus_out_befor[3] + won - bet >= self.no_bonus_out_befor[0] and self.bonus_initial == 0:
                # self.log.error('2 %s %s %s' % (self.no_bonus_out_befor, self.no_bonus_out_befor[3]+won-bet, self.bonus_initial))
                self.no_bonus_out_befor = None
                self.bonus_initial = 0
                # self.bonus_for_hold = None

        if self.revert_player_bonus_by_bet is False:
            if self.no_cust_bonus_out_befor != None:
                self.log.debug('no_cust_bonus_out_befor %s', str(self.no_cust_bonus_out_befor))
                won = self.meter['won'] - self.no_cust_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_cust_bonus_out_befor[1]
                self.log.debug(
                    '%s, %s' % (self.no_cust_bonus_out_befor[3] + won - bet, self.no_cust_bonus_out_befor[0]))
                if self.player_bonus_initial != 0 and self.bonus_is_down != self.meter['won']:
                    self.player_bonus_initial = 0
                elif self.no_cust_bonus_out_befor[
                    3] + won - bet <= self.cust_hold_mony and self.player_bonus_initial == 0:
                    self.no_cust_bonus_out_befor = None
                    self.get_single_meter(command='enable bill')
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.bonus_revert_old_bet = None
                    self.player_bonus_initial = 0
                elif self.no_cust_bonus_out_befor[3] + won - bet >= self.no_cust_bonus_out_befor[
                    0] and self.player_bonus_initial == 0:
                    # raise KeyError, (self.no_cust_bonus_out_befor[3]+won-bet, self.no_cust_bonus_out_befor[0])
                    self.no_cust_bonus_out_befor = None
                    self.get_single_meter(command='enable bill')
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.bonus_revert_old_bet = None
                    self.player_bonus_initial = 0
        else:
            if self.no_cust_bonus_out_befor != None:
                won = self.meter['won'] - self.no_cust_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_cust_bonus_out_befor[1]
                self.log.debug('bet: %s no_bonus_out_befor: %s' % (bet, self.player_bonus_initial))
                if self.player_bonus_initial != 0 and self.bonus_is_down != self.meter['won']:
                    # self.log.error('1')
                    self.player_bonus_initial = 0
                elif self.no_cust_bonus_out_befor[0] + won - bet <= self.cust_hold_mony:
                    self.no_cust_bonus_out_befor = None
                    self.get_single_meter(command='enable bill')
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.bonus_revert_old_bet = None
                    self.player_bonus_initial = 0
                elif bet >= self.no_cust_bonus_out_befor[0]:
                    self.no_cust_bonus_out_befor = None
                    self.get_single_meter(command='enable bill')
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.bonus_revert_old_bet = None
                    self.player_bonus_initial = 0
        # self.log.error('cust_bonus_for_hold %s, player_bonus_initial: %s, no_cust_bonus_out_befor: %s' % (self.cust_bonus_for_hold, self.player_bonus_initial, self.no_cust_bonus_out_befor))
        if self.bonus_for_hold != None and self.bonus_initial == 0 and self.no_bonus_out_befor == None:
            won = self.meter['won'] - self.bonus_for_hold['won']
            bet = self.meter['bet'] - self.bonus_for_hold['bet']
            credit = self.meter['curent credit']
            if credit <= self.hold_mony:
                self.bonus_for_hold = None
        # else:
        #     self.bonus_initial = 0
        # self.log.debug('no_cust_bonus_out_befor %s player_bonus_initial %s cust_bonus_for_hold %s' % (
        # str(self.no_cust_bonus_out_befor), self.player_bonus_initial, self.cust_bonus_for_hold))
        if self.cust_bonus_for_hold != None and self.player_bonus_initial == 0 and self.no_cust_bonus_out_befor == None:
            # self.log.debug('no_cust_bonus_out_befor %s', str(self.no_cust_bonus_out_befor))
            won = self.meter['won'] - self.cust_bonus_for_hold['won']
            bet = self.meter['bet'] - self.cust_bonus_for_hold['bet']
            credit = self.meter['curent credit']
            if credit <= self.cust_hold_mony:
                self.cust_bonus_for_hold = None
                self.mem_server.set('PLAYER_PLAY_BONUS_MONY', [0, 0])
        # else:
        #     self.player_bonus_initial = 0

    def check_bonus_to_clean_by_credit(self, reset=False):
        if self.use_aft is False:
            self.bonus_initial = 0
            self.player_bonus_initial = 0

        if self.no_bonus_out_befor != None:
            self.log.debug('no_bonus_out_befor %s', str(self.no_bonus_out_befor))
            # self.log.debug('no_cust_bonus_out_befor %s', str(self.no_cust_bonus_out_befor))
        if self.no_cust_bonus_out_befor != None:
            self.log.debug('no_cust_bonus_out_befor %s', str(self.no_cust_bonus_out_befor))
            # self.log.debug('no_cust_bonus_out_befor %s', str(self.no_cust_bonus_out_befor))

        if self.no_bonus_out_befor != None:
            self.log.debug('no_bonus_out_befor %s', str(self.no_bonus_out_befor))
            won = self.meter['won'] - self.no_bonus_out_befor[2]
            bet = self.meter['bet'] - self.no_bonus_out_befor[1]
            if self.bonus_initial != 0 and self.bonus_is_down != self.meter['won']:
                self.bonus_initial = 0
            elif self.no_bonus_out_befor[3] + won - bet <= self.hold_mony and self.bonus_initial == 0:
                # self.log.error('1 %s' % (self.no_bonus_out_befor))
                self.no_bonus_out_befor = None
                self.bonus_initial = 0
            elif self.no_bonus_out_befor[3] + won - bet >= self.no_bonus_out_befor[0] and self.bonus_initial == 0 and reset is True:
                # self.log.error('2 %s %s %s' % (self.no_bonus_out_befor, self.no_bonus_out_befor[3]+won-bet, self.bonus_initial))
                self.no_bonus_out_befor = None
                self.bonus_initial = 0
                # self.bonus_for_hold = None

        if self.revert_player_bonus_by_bet is False:
            if self.no_cust_bonus_out_befor != None:
                won = self.meter['won'] - self.no_cust_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_cust_bonus_out_befor[1]
                # won = self.meter['won'] - self.no_bonus_out_befor[2]
                # bet = self.meter['bet'] - self.no_bonus_out_befor[1]
                credit = self.no_cust_bonus_out_befor[3] + won - bet
                if self.meter['in'] != self.old_in:
                    # if self.meter['in']> self.old_in:
                    # self.no_cust_bonus_out_befor[0] += (self.meter['in'] - self.old_in)
                    self.old_in = self.meter['in']
                    self.player_bonus_initial = credit

                # self.log.debug(
                #     'cust credit: %s no_cust_bonus_out_befor: %s' % (credit, self.no_cust_bonus_out_befor[0]))
                if self.no_cust_bonus_out_befor[0] >= self.player_bonus_initial and self.player_bonus_initial != 0 and self.bonus_is_down != self.meter['won']:
                    self.player_bonus_initial = 0
                elif credit <= self.cust_hold_mony and self.player_bonus_initial == 0 and self.meter[
                    'curent credit'] <= self.cust_hold_mony:
                    self.no_cust_bonus_out_befor = None
                    self.get_single_meter(command='enable bill')
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.bonus_revert_old_bet = None
                    self.player_bonus_initial = 0
                elif credit+0.01 >= self.no_cust_bonus_out_befor[0] and self.player_bonus_initial == 0 and reset is True:
                    self.get_single_meter(command='enable bill')
                    self.no_cust_bonus_out_befor = None
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.bonus_revert_old_bet = None
                    self.player_bonus_initial = 0
                elif credit < self.cust_hold_mony and self.player_bonus_initial == 0 and reset is True:
                    self.get_single_meter(command='enable bill')
                    self.no_cust_bonus_out_befor = None
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.bonus_revert_old_bet = None
                    self.player_bonus_initial = 0
        else:
            if self.no_cust_bonus_out_befor != None:
                won = self.meter['won'] - self.no_cust_bonus_out_befor[2]
                bet = self.meter['bet'] - self.no_cust_bonus_out_befor[1]
                self.log.debug('bet: %s no_bonus_out_befor: %s' % (bet, self.player_bonus_initial))
                if bet >= self.player_bonus_initial and self.player_bonus_initial != 0 and self.bonus_is_down != self.meter['won']:
                    # self.log.error('1')
                    self.player_bonus_initial = 0
                elif self.no_cust_bonus_out_befor[3] + won - bet <= self.cust_hold_mony:
                    self.no_cust_bonus_out_befor = None
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.bonus_revert_old_bet = None
                    self.get_single_meter(command='enable bill')
                    self.player_bonus_initial = 0
                elif bet >= self.no_cust_bonus_out_befor[0]:
                    self.no_cust_bonus_out_befor = None
                    self.mem_server.set('PLAYER_BONUS_REVERT', [0, 0])
                    self.bonus_revert_old_bet = None
                    self.player_bonus_initial = 0
                    self.get_single_meter(command='enable bill')
        if self.bonus_for_hold != None and self.bonus_initial == 0 and self.no_bonus_out_befor == None:
            won = self.meter['won'] - self.bonus_for_hold['won']
            bet = self.meter['bet'] - self.bonus_for_hold['bet']
            credit = self.meter['curent credit']
            if credit <= self.hold_mony:
                self.bonus_for_hold = None
        # else:
        #     self.bonus_initial = 0
        # self.log.info('no_cust_bonus_out_befor %s player_bonus_initial %s cust_bonus_for_hold %s' % (str(self.no_cust_bonus_out_befor), self.player_bonus_initial, self.cust_bonus_for_hold))
        if self.cust_bonus_for_hold != None and self.player_bonus_initial == 0 and self.no_cust_bonus_out_befor == None:
            self.log.debug('no_cust_bonus_out_befor %s', str(self.no_cust_bonus_out_befor))
            won = self.meter['won'] - self.cust_bonus_for_hold['won']
            bet = self.meter['bet'] - self.cust_bonus_for_hold['bet']
            credit = self.meter['curent credit']
            if credit <= self.cust_hold_mony:
                self.cust_bonus_for_hold = None
                # self.mem_server.set('PLAYER_PLAY_BONUS_MONY', [0, 0])
        # else:
        #     self.player_bonus_initial = 0

    def out_event(self, event=None):
        my_old_credit = self.meter['curent credit']
        block_one_time = False
        out = 0
        self.check_bonus_to_clean(reset=True)
        i_make_out = False
        self.old_out = self.meter['out']
        if self.use_aft is True:
            try:
                if self.no_bonus_out_befor == None and self.no_cust_bonus_out_befor == None:
                    if block_one_time is False and self.emg_type != 4:
                        self.sas.AFT_cashout_enable()
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        # data = self.sas.AFT_cansel_request()
                        data = self.sas.AFT_clean_transaction_poll()
                        self.log.debug('%s', data)
                        event = None
                elif event == 'AFT request for host cashout':
                    data = None
                    try:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        if self.emg_type != 4:
                            self.sas.AFT_out(lock_timeout=0)
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            data = self.sas.AFT_clean_transaction_poll()
                            if not data:
                                pass
                            elif data['Transfer status'] == 'Full transfer successful' or data[
                                'Transfer status'] == 'Transfer pending (not complete)':
                                i_make_out = True
                                pass
                            else:
                                event = None
                    except Exception as e:
                        event = None
                        self.log.error(e, exc_info=True)
                    self.log.debug('%s', data)
                # elif event == 'Cash out button pressed':
                #     event = None
                # try:
                #     self.sas.remote_handpay_reset()
                # except Exception as e:
                #     event = None
                #     self.log.error(e, exc_info=True)
                else:
                    event = None
            except Exception as e:
                self.log.info(e, exc_info=True)
            if self.no_bonus_out_befor != None or self.no_cust_bonus_out_befor != None and event == 'AFT request for host cashout':

                my_time = time.time()
                while True:
                    try:
                        self.clear_meter()
                        out = self.meter['out']
                    except sas.BadCRC as e:
                        time.sleep(self.sas_sleep)
                    except Exception as e:
                        out = 0
                        self.log.error(e, exc_info=True)
                    if self.mem_server.get('MAKE_IN_OUT'):
                        self.mem_server.set('MAKE_IN_OUT', False)
                        try:
                            self.sas.remote_handpay_reset()
                        except:
                            pass
                    if self.slee_on_down is True:
                        time.sleep(self.sas_sleep)

                    if not out:
                        self.log.warning('out block: no out')
                        pass
                    elif self.old_out == None:
                        self.log.warning('out block: no old_out')
                        self.old_out = out
                    elif out < self.old_out:
                        self.log.error('out block: out revert')
                        self.no_bonus_out_befor = None
                        self.no_cust_bonus_out_befor = None
                        i_make_out = True
                        break
                    elif out == self.old_out:
                        self.log.info('out block: old_out: %s out: %s' % (self.old_out, out))
                        pass
                    else:
                        i_make_out = True
                        break
                    if my_time + 120 <= time.time():
                        self.log.error('out block: make cache out')
                        my_time = time.time()
                # if self.emg_type != 1:
                time.sleep(4)  # FIXME: Връщане на бонус
            in_again = out - self.old_out
            self.log.info('for hold_bonus %s, hold_cust %s \n out %s credit %s' % (
                self.cust_bonus_for_hold, self.no_cust_bonus_out_befor, out, my_old_credit))
            if self.no_bonus_out_befor != None:
                block_one_time = self.block_out(self.no_bonus_out_befor[0], out=out)
            if self.no_cust_bonus_out_befor != None and block_one_time is False:
                block_one_time = self.block_out(self.no_cust_bonus_out_befor[0], True, out=out)
            if self.no_cust_bonus_out_befor == None and self.no_bonus_out_befor == None and event == 'AFT request for host cashout' and block_one_time is False and i_make_out is True:
                try:
                    if self.slee_on_down is True:
                        time.sleep(self.sas_sleep)
                    self.sas.AFT_in(in_again)

                    while True:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        data = self.sas.AFT_clean_transaction_poll()
                        if not data:
                            pass
                        elif data['Transfer status'] == 'Full transfer successful' or data[
                            'Transfer status'] == 'Transfer pending (not complete)':
                            break
                    self.mem_server.set('PLAYER_BONUS_REVERT', None)
                    # try:
                    #     self.sas.AFT_initial_out()
                    #     self.sas.AFT_clean_transaction_poll()
                    # except:
                    #     pass
                except Exception as e:
                    self.log.error(e, exc_info=True)
                    self.sas.shutdown()
            elif self.no_cust_bonus_out_befor != None or self.no_bonus_out_befor != None and block_one_time:
                pass
            else:
                self.mem_server.set('PLAYER_BONUS_REVERT', None)
            # try:
            #     if block_one_time is False:
            #         if self.slee_on_down is True:
            #             time.sleep(self.sas_sleep)
            #         self.sas.AFT_cashout_enable()
            #
            #         # data = self.sas.AFT_cansel_request()
            #         data = self.sas.AFT_clean_transaction_poll()
            #         self.log.info('%s', data)
            # except Exception as e:
            #     self.log.info(e, exc_info=True)

        else:
            self.no_bonus_out_befor = None
            self.no_cust_bonus_out_befor = None

        self.log.info('%s', self.event)
        if self.notifiti_if_won is True:
            if my_old_credit != None:
                if my_old_credit >= self.notifity_if_won_mony:
                    self.send_mail(won=round(my_old_credit, 2), cash_out=True)

        if self.bonus_for_hold != None and self.no_bonus_out_befor == None:
            won = self.meter['won'] - self.bonus_for_hold['won']
            bet = self.meter['bet'] - self.bonus_for_hold['bet']
            credit = my_old_credit
            if credit > self.hold_mony:
                self.bonus_for_hold['credit'] = credit
                self.send_honus_hold_data(**self.bonus_for_hold)
            self.bonus_for_hold = None
        # self.log.info('for hold %s, \n out %s credit %s' % (
        # self.cust_bonus_for_hold, self.no_cust_bonus_out_befor, my_old_credit))
        if self.cust_bonus_for_hold != None and self.no_cust_bonus_out_befor == None:
            won = self.meter['won'] - self.cust_bonus_for_hold['won']
            bet = self.meter['bet'] - self.cust_bonus_for_hold['bet']
            credit = my_old_credit
            self.log.warning('credit %s, cust_hold_mony %s' % (credit, self.cust_hold_mony))
            if credit > self.cust_hold_mony:
                self.cust_bonus_for_hold['credit'] = credit
                self.send_player_hold_data(**self.cust_bonus_for_hold)
            self.cust_bonus_for_hold = None
        self.smib_reload_securiy = True
        self.init_security_time = time.time() + 30
        self.clear_meter()

    def run(self):
        # self.sas.clean_buffer()
        aft_request = False
        cache_out_pressed = False
        t = threading.Thread(target=self._send_to_server, args=[self.send_q, self.SEND, self.log])
        t.start()
        while True:
            if t.is_alive() == False:
                self.send_q = Queue()
                t = threading.Thread(target=self._send_to_server, args=[self.send_q, self.SEND, self.log])
                t.start()
            my_time = time.time()
            self.working_mod = self.db.get('WORKING_MODULE')
            # aft_out = False
            if self.sas == None:
                try:
                    if self.conf.get('SAS', 'usb', 'bool') is True:
                        self.port = '/dev/ia'
                        self.sas = sas.SAS_USB(port=self.port, timeout=self.timeout, log=self.log,
                                               aft_check_last_transaction=self.aft_check_last_transaction, sas_dump=self.sas_dump,
                                               denom=self.coef_my_denom, lock_time=self.conf.get('SAS', 'aft_lock_time', 'int'),
                                               get_aft_transaction_from_EMG=self.last_aft_transaction_from_emg)
                    else:
                        # realise = os.popen('lsb_release -a | grep Description:').read()
                        # if 'buster' in realise:
                        self.port = '/dev/ttyS4'
                        # else:
                        #     self.port = '/dev/ttyS1'
                        self.sas = sas.Sas(port=self.port, timeout=self.timeout, log=self.log,
                                           aft_check_last_transaction=self.aft_check_last_transaction, sas_dump=self.sas_dump,
                                           denom=self.coef_my_denom, lock_time=self.conf.get('SAS', 'aft_lock_time', 'int'),
                                           get_aft_transaction_from_EMG=self.last_aft_transaction_from_emg)
                    if self.sas_n != '00':
                        self.sas.mashin_n = self.sas_n
                        self.sas.adress = int(self.sas_n)
                    # else:
                    #     self.sas.start()
                except Exception as e:
                    self.sas = None
                    self.log.critical(e, exc_info=True)
            else:
                try:
                    if not self.sas.mashin_n and self.sas_n == '00':
                        self.sas.start()
                        self.sas_n = self.sas.mashin_n
                        # time.sleep(5)
                    # elif self.coef_use is False:
                    #     denom = None
                    #     while denom == None:
                    #         denom = self.sas.gaming_machine_ID()
                    #         if denom != None:
                    #             break
                    #         self.log.error('no Coef: %s', denom)
                    #         time.sleep(5)
                    #     self.sas.denom = denom
                    #     self.coef_use = True
                    #     self.log.info('get emg Coef: %s', self.sas.denom)
                    # elif self.sas.denom != self.coef_my_denom:
                    #     self.sas.denom = self.coef_my_denom
                    elif self.my_game == None and self.check_for_game is True:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        self.my_game = self.sas.selected_game_number()
                        self.log.info('get emg Game Selected: %s', self.my_game)
                        if not self.my_game:
                            self.my_game = '0000'
                    elif self.db_security == None and self.use_security is True:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)

                        self.security_reload()
                    elif self.emg_security == None and self.use_security is True:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        self.security_get()
                    elif self.sync_datetime is True:
                        self.log.info('sync emg time')
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        self.sync_time_now()
                        self.sync_datetime = False
                    elif self.delay_rill is False and self.rill_hold is True:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        self.sas.delay_game(delay_time=0)
                        self.rill_hold_time = None
                        self.rill_hold = False
                    elif self.delay_rill is True and self.rill_hold is True:
                        delay_time_now = self.stop_autoplay_time[random.randint(0, len(self.stop_autoplay_time) - 1)]
                        self.log.info('start delay: %s', delay_time_now)
                        self.rill_hold = False
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        self.sas.delay_game(delay_time=delay_time_now)
                        self.rill_hold_time = time.time()
                    # elif self.rill_hold is False and self.delay_rill is True:
                    #     if self.slee_on_down is True:
                    #         time.sleep(self.sas_sleep)
                    #     self.sas.delay_game(delay_time=0)
                    #     self.rill_hold = False
                    elif self.aft_register_initial is False and self.use_aft is True:
                        data = None
                        for i in range(3):
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            try:
                                data = self.sas.AFT_register_initial()
                                if data != None:
                                    break
                            except:
                                data = None
                        self.log.info('aft register: %s', data)
                        for i in range(3):
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            try:
                                data = self.sas.AFT_register(mk_reg=True)
                                if data != None:
                                    break
                            except:
                                data = None
                            # time.sleep(self.sas_sleep)
                        self.log.info('aft register: %s', data)
                        self.aft_register_initial = True
                        try:
                            self.sas.AFT_clean_transaction_poll()
                        except Exception:
                            pass
                    elif self.disable_all_games is True:
                        self.disable_all_games = False
                        disable_game = self.db.get('GAME_DISABLE')
                        if disable_game != []:
                            self.log.warning('disable games: %s', disable_game)
                        for i in disable_game:
                            self.log.info('disable game %s', i)
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.sas.en_dis_game(en_dis=True, game_number=i)
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        self.sas.startup()
                    elif not self.sas.transaction and self.use_aft is True:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        if not self.db.get('AFT_TRANSACTION') or self.db.get('AFT_TRANSACTION') == 0:
                            self.sas.transaction = self.sas.AFT_get_last_transaction()
                            for i in range(3):
                                if self.sas.transaction:
                                    if self.sas.transaction == int('2020202020202020202020202020202021', 16):
                                        if self.slee_on_down is True:
                                            time.sleep(self.sas_sleep)
                                        self.sas.transaction = self.sas.AFT_get_last_transaction()
                                    else:
                                        break
                                else:
                                    self.sas.transaction = self.sas.AFT_get_last_transaction()
                                time.sleep(self.sas_sleep)
                            self.db.set('AFT_TRANSACTION', self.sas.transaction)
                        else:
                            self.sas.transaction = self.db.get('AFT_TRANSACTION')
                    elif self.bonus_clear_transaction_pool is True:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        data = None
                        while True:
                            self.smib_reload_securiy = True
                            self.init_security_time = time.time() + 30
                            try:
                                if data == None or data is False:
                                    # if self.slee_on_down is True:
                                    #     time.sleep(self.sas_sleep)
                                    try:
                                        data = self.clean_transaction_poll()
                                    except sas.BadCRC as e:
                                        data = None
                                        self.log.info(e, exc_info=True)
                                    except sas.BadTransactionID as e:
                                        data = None
                                        self.log.error(e, exc_info=True)
                                    except Exception as e:
                                        data = None
                                        self.log.error(e, exc_info=True)
                                else:
                                    if data['Transfer status'] == 'Full transfer successful':
                                        self.bonus_clear_transaction_pool = False
                                        break
                                    elif data['Transfer status'] == 'Transfer pending (not complete)':
                                        data = None
                                    else:
                                        self.log.critical('jp_by_aft clean transaction: %s', data)
                                        self.bonus_clear_transaction_pool = False
                                        break
                            except Exception as e:
                                self.log.critical(e, exc_info=True)
                                self.bonus_clear_transaction_pool = False

                    elif self.jp_clean_transaction_poll is True and self.jp_down_by_aft is True:
                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        data = None
                        while True:
                            self.smib_reload_securiy = True
                            self.init_security_time = time.time() + 30
                            try:
                                if data == None or data is False:
                                    if self.slee_on_down is True:
                                        time.sleep(self.sas_sleep)
                                    try:
                                        data = self.clean_transaction_poll()
                                    except sas.BadCRC as e:
                                        data = None
                                        self.log.info(e, exc_info=True)
                                    except sas.BadTransactionID as e:
                                        data = None
                                        self.log.error(e, exc_info=True)
                                    except Exception as e:
                                        data = None
                                        self.log.error(e, exc_info=True)
                                else:
                                    if data['Transfer status'] == 'Full transfer successful':
                                        self.jp_clean_transaction_poll = False
                                        break
                                    elif data['Transfer status'] == 'Transfer pending (not complete)':
                                        data = None
                                    else:
                                        self.log.critical('jp_by_aft clean transaction: %s', data)
                                        self.jp_clean_transaction_poll = False
                                        break
                            except Exception as e:
                                self.log.critical(e, exc_info=True)
                                self.jp_clean_transaction_poll = False
                                break

                    else:

                        if self.smib_reload_securiy is True and self.use_security is True:
                            self.init_security_time = my_time
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.security_reload()
                            self.init_security_time = my_time + 30
                            self.smib_reload_securiy + False
                        if self.init_security_time + 30 <= my_time and self.use_security is True:
                            # time.sleep(self.sas_sleep)
                            self.init_security_time = my_time + 30
                            if self.securite_check() is False:
                                if self.slee_on_down is True:
                                    time.sleep(self.sas_sleep)
                                self.sas.shutdown()
                        self.clear_meter()
                        self.check_bonus_to_clean()
                        if self.no_cust_bonus_out_befor and self.meter:
                            a = self.mem_server.get('PLAYER_BONUS_REVERT')
                            if a:
                                if type(a) is not list and self.bonus_old_in != self.meter['in']:
                                    if self.bonus_old_in and self.meter['in']:
                                        a += self.meter['in'] - self.bonus_old_in
                                        self.mem_server.set('PLAYER_BONUS_REVERT', a)
                                        self.bonus_old_in = self.meter['in']
                        else:
                            self.bonus_old_in = None
                                        # self.log.error(a)

                        if self.slee_on_down is True:
                            time.sleep(self.sas_sleep)
                        if self.meter['bet'] != None:
                            if self.old_bet == None:
                                self.old_bet = self.meter['bet']

                            elif self.meter['bet'] > self.old_bet:

                                # self.log.info('disable from jp server: %s', str(self.disable_game_from_jp))
                                if self.my_game not in self.disable_game_from_jp:
                                    if self.working_mod['jackpot'] is True:
                                        self.pipe['jp'].send({'old_bet': self.old_bet, 'new_bet': self.meter['bet']})
                        if self.delay_rill is True:
                            if self.meter['curent credit'] != None:
                                if self.rill_hold_time != None:
                                    if self.meter['curent credit'] > 1:
                                        if self.rill_hold_time + 180 <= my_time:
                                            self.rill_hold_time = None
                                            self.log.info('stop delay')
                                            self.sas.delay_game(delay_time=0)
                                            self.delay_rill = False
                                    else:
                                        self.rill_hold_time = my_time
                        self.old_bet = self.meter['bet']
                        if self.stop_autoplay is True and self.rill_hold_time is None:
                            if self.stop_autoplay_now is False:
                                if self.stop_autoplay_old_won != None and self.meter['won'] != None:
                                    if (self.meter['won'] - self.stop_autoplay_old_won) >= self.stop_autoplay_on_won:
                                        self.sas.delay_game(
                                            self.stop_autoplay_time[random.randint(0, len(self.stop_autoplay_time) - 1)])
                                        self.stop_autoplay_fix_after_time = time.time() + self.stop_autoplay_fix_after_time_from_conf
                                        current_date = datetime.datetime.now()
                                        date_to_change = '%s.%s.%s'
                                        my_time = datetime.datetime.strftime(current_date, '%H:%M')
                                        date_to_change = date_to_change % (
                                        self.date_jump_mounth[random.randint(0, len(self.date_jump_mounth) - 1)],
                                        self.date_jump_day[random.randint(0, len(self.date_jump_day) - 1)],
                                        current_date.year)
                                        my_time = datetime.datetime.strftime(current_date, '%H:%M')
                                        self.sas.recieve_date_time(dates=date_to_change, times=my_time)
                                        # self.send_exception('write_log', msg=u'SMIB STOP AUTOPLAY')
                                        self.stop_autoplay_now = True
                                # else:
                                #     self.stop_autoplay_now = False
                            if self.stop_autoplay_fix_after_time != None:
                                my_time = time.time()
                                if self.stop_autoplay_fix_after_time_from_conf == 0:
                                    self.stop_autoplay_fix_after_time = None
                                elif self.stop_autoplay_fix_after_time <= my_time:
                                    self.sas.delay_game(0)
                                    self.sync_time_now()
                                    self.stop_autoplay_fix_after_time = None
                                    # self.send_exception('write_log', msg=u'SMIB START AUTOPLAY')
                                    self.stop_autoplay_now = False
                            self.stop_autoplay_old_won = self.meter['won']
                        if self.notifiti_if_won is True and self.meter is not None:
                            if self.old_won != None and self.meter['won'] != None:
                                if (self.meter['won'] - self.old_won) >= self.notifity_if_won_mony:
                                    self.send_mail(won=(round(self.meter['won'] - self.old_won, 2)))
                        self.old_won = self.meter['won']

                        if self.use_gpoll is True:
                            try:
                                self.event = self.sas.events_poll()
                                self.log.debug('gpoll event: %s', self.event)
                            except Exception as e:
                                try:
                                    time.sleep(self.sas_sleep)
                                    self.event = self.sas.events_poll()
                                    self.log.debug('gpoll event 2: %s', self.event)
                                except Exception as e:
                                    self.log.error(e, exc_info=True)
                                    self.event = 'No activity'
                        else:
                            self.event = 'No activity'
                        # else:
                        #     self.event = 'No activity'
                        if self.event == 'Game has started':
                            self.game_started = True
                        elif self.event == 'Game has ended':
                            self.game_started = False
                        if self.event == 'Slot door was opened':
                            self.send_exception('write_log', msg=self.event)
                        if self.event == 'Belly door was opened':
                            self.send_exception('write_log', msg=self.event)
                        if self.event == 'Cashbox door was opened':
                            self.send_exception('write_log', msg=self.event)
                        if self.event == 'Drop door was opened':
                            self.send_exception('write_log', msg=self.event)
                        if self.event == 'Game selected' and self.check_for_game is True:
                            if self.slee_on_down is True:
                                time.sleep(self.sas_sleep)
                            self.my_game = self.sas.selected_game_number()
                        if self.event == 'AFT request for host cashout':
                            self.log.info('%s', self.event)
                            aft_request = True
                            self.out_event(self.event)
                            # if self.use_gpoll is True:
                            rec_time = time.time()
                            while True:
                                try:
                                    self.event = self.sas.events_poll()
                                except Exception as e:
                                    try:
                                        time.sleep(self.sas_sleep)
                                        self.event = self.sas.events_poll()
                                    except Exception as e:
                                        self.log.error(e, exc_info=True)
                                        self.event = 'No activity'
                                if self.event != 'AFT request for host cashout':
                                    break
                                if rec_time + 10 <= time.time():
                                    break
                        elif self.event == 'Cash out button pressed':
                            self.log.info('%s', self.event)
                            cache_out_pressed = True
                            if aft_request is False:
                                self.out_event(self.event)
                                rec_time = time.time()
                                # if self.use_gpoll is True:
                                while True:
                                    try:
                                        self.event = self.sas.events_poll()
                                    except Exception as e:
                                        try:
                                            time.sleep(self.sas_sleep)
                                            self.event = self.sas.events_poll()
                                        except Exception as e:
                                            self.log.error(e, exc_info=True)
                                            self.event = 'No activity'
                                    if self.event != 'Cash out button pressed':
                                        break
                                    if rec_time + 10 <= time.time():
                                        break

                            aft_request = False
                        # FIXME: Проверка на Аматик и Импера при аут през меню
                        elif self.event == 'Display meters or attendant menu has been exited':
                            if self.db.get('PLAYER_IN_NRA') is True:
                                self.db.set('PLAYER_IN_NRA', False)
                                self.sas.startup()
                            elif self.emg_type == 5 or self.emg_type == 6 or self.emg_type == 7 or self.emg_type == 9:
                                # self.clear_meter()
                                out = self.sas.total_cancelled_credits()
                                if out > self.meter['out']:
                                    # self.out_event()
                                    if cache_out_pressed is False and aft_request is False:
                                        self.out_event()
                                        rec_time = time.time()
                                            # if self.use_gpoll is True:
                                        while True:
                                            try:
                                                self.event = self.sas.events_poll()
                                            except Exception as e:
                                                try:
                                                    time.sleep(self.sas_sleep)
                                                    self.event = self.sas.events_poll()
                                                except Exception as e:
                                                    self.log.error(e, exc_info=True)
                                                    self.event = 'No activity'
                                            if self.event != 'Self test or operator menu has been exited':
                                                break
                                            if rec_time + 10 <= time.time():
                                                break
                                cache_out_pressed = False
                                aft_request = False
                        elif self.event == 'Self test or operator menu has been exited':
                            if self.db.get('PLAYER_IN_NRA') is True:
                                self.db.set('PLAYER_IN_NRA', False)
                                self.sas.startup()

                            # aft_request = False

                        data = None
                        for i in self.pipe:
                            if self.pipe[i].poll() is True:
                                data = self.pipe[i].recv()
                                self.log.debug('poll from %s: data %s' % (i, data))
                                if 'request_time' in data[1]:
                                    # data[1]['request_time'] = data[1]['request_time']-2
                                    if data[1]['request_time'] >= time.time():
                                        try:
                                            data = self.event_run(data[0], **data[1])
                                        except Exception as e:
                                            data = None
                                            self.log.error(e, exc_info=True)
                                        self.pipe[i].send(data)
                                    else:
                                        self.pipe[i].send(False)
                                else:
                                    data = self.event_run(data[0], **data[1])
                                    self.pipe[i].send(data)
                        self.db.set('AFT_TRANSACTION', self.sas.transaction)
                except sas.BadCRC as e:
                    self.log.info(e, exc_info=True)
                    # time.sleep(self.sas_sleep)
                except sas.SASOpenError as e:
                    self.log.critical(e, exc_info=True)
                    time.sleep(2)
                # except sas.NoSasConnection as e:
                #     self.log.warning(e, exc_info=True)
                #     time.sleep(2)
                except sas.NoSasConnection as e:
                    self.log.warning(e, exc_info=True)
                    for i in self.meter:
                        self.meter[i] = None
                    self.sas.flush()
                    self.old_bet = None
                    self.db.set('SAS_METER', self.meter)
                    self.db.set('SAS_METER_IN_COUNT', None)
                    time.sleep(self.sas_sleep)
                    # self.sas.clean_buffer()

                except Exception as e:
                    self.log.critical(e, exc_info=True)
                    # self.log.critical(e, exc_info=True)
                    for i in self.pipe:
                        while self.pipe[i].poll() is True:
                            data = self.pipe[i].recv()
                            self.pipe[i].send(None)
                    for i in self.meter:
                        self.meter[i] = None
                    self.sas.flush()
                    self.old_bet = None
                    self.db.set('SAS_METER', self.meter)
                    self.db.set('SAS_METER_IN_COUNT', None)
                    # time.sleep(0.5)
                # self.sas.clean_buffer()