# -*- coding:utf-8 -*-
'''
Created on 23.06.2017 г.

@author: dedal
'''

import wx
import libs
import gui_lib
import mony
from . import gui
# import __builtin__
from . import task
import datetime
import json
import time
import os
import threading
from queue import Empty, Queue
Q = Queue()
class OrderByHand(gui.OrderByHand):  # @UndefinedVariable
    def __init__(self, parent, error_m=[], user=None):
        gui.OrderByHand.__init__(self, parent)  # @UndefinedVariable
        self.width, self.height = wx.GetDisplaySize()
        self.SetTitle(gui_lib.msg.order_main_OrderByHand_name)
        self.m_button4.SetLabel(gui_lib.msg.order_main_OrderByHand_button['m_button4'])
        self.m_listCtrl4.InsertColumn(0, gui_lib.msg.order_main_OrderByHand_text[1])
        self.m_listCtrl4.InsertColumn(1, gui_lib.msg.order_main_OrderByHand_text[2])
        self.m_listCtrl4.SetColumnWidth(1, self.width // 3)
        self.parent = parent
        if user == None:
            user = self.parent.GetParent().USER
        self.user =   user
        self.error = error_m
        self._add_list()
        self.parent = parent

    def _add_list(self):
        if self.user.flor_id == None:
            mashins = libs.DB.get_all_where(libs.models.Device, enable=True, sas=False, order='nom_in_l')
        else:
            mashins = libs.DB.get_all_where(libs.models.Device, flor_id=self.user.flor_id, enable=True, sas=False,
                                            order='nom_in_l')
        if self.error != []:
            for item in self.error:
                mashins.append(libs.DB.get_one_where(libs.models.Device, nom_in_l=item, enable=True))
        index = 0
        self.mashinDict = {}
        for item in mashins:
            self.m_listCtrl4.InsertItem(index, str(item.nom_in_l))
            self.m_listCtrl4.SetItem(index, 1, str(item.model.name))
            self.mashinDict[index] = item
            index += 1

    def _list_update(self):
        index = 0
        var = {}
        for item in self.mashinDict:
            self.m_listCtrl4.InsertItem(index, str(self.mashinDict[item].nom_in_l))
            self.m_listCtrl4.SetItem(index, 1, str(self.mashinDict[item].model.name))
            var[index] = self.mashinDict[item]
            index += 1
        self.mashinDict = {}
        self.mashinDict = var

    def list_refresh(self):
        self.m_listCtrl4.DeleteAllItems()
        self._list_update()

    def OnOrder(self, event):
        currentItem = event.GetIndex()
        mashine = self.mashinDict[currentItem]
        panel = NotSASCounter(self.parent, mashine, user=self.user)
        panel.ShowModal()
        save = panel.save
        if save is True:
            if self.mashinDict[currentItem].nom_in_l in self.error:
                try:
                    del self.error[self.error.index(self.mashinDict[currentItem].nom_in_l)]
                except KeyError as e:
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
                    libs.log.stderr_logger.critical('%s', self.error)

            del self.mashinDict[currentItem]
            self.list_refresh()
            # self.parent.order_refresh()
            self.parent.kasa_refresh()
        if len(self.mashinDict) == 0:
            self.OnClose(event)

    def OnClose(self, event):
        # self.parent.order_refresh()
        self.parent.kasa_refresh()
        self.Destroy()

class NotSASCounter(gui.NotSASCounter, gui_lib.keybords.Keyboard):
    def __init__(self, parent, mashins, edit=None, user=None):
        gui.NotSASCounter.__init__(self, parent)
        self.mashins = mashins
        self.save = False
        self.edit = edit
        self.parent = parent
        if user == None:
            user = self.parent.GetParent().USER
        self.user = user
        self.m_textCtrl8.SetFocus()
        self.SetTitle(gui_lib.msg.order_main_NotSASCounter_name)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl8.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl9.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl10.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

        self.m_staticText15.SetLabel(
            gui_lib.msg.order_main_NotSASCounter_text['m_staticText15'] + u': ' + str(self.mashins.nom_in_l))
        self.m_staticText17.SetLabel(gui_lib.msg.order_main_NotSASCounter_text['m_staticText17'])
        self.m_staticText19.SetLabel(gui_lib.msg.order_main_NotSASCounter_text['m_staticText19'])
        self.m_staticText21.SetLabel(gui_lib.msg.order_main_NotSASCounter_text['m_staticText21'])
        self.m_staticText16.SetLabel(gui_lib.msg.order_main_NotSASCounter_text['m_staticText16'])
        self.m_staticText18.SetLabel(gui_lib.msg.order_main_NotSASCounter_text['m_staticText18'])
        self.m_staticText20.SetLabel(gui_lib.msg.order_main_NotSASCounter_text['m_staticText20'])
        self.m_checkBox1.SetLabel(gui_lib.msg.order_main_NotSASCounter_button['m_checkBox1'])
        self.m_button6.SetLabel(gui_lib.msg.order_main_NotSASCounter_button['m_button6'])
        self.m_button7.SetLabel(gui_lib.msg.order_main_NotSASCounter_button['m_button7'])
        self.m_checkBox1.SetToolTip(gui_lib.msg.order_main_NotSASCounter_tooltip['m_checkBox1'])
        self.m_textCtrl10.SetToolTip(gui_lib.msg.order_main_NotSASCounter_tooltip['m_textCtrl10'])
        if self.edit != None:
            libs.DB.expire(self.edit)
            self.m_textCtrl8.SetValue(str(self.edit.new_enter))
            self.m_textCtrl9.SetValue(str(self.edit.new_exit))
            self.m_textCtrl10.SetValue(str(self.edit.bill_new))
            self.OnCheck(None)
        else:
            self.m_staticText22.SetLabel(gui_lib.msg.order_main_NotSASCounter_text['m_staticText22'] + u': 0.00')
        self.Layout()
        self.Fit()

    def OnMathIn(self, event):
        try:
            if self.m_checkBox1.GetValue() is False:
                math = int(self.m_textCtrl8.GetValue()) * self.mashins.el_coef
                if self.edit == None:
                    math = math - (self.mashins.el_in * self.mashins.el_coef)
                else:
                    math = math - (self.edit.old_enter * self.mashins.el_coef)
                self.m_staticText17.SetLabel("{:.2f}".format(math))
            else:
                math = int(self.m_textCtrl8.GetValue()) * self.mashins.mex_coef
                math = math - (self.mashins.mex_in * self.mashins.mex_coef)
                self.m_staticText17.SetLabel("{:.2f}".format(math))
        except ValueError:
            pass
        self.OnMathTotal()

    def OnMathOut(self, event):
        try:
            if self.m_checkBox1.GetValue() is False:
                math = int(self.m_textCtrl9.GetValue()) * self.mashins.el_coef
                if self.edit == None:
                    math = math - (self.mashins.el_out * self.mashins.el_coef)
                else:
                    math = math - (self.edit.old_exit * self.mashins.el_coef)
                self.m_staticText19.SetLabel("{:.2f}".format(math))
            else:
                math = int(self.m_textCtrl9.GetValue()) * self.mashins.mex_coef
                math = math - (self.mashins.mex_out * self.mashins.mex_coef)
                self.m_staticText19.SetLabel("{:.2f}".format(math))
        except ValueError:
            pass
        self.OnMathTotal()

    def OnMathBill(self, event):
        try:
            if self.m_checkBox1.GetValue() is False:
                if self.edit == None:
                    math = int(self.m_textCtrl10.GetValue()) - self.mashins.bill
                    math = round(math, 2)
                else:
                    math = int(self.m_textCtrl10.GetValue()) - self.edit.bill_old
                    math = round(math, 2)
            else:
                math = int(self.m_textCtrl10.GetValue())
                math = round(math, 2)

            self.m_staticText21.SetLabel("{:.2f}".format(math))
        except ValueError:
            pass
        self.Fit()

    def OnMathTotal(self):
        ins = float(self.m_staticText17.GetLabel())
        out = float(self.m_staticText19.GetLabel())
        self.m_staticText22.SetLabel(
            gui_lib.msg.order_main_NotSASCounter_text['m_staticText22'] + u': ' + "{:.2f}".format(ins - out))
        self.Fit()

    def OnCheck(self, event):
        if self.m_checkBox1.GetValue() is False:
            self.m_textCtrl10.SetToolTip(gui_lib.msg.order_main_NotSASCounter_tooltip['m_textCtrl10'])
        else:
            self.m_textCtrl10.SetToolTip(gui_lib.msg.order_main_NotSASCounter_tooltip['m_textCtrl10_1'])
        try:
            self.OnMathIn(event)
        except ValueError:
            pass
        try:
            self.OnMathOut(event)
        except ValueError:
            pass
        try:
            self.OnMathBill(event)
        except ValueError:
            pass

    def OnGo(self, event):
        libs.DB.expire(self.mashins)
        mashin_id = self.mashins.id
        libs.DB.expire(self.user)
        if self.edit == None:
            if float(self.m_staticText17.GetLabel()) < 0 or float(self.m_staticText19.GetLabel()) < 0 or float(
                    self.m_staticText21.GetLabel()) < 0:
                dial = wx.MessageDialog(self, *gui_lib.msg.BAD_COUNTER)
                dial.ShowModal()
                return
            old_enter = self.mashins.el_in
            old_exit = self.mashins.el_out
            old_bill = self.mashins.bill
            old_mex_enter = self.mashins.mex_in
            old_mex_exit = self.mashins.mex_out
        else:
            libs.DB.expire(self.edit)
            self.mashins.mex_out = self.edit.mex_old_exit
            self.mashins.mex_in = self.edit.mex_old_enter
            self.mashins.el_in = self.edit.old_enter
            self.mashins.el_out = self.edit.old_exit
            self.mashins.bill = self.edit.bill_old
            if self.m_checkBox1.GetValue() is False:
                if int(self.m_textCtrl10.GetValue()) < self.mashins.bill:
                    dial = wx.MessageDialog(self, *gui_lib.msg.BAD_COUNTER)
                    dial.ShowModal()
                    return
            else:
                self.m_textCtrl10.SetValue(str(int(self.m_textCtrl10.GetValue()) + self.mashins.bill))
            if int(self.m_textCtrl8.GetValue()) < self.mashins.el_in or int(
                    self.m_textCtrl9.GetValue()) < self.mashins.el_out:
                dial = wx.MessageDialog(self, *gui_lib.msg.BAD_COUNTER)
                dial.ShowModal()
                return

            total = ((self.edit.new_enter - self.edit.old_enter) - (
                    self.edit.new_exit - self.edit.old_exit)) * self.mashins.el_coef

            self.user.kasa = self.user.kasa - total


            old_enter = self.mashins.el_in
            old_exit = self.mashins.el_out
            old_bill = self.mashins.bill
            old_mex_enter = self.mashins.mex_in
            old_mex_exit = self.mashins.mex_out

        old_won = self.mashins.won
        old_bet = self.mashins.bet
        new_won = old_won
        new_bet = old_bet

        try:
            new_enter = int(self.m_textCtrl8.GetValue())
            new_exit = int(self.m_textCtrl9.GetValue())
            new_bill = int(self.m_textCtrl10.GetValue())
        except ValueError:
            dial = wx.MessageDialog(self, *gui_lib.msg.BAD_COUNTER)
            dial.ShowModal()
            return
        if self.m_checkBox1.GetValue() is True:
            if new_bill - self.mashins.bill_in_device < 0:
                dial = wx.MessageDialog(self, *gui_lib.msg.BAD_COUNTER)
                dial.ShowModal()
                return
            new_bill = old_bill + new_bill - self.mashins.bill_in_device
            new_enter = int(old_enter + (new_enter - self.mashins.mex_in) / self.mashins.el_coef)
            new_exit = int(old_exit + (new_exit - self.mashins.mex_out) / self.mashins.el_coef)
        if new_bill - old_bill > (new_enter - old_enter) * self.mashins.el_coef and self.edit == None:
            dial = wx.MessageDialog(self, *gui_lib.msg.BAD_COUNTER)
            dial.ShowModal()
            return
        total = self.m_staticText22.GetLabel()
        total = total.replace((gui_lib.msg.order_main_NotSASCounter_text['m_staticText22'] + u': '), '')
        total = float(total)
        m_in = self.mashins.mex_in + int(float(self.m_staticText17.GetLabel()))
        m_out = self.mashins.mex_out + int(float(self.m_staticText19.GetLabel()))

        new_mex_enter = m_in
        new_mex_exit = m_out
        self.mashins.el_in = new_enter
        self.mashins.el_out = new_exit
        self.mashins.mex_in = m_in
        self.mashins.mex_out = m_out

        if self.edit == None:
            mony_in_user = self.user.kasa + total
            bill_in_device = new_bill - self.mashins.bill
            mony_in_user -= bill_in_device
            self.mashins.bill_in_device += bill_in_device
        else:
            mony_in_user = self.user.kasa + total
            mony_in_user += self.mashins.bill_in_device
            write_bill_in_device = self.mashins.bill_in_device
            self.mashins.bill_in_device = 0
            dial = wx.MessageDialog(self, *gui_lib.msg.GET_BILL_NOW)
            dial.ShowModal()

        self.mashins.won = self.mashins.won
        self.mashins.bet = self.mashins.bet
        self.mashins.bill = new_bill
        self.mashins.by_hend_order = self.m_checkBox1.GetValue()

        libs.DB.add_object_to_session(self.mashins)

        if self.edit == None:
            ords = libs.DB.make_obj(libs.models.Order)
            ords.mashin_id = mashin_id
            ords.flor_id = self.mashins.flor_id
            ords.old_enter = old_enter
            ords.new_enter = new_enter
            ords.old_exit = old_exit
            ords.new_exit = new_exit
            ords.mex_old_enter = old_mex_enter
            ords.mex_new_enter = new_mex_enter
            ords.mex_old_exit = old_mex_exit
            ords.mex_new_exit = new_mex_exit
            ords.bill_old = old_bill
            ords.bill_new = new_bill
            ords.user_id = self.user.id
            ords.old_won = old_won
            ords.new_won = new_won
            ords.old_bet = old_bet
            ords.new_bet = new_bet

            libs.DB.add_object_to_session(ords)

        else:
            old_data = {'new_enter': self.edit.new_enter,
                        'new_exit': self.edit.new_exit,
                        'new_bill': self.edit.bill_new,
                        'user': self.user.id,
                        'date': libs.models.TZ.date_to_str(libs.models.TZ.now()),
                        }
            bill_take = libs.DB.get_one_where(libs.models.BillTake, mashin_id=mashin_id, chk=False, user_id=self.user.id)
            if bill_take != None:
                bill_take.mony -= self.edit.bill_new-self.edit.bill_old
                bill_take.mony += new_bill-old_bill

            else:
                bill_take = libs.DB.make_obj(libs.models.BillTake)

                bill_take.mony = write_bill_in_device + new_bill-old_bill
                bill_take.mashin_id = mashin_id
                bill_take.user_id = self.user.id
                bill_take.chk = False
            libs.DB.add_object_to_session(bill_take)
            ords = libs.DB.make_obj(libs.models.Order)
            ords.mashin_id = mashin_id
            ords.flor_id = self.mashins.flor_id
            ords.old_enter = old_enter
            ords.new_enter = new_enter
            ords.old_exit = old_exit
            ords.new_exit = new_exit
            ords.mex_old_enter = old_mex_enter
            ords.mex_new_enter = new_mex_enter
            ords.mex_old_exit = old_mex_exit
            ords.mex_new_exit = new_mex_exit
            ords.bill_old = old_bill
            ords.bill_new = new_bill
            ords.user_id = self.user.id
            ords.old_won = old_won
            ords.new_won = new_won
            ords.old_bet = old_bet
            ords.new_bet = new_bet
            ords.last_edit_by_id = self.user.id
            ords.last_edit_time = libs.models.TZ.now()
            if self.edit.old_data != None:
                my_old_data = json.loads(self.edit.old_data)
            else:
                my_old_data = []
            my_old_data.append(old_data)
            ords.old_data = json.dumps(my_old_data)
            libs.DB.add_object_to_session(ords)
            libs.DB.delete_object(self.edit)
        self.user.kasa = mony_in_user
        libs.DB.add_object_to_session(self.user)
        try:
            libs.DB.commit()
            self.save = True
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
            dial.ShowModal()
            libs.DB.rollback()
            return

        self.Destroy()

    def OnClose(self, event):
        self.Destroy()


class GetCounter(gui.GetCounter):
    def __init__(self, parent, mashin_to_ord=[], user=None, cart=False):
        gui.GetCounter.__init__(self, parent)
        self.width, self.height = wx.GetDisplaySize()
        self.m_gauge1.SetMinSize((self.width // 2, -1))
        self.SetTitle(gui_lib.msg.order_main_GetCounter_name)
        self.cart = cart
        self.m_button1.SetLabel(gui_lib.msg.order_main_GetCounter_button['m_button1'])
        self.parent = parent
        if user == None:
            user = self.parent.GetParent().USER
        self.user = user
        self.error = []
        self.m_staticText15.SetLabel(gui_lib.msg.order_main_GetCounter_text['m_staticText15'] + u': ')
        if mashin_to_ord == []:
            if self.user.flor_id != None:
                self.mashin = libs.DB.get_all_where(libs.models.Device, flor_id=self.user.flor_id, enable=True,
                                                    sas=True, order='nom_in_l')
            else:
                self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, sas=True, order='nom_in_l')
        else:
            self.mashin = []
            for item in mashin_to_ord:
                self.mashin.append(libs.DB.get_one_where(libs.models.Device, nom_in_l=item, enable=True, sas=True))
        self.m_gauge1.SetRange(len(self.mashin)+1)
        # self.m_button1.Disable()
        self.worker = task.CounterInfo(self, self.mashin, self.user, self.cart)
        task.EVT_COUNTER_GET(self, self.GetCount)
        self.loop = 0

    def GetCount(self, event):
        try:
            if type(event.data) == int:
                self.loop = self.loop + 1
                self.m_staticText15.SetLabel(
                    gui_lib.msg.order_main_GetCounter_text['m_staticText15'] + u': ' + str(event.data) + ' ' +
                    gui_lib.msg.order_main_GetCounter_text['OK'])
                self.m_gauge1.SetValue(self.loop)
            elif type(event.data) == dict:
                self.loop = self.loop + 1
                self.m_staticText15.SetLabel(gui_lib.msg.order_main_GetCounter_text['m_staticText15'] + u': ' + str(
                    event.data['ERROR']) + ' ' + gui_lib.msg.order_main_GetCounter_text['error'])
                self.m_gauge1.SetValue(self.loop)

            elif type(event.data) == list:
                self.loop = self.loop + 1
                self.m_gauge1.SetValue(self.loop)
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
                self.error = event.data
                # self.m_button1.Enable()
            elif type(event.data) == str:
                if event.data != 'ERROR':
                    self.loop = self.loop + 1
                    self.m_staticText15.SetLabel(gui_lib.msg.order_main_GetCounter_text['m_staticText15'] + u': ' + str(event.data))
                    self.m_gauge1.SetValue(self.loop)
                else:
                    self.loop = self.loop + 1
                    self.m_gauge1.SetValue(self.loop)
                    dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                    dial.ShowModal()
        except NameError:
            pass


    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.worker:
            self.worker.abort()
            self.Destroy()

    def OnClose(self, event):
        if self.worker.is_alive():
            self.OnTaskStop(event)
        self.Destroy()

class GetBillGuage(gui.GetCounter):
    def __init__(self, parent):
        gui.GetCounter.__init__(self, parent)
        self.width, self.height = wx.GetDisplaySize()
        self.m_gauge1.SetMinSize((self.width // 2, -1))
        self.parent = parent
        self.m_staticText15.SetLabel(gui_lib.msg.order_main_GetBillGuage_text['m_staticText15'] + u': ')
        self.SetTitle(gui_lib.msg.order_main_GetBillGuage_name)
        self.m_button1.SetLabel(gui_lib.msg.order_main_GetBillGuage_button['m_button1'])
        count = 0
        for i in self.parent.mashin:
            if i.bill_get is True:
                count += 1
        self.m_gauge1.SetRange(count)
        # self.m_button1.Disable()
        self.loop = 0
        self.worker = task.BillGet(self, self.parent.mashin, self.parent.GetParent().USER)
        task.EVT_BILL_GET(self, self.GetCount)
        self.error = []

    def GetCount(self, event):
        if type(event.data) == int:
            self.loop = self.loop + 1
            self.m_staticText15.SetLabel(
                gui_lib.msg.order_main_GetBillGuage_text['m_staticText15'] + u': ' + str(event.data) + ' ' +
                gui_lib.msg.order_main_GetBillGuage_text['OK'])
            self.m_gauge1.SetValue(self.loop)
        elif type(event.data) == dict:
            self.loop = self.loop + 1
            self.m_staticText15.SetLabel(gui_lib.msg.order_main_GetBillGuage_text['m_staticText15'] + u': ' + str(
                event.data['ERROR']) + ' ' + gui_lib.msg.order_main_GetBillGuage_text['error'])
            self.m_gauge1.SetValue(self.loop)
        else:
            if event.data == 'DONE':
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
            elif event.data == 'ERROR':
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
            # self.m_button1.Enable()

    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.worker:
            self.worker.abort()

    # def OnClose(self, event):
    #     self.Destroy()

    def OnClose(self, event):
        if self.worker.is_alive():
            self.OnTaskStop(event)
        self.Destroy()


#         self.parent.OnClose(event)


class BillInfoGuage(gui.GetCounter):
    def __init__(self, parent):
        gui.GetCounter.__init__(self, parent)
        self.width, self.height = wx.GetDisplaySize()
        self.m_gauge1.SetMinSize((self.width // 2, -1))
        self.parent = parent
        count = len(self.parent.mashin)
        self.m_gauge1.SetRange(count)
        self.SetTitle(gui_lib.msg.order_main_BillInfoGuage_name)
        self.m_button1.SetLabel(gui_lib.msg.order_main_BillInfoGuage_button['m_button1'])
        self.m_staticText15.SetLabel(gui_lib.msg.order_main_BillInfoGuage_text['m_staticText15'] + u': ')
        self.loop = 0
        # self.m_button1.Disable()
        self.worker = task.BillInfo(self, self.parent.mashin)
        task.EVT_BILL_GET(self, self.GetCount)

    def GetCount(self, event):
        # print(e)vent.data
        if type(event.data) == int:
            self.loop = self.loop + 1
            self.m_staticText15.SetLabel(
                gui_lib.msg.order_main_BillInfoGuage_text['m_staticText15'] + u': ' + str(event.data) + ' ' +
                gui_lib.msg.order_main_BillInfoGuage_text['OK'])
            self.m_gauge1.SetValue(self.loop)
        elif type(event.data) == dict:
            self.loop = self.loop + 1
            self.m_staticText15.SetLabel(gui_lib.msg.order_main_BillInfoGuage_text['m_staticText15'] + u': ' + str(
                event.data['ERROR']) + ' ' + gui_lib.msg.order_main_BillInfoGuage_text['error'])
            self.m_gauge1.SetValue(self.loop)
        else:
            #
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            # self.m_button1.Enable()

    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.worker:
            self.worker.abort()

    def OnClose(self, event):
        if self.worker.is_alive():
            self.OnTaskStop(event)
        self.Destroy()


class BillGet(gui.BillGet):
    def __init__(self, parent, i_get_bill=True, user=None):
        gui.BillGet.__init__(self, parent)
        self.parent = parent
        global Q
        self.q = Q
        self.i_get_bill = i_get_bill
        self.width, self.height = wx.GetDisplaySize()
        if user == None:
            user = self.parent.USER
        self.user = user
        # self.SetMinSize((-1, self.height*0.75))
        self.SetMinSize((-1, self.height * 0.55))
        self.SetTitle(gui_lib.msg.order_main_BillGet_name)
        self.m_button7.SetLabel(gui_lib.msg.order_main_BillGet_button['m_button7'])
        self.m_button8.SetLabel(gui_lib.msg.order_main_BillGet_button['m_button8'])
        self.m_listCtrl5.SetToolTip(gui_lib.msg.order_main_BillGet_tolltip['m_listCtrl5'])
        self.m_staticText11.SetLabel(gui_lib.msg.order_main_BillGet_text[1] + u': ' + u'0')
        self.m_listCtrl5.SetMinSize((self.width * 0.5, self.height * 0.4))
        if i_get_bill is True:
            if self.user.flor_id == None:
                self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, order='nom_in_l')
            else:
                self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, flor_id=self.user.flor_id,
                                                    order='nom_in_l')
        else:
            if self.user.flor_id == None:
                self.mashin = libs.DB.get_all_where(libs.models.Device, sas=True, enable=True, order='nom_in_l')
            else:
                self.mashin = libs.DB.get_all_where(libs.models.Device, sas=True, enable=True,
                                                    flor_id=self.user.flor_id, order='nom_in_l')

        for i in self.mashin:
            if i_get_bill is False:
                i.bill_get = False
                i.bill_mony = None
            else:
                i.bill_get = self.user.grup.get_all_bill
                i.bill_mony = i.bill_in_device

        self.m_listCtrl5.InsertColumn(0, gui_lib.msg.order_main_BillGet_text[2])
        self.m_listCtrl5.SetColumnWidth(0, self.width * 0.06)
        self.m_listCtrl5.InsertColumn(1, gui_lib.msg.order_main_BillGet_text[3])
        self.m_listCtrl5.SetColumnWidth(1, self.width * 0.20)
        self.m_listCtrl5.InsertColumn(2, gui_lib.msg.order_main_BillGet_text[1])
        self.m_listCtrl5.SetColumnWidth(2, self.width * 0.20)

        if i_get_bill is False:
            diallog = BillInfoGuage(self)
            diallog.ShowModal()

        if i_get_bill is False and self.user.grup.bill_disable is True:
            self.t = task.BlockBill(self.q)
            self.t.start()
        else:
            self.t = None
        self._mashin_list()
        self.m_listCtrl5.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnChange)
        self.Fit()

    def _mashin_list(self):
        self.mashinDict = {}
        index = 0
        self.bill_sum = 0
        for item in self.mashin:
            self.m_listCtrl5.InsertItem(index, str(item.nom_in_l))
            self.m_listCtrl5.SetItem(index, 1, str(item.model.name))
            if item.bill_get is True:
                self.m_listCtrl5.SetItemTextColour(item=index, col=wx.Colour(0, 135, 11))
            else:
                self.m_listCtrl5.SetItemTextColour(item=index, col=wx.Colour(199, 16, 29))

            if item.bill_mony == None:
                self.m_listCtrl5.SetItem(index, 2, gui_lib.msg.order_main_BillGet_text[4])
            else:
                self.m_listCtrl5.SetItem(index, 2, str(item.bill_mony))
                if item.bill_get is True:
                    self.bill_sum = self.bill_sum + item.bill_mony
                    self.m_staticText11.SetLabel(gui_lib.msg.order_main_BillGet_text[1] +':' + str(self.bill_sum))
            self.mashinDict[index] = item
            index += 1

    def mashin_list_refresh(self):
        self.m_listCtrl5.DeleteAllItems()
        self._mashin_list()

    def OnChange(self, event):
        currentItem = event.GetIndex()
        if self.mashinDict[currentItem].bill_get is True:
            self.mashinDict[currentItem].bill_get = False
            self.m_listCtrl5.SetItemTextColour(item=currentItem, col=wx.Colour(199, 16, 29))
            if self.mashinDict[currentItem].bill_mony == None:
                pass
            else:
                self.bill_sum = self.bill_sum - self.mashinDict[currentItem].bill_mony
            self.m_staticText11.SetLabel(gui_lib.msg.order_main_BillGet_text[1] + u': ' + str(self.bill_sum))
            if self.i_get_bill is False and self.user.grup.bill_disable is True:
                self.q.put([libs.smib.SAS_F_METER_SINGLE, self.mashinDict[currentItem].ip,
                              libs.smib.SAS_C_SINGLE_BILL_START])
                # libs.udp.send()
        else:
            self.mashinDict[currentItem].bill_get = True
            self.m_listCtrl5.SetItemTextColour(item=currentItem, col=wx.Colour(0, 135, 11))
            if self.mashinDict[currentItem].bill_mony == None:
                pass
            else:
                self.bill_sum = self.bill_sum + self.mashinDict[currentItem].bill_mony
            self.m_staticText11.SetLabel(gui_lib.msg.order_main_BillGet_text[1] + u': ' + str(self.bill_sum))
            if self.i_get_bill is False and self.user.grup.bill_disable is True:
                self.q.put([libs.smib.SAS_F_METER_SINGLE, self.mashinDict[currentItem].ip,
                              libs.smib.SAS_C_SINGLE_BILL_STOP])
                # libs.udp.send()

    def OnClose(self, event):
        if self.t:
            self.t.abort()
        self.Destroy()

    def user_get_bill(self):
        user_kasa = 0
        for item in self.mashin:
            libs.DB.expire(item)
            if item.bill_get is True:
                obj = libs.DB.make_obj(libs.models.BillTake)
                obj.user_id = self.user.id
                obj.mashin_id = item.id
                obj.mony = item.bill_in_device
                user_kasa = user_kasa + item.bill_in_device
                item.bill_in_device = 0
                libs.DB.add_object_to_session(obj)
                libs.DB.add_object_to_session(item)
        libs.DB.expire(self.user)
        self.user.kasa += user_kasa
        libs.DB.add_object_to_session(self.user)
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
            dial.ShowModal()
            libs.DB.rollback()
            return

    def OnGo(self, event):
        if self.i_get_bill is False:
            dialog = GetBillGuage(self)
            dialog.ShowModal()
            error = dialog.error
            if error != []:
                pass
            if not dialog.worker._want_abort:
                self.parent.panel_kasa_refresh()
                self.OnClose(event)
        else:
            self.user_get_bill()
            self.OnClose(event)

class BillEnableGuage(gui.GetCounter):
    def __init__(self, parent, user=None):
        gui.GetCounter.__init__(self, parent)
        self.width, self.height = wx.GetDisplaySize()
        self.m_gauge1.SetMinSize((self.width // 2, -1))
        self.parent = parent
        if user == None:
            user = self.parent.GetParent().USER
        self.user = user
        self.m_staticText15.SetLabel(gui_lib.msg.order_main_BillEnableGuage_text['m_staticText15'] + u': ')
        if self.user.flor_id != None:
            self.mashin = libs.DB.get_all_where(libs.models.Device, flor_id=self.user.flor_id, enable=True, sas=True,
                                                order='nom_in_l', descs=True)
        else:
            self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, sas=True, order='nom_in_l', descs=True)
        self.SetTitle(gui_lib.msg.order_main_BillEnableGuage_name)
        self.m_button1.SetLabel(gui_lib.msg.order_main_BillEnableGuage_button['m_button1'])
        self.m_gauge1.SetRange(len(self.mashin))
        # self.m_button1.Disable()
        self.loop = 0
        self.worker = task.BillStart(self, self.mashin, self.parent.GetParent().USER)
        task.EVT_BILL_GET(self, self.GetCount)

    def GetCount(self, event):
        if type(event.data) == int:
            self.loop = self.loop + 1
            self.m_staticText15.SetLabel(
                gui_lib.msg.order_main_BillEnableGuage_text['m_staticText15'] + u': ' + str(event.data) + u' ' +
                gui_lib.msg.order_main_BillEnableGuage_text['OK'])
            self.m_gauge1.SetValue(self.loop)
        elif type(event.data) == dict:
            self.loop = self.loop + 1
            self.m_staticText15.SetLabel(
                gui_lib.msg.order_main_BillEnableGuage_text['m_staticText15'] + u': ' + str(
                    event.data['ERROR']) + u' ' + gui_lib.msg.order_main_BillEnableGuage_text['error'])
            self.m_gauge1.SetValue(self.loop)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            # self.m_button1.Enable()

    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.worker:
            self.worker.abort()

    def OnClose(self, event):
        self.OnTaskStop(event)
        self.Destroy()


class UserEditOrderSelect(gui.UserEditOrderSelect):
    def __init__(self, parent):
        self.parent = parent
        self.user = None
        self.close = False
        gui.UserEditOrderSelect.__init__(self, self.parent)
        self._add_user_in_list()
        self.SetMinSize((350, 150))
        self.m_button14.SetLabel(gui_lib.msg.order_main_UserEditOrderSelect['m_button14'])
        self.m_button15.SetLabel(gui_lib.msg.order_main_UserEditOrderSelect['m_button15'])
        self.m_staticText18.SetLabel(gui_lib.msg.order_main_UserEditOrderSelect['m_staticText18'])
        self.SetTitle(gui_lib.msg.order_main_UserEditOrderSelect['name'])
        self.Fit()

    def _add_user_in_list(self):
        self.selected_list = ['']
        group = libs.DB.get_all_where(libs.models.UserGrup, default_use=True)
        for b in group:
            user = libs.DB.get_all_where(libs.models.User, enable=True, grup_id=b.id)
            for i in user:
                self.selected_list.append(i.name)
        self.m_choice1.SetItems(self.selected_list)
        self.m_choice1.SetSelection(0)

    def OnClose(self, event):
        self.close = True
        self.Destroy()

    def OnSelect(self, event):
        user = self.selected_list[self.m_choice1.GetSelection()]
        if user != '':
            self.user = libs.DB.get_one_where(libs.models.User, name=user)
            self.Destroy()

class UserHaveMony(gui.MexEdit):
    def __init__(self, parent):
        self.parent = parent
        self.close = True
        gui.MexEdit.__init__(self, self.parent)
        self.m_textCtrl5.Hide()
        self.m_staticText13.Hide()
        self.mony = 0
        self.SetTitle(gui_lib.msg.order_UserHaveMony['name'])
        self.m_staticText12.SetLabel(gui_lib.msg.order_UserHaveMony['m_staticText12'])
        self.m_button10.SetLabel(gui_lib.msg.order_UserHaveMony['m_button10'])
        self.m_button11.SetLabel(gui_lib.msg.order_UserHaveMony['m_button11'])
        self.m_textCtrl4.SetValue('0.00')
        self.Fit()
        self.Layout()

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        self.close = False
        mony = self.m_textCtrl4.GetValue()
        mony = mony.replace(',', '.')
        try:
            self.mony = float(mony)
            if self.mony < 0:
                self.close = False
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                dial.ShowModal()
        except:
            self.close = False
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
        self.OnClose(event)



class Order(gui.OrderPanel):
    def __init__(self, parent):
        gui.OrderPanel.__init__(self, parent)
        msg = libs.DB.get_one_where(libs.models.Config, name='admin_msg')
        self.old_user = None
        if msg == None:
            self.m_staticText16.SetLabel(u'')
        elif msg.value == None or msg.value == u'':
            libs.DB.get_one_where(libs.models.Config, name='admin_msg')
        else:
            self.m_staticText16.SetLabel(
                gui_lib.msg.order_main_Order_text[4] + u': ' + gui_lib.msg.order_main_Order_text['yes'])
        self.parent = parent
        self.parent.help_name = 'order.html'
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.order_main_Order_name[1])
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        libs.DB.expire()
        self.user = self.parent.USER
        if self.user.flor_id == None:
            self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, order='nom_in_l')
        else:
            self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, flor_id=self.user.flor_id,
                                                order='nom_in_l')

        self.m_listCtrl3.InsertColumn(0, gui_lib.msg.order_main_Order_text[6])

        self.m_listCtrl3.InsertColumn(1, gui_lib.msg.order_main_Order_text[7])

        self.m_listCtrl3.InsertColumn(2, gui_lib.msg.order_main_Order_text[8])

        self.m_listCtrl3.InsertColumn(3, gui_lib.msg.order_main_Order_text[9])

        self.m_listCtrl3.InsertColumn(4, gui_lib.msg.order_main_Order_text[10])

        self.m_listCtrl3.InsertColumn(5, gui_lib.msg.order_main_Order_text[11])

        self.m_listCtrl1.InsertColumn(0, gui_lib.msg.order_main_Order_text[12])

        self.m_listCtrl1.InsertColumn(1, gui_lib.msg.order_main_Order_text[14])

        self.m_listCtrl2.InsertColumn(0, gui_lib.msg.order_main_Order_text[13])

        self.m_listCtrl2.InsertColumn(1, gui_lib.msg.order_main_Order_text[14])
        self.m_staticText14.SetLabel(gui_lib.msg.order_main_Order_text[3] + u' ID ' + str(self.user.id) + u': ' + self.user.name)
        self.m_staticText1.SetLabel(gui_lib.msg.order_main_Order_text[1] + u': ' + str(self.user.kasa))


        if self.user.flor_id != None:
            self.m_staticText3.SetLabel(gui_lib.msg.order_main_Order_text[2] + u': ' + self.user.flor.name)
        else:
            self.m_staticText3.SetLabel(gui_lib.msg.order_main_Order_text[2] + u': ' + gui_lib.msg.order_main_Order_text[19])

        self.get_bill = False
        self.kasa_refresh()
        self._set_tools()
        # self._razhodi_list()
        # self._prihodi_list()
        # self._order_list()
        self.on_resize(None)
        self.order_error = []
        time_chk = libs.chk_time()
        if time_chk is not True:
            MyFrame = wx.MessageDialog(None, gui_lib.msg.bad_rtc_server+time_chk, gui_lib.msg.on_run_error,
                                       wx.OK | wx.ICON_ERROR)
            MyFrame.ShowModal()
            self.OnClose(None)
        self.user_start_work = self.chk_for_order_start(init=True)
        self.Fit()

    def commit(self):
        try:
            libs.DB.commit()
            return True
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()

    def send_mail(self, data, to_mail, subject):
        try:
            html = gui_lib.printer.render('mony_order.html', data)
            send_to = to_mail
            mail_to_send = send_to.split(',')
            for i in mail_to_send:
                libs.sendmail.Gmail(html, i, subject)
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)

    def OnShowMSG(self, event):
        dial = MSGAdd(self, edit=False)
        dial.ShowModal()

    def MakeMonyOrder( self, event ):
        libs.DB.expire()
        dial = Opis(self, self.user)
        dial.ShowModal()
        # self.commit()

    def LoadUser(self, event):
        libs.DB.expire()
        dial = UserEditOrderSelect(self)
        dial.ShowModal()
        if dial.close is False:
            if self.old_user == None:
                self.old_user = self.user
            self.user = dial.user
            self.m_staticText14.SetLabel(gui_lib.msg.order_main_Order_text[3] + u' ID ' + str(self.user.id) + u': ' + self.user.name)

            if self.user.flor_id == None:
                self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, order='nom_in_l')
            else:
                self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, flor_id=self.user.flor_id,
                                                    order='nom_in_l')
            if self.user.flor_id != None:
                self.m_staticText3.SetLabel(gui_lib.msg.order_main_Order_text[2] + u': ' + self.user.flor.name)
            else:
                self.m_staticText3.SetLabel(
                    gui_lib.msg.order_main_Order_text[2] + u': ' + gui_lib.msg.order_main_Order_text[19])
            self.chk_for_order_start(init=True)
        # self.razhodi_refresh()
        # self.prihodi_refresh()
        # self.order_refresh()
        self.kasa_refresh()
        self._set_tools()

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        self.m_listCtrl3.SetMinSize((self.width * 0.68, self.height * 0.50))
        self.m_listCtrl3.SetColumnWidth(0, self.width * 0.06)
        self.m_listCtrl3.SetColumnWidth(1, self.width * 0.14)
        self.m_listCtrl3.SetColumnWidth(2, self.width * 0.12)
        self.m_listCtrl3.SetColumnWidth(3, self.width * 0.12)
        self.m_listCtrl3.SetColumnWidth(4, self.width * 0.12)
        self.m_listCtrl3.SetColumnWidth(5, self.width * 0.12)
        self.m_toolBar1.SetMinSize((self.width, -1))
        self.m_listCtrl1.SetMinSize((self.width // 4, self.height * 0.28))
        self.m_listCtrl1.SetColumnWidth(0, self.width // 6)
        self.m_listCtrl1.SetColumnWidth(1, self.width // 4)
        self.m_listCtrl2.SetMinSize((self.width // 4, self.height * 0.28))
        self.m_listCtrl2.SetColumnWidth(0, self.width // 6)
        self.m_listCtrl2.SetColumnWidth(1, self.width // 4)
        self.m_listCtrl1.SetToolTip(gui_lib.msg.order_main_Order_tooltip['m_listCtrl1'])
        self.m_listCtrl2.SetToolTip(gui_lib.msg.order_main_Order_tooltip['m_listCtrl2'])
        self.m_listCtrl3.SetToolTip(gui_lib.msg.order_main_Order_tooltip['m_listCtrl3'])

        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height * 0.95))
        if event != None:
            event.Skip()
        self.Layout()

    def chk_if_no_order(self):
        ord_have = None
        for item in self.mashin:
            ord_have = libs.DB.get_one_where(libs.models.Order, user_id=self.user.id, chk=False, mashin_id=item.id)
            if ord_have == None:
                dial = wx.MessageDialog(self, *gui_lib.msg.NOT_ALL_MASHIN_IS_IN_ORDER)
                dial.ShowModal()
                break
        if ord_have == None:
            return False
        else:
            return True

    def _set_tools(self):
        self.m_toolBar1.ClearTools()
        if self.user.grup.right != None:
            right = self.user.grup.from_json()
            if 2 in right['order']:
                self.m_tool2 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.order_main_Order_button['m_tool2'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-Edit-Redo-64.png",
                                                                wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.order_main_Order_tooltip['m_tool2'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnPrihod, id=self.m_tool2.GetId())
            if 3 in right['order']:
                self.m_tool102 = self.m_toolBar1.AddTool(wx.ID_ANY,
                                                              gui_lib.msg.order_main_Order_button['m_tool102'],
                                                              wx.Bitmap(
                                                                  libs.conf.IMG_FOLDER + u"64x64/Gnome-Object-Flip-Horizontal-64.png",
                                                                  wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                              gui_lib.msg.order_main_Order_tooltip['m_tool102'],
                                                              wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnMonyTransfer, id=self.m_tool102.GetId())

            if 4 in right['order']:
                self.m_tool3 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.order_main_Order_button['m_tool3'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-Edit-Undo-64.png",
                                                                wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.order_main_Order_tooltip['m_tool3'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnRazhod, id=self.m_tool3.GetId())

            if 5 in right['order']:
                self.m_tool4 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.order_main_Order_button['m_tool4'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-List-Remove-64.png",
                                                                wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.order_main_Order_tooltip['m_tool4'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnLipsi, id=self.m_tool4.GetId())

            if 6 in right['order']:
                self.m_tool8 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.order_main_Order_button['m_tool8'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-Emblem-Downloads-64.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.order_main_Order_tooltip['m_tool8'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnGetCounter, id=self.m_tool8.GetId())

            if 7 in right['order']:
                self.m_tool101 = self.m_toolBar1.AddTool(wx.ID_ANY,
                                                              gui_lib.msg.order_main_Order_button['m_tool101'],
                                                              wx.Bitmap(
                                                                  libs.conf.IMG_FOLDER + u"64x64/Gnome-Preferences-Desktop-Keyboard-Shortcuts-64.png",
                                                                  wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                              gui_lib.msg.order_main_Order_tooltip['m_tool101'],
                                                              wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnHandWork, id=self.m_tool101.GetId())

            if 8 in right['order']:
                self.m_tool111 = self.m_toolBar1.AddTool(wx.ID_ANY,
                                                              gui_lib.msg.order_main_Order_button['m_tool111'],
                                                              wx.Bitmap(
                                                                  libs.conf.IMG_FOLDER + u"64x64/Gnome-Insert-Link-64.png",
                                                                  wx.BITMAP_TYPE_ANY),
                                                              wx.NullBitmap, wx.ITEM_NORMAL,
                                                              gui_lib.msg.order_main_Order_tooltip['m_tool111'],
                                                              wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnBillGet, id=self.m_tool111.GetId())

            if 9 in right['order']:
                self.m_tool10 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.order_main_Order_button['m_tool10'],
                                                             wx.Bitmap(
                                                                 libs.conf.IMG_FOLDER + u"64x64/Gnome-View-Refresh-64.png",
                                                                 wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                             wx.ITEM_NORMAL,
                                                             gui_lib.msg.order_main_Order_tooltip['m_tool10'],
                                                             wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnEndWork, id=self.m_tool10.GetId())

            if 1 in right['order']:
                self.m_tool6 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.order_main_Order_button['m_tool6'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-Printer-Printing-64.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL,
                                                            gui_lib.msg.order_main_Order_tooltip['m_tool6'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnPrint, id=self.m_tool6.GetId())
            # print right['order']
            # if 10 in right['order']:
            self.m_listCtrl3.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnEditOrder)
            if 14 in right['order']:
                self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnRazhodiEdit)
            if 13 in right['order']:
                self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnPrihodiEdit)
            if 15 in right['order']:
                self.m_staticText14.Bind(wx.EVT_LEFT_DCLICK, self.LoadUser)

        self.m_tool1 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.order_main_Order_button['m_tool1'],
                                                    wx.Bitmap(
                                                        libs.conf.IMG_FOLDER + u"64x64/dialog-error.png",
                                                        wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                    gui_lib.msg.order_main_Order_tooltip['m_tool1'], wx.EmptyString,
                                                    None)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_TOOL, self.OnClose, id=self.m_tool1.GetId())
        self.m_toolBar1.Realize()

    def _razhodi_list(self):
        self.razhod = libs.DB.get_all_where(libs.models.Razhod, user_id=self.user.id, chk=False)
        suma = 0
        self.m_listCtrl1.InsertItem(0, gui_lib.msg.order_main_Order_text[20])
        self.m_listCtrl1.InsertItem(1, '-' * 20)
        self.m_listCtrl1.SetItem(1, 1, '-' * 10)
        index = 2
        self.razhodListDict = {}
        for item in self.razhod:
            self.m_listCtrl1.InsertItem(index, item.reson.name)
            self.m_listCtrl1.SetItem(index, 1, "{:.2f}".format(item.mony))
            suma = suma + item.mony
            self.razhodListDict[index] = item
            index += 1
        atm = libs.DB.get_all_where(libs.models.BankTransfer, user_id=self.user.id, chk=False)
        atm_mony = 0
        for i in atm:
            atm_mony += i.mony
            suma = suma + i.mony
        self.m_listCtrl1.InsertItem(index, gui_lib.msg.cust_atm)
        self.m_listCtrl1.SetItem(index, 1, "{:.2f}".format(atm_mony))
        index += 1
        restricted = libs.DB.get_all_where(libs.models.BonusPay, user_id=self.user.id, chk=False, from_in=True)
        restricted_sum = 0
        for i in restricted:
            restricted_sum += i.mony
            suma = suma + i.mony
        restricted_cart = libs.DB.get_all_where(libs.models.BonusCartLog, user_id=self.user.id, chk=False)
        for i in restricted_cart:
            if i.cart.cart_type == 'restricted':
                restricted_sum += i.mony
                suma = suma + i.mony
        self.m_listCtrl1.InsertItem(index, gui_lib.msg.restricted_bonus)
        self.m_listCtrl1.SetItem(index, 1, "{:.2f}".format(restricted_sum))
        index += 1
        mony_back = libs.DB.get_all_where(libs.models.MonuBackPay, pub_user_id=self.user.id, chk=False)
        mony_back_mony = 0
        for i in mony_back:
            mony_back_mony += i.mony
            suma = suma + i.mony
        self.m_listCtrl1.InsertItem(index, gui_lib.msg.cust_MonyBack)
        self.m_listCtrl1.SetItem(index, 1, "{:.2f}".format(mony_back_mony))
        index += 1
        lipsi = libs.DB.get_all_where(libs.models.Lipsi, user_id=self.user.id, chk=False, if_lipsa=True)
        lipsi_sum = 0
        for i in lipsi:
            # if i.mony > 0:
            lipsi_sum += i.mony
            suma = suma + i.mony
        self.m_listCtrl1.InsertItem(index, gui_lib.msg.order_m_tool4)
        self.m_listCtrl1.SetItem(index, 1, "{:.2f}".format(lipsi_sum))
        index += 1
        mony_on_cart = libs.DB.get_all_where(libs.models.MonyOnCart, pub_user_id=self.user.id, chk=False, out=True)
        mony_on_cart_mony = 0
        for i in mony_on_cart:
            mony_on_cart_mony += i.mony
            suma = suma + i.mony
        self.m_listCtrl1.InsertItem(index, gui_lib.msg.cust_MonyOnCart_OUT)
        self.m_listCtrl1.SetItem(index, 1, "{:.2f}".format(mony_on_cart_mony))
        index += 1
        virtual_in = libs.DB.get_all_where(libs.models.CustInOutAFT, chk=False, user_id=self.user.id, out=False)
        virtual_in_mony = 0
        for i in virtual_in:
            virtual_in_mony += i.mony
            suma = suma + i.mony
        self.m_listCtrl1.InsertItem(index, gui_lib.msg.aft_in)
        self.m_listCtrl1.SetItem(index, 1, "{:.2f}".format(virtual_in_mony))
        index += 1
        transfer = libs.DB.get_all_where(libs.models.KasaTransfer, chk_to=False, from_user_id=self.user.id)
        transfer_mony = 0
        for i in transfer:
            transfer_mony += i.mony
        self.m_listCtrl1.InsertItem(index, gui_lib.msg.mony_transfer)
        self.m_listCtrl1.SetItem(index, 1, "{:.2f}".format(transfer_mony))
        suma += transfer_mony
        index += 1
        self.m_listCtrl1.SetItem(0, 1, "{:.2f}".format(suma))

    def OnMonyTransfer(self, event):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return
        dial = mony.main.MonyTransfer(self, self.user)
        dial.ShowModal()
        # self.commit()
        self.kasa_refresh()
        # self.razhodi_refresh()
        # self.prihodi_refresh()

    def razhodi_refresh(self):
        self.m_listCtrl1.DeleteAllItems()
        self._razhodi_list()

    def _prihodi_list(self):
        self.prihod = libs.DB.get_all_where(libs.models.Prihod, user_id=self.user.id, chk=False)
        suma = 0
        self.m_listCtrl2.InsertItem(0, gui_lib.msg.order_main_Order_text[20])
        self.m_listCtrl2.InsertItem(1, '-' * 20)
        self.m_listCtrl2.SetItem(1, 1, '-' * 10)
        index = 2
        self.prihodListDict = {}
        for item in self.prihod:
            self.m_listCtrl2.InsertItem(index, item.reson.name)
            self.m_listCtrl2.SetItem(index, 1, "{:.2f}".format(item.mony))
            suma = suma + item.mony
            self.prihodListDict[index] = item
            index += 1
        mony_on_cart = libs.DB.get_all_where(libs.models.MonyOnCart, pub_user_id=self.user.id, chk=False, out=False)
        mony_on_cart_mony = 0
        for i in mony_on_cart:
            mony_on_cart_mony += i.mony
            suma = suma + i.mony
        self.m_listCtrl2.InsertItem(index, gui_lib.msg.cust_MonyOnCart_IN)
        self.m_listCtrl2.SetItem(index, 1, "{:.2f}".format(mony_on_cart_mony))
        index += 1
        bonus_cart = libs.DB.get_all_where(libs.models.BonusCartLog, user_id=self.user.id, chk=False)
        bonus_cart_mony = 0
        for i in bonus_cart:
            if i.bonus_hold is False and i.cart.cart_type != 'restricted':
                bonus_cart_mony += i.mony
        self.m_listCtrl2.InsertItem(index, gui_lib.msg.bonus_cart)
        self.m_listCtrl2.SetItem(index, 1, "{:.2f}".format(bonus_cart_mony))
        index += 1
        if libs.DB.get_one_where(libs.models.Config, name='bonus_cart_hold').value == 'True':
            bonus_cart_hold_mony = 0
            for i in bonus_cart:
                if i.bonus_hold is True:
                    bonus_cart_hold_mony += i.bonus
            bonus_cart = libs.DB.get_all_where(libs.models.ClienBonusHold, user_id=self.user.id, chk=False)
            for i in bonus_cart:
                bonus_cart_hold_mony += i.bonus
                suma += i.mony
            self.m_listCtrl2.InsertItem(index, gui_lib.msg.bonus_cart_hold)
            self.m_listCtrl2.SetItem(index, 1, "{:.2f}".format(bonus_cart_hold_mony))
            index += 1
        virtual_in = libs.DB.get_all_where(libs.models.CustInOutAFT, chk=False, user_id=self.user.id, out=True)
        virtual_in_mony = 0
        for i in virtual_in:
            virtual_in_mony += i.mony
        self.m_listCtrl2.InsertItem(index, gui_lib.msg.aft_out)
        self.m_listCtrl2.SetItem(index, 1, "{:.2f}".format(virtual_in_mony))
        index += 1
        lipsi = libs.DB.get_all_where(libs.models.Lipsi, user_id=self.user.id, chk=False, if_lipsa=False)
        lipsi_sum = 0
        for i in lipsi:
            # if i.mony < 0:
            lipsi_sum += i.mony
                # suma += i.mony
        self.m_listCtrl2.InsertItem(index, gui_lib.msg.order_m_tool4)
        self.m_listCtrl2.SetItem(index, 1, "{:.2f}".format(lipsi_sum))
        index += 1
        transfer = libs.DB.get_all_where(libs.models.KasaTransfer, chk=False, to_user_id=self.user.id)
        transfer_mony = 0
        for i in transfer:
            transfer_mony += i.mony
        self.m_listCtrl2.InsertItem(index, gui_lib.msg.mony_transfer)
        self.m_listCtrl2.SetItem(index, 1, "{:.2f}".format(transfer_mony))
        index += 1
        suma = suma + lipsi_sum + virtual_in_mony + bonus_cart_mony + transfer_mony
        self.m_listCtrl2.SetItem(0, 1, "{:.2f}".format(suma))

    def prihodi_refresh(self):
        self.m_listCtrl2.DeleteAllItems()
        self._prihodi_list()

    def _order_list(self):
        suma_total = 0
        suma_in = 0
        suma_out = 0
        row = libs.DB.get_all_where(libs.models.Order, user_id=self.user.id, chk=False)
        index = 0
        self.mashinListDict = {}
        self.old_bill = 0
        self.suma_bill = 0
        for item in row:
            self.m_listCtrl3.InsertItem(index, str(item.mashin.nom_in_l))
            self.m_listCtrl3.SetItem(index, 1, str(item.mashin.model.name))
            ins = item.new_enter - item.old_enter
            ins = ins * item.mashin.el_coef
            suma_in = suma_in + ins
            self.m_listCtrl3.SetItem(index, 2, "{:.2f}".format(ins))
            out = item.new_exit - item.old_exit
            out = out * item.mashin.el_coef
            suma_out = suma_out + out
            self.m_listCtrl3.SetItem(index, 3, "{:.2f}".format(out))

            bill = item.bill_new - item.bill_old

            self.suma_bill = self.suma_bill + bill
            self.m_listCtrl3.SetItem(index, 4, str(bill))

            total = ins - out
            suma_total = suma_total + total
            self.m_listCtrl3.SetItem(index, 5, "{:.2f}".format(total))

            self.mashinListDict[index] = item
            index += 1

        self.m_listCtrl3.InsertItem(0, '')
        self.m_listCtrl3.SetItem(0, 1, gui_lib.msg.order_main_Order_text[20])
        self.m_listCtrl3.SetItem(0, 2, "{:.2f}".format(suma_in))
        self.m_listCtrl3.SetItem(0, 3, "{:.2f}".format(suma_out))
        self.suma_in = "{:.2f}".format(suma_in)
        self.suma_out = "{:.2f}".format(suma_out)
        self.m_listCtrl3.SetItem(0, 4, str(self.suma_bill))
        self.m_listCtrl3.SetItem(0, 5, "{:.2f}".format(suma_total))
        self.suma_total = "{:.2f}".format(suma_total)

        self.m_listCtrl3.InsertItem(1, '-' * 10)
        self.m_listCtrl3.SetItem(1, 1, '-' * 10)
        self.m_listCtrl3.SetItem(1, 2, '-' * 10)
        self.m_listCtrl3.SetItem(1, 3, '-' * 10)
        self.m_listCtrl3.SetItem(1, 4, '-' * 10)
        self.m_listCtrl3.SetItem(1, 5, '-' * 10)

    def order_refresh(self):
        self.m_listCtrl3.DeleteAllItems()
        self._order_list()

    def kasa_refresh(self):
        libs.DB.expire()
        self.parent.mashin_list_refresh()
        self.order_refresh()
        self.prihodi_refresh()
        self.razhodi_refresh()
        self.m_staticText1.SetLabel(gui_lib.msg.order_main_Order_text[1] + u': ' + "{:.2f}".format(self.user.kasa))

    def OnHandWork(self, event):
        if not self.chk_for_order_start():
            return
        libs.DB.expire()
        dialog = OrderByHand(self, self.order_error, user=self.user)
        dialog.ShowModal()
        # self.commit()
        self.kasa_refresh()

    def OnPrihod(self, event, edit=None):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return
        dialog = mony.main.MonyInOut(self, 'IN', edit, user=self.user)
        dialog.ShowModal()
        # self.commit()
        self.kasa_refresh()
        # self.prihodi_refresh()

    def OnRazhod(self, event, edit=None):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return
        # libs.DB.expire(self.user)
        dialog = mony.main.MonyInOut(self, 'OUT', edit, user=self.user)
        dialog.ShowModal()
        # self.commit()
        self.kasa_refresh()

    def OnLipsi(self, event):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return
        dialog = mony.main.InOutReson(self, 'LIPSI', user=self.user)
        dialog.ShowModal()
        # self.commit()
        self.kasa_refresh()

    def OnClose(self, event):
        if self.old_user != None:
            self.user = self.old_user
            self.old_user = None

            self.m_staticText14.SetLabel(gui_lib.msg.order_main_Order_text[3] + u': ' + self.user.name)
            self.kasa_refresh()
        self.parent.show_panel()
        self.parent.panel_kasa_refresh()
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.order_main_Order_name[2])
        self.parent.help_name = 'main.html'
        self.Destroy()

    def OnPrint(self, event, print_rko=True):
        if not self.chk_for_order_start():
            return
        if self.chk_if_no_order() is True:
            data = {}
            data['nom'] = libs.DB.get_next_doc_num(libs.models.MonyRKO, 'id')
            dates = libs.models.TZ.now()
            data['dates'] = libs.models.TZ.date_to_str(dates, '%d.%m.%Y %H:%M')
            start_dates = libs.DB.get_one_where(libs.models.StartWork, user_id=self.user.id, start=True)
            if start_dates == None:
                data['start_dates'] = None
            elif start_dates.pub_time == None:
                data['start_dates'] = None
            else:
                data['start_dates'] = libs.models.TZ.date_to_str(start_dates.pub_time, '%d.%m.%Y %H:%M:%S')

            if self.user.flor_id == None:
                data['region'] = gui_lib.msg.order_main_Order_text[19]
            else:
                data['region'] = self.user.flor.name
            data['user'] = self.user.name

            data['total'] = "{:.2f}".format(self.user.kasa)

            razhodi = []
            prihodi = []
            data['total_zala'] = self.suma_total
            prihodi_sum = 0
            razhodi_sum = 0
            atm = libs.DB.get_all_where(libs.models.BankTransfer, user_id=self.user.id, chk=False)
            atm_mony = 0
            for i in atm:
                atm_mony += i.mony
            restricted = libs.DB.get_all_where(libs.models.BonusPay, user_id=self.user.id, chk=False, from_in=True)
            restricted_sum = 0
            for i in restricted:
                restricted_sum += i.mony
                razhodi_sum += i.mony
            lipsi = libs.DB.get_all_where(libs.models.Lipsi, user_id=self.user.id, chk=False)
            lipsi_prihod = 0
            lipsi_razhod = 0
            for i in lipsi:
                if i.if_lipsa is True:
                    lipsi_razhod += i.mony
                else:
                    lipsi_prihod += i.mony
            # lipsi_razhod = lipsi_razhod*-1
            mony_back = libs.DB.get_all_where(libs.models.MonuBackPay, pub_user_id=self.user.id, chk=False)
            mony_back_mony = 0
            for i in mony_back:
                mony_back_mony += i.mony
                # suma = suma + i.mony
            mony_on_cart = libs.DB.get_all_where(libs.models.MonyOnCart, pub_user_id=self.user.id, chk=False, out=True)
            mony_on_cart_mony = 0
            for i in mony_on_cart:
                mony_on_cart_mony += i.mony

            virtual_in = libs.DB.get_all_where(libs.models.CustInOutAFT, chk=False, user_id=self.user.id, out=False)
            virtual_in_mony = 0
            for i in virtual_in:
                virtual_in_mony += i.mony

            virtual_out = libs.DB.get_all_where(libs.models.CustInOutAFT, chk=False, user_id=self.user.id, out=True)
            virtual_out_mony = 0
            for i in virtual_out:
                virtual_out_mony += i.mony
            my_prihod = {}
            for item in self.prihod:
                if item.reson.name not in my_prihod:
                    my_prihod[item.reson.name] = item.mony
                else:
                    my_prihod[item.reson.name] += item.mony
                prihodi_sum = prihodi_sum + item.mony
            for i in my_prihod:
                prihodi.append([i, my_prihod[i]])
            my_razhod = {}
            for item in self.razhod:
                if item.reson.name not in my_razhod:
                    my_razhod[item.reson.name] = item.mony
                else:
                    my_razhod[item.reson.name] += item.mony
                # razhodi.append([item.reson.name, item.mony])
                razhodi_sum = razhodi_sum + item.mony
            for i in my_razhod:
                razhodi.append([i, my_razhod[i]])

            transfer = libs.DB.get_all_where(libs.models.KasaTransfer, chk=False, to_user_id=self.user.id)
            transfer2 = libs.DB.get_all_where(libs.models.KasaTransfer, chk_to=False, from_user_id=self.user.id)
            transfer_razhod = 0
            transfer_prihod = 0
            for i in transfer:
                transfer_prihod += i.mony
            for i in transfer2:
                transfer_razhod += i.mony
            bonus_cart = libs.DB.get_all_where(libs.models.BonusCartLog, user_id=self.user.id, chk=False)
            for i in bonus_cart:
                if i.cart.cart_type == 'restricted':
                    restricted_sum += i.bonus
                    razhodi_sum = razhodi_sum + i.bonus
            razhodi.append([gui_lib.msg.cust_atm, round(float(atm_mony), 2)])
            razhodi.append([gui_lib.msg.restricted_bonus, round(float(restricted_sum),2)])
            razhodi.append([gui_lib.msg.cust_MonyBack, round(float(mony_back_mony), 2)])
            razhodi.append([gui_lib.msg.cust_MonyOnCart_OUT, round(float(mony_on_cart_mony),2)])
            razhodi.append([gui_lib.msg.aft_in, round(float(virtual_in_mony),2)])
            razhodi.append([gui_lib.msg.order_m_tool4, round(float(lipsi_razhod),2)])
            razhodi.append([gui_lib.msg.mony_transfer, round(float(transfer_razhod),2)])

            razhodi_sum += atm_mony + mony_back_mony + mony_on_cart_mony + virtual_in_mony + lipsi_razhod + transfer_razhod

            mony_on_cart = libs.DB.get_all_where(libs.models.MonyOnCart, pub_user_id=self.user.id, chk=False, out=False)
            mony_on_cart_mony_prihodi = 0
            for i in mony_on_cart:
                mony_on_cart_mony_prihodi += i.mony


            bonus_cart_mony = 0
            for i in bonus_cart:
                if i.bonus_hold is False and i.cart.cart_type != 'restricted':
                    bonus_cart_mony += i.mony
            if libs.DB.get_one_where(libs.models.Config, name='bonus_cart_hold').value == 'True':
                bonus_cart_hold_mony = 0
                for i in bonus_cart:
                    if i.bonus_hold is True and i.cart.cart_type != 'restricted':
                        bonus_cart_hold_mony += i.bonus
                cust_bonus_cart = libs.DB.get_all_where(libs.models.ClienBonusHold, user_id=self.user.id, chk=False)
                for i in cust_bonus_cart:
                    bonus_cart_hold_mony += i.bonus
                prihodi_sum += bonus_cart_hold_mony
                prihodi.append([gui_lib.msg.bonus_cart_hold, round(float(bonus_cart_hold_mony),2)])


            prihodi.append([gui_lib.msg.cust_MonyOnCart_IN, round(float(mony_on_cart_mony_prihodi),2)])
            prihodi.append([gui_lib.msg.bonus_cart, round(float(bonus_cart_mony),2)])
            prihodi.append([gui_lib.msg.aft_out, round(float(virtual_out_mony),2)])
            prihodi.append([gui_lib.msg.order_m_tool4, round(float(lipsi_prihod),2)])
            prihodi.append([gui_lib.msg.mony_transfer, round(float(transfer_prihod),2)])
            prihodi_sum += mony_on_cart_mony_prihodi + bonus_cart_mony + virtual_out_mony + lipsi_prihod + transfer_prihod

            prihodi_sum = prihodi_sum + round(float(self.suma_in),2)
            razhodi_sum = razhodi_sum + round(float(self.suma_out),2)
            data['razhodi_sum'] = "{:.2f}".format(razhodi_sum)
            data['prihodi_sum'] = "{:.2f}".format(prihodi_sum)
            data['prihodi'] = prihodi
            data['razhodi'] = razhodi
            data['ins'] = self.suma_in
            data['out'] = self.suma_out
            bill = libs.DB.get_all_where(libs.models.BillTake, user_id=self.user.id, chk=False)
            if bill == []:
                data['bill'] = 0
                data['bill_r'] = "{:.2f}".format(self.suma_bill)
            else:
                var = 0
                for i in bill:
                    var = var + i.mony
                data['bill'] = "{:.2f}".format(var - self.suma_bill)
                data['bill_r'] = "{:.2f}".format(var)

            data['len_row'] = max(len(prihodi), len(razhodi))
            rko = libs.DB.make_obj(libs.models.MonyRKO)
            rko.user_id = self.user.id
            rko.total = self.user.kasa
            rko.rko_data = json.dumps(data)
            libs.DB.add_object_to_session(rko)
            if event is None and self.user.grup.rko_auto_mail is True:
                t = threading.Thread(target=self.send_mail, args=(data, self.user.grup.boss_mail, self.user.grup.subject))
                t.start()
            if self.commit() is True:
                if print_rko is True:
                    gui_lib.printer.Print(self, 'mony_order.html', data)
                    if libs.conf.PRINT_DIRECT is True:
                        dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_OK)
                        dlg.ShowModal()

    def OnGetCounter(self, event):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return
        user_heve_mony = libs.DB.get_one_where(libs.models.Config, name='user_have_mony')
        if not user_heve_mony:
            obj = libs.DB.make_obj(libs.models.Config)
            obj.name = 'user_have_mony'
            obj.value = 'False'
            libs.DB.add_object_to_session(obj)
            try:
                libs.DB.commit()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
                dial.ShowModal()
                libs.DB.rollback()
                return
        elif user_heve_mony.value == 'False':
            pass
        else:
            dial = Opis(self, self.user)
            dial.ShowModal()
            if dial.close is True:
                return
            else:
                obj = libs.DB.make_obj(libs.models.UserHaveMony)
                obj.mony = dial.mony
                obj.user_id = self.user.id
                libs.DB.add_object_to_session(obj)
                try:
                    libs.DB.commit()
                except Exception as e:
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
                    dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                    dial.ShowModal()
                    libs.DB.rollback()
                    return
        cart = False
        if libs.conf.KS_JUMP is True and libs.conf.CHANGE_KS_ON_ORDER is True:
            dlg = wx.MessageBox(gui_lib.msg.order_main_Order_text[23], 'Info',
                                wx.YES_NO | wx.ICON_QUESTION)

            if dlg == wx.YES:
                dial = SelectUser(self, self.user)
                dial.ShowModal()
                cart = dial.close
                if cart is True:
                    return
        dialog = GetCounter(self, user=self.user, cart=cart)
        dialog.ShowModal()
        abort = dialog.worker._want_abort
        if abort:
            return
        error = dialog.error
        if error != []:
            text = (gui_lib.msg.order_main_Order_text[15] + '\n' + str(error) + '\n' +
                    gui_lib.msg.order_main_Order_text[16])
            dlg = wx.MessageDialog(self, text, gui_lib.msg.order_main_Order_text[17], wx.YES_NO | wx.ICON_WARNING)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                dialog = GetCounter(self, mashin_to_ord=error)
                dialog.ShowModal()
                abort_try_2 = dialog.worker._want_abort
                if not abort_try_2:
                    error = dialog.error
                else:
                    pass
        if error != []:
            for i in error:
                err = libs.DB.make_obj(libs.models.GetCounterError)
                err.user_id = self.user.id
                err.mashin_nom_in_l = i
                err.info = gui_lib.msg.order_main_Order_text[18]
                libs.DB.add_object_to_session(err)
            try:
                libs.DB.commit()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                dial.ShowModal()
                libs.DB.rollback()
                return
            self.order_error = error
            panel = OrderByHand(self, self.order_error)
            panel.ShowModal()
        self.commit()
        self.kasa_refresh()

    def OnEndWork(self, event):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return
        if self.chk_if_no_order() is True:
            if self.user.kasa > 0:
                dlg = wx.MessageBox(gui_lib.msg.order_main_Order_text[21], 'Info',
                                    wx.YES_NO | wx.ICON_QUESTION)

                if dlg == wx.YES:
                    if not self.chk_for_order_start():
                        return
                    dial = mony.main.MonyTransfer(self, self.user)
                    dial.ShowModal()
                    if dial.error is True:
                        return
        else:
            return
        self.OnPrint(None, False)

        if self.chk_if_no_order() is True:
            boss_get = libs.DB.make_obj(libs.models.BosGetMony)
            boss_get.user_id = self.user.id
            boss_get.mony = self.user.kasa
            boss_get.flor_id = self.user.flor_id
            libs.DB.add_object_to_session(boss_get)
            # old_kasa = self.user.kasa
            self.user.kasa = 0
            libs.DB.add_object_to_session(self.user)
            obj = libs.DB.get_all_where(libs.models.StartWork, user_id=self.user.id, start=True)
            for i in obj:
            # if obj != None:
                i.start = False
                i.end_time = libs.models.TZ.now()
                libs.DB.add_object_to_session(i)

            prihod = libs.DB.get_all_where(libs.models.Prihod, user_id=self.user.id, chk=False)
            razhod = libs.DB.get_all_where(libs.models.Razhod, user_id=self.user.id, chk=False)
            orders = libs.DB.get_all_where(libs.models.Order, user_id=self.user.id, chk=False)
            bill = libs.DB.get_all_where(libs.models.BillTake, user_id=self.user.id, chk=False)
            atm = libs.DB.get_all_where(libs.models.BankTransfer, user_id=self.user.id, chk=False)
            bonus_cart = libs.DB.get_all_where(libs.models.BonusCartLog, user_id=self.user.id, chk=False)
            cust_bonus_cart = libs.DB.get_all_where(libs.models.ClienBonusHold, user_id=self.user.id, chk=False)
            mony_back = libs.DB.get_all_where(libs.models.MonuBackPay, pub_user_id=self.user.id, chk=False)
            mony_on_cart = libs.DB.get_all_where(libs.models.MonyOnCart, pub_user_id=self.user.id, chk=False)
            virtual_in = libs.DB.get_all_where(libs.models.CustInOutAFT, chk=False, user_id=self.user.id)
            lipsi = libs.DB.get_all_where(libs.models.Lipsi, chk=False, user_id=self.user.id)
            transfer_to = libs.DB.get_all_where(libs.models.KasaTransfer, chk_to=False, from_user_id=self.user.id)
            transfer_from = libs.DB.get_all_where(libs.models.KasaTransfer, chk=False, to_user_id=self.user.id)
            restricted = libs.DB.get_all_where(libs.models.BonusPay, user_id=self.user.id, chk=False, from_in=True)
            for i in restricted:
                i.chk = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for i in transfer_to:
                i.chk_to = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for i in transfer_from:
                i.chk = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for i in lipsi:
                i.chk = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for i in cust_bonus_cart:
                i.chk = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return

            for i in virtual_in:
                i.chk = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for i in bonus_cart:
                i.chk = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for i in atm:
                i.chk = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for i in mony_back:
                i.chk = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for i in mony_on_cart:
                i.chk = True
                libs.DB.add_object_to_session(i)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for item in bill:
                item.chk = True
                libs.DB.add_object_to_session(item)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for item in orders:
                item.chk = True
                libs.DB.add_object_to_session(item)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for item in prihod:
                item.chk = True
                libs.DB.add_object_to_session(item)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            for item in razhod:
                item.chk = True
                libs.DB.add_object_to_session(item)
            try:
                libs.DB.flush()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                libs.DB.rollback()
                return
            # try:
            if self.user.grup.bill_disable is True:
                dialog = BillEnableGuage(self)
                dialog.ShowModal()
            if self.commit() is not True:
                return
            self.m_staticText1.SetLabel(gui_lib.msg.order_main_Order_text[1] + u': ' + str(self.user.kasa))
                # self.order_refresh()
                # self.razhodi_refresh()
                # self.prihodi_refresh()

            dial = wx.MessageDialog(self, *gui_lib.msg.WORK_OFF)
            dial.ShowModal()
            self.kasa_refresh()
            # self.parent.OnLogOut(event)
            # except Exception as e:
            #     print(e)
            #     libs.log.stderr_logger.critical(e, exc_info=True)
            #     dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            #     dial.ShowModal()
            #     libs.DB.rollback()

    def OnEditOrder(self, event):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return
        right = self.user.grup.from_json()
        order = self.m_listCtrl3.GetFirstSelected() - 2
        try:
            order = self.mashinListDict[order]
        except KeyError:
            return
        if 10 in right['order']:
            if order.mashin.sas is True:
                pass
            else:
                if 16 not in right['order']:
                    return
        else:
            if order.mashin.sas is True:
                return
            else:
                if 16 not in right['order']:
                    return

        dialog = NotSASCounter(self, mashins=order.mashin, edit=order, user=self.user)
        dialog.ShowModal()
        # self.commit()
        self.kasa_refresh()

    def OnPrihodiEdit(self, event):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return

        prihod = self.m_listCtrl2.GetFirstSelected()
        try:
            prihod = self.prihodListDict[prihod]
            if prihod.reson.name == u'Cust Cart':
                return
            self.OnPrihod(event, prihod)
        except KeyError:
            return



    def OnRazhodiEdit(self, event):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return

        razhod = self.m_listCtrl1.GetFirstSelected()
        try:
            razhod = self.razhodListDict[razhod]
            if razhod.reson.name == u'SAS Bonus Cart':
                pass
            elif razhod.reson.name == u'AFT Bonus':
                pass
            elif razhod.reson.name == gui_lib.msg.cust_MonyBack:
                pass
            elif razhod.reson.name == gui_lib.msg.cust_atm:
                pass
            else:
                self.OnRazhod(event, razhod)
        except KeyError:
            return

    def chk_for_order_start(self, init=True):
        if init is True:
            start_work = libs.DB.get_one_where(libs.models.StartWork, user_id=self.user.id, start=True)
            if start_work == None:
                self.user_start_work = False
                dial = wx.MessageDialog(self, *gui_lib.msg.WORK_NOT_START)
                dial.ShowModal()
                return False
            else:
                self.user_start_work = True
                return True
        else:
            if self.user_start_work is False:
                dial = wx.MessageDialog(self, *gui_lib.msg.WORK_NOT_START)
                dial.ShowModal()
            return self.user_start_work

    def OnBillGet(self, event):
        libs.DB.expire()
        if not self.chk_for_order_start():
            return
        if self.chk_if_no_order() is True:

            frame = BillGet(self.parent, True, user=self.user)
            frame.ShowModal()
            # self.commit()
            self.kasa_refresh()


class MSGAdd(gui.BugReport, gui_lib.keybords.Keyboard):
    def __init__(self, parent, edit=False):
        self.parent = parent
        gui.BugReport.__init__(self, parent)
        if edit is False:
            self.m_textCtrl7.SetEditable(False)
            self.m_button30.Hide()
        self.SetTitle(gui_lib.msg.main_MSGAdd_name)
        self.m_staticText17.SetLabel(gui_lib.msg.main_MSGAdd_text['Text17'])
        self.m_button29.SetLabel(gui_lib.msg.main_MSGAdd_button['button29'])
        self.m_button30.SetLabel(gui_lib.msg.main_MSGAdd_button['button30'])
        self.m_textCtrl7.SetToolTip(gui_lib.msg.main_MSGAdd_tolltip['Ctrl7'])
        self.msg = libs.DB.get_one_where(libs.models.Config, name='admin_msg')
        if self.msg != None:
            if self.msg.value != None:
                self.m_textCtrl7.SetValue(self.msg.value)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl7.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        msg = self.m_textCtrl7.GetValue()
        if self.msg == None:
            self.msg = libs.DB.make_obj(libs.models.Config)
            self.msg.name = 'admin_msg'
        self.msg.value = msg
        libs.DB.add_object_to_session(self.msg)
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
            dial.ShowModal()
            libs.DB.rollback()
            return
        self.OnClose(event)

class Opis(gui.Opis, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user):
        self.user = user
        gui.Opis.__init__(self, parent)
        self.SetTitle(gui_lib.msg.order_mony_opis['title'])
        self.m_button16.SetLabel(gui_lib.msg.order_mony_opis['m_button16'])
        self.m_button17.SetLabel(gui_lib.msg.order_mony_opis['m_button17'])
        self.m_staticText51.SetLabel(gui_lib.msg.order_mony_opis['m_staticText51'] + ':')
        self.close = True
        self.mony = 0
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl1.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl11.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl12.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl13.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl14.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl15.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl16.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl17.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl18.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl19.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl110.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl111.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl112.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
        self.Fit()

    def onEnter(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_NUMPAD_RIGHT or keycode == wx.WXK_TAB or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_RIGHT or keycode == wx.WXK_RETURN:
            event.EventObject.Navigate()
        elif keycode == wx.WXK_LEFT or keycode == wx.WXK_NUMPAD_LEFT:
            event.EventObject.Navigate(wx.NavigationKeyEvent.IsBackward)
        else:
            event.Skip()

    def calc_all(self, event):
        total = 0
        total += self.m_spinCtrl1.GetValue() * 100
        total += self.m_spinCtrl11.GetValue() * 50
        total += self.m_spinCtrl12.GetValue() * 20
        total += self.m_spinCtrl13.GetValue() * 10
        total += self.m_spinCtrl14.GetValue() * 5
        total += self.m_spinCtrl15.GetValue() * 2
        total += self.m_spinCtrl16.GetValue() * 1
        total += self.m_spinCtrl17.GetValue() * 0.5
        total += self.m_spinCtrl18.GetValue() * 0.2
        total += self.m_spinCtrl19.GetValue() * 0.1
        total += self.m_spinCtrl110.GetValue() * 0.05
        total += self.m_spinCtrl111.GetValue() * 0.02
        total += self.m_spinCtrl112.GetValue() * 0.01
        self.m_staticText52.SetLabel("{:.2f}".format(total))
        self.Fit()

    def c100( self, event ):
        total = self.m_spinCtrl1.GetValue() * 100
        self.m_staticText22.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c50( self, event ):
        total = self.m_spinCtrl11.GetValue() * 50
        self.m_staticText221.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c20( self, event ):
        total = self.m_spinCtrl12.GetValue() * 20
        self.m_staticText222.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c10( self, event ):
        total = self.m_spinCtrl13.GetValue() * 10
        self.m_staticText223.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c5( self, event ):
        total = self.m_spinCtrl14.GetValue() * 5
        self.m_staticText224.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c2( self, event ):
        total = self.m_spinCtrl15.GetValue() * 2
        self.m_staticText225.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c1( self, event ):
        total = self.m_spinCtrl16.GetValue() * 1
        self.m_staticText226.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c50st(self, event):
        total = self.m_spinCtrl17.GetValue() * 0.5
        self.m_staticText227.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c20st(self, event):
        total = self.m_spinCtrl18.GetValue() * 0.2
        self.m_staticText228.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c10st(self, event):
        total = self.m_spinCtrl19.GetValue() * 0.1
        self.m_staticText229.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c05st(self, event):
        total = self.m_spinCtrl110.GetValue() * 0.05
        self.m_staticText2210.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c02st(self, event):
        total = self.m_spinCtrl111.GetValue() * 0.02
        self.m_staticText2211.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def c01st(self, event):
        total = self.m_spinCtrl112.GetValue() * 0.01
        self.m_staticText2212.SetLabel("{:.2f}".format(total))
        self.calc_all(event)

    def OnClose(self, event):
        self.Destroy()

    def OnGo( self, event ):
        opis = {
            100:self.m_spinCtrl1.GetValue(),
            50:self.m_spinCtrl11.GetValue(),
            20:self.m_spinCtrl12.GetValue(),
            10:self.m_spinCtrl13.GetValue(),
            5:self.m_spinCtrl14.GetValue(),
            2:self.m_spinCtrl15.GetValue(),
            1:self.m_spinCtrl16.GetValue(),
            0.5:self.m_spinCtrl17.GetValue(),
            0.2:self.m_spinCtrl18.GetValue(),
            0.1:self.m_spinCtrl19.GetValue(),
            0.05:self.m_spinCtrl110.GetValue(),
            0.02:self.m_spinCtrl111.GetValue(),
            0.01:self.m_spinCtrl112.GetValue()
        }
        total = 0
        for i in opis:
            total += opis[i]*i
        opis = json.dumps(opis)
        obj = libs.DB.make_obj(libs.models.MonyOrder)
        obj.user_id = self.user.id
        obj.data = opis
        obj.total = total
        libs.DB.add_object_to_session(obj)
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
            dial.ShowModal()
            libs.DB.rollback()
            return
        self.close = False
        self.mony = float(self.m_staticText52.GetLabel())
        self.OnClose(event)

class SelectUser(gui.SelectUser):
    def __init__(self, parent, user):
        self.close = True
        self.user = user
        self.parent = parent
        gui.SelectUser.__init__(self, parent)
        self.SetTitle(gui_lib.msg.odrer_SelectUser['title'])
        self.m_staticText36.SetLabel(gui_lib.msg.odrer_SelectUser['m_staticText36'])
        self.m_button18.SetLabel(gui_lib.msg.odrer_SelectUser['m_button18'])
        self.m_button19.SetLabel(gui_lib.msg.odrer_SelectUser['m_button19'])
        self.set_all_user()
        self.Fit()

    def set_all_user(self):
        self.all_user = libs.DB.get_all_where(libs.models.User, enable=True, order='name')
        my_user_list = ['']
        for i in range(len(self.all_user)):
            if self.all_user[i].name == self.user.name:
                pass
            else:
                my_user_list.append(self.all_user[i].name)
        self.m_choice2.SetItems(my_user_list)

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):

        self.to_user = self.m_choice2.GetString(self.m_choice2.GetSelection())
        self.to_user = libs.DB.get_one_where(libs.models.User, name=self.to_user)
        if self.to_user == None:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return
        if self.to_user.cart is None:
            dial = wx.MessageDialog(self, *gui_lib.msg.USER_NOT_HAVE_CART)
            dial.ShowModal()
            return
        self.close = self.to_user.cart
        self.Destroy()
