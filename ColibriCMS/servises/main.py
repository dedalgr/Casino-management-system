# -*- coding:utf-8 -*-
'''
Created on 14.04.2020 г.

@author: dedal
'''

import wx
import libs
import gui_lib
from . import gui
import mony
import order
import os
import datetime
from . import task
import json
import webbrowser

class TransferMony(mony.main.MonyTransfer):
    pass

class NotSASCounter(order.main.NotSASCounter):
    pass

class AutoOrder(order.main.GetCounter):
    pass

class Fix(gui.Fix, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user, db_row):
        self.parent = parent
        gui.Fix.__init__(self, self.parent)
        self.user = user
        self.db_row = db_row
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl2.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_richText2.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

        self.OnHide(None)
        self._localise()

    def _localise(self):
        self.SetLabel(gui_lib.msg.service_Fix['name'])
        self.m_radioBtn1.SetLabel(gui_lib.msg.service_Fix['m_radioBtn1'])
        self.m_radioBtn2.SetLabel(gui_lib.msg.service_Fix['m_radioBtn2'])
        self.m_checkBox1.SetLabel(gui_lib.msg.service_Fix['m_checkBox1'])
        self.m_checkBox2.SetLabel(gui_lib.msg.service_Fix['m_checkBox2'])
        self.m_checkBox3.SetLabel(gui_lib.msg.service_Fix['m_checkBox3'])
        self.m_staticText2.SetLabel(gui_lib.msg.service_Fix['m_staticText2'])
        self.m_staticText3.SetLabel(gui_lib.msg.service_Fix['m_staticText3'])
        self.m_button3.SetLabel(gui_lib.msg.service_Fix['m_button3'])
        self.m_button4.SetLabel(gui_lib.msg.service_Fix['m_button4'])
        self.m_checkBox4.SetLabel(gui_lib.msg.service_Fix['m_checkBox4'])

        self.m_radioBtn1.SetToolTip(gui_lib.msg.service_Fix['m_radioBtn1t'])
        self.m_radioBtn2.SetToolTip(gui_lib.msg.service_Fix['m_radioBtn2t'])
        self.m_checkBox1.SetToolTip(gui_lib.msg.service_Fix['m_checkBox1t'])
        self.m_checkBox2.SetToolTip(gui_lib.msg.service_Fix['m_checkBox2t'])
        self.m_checkBox3.SetToolTip(gui_lib.msg.service_Fix['m_checkBox3t'])
        self.m_checkBox4.SetToolTip(gui_lib.msg.service_Fix['m_checkBox4t'])

    def sendMail(self, text):
        try:
            send_to = self.user.grup.boss_mail
            subject = self.user.grup.subject
            # subject = json.loads(subject.value)[libs.conf.ID]
            send_mail_to = send_to.split(',')
            for i in send_mail_to:
                # libs.sendmail.Gmail(html, i, libs.conf.CONF.get('MAIL', 'subject', 'str'))
                libs.sendmail.Gmail(text, i, subject+' FIX TASK')
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)

    def OnSave( self, event ):
        try:
            mony = self.m_textCtrl2.GetValue()
            mony = mony.replace(',', '.')
            mony = float(mony)
        except:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        if self.db_row.mashin_id != None:

            if self.m_radioBtn1.GetValue() is True:
                self.db_row.is_ram_clear = False
            else:
                self.db_row.is_ram_clear = True
                obj = libs.DB.make_obj(libs.models.RamClear)
                obj.user_id = self.user.id
                obj.mashin_id = self.db_row.mashin_id
                obj.el_in = self.db_row.mashin.el_in
                obj.el_out = self.db_row.mashin.el_out
                obj.mex_in = self.db_row.mashin.mex_in
                obj.mex_out = self.db_row.mashin.mex_out
                obj.bill = self.db_row.mashin.bill

                libs.DB.add_object_to_session(obj)
                try:
                    libs.DB.flush()
                except Exception as e:
                    libs.DB.rollback()
                    dial = wx.MessageDialog(self, *gui_lib.msg.CART_IN_USE)
                    dial.ShowModal()
                    return
                self.db_row.ramclear_id = obj.id

                if self.m_checkBox3.GetValue() is False:
                    if self.m_checkBox1.GetValue() is True:
                        dial = NotSASCounter(self.parent, self.db_row.mashin)
                        dial.ShowModal()
                    else:
                        dial = AutoOrder(self.parent, [self.db_row.mashin.nom_in_l])
                        dial.ShowModal()
                        error = dial.error
                        if error != []:
                            text = (gui_lib.msg.order_main_Order_text[15] + '\n' + str(error) + '\n' +
                                    gui_lib.msg.order_main_Order_text[16])
                            dlg = wx.MessageDialog(self, text, gui_lib.msg.order_main_Order_text[17],
                                                   wx.YES_NO | wx.ICON_WARNING)
                            result = dlg.ShowModal()
                            if result == wx.ID_YES:
                                dialog = AutoOrder(self, mashin_to_ord=error)
                                dialog.ShowModal()
                            else:
                                dial = NotSASCounter(self.parent, self.db_row.mashin)
                                dial.ShowModal()
                    if self.m_checkBox2.GetValue() is True:
                        self.user.kasa += self.db_row.mashin.bill_in_device
                        self.db_row.mashin.bill_in_device = 0
                    if self.m_checkBox4.GetValue() is True:
                        dial = TransferMony(self.parent, self.user, chk_for_mony=False)
                        dial.m_textCtrl6.SetValue("{:.2f}".format(self.user.kasa))
                        dial.m_textCtrl6.SetEditable(False)
                        dial.ShowModal()
                        # self.user.kasa = 0


                    data = libs.DB.get_one_where(libs.models.Order, mashin_id = self.db_row.mashin.id, user_id=self.user.id,
                                                         chk=False)
                    # libs.DB.delete_object(data)
                    # for i in data:
                    data.chk = True
                    libs.DB.add_object_to_session(data)

                    self.db_row.mashin.el_in = 0
                    self.db_row.mashin.el_out = 0
                    self.db_row.mashin.bill = 0

                    libs.DB.add_object_to_session(self.db_row.mashin)
        self.db_row.fix_info = self.m_richText2.GetValue()
        self.db_row.is_fix = True
        self.db_row.user_fix_id = self.user.id
        self.db_row.fix_time = libs.models.TZ.now()
        self.db_row.part_mony = mony
        libs.DB.add_object_to_session(self.db_row)
        try:
            libs.DB.commit()
        except Exception as e:
            libs.DB.rollback()
            dial = wx.MessageDialog(self, *gui_lib.msg.CART_IN_USE)
            dial.ShowModal()
            return
        if self.user.grup.auto_mail is True:
            if self.db_row.mashin_id != None:
                my_text = u'STATUS:OK \n %s: %s \n FIX %s: %s \n %s: %s' % (gui_lib.msg.service_NewTask[1], str(self.db_row.mashin.nom_in_l), gui_lib.msg.service_NewTask[2], str(self.user.name), gui_lib.msg.service_NewTask[3], self.m_richText2.GetValue())
            else:
                my_text = u'STATUS:OK \n %s: %s \n FIX %s: %s \n %s: %s' % (
                gui_lib.msg.service_NewTask[1], gui_lib.msg.service_NewTask[4], gui_lib.msg.service_NewTask[2],
                str(self.user.name), gui_lib.msg.service_NewTask[3], self.m_richText2.GetValue())
            self.sendMail(my_text)
        self.OnClose(event)


    def OnHide( self, event ):
        self.m_checkBox1.Hide()
        self.m_checkBox2.Hide()
        self.m_checkBox1.SetValue(False)
        self.m_checkBox2.SetValue(False)
        self.m_checkBox3.Hide()
        self.m_checkBox4.SetValue(True)
        self.m_checkBox4.Hide()
        self.Layout()

    def OnShow( self, event ):
        self.m_checkBox1.Show()
        self.m_checkBox2.Show()
        self.m_checkBox3.Show()
        self.m_checkBox3.SetValue(True)
        self.m_checkBox4.SetValue(True)
        self.m_checkBox4.Show()
        self.Layout()

    def OnDeselect( self, event ):
        self.m_checkBox1.SetValue(False)
        self.m_checkBox2.SetValue(False)
        # self.m_checkBox4.SetValue(True)

    def OnDeselect3( self, event ):
        self.m_checkBox3.SetValue(False)
        # self.m_checkBox4.SetValue(True)

    def OnClose(self, event):
        self.Destroy()

class NewTask(gui.NewTask, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user, device=None, show=False):
        self.parent = parent
        self.show = show
        gui.NewTask.__init__(self, self.parent)
        self.user = user
        self.device = device
        if self.device != None:
            self.m_staticText1.SetLabel(u'')
            lists = [str(self.device.nom_in_l)]
            self.m_choice1.SetItems(lists)
            self.m_choice1.SetSelection(0)
            self.m_choice1.Disable()
        else:
            self._load_mashin()
        if show is not False:
            # self.m_button2.Disable()
            self.m_staticText1.SetLabel(u'')
            if show.mashin_id != None:
                lists = [str(show.mashin.nom_in_l)]
            else:
                lists = [u'']
            self.m_choice1.SetItems(lists)
            self.m_choice1.SetSelection(0)
            self.m_choice1.Disable()
            self.m_richText1.SetValue(show.info)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_richText1.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
        self._localise()
        # self.Layout()
        # self.Fit()

    def _localise(self):
        self.SetLabel(gui_lib.msg.service_NewTask['name'])
        self.m_staticText1.SetLabel(gui_lib.msg.service_NewTask['m_staticText1'])
        self.m_button1.SetLabel(gui_lib.msg.service_NewTask['m_button1'])
        self.m_button2.SetLabel(gui_lib.msg.service_NewTask['m_button2'])

    def _load_mashin(self):
        device = libs.DB.get_all_where(libs.models.Device, enable=True, order='nom_in_l')
        self.load = ['']
        for i in device:
            self.load.append(str(i.nom_in_l))
        self.m_choice1.SetItems(self.load)

    def OnDeviceSelect(self, event):
        if self.m_choice1.GetString(self.m_choice1.GetSelection()) != '':
            nom_in_l = self.m_choice1.GetString(self.m_choice1.GetSelection())
            self.device = libs.DB.get_one_where(libs.models.Device, nom_in_l=nom_in_l, enable=True)
        else:
            self.device = None

    def sendMail(self, text):
        try:
            send_to = self.user.grup.boss_mail
            subject = self.user.grup.subject
            # subject = json.loads(subject.value)[libs.conf.ID]
            send_mail_to = send_to.split(',')
            for i in send_mail_to:
                # libs.sendmail.Gmail(html, i, libs.conf.CONF.get('MAIL', 'subject', 'str'))
                a1 = libs.sendmail.Gmail(text, i,
                                         subject+' NEW TASK')
            a2 = libs.sendmail.Gmail(text, self.user.grup.service_mail,
                                         subject + ' NEW TASK')
            if a2 is not True:
                dlg = wx.MessageDialog(self, *gui_lib.msg.MAIL_NOT_SEND)
                dlg.ShowModal()
        except Exception as e:
            dlg = wx.MessageDialog(self, *gui_lib.msg.MAIL_NOT_SEND)
            dlg.ShowModal()
            raise e

    def OnSave( self, event ):
        # print self.m_richText1.GetValue()
        # return
            # dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            # dial.ShowModal()
            # return
        if self.show is False:
            obj = libs.DB.make_obj(libs.models.EMGService)
            if self.device != None:
                obj.mashin_id = self.device.id
        else:
            obj = self.show

        obj.user_id = self.user.id
        obj.info = self.m_richText1.GetValue()
        libs.DB.add_object_to_session(obj)
        libs.DB.commit()
        if self.user.grup.auto_mail is True:
            if self.show is False:
                if self.device != None:
                    my_text = u'%s: %s \n %s: %s \n %s: %s' % (gui_lib.msg.service_NewTask[1], str(self.device.nom_in_l), gui_lib.msg.service_NewTask[2], str(self.user.name), gui_lib.msg.service_NewTask[3], self.m_richText1.GetValue())
                else:
                    my_text = u'%s: %s \n %s: %s \n %s: %s' % (
                    gui_lib.msg.service_NewTask[1], gui_lib.msg.service_NewTask[4], gui_lib.msg.service_NewTask[2],
                    str(self.user.name), gui_lib.msg.service_NewTask[3], self.m_richText1.GetValue())
            else:
                if self.device != None:
                    my_text = u'%s: %s \n EDIT %s: %s \n %s: %s' % (gui_lib.msg.service_NewTask[1], str(self.device.nom_in_l), gui_lib.msg.service_NewTask[2], str(self.user.name), gui_lib.msg.service_NewTask[3], self.m_richText1.GetValue())
                else:
                    my_text = u'%s: %s \n EDIT %s: %s \n %s: %s' % (
                    gui_lib.msg.service_NewTask[1], gui_lib.msg.service_NewTask[4], gui_lib.msg.service_NewTask[2],
                    str(self.user.name), gui_lib.msg.service_NewTask[3], self.m_richText1.GetValue())
            self.sendMail(my_text)
        self.OnClose(event)

    def OnClose(self, event):
        self.Destroy()

class MSG(gui.MSG, gui_lib.keybords.Keyboard):
    def __init__(self, parent, msg=u''):
        gui.MSG.__init__(self, parent)
        self.m_richText2.SetValue(msg)
        # if libs.conf.USE_VIRTUAL_KEYBORD is True:
        #     self.m_richText2.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose( self, event ):
        self.Destroy()

class RunCommand(gui.RunCommand, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        self.parent = parent
        gui.RunCommand.__init__(self, parent)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl20.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)
            self.m_textCtrl21.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
        self.add_device()
        self._resize()

    def _resize(self):
        self.SetMinSize((428,378))

    def add_device(self):
        var = ['jackpot', 'redirect', gui_lib.msg.service_NewTask[5]]
        for i in self.parent.all_mashin():
            var.append(str(i.nom_in_l))
        self.m_choice17.SetItems(var)
        self.m_choice17.SetSelection(0)

    def OnSend( self, event ):
        passwd = self.m_textCtrl20.GetValue()
        show_response = self.m_checkBox8.GetValue()
        if passwd != u'use_system10':
            dial = wx.MessageDialog(self, *gui_lib.msg.PASSWD_WRONG)
            dial.ShowModal()
        else:
            cmd = self.m_textCtrl21.GetValue()
            if self.m_choice17.GetString(self.m_choice17.GetSelection()) == gui_lib.msg.service_NewTask[5]:
                device = self.parent.all_mashin()
                dial = RunCMDOnAllSMIB(self, device, cmd, show_response=show_response)
                dial.ShowModal()
                if dial.msg != None:
                    dial = MSG(self, dial.msg)
                    dial.ShowModal()
            else:
                try:
                    device = int( self.m_choice17.GetString(self.m_choice17.GetSelection()))
                    device = libs.DB.get_one_where(libs.models.Device, enable=True, nom_in_l=device)
                    response = libs.udp.send('run_linux_cmd', device.ip, cmd=cmd, show_response=show_response)
                except ValueError:
                    device = self.m_choice17.GetString(self.m_choice17.GetSelection())
                    if device == 'jackpot':
                        response = libs.udp.send('run_linux_cmd', libs.conf.JPSERVERIP, libs.conf.JPSERVERPORT, cmd=cmd)
                    else:
                        response = libs.udp.send('run_linux_cmd_on_redirect', libs.conf.SERVER, cmd=cmd)
                if response == None:
                    response = 'None'
                elif response is True:
                    response = 'True'
                elif response is False:
                    response = 'False'
                dial = MSG(self, response)
                dial.ShowModal()


    def OnClose( self, event ):
        self.Destroy()

class Main(gui.Main):
    def __init__(self, parent, user, all_mashin):
        self.parent = parent
        self.user = user
        self.USER = self.user
        self.mashinDict = all_mashin
        gui.Main.__init__(self, self.parent)
        self.parent.help_name = 'service.html'
        self.m_listCtrl1.InsertColumn(0, gui_lib.msg.service_Main[2])
        self.m_listCtrl1.InsertColumn(1, gui_lib.msg.service_Main[3])
        self.m_listCtrl1.InsertColumn(2, gui_lib.msg.service_Main[4])
        self.m_listCtrl1.InsertColumn(3, gui_lib.msg.service_Main[5])
        self.m_listCtrl1.InsertColumn(4, gui_lib.msg.service_Main[6])


        self._set_menu()
        self._resize(None)

        self.parent.SetLabel(libs.conf.CASINO_NAME + ': ' +  gui_lib.msg.service_Main['name'])

        self._load_fix(None)
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_SIZE, self._resize)
        randomId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OpenForCMD, id=randomId)
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('r'), randomId)])
        self.SetAcceleratorTable(accel_tbl)
        # self.Fit()

    def OpenForCMD(self, event):
        dial = RunCommand(self.parent)
        dial.ShowModal()

    def _set_menu(self):
        self.m_toolBar1.ClearTools()
        self.m_tool2 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.service_Main['m_tool2'],
                                                    wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/preferences-system-time.png",
                                                              wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                    gui_lib.msg.service_Main['m_tool2m'], wx.EmptyString, None)

        self.m_tool3 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.service_Main['m_tool3'],
                                                    wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/Gnome-Audio-Volume-Muted-64.png",
                                                              wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                    gui_lib.msg.service_Main['m_tool3m'], wx.EmptyString, None)

        self.m_tool41 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.service_Main['m_tool41'],
                                                     wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/Gnome-Audio-Volume-High-64.png",
                                                               wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                     gui_lib.msg.service_Main['m_tool41m'], wx.EmptyString, None)

        self.m_tool5 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.service_Main['m_tool5'],
                                                    wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/cpu.png", wx.BITMAP_TYPE_ANY),
                                                    wx.NullBitmap,
                                                    wx.ITEM_NORMAL, gui_lib.msg.service_Main['m_tool5m'], wx.EmptyString, None)

        # self.m_tool6 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.service_Main['m_tool6'],
        #                                             wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/Gnome-Preferences-Other-64.png",
        #                                                       wx.BITMAP_TYPE_ANY),
        #                                             wx.NullBitmap,
        #                                             wx.ITEM_NORMAL, gui_lib.msg.service_Main['m_tool6m'],
        #                                             wx.EmptyString, None)

        self.m_tool4 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.service_Main['m_tool4'],
                                                    wx.Bitmap(
                                                        libs.conf.IMG_FOLDER + u"64x64/dialog-error.png",
                                                        wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                    gui_lib.msg.service_Main['m_tool4m'], wx.EmptyString,
                                                    None)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_TOOL, self.OnClose, id=self.m_tool4.GetId())
        self.Bind(wx.EVT_TOOL, self.NewTask, id=self.m_tool2.GetId())
        self.Bind(wx.EVT_TOOL, self.AlarmStop, id=self.m_tool3.GetId())
        self.Bind(wx.EVT_TOOL, self.AlarmStart, id=self.m_tool41.GetId())
        self.Bind(wx.EVT_TOOL, self.OnFix, id=self.m_tool5.GetId())
        # self.Bind(wx.EVT_TOOL, self.OnMonitoring, id=self.m_tool6.GetId())
        self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnShowInfo)
        self.m_toolBar1.Realize()

    def OnMonitoring(self, event):
        webbrowser.open_new_tab('http://%s:9021' % (libs.conf.SERVER))

    def _load_fix(self, event):
        self.mashinDict = {}
        index = 0
        data = libs.DB.get_all_where(libs.models.EMGService, is_fix=False)
        self.m_listCtrl1.DeleteAllItems()
        for i in data:
            if i.mashin_id == None:
                self.m_listCtrl1.InsertItem(index, u'')
                self.m_listCtrl1.SetItem(index, 1, u'')
                self.m_listCtrl1.SetItem(index, 2, u'')
            else:
                self.m_listCtrl1.InsertItem(index, str(i.mashin.nom_in_l))
                self.m_listCtrl1.SetItem(index, 1, str(i.mashin.serial))
                self.m_listCtrl1.SetItem(index, 2, str(i.mashin.model.name))
            self.m_listCtrl1.SetItem(index, 3, str(i.info))
            self.m_listCtrl1.SetItem(index, 4, libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
            self.mashinDict[index] = i
            index += 1


    def _resize(self, event):
        width, height = self.parent.GetSize()
        if width != width or height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height * 0.95))
        self.m_listCtrl1.SetSize((self.width * 0.95, self.height * 0.75))
        self.m_toolBar1.SetMinSize((self.width, -1))
        self.m_listCtrl1.SetColumnWidth(0, self.width * 0.06)
        self.m_listCtrl1.SetColumnWidth(1, self.width * 0.18)
        self.m_listCtrl1.SetColumnWidth(2, self.width * 0.18)
        self.m_listCtrl1.SetColumnWidth(3, self.width * 0.35)
        self.m_listCtrl1.SetColumnWidth(4, self.width * 0.20)
        # self.Layout()


    def NewTask( self, event ):
        dial = NewTask(self, self.user)
        dial.ShowModal()
        self._load_fix(event)

    def AlarmStart( self, event ):
        try:
            item = self.mashinDict[self.m_listCtrl1.GetFirstSelected()]
            if item.mashin_id == None:
                raise KeyError
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            data = libs.udp.send('sas.start_alarm', item.mashin.ip)
            if data is True:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
                dial.ShowModal()

    def AlarmStop( self, event ):
        try:
            item = self.mashinDict[self.m_listCtrl1.GetFirstSelected()]
            if item.mashin_id == None:
                raise KeyError
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            data = libs.udp.send('sas.stop_alarm', item.mashin.ip)
            if data is True:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
                dial.ShowModal()

    def OnFix( self, event ):
        try:
            item = self.mashinDict[self.m_listCtrl1.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            dial = Fix(self, self.user, item)
            dial.ShowModal()
            self._load_fix(event)

    def OnShowInfo( self, event ):
        try:
            item = self.mashinDict[self.m_listCtrl1.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            dial = NewTask(self, self.user, show=item)
            dial.ShowModal()

    def OnClose( self, event ):
        self.parent.help_name = 'main.html'
        self.parent.show_panel()
        self.Destroy()


class RunCMDOnAllSMIB(gui.Guage):
    def __init__(self, parent, device, comand, show_response=False):
        self.parent = parent
        self.device = device
        self.cmd = comand
        gui.Guage.__init__(self, parent)
        self.SetTitle(gui_lib.msg.service_NewTask[6])
        self.m_button23.SetLabel(gui_lib.msg.service_NewTask['m_button1'])

        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width * 0.47, self.height * 0.15))
        self.m_gauge1.SetMinSize((self.width * 0.45, -1))
        # self.mashin = mashin
        # self.reboot_time = reboot_time
        self.m_gauge1.SetRange(len(self.device))
        self.worker = task.ComandRun(self, device=self.device, comand=self.cmd, show_response=show_response)
        task.EVT_COMAND(self, self.SetData)
        self.loop = 0
        self.msg = None
        self.Layout()

    def SetData(self, event):
        '''
            Когато командата мине позицията на лентата се премества с 1
            Ако броя на машините е 50 и са минали 10
            Лентата за прогреса се мести на позиция 10 или 10 % от общата дължина на процеса
        '''
        if event.data is True:
            self.loop = self.loop + 1
            self.m_gauge1.SetValue(self.loop)
        else:
            self.msg = event.data
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()


    def OnClose(self, event):
        '''
            Затваря прозореца като спира препрограмирането на кей системите
        '''
        self.worker.abort()
        self.Destroy()
