#-*- coding:utf-8 -*-
'''
Created on 16.06.2017 г.

@author: dedal
'''
import wx
import libs
import gui_lib
# import __builtin__
from . import gui
import time
import os
import socket

class AddMashin(gui.AddMashin, gui_lib.keybords.Keyboard):  # @UndefinedVariable
    def __init__(self, parent, edit = None):
        gui.AddMashin.__init__(self, parent)  # @UndefinedVariable
        self.edit = edit
        self.parent = parent
        self._maker_choice()
        self._model_choise()
        self._flor_choice()
        self.SetTitle(gui_lib.msg.mashin_main_AddMashin_name)
        self.m_staticText28.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[5])
        self.m_staticText29.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[4])
        self.m_staticText30.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[3])
        self.m_radioBtn1.SetLabel(gui_lib.msg.mashin_main_AddMashin_button['m_radioBtn1'])
        self.m_radioBtn2.SetLabel(gui_lib.msg.mashin_main_AddMashin_button['m_radioBtn2'])
        self.m_checkBox1.SetLabel(gui_lib.msg.mashin_main_AddMashin_button['m_checkBox1'])
        self.m_checkBox3.SetLabel(gui_lib.msg.mashin_main_AddMashin_button['m_checkBox3'])
        self.m_button20.SetLabel(gui_lib.msg.mashin_main_AddMashin_button['m_button20'])
        self.m_staticText26.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[8])
        self.m_staticText91.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[11])
        self.m_staticText101.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[12])
        self.m_staticText9.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[13])
        self.m_staticText10.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[14])
        self.m_staticText47.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[17])
        self.m_staticText55.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[18])
        self.m_staticText57.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[19])
        self.m_button18.SetLabel(gui_lib.msg.mashin_main_AddMashin_button['m_button18'])
        self.m_button19.SetLabel(gui_lib.msg.mashin_main_AddMashin_button['m_button19'])
        self.m_staticText18.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[1])
        self.m_button11.SetLabel(gui_lib.msg.mashin_main_AddMashin_button['m_button11'])
        self.m_button13.SetLabel(gui_lib.msg.mashin_main_AddMashin_button['m_button13'])

        self.m_bpButton4.SetToolTip(gui_lib.msg.mashin_main_AddMashin_tolltip['m_bpButton4'])
        self.m_bpButton3.SetToolTip(gui_lib.msg.mashin_main_AddMashin_tolltip['m_bpButton3'])
        self.m_bpButton2.SetToolTip(gui_lib.msg.mashin_main_AddMashin_tolltip['m_bpButton2'])
        self.m_textCtrl37.SetToolTip(gui_lib.msg.mashin_main_AddMashin_tolltip['m_textCtrl37'])
        self.m_button20.SetToolTip(gui_lib.msg.mashin_main_AddMashin_tolltip['m_button20'])
        self.m_checkBox3.SetToolTip(gui_lib.msg.mashin_main_AddMashin_tolltip['m_checkBox3'])
        self.m_checkBox1.SetToolTip(gui_lib.msg.mashin_main_AddMashin_tolltip['m_checkBox1'])
        self.m_radioBtn2.SetToolTip(gui_lib.msg.mashin_main_AddMashin_tolltip['m_radioBtn2'])

        # self.m_checkBox1.SetLabel(_(u'Работеща'))
        self.m_staticText19.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[10])
        if self.edit == None:
            self.m_radioBtn1.SetValue(True)
            self.m_radioBtn2.SetValue(False)
            self.m_staticText51.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[9])
            self.m_staticText44.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[9])
            self.m_staticText45.SetLabel(gui_lib.msg.mashin_main_AddMashin_text[9])
            self.m_textCtrl16.SetValue('0')
            self.m_textCtrl17.SetValue('0')
        else:
            self.serial = self.edit.serial
            self.m_checkBox3.SetValue(self.edit.mk_revert)
            if self.edit.ip != None:
                self.m_textCtrl37.SetValue(self.edit.ip)
            if self.edit.sas is True:
                self.m_radioBtn1.SetValue(True)
                self.m_radioBtn2.SetValue(False)

                # self.m_checkBox31.SetValue(self.edit.aft_enable)
            else:
                self.m_radioBtn1.SetValue(False)
                self.m_radioBtn2.SetValue(True)
            if self.edit.enable is True:
                self.m_checkBox1.SetValue(True)
            else:
                self.m_checkBox1.SetValue(False)
            self.m_choice1.SetSelection(self.makerChoice.index(self.edit.maker.name))
            self.m_choice2.SetSelection(self.modelChoice.index(self.edit.model.name))
            self.m_choice3.SetSelection(self.florChoice.index(self.edit.flor.name))
            self.m_textCtrl12.SetValue(str(self.edit.serial))
            self.m_staticText51.SetLabel(str(self.edit.ip))
            self.m_staticText44.SetLabel(str(self.edit.smib_uuid))
            self.m_staticText45.SetLabel(str(self.edit.smib_version))
            self.m_textCtrl13.SetValue(str(self.edit.nom_in_l))
            self.m_textCtrl211.SetValue(str(self.edit.el_in))
            self.m_textCtrl221.SetValue(str(self.edit.el_out))
            self.m_textCtrl21.SetValue(str(self.edit.mex_in))
            self.m_textCtrl22.SetValue(str(self.edit.mex_out))
            self.m_textCtrl35.SetValue(str(self.edit.bill))
            self.m_textCtrl39.SetValue(str(self.edit.el_coef))
            self.m_textCtrl40.SetValue(str(self.edit.mex_coef))
            
            self.m_textCtrl16.SetValue(str(self.edit.bet))
            self.m_textCtrl17.SetValue(str(self.edit.won))
            #self.Fit()
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl12.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl37.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl13.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl21.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl22.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl40.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)




                # self.m_textCtrl16.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                # self.m_textCtrl17.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                
        self.get_info_from_smib = False
        self.OnSetShow()
        self._set_right()
        randomId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnFind, id=randomId)
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('n'), randomId)])
        self.SetAcceleratorTable(accel_tbl)
        #
        self.OnSize(None)

    def OnGetNewUUID(self, event):
        if self.edit:
            self.ip = self.m_textCtrl37.GetValue()
            self.who = libs.udp.send(libs.smib.WHO, self.ip)
            if self.who == None:
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_SMIB_CONNECTION)
                dial.ShowModal()
                return False
            else:
                self.m_staticText44.SetLabel(self.who['sw_id'])
                self.m_staticText45.SetLabel(self.who['version'])


    def OnSize(self, event):
        self.SetSize((1060, 500))
        self.width, self.height = self.GetSize()
        self.m_scrolledWindow1.SetMinSize((self.width * 0.98, self.height * 0.80))
        self.m_scrolledWindow1.SetSize((self.width * 0.98, self.height * 0.80))
        # self.Fit()
        self.Layout()

    def OnFind(self, parent):
        my_ip = None
        if self.m_radioBtn2.GetValue() is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_SAS_IN_DEVICE)
            dial.ShowModal()
            return
        old_ip = self.m_textCtrl37.GetValue()
        try:
            socket.inet_pton(socket.AF_INET, old_ip)
        except:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_IP)
            dial.ShowModal()
            return
        device = libs.DB.get_all_where(libs.models.Device, enable=True, order='ip')
        ip = []
        for i in device:
            if i.ip != None:
                ip.append(i.ip)
        all_ip = []
        tmp = '192.168.1.%s'
        for i in range(11, 250):
            if tmp % (i) not in ip:
                my_ip = tmp % i
                response = libs.udp.send('ping_smib', ip=libs.conf.SERVER, new_ip=my_ip)
                if response is True:
                    my_ip = None
                    pass
                else:
                    break
        if not my_ip:
            dial = wx.MessageDialog(self, *gui_lib.msg.IP_IS_IN_USE)
            dial.ShowModal()
            return
        # response = libs.udp.send('ping_smib', old_ip, new_ip=my_ip)
        # if response is True:
        #     dial = wx.MessageDialog(self, *gui_lib.msg.IP_IS_IN_USE)
        #     dial.ShowModal()
        #     return
        # elif response == None:
        #     dial = wx.MessageDialog(self, *gui_lib.msg.NO_SMIB_CONNECTION)
        #     dial.ShowModal()
        #     return
        msg = DevType(self)
        msg.ShowModal()
        emg_type = msg.sas_config
        for i in range(3):
            response = libs.udp.send('change_ip', old_ip, new_ip=my_ip)
            if response:
                break
        if response is not True:
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_SMIB_CONNECTION)
            dial.ShowModal()
        else:
            data = None
            for i in range(5):
                data = libs.udp.send('alive', ip=my_ip)
                # time.sleep(1)
                if data is True:
                    break
            if data == None:
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_SMIB_CONNECTION)
                dial.ShowModal()
                return
            self.ip = my_ip
            if emg_type:
                sas_response = libs.udp.send('conf_update', ip=self.ip, section='SAS',
                                             sync_time=emg_type['sync_time'],
                                             aft=emg_type['aft'],
                                             check_for_game=emg_type['check_for_game'],
                                             sleep_on_down=emg_type['sleep_on_down'],
                                             sas_n=emg_type['sas_n'],
                                             sleep_time=emg_type['sleep_time'],
                                             aft_check_last_transaction=emg_type['aft_check_last_transaction'],
                                             set_jp_mether_to_out=emg_type['set_jp_mether_to_out'],
                                             emg_type=emg_type['emg_type'],
                                             )
                if sas_response:
                    dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                    dial.ShowModal()
                else:
                    dial = wx.MessageDialog(self, *gui_lib.msg.NO_CONFIG)
                    dial.ShowModal()
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
            self.ip = my_ip
            self.m_textCtrl37.SetValue(my_ip)
            self.m_staticText51.SetLabel(my_ip)
            dial = wx.MessageDialog(self, *gui_lib.msg.NEED_HARD_REBOOT)
            dial.ShowModal()
            # time.sleep(2)


    def _set_right(self):
        self.m_bpButton2.Hide()
        self.m_bpButton3.Hide()
        self.m_bpButton4.Hide()
        if self.parent.GetParent().USER.grup.right != None:
            right = self.parent.GetParent().USER.grup.from_json()
            if 2 in right['mashin']:
                self.m_bpButton4.Show()
                self.m_bpButton4.Bind(wx.EVT_BUTTON, self.OnAddFlor)
            if 3 in right['mashin']:
                self.m_bpButton3.Show()
                self.m_bpButton3.Bind(wx.EVT_BUTTON, self.OnAddModel)
            if 4 in right['mashin']:
                self.m_bpButton2.Show()
                self.m_bpButton2.Bind(wx.EVT_BUTTON, self.OnAddMaker)
            # if 8 not in right['mashin']:


        
    def NotEditable(self, event):
        dial = wx.MessageDialog(self, *gui_lib.msg.NOT_EDITABLE)
        dial.ShowModal()
                
    def OnSetShow(self, event=None):
        if self.m_radioBtn1.GetValue() is True:
            self.m_textCtrl37.SetEditable(True)
            self.m_button20.Enable()

            self.m_textCtrl211.SetForegroundColour(( 154, 0, 0 ))
            self.m_textCtrl221.SetForegroundColour(( 154, 0, 0 ))
            self.m_textCtrl39.SetForegroundColour(( 154, 0, 0 ))
            self.m_textCtrl35.SetForegroundColour(( 154, 0, 0 ))
            self.m_textCtrl16.SetForegroundColour(( 154, 0, 0 ))
            self.m_textCtrl17.SetForegroundColour(( 154, 0, 0 ))

            if self.parent.GetParent().USER.grup.right != None:
                right = self.parent.GetParent().USER.grup.from_json()
                if 5 in right['mashin']:
                    if libs.conf.USE_VIRTUAL_KEYBORD is True:
                        self.m_textCtrl211.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                        self.m_textCtrl221.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                        self.m_textCtrl39.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                        self.m_textCtrl35.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                        self.m_textCtrl16.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                        self.m_textCtrl17.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                    self.m_textCtrl211.SetEditable(True)
                    self.m_textCtrl221.SetEditable(True)
                    self.m_textCtrl39.SetEditable(True)
                    self.m_textCtrl35.SetEditable(True)
                    self.m_textCtrl16.SetEditable(True)
                    self.m_textCtrl17.SetEditable(True)
                else:
                    self.m_textCtrl211.SetEditable(False)
                    self.m_textCtrl221.SetEditable(False)
                    self.m_textCtrl39.SetEditable(False)
                    self.m_textCtrl35.SetEditable(False)
                    self.m_textCtrl16.SetEditable(False)
                    self.m_textCtrl17.SetEditable(False)
                    self.m_radioBtn1.Hide()
                    self.m_radioBtn2.Hide()
        else:
            self.m_textCtrl37.SetEditable(False)
            self.m_button20.Disable()
            if libs.conf.USE_VIRTUAL_KEYBORD is True:
                self.m_textCtrl211.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                self.m_textCtrl221.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                self.m_textCtrl39.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                self.m_textCtrl35.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                self.m_textCtrl16.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
                self.m_textCtrl17.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl211.SetEditable(True)
            self.m_textCtrl221.SetEditable(True)
            self.m_textCtrl39.SetEditable(True)
            self.m_textCtrl35.SetEditable(True)
            self.m_textCtrl16.SetEditable(True)
            self.m_textCtrl17.SetEditable(True)
            
            color = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT)
            self.m_textCtrl211.SetForegroundColour(color)
            self.m_textCtrl221.SetForegroundColour(color)
            self.m_textCtrl39.SetForegroundColour(color)
            self.m_textCtrl35.SetForegroundColour(color)

    def OnEditeble(self, event):
        return None

    def OnGetInfo(self, event):
        
        self.ip = self.m_textCtrl37.GetValue()
        reserv_ip = '192.168.%s.%s'
        cant_use_ip = []
        for i in range(1, 11):
            cant_use_ip.append(reserv_ip % ('0', i))
            cant_use_ip.append(reserv_ip % ('1', i))
            if self.edit == None:
                if self.ip in cant_use_ip or libs.DB.get_one_where(libs.models.Device, ip=self.ip, enable=True) != None:
                    dial = wx.MessageDialog(self, *gui_lib.msg.CANT_USE_IP)
                    dial.ShowModal()
                    return False
            else:
                if self.ip in cant_use_ip:
                    dial = wx.MessageDialog(self, *gui_lib.msg.CANT_USE_IP)
                    dial.ShowModal()
                    return False
        else:
            self.who = libs.udp.send(libs.smib.WHO, self.ip)
            if self.who == None:
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_SMIB_CONNECTION)
                dial.ShowModal()
                return False
            else:
                self.m_staticText51.SetLabel(self.ip)
                self.m_staticText44.SetLabel(self.who['sw_id'])
                self.m_staticText45.SetLabel(self.who['version'])
                self.coef = libs.udp.send('sas.denom', self.ip)
                # print self.coef, 290
                if self.coef == None or self.coef is False:
                    dial = wx.MessageDialog(self, *gui_lib.msg.NO_MASHIN_CONNECTION)
                    dial.ShowModal()
                    return False
                else:
                    self.m_textCtrl39.SetValue(str(self.coef))
                    self.count = libs.udp.send('sas.mether_count', ip=self.ip)
                    # print self.count
                    #time.sleep(2)
                    if self.count == None:
                        dial = wx.MessageDialog(self, *gui_lib.msg.NO_MASHIN_CONNECTION)
                        dial.ShowModal()
                        return False
                    else:
                        self.m_textCtrl211.SetValue(str(self.count['in']))
                        self.m_textCtrl221.SetValue(str(self.count['out']))
                        self.m_textCtrl16.SetValue(str(self.count['bet']))
                        self.m_textCtrl17.SetValue(str(self.count['won']))
                        
                        self.bill = self.count['bill']
                        
                        if self.bill == None:
                            dial = wx.MessageDialog(self, *gui_lib.msg.NO_MASHIN_CONNECTION)
                            dial.ShowModal()
                            return False
                        else:
                            self.m_textCtrl35.SetValue(str(self.bill))
                            dial = wx.MessageDialog(self, *gui_lib.msg.GET_DATA_OK)
                            dial.ShowModal()
        self.get_info_from_smib = True
#         self.Fit()
        return True
    
    def _flor_choice(self):
        self.flor = libs.DB.get_all(libs.models.Flor)
        self.florChoice = ['']
        for i in self.flor:
            self.florChoice.append(i.name)
        self.m_choice3.SetItems(self.florChoice)
        self.m_choice3.SetSelection(0)
    
    def _maker_choice(self):
        self.maker = libs.DB.get_all(libs.models.Maker)
        self.makerChoice = ['']
        for i in self.maker:
            self.makerChoice.append(i.name)
        self.m_choice1.SetItems(self.makerChoice)
        self.m_choice1.SetSelection(0)
        
    def _model_choise(self):
        self.model = libs.DB.get_all(libs.models.Model)
        self.modelChoice = ['']
        for i in self.model:
            self.modelChoice.append(i.name)
        self.m_choice2.SetItems(self.modelChoice)
        self.m_choice2.SetSelection(0)
    
    def OnSave(self, event):
        serial = self.m_textCtrl12.GetValue()
        mex_coef = self.m_textCtrl40.GetValue()
        mex_coef = mex_coef.replace(',', '.')
        mex_in = self.m_textCtrl21.GetValue()
        mex_out = self.m_textCtrl22.GetValue()
        sas = self.m_radioBtn1.GetValue()
        enable = self.m_checkBox1.GetValue()
        nom_in_l = self.m_textCtrl13.GetValue()
        model = self.model[self.m_choice2.GetSelection()-1]
        maker = self.maker[self.m_choice1.GetSelection()-1]
        flor = self.flor[self.m_choice3.GetSelection()-1]
        error = False
        mk_revert = self.m_checkBox3.GetValue()
#         el_coef = self.m_textCtrl39.GetValue()
#         el_coef = el_coef.replace(',', '.')
        if sas is True:
#             response = self.OnGetInfo(event)
            if self.get_info_from_smib is True:
                if self.ip == '192.168.1.9' or int(self.ip[10:]) <= 10:
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                    dial.ShowModal()
                    return
                smib_ip = self.ip
                smib_uuid = self.who['sw_id']
                smib_version = self.who['version']
                # by_hand_order = False
#                 el_in = self.m_textCtrl211.GetValue()
#                 el_out = self.m_textCtrl221.GetValue()
#                 won = self.m_textCtrl16.GetValue()
#                 bet = self.m_textCtrl17.GetValue()
#                 
#                 el_coef = self.coef
#                 bill = self.bill
            else:
                smib_ip = self.m_textCtrl37.GetValue()
                smib_uuid = self.m_staticText44.GetLabel()
                smib_version = self.m_staticText45.GetLabel()
            by_hand_order = False
                
            el_in = self.m_textCtrl211.GetValue()
            el_out = self.m_textCtrl221.GetValue()
            el_coef = self.m_textCtrl39.GetValue()
            bill = self.m_textCtrl35.GetValue()
            # if self.edit == None:
            #     won = 0
            #     bet = 0
            # else:
            won = self.m_textCtrl17.GetValue()
            bet = self.m_textCtrl16.GetValue()
        else:
            by_hand_order = True
            smib_ip = self.m_textCtrl37.GetValue()
            smib_uuid = None
            smib_version = None
            el_in = self.m_textCtrl211.GetValue()
            el_out = self.m_textCtrl221.GetValue()
            won = self.m_textCtrl17.GetValue()
            bet = self.m_textCtrl16.GetValue()
            el_coef = self.m_textCtrl39.GetValue()
            el_coef = el_coef.replace(',', '.')
            bill = self.m_textCtrl35.GetValue()
        try:
            mex_coef = float(mex_coef)
            mex_in = int(mex_in)
            mex_out = int(mex_out)
            el_in = int(el_in)
            el_out = int(el_out)
            won = int(won)
            bet = int(bet)
            el_coef = float(el_coef)
            bill = int(bill)
            nom_in_l = int(nom_in_l)
        except ValueError:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
        else:
            if model == '' or flor == '' or maker == '':
                if error is False:
                    dial = wx.MessageDialog(self, *gui_lib.msg.EMPTY_FIELD)
                    dial.ShowModal()
            else:
                if self.edit == None:
                    smib = libs.DB.make_obj(libs.models.Device)
                else:
                    smib = self.edit
                smib.serial = serial
                smib.by_hend_order = by_hand_order
                smib.model_id = model.id
                smib.nom_in_l = nom_in_l
                smib.el_in = el_in
                smib.el_out = el_out
                smib.mex_in = mex_in
                smib.mex_out = mex_out
                smib.el_coef = el_coef
                smib.mex_coef = mex_coef
                smib.flor_id = flor.id
                smib.maker_id = maker.id
                smib.won = won
                smib.bet = bet
                smib.bill = bill
                smib.enable = enable
                smib.sas = sas
                smib.ip = smib_ip
                smib.smib_uuid = smib_uuid
                smib.smib_version = smib_version
                smib.mk_revert = mk_revert
                # smib.aft_enable = self.m_checkBox31.GetValue()
                libs.DB.add_object_to_session(smib)
                err = libs.DB.make_obj(libs.models.GetCounterError)
                err.user_id = self.parent.GetParent().USER.id
                err.mashin_nom_in_l = nom_in_l
                err.info = 'CHANGE DEVICE CONFIG' + ': ' + self.parent.user.name
                libs.DB.add_object_to_session(err)
                try:
                    libs.DB.commit()
                    self.Destroy()
                except Exception as e:
                    libs.DB.rollback()
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
                    dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                    dial.ShowModal()
                
    def OnClose(self, event):
        self.Destroy()
    
    def OnAddMaker(self, event):
        frame = AddMaker(self)
        frame.ShowModal()
        self._maker_choice()
        
    def OnAddModel(self, event):
        frame = AddModel(self)
        frame.ShowModal()
        self._model_choise()
        
    def OnAddFlor(self, event):
        frame = FlorAdd(self)
        frame.ShowModal()
        self._flor_choice()
    
class AddMaker(gui.AddMaker, gui_lib.keybords.Keyboard):  # @UndefinedVariable
    def __init__(self, parent):
        gui.AddMaker.__init__(self, parent)  # @UndefinedVariable
        self.SetTitle(gui_lib.msg.mashin_main_AddMaker_name)
        self.m_button3.SetLabel(gui_lib.msg.mashin_main_AddMaker_button['m_button3'])
        self.m_button4.SetLabel(gui_lib.msg.mashin_main_AddMaker_button['m_button4'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl1.Bind( wx.EVT_LEFT_UP, self.OnKeyboard )
        self.Layout()
        
    def OnGo(self, event):
        name = self.m_textCtrl1.GetValue()
        if name == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
        else:
            maker = libs.DB.make_obj(libs.models.Maker)
            maker.name = name
            libs.DB.add_object_to_session(maker)
            try:
                libs.DB.commit()
                self.Destroy()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                libs.DB.rollback()
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
                dial.ShowModal()

    
    def OnClose(self, event):
        self.Destroy()

class AddModel(gui.AddModel, gui_lib.keybords.Keyboard):  # @UndefinedVariable
    def __init__(self, parent):
        gui.AddModel.__init__(self, parent)  # @UndefinedVariable
        self.SetTitle(gui_lib.msg.mashin_main_AddModel_name)
        self.m_button1.SetLabel(gui_lib.msg.mashin_main_AddModel_button['m_button1'])
        self.m_button14.SetLabel(gui_lib.msg.mashin_main_AddModel_button['m_button14'])
        self.width, self.height = wx.GetDisplaySize()
        self.m_listCtrl1.InsertColumn(0, gui_lib.msg.mashin_main_AddModel_text[1])
        self.m_listCtrl1.SetColumnWidth(0, self.width // 2)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl14.Bind( wx.EVT_LEFT_UP, self.OnKeyboard )
        self._get_list_box()
        self.Layout()
        
    def _get_list_box(self):
        self.model = libs.DB.get_all(libs.models.Model)
        index = 0
        for item in self.model:
            self.m_listCtrl1.InsertItem(index, item.name)
            index += 1
            
    def _refresh_list_ctrl(self):
        self.m_listCtrl1.DeleteAllItems()
        self._get_list_box()
        
    def OnGo(self, event):
        name = self.m_textCtrl14.GetValue()
        if name == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
        else:
                model = libs.DB.make_obj(libs.models.Model)
                model.name = name
                libs.DB.add_object_to_session(model)
                try:
                    libs.DB.commit()
                    self.m_textCtrl14.SetValue('')
                    self._refresh_list_ctrl()
                except Exception as e:
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
                    libs.DB.rollback()
                    dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
                    dial.ShowModal()

        
    def OnClose(self, event):
        self.Destroy()
          
class FlorAdd(gui.FlorAdd, gui_lib.keybords.Keyboard):  # @UndefinedVariable
    def __init__(self, parent):
        gui.FlorAdd.__init__(self, parent)  # @UndefinedVariable
        self.SetTitle(gui_lib.msg.mashin_main_FlorAdd_name)
        self.m_button3.SetLabel(gui_lib.msg.mashin_main_FlorAdd_button['m_button3'])
        self.m_button4.SetLabel(gui_lib.msg.mashin_main_FlorAdd_button['m_button4'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl1.Bind( wx.EVT_LEFT_UP, self.OnKeyboard )
        self.Layout()
        
    def OnGo(self, event):
        name = self.m_textCtrl1.GetValue()
        if name == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
        else:
            flor = libs.DB.make_obj(libs.models.Flor)
            flor.name = name
            libs.DB.add_object_to_session(flor)
            try:
                libs.DB.commit()
                self.Destroy()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                libs.DB.rollback()
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
                dial.ShowModal()

    
    def OnClose(self, event):
        self.Destroy()
        
class FlorSelect(gui.FlorSelect):  # @UndefinedVariable
    def __init__(self, parent):
        gui.FlorSelect.__init__(self, parent)  # @UndefinedVariable
        self.m_button1.SetLabel(gui_lib.msg.mashin_main_FlorSelect_button['m_button1'])
        self.m_bpButton1.SetToolTip(gui_lib.msg.mashin_main_FlorSelect_tolltip['bpButton1'])
        self.m_listCtrl1.SetToolTip(gui_lib.msg.mashin_main_FlorSelect_tolltip['m_listCtrl1'])
        self.SetTitle(gui_lib.msg.mashin_main_FlorSelect_name)
        self.parent = parent
        self.m_listCtrl1.InsertColumn(0, gui_lib.msg.mashin_main_FlorSelect_text[1])
        self.width, self.height = wx.GetDisplaySize()
        self.m_listCtrl1.SetColumnWidth(0, self.width // 2)
        self.m_bpButton1.Hide()
        self.close = False
#         self.user = USER # @UndefinedVariable
        right = self.parent.USER.grup.from_json()
        if 2 in right['mashin']:
            self.m_bpButton1.Show()
        self._add_list()
        self.Fit()
        
    def _add_list(self):
        self.m_listCtrl1.InsertItem(0, gui_lib.msg.mashin_main_FlorSelect_text[2])
        self.flor = libs.DB.get_all(libs.models.Flor)
        index = 1
        for item in self.flor:
            self.m_listCtrl1.InsertItem(index, item.name)
            index += 1
    
    def _refresh_list_ctrl(self):
        self.m_listCtrl1.DeleteAllItems()
        self._add_list()
        
    def OnAdd(self, event):
        dialog = FlorAdd(self)
        if libs.conf.UNITEST:
            wx.CallLater(250, dialog.EndModal, wx.ID_OK)
        dialog.ShowModal()
        self._refresh_list_ctrl()
        self.Fit()
    
    def OnGo(self, event):
        flor = self.m_listCtrl1.GetFirstSelected()
        flor = self.m_listCtrl1.GetItem(flor, col=0).GetText()
        if flor == gui_lib.msg.mashin_main_FlorSelect_text[2]: # _(u'Всички'):
            self.parent.USER.flor_id = None
        else:
            flor = self.flor[self.m_listCtrl1.GetFirstSelected()-1]
            self.parent.USER.flor_id = flor.id
        
        libs.DB.add_object_to_session(self.parent.USER)
        try:
            libs.DB.commit()
            self.Destroy()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            libs.DB.rollback()
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            
        
    def OnClose(self, event):
        self.close = True
        self.Destroy()

class Mashin(gui.MashinPanel):
    def __init__(self, parent):
        gui.MashinPanel.__init__(self, parent)
        # reload(libs.conf)
#         if libs.conf.FULSCREEAN is True:
#             self.SetWindowStyle(wx.STAY_ON_TOP)
        
        self.parent = parent
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.mashin_main_Mashin_name)
        self.user = self.parent.USER
        self.width, self.height = self.parent.GetSize()
        self.Bind( wx.EVT_SIZE, self.on_resize )
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        
#         self.SetSize((self.width, self.height*0.95))
#         if os.name == 'posix':
#             self.SetSize((self.width, self.height))
#         else:
#             self.SetSize((self.width, self.height*0.95))
#             self.Center()

        self.m_listCtrl2.SetToolTip(gui_lib.msg.mashin_main_Mashin_tolltip['m_listCtrl2'])
        self.m_listCtrl5.InsertColumn(0, gui_lib.msg.mashin_main_Mashin_text[1])
        
        
        
        self.m_listCtrl6.InsertColumn(0, gui_lib.msg.mashin_main_Mashin_text[2])
        
        self.m_listCtrl6.InsertItem(0, gui_lib.msg.mashin_main_Mashin_text[3])
        self.m_listCtrl6.InsertItem(1, gui_lib.msg.mashin_main_Mashin_text[2])
        
        self.m_listCtrl6.InsertItem(2, gui_lib.msg.mashin_main_Mashin_text[4])
        
#         self.m_listCtrl2.SetMaxSize((self.width//1.40, self.height*0.80))
        self.m_listCtrl2.InsertColumn(0, gui_lib.msg.mashin_main_Mashin_text[5])
        
        self.m_listCtrl2.InsertColumn(1, gui_lib.msg.mashin_main_Mashin_text[6])
        
        self.m_listCtrl2.InsertColumn(2, gui_lib.msg.mashin_main_Mashin_text[7])
        
        self.m_listCtrl2.InsertColumn(3, gui_lib.msg.mashin_main_Mashin_text[8])
        
        self.m_listCtrl2.InsertColumn(4, gui_lib.msg.mashin_main_Mashin_text[9])
        
        
        self._maker_list()
        self._mashin_list(data=None)
        self._right_set()
        self.on_resize(None)

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        self.m_toolBar1.SetMinSize((self.width, -1))
        self.m_listCtrl5.SetMinSize((self.width *0.3, self.height * 0.30))
        self.m_listCtrl5.SetColumnWidth(0, self.width//4)
        self.m_listCtrl6.SetMinSize((self.width *0.3, self.height * 0.30))
        self.m_listCtrl6.SetColumnWidth(0, self.width//4)
        self.m_listCtrl6.SetItemTextColour( item=1, col=wx.Colour( 0, 135, 11 ))
        self.m_listCtrl6.SetItemTextColour( item=2, col=wx.Colour( 199, 16, 29 ))
        
        self.m_listCtrl2.SetMinSize((self.width*0.68, self.height * 0.78))
        self.m_listCtrl2.SetColumnWidth(0, self.width*0.06)
        self.m_listCtrl2.SetColumnWidth(1, self.width*0.19)
        self.m_listCtrl2.SetColumnWidth(2, self.width*0.12)
        self.m_listCtrl2.SetColumnWidth(3, self.width*0.20)
        self.m_listCtrl2.SetColumnWidth(4, self.width*0.12)
#         self.SetSize((self.width, self.height*0.90))
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height*0.95))
        if event != None:
            event.Skip() 
            self.Layout()
            
    def _right_set(self):
        self.m_toolBar1.ClearTools()
        if self.parent.USER.grup != None:
            right = self.parent.USER.grup.from_json()
            if 1 in right['mashin']:
                self.m_tool2 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.mashin_main_Mashin_button['m_tool2'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER +u"64x64/network-server.png",
                                                                      wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.mashin_main_Mashin_tolltip['m_tool2'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnAddMashin, id=self.m_tool2.GetId())
            if 2 in right['mashin']:
                self.m_tool3 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.mashin_main_Mashin_button['m_tool3'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER +u"64x64/network-server-database.png",
                                                                      wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.mashin_main_Mashin_tolltip['m_tool3'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnAddFlor, id=self.m_tool3.GetId())
            if 3 in right['mashin']:
                self.m_tool5 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.mashin_main_Mashin_button['m_tool5'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER +u"64x64/cpu.png", wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL, gui_lib.msg.mashin_main_Mashin_tolltip['m_tool5'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnAddModel, id=self.m_tool5.GetId())
            if 4 in right['mashin']:
                self.m_tool4 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.mashin_main_Mashin_button['m_tool4'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER +u"64x64/xarchiver-add.png",
                                                                      wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.mashin_main_Mashin_tolltip['m_tool4'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnAddMaker, id=self.m_tool4.GetId())
            if 6 in right['mashin']:
                self.m_listCtrl2.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnEdit )
            if 7 in right['mashin']:
                self.m_tool6 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.mashin_main_Mashin_button['m_tool6'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER +u"64x64/Add-Files-To-Archive-64.png",
                                                                      wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL,  gui_lib.msg.mashin_main_Mashin_tolltip['m_tool6'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnSendToJP, id=self.m_tool6.GetId())
        self.m_tool1 = self.m_toolBar1.AddTool( wx.ID_ANY, gui_lib.msg.mashin_main_Mashin_button['m_tool1'], wx.Bitmap( libs.conf.IMG_FOLDER +u"64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, gui_lib.msg.mashin_main_Mashin_tolltip['m_tool1'], wx.EmptyString, None )
        self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool1.GetId() )
        self.m_toolBar1.Realize()

    def OnSendToJP(self, event):
        smib = None
        for i in range(3):
            smib = libs.udp.send('GET_DB_KEY', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, key='smib')
            if smib != None:
                break
        if smib == None:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            return
        all_smib = libs.DB.get_all_where(libs.models.Device, enable=True, sas=True)
        for i in all_smib:
            if i.ip in list(smib.keys()):
                smib[i.ip]['mashin_sn'] = i.serial
                smib[i.ip]['version'] = i.smib_version
                smib[i.ip]['hw_uuid'] = i.smib_uuid
                smib[i.ip]['sas'] = True
                smib[i.ip]['hw_id'] = i.smib_uuid
                smib[i.ip]['licenz'] = str(i.nom_in_l)
                smib[i.ip]['model'] = i.model.name
                smib[i.ip]['soft_uuid'] = libs.conf.ID
            else:
                smib[i.ip] = {u'mashin_sn':i.serial,
                              u'group': [],
                              u'procent':0,
                              u'ip':i.ip,
                              u'init_time':time.time(),
                              u'crc':1407085226,
                              u'version':i.smib_version,
                              u'hw_uuid':i.smib_uuid,
                              u'sas':True,
                              u'licenz':str(i.nom_in_l),
                              u'model':i.model.name,
                              u'hw_id':i.smib_uuid,
                              u'soft_uuid':libs.conf.ID,
                              }
        # libs.udp.send('STOP_ROTATION', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, command=True)
        data = None
        for i in range(3):
            data = libs.udp.send('SET_DB_KEY', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, key='smib', data=smib)
            if data is True:
                break
        if data is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()

    def _maker_list(self):
        self.maker = libs.DB.get_all(libs.models.Maker)
        self.m_listCtrl5.InsertItem(0, gui_lib.msg.mashin_main_Mashin_text[3])
        index = 1
        for item in self.maker:
            self.m_listCtrl5.InsertItem(index, item.name)
            index += 1
    
    def refresh_maker_list(self):
        self.m_listCtrl5.DeleteAllItems()
        self._maker_list()
        
    def _mashin_list(self, data=None):
        if data == None:
            mashin = libs.DB.get_all(libs.models.Device, order='nom_in_l')
        else:
            mashin = data  # @UnusedVariable

        self.mashinDict = {}
        index = 0
        for item in mashin:
            self.m_listCtrl2.InsertItem(index, str(item.nom_in_l))
            self.m_listCtrl2.SetItem(index, 1, item.model.name)
            self.m_listCtrl2.SetItem(index, 2, item.serial)
            if item.sas is False:
                self.m_listCtrl2.SetItem(index, 3, gui_lib.msg.mashin_main_Mashin_text[10])
                self.m_listCtrl2.SetItem(index, 4, gui_lib.msg.mashin_main_Mashin_text[10])
            else:
                self.m_listCtrl2.SetItem(index, 3, item.ip)
                self.m_listCtrl2.SetItem(index, 4, item.smib_version)
            if item.enable is False:
                self.m_listCtrl2.SetItemTextColour(item=index, col=wx.Colour( 199, 16, 29 ))
            else:
                self.m_listCtrl2.SetItemTextColour(item=index, col=wx.Colour( 0, 135, 11 ))
            self.mashinDict[index] = item
            index += 1
            
    def refresh_mashin_list(self, data):
        self.m_listCtrl2.DeleteAllItems()
        self._mashin_list(data)
        
    
    def OnEdit(self, event):
        mashin = self.mashinDict[self.m_listCtrl2.GetFirstSelected()]
        select = self.m_listCtrl2.GetFirstSelected()
        panel = AddMashin(self, edit=mashin)
        panel.ShowModal()
        self.refresh_mashin_list(None)
        self.m_listCtrl2.Focus(select)


        
    def OnShowEnableDisable(self, event):
        enable = self.m_listCtrl6.GetFirstSelected()
        enable = self.m_listCtrl6.GetItem(enable, col=0).GetText()
        try:
            maker = self.m_listCtrl5.GetFirstSelected()
            maker = self.m_listCtrl5.GetItem(maker, col=0).GetText()
        except wx._core.PyAssertionError:
            if enable == gui_lib.msg.mashin_main_Mashin_text[3]: #_(u'Всички'):
                self.refresh_mashin_list(data = None)
            elif enable == gui_lib.msg.mashin_main_Mashin_text[2]: #_(u'Активни'):
                data = libs.DB.get_all_where(libs.models.Device, enable=True, order='nom_in_l')
                self.refresh_mashin_list(data)
            elif enable == gui_lib.msg.mashin_main_Mashin_text[4]: #_(u'Неактивни'):
                data = libs.DB.get_all_where(libs.models.Device, enable=False, order='nom_in_l')
                self.refresh_mashin_list(data)
        else:
#             maker = db_ctrl.maker_get(maker)
            maker = self.m_listCtrl5.GetFirstSelected()
            maker = self.m_listCtrl5.GetItem(maker, col=0).GetText()
            if maker !=  gui_lib.msg.mashin_main_Mashin_text[3]: #_(u'Всички'):
                maker = self.maker[self.m_listCtrl5.GetFirstSelected() -1 ]
                if enable == gui_lib.msg.mashin_main_Mashin_text[3]: #_(u'Всички'):
                    data = libs.DB.get_all_where(libs.models.Device, maker_id=maker.id, order='nom_in_l')
                    self.refresh_mashin_list(data)
                elif enable == gui_lib.msg.mashin_main_Mashin_text[2]: #_(u'Активни'):
                    data = libs.DB.get_all_where(libs.models.Device, maker_id=maker.id, enable=True, order='nom_in_l')
                    self.refresh_mashin_list(data)
                elif enable == gui_lib.msg.mashin_main_Mashin_text[4]: #_(u'Неактивни'):
                    data = libs.DB.get_all_where(libs.models.Device, maker_id=maker.id, enable=False, order='nom_in_l')
                    self.refresh_mashin_list(data)
            else:
                if enable == gui_lib.msg.mashin_main_Mashin_text[4]: #_(u'Неактивни'):
                    data = libs.DB.get_all_where(libs.models.Device, enable=False, order='nom_in_l')
                    self.refresh_mashin_list(data)
                elif enable == gui_lib.msg.mashin_main_Mashin_text[2]: # _(u'Активни'):
                    data = libs.DB.get_all_where(libs.models.Device, enable=True, order='nom_in_l')
                    self.refresh_mashin_list(data)
                elif enable == gui_lib.msg.mashin_main_Mashin_text[3]: #_(u'Всички'):
                    data = libs.DB.get_all(libs.models.Device, order='nom_in_l')
                    self.refresh_mashin_list(data)
                
    def OnShowMaker(self, event):
        maker = self.m_listCtrl5.GetFirstSelected()
        maker = self.m_listCtrl5.GetItem(maker, col=0).GetText()
        data = None
        enable = None
        try:
            enable = self.m_listCtrl6.GetFirstSelected()
            enable = self.m_listCtrl6.GetItem(enable, col=0).GetText()
            if enable == gui_lib.msg.mashin_main_Mashin_text[2]:
                enable = True
            elif enable == gui_lib.msg.mashin_main_Mashin_text[3]:
                enable = None
            else:
                enable = False
            
        except wx._core.PyAssertionError:
            enable = None

            if maker == gui_lib.msg.mashin_main_Mashin_text[3] and enable == None:
                data = libs.DB.get_all(libs.models.Device, order='nom_in_l')
            elif maker == gui_lib.msg.mashin_main_Mashin_text[3]:
                if enable != None:
                    data = libs.DB.get_all_where(libs.models.Device, enable=enable, order='nom_in_l')
                else:
                    data = libs.DB.get_all_where(libs.models.Device, order='nom_in_l')
            else:
                maker = self.maker[self.m_listCtrl5.GetFirstSelected()-1]
#                 maker = db_ctrl.maker_get(maker)
                data = libs.DB.get_all_where(libs.models.Device, maker_id=maker.id, order='nom_in_l')
        else:
            if maker == gui_lib.msg.mashin_main_Mashin_text[3]:
                data = libs.DB.get_all(libs.models.Device, order='nom_in_l')
            elif maker == gui_lib.msg.mashin_main_Mashin_text[2]:
                maker = self.maker[self.m_listCtrl5.GetFirstSelected() - 1]
                data = libs.DB.get_all(libs.models.Device, maker_id=maker.id,  order='nom_in_l')
            else:
                
#                 maker = db_ctrl.maker_get(maker)
                maker = self.maker[self.m_listCtrl5.GetFirstSelected()-1]
                data = libs.DB.get_all_where(libs.models.Device, maker_id=maker.id, order='nom_in_l')
        self.refresh_mashin_list(data)
            
    def OnAddFlor(self, event):
        dialog = FlorSelect(self.parent)
        if libs.conf.UNITEST:
            wx.CallLater(250, dialog.EndModal, wx.ID_OK)
        dialog.ShowModal()
    
    def OnAddMaker(self, event):
        dialog = AddMaker(self)
        dialog.ShowModal()
        self.refresh_maker_list()
    
    def OnAddMashin(self, event):
        dialog = AddMashin(self)
        dialog.ShowModal()
        self.refresh_mashin_list(data=None)
        self.m_listCtrl2.Focus(len(self.mashinDict)-1)
        
    def OnAddModel(self, event):
        dialog = AddModel(self)
        dialog.ShowModal()
        
        
    def OnClose(self, event):
        self.parent.all_mashin_refresh()
        self.parent.OnConfig(None)
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.mashin_main_Mashin_text[11])
        self.Destroy()
        

class DevType(gui.DevType):
    def __init__(self, parent):
        gui.DevType.__init__(self, parent)
        self.SetTitle(gui_lib.msg.DevType['name'])
        self.m_button13.SetLabel(gui_lib.msg.DevType['m_button13'])
        self.m_button14.SetLabel(gui_lib.msg.DevType['m_button14'])
        self.sas_config = {}
        my_list = [u'', gui_lib.msg.config_SMIB['list_1'], gui_lib.msg.config_SMIB['list_2'],
                   gui_lib.msg.config_SMIB['list_3'], gui_lib.msg.config_SMIB['list_4'],
                   gui_lib.msg.config_SMIB['list_5'], gui_lib.msg.config_SMIB['list_6'],
                   gui_lib.msg.config_SMIB['list_7'], gui_lib.msg.config_SMIB['list_8'],
                   gui_lib.msg.config_SMIB['list_9']]
        try:
            self.m_choice4.SetItems(my_list)
        except:
            self.m_choice4.SetItems([u''])
        self.m_choice4.SetSelection(0)
        self.Fit()

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        selected_conf = self.m_choice4.GetSelection()
        if selected_conf == 0:
            self.OnClose(event)
        elif selected_conf == 1 or selected_conf == 2 or selected_conf == 8 or selected_conf == 9:
            self.sas_config['sync_time'] = True
            self.sas_config['aft'] = True
            self.sas_config['check_for_game'] = True
            self.sas_config['sleep_on_down'] = False
            self.sas_config['sleep_time'] = 0.04
            self.sas_config['emg_type'] = selected_conf
            self.sas_config['aft_check_last_transaction'] = True
            self.sas_config['sas_n'] = '00'
            self.sas_config['set_jp_mether_to_out'] = True
        elif selected_conf == 3:
            self.sas_config['sync_time'] = False
            self.sas_config['aft'] = True
            self.sas_config['check_for_game'] = False
            self.sas_config['sleep_on_down'] = True
            self.sas_config['sleep_time'] = 0.04
            self.sas_config['emg_type'] = selected_conf
            self.sas_config['aft_check_last_transaction'] = False
            self.sas_config['sas_n'] = '01'
            self.sas_config['set_jp_mether_to_out'] = True
        elif selected_conf == 4:
            self.sas_config['sync_time'] = False
            self.sas_config['aft'] = True
            self.sas_config['check_for_game'] = False
            self.sas_config['sleep_on_down'] = True
            self.sas_config['sleep_time'] = 0.05
            self.sas_config['emg_type'] = selected_conf
            self.sas_config['aft_check_last_transaction'] = True
            self.sas_config['sas_n'] = '01'
            self.sas_config['set_jp_mether_to_out'] = True
        elif selected_conf == 5:
            self.sas_config['sync_time'] = False
            self.sas_config['aft'] = True
            self.sas_config['check_for_game'] = False
            self.sas_config['sleep_on_down'] = True
            self.sas_config['sleep_time'] = 0.04
            self.sas_config['emg_type'] = selected_conf
            self.sas_config['aft_check_last_transaction'] = True
            self.sas_config['sas_n'] = '01'
            self.sas_config['set_jp_mether_to_out'] = True
        elif selected_conf == 6:
            self.sas_config['sync_time'] = False
            self.sas_config['aft'] = False
            self.sas_config['check_for_game'] = False
            self.sas_config['sleep_on_down'] = True
            self.sas_config['sleep_time'] = 0.04
            self.sas_config['emg_type'] = selected_conf
            self.sas_config['aft_check_last_transaction'] = False
            self.sas_config['sas_n'] = '01'
            self.sas_config['set_jp_mether_to_out'] = True
        elif selected_conf == 7:
            self.sas_config['sync_time'] = True
            self.sas_config['aft'] = True
            self.sas_config['check_for_game'] = True
            self.sas_config['sleep_on_down'] = False
            self.sas_config['sleep_time'] = 0.04
            self.sas_config['emg_type'] = selected_conf
            self.sas_config['aft_check_last_transaction'] = True
            self.sas_config['sas_n'] = '00'
            self.sas_config['set_jp_mether_to_out'] = True
        self.OnClose(event)

