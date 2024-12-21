# -*- coding:utf-8 -*-
'''
Created on 24.10.2024 г.

@author: dedal
Прозорец за настройки.
'''
import wx
import libs
import gui_lib
from . import gui
import datetime
import os
import json
from threading import *
import time

ID_GPOLL_ID = wx.NewId()
ID_GPOLL_RUN = wx.NewId()
ID_GPOLL_STOP = wx.NewId()


def EVT_GPOLL_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_GPOLL_ID, func)


class GPOLLResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_GPOLL_ID)
        self.data = data

class GpollThread(Thread):
    def __init__(self, notify_window, ip, sleep_time=0.2):
        Thread.__init__(self)
        self._want_abort = 0
        self.ip = ip
        self._notify_window = notify_window
        self.sleep_time = sleep_time
        self.start()

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1

    def run(self):
        error = 0
        while True:
            if self._want_abort:
                wx.PostEvent(self._notify_window, GPOLLResultEvent('Gpoll event task abort'))
                return
            request = libs.udp.send('sas_tester_gpoll', ip=self.ip)
            if not request:
                request = 'No SMIB connection'
            try:
                wx.PostEvent(self._notify_window, GPOLLResultEvent(request))
            except Exception as e:
                error += 1
                print (e)
            if error > 5:
                wx.PostEvent(self._notify_window, GPOLLResultEvent('Gpoll event error is 5. Task abort!'))
                break
            time.sleep(self.sleep_time)


class SasTester(gui.Sas_Tester):
    def __init__(self, parent, device):
        gui.Sas_Tester.__init__(self, parent)
        self.gpoll_worker = None
        self.device = device
        self.TZ = libs.models.TZ
        self.event = {
            'shutdown': {},
            'startup': {},
            # 'sound_off':{},
            # 'sound_on': {},
            # 'reel_spin_game_sounds_disabled':{},
            'enable_bill_acceptor': {},
            'disable_bill_acceptor':{},
            # 'configure_bill_denom':{
            #     'bill_denom':[0xFF, 0xFF, 0xFF],
            #     'action_flag':[0xff]
            # },
            'en_dis_game':{
                'game_number':None,
                'en_dis':True,
            },
            'enter_maintenance_mode':{},
            'exit_maintanance_mode':{},
            # 'en_dis_rt_event_reporting':{'enable':False},
            'send_meters_10_15':{'denom':True},
            'total_cancelled_credits':{'denom':True},
            'total_bet_meter':{'denom', True},
            'total_win_meter':{'denom':True},
            'total_in_meter':{'denom':True},
            'total_jackpot_meter':{'denom':True},
            'games_played_meter':{},
            'games_won_meter':{'denom':True},
            'games_lost_meter':{},
            'games_powerup_door_opened':{},
            'meters_11_15':{'denom':True},
            'current_credits':{'denom':True},
            'handpay_info':{},
            'meters':{'denom':True},
            'total_bill_meters':{},
            # 'gaming_machine_ID':{},
            'total_dollar_value_of_bills_meter':{},
            # 'ROM_signature_verification':{},
            'true_coin_in':{'denom':True},
            'true_coin_out':{'denom':True},
            'total_hand_paid_cancelled_credit':{},
            'delay_game':{'delay_time':200},
            # 'credit_amount_of_all_bills_accepted':{},
            # 'coin_amount_accepted_from_external_coin_acceptor':{},
            'last_accepted_bill_info':{},
            'number_of_bills_currently_in_stacker':{},
            'total_credit_amount_of_all_bills_in_stacker':{},
            'total_number_of_games_impimented':{},
            'game_meters':{
                'game_number':None,
                'denom':True,
            },
            'game_configuration':{'game_number':None,},
            # 'SAS_version_gaming_machine_serial_ID':{},
            'selected_game_number':{'in_hex':True},
            # 'enabled_game_numbers':{},
            'pending_cashout_info':{},
            'AFT_jp':{ 'mony':1,
                       'amount':1,
                       'lock_timeout':0,
                       'games':None,
                       },
            'AFT_change_transaction':{'transaction':'2020202020202020202020202020202021'},
            'AFT_out':{'mony':1,
                               'amount':1,
                               'lock_timeout':0},
            'AFT_cashout_enable':{'amount':1},
            'AFT_won':{ 'mony':1,
                       'amount':1,
                       'lock_timeout':0,
                       'games':None,
                       },
            'AFT_in':{ 'mony':1,
                       'amount':1,
                       'lock_timeout':0,
                       'games':None,
                       },
            'AFT_game_lock_and_status_request':{'lock_code':'00',
                                                'lock_timeout':200,
                                                'condition':'01',},
            'AFT_clean_transaction_poll':{},
            'AFT_get_last_transaction':{},
            'AFT_register':{'mk_reg':False},
            'AFT_unregister':{},
            'AFT_cansel_request':{},
            'current_date_time':{},
            'recieve_date_time':{'dates':'01302024',
                                 'times':'12:12'},
            'initiate_legacy_bonus_pay':{
                'mony':1,
                'tax':'00',
                'games':None,
            },
            'remote_handpay_reset':{},
            'legacy_bonus_meters':{'denom':True,
                                   'game_number':'0000'}

        }
        self.m_choice20.SetItems(sorted(self.event.keys()))
        self.set_var(sorted(self.event.keys())[0])
        self.m_choice20.SetSelection(0)
        self.Layout()

    def set_var(self, var):
        var = json.dumps(self.event[var])
        # var = var.replace(',', '\n')
        self.m_textCtrl32.SetValue(var)

    def get_var(self):
        var = self.m_textCtrl32.GetValue()
        # var = var.replace('\n', ',')
        return json.loads(var)

    def update_response(self, response):
        response = '[' + self.TZ.date_to_str(self.TZ.now(), '%d.%m.%Y %H:%M:%S') + '] ' + str(response) + '\n'
        self.m_textCtrl30.AppendText(response)
        # self.m_textCtrl30.SetFocus()
        self.Fit()
        # self.Layout()

    def OnConnect( self, event ):
        self.m_textCtrl30.SetValue('')
        response = libs.udp.send('sas_tester_connect', self.device.ip)
        if type(response) == list:
            self.update_response(response[0])
            self.update_response(response[1])
            self.update_response(response[2])
            self.update_response('-'*50)
        else:
            self.update_response(str(response))

    def Gpoll_Start( self, event ):
        try:
            sleep_time = float(self.m_textCtrl31.GetValue())
        except:
            dial = wx.MessageDialog(None, 'Bad sleep time fot gpoll event thread.', 'ERROR', wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
            dial.ShowModal()
            return
        if not self.gpoll_worker:
            self.gpoll_worker = GpollThread(self, self.device.ip, sleep_time=sleep_time)
            EVT_GPOLL_RESULT(self, self.OnGetGpoll)

    def Gpoll_Stop( self, event ):
        if self.gpoll_worker:
            self.gpoll_worker.abort()
            self.gpoll_worker = None
        return True

    def OnGetGpoll(self, event):
        self.update_response(event.data)

    def OnClose( self, event ):
        self.Gpoll_Stop(event)
        self.Destroy()

    def OnChoise( self, event ):
        var = sorted(self.event.keys())[self.m_choice20.GetSelection()]
        self.set_var(var)

    def Run( self, event ):
        event = sorted(self.event.keys())[self.m_choice20.GetSelection()]
        var = self.get_var()
        response = libs.udp.send('sas_tester_run', self.device.ip, cmd=event, **var)
        self.update_response(response)