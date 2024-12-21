#-*- coding:utf-8 -*-
'''
Created on 2.11.2017 г.

@author: dedal
'''

import wx
import libs
import gui_lib
from . import gui
import os
import random
import users.task
import datetime
from . import task
import datetime
import json
import importlib

class SetMonyOnUser(gui.SetMonyOnUser, gui_lib.keybords.Keyboard):
    def __init__(self, parent, cust, user):
        gui.SetMonyOnUser.__init__(self, parent)
        self.SetTitle(gui_lib.msg.cust_main_SetMonyOnUser_name)
        self.m_staticText75.SetLabel(gui_lib.msg.cust_main_SetMonyOnUser_text['m_staticText75'] + ': ' + cust.name)
        self.m_button21.SetLabel(gui_lib.msg.cust_main_SetMonyOnUser_button['m_button21'])
        self.m_button20.SetLabel(gui_lib.msg.cust_main_SetMonyOnUser_button['m_button20'])
        self.cust = cust
        self.parent = parent
        self.user = user
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl19.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        libs.DB.expire()
        self.cust = libs.DB.get_one_where(libs.models.CustUser, id=self.cust.id)
        self.cust.curent_mony += self.m_spinCtrl19.GetValue()
        self.user.kasa += self.m_spinCtrl19.GetValue()
        libs.DB.add_object_to_session(self.cust)
        libs.DB.add_object_to_session(self.user)
        obj = libs.DB.make_obj(libs.models.MonyOnCart)
        obj.cust_id = self.cust.id
        obj.pub_user_id = self.user.id
        obj.mony = self.m_spinCtrl19.GetValue()
        obj.out = False
        libs.DB.add_object_to_session(obj)
        try:
            libs.DB.commit()
            self.Destroy()
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()


    def add_1( self, event ):
        self.m_spinCtrl19.SetValue(self.m_spinCtrl19.GetValue()+1)

    def add_10( self, event ):
        self.m_spinCtrl19.SetValue(self.m_spinCtrl19.GetValue() + 10)

    def add_100( self, event ):
        self.m_spinCtrl19.SetValue(self.m_spinCtrl19.GetValue() + 100)

    def del_last( self, event ):
        self.m_spinCtrl19.SetValue(0)

class SetMonyOnUserCart(gui.AddCart):
    def __init__(self, parent, my_user):
        self.parent = parent
        self.my_user = my_user
        gui.AddCart.__init__(self, parent)
        self.SetTitle(gui_lib.msg.cust_main_SetMonyOnUserCart_name)
        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_text[1])
        # self.parent_worker = self.parent.GetParent().rfid_task()
        self.m_button8.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_button['m_button8'])
        self.m_button7.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_button['m_button7'])
        self.m_button8.Disable()
        self.cust = None
        self.cart = None
        self.set = False
        # if self.parent.GetParent().login.worker == None:
        if self.parent.GetParent().login.worker:
            self.parent.GetParent().rfid_bind(self)
        else:
            self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)
            users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)
        # self.SetMinSize((640, 200))
        self.Fit()
        # else:
        #     self.parent.GetParent().rfid_task_stop(None)
        #     self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)  # @UndefinedVariable
        #     users.task.EVT_WORK_RFID_RESULT(self, self.OnAddCard)

    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.parent.GetParent().login.worker:
            self.parent.GetParent().rfid_unbind()
            return
        try:
            self.worker.abort()
        except AttributeError:
            pass

    def OnCard(self, event):
        if event.data == None or event.data is False:
            pass
        elif event.data == 'ERROR':
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_RFID)
            dial.ShowModal()
            self.OnTaskStop(None)
        # elif event.data == self.my_user.cart:
        #     pass
        elif self.cust != None:
            pass
        else:
                self.cart = libs.DB.get_one_where(libs.models.CustCart, catr_id=event.data)
                if self.cart == None:
                    self.m_staticText13.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_text[2])
                    # self.OnTaskStop(event)
                    # return
                else:
                    # libs.DB.expire()
                    self.cust = libs.DB.get_one_where(libs.models.CustUser, id=self.cart.user.id)
                    if self.cust == None:
                        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_text[3])
                    elif self.cust.forbiden is True:
                        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_text[5])
                    else:
                        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_text[4] + u':\n' + str(self.cust.name))
                        self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
                        self.m_button8.Enable()
                self.OnTaskStop(None)
                self.Fit()

    def OnAddNew(self, event):
        dial = SetMonyOnUser(self, user=self.my_user, cust=self.cust)
        dial.ShowModal()
        self.OnTaskStop(event)
        self.Destroy()

    def OnClose(self, event):
        self.OnTaskStop(event)
        # if self.parent.GetParent().login.with_rfid_in is True:
        #     self.parent.GetParent().rfid_task_start(event)
        self.Destroy()

class ReadOCR(gui.AddCart):
    def __init__(self, parent):
        self.parent = parent
        gui.AddCart.__init__(self, parent)
        self.SetTitle(gui_lib.msg.OCR_READ['name'])
        self.m_staticText13.SetLabel(gui_lib.msg.OCR_READ[1])
        self.m_button8.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_button['m_button8'])
        self.m_button7.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_button['m_button7'])
        self.data = False
        self.SetMinSize((640, 200))
        self.Fit()
        self.worker = task.ORCDataGet(self, self.parent)
        task.EVT_ORC_GET(self, self.OnCard)


    def OnTaskStop(self, event):
        self.worker.abort()

    def OnCard(self, event):
        self.data = event.data
        if self.data != False:
            if self.data[0] == 'DISABLE':
                self.OnTaskStop(event)
                self.m_staticText13.SetLabel(gui_lib.msg.OCR_READ[3])
                self.m_staticText13.SetForegroundColour(wx.Colour(27, 0, 125))
                # self.data = self.data[0]
            elif self.data[0] == 'ERROR':
                self.OnTaskStop(event)
                self.m_staticText13.SetLabel(gui_lib.msg.OCR_READ[2])
                self.m_staticText13.SetForegroundColour(wx.Colour(27, 0, 125))
                # self.data = self.data[1]
            elif self.data[0] == 'LITLE':
                self.OnTaskStop(event)
                self.m_staticText13.SetLabel(gui_lib.msg.EGN_NO_YEARS[0])
                self.m_staticText13.SetForegroundColour(wx.Colour(27, 0, 125))
                # self.data = self.data[0]
            elif self.data[0]  == 'CANT_PLAY':
                self.OnTaskStop(event)
                self.m_staticText13.SetLabel(gui_lib.msg.CANT_PLAY)
                self.m_staticText13.SetForegroundColour(wx.Colour(27, 0, 125))
                # self.data = self.data[0]
                # dial = wx.MessageDialog(self, *gui_lib.msg.CANT_PLAY)
                # dial.ShowModal()
            elif self.data[0] == 'EXPIRED':
                self.OnTaskStop(event)
                self.m_staticText13.SetLabel(gui_lib.msg.CART_EXPIRED[0])
                self.m_staticText13.SetForegroundColour(wx.Colour(27, 0, 125))
            else:
                self.OnTaskStop(event)
                # self.data = self.data[1]
                self.m_staticText13.SetLabel(gui_lib.msg.OCR_READ[2])
                self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))


    def OnClose( self, event ):
        self.OnTaskStop(event)
        self.data = False
        self.Destroy()

    def OnAddNew(self, event):
        self.OnTaskStop(event)
        self.Destroy()

class PayMony(gui.AddCart):
    def __init__(self, parent, my_user):
        self.parent = parent
        self.my_user = my_user
        gui.AddCart.__init__(self, parent)
        self.SetTitle(gui_lib.msg.cust_main_PayMony_name)
        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_PayMony_text[1])
        # self.parent_worker = self.parent.GetParent().rfid_task()
        self.m_button8.SetLabel(gui_lib.msg.cust_main_PayMony_button['m_button8'])
        self.m_button7.SetLabel(gui_lib.msg.cust_main_PayMony_button['m_button7'])
        self.m_button8.Disable()
        # self.parent_worker = self.parent.GetParent().rfid_task()
        # self.m_button8.SetLabel(u'Изплати')
        self.cust = None
        self.cart = None

        if  self.parent.GetParent().login.worker:
            self.parent.GetParent().rfid_bind(self)
        else:
            self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)  # @UndefinedVariable
            users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)
        # else:
        #     self.parent.GetParent().rfid_task_stop(None)
        #     self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)  # @UndefinedVariable
        #     users.task.EVT_WORK_RFID_RESULT(self, self.OnAddCard)
        
    def OnTaskStop(self, event):
        """Stop Computation."""
        if  self.parent.GetParent().login.worker:
            self.parent.GetParent().rfid_unbind()
            return
        try:
            self.worker.abort()
        except AttributeError:
            pass
     
    def OnCard(self, event):
        if event.data == None or event.data is False:
            pass
        elif event.data == 'ERROR':
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_RFID)
            dial.ShowModal()
            self.OnTaskStop(None)
        # elif event.data == self.my_user.cart:
        #     pass
        elif self.cust != None:
            pass
        else:
            self.cart = libs.DB.get_one_where(libs.models.CustCart, catr_id=event.data)
            if self.cart == None:
                self.m_staticText13.SetLabel(gui_lib.msg.cust_main_SetMonyOnUserCart_text[2])
            else:
                # libs.DB.expire()
                self.cust = libs.DB.get_one_where(libs.models.CustUser, id=self.cart.user.id)
                if self.cust == None:
                    self.m_staticText13.SetLabel(gui_lib.msg.cust_main_PayMony_text[3])
                elif self.cust.forbiden is True:
                    self.m_staticText13.SetLabel(gui_lib.msg.cust_main_PayMony_text[8])
                else:
                    self.m_staticText13.SetLabel(gui_lib.msg.cust_main_PayMony_text[4] +
                                                     str(self.cust.name) + '\n' +
                                                     gui_lib.msg.cust_main_PayMony_text[6] + u': ' +
                                                     "{:.2f}".format(self.cust.curent_mony))
                    self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
                    self.m_button8.Enable()
            self.OnTaskStop(None)
            self.Fit()


    def PrintRKO(self, data):
        template = 'rko.html'
        data['my_copy'] = False
        html = gui_lib.printer.render(template, data)
        if os.name == 'posix':
            tmp_folder = '/tmp/'
        else:
            tmp_folder = r'C:/Users/Public/'
        gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp1.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
        if libs.conf.PRINT_DIRECT_POS is True:
            gui_lib.printer.PDFPrint(tmp_folder + 'tmp1.pdf', default=libs.conf.DEFAULT_POS_PRINTER, pos=True)
        else:
            cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp1.pdf'
            os.system(cmd)
             
    def OnAddNew(self, event):
        libs.DB.expire()
        if libs.conf.POS_PRINTER_USE is True:
            dlg = wx.MessageBox(gui_lib.msg.cust_main_PayMony_text[7], 'Info',
                                wx.YES_NO | wx.ICON_QUESTION)

            if dlg == wx.YES:
                if libs.conf.PRINT_DIRECT_POS is True and libs.conf.DEFAULT_POS_PRINTER == '':
                    dial = wx.MessageDialog(self, *gui_lib.msg.NO_POS_PRINTER)
                    dial.ShowModal()
                    return
                casino = libs.DB.get_one_where(libs.models.Config, name='pos_printer_info')
                if casino == None:
                    objects = gui_lib.msg.cust_main_TaloniPrint_text[9]
                    sity = gui_lib.msg.cust_main_TaloniPrint_text[9]
                    objects_adress = gui_lib.msg.cust_main_TaloniPrint_text[9]
                else:
                    casino = json.loads(casino.value)
                    objects = casino['object']
                    sity = casino['sity']
                    objects_adress = casino['adress']
                object_info = libs.DB.get_one_where(libs.models.Config, name='object_info')
                object_info = json.loads(object_info.value)
                EIK = object_info['EIK']
                company = object_info['company']
                mony = "{:.2f}".format(self.cust.curent_mony)
                egn = self.cust.personal_egn
                cust_name = self.cust.name
                user_id = str(self.my_user.id)
                dates = libs.models.TZ.date_to_str(formats='%d.%m.%Y %H:%M:%S')
                id = libs.DB.get_one(libs.models.CashOutPrinted, order='id', descs=True)
                if id == None:
                    ID = 1
                else:
                    ID = id.id + 1
                ID = str(ID)
                ID = ('0'*(9 - len(ID)) ) + ID
                rko = libs.DB.make_obj(libs.models.CashOutPrinted)
                rko.mony = float("{:.2f}".format(self.cust.curent_mony))
                rko.cust_id = self.cust.id
                rko.pub_user_id = self.my_user.id
                libs.DB.add_object_to_session(rko)
                # cust_sity = self.cust.persona_sity.name
                if self.cust.persona_sity_id:
                    cust_sity = self.cust.persona_sity.name
                else:
                    cust_sity = ''
                cust_adress = self.cust.personal_addres
                data = {'company':company, 'EIK':EIK, 'objects':objects, 'sity':sity, 'objects_adress':objects_adress,
                        'name':cust_name, 'egn':egn, 'mony':[mony], 'user_id':user_id, 'ID':[ID], 'dates':dates, 'cust_sity':cust_sity,
                        'cust_adress':cust_adress, 'count':1}
                self.PrintRKO(data)


        self.my_user.kasa -= float("{:.2f}".format(self.cust.curent_mony))
        libs.DB.add_object_to_session(self.my_user)
        obj = libs.DB.make_obj(libs.models.MonyOnCart)
        obj.cust_id = self.cust.id
        obj.pub_user_id = self.my_user.id
        obj.mony = float("{:.2f}".format(self.cust.curent_mony))
        obj.out = True
        libs.DB.add_object_to_session(obj)
        self.cust.curent_mony = 0
        libs.DB.add_object_to_session(self.cust)
        try:
            libs.DB.commit()
            for i in range(3):
                try:
                    data = None
                    data = libs.udp.send('del_get_mony', player_id=self.my_user.id)
                except:
                    libs.log.stderr_logger.warning('redirect not response: del_get_mony')
                if not data:
                    libs.log.stderr_logger.warning('redirect not response: del_get_mony')
                else:
                    break
            self.OnClose(event)
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()

    def OnClose(self, event):
        self.OnTaskStop(event)
        # if self.parent.GetParent().login.with_rfid_in is True:
        #     self.parent.GetParent().rfid_task_start(event)
        self.Destroy()

        
class TaloniPrint(gui.AddCart):
    def __init__(self, parent, my_user, cust=None):
        self.parent = parent
        self.my_user = my_user
        gui.AddCart.__init__(self, parent)
        self.SetTitle(gui_lib.msg.cust_main_TaloniPrint_name)
        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_TaloniPrint_text[1])
        self.m_button8.Hide()
        # self.parent_worker = self.parent.GetParent().rfid_task()
        self.m_button8.SetLabel(gui_lib.msg.cust_main_TaloniPrint_button['m_button8'])
        self.m_button7.SetLabel(gui_lib.msg.cust_main_TaloniPrint_button['m_button7'])
        self.user = cust
        self.no_cart = False
        self.cart = None
        if self.user == None:
            if self.parent.GetParent().login.worker:
                self.parent.GetParent().rfid_bind(self)
            else:
                self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)  # @UndefinedVariable
                users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)
            # else:
            #     self.parent.GetParent().rfid_task_stop(None)
            #     self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)  # @UndefinedVariable
            #     users.task.EVT_WORK_RFID_RESULT(self, self.OnAddCard)
        else:
            self.set_cust()

    def set_cust(self):
        if self.user.forbiden is True:
            return
        if int(self.user.total_tombula) > 0:
            self.m_button8.Show()
            self.m_staticText13.SetLabel(
                gui_lib.msg.cust_main_TaloniPrint_text[4] + str(self.user.name) + '\n' +
                str(int(self.user.total_tombula)))
            self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
            self.no_cart = True
        else:
            self.m_staticText13.SetLabel(gui_lib.msg.cust_main_TaloniPrint_text[5])
        self.SetMinSize((640, 200))
        
    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.parent.GetParent().login.worker:
            self.parent.GetParent().rfid_unbind()
        try:
            self.worker.abort()
        except AttributeError:
            pass
    
    def OnCard(self, event):
        if event.data == None or event.data is False:
            pass
        elif event.data == 'ERROR':
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_RFID)
            dial.ShowModal()
            self.OnTaskStop(None)
        # elif event.data == self.my_user.cart:
        #     pass
        elif self.user != None:
            pass
        else:
            self.cart = libs.DB.get_one_where(libs.models.CustCart, catr_id=event.data)
            if self.cart == None:
                self.m_staticText13.SetLabel(gui_lib.msg.cust_main_TaloniPrint_text[2])
                    # return
            else:
                self.user = libs.DB.get_one_where(libs.models.CustUser, id=self.cart.user_id)
                if self.user == None:
                    self.m_staticText13.SetLabel(gui_lib.msg.cust_main_TaloniPrint_text[3])
                    # return
                else:
                    if self.user.forbiden is True:
                        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_TaloniPrint_text[10])
                    elif int(self.user.total_tombula) > 0:
                        self.m_button8.Show()
                        self.m_staticText13.SetLabel(
                            gui_lib.msg.cust_main_TaloniPrint_text[4] +u':' + str(self.user.name) + '\n' +
                            str(int(self.user.total_tombula)))
                        self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
                        # return
                    else:
                        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_TaloniPrint_text[5])
                self.OnTaskStop(None)
                self.Fit()
            
    def OnAddNew(self, event):
        try:
            if libs.conf.POS_PRINTER_USE is False:
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_POS_PRINTER)
                dial.ShowModal()
                return
            if libs.conf.PRINT_DIRECT_POS is True and libs.conf.DEFAULT_POS_PRINTER == '' and libs.conf.PRINT_ON_SERVER_POS is False:
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_POS_PRINTER)
                dial.ShowModal()
                return
            if int(self.user.total_tombula) < 1:
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_MONY)
                dial.ShowModal()
                self.OnClose(event)
                return
            libs.DB.expire()
            if self.user.tombola_on_in is True:
                last_day_order = libs.DB.get_one_where(libs.models.DayReport, day_report=True, descs=True, order='id')
                if last_day_order == None:
                    start_time = '2010-01-01'
                else:
                    start_time = libs.models.TZ.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
                obj = libs.DB.get_one_where(libs.models.TombulaPrinted, cust_id=self.user.id, pub_time__gte=start_time)
                if obj:
                    dial = wx.MessageDialog(self, *gui_lib.msg.NO_POS_PRINTER)
                    dial.ShowModal()
                    return
                # start_time = libs.models.TZ.date_to_str(last_day_order.pub_time

            if self.user.bonus_in_mony is False:
                obj = libs.DB.make_obj(libs.models.TombulaPrinted)
                obj.tombula_count = int(self.user.total_tombula)
                obj.cust_id = self.user.id
                obj.pub_user_id = self.my_user.id
                self.user.total_tombula = round(self.user.total_tombula - obj.tombula_count, 2)
                libs.DB.add_object_to_session(obj)
    #             libs.DB.add_object_to_session(self.my_user)
                libs.DB.add_object_to_session(self.user)

                if obj.tombula_count >= 1 :
                    template = 'pos_print_tombula.html'
                    if self.no_cart is True:
                        err_obj = libs.DB.make_obj(libs.models.GetCounterError)
                        err_obj.user_id = self.my_user.id
                        err_obj.info = u'Talon print no cart: cust %s, count %s' % (
                        self.user.name, str(obj.tombula_count))
                        libs.DB.add_object_to_session(err_obj)
                    libs.DB.commit()
                    dates = libs.models.TZ.now()
                    dates = libs.models.TZ.date_to_str(dates)
                    casino = libs.DB.get_one_where(libs.models.Config, name='pos_printer_info')
                    if casino == None:
                        object = gui_lib.msg.cust_main_TaloniPrint_text[9]
                        sity = gui_lib.msg.cust_main_TaloniPrint_text[9]
                        adress = gui_lib.msg.cust_main_TaloniPrint_text[9]
                    else:
                        casino = json.loads(casino.value)
                        object = casino['object']
                        sity = casino['sity']
                        adress = casino['adress']
                    name = self.user.name
                    for i in range(2, 10):
                        name = name.replace(' ' * i, '')
                    br_index = 0
                    for i in name:
                        if i == ' ':
                            br_index += 1
                    name = name.replace(' ', '<br>')
                    if br_index == 1:
                        name += '<br>&nbsp;'
                    elif br_index == 0:
                        name += '<br>&nbsp;<br>&nbsp;'
                    elif br_index == 3:
                        name = name[0:-4]
                    data = {'count': obj.tombula_count, 'sity':sity, 'copy':False, 'object':object, 'adress':adress, 'name':name, 'dates':dates, 'ID':obj.id, 'len':len(self.user.name)}
                    html = gui_lib.printer.render(template, data)
                    if os.name == 'posix':
                        tmp_folder = '/tmp/'
                    else:
                        tmp_folder = r'C:/Users/Public/'
                    gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp2.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
                    if libs.conf.PRINT_DIRECT_POS is True:
                        gui_lib.printer.PDFPrint(tmp_folder + 'tmp2.pdf', default=libs.conf.DEFAULT_POS_PRINTER, pos=True)
                    else:
                        cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp2.pdf'
                        os.system(cmd)
                    # gui_lib.printer.PDFPrint(tmp_folder + 'tmp.pdf', default=libs.conf.DEFAULT_POS_PRINTER)
                    # dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_OK)
                    # dlg.ShowModal()
                    dlg = wx.MessageDialog(self, gui_lib.msg.cust_main_TaloniPrint_text[7], gui_lib.msg.cust_main_TaloniPrint_text[8], wx.YES_NO | wx.ICON_WARNING)
                    result = dlg.ShowModal()
                    if result == wx.ID_YES:
                        data = {'count': obj.tombula_count, 'sity': sity, 'copy': True, 'object': object, 'adress': adress,
                                'name': name, 'dates': dates, 'ID': obj.id, 'len': len(self.user.name)}
                        html = gui_lib.printer.render(template, data)
                        if os.name == 'posix':
                            tmp_folder = '/tmp/'
                        else:
                            tmp_folder = r'C:/Users/Public/'
                        gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp2.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
                        if libs.conf.PRINT_DIRECT_POS is True:
                            gui_lib.printer.PDFPrint(tmp_folder + 'tmp2.pdf', default=libs.conf.DEFAULT_POS_PRINTER, pos=True)
                        else:
                            cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp2.pdf'
                            os.system(cmd)
                    libs.DB.commit()
                else:
                    libs.DB.rollback()
                    dial = wx.MessageDialog(self, *gui_lib.msg.NO_MONY)
                    dial.ShowModal()
                self.OnClose(event)
                return
            else:
                obj = libs.DB.make_obj(libs.models.PointInMonyPrinted)
                obj.point_sum = float(round(int(self.user.total_tombula)*self.user.bonus_in_mony_sum, 2))
                obj.cust_id = self.user.id
                obj.pub_user_id = self.my_user.id
                self.user.total_tombula = round(self.user.total_tombula - int(self.user.total_tombula), 2)
                libs.DB.add_object_to_session(obj)
                #             libs.DB.add_object_to_session(self.my_user)
                libs.DB.add_object_to_session(self.user)

                if obj.point_sum > 0:
                    template = 'poin_in_mony.html'
                    if self.no_cart is True:
                        err_obj = libs.DB.make_obj(libs.models.GetCounterError)
                        err_obj.user_id = self.my_user.id
                        err_obj.info = u'Talon print no cart: cust %s, count %s' % (
                            self.user.name, str(obj.point_sum))
                        libs.DB.add_object_to_session(err_obj)
                    libs.DB.commit()
                    dates = libs.models.TZ.now()
                    dates = libs.models.TZ.date_to_str(dates, '%d.%m%Y %H:%M:%S')
                    casino = libs.DB.get_one_where(libs.models.Config, name='pos_printer_info')
                    if casino == None:
                        object = gui_lib.msg.cust_main_TaloniPrint_text[9]
                        sity = gui_lib.msg.cust_main_TaloniPrint_text[9]
                        adress = gui_lib.msg.cust_main_TaloniPrint_text[9]
                    else:
                        casino = json.loads(casino.value)
                        object = casino['object']
                        sity = casino['sity']
                        adress = casino['adress']
                    name = self.user.name
                    for i in range(2, 10):
                        name = name.replace(' ' * i, '')
                    br_index = 0
                    for i in name:
                        if i == ' ':
                            br_index += 1
                    name = name.replace(' ', '<br>')
                    if br_index == 1:
                        name += '<br>&nbsp;'
                    elif br_index == 0:
                        name += '<br>&nbsp;<br>&nbsp;'
                    elif br_index == 3:
                        name = name[0:-4]
                    id = libs.DB.get_one(libs.models.PointInMonyPrinted, order='id', descs=True)
                    if id == None:
                        ID = 1
                    else:
                        ID = id.id + 1
                    ID = str(ID)
                    ID = ('0' * (9 - len(ID))) + ID
                    cust_adress = self.user.personal_addres
                    # cust_sity = self.user.persona_sity.name
                    if self.user.persona_sity_id:
                        cust_sity = self.user.persona_sity.name
                    else:
                        cust_sity = ''
                    dlg = wx.MessageDialog(self, gui_lib.msg.cust_main_TaloniPrint_text[7],
                                           gui_lib.msg.cust_main_TaloniPrint_text[8], wx.YES_NO | wx.ICON_WARNING)
                    result = dlg.ShowModal()
                    if result == wx.ID_YES:
                        data = {'count': "{:.2f}".format(obj.point_sum), 'sity': sity, 'copy': True, 'objects': object,
                                'adress': adress,
                                'name': name, 'dates': dates, 'ID': ID, 'len': len(self.user.name), 'user_id':self.my_user.id, 'cust_adress':cust_adress,
                                'cust_sity':cust_sity, 'original':True}
                    else:
                        data = {'count': "{:.2f}".format(obj.point_sum), 'sity': sity, 'copy': False,
                                'objects': object,
                                'adress': adress,
                                'name': name, 'dates': dates, 'ID': ID, 'len': len(self.user.name), 'user_id':self.my_user.id, 'cust_adress':cust_adress,
                                'cust_sity':cust_sity, 'original':True}
                    html = gui_lib.printer.render(template, data)
                    if os.name == 'posix':
                        tmp_folder = '/tmp/'
                    else:
                        tmp_folder = r'C:/Users/Public/'
                    gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp3.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
                    if libs.conf.PRINT_DIRECT_POS is True:
                        gui_lib.printer.PDFPrint(tmp_folder + 'tmp3.pdf', default=libs.conf.DEFAULT_POS_PRINTER,
                                                 pos=True)
                    else:
                        cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp3.pdf'
                        os.system(cmd)
                    libs.DB.commit()
                    # if libs.DB.get_one_where(libs.models.Config, name='block_cust_if_print_tombula') == 'True':
                    #     data = libs.udp.send('user_block', cust_id=self.user.id)
                else:
                    libs.DB.rollback()
                    dial = wx.MessageDialog(self, *gui_lib.msg.NO_MONY)
                    dial.ShowModal()
                self.OnClose(event)
                return
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            
        
    def OnClose(self, event):
        self.OnTaskStop(event)
        self.Destroy()
        
class MonyBackPay(gui.AddCart):

    def __init__(self, parent, my_user, cust=None):
        self.parent = parent
        self.my_user = my_user
        gui.AddCart.__init__(self, parent)
        self.SetTitle(gui_lib.msg.cust_main_MonyBackPay_name)
        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_MonyBackPay_text[1])
        # self.parent_worker = self.parent.GetParent().rfid_task()
        self.m_button8.SetLabel(gui_lib.msg.cust_main_MonyBackPay_button['m_button8'])
        self.m_button7.SetLabel(gui_lib.msg.cust_main_MonyBackPay_button['m_button7'])
        self.no_cart = False
        self.user = cust
        self.cart = None
        self.m_button8.Hide()
        # self.parent_worker = self.parent.GetParent().rfid_task()
        if self.user == None:
            if self.parent.GetParent().login.worker:
                self.parent.GetParent().rfid_bind(self)
            else:
                self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)
                users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)
        else:
            if self.user.forbiden is True:
                return
            else:
                self.user_set()
        # self.SetTitle(_(u'Изплащане на мънибек'))
        # self.m_staticText13.SetLabel(_(u'Моля поставете карта в четеца!'))
        self.Fit()

    def user_set(self):
        if self.user.forbiden is True:
            self.m_staticText13.SetLabel(gui_lib.msg.cust_main_MonyBackPay_text[8])
        elif int(self.user.total_mony_back) < self.user.mony_back_pay:
            self.m_staticText13.SetLabel(
                gui_lib.msg.cust_main_MonyBackPay_text[7] + '\n' +
                gui_lib.msg.cust_main_MonyBackPay_text[4] + u': ' + str(self.user.name) + '\n' +
                gui_lib.msg.cust_main_MonyBackPay_text[6] + u': ' + str(int(self.user.total_mony_back)))

        else:
            # self.m_staticText13.SetLabel(_(u'Потребител: %s\nМънибек: %s')%(self.user.name, int(self.user.total_mony_back)))
            # if self.user.total_mony_back > self.user.mony_back_min_pay and self.user.mony_back_min_pay > 0:
            #     self.user.total_mony_back = self.user.mony_back_min_pay
            self.m_staticText13.SetLabel(
                gui_lib.msg.cust_main_MonyBackPay_text[4] + u': ' + str(self.user.name) + '\n' +
                gui_lib.msg.cust_main_MonyBackPay_text[6] + u': ' + str(int(self.user.total_mony_back)))
            self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
            self.no_cart = True
            self.m_button8.Show()
        self.SetMinSize((830, 230))
        self.Fit()
        self.Layout()

    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.parent.GetParent().login.worker:
            self.parent.GetParent().rfid_unbind()
            return
        try:
            self.worker.abort()
        except AttributeError:
            pass
        # if self.parent.GetParent().login.with_rfid_in is True:
        #     self.parent.GetParent().rfid_task_start(None)

    def PrintRKO(self, data):
        template = 'rko.html'
        data['my_copy'] = False
        html = gui_lib.printer.render(template, data)
        if os.name == 'posix':
            tmp_folder = '/tmp/'
        else:
            tmp_folder = r'C:/Users/Public/'
        gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp1.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
        if libs.conf.PRINT_DIRECT_POS is True:
            gui_lib.printer.PDFPrint(tmp_folder + 'tmp1.pdf', default=libs.conf.DEFAULT_POS_PRINTER, pos=True)
        else:
            cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp1.pdf'
            os.system(cmd)

    def OnCard(self, event):
        if event.data == None or event.data is False:
            pass
        elif event.data == 'ERROR':
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_RFID)
            dial.ShowModal()
            self.OnTaskStop(None)
        # elif event.data == self.my_user.cart:
        #     pass
        elif self.user != None:
            pass
        else:
            self.cart = libs.DB.get_one_where(libs.models.CustCart, catr_id=event.data)
            if self.cart == None:
                self.m_staticText13.SetLabel(gui_lib.msg.cust_main_MonyBackPay_text[2])
            elif self.cart is False:
                self.m_staticText13.SetLabel(gui_lib.msg.cust_main_MonyBackPay_text[2])
            else:
                self.user = libs.DB.get_one_where(libs.models.CustUser, id=self.cart.user_id)
                if self.user == None:
                    self.m_staticText13.SetLabel(gui_lib.msg.cust_main_MonyBackPay_text[3])
                else:
                    if self.user.mony_back_pay == None:
                        self.user.mony_back_pay = 0

                    if self.user.forbiden is True:
                        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_MonyBackPay_text[8])
                    elif int(self.user.total_mony_back) < self.user.mony_back_pay:
                        self.m_staticText13.SetLabel(
                            gui_lib.msg.cust_main_MonyBackPay_text[7] + '\n' +
                            gui_lib.msg.cust_main_MonyBackPay_text[4] + u': ' + str(self.user.name) + '\n' +
                            gui_lib.msg.cust_main_MonyBackPay_text[6] + u': ' + str(int(self.user.total_mony_back)))
                        self.SetMinSize((540, 200))

                    else:
                        # self.m_staticText13.SetLabel(_(u'Потребител: %s\nМънибек: %s')%(self.user.name, int(self.user.total_mony_back)))
                        self.m_staticText13.SetLabel(
                            gui_lib.msg.cust_main_MonyBackPay_text[4] + u': ' + str(self.user.name) + '\n' +
                            gui_lib.msg.cust_main_MonyBackPay_text[6] + u': ' + str(int(self.user.total_mony_back)))
                        self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
                        self.m_button8.Show()
                        self.SetMinSize((540, 200))
                    self.OnTaskStop(None)
                self.Fit()
            
    def OnAddNew(self, event):
        try:
            libs.DB.expire()
            self.my_user.kasa -= int(self.user.total_mony_back)
            obj = libs.DB.make_obj(libs.models.MonuBackPay)
            obj.mony = int(self.user.total_mony_back)
            obj.cust_id = self.user.id
            obj.pub_user_id = self.my_user.id
            self.user.total_mony_back = round(self.user.total_mony_back-int(self.user.total_mony_back),2)
            libs.DB.add_object_to_session(obj)
            libs.DB.add_object_to_session(self.my_user)
            libs.DB.add_object_to_session(self.user)
            if self.no_cart is True:
                objn = libs.DB.make_obj(libs.models.GetCounterError)
                objn.user_id = self.my_user.id
                objn.info = u'MonyBack pay no cart: cust %s, mony %s' % (self.user.name ,str(obj.mony))
                libs.DB.add_object_to_session(objn)
            if libs.conf.POS_PRINTER_USE is True and libs.conf.DEFAULT_POS_PRINTER != '' and libs.conf.MONYBACK_ON_POS is True:
                casino = libs.DB.get_one_where(libs.models.Config, name='pos_printer_info')
                if casino == None:
                    objects = gui_lib.msg.cust_main_TaloniPrint_text[9]
                    sity = gui_lib.msg.cust_main_TaloniPrint_text[9]
                    objects_adress = gui_lib.msg.cust_main_TaloniPrint_text[9]
                else:
                    casino = json.loads(casino.value)
                    objects = casino['object']
                    sity = casino['sity']
                    objects_adress = casino['adress']
                object_info = libs.DB.get_one_where(libs.models.Config, name='object_info')
                object_info = json.loads(object_info.value)
                EIK = object_info['EIK']
                company = object_info['company']
                mony = "{:.2f}".format(obj.mony)
                egn = self.user.personal_egn
                cust_name = self.user.name
                user_id = str(self.my_user.id)
                dates = libs.models.TZ.date_to_str(formats='%d.%m.%Y %H:%M:%S')
                id = libs.DB.get_one(libs.models.CashOutPrinted, order='id', descs=True)
                if id == None:
                    ID = 1
                else:
                    ID = id.id + 1
                ID = str(ID)
                ID = ('0' * (9 - len(ID))) + ID
                rko = libs.DB.make_obj(libs.models.CashOutPrinted)
                rko.mony = obj.mony
                rko.cust_id = self.user.id
                rko.pub_user_id = self.my_user.id
                libs.DB.add_object_to_session(rko)

                # cust_sity = self.user.persona_sity.name
                if self.user.persona_sity_id:
                    cust_sity = self.user.persona_sity.name
                else:
                    cust_sity = ''
                cust_adress = self.user.personal_addres
                data = {'company': company, 'EIK': EIK, 'objects': objects, 'sity': sity,
                        'objects_adress': objects_adress,
                        'name': cust_name, 'egn': egn, 'mony': [mony], 'user_id': user_id, 'ID': [ID], 'dates': dates,
                        'cust_sity': cust_sity,
                        'cust_adress': cust_adress, 'count': 1, 'reson': gui_lib.msg.cust_main_MonyBackPay_text[6]}

            libs.DB.commit()
            if libs.conf.POS_PRINTER_USE is True and libs.conf.DEFAULT_POS_PRINTER != '' and libs.conf.MONYBACK_ON_POS is True:
                self.PrintRKO(data)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_OK)
            dial.ShowModal()
            self.OnClose(event)
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            
        
    def OnClose(self, event):
        self.OnTaskStop(event)
        self.Destroy()
        
    
class AddCart(gui.AddCart):
    def __init__(self, parent, dell=False):
        self.parent = parent
        self.dell = dell
        gui.AddCart.__init__(self, parent)
        self.SetTitle(gui_lib.msg.cust_main_AddCart_name)
        self.m_staticText13.SetLabel(gui_lib.msg.cust_main_AddCart_text[1])
        # self.parent_worker = self.parent.GetParent().rfid_task()
        self.m_button8.SetLabel(gui_lib.msg.cust_main_AddCart_button['m_button8'])
        self.m_button7.SetLabel(gui_lib.msg.cust_main_AddCart_button['m_button7'])
        # try:
        #     self.parent_worker = self.parent.GetParent().GetParent().rfid_task()
        # except AttributeError:
        #     self.parent_worker = self.parent.GetParent().rfid_task()
        self.cart = None
        self.data = None
        self.close = True
        # if  self.parent.GetParent().GetParent().login.with_rfid_in== False:
        try:
            if not self.parent.GetParent().GetParent().login.worker:
                self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)
                users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)
            else:
                users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)
                self.parent.GetParent().GetParent().rfid_bind(self)
        except AttributeError:
            if not self.parent.GetParent().login.worker:
                self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)
                users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)
            else:
                users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)
                self.parent.GetParent().rfid_bind(self)
        except Exception as e:
            libs.log.stderr_logger.error(e, exc_info=True)
        # else:
        #     self.parent.GetParent().GetParent().rfid_task_stop(None)
        #     self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)  # @UndefinedVariable
        #     users.task.EVT_WORK_RFID_RESULT(self, self.OnAddCard)
        
    def OnTaskStop(self, event):
        """Stop Computation."""

        try:
            if self.parent.GetParent().GetParent().login.worker:
                self.parent.GetParent().GetParent().rfid_unbind()
                return
            else:
                try:
                    self.worker.abort()
                except AttributeError:
                    pass
        except AttributeError:
            if self.parent.GetParent().login.worker:
                self.parent.GetParent().rfid_unbind()
                return
            else:
                try:
                    self.worker.abort()
                except AttributeError:
                    pass

    def OnCard(self, event):
        # print self.cart, event.data
        if event.data == None or event.data is False:
            pass
        # elif self.cart != event.data and self.cart != None:
        #     self.cart = None
        elif event.data == 'ERROR':
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_RFID)
            dial.ShowModal()
            self.OnTaskStop(None)
        elif self.cart != None and self.dell is True:
            pass
        elif self.cart != None and self.dell is False:
            pass
        # elif event.data == self.parent.user.cart:
        #     pass
        # raise IndexError, (event.data, self.parent.user.cart)
        else:
            # data = event.data
            self.cart = event.data
            # if self.cart == self.parent.user.cart:
            #     pass
            # if data == None:
            #     data = libs.DB.get_one_where(libs.models.User, cart=self.cart)
            # if self.data == None:
            self.data = libs.DB.get_one_where(libs.models.CustCart, catr_id=self.cart)
            if self.dell is False:
                # self.data = True
                # if data == None:
                self.m_staticText13.SetLabel(gui_lib.msg.cust_main_AddCart_text[2])
                self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
                # self.OnTaskStop(event)
            elif self.dell is True:
                # if data == None:
                self.m_staticText13.SetLabel(gui_lib.msg.cust_main_AddCart_text[2])
                self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
        self.Fit()

            
    def OnAddNew(self, event):
        self.close = False
        self.OnClose(event)
         
    def OnClose(self, event):
#         if del_cart is True:
#             self.cart = None
#         if  self.parent.GetParent().GetParent().login.with_rfid_in is False:
        # if  self.parent.GetParent().GetParent().login.worker == None:
        self.OnTaskStop(event)

        # else:
        #     self.OnTaskStop(event)
        #     self.parent.GetParent().GetParent().rfid_task_start(event)
        self.Destroy()

# class AllCart(gui.AllCart):
#     def __init__(self, parent, cust = None):
#         gui.AllCart.__init__(self, parent)
#         self.parent = parent
#         self.cust = cust
#         self.all_cart = []
#         if self.cust != None:
#             cart_id = libs.DB.get_all_where(libs.models.CustCart, user_id=self.edit.id)
#         self._add_cart()
#         
#     def _add_cart(self):
#         
#         if self.cust != None:
#             pass
#         else:
#             pass
#             
#     def OnGo(self, event):
#         self.OnClose(event)
#     
#     def OnClose(self, event):
#         self.Destroy()
#     
#     def OnDel(self, event):
#         gui.AllCart.OnDel(self, event)
#         
#     def OnAdd(self, event):
#         dial = AddCart(self)
#         dial.ShowModal()
#         self._add_cart()
class AllUserEditByGroup(gui.AllUserEditByGroup):
    def __init__(self, parent, all_user, group):
        gui.AllUserEditByGroup.__init__(self, parent)
        self.parent = parent
        self.SetTitle(gui_lib.msg.cust_main_AllUserEditByGroup_name)
        self.m_button14.SetLabel(gui_lib.msg.cust_main_AllUserEditByGroup_button['m_button14'])
        self.all_user = all_user
        self.group = group
        self.m_gauge1.SetRange(len(self.all_user))
        self.loop = 0
        # self.m_button14.Disable()
        self.worker = task.UpdateUser(self, all_user, group)
        task.EVT_UPDATE_USER_GET(self, self.GetUserUpdate)
        self.error = 'ERROR'
        
    def GetUserUpdate(self, event):
        if type(event.data) == int:
            self.SetTitle(gui_lib.msg.cust_main_AllUserEditByGroup_name +': ID-' + str(event.data))
            self.loop = self.loop + 1
            self.m_gauge1.SetValue(self.loop)
#             self.error = event.data
        else:
            if event.data == 'DONE':
                self.error = event.data
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
            elif event.data == 'ERROR':
                self.error = event.data
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                # self.m_button14.Enable()
            
    def OnClose(self, event):
        if self.worker.is_alive():
            self.worker.abort()
        self.Destroy()
        
class AddGrup(gui.AddGrup, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user, edit=None):
        self.parent = parent
        gui.AddGrup.__init__(self, parent)
        self.edit = edit
        self.user = user
        self.SetTitle(gui_lib.msg.cust_main_AddGrup_name)
        self.m_checkBox55.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_checkBox55'])
        self.m_checkBox46.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_checkBox46'])
        self.m_checkBox51.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_checkBox51'])
        self.m_checkBox49.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_checkBox49'])
        self.m_staticText90.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_staticText90'])
        self.m_staticText2.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_staticText2'])
        self.m_checkBox40.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_checkBox40'])
        self.m_checkBox42.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_checkBox42'])
        self.m_staticText3.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_staticText3'])
        self.m_staticText77.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_staticText77'])
        self.m_staticText71.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_staticText71'])
        self.m_staticText39.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_staticText39'])
        self.m_staticText78.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_staticText78'])
        self.m_staticText5.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_staticText5'])
        self.m_listCtrl5.InsertColumn(0, gui_lib.msg.cust_main_AddGrup_text['mony'])
        self.m_listCtrl5.InsertColumn(1, gui_lib.msg.cust_main_AddGrup_text['count'])
        # self.m_staticText33.SetLabel(gui_lib.msg.cust_main_AddGrup_text['count'])
        # self.m_staticText34.SetLabel(gui_lib.msg.cust_main_AddGrup_text['mony'])
        # self.m_staticText35.SetLabel(gui_lib.msg.cust_main_AddGrup_text['count'])
        # self.m_staticText36.SetLabel(gui_lib.msg.cust_main_AddGrup_text['mony'])
        # self.m_staticText37.SetLabel(gui_lib.msg.cust_main_AddGrup_text['count'])
        # self.m_staticText38.SetLabel(gui_lib.msg.cust_main_AddGrup_text['mony'])
        # self.m_staticText331.SetLabel(gui_lib.msg.cust_main_AddGrup_text['count'])
        # self.m_staticText341.SetLabel(gui_lib.msg.cust_main_AddGrup_text['mony'])
        self.m_checkBox47.SetLabel(gui_lib.msg.cust_main_AddGrup_text['m_checkBox47'])

        self.m_checkBox59.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox59'])
        self.m_checkBox53.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox53'])
        self.m_radioBtn2.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_radioBtn2'])
        self.m_radioBtn1.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_radioBtn1'])
        self.m_radioBtn12.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_radioBtn12'])
        self.m_checkBox31.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox31'])
        self.m_checkBox8.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox8'])
        self.m_checkBox9.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox9'])
        self.m_checkBox12.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox12'])
        self.m_checkBox20.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox20'])
        self.m_checkBox18.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox18'])
        self.m_checkBox19.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox19'])
        self.m_checkBox21.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox21'])
        self.m_checkBox24.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox24'])
        self.m_checkBox25.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox25'])
        self.m_checkBox26.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox26'])
        self.m_checkBox27.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox27'])
        self.m_checkBox1.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox1'])
        self.m_checkBox2.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox2'])
        self.m_checkBox3.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_checkBox3'])
        self.m_radioBtn9.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_radioBtn9'])
        self.m_radioBtn10.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_radioBtn10'])
        self.m_button4.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_button4'])
        self.m_button5.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_button5'])

        self.m_spinCtrl21.SetToolTip(gui_lib.msg.cust_main_AddGrup_tooltip['m_spinCtrl21'])
        self.m_checkBox42.SetToolTip(gui_lib.msg.cust_main_AddGrup_tooltip['m_checkBox42'])
        self.m_checkBox1.SetToolTip(gui_lib.msg.cust_main_AddGrup_tooltip['m_checkBox1'])
        self.m_checkBox2.SetToolTip(gui_lib.msg.cust_main_AddGrup_tooltip['m_checkBox2'])
        self.m_checkBox3.SetToolTip(gui_lib.msg.cust_main_AddGrup_tooltip['m_checkBox3'])
        self.m_textCtrl5.SetToolTip(gui_lib.msg.cust_main_AddGrup_tooltip['m_textCtrl5'])
        self.m_spinCtrl22.SetToolTip(gui_lib.msg.cust_main_AddGrup_tooltip['m_spinCtrl22'])
        self.m_spinCtrl39.SetToolTip(gui_lib.msg.cust_main_AddGrup_tooltip['m_spinCtrl39'])
        if self.edit:
            # self.m_checkBox59.SetValue(self.edit.x2)
            try:
                self.bonus_row = json.loads(self.edit.bonus_row)
            except ValueError:
                self.bonus_row = {}
                self.edit.bonus_row = json.dumps({})
                libs.DB.add_object_to_session(self.edit)
                libs.DB.commit()

        else:
            self.bonus_row = {}
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl2.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl4.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl21.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl43.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl5.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl47.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl14.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl22.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl39.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl44.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

            self.m_spinCtrl11.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl12.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl131.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl141.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl13.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl111.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl15.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl16.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

        self.m_spinCtrl44.Enable()
        self.region = libs.DB.get_all(libs.models.Flor)
        self.region_name = ['']
        for i in self.region:
            self.region_name.append(i.name)
        self.m_choice8.SetItems(self.region_name)
        self.pol = [gui_lib.msg.cust_main_AddGrup_button[1], gui_lib.msg.cust_main_AddGrup_button[2], gui_lib.msg.cust_main_AddGrup_button[3]]
        self.m_choice11.SetItems(self.pol)
        self.m_choice11.SetSelection(0)
        if self.edit != None:
            if self.edit.region_id:
                self.m_choice8.SetSelection(self.edit.region_id)
            if self.edit.bonus_if_man is True:
                self.m_choice11.SetSelection(1)
            elif self.edit.bonus_if_man is False:
                self.m_choice11.SetSelection(2)
            else:
                self.m_choice11.SetSelection(0)
            self.m_checkBox31.SetValue(self.edit.bonus_hold)
            self.m_checkBox51.SetValue(self.edit.selected)
            self.m_checkBox53.SetValue(self.edit.more_than_one_from_redirect)
            self.m_checkBox55.SetValue(self.edit.bonus_in_mony)
            self.m_spinCtrl47.SetValue(self.edit.bonus_in_mony_sum)
            self.m_spinCtrl34.SetValue(self.edit.bonus_waith_for_in_mony)
            if self.edit.bonus_in_mony is False:
                self.m_spinCtrl47.Disable()
            else:
                self.m_spinCtrl47.Enable()
            if self.edit.bonus_on_day == '':
                self.m_checkBox20.SetValue(True)
                self.m_checkBox18.SetValue(False)
                self.m_checkBox19.SetValue(False)
                self.m_checkBox24.SetValue(False)
                self.m_checkBox25.SetValue(False)
                self.m_checkBox26.SetValue(False)
                self.m_checkBox27.SetValue(False)
                self.m_checkBox21.SetValue(False)
            else:
                data = json.loads(self.edit.bonus_on_day)
                self.m_checkBox20.SetValue(False)
                if 0 in data:
                    self.m_checkBox18.SetValue(True)
                if 1 in data:
                    self.m_checkBox19.SetValue(True)
                if 2 in data:
                    self.m_checkBox21.SetValue(True)
                if 3 in data:
                    self.m_checkBox24.SetValue(True)
                if 4 in data:
                    self.m_checkBox25.SetValue(True)
                if 5 in data:
                    self.m_checkBox26.SetValue(True)
                if 6 in data:
                    self.m_checkBox27.SetValue(True)
            self.m_checkBox47.SetValue(self.edit.restricted_bonus)
            self.m_checkBox40.SetValue(self.edit.bonus_warning_use)
            self.m_spinCtrl39.SetValue(self.edit.bonus_warning_mony)
            self.m_spinCtrl43.SetValue(self.edit.mony_back_min_pay)
            self.m_textCtrl2.SetEditable(False)
            self.m_spinCtrl22.SetValue(self.edit.no_out_befor)
            self.m_spinCtrl14.SetValue(self.edit.bonus_on_mony)
            self.m_textCtrl2.SetValue(self.edit.name)
            self.m_checkBox1.SetValue(self.edit.mony_back_use)
            self.m_textCtrl4.SetValue(str(self.edit.mony_back_pr/0.01))
            self.m_checkBox3.SetValue(self.edit.tombola_use)
            self.m_textCtrl5.SetValue(str(self.edit.tombola_coef))
            self.m_checkBox2.SetValue(self.edit.bonus_use)
            self.m_checkBox12.SetValue(self.edit.bonus_waith_for_in)
            # self.m_checkBox59.SetValue(self.edit.x2)

            # self.m_spinCtrl131.SetValue(self.edit.bonus_row_1_mony)
            # self.m_spinCtrl11.SetValue(self.edit.bonus_row_1_count)
            # self.m_spinCtrl141.SetValue(self.edit.bonus_row_2_mony)
            # self.m_spinCtrl12.SetValue(self.edit.bonus_row_2_count)
            # self.m_spinCtrl15.SetValue(self.edit.bonus_row_3_mony)
            # self.m_spinCtrl13.SetValue(self.edit.bonus_row_3_count)
            # self.m_spinCtrl16.SetValue(self.edit.bonus_row_4_mony)
            # self.m_spinCtrl111.SetValue(self.edit.bonus_row_4_count)
            self.m_radioBtn10.SetValue(self.edit.tombola_on_in)
            self.m_checkBox42.SetValue(self.edit.bonus_revert_by_bet)
            self.m_checkBox49.SetValue(self.edit.use_total_procent)
            self.m_spinCtrl44.SetValue(self.edit.total_procent)


            if self.edit.mony_back_pay == None:
                self.m_spinCtrl21.SetValue(0)
            else:
                self.m_spinCtrl21.SetValue(self.edit.mony_back_pay)
            if self.edit.bonus_direct is True:
                self.m_radioBtn12.SetValue(True)
                self.m_radioBtn2.SetValue(False)
                self.m_radioBtn1.SetValue(False)
                self.m_checkBox9.SetValue(self.edit.one_day_back_total)
                self.m_checkBox46.SetValue(self.edit.month_back)
                # if self.edit.one_day_back_total or self.edit.month_back:
                #     self.m_checkBox53.SetValue(False)
                #     self.m_checkBox53.Disable()
                self.OnOnDirectBonus(None)
            elif self.edit.bonus_by_in is True:
                self.ShowOnLost(None)
                self.m_checkBox9.SetValue(self.edit.one_day_back_total)
                self.m_checkBox46.SetValue(self.edit.month_back)
                self.m_radioBtn2.SetValue(True)
                self.m_radioBtn1.SetValue(False)
                self.m_radioBtn12.SetValue(False)
                # if self.edit.one_day_back_total or self.edit.month_back:
                #     self.m_checkBox53.SetValue(False)
                #     self.m_checkBox53.Disable()
            else:
                self.HideOnLost(None)
                self.m_radioBtn1.SetValue(True)
                self.m_radioBtn2.SetValue(False)
                self.m_checkBox9.SetValue(False)
                self.m_radioBtn12.SetValue(False)
                # if self.edit.one_day_back_total or self.edit.month_back:
                #     self.m_checkBox53.SetValue(False)
                #     self.m_checkBox53.Disable()
            self.m_checkBox8.SetValue(self.edit.bonus_one_per_day)

            self.HideOptions(None)
            if self.m_checkBox46.GetValue() is True or self.m_checkBox9.GetValue() is True:
                self.m_checkBox8.SetValue(True)
                self.m_checkBox8.Disable()
                self.m_checkBox49.Enable()
        self.OnShowWaithMony(None)
        self.OnSize(None)

        self.old_total_change(None)
        self.refresh_bonus_row()

    def OnShowWaithMony(self, event):
        if self.m_checkBox12.GetValue() == False:
            self.m_spinCtrl34.Disable()
            self.m_spinCtrl34.SetValue(0)
        else:
            if self.edit:
                self.m_spinCtrl34.SetValue(self.edit.bonus_waith_for_in_mony)
            self.m_spinCtrl34.Enable()

    def DelBonus( self, event ):
        item = self.m_listCtrl5.GetFirstSelected()
        item = self.m_listCtrl5.GetItem(item, col=0).GetText()
        try:
            del self.bonus_row[item]
            self.refresh_bonus_row()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()

    def OnEditBonus( self, event ):
        # item = self.bonus_row[self.m_listCtrl5.GetFirstSelected()]
        item = self.m_listCtrl5.GetFirstSelected()
        item = self.m_listCtrl5.GetItem(item, col=0).GetText()
        # print item, self.bonus_row
        dial = AddBonus(self, edit=[item, self.bonus_row[item]])
        dial.ShowModal()
        if dial.close is False:
            data = dial.edit
            del self.bonus_row[item]
            self.bonus_row[data[0]] = data[1]
            self.refresh_bonus_row()


    def SetBonus( self, event ):
        dial = AddBonus(self)
        dial.ShowModal()
        if dial.close is False:
            data =  dial.edit
            if data[0] in self.bonus_row:
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_BONUS_HAVE)
                dial.ShowModal()
                return
            self.bonus_row[data[0]] = data[1]
            self.refresh_bonus_row()


    def refresh_bonus_row(self):
        self.m_listCtrl5.DeleteAllItems()
        index = 0
        # print self.bonus_row
        for i in self.bonus_row:
            # try:
            #     self.m_listCtrl5.InsertItem(index, "{:.2f}".format(i))
            # except ValueError:
            self.m_listCtrl5.InsertItem(index, i)
            self.m_listCtrl5.SetItem(index, 1, str(self.bonus_row[i]))
            index += 1

    def OnPointInMony( self, event ):
        if self.m_checkBox55.GetValue() is True:
            self.m_spinCtrl47.Enable()
        else:
            self.m_spinCtrl47.Disable()

    def old_total_change(self, event):
        if self.m_checkBox49.GetValue() is False:
            self.m_spinCtrl44.Disable()
        else:
            self.m_spinCtrl44.Enable()

    def MountChange( self, event ):
        if self.m_checkBox46.GetValue() is True:
            self.m_checkBox9.SetValue(False)
            self.m_checkBox8.SetValue(True)
            self.m_checkBox8.Disable()
            # self.m_checkBox53.SetValue(False)
            # self.m_checkBox53.Disable()
            # self.m_checkBox49.Enable()
            # self.m_spinCtrl44.Enable()
        else:
            self.m_checkBox8.Enable()
            self.m_checkBox49.SetValue(False)
            # self.m_checkBox53.Enable()
            # self.m_checkBox49.Disable()
            # self.m_spinCtrl44.Disable()
            # self.m_checkBox49.SetValue(False)

    def DayChange( self, event ):
        if self.m_checkBox9.GetValue() is True:
            self.m_checkBox46.SetValue(False)
            self.m_checkBox8.SetValue(True)
            self.m_checkBox8.Disable()
            # self.m_checkBox53.Disable()
            # self.m_checkBox53.SetValue(False)
            self.m_checkBox49.Enable()
            # self.m_spinCtrl44.Enable()
        else:
            self.m_checkBox8.Enable()
            # self.m_checkBox53.Enable()
            self.m_checkBox49.SetValue(False)
            self.m_checkBox49.Disable()
            # self.m_spinCtrl44.Disable()
            # self.m_checkBox49.SetValue(False)

    def OnSize( self, event ):
        self.width, self.height = self.GetSize()
        # self.SetMinSize((self.width, self.height))
        # self.SetSize((self.width, self.height))
        self.m_listCtrl5.SetColumnWidth(0, self.width * 0.12)
        self.m_listCtrl5.SetColumnWidth(1, self.width * 0.12)
        self.m_scrolledWindow2.SetMinSize((self.width * 0.98, self.height * 0.85))
        self.m_scrolledWindow2.SetSize((self.width * 0.98, self.height * 0.85))
        # self.SetMinSize((self.width * 0.98, self.height * 0.85))
        # self.SetSize((self.width * 0.98, self.height * 0.85))
        # self.Fit()
        self.Layout()

    def HideOptions( self, event ):
        if self.m_checkBox47.GetValue() is True:
            self.m_checkBox12.SetValue(False)
            self.m_checkBox12.Disable()
            self.m_checkBox31.SetValue(False)
            self.m_checkBox31.Disable()
            self.m_spinCtrl22.SetValue(1)
            self.m_spinCtrl22.Disable()
            self.m_checkBox42.SetValue(False)
            self.m_checkBox42.Disable()
        else:
            self.m_checkBox12.Enable()
            self.m_checkBox31.Enable()
            self.m_spinCtrl22.Enable()
            self.m_checkBox42.Enable()

    def ShowOnLost(self, event):
        self.m_checkBox9.Show()
        self.m_checkBox8.Show()
        self.m_checkBox8.Enable()
        self.m_checkBox12.Show()
        self.m_checkBox46.Show()
        # self.m_checkBox49.Disable()
        # self.m_checkBox49.SetValue(False)
        # self.m_spinCtrl44.Disable()
        self.Layout()

    def OnOnDirectBonus(self, event):
        self.m_checkBox8.SetValue(True)
        self.m_checkBox8.Hide()
        # self.m_checkBox9.SetValue(False)
        # self.m_checkBox9.Hide()
        # self.m_checkBox46.SetValue(False)
        # self.m_checkBox46.Hide()
        self.m_checkBox8.Enable()
        # self.m_checkBox49.SetValue(False)
        # self.m_checkBox49.Enable()
        # self.m_spinCtrl44.Enable()
        # self.m_checkBox12.SetValue(True)
        self.m_checkBox12.Show()
        self.Layout()

    def HideOnLost(self, event):
        self.m_checkBox9.Hide()
        self.m_checkBox46.Hide()
        self.m_checkBox8.Show()
        self.m_checkBox8.Enable()
        self.m_checkBox12.Hide()
        self.m_checkBox8.SetValue(True)
        self.m_checkBox12.SetValue(False)
        # self.m_checkBox49.SetValue(False)
        # self.m_checkBox49.Disable()
        # self.m_spinCtrl44.Disable()
        self.m_checkBox9.SetValue(False)
        self.m_checkBox46.SetValue(False)
        self.Layout()
        
    def OnGo(self, event):
        err = libs.DB.make_obj(libs.models.GetCounterError)
        err.user_id = self.user.id
        err.info = 'CUST GROUP CHANGE' + ': ' + u'%s from %s' % (self.m_textCtrl2.GetValue(), self.user.name)
        libs.DB.add_object_to_session(err)
        if self.edit == None:
            obj = libs.DB.make_obj(libs.models.CustGrup)
            obj.name = self.m_textCtrl2.GetValue()
        else:
            obj = self.edit
            libs.DB.expire(obj)
        if self.m_checkBox20.GetValue() is True:
            obj.bonus_on_day = ''
        else:
            bonus_on_day = []
            if self.m_checkBox18.GetValue() is True:
                bonus_on_day.append(0)
            if self.m_checkBox19.GetValue() is True:
                bonus_on_day.append(1)
            if self.m_checkBox21.GetValue() is True:
                bonus_on_day.append(2)
            if self.m_checkBox24.GetValue() is True:
                bonus_on_day.append(3)
            if self.m_checkBox25.GetValue() is True:
                bonus_on_day.append(4)
            if self.m_checkBox26.GetValue() is True:
                bonus_on_day.append(5)
            if self.m_checkBox27.GetValue() is True:
                bonus_on_day.append(6)
            obj.bonus_on_day = json.dumps(bonus_on_day)

        try:
            obj.mony_back_use = self.m_checkBox1.GetValue()
            obj.bonus_hold = self.m_checkBox31.GetValue()
            pr = self.m_textCtrl4.GetValue()
            pr = pr.replace(',', '.')
            pr = float(pr)
            obj.mony_back_pr = pr*0.01
            
            obj.tombola_use = self.m_checkBox3.GetValue()
            t_coef = self.m_textCtrl5.GetValue()
            t_coef = t_coef.replace(',', '.')
            t_coef = float(t_coef)
            obj.bonus_in_mony = self.m_checkBox55.GetValue()
            obj.bonus_in_mony_sum = self.m_spinCtrl47.GetValue()
            obj.tombola_coef = t_coef
            obj.restricted_bonus = self.m_checkBox47.GetValue()
            obj.more_than_one_from_redirect = self.m_checkBox53.GetValue()
            obj.tombola_on_in = self.m_radioBtn10.GetValue()
            obj.mony_back_min_pay = self.m_spinCtrl43.GetValue()
            obj.no_out_befor = self.m_spinCtrl22.GetValue()
            obj.bonus_use = self.m_checkBox2.GetValue()
            obj.bonus_direct = self.m_radioBtn12.GetValue()
            obj.bonus_by_in = self.m_radioBtn2.GetValue()
            obj.bonus_on_mony = self.m_spinCtrl14.GetValue()
            obj.bonus_one_per_day = self.m_checkBox8.GetValue()
            obj.one_day_back_total = self.m_checkBox9.GetValue()
            obj.month_back = self.m_checkBox46.GetValue()
            obj.mony_back_pay = self.m_spinCtrl21.GetValue()
            obj.bonus_revert_by_bet = self.m_checkBox42.GetValue()
            obj.selected = self.m_checkBox51.GetValue()
            obj.use_total_procent = self.m_checkBox49.GetValue()
            obj.total_procent = self.m_spinCtrl44.GetValue()
            if self.m_choice8.GetSelection() > 0:
                obj.region_id = self.m_choice8.GetSelection()
            else:
                obj.region_id = None
            if self.m_choice11.GetSelection() == 1:
                obj.bonus_if_man = True
            elif self.m_choice11.GetSelection() == 2:
                obj.bonus_if_man = False
            else:
                obj.bonus_if_man = None
            # if self.edit.region_id:
            #     self.m_choice8.SetSelection(self.edit.region_id)
#             obj.bonus_row = self.m_spinCtrl2.GetValue()

            obj.bonus_row = json.dumps(self.bonus_row)
            # raise KeyError, obj.bonus_row
            # obj.x2 = self.m_checkBox59.GetValue()
            # obj.bonus_row_1_mony = self.m_spinCtrl131.GetValue()
            # obj.bonus_row_1_count = self.m_spinCtrl11.GetValue()
            #
            # obj.bonus_row_2_mony = self.m_spinCtrl141.GetValue()
            # obj.bonus_row_2_count = self.m_spinCtrl12.GetValue()
            #
            # obj.bonus_row_3_mony = self.m_spinCtrl15.GetValue()
            # obj.bonus_row_3_count = self.m_spinCtrl13.GetValue()
            #
            # obj.bonus_row_4_mony = self.m_spinCtrl16.GetValue()
            # obj.bonus_row_4_count = self.m_spinCtrl111.GetValue()
                
            obj.pub_user_id = self.user.id
            obj.bonus_waith_for_in = self.m_checkBox12.GetValue()
            obj.bonus_waith_for_in_mony = self.m_spinCtrl34.GetValue()
            obj.bonus_warning_use = self.m_checkBox40.GetValue()
            obj.bonus_warning_mony = self.m_spinCtrl39.GetValue()
            
        except Exception as e:
            libs.log.stderr_logger.error(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.BAD_VALUE)
            dial.ShowModal()
        else:
            libs.DB.add_object_to_session(obj)
            try:                
                if self.edit != None:
                    all_user = libs.DB.get_all_where(libs.models.CustUser, grup_id=obj.id, use_group_conf=True)
                    if all_user != []:
                        dial = AllUserEditByGroup(self, all_user, obj)
                        dial.ShowModal()
                        if dial.error == 'DONE':
                            libs.DB.commit()
                    else:
                        libs.DB.commit()
                else:
                    libs.DB.commit()
            except Exception as e:
                libs.DB.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
            else:
                self.OnClose(event)
            
            
    def AllDayClick( self, event ):
        self.m_checkBox20.SetValue(True)
        self.m_checkBox18.SetValue(False)
        self.m_checkBox19.SetValue(False)
        self.m_checkBox24.SetValue(False)
        self.m_checkBox25.SetValue(False)
        self.m_checkBox26.SetValue(False)
        self.m_checkBox27.SetValue(False)
        self.m_checkBox21.SetValue(False)

    def OneDayClick( self, event ):
        self.m_checkBox20.SetValue(False)

    def OnClose(self,event):
        try:
            self.parent.add_grup()
        except AttributeError:
            self.parent.GetParent().add_grup()
        self.Destroy()

class AddGrupNameForCopy(gui.AddSity, gui_lib.keybords.Keyboard):
    def __init__(self, parent, group, user):
        gui.AddSity.__init__(self, parent)
        self.parent = parent
        self.group = group
        self.user = user
        self.SetTitle(gui_lib.msg.users_main_AddGrup_text['Text1'])
        self.m_staticText40.SetLabel(gui_lib.msg.users_main_AddGrup_text['Text1'])
        self.m_button9.SetLabel(gui_lib.msg.cust_main_AddSity_button['m_button9'])
        self.m_button10.SetLabel(gui_lib.msg.cust_main_AddSity_button['m_button10'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl21.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose(self, event):
        try:
            self.parent.add_grup()
        except AttributeError:
            self.parent.GetParent().add_grup()
        self.Destroy()

    def OnGo(self, event):
        name = self.m_textCtrl21.GetValue()
        try:
            if name == '' or name == u'':
                raise NameError
            if name in self.parent.my_grup_text:
                raise NameError
            obj = libs.DB.make_obj(libs.models.CustGrup)
            obj.name = name
            obj.mony_back_use = self.group.mony_back_use
            obj.mony_back_pr = self.group.mony_back_pr
            obj.mony_back_pay = self.group.mony_back_pay
            obj.mony_back_min_pay = self.group.mony_back_min_pay
            obj.bonus_if_man = self.group.bonus_if_man
            obj.tombola_use = self.group.tombola_use
            obj.tombola_on_in = self.group.tombola_on_in
            obj.tombola_coef = self.group.tombola_coef

            obj.bonus_hold = self.group.bonus_hold
            obj.bonus_use = self.group.bonus_use
            obj.bonus_direct = self.group.bonus_direct
            obj.bonus_by_in = self.group.bonus_by_in
            obj.bonus_one_per_day = self.group.bonus_one_per_day
            obj.bonus_on_mony = self.group.bonus_on_mony

            obj.bonus_waith_for_in = self.group.bonus_waith_for_in
            obj.no_out_befor = self.group.no_out_befor

            obj.bonus_row = self.group.bonus_row
            # obj.x2 = self.group.x2
            # obj.bonus_row_1_count = self.group.bonus_row_1_count
            # obj.bonus_row_2_mony = self.group.bonus_row_2_mony
            # obj.bonus_row_2_count = self.group.bonus_row_2_count
            # obj.bonus_row_3_mony = self.group.bonus_row_3_mony
            # obj.bonus_row_3_count = self.group.bonus_row_3_count
            # obj.bonus_row_4_mony = self.group.bonus_row_4_mony
            # obj.bonus_row_4_count = self.group.bonus_row_4_count
            obj.pub_user_id = self.user.id
            obj.bonus_on_day = self.group.bonus_on_day

            obj.bonus_warning_use = self.group.bonus_warning_use
            obj.bonus_warning_mony = self.group.bonus_warning_mony
            obj.bonus_revert_by_bet = self.group.bonus_revert_by_bet
            obj.one_day_back_total = self.group.one_day_back_total
            obj.month_back = self.group.month_back
            obj.restricted_bonus = self.group.restricted_bonus
            obj.region_id = self.group.region_id

            obj.use_total_procent = self.group.use_total_procent
            obj.total_procent = self.group.total_procent
            obj.more_than_one_from_redirect = self.group.more_than_one_from_redirect
            libs.DB.add_object_to_session(obj)
            libs.DB.commit()
            self.OnClose(event)
        except NameError:
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
            dial.ShowModal()
            return
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()

class AddSity(gui.AddSity, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        gui.AddSity.__init__(self, parent)
        self.parent = parent
        self.SetTitle(gui_lib.msg.cust_main_AddSity_name)
        self.m_staticText40.SetLabel(gui_lib.msg.cust_main_AddSity_text['m_staticText40'])
        self.m_button9.SetLabel(gui_lib.msg.cust_main_AddSity_button['m_button9'])
        self.m_button10.SetLabel(gui_lib.msg.cust_main_AddSity_button['m_button10'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl21.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose(self, event):
        self.Destroy()
        
    def OnGo(self, event):
        obj = libs.DB.make_obj(libs.models.Sity)
        name = self.m_textCtrl21.GetValue()
        try:
            if name == '' or name == u'':
                raise NameError
            if name in self.parent.m_choice2Choices:
                raise NameError
            obj.name = name
            libs.DB.add_object_to_session(obj)
            libs.DB.commit()
            self.OnClose(event)
        except NameError:
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
            dial.ShowModal()
            return
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
        
class AddCust(gui.AddCust, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user, edit=None):
        self.parent = parent
        gui.AddCust.__init__(self, parent)
        self.user = user
        self.edit = edit
        self.m_button1011.Hide()
        self.m_radioBtn411.Hide()
        self._set_right()

        self._set_sity()
        self.cart = []
        self.region = libs.DB.get_all(libs.models.Flor)
        self.region_name = ['']
        for i in self.region:
            self.region_name.append(i.name)
        self.pol = [gui_lib.msg.cust_main_AddCust_text['all'], gui_lib.msg.cust_main_AddCust_text['man'], gui_lib.msg.cust_main_AddCust_text['women']]
        self.m_choice9.SetItems(self.region_name)
        self.m_choice10.SetItems(self.pol)

        if self.edit == None:
            a = range(100000, 999999)
            self.m_staticText421.SetLabel(u'%s' % (a[random.randint(0, len(a))]))
            self.m_textCtrl18.SetValue(libs.models.TZ.date_to_str(libs.models.TZ.now()))
            self.bonus_row = {}
            self.m_choice10.SetSelection(0)
        else:
            if self.edit.bonus_if_man == True:
                self.m_choice10.SetSelection(1)
            elif self.edit.bonus_if_man is False:
                self.m_choice10.SetSelection(2)
            else:
                self.m_choice10.SetSelection(0)
            if self.edit.region_id:
                self.m_choice9.SetSelection(self.edit.region_id)
            cart = libs.DB.get_all_where(libs.models.CustCart, user_id=self.edit.id)
            for i in cart:
                self.cart.append(i.catr_id)
            self.m_staticText421.SetLabel('')
            # self.m_textCtrl20.SetValue(self.edit.country_code)
            self.m_textCtrl911.SetValue(self.edit.name)
            self.m_textCtrl1011.SetValue(self.edit.tel)
            self.m_textCtrl1211.SetValue(self.edit.e_mail)
            self.m_textCtrl1721.SetValue(self.edit.personal_cart_id)
            self.m_textCtrl1621.SetValue(self.edit.personal_egn)
            self.m_textCtrl1811.SetValue(self.edit.personal_addres)
            if self.edit.man is None:
                self.m_checkBox601.SetValue(True)
            else:
                self.m_checkBox601.SetValue(self.edit.man)
            if self.edit.persona_sity_id:
                self.m_choice211.SetSelection(self.user_sity.index(self.edit.persona_sity_id) + 1)

            # self.m_choice211.SetSelection(self.user_sity.index(self.edit.persona_sity_id)+1)
            index = self.parent.my_grup_text.index(self.edit.grup.name)
            self.m_choice311.SetSelection(index+1)
            valit_time = libs.models.TZ.date_to_str(self.edit.personal_cart_valid)
            # print valit_time
            # x = wx.DateTime()
            # x.ParseDate(valit_time)

            self.m_textCtrl18.SetValue(valit_time)
            if self.edit.use_group_conf is True:
                # print json.loads(self.edit.grup.bonus_row)
                try:
                    self.bonus_row = json.loads(self.edit.grup.bonus_row)
                except ValueError:
                    self.bonus_row = {}
                    self.edit.grup.bonus_row = json.dumps({})
                    libs.DB.add_object_to_session(self.edit.grup)
                    libs.DB.commit()
                # else:
                #     self.bonus_row = {}
                # self.m_button37.Hide()
                # self.m_button36.Hide()
                # self.m_checkBox60.SetValue(self.edit.grup.x2)
                self.m_checkBox60.Disable()
                if self.edit.grup.mony_back_pay == None:
                    self.m_spinCtrl20.SetValue(0)
                else:
                    self.m_spinCtrl20.SetValue(self.edit.grup.mony_back_pay)

                self.m_checkBox50.SetValue(self.edit.grup.use_total_procent)
                self.m_spinCtrl45.SetValue(self.edit.grup.total_procent)
                self.m_checkBox56.SetValue(self.edit.grup.bonus_in_mony)
                self.m_spinCtrl48.SetValue(self.edit.grup.bonus_in_mony_sum)
                if self.edit.grup.bonus_in_mony is True:
                    self.m_spinCtrl48.Enable()
                else:
                    self.m_spinCtrl48.Disable()

                self.m_checkBox48.SetValue(self.edit.grup.restricted_bonus)
                self.m_checkBox41.SetValue(self.edit.grup.bonus_warning_use)
                self.m_checkBox43.SetValue(self.edit.grup.bonus_revert_by_bet)
                self.m_spinCtrl40.SetValue(self.edit.grup.bonus_warning_mony)
                self.m_checkBox30.SetValue(self.edit.grup.bonus_hold)
                self.m_spinCtrl42.SetValue(self.edit.mony_back_min_pay)
                self.m_radioBtn311.SetValue(True)
                self.m_radioBtn411.SetValue(False)
                self.m_checkBox111.SetValue(self.edit.grup.mony_back_use)
#                 print self.edit.grup.mony_back_pr, self.edit.grup.mony_back_pr/0.01
                self.m_textCtrl411.SetValue(str(self.edit.grup.mony_back_pr/0.01))
                self.m_checkBox311.SetValue(self.edit.grup.tombola_use)
                self.m_textCtrl511.SetValue(str(self.edit.grup.tombola_coef))
                
                self.m_checkBox211.SetValue(self.edit.grup.bonus_use)
                self.m_spinCtrl14111.SetValue(self.edit.grup.bonus_on_mony)
                self.m_radioBtn211.SetValue(self.edit.grup.bonus_by_in)
#                 self.m_spinCtrl2111.SetValue(self.edit.grup.bonus_row)
                
                # self.m_spinCtrl131.SetValue(self.edit.grup.bonus_row_1_mony)
                # self.m_spinCtrl11.SetValue(self.edit.grup.bonus_row_1_count)
                # self.m_spinCtrl141.SetValue(self.edit.grup.bonus_row_2_mony)
                # self.m_spinCtrl12.SetValue(self.edit.grup.bonus_row_2_count)
                # self.m_spinCtrl15.SetValue(self.edit.grup.bonus_row_3_mony)
                # self.m_spinCtrl13.SetValue(self.edit.grup.bonus_row_3_count)
                self.m_spinCtrl23.SetValue(self.edit.grup.no_out_befor)

                # self.m_spinCtrl16.SetValue(self.edit.grup.bonus_row_4_mony)
                # print self.edit.grup.bonus_row_4_mony, self.m_spinCtrl16.GetValue()  # self.edit.grup.bonus_row_4_count
                # self.m_spinCtrl111.SetValue(self.edit.grup.bonus_row_4_count)
                self.m_checkBox52.SetValue(self.edit.grup.more_than_one_from_redirect)
                self.m_radioBtn10.SetValue(self.edit.grup.tombola_on_in)
                self.m_checkBox131.SetValue(self.edit.grup.bonus_waith_for_in)
                if self.edit.grup.bonus_on_day == '':
                    self.m_checkBox22.SetValue(True)
                    self.m_checkBox23.SetValue(False)
                    self.m_checkBox24.SetValue(False)
                    self.m_checkBox25.SetValue(False)
                    self.m_checkBox26.SetValue(False)
                    self.m_checkBox27.SetValue(False)
                    self.m_checkBox28.SetValue(False)
                    self.m_checkBox29.SetValue(False)
                else:
                    bonus_on_day = json.loads(self.edit.grup.bonus_on_day)
                    self.m_checkBox22.SetValue(False)
                    if 0 in bonus_on_day:
                        self.m_checkBox23.SetValue(True)
                    if 1 in bonus_on_day:
                        self.m_checkBox24.SetValue(True)
                    if 2 in bonus_on_day:
                        self.m_checkBox25.SetValue(True)
                    if 3 in bonus_on_day:
                        self.m_checkBox26.SetValue(True)
                    if 4 in bonus_on_day:
                        self.m_checkBox27.SetValue(True)
                    if 5 in bonus_on_day:
                        self.m_checkBox28.SetValue(True)
                    if 6 in bonus_on_day:
                        self.m_checkBox29.SetValue(True)
                if  self.edit.grup.bonus_direct is True:
                    self.OnDirectBonus(None)
                    self.m_radioBtn11.SetValue(True)
                    self.m_radioBtn211.SetValue(False)
                    self.m_radioBtn111.SetValue(False)
                    self.m_checkBox11.SetValue(self.edit.grup.one_day_back_total)
                    self.m_checkBox45.SetValue(self.edit.grup.month_back)
                elif self.edit.grup.bonus_by_in is True:
                    self.ShowOnLost(None)
                    self.m_checkBox11.SetValue(self.edit.grup.one_day_back_total)
                    self.m_checkBox45.SetValue(self.edit.grup.month_back)
                    self.m_radioBtn211.SetValue(True)
                    self.m_radioBtn111.SetValue(False)

                else:
                    self.HideOnLost(None)
                    self.m_radioBtn111.SetValue(True)
                    self.m_radioBtn211.SetValue(False)
                    self.m_checkBox11.SetValue(False)
                self.m_checkBox10.SetValue(self.edit.grup.bonus_one_per_day)
            
            else:
                try:
                    self.bonus_row = json.loads(self.edit.bonus_row)
                except ValueError:
                    self.bonus_row = {}
                    self.edit.bonus_row = json.dumps({})
                    libs.DB.add_object_to_session(self.edit)
                    libs.DB.commit()
                # else:
                #     self.bonus_row = {}
                # self.m_button37.Show()
                # self.m_button36.Show()
                # self.m_checkBox60.SetValue(self.edit.x2)
                self.m_checkBox60.Enable()

                self.m_radioBtn311.SetValue(False)
                self.m_radioBtn411.SetValue(True)
                self.m_checkBox56.SetValue(self.edit.bonus_in_mony)
                self.m_spinCtrl48.SetValue(self.edit.bonus_in_mony_sum)
                if self.edit.bonus_in_mony is True:
                    self.m_spinCtrl48.Enable()
                else:
                    self.m_spinCtrl48.Disable()
                self.m_checkBox50.SetValue(self.edit.use_total_procent)
                self.m_spinCtrl45.SetValue(self.edit.total_procent)
                self.m_checkBox48.SetValue(self.edit.restricted_bonus)
                self.m_checkBox111.SetValue(self.edit.mony_back_use)
                self.m_spinCtrl23.SetValue(self.edit.no_out_befor)
                self.m_textCtrl411.SetValue(str(self.edit.mony_back_pr/0.01))
                self.m_checkBox311.SetValue(self.edit.tombola_use)
                self.m_textCtrl511.SetValue(str(self.edit.tombola_coef))
                self.m_checkBox30.SetValue(self.edit.bonus_hold)
                self.m_checkBox41.SetValue(self.edit.bonus_warning_use)
                self.m_spinCtrl40.SetValue(self.edit.bonus_warning_mony)
                self.m_checkBox43.SetValue(self.edit.bonus_revert_by_bet)
                if self.edit.bonus_on_day == '':
                    self.m_checkBox22.SetValue(True)
                    self.m_checkBox23.SetValue(False)
                    self.m_checkBox24.SetValue(False)
                    self.m_checkBox25.SetValue(False)
                    self.m_checkBox26.SetValue(False)
                    self.m_checkBox27.SetValue(False)
                    self.m_checkBox28.SetValue(False)
                    self.m_checkBox29.SetValue(False)
                else:
                    bonus_on_day = json.loads(self.edit.bonus_on_day)
                    self.m_checkBox22.SetValue(False)
                    if 0 in bonus_on_day:
                        self.m_checkBox23.SetValue(True)
                    if 1 in bonus_on_day:
                        self.m_checkBox24.SetValue(True)
                    if 2 in bonus_on_day:
                        self.m_checkBox25.SetValue(True)
                    if 3 in bonus_on_day:
                        self.m_checkBox26.SetValue(True)
                    if 4 in bonus_on_day:
                        self.m_checkBox27.SetValue(True)
                    if 5 in bonus_on_day:
                        self.m_checkBox28.SetValue(True)
                    if 6 in bonus_on_day:
                        self.m_checkBox29.SetValue(True)
                if self.edit.mony_back_pay == None:
                    self.m_spinCtrl20.SetValue(0)
                else:
                    self.m_spinCtrl20.SetValue(self.edit.mony_back_pay)
                self.m_checkBox50.SetValue(self.edit.use_total_procent)
                self.m_spinCtrl45.SetValue(self.edit.total_procent)
                self.m_checkBox211.SetValue(self.edit.bonus_use)
                self.m_spinCtrl14111.SetValue(self.edit.bonus_on_mony)
                self.m_radioBtn211.SetValue(self.edit.bonus_on_mony)
#                 self.m_spinCtrl2111.SetValue(self.edit.bonus_row)
                self.m_checkBox131.SetValue(self.edit.bonus_waith_for_in)
                # self.m_spinCtrl131.SetValue(self.edit.bonus_row_1_mony)
                # self.m_spinCtrl11.SetValue(self.edit.bonus_row_1_count)
                # self.m_spinCtrl141.SetValue(self.edit.bonus_row_2_mony)
                # self.m_spinCtrl12.SetValue(self.edit.bonus_row_2_count)
                # self.m_spinCtrl15.SetValue(self.edit.bonus_row_3_mony)
                # self.m_spinCtrl13.SetValue(self.edit.bonus_row_3_count)
                # self.m_spinCtrl16.SetValue(self.edit.bonus_row_4_mony)
                # self.m_spinCtrl111.SetValue(self.edit.bonus_row_4_count)
                self.m_radioBtn10.SetValue(self.edit.tombola_on_in)
                self.m_checkBox52.SetValue(self.edit.more_than_one_from_redirect)
                # raise KeyError, self.edit.bonus_direct
                if self.edit.bonus_direct is True:
                    self.OnDirectBonus(None)
                    self.m_radioBtn11.SetValue(True)
                    self.m_radioBtn211.SetValue(False)
                    self.m_radioBtn111.SetValue(False)
                    self.m_checkBox11.SetValue(self.edit.one_day_back_total)
                    # if self.edit.one_day_back_total or self.edit.month_back:
                    #     self.m_checkBox52.SetValue(False)
                        # self.m_checkBox52.Disable()
                    self.m_checkBox45.SetValue(self.edit.month_back)
                elif self.edit.bonus_by_in is True:
                    self.ShowOnLost(None)
                    self.m_checkBox11.SetValue(self.edit.one_day_back_total)
                    self.m_checkBox45.SetValue(self.edit.month_back)
                    # if self.edit.one_day_back_total or self.edit.month_back:
                    #     self.m_checkBox52.SetValue(False)
                        # self.m_checkBox52.Disable()
                    self.m_radioBtn211.SetValue(True)
                    self.m_radioBtn111.SetValue(False)
                    self.m_radioBtn11.SetValue(False)

                else:
                    self.HideOnLost(None)
                    self.m_radioBtn111.SetValue(True)
                    self.m_radioBtn211.SetValue(False)
                    self.m_checkBox11.SetValue(False)
                self.m_checkBox10.SetValue(self.edit.bonus_one_per_day)
            self.m_checkBox13.SetValue(self.edit.forbiden)
            self.m_checkBox59.SetValue(self.edit.in_nra)
        # self.width, self.height = self.parent.GetSize()
        # self.SetSize((self.width, self.height))
        self.SetTitle(gui_lib.msg.cust_main_AddCust_name)
        self.m_button34.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_button34'])
        self.m_checkBox56.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_checkBox56'])
        self.m_checkBox45.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_checkBox45'])
        self.m_staticText3011.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText3011'])
        self.m_button29.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_button29'])
        self.m_checkBox601.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox601'])
        self.m_checkBox41.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_checkBox41'])
        self.m_staticText42.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText42']+ ': ' + str(len(self.cart)))
        self.m_staticText311.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText311'])
        self.m_checkBox48.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_checkBox48'])
        self.m_staticText77.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText77'])
        self.m_staticText511.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText511'])
        self.m_staticText1711.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText1711'])
        self.m_checkBox43.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_checkBox43'])
        self.m_staticText89.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText89'])
        self.m_staticText80.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText80'])
        self.m_staticText1811.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText1811'])
        self.m_staticText2011.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText2011'])
        self.m_staticText2411.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText2411'])
        self.m_staticText2511.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText2511'])
        self.m_staticText2611.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText2611'])
        self.m_staticText2711.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText2711'])
        self.m_staticText2811.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText2811'])
        self.m_staticText39111.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText39111'])
        self.m_staticText79.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText79'])
        self.m_listCtrl6.InsertColumn(0, gui_lib.msg.cust_main_AddCust_text['mony'])
        self.m_listCtrl6.InsertColumn(1, gui_lib.msg.cust_main_AddCust_text['count'])
        # self.m_staticText33.SetLabel(gui_lib.msg.cust_main_AddCust_text['count'])
        # self.m_staticText34.SetLabel(gui_lib.msg.cust_main_AddCust_text['mony'])
        # self.m_staticText35.SetLabel(gui_lib.msg.cust_main_AddCust_text['count'])
        # self.m_staticText36.SetLabel(gui_lib.msg.cust_main_AddCust_text['mony'])
        # self.m_staticText37.SetLabel(gui_lib.msg.cust_main_AddCust_text['count'])
        # self.m_staticText38.SetLabel(gui_lib.msg.cust_main_AddCust_text['mony'])
        # self.m_staticText331.SetLabel(gui_lib.msg.cust_main_AddCust_text['count'])
        # self.m_staticText341.SetLabel(gui_lib.msg.cust_main_AddCust_text['mony'])

        self.m_checkBox50.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox50'])
        self.m_button1011.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_button1011'])
        self.m_radioBtn311.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_radioBtn311'])
        self.m_radioBtn411.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_radioBtn411'])
        self.m_checkBox13.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox13'])
        self.m_checkBox59.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox59'])
        self.m_radioBtn9.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_radioBtn9'])
        self.m_radioBtn10.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_radioBtn10'])
        self.m_radioBtn211.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_radioBtn211'])
        self.m_radioBtn111.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_radioBtn111'])
        self.m_radioBtn11.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_radioBtn11'])
        self.m_checkBox30.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox30'])
        self.m_checkBox10.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox10'])
        self.m_checkBox11.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox11'])
        self.m_checkBox131.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox131'])
        self.m_checkBox52.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox52'])
        self.m_checkBox22.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox22'])
        self.m_checkBox23.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox23'])
        self.m_checkBox24.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox24'])
        self.m_checkBox25.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox25'])
        self.m_checkBox26.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox26'])
        self.m_checkBox27.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox27'])
        self.m_checkBox29.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox29'])
        self.m_checkBox28.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_checkBox28'])
        self.m_button911.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_button911'])
        self.m_button811.SetLabel(gui_lib.msg.cust_main_AddCust_button['m_button811'])

        self.m_checkBox43.SetToolTip(gui_lib.msg.cust_main_AddCust_tooltip['m_checkBox43'])
        self.m_button811.SetToolTip(gui_lib.msg.cust_main_AddCust_tooltip['m_button811'])
        self.m_button1011.SetToolTip(gui_lib.msg.cust_main_AddCust_tooltip['m_button1011'])
        self.m_bpButton312.SetToolTip(gui_lib.msg.cust_main_AddCust_tooltip['m_bpButton312'])
        self.m_bpButton13.SetToolTip(gui_lib.msg.cust_main_AddCust_tooltip['m_bpButton13'])
        self.m_bpButton81.SetToolTip(gui_lib.msg.cust_main_AddCust_tooltip['m_bpButton81'])
        self.m_bpButton311.SetToolTip(gui_lib.msg.cust_main_AddCust_tooltip['m_bpButton311'])
        self.m_spinCtrl40.SetToolTip(gui_lib.msg.cust_main_AddCust_tooltip['m_spinCtrl40'])

        self.width, self.height = self.parent.GetSize()
        self.SetSize((self.width*0.80, self.height*0.85))
        self.HideOptions(None)
        if self.m_checkBox11.GetValue() is True or self.m_checkBox45.GetValue() is True:
            self.m_checkBox10.SetValue(True)
            self.m_checkBox10.Disable()
            self.m_checkBox50.Enable()
            self.m_spinCtrl45.Enable()
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl911.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl1011.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl1211.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl1621.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl1721.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl18.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl1811.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl411.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl20.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl42.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

            self.m_textCtrl511.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl48.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl11.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl131.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl13.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl15.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl12.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl141.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl111.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl16.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

            self.m_spinCtrl14111.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl23.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl40.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl45.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
        self.refresh_bonus_row()
        self.OnShowWaithMony(None)
        self.OnSize(None)

    def OnShowWaithMony(self, event):
        if self.m_checkBox131.GetValue() == False:
            self.m_spinCtrl33.Disable()
            self.m_spinCtrl33.SetValue(0)
        else:
            if self.edit:
                self.m_spinCtrl33.SetValue(self.edit.bonus_waith_for_in_mony)
            self.m_spinCtrl33.Enable()
        self.Fit()
        self.Layout()

    def OnPersonal( self, event ):
        if self.m_radioBtn311.GetValue() is True:
            # self.m_button37.Hide()
            # self.m_button36.Hide()
            self.m_checkBox60.Disable()
        else:
            # self.m_button37.Show()
            # self.m_button36.Show()
            self.m_checkBox60.Enable()

    def ReadOCR( self, event ):
        data = False
        dial = ReadOCR(self.parent.GetParent())
        dial.ShowModal()
        data = dial.data
        if data == False or data == None:
            dial = wx.MessageDialog(self, *gui_lib.msg.OCR_READ_ERROR)
            dial.ShowModal()
            return
        # else:
        #     data = data
        if data[0] != 'DISABLE' and data[0] != 'ERROR' and data[0] != 'LITLE' and data[0] != 'EXPIRED':
            self.m_textCtrl1621.SetValue(data[1]['EGN'])
            self.m_textCtrl1721.SetValue(data[1]['LK'])
            self.m_textCtrl911.SetValue(data[1]['name'] + " " + data[1]['father_name'] + " " + data[1]['surname'])
            self.m_textCtrl20.SetValue(data[1]['country_code'])
            self.m_textCtrl18.SetValue(data[1]['VALID'])
        elif data[0] == 'LITLE':
            dial = wx.MessageDialog(self, *gui_lib.msg.EGN_NO_YEARS)
            dial.ShowModal()
        elif data[0] == 'EXPIRED':
            dial = wx.MessageDialog(self, *gui_lib.msg.CART_EXPIRED)
            dial.ShowModal()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.OCR_READ_ERROR)
            dial.ShowModal()

    def DelBonus(self, event):
        item = self.m_listCtrl6.GetFirstSelected()
        item = self.m_listCtrl6.GetItem(item, col=0).GetText()
        try:
            del self.bonus_row[item]
            self.refresh_bonus_row()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()

    def OnEditBonus(self, event):
        # item = self.bonus_row[self.m_listCtrl5.GetFirstSelected()]
        item = self.m_listCtrl6.GetFirstSelected()
        item = self.m_listCtrl6.GetItem(item, col=0).GetText()
        # print item, self.bonus_row
        dial = AddBonus(self, edit=[item, self.bonus_row[item]])
        dial.ShowModal()
        if dial.close is False:
            data = dial.edit
            del self.bonus_row[item]
            self.bonus_row[data[0]] = data[1]
            self.refresh_bonus_row()

    def SetBonus(self, event):
        dial = AddBonus(self)
        dial.ShowModal()
        if dial.close is False:
            data = dial.edit
            if data[0] in self.bonus_row:
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_BONUS_HAVE)
                dial.ShowModal()
                return
            self.bonus_row[data[0]] = data[1]
            self.refresh_bonus_row()

    def refresh_bonus_row(self):
        self.m_listCtrl6.DeleteAllItems()
        index = 0
        # print self.bonus_row
        for i in self.bonus_row:
            # try:
            #     self.m_listCtrl5.InsertItem(index, "{:.2f}".format(i))
            # except ValueError:
            self.m_listCtrl6.InsertItem(index, i)
            self.m_listCtrl6.SetItem(index, 1, str(self.bonus_row[i]))
            index += 1

    def OnPointInMony( self, event ):
        if self.m_checkBox56.GetValue() is True:
            self.m_spinCtrl48.Enable()
        else:
            self.m_spinCtrl48.Disable()

    def IsEGNValid( self, event , button_click=True):
        egn = self.m_textCtrl1621.GetValue()
        try:
            int(egn)
        except Exception:
            dial = wx.MessageDialog(self, *gui_lib.msg.EGN_IS_NOT_VALID)
            dial.ShowModal()
            return
        if len(egn) != 10:
            dial = wx.MessageDialog(self, *gui_lib.msg.EGN_IS_NOT_VALID)
            dial.ShowModal()
            return
        else:
            mounth = int(str('%s%s' % (egn[2:3], egn[3:4])))
            if mounth >=40:
                mounth = mounth - 40
                year = int('20' + egn[0:1] + egn[1:2])
            else:
                year = int('19' + egn[0:1] + egn[1:2])
            day = int(egn[4:5] + egn[5:6])
            my_sity = int(egn[6:7] + egn[7:8]+egn[8:9])
            tmp = []
            for i in egn:
                tmp.append(int(i))
            egn = tmp


            my_date = datetime.datetime.now()
            if mounth > 12 or mounth < 0:
                dial = wx.MessageDialog(self, *gui_lib.msg.EGN_IS_NOT_VALID)
                dial.ShowModal()
                return
            if year < my_date.year - 100:
                dial = wx.MessageDialog(self, *gui_lib.msg.EGN_IS_NOT_VALID)
                dial.ShowModal()
                return
            if my_date.year - 18 < year:
                dial = wx.MessageDialog(self, *gui_lib.msg.EGN_NO_YEARS)
                dial.ShowModal()
                return
            elif my_date.year - 18 == year:
                if my_date.month < mounth:
                    dial = wx.MessageDialog(self, *gui_lib.msg.EGN_NO_YEARS)
                    dial.ShowModal()
                    return
                elif my_date.month == mounth:
                    if my_date.day <= day:
                        dial = wx.MessageDialog(self, *gui_lib.msg.EGN_NO_YEARS)
                        dial.ShowModal()
                        return

            if egn[8] % 2 > 0:
                man = gui_lib.msg.cust_main_AddCust_text['women']
                self.m_checkBox601.SetValue(False)
            else:
                man = gui_lib.msg.cust_main_AddCust_text['man']
                self.m_checkBox601.SetValue(True)
            coef = [2,4,8,5,10,9,7,3,6]
            sum = 0.0
            for i in range(0, len(egn)):
                if i < 9:
                    sum += egn[i] * coef[i]
            sum = sum % 11
            sum = int(sum)
            if sum == 10:
                sum = 0
            if sum != egn[9]:
                dial = wx.MessageDialog(self, *gui_lib.msg.EGN_IS_NOT_VALID)
                dial.ShowModal()
                return
            # if sum >= 10 and egn[9] != 0:
            #     print sum, egn[9]
            #     dial = wx.MessageDialog(self, *gui_lib.msg.EGN_IS_NOT_VALID)
            #     dial.ShowModal()
            #     return
            # elif sum < 10 and egn[9] != sum:
            #     print 6
            #     dial = wx.MessageDialog(self, *gui_lib.msg.EGN_IS_NOT_VALID)
            #     dial.ShowModal()
            #     return
            data = libs.DB.get_one_where(libs.models.CustUser, personal_egn=self.m_textCtrl1621.GetValue())
            if data == None:
                pass
            else:
                if self.edit == None:
                    dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
                    dial.ShowModal()
                    return
                else:
                    if data.id != self.edit.id:
                        dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
                        dial.ShowModal()
                        return


            burt_date = '%s.%s.%s' % (day, mounth, year)
            sity = gui_lib.msg.SITY[999]
            for i in sorted(list(gui_lib.msg.SITY.keys())):
                if my_sity <= i:
                    sity = gui_lib.msg.SITY[i]
                    break
            if button_click is False:
                return True
            gui_lib.msg.EGN_IS_VALID[0] = gui_lib.msg.EGN_IS_VALID[0] % {'man':man, 'burt_date':burt_date, 'sity':sity}
            dial = wx.MessageDialog(self, *gui_lib.msg.EGN_IS_VALID)
            dial.ShowModal()
            importlib.reload(gui_lib.msg)

    def DayChange( self, event ):
        if self.m_checkBox11.GetValue() is True:
            self.m_checkBox45.SetValue(False)
            self.m_checkBox10.SetValue(True)
            self.m_checkBox10.Disable()
            self.m_checkBox50.Enable()
            self.m_spinCtrl45.Enable()
            # self.m_checkBox52.SetValue(False)
            # self.m_checkBox52.Disable()
        else:
            self.m_checkBox10.Enable()
            self.m_checkBox50.Disable()
            self.m_checkBox50.SetValue(False)
            self.m_spinCtrl45.Disable()
            # self.m_checkBox52.Enable()
            # self.m_checkBox50.SetValue()


    def MountChange( self, event ):
        if self.m_checkBox45.GetValue() is True:
            self.m_checkBox11.SetValue(False)
            self.m_checkBox10.SetValue(True)
            self.m_checkBox10.Disable()
            self.m_checkBox50.Enable()
            # self.m_checkBox52.SetValue(False)
            # self.m_checkBox52.Disable()
            self.m_spinCtrl45.Enable()
        else:
            self.m_checkBox10.Enable()
            self.m_checkBox50.Disable()
            self.m_checkBox50.SetValue(False)
            self.m_spinCtrl45.Disable()
            # self.m_checkBox52.Enable()

    def AllDayClick( self, event ):
        self.m_checkBox22.SetValue(True)
        self.m_checkBox23.SetValue(False)
        self.m_checkBox24.SetValue(False)
        self.m_checkBox25.SetValue(False)
        self.m_checkBox26.SetValue(False)
        self.m_checkBox27.SetValue(False)
        self.m_checkBox28.SetValue(False)
        self.m_checkBox29.SetValue(False)

    def OneDayClick( self, event ):
        self.m_checkBox22.SetValue(False)

    def OnSize( self, event ):
        self.width, self.height = self.GetSize()
        # self.SetSize((self.width, self.height ))
        self.m_scrolledWindow3.SetMinSize((self.width*0.98, self.height*0.80))
        self.m_scrolledWindow3.SetSize((self.width*0.98, self.height * 0.80))
        self.Layout()

    def OnDirectBonus(self, event):
        self.m_checkBox10.SetValue(True)
        self.m_checkBox10.Hide()
        self.m_checkBox10.Enable()
        # self.m_checkBox11.SetValue(False)
        # self.m_checkBox11.Hide()
        # self.m_checkBox45.SetValue(False)
        # self.m_checkBox45.Hide()
        # self.m_checkBox50.Enable()
        # self.m_checkBox50.SetValue(False)
        # self.m_spinCtrl45.Enable()
        # self.m_checkBox131.SetValue(True)
        self.m_checkBox131.Show()

    def ShowOnLost(self, event):
        # self.m_checkBox11.Show()
        # self.m_checkBox45.Show()
        self.m_checkBox10.Show()
        self.m_checkBox11.Show()
        self.m_checkBox10.Enable()
        self.m_checkBox131.Show()

    def HideOnLost(self, event):
        self.m_checkBox11.Hide()
        # self.m_checkBox45.Hide()
        self.m_checkBox11.SetValue(False)
        # self.m_checkBox45.SetValue(False)
        self.m_checkBox10.Show()
        self.m_checkBox10.Enable()
        self.m_checkBox131.Show()
        self.m_checkBox131.SetValue(False)
        self.m_checkBox10.SetValue(True)
        # self.m_checkBox50.Disable()
        # self.m_checkBox50.SetValue(False)
        # self.m_spinCtrl45.Disable()

    def HideOptions( self, event ):
        if self.m_checkBox48.GetValue() is True:
            self.m_checkBox30.SetValue(False)
            self.m_checkBox30.Disable()
            self.m_checkBox131.SetValue(False)
            self.m_checkBox131.Disable()
            self.m_checkBox43.SetValue(False)
            self.m_checkBox43.Disable()
            self.m_spinCtrl23.SetValue(1)
            self.m_spinCtrl23.Disable()
        else:

            self.m_checkBox30.Enable()
            self.m_checkBox131.Enable()
            self.m_checkBox43.Enable()
            self.m_spinCtrl23.Enable()



    def _set_right(self):
        if self.user.grup.right != None:
            right = self.user.grup.from_json()
            if 3 in right['cust']:
                self.m_button1011.Show()
                self.m_radioBtn411.Show()
                self.m_button1011.Bind(wx.EVT_BUTTON, self.AddGroup)
                self._set_group()

            else:
                if self.edit != None:
                    if self.edit.use_group_conf is False or self.edit.forbiden is True:
                        raise GeneratorExit('Forbiden: %s, Use Group: %s' % (self.edit.forbiden, self.edit.use_group_conf))

                    self._set_group()
                    self.m_choice311.Disable()
                else:
                    self._set_group(True)

                self.m_radioBtn311.Disable()
                self.m_radioBtn411.Disable()
                self.m_checkBox13.Disable()
                self.m_checkBox59.Disable()


    def _set_group(self, selected=False):
        self.m_choice1Choices = ['']
        for item in sorted(list(self.parent.group_obj.keys())):
            if selected is False:
                self.m_choice1Choices.append(self.parent.group_obj[item].name)
            else:
                if self.parent.group_obj[item].selected is True:
                    self.m_choice1Choices.append(self.parent.group_obj[item].name)
        self.m_choice311.SetItems(self.m_choice1Choices)
    
    def _set_sity(self):
        self.sity = libs.DB.get_all(libs.models.Sity, order='name')
        self.m_choice2Choices = ['']
        self.user_sity = []
        if self.sity != None:
            for i in self.sity:
                self.m_choice2Choices.append(i.name)
                self.user_sity.append(i.id)
        self.m_choice211.SetItems(self.m_choice2Choices)
        
    def OnPicAdd(self, event):
        gui.AddCust.OnPicAdd(self, event)
        
    def AddGroup(self, event):
        dial = AddGrup(self, self.user)
        dial.ShowModal()
        self._set_group()
        
    def OnGo(self, event):

        try:
            grup = self.m_choice311.GetSelection()
            if grup > -1:
                group = self.m_choice311.GetString(self.m_choice311.GetSelection())
                group = libs.DB.get_one_where(libs.models.CustGrup, name=group)
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.SELECT_GROUP)
                dial.ShowModal()
                # libs.DB.rollback()
                # libs.DB.dispose()
                return
            if self.m_textCtrl20.GetValue() not in gui_lib.msg.COUNTRY_CODE:
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_COUNTRY_CODE)
                dial.ShowModal()
                return
            if self.m_textCtrl20.GetValue() == 'BGR' and self.m_checkBox13.GetValue() == False:
                if self.IsEGNValid(event, button_click=False) is not True:
                    return False
            if self.edit == None:
                if libs.DB.get_one_where(libs.models.CustUser, personal_egn=self.m_textCtrl1621.GetValue()):
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
                    dial.ShowModal()
                    return
                if libs.DB.get_one_where(libs.models.CustUser, name=self.m_textCtrl911.GetValue()):
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
                    dial.ShowModal()
                    return
                self.edit = libs.DB.make_obj(libs.models.CustUser)
                self.edit.pin = self.m_staticText421.GetLabel()
            else:
                libs.DB.expire(self.edit)


            # else:
            #     self.m_textCtrl1621.SetValue(self.m_textCtrl20.GetValue() + ': ' + self.m_textCtrl1721.GetValue())
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.user.id
            err.info = 'CUST USER CHANGE' + ': ' + u'%s from %s.' % (self.m_textCtrl911.GetValue(), self.user.name)
            libs.DB.add_object_to_session(err)
            self.edit.grup_id = group.id
            self.edit.name = self.m_textCtrl911.GetValue()
            self.edit.tel = self.m_textCtrl1011.GetValue()
            self.edit.e_mail = self.m_textCtrl1211.GetValue()
            self.edit.personal_cart_id = self.m_textCtrl1721.GetValue()
            self.edit.country_code = self.m_textCtrl20.GetValue()
            date = self.m_textCtrl18.GetValue()
            date = date.replace(',', '.')
            date = libs.models.TZ.str_to_date(date)
            date = libs.models.TZ.date_to_str(date, '%Y-%m-%d')
            self.edit.personal_cart_valid = date
            self.edit.personal_egn = self.m_textCtrl1621.GetValue()
            self.edit.personal_addres = self.m_textCtrl1811.GetValue()
            self.edit.man = self.m_checkBox601.GetValue()
            sity = self.m_choice211.GetSelection()
            # if sity == 1:
            #     self.edit.persona_sity_id = self.user_sity[0]
            if sity > 0:
                self.edit.persona_sity_id = self.user_sity[sity - 1]
            else:
                pass
                # dial = wx.MessageDialog(self, *gui_lib.msg.SELECT_SITY)
                # dial.ShowModal()
                # libs.DB.rollback()
                # libs.DB.dispose()
                # pass
            self.edit.forbiden = self.m_checkBox13.GetValue()
            self.edit.in_nra = self.m_checkBox59.GetValue()

            self.edit.use_group_conf = self.m_radioBtn311.GetValue()
            if self.edit.use_group_conf is True:
                self.edit.region_id = group.region_id
                self.edit.bonus_if_man = group.bonus_if_man
                self.edit.bonus_in_mony = group.bonus_in_mony
                self.edit.bonus_in_mony_sum = group.bonus_in_mony_sum
                self.edit.more_than_one_from_redirect = group.more_than_one_from_redirect
                self.edit.restricted_bonus = group.restricted_bonus
                self.edit.bonus_waith_for_in_mony = group.bonus_waith_for_in_mony

                self.edit.use_total_procent = group.use_total_procent
                self.edit.total_procent = group.total_procent

                self.edit.mony_back_min_pay = group.mony_back_min_pay
                self.edit.bonus_on_day = group.bonus_on_day
                self.edit.bonus_hold = group.bonus_hold
                self.edit.bonus_warning_use = group.bonus_warning_use
                self.edit.bonus_revert_by_bet = group.bonus_revert_by_bet
                self.edit.bonus_warning_mony = group.bonus_warning_mony
                self.edit.mony_back_use = group.mony_back_use
                self.edit.mony_back_pr = group.mony_back_pr
                self.edit.tombola_use = group.tombola_use
                self.edit.tombola_coef = group.tombola_coef
                self.edit.no_out_befor = group.no_out_befor
                self.edit.tombola_on_in = group.tombola_on_in
                self.edit.bonus_by_in = group.bonus_by_in
                self.edit.bonus_one_per_day = group.bonus_one_per_day
                self.edit.one_day_back_total = group.one_day_back_total
                self.edit.month_back = group.month_back
                self.edit.bonus_waith_for_in = group.bonus_waith_for_in
                self.edit.bonus_use = group.bonus_use
                self.edit.bonus_on_mony = group.bonus_on_mony
                self.edit.mony_back_pay = group.mony_back_pay
                self.edit.bonus_direct = group.bonus_direct
#                 self.edit.bonus_on_mony = group.bonus_on_mony
                self.edit.bonus_row = group.bonus_row
                # self.edit.x2 = group.x2
#                 self.edit.bonus_row_1_mony = group.bonus_row_1_mony
#                 self.edit.bonus_row_1_count = group.bonus_row_1_count
#                 self.edit.bonus_row_2_mony = group.bonus_row_2_mony
#                 self.edit.bonus_row_2_count = group.bonus_row_2_count
#                 self.edit.bonus_row_3_mony = group.bonus_row_3_mony
#                 self.edit.bonus_row_3_count = group.bonus_row_3_count
#                 self.edit.bonus_row_4_mony = group.bonus_row_4_mony
#                 self.edit.bonus_row_4_count = group.bonus_row_4_count
                
            else:
                if self.m_choice9.GetSelection() > 0:
                    self.edit.region_id = self.m_choice9.GetSelection()
                else:
                    self.edit.region_id = None
                if self.m_choice10.GetSelection() == 1:
                    self.edit.bonus_if_man = True
                elif self.m_choice10.GetSelection() == 2:
                    self.edit.bonus_if_man = False
                else:
                    self.edit.bonus_if_man = None
                self.edit.mony_back_use = self.m_checkBox111.GetValue()
                self.edit.more_than_one_from_redirect = self.m_checkBox52.GetValue()
                pr = self.m_textCtrl411.GetValue()
                pr = pr.replace(',', '.')
                pr = float(pr)
                self.edit.mony_back_pr = pr*0.01
                # self.edit.bonus_hold = self.m_checkBox30.GetValue()
                # self.m_checkBox30.SetValue(self.edit.grup.bonus_hold)
                if self.m_checkBox22.GetValue() is True:
                    self.edit.bonus_on_day = ''
                else:
                    bonus_on_day = []
                    if self.m_checkBox23.GetValue() is True:
                        bonus_on_day.append(0)
                    if self.m_checkBox24.GetValue() is True:
                        bonus_on_day.append(1)
                    if self.m_checkBox25.GetValue() is True:
                        bonus_on_day.append(2)
                    if self.m_checkBox26.GetValue() is True:
                        bonus_on_day.append(3)
                    if self.m_checkBox27.GetValue() is True:
                        bonus_on_day.append(4)
                    if self.m_checkBox28.GetValue() is True:
                        bonus_on_day.append(5)
                    if self.m_checkBox29.GetValue() is True:
                        bonus_on_day.append(6)
                    self.edit.bonus_on_day = json.dumps(bonus_on_day)

                self.edit.tombola_use = self.m_checkBox311.GetValue()
                t_coef = self.m_textCtrl511.GetValue()
                t_coef = t_coef.replace(',', '.')
                t_coef = float(t_coef)
                self.edit.tombola_coef = t_coef
                # self.m_checkBox48.SetValue(self.edit.grup.restricted_bonus)

                self.edit.use_total_procent = self.m_checkBox50.GetValue()
                self.edit.total_procent = self.m_spinCtrl45.GetValue()
                self.edit.bonus_in_mony = self.m_checkBox56.GetValue()
                self.edit.bonus_in_mony_sum = self.m_spinCtrl48.GetValue()
                self.edit.bonus_waith_for_in_mony = self.m_spinCtrl33.GetValue()
                self.edit.more_than_one_from_redirect = self.m_checkBox52.GetValue()
                self.edit.restricted_bonus = self.m_checkBox48.GetValue()
                self.edit.mony_back_min_pay = self.m_spinCtrl42.GetValue()
                self.edit.bonus_warning_use = self.m_checkBox41.GetValue()
                self.edit.bonus_warning_mony = self.m_spinCtrl40.GetValue()
                self.edit.bonus_revert_by_bet = self.m_checkBox43.GetValue()
                self.edit.tombola_on_in = self.m_radioBtn10.GetValue()
                self.edit.bonus_by_in = self.m_radioBtn211.GetValue()
                self.edit.bonus_one_per_day = self.m_checkBox10.GetValue()
                self.edit.one_day_back_total = self.m_checkBox11.GetValue()
                self.edit.month_back = self.m_checkBox45.GetValue()
                self.edit.no_out_befor = self.m_spinCtrl23.GetValue()
                self.edit.bonus_use = self.m_checkBox211.GetValue()
                self.edit.bonus_on_mony = self.m_spinCtrl14111.GetValue()

#                 self.edit.bonus_by_in = self.m_radioBtn211.GetValue()
#                 self.edit.bonus_row = self.m_spinCtrl2111.GetValue()
                self.edit.bonus_waith_for_in = self.m_checkBox131.GetValue()
                self.edit.bonus_row = json.dumps(self.bonus_row)
                # self.edit.x2 = self.m_checkBox60.GetValue()
                # self.edit.bonus_row_2_mony = self.m_spinCtrl141.GetValue()
                # self.edit.bonus_row_2_count = self.m_spinCtrl12.GetValue()
                # self.edit.bonus_row_3_mony = self.m_spinCtrl15.GetValue()
                # self.edit.bonus_row_3_count = self.m_spinCtrl13.GetValue()
                # self.edit.bonus_row_4_mony = self.m_spinCtrl16.GetValue()
                # self.edit.bonus_row_4_count = self.m_spinCtrl111.GetValue()
                self.edit.mony_back_pay = self.m_spinCtrl20.GetValue()
                self.edit.bonus_direct = self.m_radioBtn11.GetValue()
                # raise KeyError, self.edit.bonus_direct

            
            self.edit.pub_user_id = self.user.id
            libs.DB.add_object_to_session(self.edit)
            for i in self.cart:
                cart = libs.DB.get_one_where(libs.models.CustCart, catr_id=i)
                if cart == None:
                    obj = libs.DB.make_obj(libs.models.CustCart)
                    obj.catr_id = i
                    obj.user_id = self.edit.id
                    obj.pub_user_id = self.user.id
                    libs.DB.add_object_to_session(obj)
                elif cart.user_id == self.edit.id:
                    pass
                elif cart.user_id == None or cart.user_id == '':
                    cart.user_id = self.edit.id
                    libs.DB.add_object_to_session(cart)
                else:
                    # libs.DB.rollback()
                    dial = wx.MessageDialog(self, *gui_lib.msg.CART_IN_USE)
                    dial.ShowModal()
                    # return
            try:
                libs.DB.commit()
            except Exception as e:
                libs.DB.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                dial.ShowModal()
                return
            # else:

            # libs.DB.commit()
            self.OnClose(event)
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            libs.DB.rollback()
            return
        
    def OnGroupConf(self, event):
        if self.edit != None:
            self.edit.use_group_conf = self.m_radioBtn311.GetValue()
            if self.edit.use_group_conf is True:

                grup = self.m_choice311.GetSelection()
                try:
                    grup = self.parent.group_obj[(grup)+4]
                except KeyError:
                    dial = wx.MessageDialog(self, *gui_lib.msg.SELECT_GROUP)
                    dial.ShowModal()
                    return
                if grup.region_id:
                    self.m_choice9.SetSelection(grup.region_id)
                # print json.loads(grup.bonus_row), grup.name
                try:
                    self.bonus_row = json.loads(grup.bonus_row)
                except ValueError:
                    self.bonus_row = {}
                    grup.bonus_row = json.dumps({})
                    libs.DB.add_object_to_session(grup)
                    libs.DB.commit()
                # else:
                #     self.bonus_row = {}
                # self.m_button37.Hide()
                # self.m_button36.Hide()
                # self.m_checkBox60.SetValue(grup.x2)
                # self.m_checkBox60.Disable()
                if grup.bonus_on_day == '':
                    self.m_checkBox22.SetValue(True)
                    self.m_checkBox23.SetValue(False)
                    self.m_checkBox24.SetValue(False)
                    self.m_checkBox25.SetValue(False)
                    self.m_checkBox26.SetValue(False)
                    self.m_checkBox27.SetValue(False)
                    self.m_checkBox28.SetValue(False)
                    self.m_checkBox29.SetValue(False)
                else:
                    bonus_on_day = json.loads(grup.bonus_on_day)
                    self.m_checkBox22.SetValue(False)
                    if 0 in bonus_on_day:
                        self.m_checkBox23.SetValue(True)
                    if 1 in bonus_on_day:
                        self.m_checkBox24.SetValue(True)
                    if 2 in bonus_on_day:
                        self.m_checkBox25.SetValue(True)
                    if 3 in bonus_on_day:
                        self.m_checkBox26.SetValue(True)
                    if 4 in bonus_on_day:
                        self.m_checkBox27.SetValue(True)
                    if 5 in bonus_on_day:
                        self.m_checkBox28.SetValue(True)
                    if 6 in bonus_on_day:
                        self.m_checkBox29.SetValue(True)

                self.m_checkBox60.Disable()
                self.m_radioBtn311.SetValue(True)
                self.m_radioBtn411.SetValue(False)
                self.m_checkBox111.SetValue(grup.mony_back_use)
                self.m_textCtrl411.SetValue(str(grup.mony_back_pr/0.01))
                self.m_checkBox311.SetValue(grup.tombola_use)
                self.m_textCtrl511.SetValue(str(grup.tombola_coef))
                self.m_spinCtrl23.SetValue(grup.no_out_befor)
                
                self.m_checkBox211.SetValue(grup.bonus_use)
                self.m_spinCtrl14111.SetValue(grup.bonus_on_mony)
                self.m_radioBtn211.SetValue(grup.bonus_by_in)
#                 self.m_spinCtrl2111.SetValue(grup.bonus_row)
                    
                # self.m_spinCtrl131.SetValue(grup.bonus_row_1_mony)
                # self.m_spinCtrl11.SetValue(grup.bonus_row_1_count)
                # self.m_spinCtrl141.SetValue(grup.bonus_row_2_mony)
                # self.m_spinCtrl12.SetValue(grup.bonus_row_2_count)
                # self.m_spinCtrl15.SetValue(grup.bonus_row_3_mony)
                # self.m_spinCtrl13.SetValue(grup.bonus_row_3_count)
                # self.m_spinCtrl16.SetValue(grup.bonus_row_4_mony)
                # self.m_spinCtrl111.SetValue(grup.bonus_row_4_count)
        else:
            grup = self.m_choice311.GetSelection()
            try:
                grup = self.parent.group_obj[(grup)+4]
                try:
                    self.bonus_row = json.loads(grup.bonus_row)
                except ValueError:
                    self.bonus_row = {}
                    grup.bonus_row = json.dumps({})
                    libs.DB.add_object_to_session(grup)
                    libs.DB.commit()
                # else:
                #     self.bonus_row = {}
            except KeyError:
                dial = wx.MessageDialog(self, *gui_lib.msg.SELECT_GROUP)
                dial.ShowModal()
                return


            # self.m_button37.Hide()
            # self.m_button36.Hide()
            # self.m_checkBox60.SetValue(grup.x2)
            self.m_radioBtn311.SetValue(True)
            self.m_radioBtn411.SetValue(False)
            self.m_checkBox111.SetValue(grup.mony_back_use)
            self.m_textCtrl411.SetValue(str(grup.mony_back_pr/0.01))
            self.m_checkBox311.SetValue(grup.tombola_use)
            self.m_textCtrl511.SetValue(str(grup.tombola_coef))
            self.m_checkBox131.SetValue(grup.bonus_waith_for_in)
            self.m_checkBox211.SetValue(grup.bonus_use)
            self.m_spinCtrl14111.SetValue(grup.bonus_on_mony)
            self.m_radioBtn211.SetValue(grup.bonus_by_in)
#             self.m_spinCtrl2111.SetValue(grup.bonus_row)
            self.m_spinCtrl23.SetValue(grup.no_out_befor)
            # self.m_spinCtrl131.SetValue(grup.bonus_row_1_mony)
            # self.m_spinCtrl11.SetValue(grup.bonus_row_1_count)
            # self.m_spinCtrl141.SetValue(grup.bonus_row_2_mony)
            # self.m_spinCtrl12.SetValue(grup.bonus_row_2_count)
            # self.m_spinCtrl15.SetValue(grup.bonus_row_3_mony)
            # self.m_spinCtrl13.SetValue(grup.bonus_row_3_count)
            # self.m_spinCtrl16.SetValue(grup.bonus_row_4_mony)
            # self.m_spinCtrl111.SetValue(grup.bonus_row_4_count)
            # self.m_checkBox22.SetValue(False)
            if grup.bonus_on_day == '':
                self.m_checkBox22.SetValue(True)
                self.m_checkBox23.SetValue(False)
                self.m_checkBox24.SetValue(False)
                self.m_checkBox25.SetValue(False)
                self.m_checkBox26.SetValue(False)
                self.m_checkBox27.SetValue(False)
                self.m_checkBox28.SetValue(False)
                self.m_checkBox29.SetValue(False)
            else:
                bonus_on_day = json.loads(grup.bonus_on_day)
                self.m_checkBox22.SetValue(False)
                if 0 in bonus_on_day:
                    self.m_checkBox23.SetValue(True)
                if 1 in bonus_on_day:
                    self.m_checkBox24.SetValue(True)
                if 2 in bonus_on_day:
                    self.m_checkBox25.SetValue(True)
                if 3 in bonus_on_day:
                    self.m_checkBox26.SetValue(True)
                if 4 in bonus_on_day:
                    self.m_checkBox27.SetValue(True)
                if 5 in bonus_on_day:
                    self.m_checkBox28.SetValue(True)
                if 6 in bonus_on_day:
                    self.m_checkBox29.SetValue(True)
        self.refresh_bonus_row()

        
    def OnAddSity(self, event):
        dial = AddSity(self)
        dial.ShowModal()
        self._set_sity()
        
    def AddCart(self, event):
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        # if self.parent.GetParent().login.with_rfid_in is True:
        #     self.parent.GetParent().rfid_task_stop(None)
        dial = AddCart(self)
        dial.m_button8.SetLabel(gui_lib.msg.cust_main_AddCart_text[3])
        dial.ShowModal()
        # if self.parent.GetParent().login.with_rfid_in is True:
        #     self.parent.GetParent().rfid_task_start(None)
        if dial.cart != None and dial.cart is not False and dial.close==False:
            tmp = libs.DB.get_one_where(libs.models.CustCart, catr_id=dial.cart)
            if tmp is not None:
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
                dial.ShowModal()
                return
            self.cart.append(dial.cart)
            self.m_staticText42.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText42'] + ': ' + str(len(self.cart)))

        
    def OnDelCart(self, event):
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        # if self.parent.GetParent().login.with_rfid_in is True:
        #     self.parent.GetParent().rfid_task_stop(None)
        dial = AddCart(self)
        dial.m_button8.SetLabel(gui_lib.msg.cust_main_AddCart_text[4])
        dial.ShowModal()
        # dial.OnStop()
        # if self.parent.GetParent().login.with_rfid_in is True:
        #     self.parent.GetParent().rfid_task_start(None)
        if dial.cart != None and dial.cart is not False and dial.close==False:
            try:
                del self.cart[self.cart.index(dial.cart)]
                # try:
                libs.DB.delete_object(libs.DB.get_one_where(libs.models.CustCart, catr_id=dial.cart))
                libs.DB.commit()
                # except Exception as e:
                #     print(e)
                #     libs.log.stderr_logger.critical(e, exc_info=True)
                self.m_staticText42.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText42'] + ': ' + str(len(self.cart)))
            except ValueError:
                pass
            except Exception as e:
                libs.DB.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
    
    def OnDelAll(self, event):
        try:
            dlg = wx.MessageDialog(None, gui_lib.msg.cust_main_AddCust_button[1],gui_lib.msg.cust_main_AddCust_button[2],wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                if self.edit == None:
                    return
                cart = libs.DB.get_all_where(libs.models.CustCart, user_id=self.edit.id)
                for i in cart:
                    libs.DB.delete_object(i)
                libs.DB.commit()
                self.cart = []
                self.m_staticText42.SetLabel(gui_lib.msg.cust_main_AddCust_text['m_staticText42'] + ': ' + str(len(self.cart)))
            else:
                return
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            return
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.ALL_CART_DEL)
            dial.ShowModal()
            
    def OnClose(self, event):
        self.parent.add_cust()
        self.Destroy()

        
        
class ShowCust(gui.ShowCust):
    def __init__(self, parent, cust, day=False):
        gui.ShowCust.__init__(self, parent)
        self.parent = parent
        self.cust = cust
        self.day = day
        self.SetTitle(gui_lib.msg.cust_main_ShowCust_name)
        if self.cust.use_group_conf is True:
            self.m_staticText79.SetLabel(u'')
        else:
            self.m_staticText79.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText79'])
        self.m_staticText78.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText78'] + u': '+ cust.grup.name)
        self.m_staticText811.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText811'] + u': ' + str(cust.personal_egn))
        self.m_staticText58.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText58']+u': ')
        self.m_staticText60.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText60'] + u': ')
        self.m_staticText64.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText64'] + u': ')
        self.m_staticText80.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText80'] + u': ')
        self.m_staticText82.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText82'] + u': ')
        self.m_staticText86.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText86'] + u': ')
        self.m_staticText44.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText44'] + u': ')
        self.m_staticText46.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText46'] + u': ')
        self.m_staticText48.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText48'] + u': ')
        self.m_staticText50.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText50'] + u': ')
        self.m_staticText52.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText52'] + u': ')
        self.m_staticText581.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText581'] + u': ')
        self.m_staticText601.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText601'] + u': ')
        self.m_staticText641.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText641'] + u': ')
        self.m_staticText84.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText84'] + u': ')
        self.m_staticText90.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText90'] + u': ')
        self.m_staticText94.SetLabel(gui_lib.msg.cust_main_ShowCust_text['m_staticText94'] + u': ')
        self.m_button14.SetLabel(gui_lib.msg.cust_main_ShowCust_button['m_button14'])

        self.end_date = libs.models.TZ.now()
        if self.day is False:
            first = libs.models.TZ.go_to_first(self.end_date)

            # first = first.replace(day=2)
            first = libs.models.TZ.date_to_str(first, '%d.%m.%Y')
            self.start_date = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__gte=first, order='id', descs=False)
        else:
            self.start_date = libs.DB.get_one_where(libs.models.DayReport, day_report=True, descs=True, order='id')
        if self.start_date != None:
            self.start_date = self.start_date.pub_time
        else:
            self.start_date = libs.models.TZ.now()
        # print self.start_date
        
        self.m_staticText43.SetLabel(libs.models.TZ.date_to_str(self.start_date , '%d.%m.%Y')+'/' + libs.models.TZ.date_to_str(self.end_date , '%d.%m.%Y'))
        
        self.end_date  = libs.models.TZ.date_to_str(self.end_date , '%Y-%m-%d %H:%M:%S')
        self.start_date = libs.models.TZ.date_to_str(self.start_date , '%Y-%m-%d %H:%M:%S')
        
        
        self.m_staticText42.SetLabel(str(cust.name))
        statistic = libs.DB.get_all_where(libs.models.CustStatistic, order='id', cust_id=self.cust.id ,descs=True, pub_time__btw=(self.start_date, self.end_date))
        tmp = {'in':0, 'out':0, 'bill':0, 'game':0, 'bet':0}
        com_on_date = 0
        all_come = []
        like_mashin = {}

        bonus_sum = 0.0
        bonus = libs.DB.get_all_where(libs.models.BonusPay, order='id', cust_id=self.cust.id ,descs=True, pub_time__btw=(self.start_date, self.end_date))
        for i in bonus:
            bonus_sum += i.mony
        self.m_staticText85.SetLabel("{:.2f}".format(bonus_sum))
        if statistic != None and statistic != []:
            for i in statistic:
                tmp['in'] += i.ins + i.curent_credit_on_in
                tmp['out'] += i.out + i.curent_credit
                tmp['total'] = tmp['in'] - tmp['out']
                tmp['bill'] += i.bill
                tmp['game'] += i.game_played
                tmp['bet'] += i.bet
                if i.device_id not in like_mashin:
                    like_mashin[i.device_id] = 1
                else:
                    like_mashin[i.device_id] += 1
                if com_on_date == 0:
                    com_on_date = i.pub_time.day
                if i.pub_time.day not in all_come:
                    all_come.append(i.pub_time.day)
            self.m_staticText45.SetLabel("{:.2f}".format(tmp['in']))
            self.m_staticText47.SetLabel("{:.2f}".format(tmp['out']))
            self.m_staticText49.SetLabel("{:.0f}".format(tmp['bill']))
            self.m_staticText51.SetLabel("{:.0f}".format(tmp['game']))
            self.m_staticText95.SetLabel("{:.2f}".format(tmp['total']))
            if tmp['game'] > 0:
                self.m_staticText53.SetLabel("{:.2f}".format(tmp['bet'] / tmp['game']))
            else:
                self.m_staticText53.SetLabel(u'0')
        
        monyback = libs.DB.get_all_where(libs.models.MonuBackPay, cust_id=self.cust.id, pub_time__btw=(self.start_date, self.end_date))
        tmp = 0
        if monyback != [] and monyback != None:
            for i in monyback:
                tmp += i.mony
            self.m_staticText61.SetLabel("{:.2f}".format(tmp))
        else:
            self.m_staticText61.SetLabel(str(0))
        self.m_staticText59.SetLabel("{:.2f}".format(self.cust.total_mony_back))
        self.m_staticText65.SetLabel("{:.2f}".format(self.cust.total_mony_back+tmp))

        tmp = 0
        taloni = libs.DB.get_all_where(libs.models.TombulaPrinted, cust_id=self.cust.id, pub_time__btw=(self.start_date, self.end_date))
        if taloni != [] and taloni != None:
            for i in taloni:
                tmp+=i.tombula_count
            self.m_staticText611.SetLabel("{:.2f}".format(tmp))
            self.m_staticText591.SetLabel("{:.2f}".format(self.cust.total_tombula))
            self.m_staticText651.SetLabel("{:.2f}".format(self.cust.total_tombula+tmp))

        self.m_staticText81.SetLabel(str(com_on_date))
        self.m_staticText83.SetLabel(str(len(all_come)))
        if like_mashin != {}:
            like_mahin_tmp = max(list(like_mashin.values()))
            for i in like_mashin:
                if like_mashin[i] == like_mahin_tmp:
                    like_mashin = i
                    break
            like_mahin = libs.DB.get_one_where(libs.models.Device, id = like_mashin)
        else:
            like_mahin = None
        if like_mahin != None:
            self.m_staticText87.SetLabel(str(like_mahin.nom_in_l))
        else:
            self.m_staticText87.SetLabel(u'0')

        cart =  libs.DB.get_all_where(libs.models.CustCart, user_id=self.cust.id)
        if cart == None:
            self.m_staticText91.SetLabel(u'0')
        else:
            self.m_staticText91.SetLabel(str(len(cart)))
        self.Layout()

        
    def OnClose(self, event):
        self.Destroy()

class FreeTalon(gui.FreeTalon, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user):
        self.parent = parent
        self.user = user
        gui.FreeTalon.__init__(self, self.parent)
        self.SetTitle(gui_lib.msg.cust_main_FreeTalon_name)
        self.m_staticText81.SetLabel(gui_lib.msg.cust_main_FreeTalon_text['m_staticText81'])
        self.m_staticText82.SetLabel(gui_lib.msg.cust_main_FreeTalon_text['m_staticText82'])
        self.m_button22.SetLabel(gui_lib.msg.cust_main_FreeTalon_button['m_button22'])
        self.m_button23.SetLabel(gui_lib.msg.cust_main_FreeTalon_button['m_button23'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl25.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl13.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        tombula_count = self.m_spinCtrl25.GetValue()

        if libs.conf.POS_PRINTER_USE is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_POS_PRINTER)
            dial.ShowModal()
            return
        if libs.conf.PRINT_DIRECT_POS is True and libs.conf.DEFAULT_POS_PRINTER == '' and libs.conf.PRINT_ON_SERVER_POS==False:
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_POS_PRINTER)
            dial.ShowModal()
            return
        if libs.conf.POS_PRINTER_USE is True and tombula_count >= 1:
            name = self.m_textCtrl13.GetValue()
            name = name.replace('\n', ' ')
            obj = libs.DB.make_obj(libs.models.GetCounterError)
            obj.user_id = self.user.id
            obj.info = u'FREE Draw PRINT: ' + self.user.name + ' ' + name + ' ' + str(tombula_count)
            libs.DB.add_object_to_session(obj)
            try:
                libs.DB.commit()
            except Exception as e:
                libs.DB.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                return
            template = 'pos_print_tombula.html'

            dates = libs.models.TZ.now()
            dates = libs.models.TZ.date_to_str(dates)
            casino = libs.DB.get_one_where(libs.models.Config, name='pos_printer_info')
            if casino == None:
                object = u'None'
                sity = u'None'
                adress = u'None'
            else:
                casino = json.loads(casino.value)
                object = casino['object']
                sity = casino['sity']
                adress = casino['adress']
            # name = self.user.name
            for i in range(2, 10):
                name = name.replace(' ' * i, '')
            br_index = 0
            for i in name:
                if i == ' ':
                    br_index += 1
            name = name.replace(' ', '<br>')
            if br_index == 1:
                name += '<br>&nbsp;'
            elif br_index == 0:
                name += '<br>&nbsp;<br>&nbsp;'
            elif br_index == 3:
                name = name[0:-4]
            data = {'count': tombula_count, 'sity': sity, 'copy': False, 'object': object, 'adress': adress,
                    'name': name, 'dates': dates, 'ID': 0, 'len': len(name)}
            html = gui_lib.printer.render(template, data)
            if os.name == 'posix':
                tmp_folder = '/tmp/'
            else:
                tmp_folder = r'C:/Users/Public/'
            gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp2.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
            if libs.conf.PRINT_DIRECT_POS is True:
                gui_lib.printer.PDFPrint(tmp_folder + 'tmp2.pdf', default=libs.conf.DEFAULT_POS_PRINTER, pos=True)
            else:
                cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp2.pdf'
                os.system(cmd)
            # gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
            # gui_lib.printer.PDFPrint(tmp_folder + 'tmp.pdf', default=libs.conf.DEFAULT_POS_PRINTER)
            # dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_OK)
            # dlg.ShowModal()
            dlg = wx.MessageDialog(self, gui_lib.msg.cust_main_FreeTalon_text[1] , gui_lib.msg.cust_main_FreeTalon_text[2],
                                   wx.YES_NO | wx.ICON_WARNING)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                data = {'count': tombula_count, 'sity': sity, 'copy': True, 'object': object, 'adress': adress,
                        'name': name, 'dates': dates, 'ID': 0, 'len': len(name)}
                html = gui_lib.printer.render(template, data)
                if os.name == 'posix':
                    tmp_folder = '/tmp/'
                else:
                    tmp_folder = r'C:/Users/Public/'
                gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp2.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
                if libs.conf.PRINT_DIRECT_POS is True:
                    gui_lib.printer.PDFPrint(tmp_folder + 'tmp2.pdf', default=libs.conf.DEFAULT_POS_PRINTER, pos=True)
                else:
                    cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp2.pdf'
                    os.system(cmd)
                # gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
                # gui_lib.printer.PDFPrint(tmp_folder + 'tmp.pdf', default=libs.conf.DEFAULT_POS_PRINTER)
            self.OnClose(event)
            return

class CleanTalon(gui.AllUserEditByGroup):
    def __init__(self, parent, user, all_cust, group_name):
        self.group_name = group_name
        self.parent = parent
        self.user = user
        self.all_cust = all_cust
        gui.AllUserEditByGroup.__init__(self, parent)
        self.SetTitle(gui_lib.msg.cust_main_CleanTalon_name)
        self.m_button14.SetLabel(gui_lib.msg.cust_main_CleanTalon_button['m_button14'])
        self.m_gauge1.SetRange(len(self.all_cust))
        self.loop = 0
        self.worker = task.DellAllTalon(self, self.all_cust)  # @UndefinedVariable
        task.EVT_DEL_TALON(self, self.GetUserUpdate)
        self.error = 'ERROR'

    def GetUserUpdate(self, event):
        if type(event.data) == int:
            self.loop = self.loop + event.data
            self.m_gauge1.SetValue(self.loop)
        else:
            if event.data == 'DONE':
                self.error = event.data
                obj = libs.DB.make_obj(libs.models.GetCounterError)
                obj.user_id = self.user.id
                obj.info = u'CLEAN GROUP TALON: %s, %s' % (self.user.name, self.group_name)
                libs.DB.add_object_to_session(obj)
                try:
                    libs.DB.commit()
                    self.OnTaskStop(event)
                    dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                    dial.ShowModal()
                    # self.OnClose(event)
                except Exception as e:
                    print(e)
                    self.OnTaskStop(event)
                    libs.log.stderr_logger.critical(e, exc_info=True)
                    libs.DB.rollback()
                    dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                    dial.ShowModal()
                    return False
            elif event.data == 'ERROR':
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()

    def OnTaskStop(self, event):
        """Stop Computation."""
        try:
            self.worker.abort()
        except AttributeError:
            pass

    def OnClose(self, event):
        self.OnTaskStop(event)
        self.Destroy()

class ReplaceGroupRow(gui.ReplaceGroupRow):
    def __init__(self, parent, user):
        gui.ReplaceGroupRow.__init__(self, parent)
        self.SetTitle(gui_lib.msg.msg_ReplaceGroupRow['name'])
        self.m_button22.SetLabel(gui_lib.msg.msg_ReplaceGroupRow['m_button22'])
        self.m_listCtrl4.SetToolTip(gui_lib.msg.msg_ReplaceGroupRow['m_listCtrl4'])
        self.m_bpButton9.SetToolTip(gui_lib.msg.msg_ReplaceGroupRow['m_bpButton9'])
        self.m_bpButton10.SetToolTip(gui_lib.msg.msg_ReplaceGroupRow['m_bpButton10'])

        self.m_listCtrl4.InsertColumn(0, gui_lib.msg.msg_ReplaceGroupRow[1])
        self.m_listCtrl4.InsertColumn(1, gui_lib.msg.msg_ReplaceGroupRow[4])
        self.m_listCtrl4.InsertColumn(2, gui_lib.msg.msg_ReplaceGroupRow[5])
        self.m_listCtrl4.InsertColumn(3, gui_lib.msg.msg_ReplaceGroupRow[2])
        self.width, self.height = self.GetSize()
        self.m_listCtrl4.SetColumnWidth(0, self.width * 0.20)
        self.m_listCtrl4.SetColumnWidth(1, self.width * 0.25)
        self.m_listCtrl4.SetColumnWidth(2, self.width * 0.25)
        self.m_listCtrl4.SetColumnWidth(3, self.width * 0.30)
        self.user = user
        self.set_list()

    def OnClose( self, event ):
        self.Destroy()

    def set_list(self, event=None):
        self.m_listCtrl4.DeleteAllItems()
        my_row = libs.DB.get_one_where(libs.models.Config, name='replace_cust_group')
        if my_row != None:
            self.my_row = json.loads(my_row.value)
        else:
            self.my_row = {}
        index = 0
        for i in sorted(self.my_row):
            self.m_listCtrl4.InsertItem(index, i)
            self.m_listCtrl4.SetItem(index, 1, self.my_row[i]['from_group'])
            self.m_listCtrl4.SetItem(index, 2, self.my_row[i]['to_group'])
            if 'total' in self.my_row[i]:
                if self.my_row[i]['total'] is True:
                    self.m_listCtrl4.SetItem(index, 3, gui_lib.msg.msg_ReplaceGroupRow[3])
                else:
                    self.m_listCtrl4.SetItem(index, 3, '')
            else:
                self.m_listCtrl4.SetItem(index, 3, '')
            index +=1

    def OnAdd( self, event ):
        dial = NewGroupReplaceRight(self, self.user, self.my_row)
        dial.ShowModal()
        self.my_row = dial.all_row
        self.my_row = json.dumps(self.my_row)
        obj = libs.DB.get_one_where(libs.models.Config, name='replace_cust_group')
        if obj == None:
            obj = libs.DB.make_obj(libs.models.Config)
            obj.name = 'replace_cust_group'
        obj.value = self.my_row
        libs.DB.add_object_to_session(obj)
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            libs.DB.rollback()
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            return False
        self.set_list(event)

    def OnDel( self, event ):
        try:
            name = self.m_listCtrl4.GetItemText(self.m_listCtrl4.GetFirstSelected())
        except wx._core.PyAssertionError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return
        else:
            del self.my_row[name]
            obj = libs.DB.get_one_where(libs.models.Config, name='replace_cust_group')
            obj.value = json.dumps(self.my_row)
            libs.DB.add_object_to_session(obj)
            try:
                libs.DB.commit()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                libs.DB.rollback()
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                return False
            self.set_list(event)


    def OnEdit( self, event ):
        name = self.m_listCtrl4.GetItemText(self.m_listCtrl4.GetFirstSelected())
        dial = NewGroupReplaceRight(self, self.user, self.my_row, name)
        dial.ShowModal()
        self.my_row = dial.all_row
        self.my_row = json.dumps(self.my_row)
        obj = libs.DB.get_one_where(libs.models.Config, name='replace_cust_group')
        if obj == None:
            obj = libs.DB.make_obj(libs.models.Config)
            obj.name = 'replace_cust_group'
        obj.value = self.my_row
        libs.DB.add_object_to_session(obj)
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            libs.DB.rollback()
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            return False
        self.set_list(event)

class NewGroupReplaceRight(gui.NewGroupReplaceRight, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user, all_row, edit=False):
        gui.NewGroupReplaceRight.__init__(self, parent)
        self.SetTitle(gui_lib.msg.msg_NewGroupReplaceRight['name'])
        self.m_staticText83.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_staticText83'])
        self.m_staticText84.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_staticText84'])
        self.m_staticText85.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_staticText85'])
        self.m_checkBox41.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox41'])
        self.m_checkBox57.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox57'])

        self.m_checkBox43.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox43'])
        self.m_checkBox45.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox45'])
        self.m_checkBox47.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox47'])
        self.m_checkBox42.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox42'])
        self.m_checkBox44.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox44'])
        self.m_checkBox46.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox46'])
        self.m_checkBox49.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox49'])

        self.m_button24.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_button24'])
        self.m_button25.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_button25'])
        self.m_checkBox451.SetLabel(gui_lib.msg.msg_NewGroupReplaceRight['m_checkBox451'])
        self.m_spinCtrl411.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['m_spinCtrl411'])
        self.m_spinCtrl41.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['from_time'])
        self.m_spinCtrl45.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['from_time'])
        self.m_spinCtrl49.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['from_time'])
        self.m_spinCtrl53.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['from_time'])
        self.m_spinCtrl43.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['from_time'])
        self.m_spinCtrl47.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['from_time'])
        self.m_spinCtrl51.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['from_time'])

        self.m_spinCtrl42.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['to_time'])
        self.m_spinCtrl46.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['to_time'])
        self.m_spinCtrl50.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['to_time'])
        self.m_spinCtrl54.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['to_time'])
        self.m_spinCtrl44.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['to_time'])
        self.m_spinCtrl48.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['to_time'])
        self.m_spinCtrl52.SetToolTip(gui_lib.msg.msg_NewGroupReplaceRight['to_time'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl14.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_spinCtrl411.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

        self.all_row = all_row
        self.user = user
        if edit is False:
            self.edit=edit
            self.m_textCtrl14.Enable(True)
        else:
            self.edit = self.all_row[edit]
            self.m_textCtrl14.Enable(False)
            self.m_textCtrl14.SetValue(edit)
            my_wow_keys = list(self.edit['replace'].keys())
            # raise ValueError, my_wow_keys
            if 'total' in self.edit:
                # if self.edit['total'] is True:
                self.m_checkBox451.SetValue(self.edit['total'])
                self.m_spinCtrl411.SetValue(self.edit['total_mony'])
                # else:
                #     self.m_checkBox451.SetValue(False)
                #     self.m_spinCtrl411.SetValue(0)
            else:
                self.m_checkBox451.SetValue(False)
                self.m_spinCtrl411.SetValue(0)
            if "one_day_back" in self.edit:
                self.m_checkBox57.SetValue(self.edit['one_day_back'])
            else:
                self.m_checkBox57.SetValue(False)
            if 'ALL' in my_wow_keys:
                self.m_checkBox49.SetValue(True)
                self.OnClick(None)
            else:
                self.m_checkBox49.SetValue(False)
                self.OnClick(None)
                if '0' in my_wow_keys:
                    self.m_checkBox41.SetValue(True)
                    self.OnClick(None)
                    self.m_spinCtrl41.SetValue(self.edit['replace']['0']['from_time'])
                    self.m_spinCtrl42.SetValue(self.edit['replace']['0']['to_time'])
                if '1' in my_wow_keys:
                    self.m_checkBox43.SetValue(True)
                    self.OnClick(None)
                    self.m_spinCtrl45.SetValue(self.edit['replace']['1']['from_time'])
                    self.m_spinCtrl46.SetValue(self.edit['replace']['1']['to_time'])
                if '2' in my_wow_keys:
                    self.m_checkBox45.SetValue(True)
                    self.OnClick(None)
                    self.m_spinCtrl49.SetValue(self.edit['replace']['2']['from_time'])
                    self.m_spinCtrl50.SetValue(self.edit['replace']['2']['to_time'])
                if '3' in my_wow_keys:
                    self.m_checkBox47.SetValue(True)
                    self.OnClick(None)
                    self.m_spinCtrl53.SetValue(self.edit['replace']['3']['from_time'])
                    self.m_spinCtrl54.SetValue(self.edit['replace']['3']['to_time'])
                if '4' in my_wow_keys:
                    self.m_checkBox42.SetValue(True)
                    self.OnClick(None)
                    self.m_spinCtrl43.SetValue(self.edit['replace']['4']['from_time'])
                    self.m_spinCtrl44.SetValue(self.edit['replace']['4']['to_time'])
                if '5' in my_wow_keys:
                    self.m_checkBox44.SetValue(True)
                    self.OnClick(None)
                    self.m_spinCtrl47.SetValue(self.edit['replace']['5']['from_time'])
                    self.m_spinCtrl48.SetValue(self.edit['replace']['5']['to_time'])
                if '6' in my_wow_keys:
                    self.m_checkBox46.SetValue(True)
                    self.OnClick(None)
                    self.m_spinCtrl51.SetValue(self.edit['replace']['6']['from_time'])
                    self.m_spinCtrl52.SetValue(self.edit['replace']['6']['to_time'])

        self.load_group()
        self.OnEnable(None)

    def OnEnable( self, event ):
        if self.m_checkBox451.GetValue() is True:
            self.m_spinCtrl411.Enable()
            self.m_checkBox57.Enable()
        else:
            self.m_spinCtrl411.Disable()
            self.m_checkBox57.Disable()

    def OnSave( self, event ):
        # if self.edit is False:
        name = self.m_textCtrl14.GetValue()
        from_group = self.m_choice5.GetSelection()

        to_group = self.m_choice6.GetSelection()
        #
        if self.edit is False:
            if name in self.all_row:
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
                dial.ShowModal()
                return
        if name == u'' or from_group < 0 or to_group < 0:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        # raise KeyError, (from_group, to_group)
        row = {}
        # self.m_checkBox451.GetValue()
        # self.m_spinCtrl411.GetValue()
        if self.m_checkBox49.GetValue() is True:
            row['ALL'] = True
        elif (self.m_checkBox41.GetValue() is False and self.m_checkBox42.GetValue() is False and self.m_checkBox43.GetValue() is False and
            self.m_checkBox44.GetValue() is False and self.m_checkBox45.GetValue() is False and self.m_checkBox46.GetValue() is False and
            self.m_checkBox47.GetValue() is False):
            # raise KeyError
            row['ALL'] = True
        else:
            # row['ALL'] = True
            if self.m_checkBox41.GetValue() is True:
                if self.m_spinCtrl41.GetValue() > self.m_spinCtrl42.GetValue():
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                    dial.ShowModal()
                    return
                row['0'] = {'from_time':self.m_spinCtrl41.GetValue(), 'to_time':self.m_spinCtrl42.GetValue()}

            if self.m_checkBox43.GetValue() is True:
                if self.m_spinCtrl45.GetValue() > self.m_spinCtrl46.GetValue():
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                    dial.ShowModal()
                    return
                row['1'] = {'from_time':self.m_spinCtrl45.GetValue(), 'to_time':self.m_spinCtrl46.GetValue()}

            if self.m_checkBox45.GetValue() is True:
                if self.m_spinCtrl49.GetValue() > self.m_spinCtrl50.GetValue():
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                    dial.ShowModal()
                    return
                row['2'] = {'from_time':self.m_spinCtrl49.GetValue(), 'to_time':self.m_spinCtrl50.GetValue()}

            if self.m_checkBox47.GetValue() is True:
                if self.m_spinCtrl53.GetValue() > self.m_spinCtrl54.GetValue():
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                    dial.ShowModal()
                    return
                row['3'] = {'from_time':self.m_spinCtrl53.GetValue(), 'to_time':self.m_spinCtrl54.GetValue()}

            if self.m_checkBox42.GetValue() is True:
                if self.m_spinCtrl43.GetValue() > self.m_spinCtrl44.GetValue():
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                    dial.ShowModal()
                    return
                row['4'] = {'from_time':self.m_spinCtrl43.GetValue(), 'to_time':self.m_spinCtrl44.GetValue()}

            if self.m_checkBox44.GetValue() is True:
                if self.m_spinCtrl47.GetValue() > self.m_spinCtrl48.GetValue():
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                    dial.ShowModal()
                    return
                row['5'] = {'from_time':self.m_spinCtrl47.GetValue(), 'to_time':self.m_spinCtrl48.GetValue()}

            if self.m_checkBox46.GetValue() is True:
                if self.m_spinCtrl51.GetValue() > self.m_spinCtrl52.GetValue():
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                    dial.ShowModal()
                    return
                row['6'] = {'from_time':self.m_spinCtrl51.GetValue(), 'to_time':self.m_spinCtrl52.GetValue()}

        self.all_row[name] = {
                'from_group':self.m_choice5.GetStringSelection(),
                'to_group':self.m_choice6.GetStringSelection(),
                'replace':row,
                'total':self.m_checkBox451.GetValue(),
                'total_mony': self.m_spinCtrl411.GetValue(),
                'one_day_back': self.m_checkBox57.GetValue()
                }
        obj = libs.DB.make_obj(libs.models.GetCounterError)
        obj.user_id = self.user.id
        obj.info = u'USER %s SET GROUP REPLACE ROW NAME %s data: %s' % (self.user.name, name, json.dumps(self.all_row[name]))
        libs.DB.add_object_to_session(obj)
        try:
            libs.DB.commit()
            self.OnClose(event)
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
            dial.ShowModal()
            libs.DB.rollback()
            return

    def load_group(self):
        all_group = libs.DB.get_all(libs.models.CustGrup, order='name')
        data = []
        selection = None
        selection1 = None
        count = 0
        count1 = 0
        for i in all_group:
            if self.edit is not False:
                if i.name == self.edit['from_group']:
                    selection = count
                if i.name == self.edit['to_group']:
                    selection1 = count1
                count +=1
                count1+=1
            data.append(i.name)
        self.m_choice5.SetItems(data)
        self.m_choice6.SetItems(data)
        if self.edit is not False:
            self.m_choice5.SetSelection(selection)
            self.m_choice6.SetSelection(selection1)

    def OnClose( self, event ):
        self.Destroy()

    def OnClick( self, event ):
        if self.m_checkBox49.GetValue() is True:
            self.m_checkBox41.SetValue(False)
            self.m_checkBox43.SetValue(False)
            self.m_checkBox45.SetValue(False)
            self.m_checkBox47.SetValue(False)
            self.m_checkBox42.SetValue(False)
            self.m_checkBox44.SetValue(False)
            self.m_checkBox46.SetValue(False)
        if self.m_checkBox41.GetValue() is True:
            self.m_checkBox49.SetValue(False)
            self.m_spinCtrl41.Enable(True)
            self.m_spinCtrl42.Enable(True)
        else:
            self.m_spinCtrl41.Enable(False)
            self.m_spinCtrl42.Enable(False)

        if self.m_checkBox43.GetValue() is True:
            self.m_checkBox49.SetValue(False)
            self.m_spinCtrl45.Enable(True)
            self.m_spinCtrl46.Enable(True)
        else:
            self.m_spinCtrl45.Enable(False)
            self.m_spinCtrl46.Enable(False)

        if self.m_checkBox45.GetValue() is True:
            self.m_checkBox49.SetValue(False)
            self.m_spinCtrl49.Enable(True)
            self.m_spinCtrl50.Enable(True)
        else:
            self.m_spinCtrl49.Enable(False)
            self.m_spinCtrl50.Enable(False)

        if self.m_checkBox47.GetValue() is True:
            self.m_checkBox49.SetValue(False)
            self.m_spinCtrl53.Enable(True)
            self.m_spinCtrl54.Enable(True)
        else:
            self.m_spinCtrl53.Enable(False)
            self.m_spinCtrl54.Enable(False)

        if self.m_checkBox42.GetValue() is True:
            self.m_checkBox49.SetValue(False)
            self.m_spinCtrl43.Enable(True)
            self.m_spinCtrl44.Enable(True)
        else:
            self.m_spinCtrl43.Enable(False)
            self.m_spinCtrl44.Enable(False)

        if self.m_checkBox44.GetValue() is True:
            self.m_checkBox49.SetValue(False)
            self.m_spinCtrl47.Enable(True)
            self.m_spinCtrl48.Enable(True)
        else:
            self.m_spinCtrl47.Enable(False)
            self.m_spinCtrl48.Enable(False)

        if self.m_checkBox46.GetValue() is True:
            self.m_checkBox49.SetValue(False)
            self.m_spinCtrl51.Enable(True)
            self.m_spinCtrl52.Enable(True)
        else:
            self.m_spinCtrl51.Enable(False)
            self.m_spinCtrl52.Enable(False)


class ATM(gui.SetMonyOnUser):
    def __init__(self, parent, cust, user):
        self.user = user
        self.cust = cust
        self.parent = parent
        gui.SetMonyOnUser.__init__(self, self.parent)
        self.SetTitle(gui_lib.msg.cust_main_atm_name)
        self.m_staticText75.SetLabel(gui_lib.msg.cust_main_ATM_text['m_staticText75'] + ': ' + cust.name)
        self.m_button21.SetLabel(gui_lib.msg.cust_main_ATM_button['m_button21'])
        self.m_button20.SetLabel(gui_lib.msg.cust_main_ATM_button['m_button20'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl19.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

    def OnClose( self, event ):
        self.Destroy()

    def add_1( self, event ):
        self.m_spinCtrl19.SetValue(self.m_spinCtrl19.GetValue()+1)

    def add_10( self, event ):
        self.m_spinCtrl19.SetValue(self.m_spinCtrl19.GetValue() + 10)

    def add_100( self, event ):
        self.m_spinCtrl19.SetValue(self.m_spinCtrl19.GetValue() + 100)

    def del_last( self, event ):
        self.m_spinCtrl19.SetValue(0)

    def OnGo( self, event ):
        mony = self.m_spinCtrl19.GetValue()
        if self.user.grup.right != None:
            right = self.user.grup.from_json()
            if 7 not in right['cust']:
                return
        # self.cust.curent_mony += mony
        # libs.DB.add_object_to_session(self.cust)

        if mony == 0:
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_MONY_SET)
            dial.ShowModal()
            return False
        self.user.kasa -= mony

        obj = libs.DB.make_obj(libs.models.BankTransfer)
        obj.user_id = self.user.id
        obj.cust_id = self.cust.id
        obj.mony = mony
        obj.chk = False
        libs.DB.add_object_to_session(obj)
        libs.DB.add_object_to_session(self.user)


        try:
            libs.DB.commit()
            self.OnClose(event)
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            libs.DB.rollback()
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            return False


class Reserve(gui.Reserve, gui_lib.keybords.Keyboard):
    def __init__(self, parent, cust, user):
        self.parent = parent
        self.user = user
        self.cust = cust
        gui.Reserve.__init__(self, parent)
        self.SetTitle(gui_lib.msg.cust_reserve_class['name'])
        self.m_staticText85.SetLabel(gui_lib.msg.cust_reserve_class['m_staticText85'] % (self.cust.name))
        self.m_staticText86.SetLabel(gui_lib.msg.cust_reserve_class['m_staticText86'])
        self.m_staticText87.SetLabel(gui_lib.msg.cust_reserve_class['m_staticText87'])
        self.m_button25.SetLabel(gui_lib.msg.cust_reserve_class['m_button25'])
        self.m_button26.SetLabel(gui_lib.msg.cust_reserve_class['m_button26'])
        self.m_staticText89.SetLabel(gui_lib.msg.cust_reserve_class['m_staticText89'])
        self.m_textCtrl15.SetToolTip(gui_lib.msg.cust_reserve_class['m_textCtrl15t'])
        self.m_textCtrl16.SetToolTip(gui_lib.msg.cust_reserve_class['m_textCtrl16t'])
        my_date = libs.models.TZ.now()
        self.m_textCtrl15.SetValue(libs.models.TZ.date_to_str(my_date, '%d.%m.%Y'))
        self.m_textCtrl16.SetValue(libs.models.TZ.date_to_str(my_date, '%H:%M'))
        self.device = self.parent.GetParent().login.panel.mashinDict
        tmp = []
        for i in self.device:
            tmp.append(str(self.device[i].nom_in_l))
        self.m_choice6.SetItems(tmp)
        self.m_choice6.SetSelection(0)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl15.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl16.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        date = self.m_textCtrl15.GetValue()
        times = self.m_textCtrl16.GetValue()
        datetimes = date + ' ' + times
        try:
            libs.models.TZ.str_to_date(datetimes, '%d.%m.%Y %H:%M')
        except Exception:
            dlg = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dlg.ShowModal()
            return
        device = self.device[self.m_choice6.GetSelection()]
        libs.udp.send(libs.smib.SAS_F_METER_SINGLE, ip=device.ip, command=libs.smib.SAS_C_SINGLE_HALT)
        data = libs.udp.send('reserve_emg', ip=device.ip, datetime=datetimes, player_id=self.cust.id)
        if data is True:
            dlg = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dlg.ShowModal()
        else:
            dlg = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dlg.ShowModal()
        self.OnClose(event)

class Main(gui.MainCust, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        self.parent = parent
        self.parent.help_name = 'cust.html'
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.cust_main_Main_name[1])
        self.user = self.parent.USER
        gui.MainCust.__init__(self, self.parent)
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind( wx.EVT_SIZE, self.on_resize )
        self.m_listCtrl1.InsertColumn(0, gui_lib.msg.cust_main_Main_text[1])
        self.parent.login.worker = self.parent.login.worker
        self.m_listCtrl2.InsertColumn(0, gui_lib.msg.cust_main_Main_text[2])
        self.m_listCtrl2.InsertColumn(1, gui_lib.msg.cust_main_Main_text[3])
        self.m_listCtrl2.InsertColumn(2, gui_lib.msg.cust_main_Main_text[4])
        self.m_listCtrl2.InsertColumn(3, gui_lib.msg.cust_main_Main_text[5])
        self.m_listCtrl2.InsertColumn(4, gui_lib.msg.cust_main_Main_text[6])
        self.m_listCtrl2.InsertColumn(5, gui_lib.msg.cust_main_Main_text[7])
        self.m_listCtrl2.InsertColumn(6, gui_lib.msg.cust_main_Main_text[18])
        
        # if libs.conf.USE_VIRTUAL_KEYBORD is True:
        #     self.m_textCtrl5.Bind( wx.EVT_LEFT_UP, self.OnKeyboard )
        time_chk = libs.chk_time()
        if time_chk is not True:
            MyFrame = wx.MessageDialog(None, gui_lib.msg.bad_rtc_server+time_chk, gui_lib.msg.on_run_error, wx.OK| wx.ICON_ERROR)
            MyFrame.ShowModal()
            self.OnClose(None)
        self.Fit()
        self.add_right()
        self.search_choises()
        self.add_grup()
        self.add_cust(None)
        self.on_resize(None)
        
    def OnClose(self, event):
        self.parent.help_name = 'main.html'
        self.parent.show_panel()
        self.parent.panel_kasa_refresh()
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.cust_main_Main_name[2])
        self.Destroy()
    
    def add_grup(self):
        self.m_listCtrl1.DeleteAllItems()
        index = 5
        self.m_listCtrl1.InsertItem(0, gui_lib.msg.cust_main_Main_text[8])
        self.m_listCtrl1.InsertItem(1, gui_lib.msg.cust_main_Main_text[9])
        self.m_listCtrl1.InsertItem(2, gui_lib.msg.cust_main_Main_text[10])
        self.m_listCtrl1.InsertItem(3, gui_lib.msg.cust_main_Main_text[11])
        self.m_listCtrl1.InsertItem(4, gui_lib.msg.cust_main_Main_text[18])
        grup = libs.DB.get_all(libs.models.CustGrup, order='id')
        self.group_obj = {}
        self.my_grup_text = []
        for i in grup:
            self.m_listCtrl1.InsertItem(index, i.name)
            self.group_obj[index] = i
            self.my_grup_text.append(i.name)
            index += 1
    
    def add_cust(self, group=None, search=None):
        self.m_listCtrl2.DeleteAllItems()
        if search == None:
            if group == None or not group:
                cust = []
            elif group == gui_lib.msg.cust_main_Main_text[8]:
                cust = libs.DB.get_all(libs.models.CustUser, order='name')
            elif group == gui_lib.msg.cust_main_Main_text[9]:
                cust = libs.DB.get_all_where(libs.models.CustUser, forbiden=False, order='name')
            elif group == gui_lib.msg.cust_main_Main_text[10]:
                cust = libs.DB.get_all_where(libs.models.CustUser, forbiden=True, order='name')
            elif group == gui_lib.msg.cust_main_Main_text[11]:
                cust = libs.DB.get_all_where(libs.models.CustUser, use_group_conf=False, order='name')
            elif group == gui_lib.msg.cust_main_Main_text[18]:
                cust = libs.DB.get_all_where(libs.models.CustUser, in_nra=True, order='name')
            else:
                group = libs.DB.get_one_where(libs.models.CustGrup, name=group)
                cust=libs.DB.get_all_where(libs.models.CustUser, grup_id=group.id, order='name')
        else:
            cust = search
        self.custDict = {}
        index = 0
        for i in cust:
            self.m_listCtrl2.InsertItem(index, str(i.id))
            self.m_listCtrl2.SetItem(index, 1, str(i.name))
            self.m_listCtrl2.SetItem(index, 2, i.grup.name)
            self.m_listCtrl2.SetItem(index, 3, "{:.2f}".format(i.curent_mony))

            if i.forbiden is True:
                self.m_listCtrl2.SetItem(index, 4, str(gui_lib.msg.cust_main_Main_text[10]))
                self.m_listCtrl2.SetItemTextColour(
                    item=index, col=wx.Colour(199, 16, 29))
            else:
                self.m_listCtrl2.SetItem(index, 4, str(''))
                self.m_listCtrl2.SetItemTextColour(
                    item=index, col=wx.Colour(0, 135, 11))
            if i.use_group_conf is False:
                self.m_listCtrl2.SetItem(index, 5, str(gui_lib.msg.cust_main_Main_text['yes']))
                self.m_listCtrl2.SetItemTextColour(
                    item=index, col=wx.Colour(5, 0, 150))
            else:
                self.m_listCtrl2.SetItem(index, 5, '')
            if i.in_nra is True:
                self.m_listCtrl2.SetItem(index, 6, str(gui_lib.msg.cust_main_Main_text['yes']))
                self.m_listCtrl2.SetItemTextColour(
                    item=index, col=wx.Colour(255, 66, 223))
            else:
                self.m_listCtrl2.SetItem(index, 6, '')
            self.custDict[index] = i
            index += 1
            
    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        self.m_toolBar5.SetMinSize((self.width, -1))
        
        self.m_choice3.SetMinSize(((self.width*0.2, -1)))
        self.m_searchCtrl1.SetMinSize(((self.width*0.70, -1)))
        # self.m_button8.SetMinSize(((self.width*0.2, -1)))
        
        self.m_listCtrl1.SetMinSize((self.width*0.2, self.height * 0.65))
        self.m_listCtrl1.SetColumnWidth(0, self.width*0.19)
        
        self.m_listCtrl2.SetMinSize((self.width*0.75, self.height * 0.70))

        self.m_listCtrl2.SetColumnWidth(0, self.width * 0.06)
        self.m_listCtrl2.SetColumnWidth(1, self.width * 0.25)
        self.m_listCtrl2.SetColumnWidth(2, self.width * 0.10)
        self.m_listCtrl2.SetColumnWidth(3, self.width * 0.10)
        self.m_listCtrl2.SetColumnWidth(4, self.width * 0.08)
        self.m_listCtrl2.SetColumnWidth(5, self.width * 0.07)
        self.m_listCtrl2.SetColumnWidth(6, self.width * 0.10)
        self.m_listCtrl1.SetToolTip(gui_lib.msg.cust_main_Main_tooltip['m_listCtrl1'])
        self.m_listCtrl2.SetToolTip(gui_lib.msg.cust_main_Main_tooltip['m_listCtrl2'])
        self.m_searchCtrl1.SetToolTip(gui_lib.msg.cust_main_Main_tooltip['m_searchCtrl1'])
        
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height*0.95))
        if event != None:
            event.Skip() 
            self.Layout()

    def OnCHKnra( self, event ):
        egn = self.m_searchCtrl1.GetValue()
        if egn:
            forb = libs.udp.send('lk_set', ip=libs.conf.SERVER, EGN=egn, by_hand=True, user_id=self.user.id)
            if forb == 'CANT_PLAY':
                dial = wx.MessageDialog(self, *gui_lib.msg.CANT_PLAY)
                dial.ShowModal()
                return
            data = libs.udp.send('chk_nra', ip=libs.conf.SERVER, egn=egn)
            if data == True:
                dial = wx.MessageDialog(self, *gui_lib.msg.IN_NRA)
                dial.ShowModal()
            elif data == 'ERROR':
                dial = wx.MessageDialog(self, *gui_lib.msg.IN_NRA_ERROR)
                dial.ShowModal()
            else:
                # libs.udp.send('lk_set', ip=libs.conf.SERVER, EGN=egn)
                dial = wx.MessageDialog(self, *gui_lib.msg.NOT_IN_NRA)
                dial.ShowModal()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.EGN_IS_NOT_VALID)
            dial.ShowModal()

    def search_choises(self):
        self.m_choice3Choices = [
                                 gui_lib.msg.cust_main_Main_text[12],
                                 gui_lib.msg.cust_main_Main_text[13],
                                 gui_lib.msg.cust_main_Main_text[16],
                                 gui_lib.msg.cust_main_Main_text[14],
                                 gui_lib.msg.cust_main_Main_text[15],
                                 'ID',
                                 ]
        self.m_choice3.SetItems(self.m_choice3Choices)
        self.m_choice3.SetSelection(0)

    def PrintRKO(self, data):
        template = 'rko.html'
        data['my_copy'] = False
        html = gui_lib.printer.render(template, data)
        if os.name == 'posix':
            tmp_folder = '/tmp/'
        else:
            tmp_folder = r'C:/Users/Public/'
        gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp1.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
        if libs.conf.PRINT_DIRECT_POS is True:
            gui_lib.printer.PDFPrint(tmp_folder + 'tmp1.pdf', default=libs.conf.DEFAULT_POS_PRINTER, pos=True)
        else:
            cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp1.pdf'
            os.system(cmd)

    def commit(self):
        try:
            libs.DB.commit()
            return True
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()

    def PrintCustRKO(self, event):
        try:
            cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            libs.DB.expire()
            if libs.conf.PRINT_DIRECT_POS is True and libs.conf.DEFAULT_POS_PRINTER == '':
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_POS_PRINTER)
                dial.ShowModal()
                return
            casino = libs.DB.get_one_where(libs.models.Config, name='pos_printer_info')
            if casino == None:
                objects = gui_lib.msg.cust_main_TaloniPrint_text[9]
                sity = gui_lib.msg.cust_main_TaloniPrint_text[9]
                objects_adress = gui_lib.msg.cust_main_TaloniPrint_text[9]
            else:
                casino = json.loads(casino.value)
                objects = casino['object']
                sity = casino['sity']
                objects_adress = casino['adress']
            object_info = libs.DB.get_one_where(libs.models.Config, name='object_info')
            object_info = json.loads(object_info.value)
            self.start_date =  libs.DB.get_one_where(libs.models.CashOutPrinted, cust_id=cust.id, order='id', descs=True)
            if self.start_date == None:
                self.start_date = libs.DB.get_one_where(libs.models.DayReport, day_report=True, descs=True, order='id')
            if self.start_date != None:
                self.start_date = self.start_date.pub_time
            else:
                self.start_date = libs.models.TZ.now()

            self.end_date = libs.models.TZ.date_to_str(libs.models.TZ.now(), '%Y-%m-%d %H:%M:%S')
            self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
            # print self.start_date, self.end_date
            statistic = libs.DB.get_all_where(libs.models.CustStatistic, order='id', cust_id=cust.id, descs=True,
                                              pub_time__btw=(self.start_date, self.end_date))
            statistic_mony = 0

            if statistic != None:
                for i in statistic:
                    ins = i.ins + i.curent_credit_on_in
                    out = i.out + i.curent_credit
                    statistic_mony += ins-out
            # print statistic_mony
            if statistic_mony >= 0:
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_MONY_TO_PRINT)
                dial.ShowModal()
                return
            else:
                statistic_mony = statistic_mony*-1
            EIK = object_info['EIK']
            company = object_info['company']
            mony = "{:.2f}".format(statistic_mony)
            egn = cust.personal_egn
            cust_name = cust.name
            user_id = str(self.user.id)
            dates = libs.models.TZ.date_to_str(formats='%d.%m.%Y %H:%M:%S')
            id = libs.DB.get_one(libs.models.CashOutPrinted, order='id', descs=True)
            if id == None:
                ID = 1
            else:
                ID = id.id + 1
            ID = str(ID)
            ID = ('0' * (9 - len(ID))) + ID
            rko = libs.DB.make_obj(libs.models.CashOutPrinted)
            rko.mony = float(mony)
            rko.cust_id = cust.id
            rko.pub_user_id = self.user.id
            libs.DB.add_object_to_session(rko)
            if self.commit() is not True:
                return
            # cust_sity = cust.persona_sity.name
            if cust.persona_sity_id:
                cust_sity = cust.persona_sity.name
            else:
                cust_sity = ''
            cust_adress = cust.personal_addres
            data = {'company': company, 'EIK': EIK, 'objects': objects, 'sity': sity, 'objects_adress': objects_adress,
                    'name': cust_name, 'egn': egn, 'mony': [mony], 'user_id': user_id, 'ID': [ID], 'dates': dates,
                    'cust_sity': cust_sity,
                    'cust_adress': cust_adress, 'count':1}
            self.PrintRKO(data)
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.ADD_EIK)
            dial.ShowModal()

    def monyback_noCart(self, event):
        try:
            cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            libs.DB.expire()
            dial = MonyBackPay(self, self.user, cust=cust)
            dial.ShowModal()
            # self.commit()
            self.parent.login.panel.kasa_refresh()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()


    def atm_mony(self, event):
        try:
            cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            libs.DB.expire()
            dial = ATM(self, cust, self.user)
            dial.ShowModal()
            # self.commit()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()

    def talon_noCart(self, event):
        try:
            cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            libs.DB.expire()
            dial = TaloniPrint(self, self.user, cust=cust)
            dial.ShowModal()
            # self.commit()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()

    def SetReplaceRow(self, event):
        libs.DB.expire()
        dial = ReplaceGroupRow(self, self.user)
        dial.ShowModal()
        # self.commit()

    def CleanAllTalon(self, event):
        try:
            libs.DB.expire()
            group = self.group_obj[self.m_listCtrl1.GetFirstSelected()]
            all_user = libs.DB.get_all_where(libs.models.CustUser, grup_id=group.id, use_group_conf=True)
            dial = CleanTalon(self, self.user, all_user, group.name)
            dial.ShowModal()
            # self.commit()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()

    def OnCleanLostCart(self, event):
        try:
            cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            libs.DB.expire()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return
        start_date = libs.DB.get_one_where(libs.models.DayReport, day_report=True, descs=True, order='id')
        dial = SelectDate(self, start_date.pub_time)
        dial.ShowModal()
        if dial.close == True:
            return
        start_date = dial.start_date
        end_date = libs.models.TZ.now()
        if not start_date:
            start_date = libs.DB.get_one_where(libs.models.DayReport, day_report=True, descs=True, order='id')
            if start_date != None:
                start_date = start_date.pub_time
            else:
                start_date = libs.models.TZ.now()
        else:
            start_date = libs.DB.get_all_where(libs.models.DayReport, day_report=True, descs=True, order='id', pub_time__btw=(start_date.Format('%Y-%m-%d'), libs.models.TZ.date_to_str(end_date, '%Y-%m-%d %H:%M:%S')))[-1]
            start_date = start_date.pub_time
        end_date = libs.models.TZ.date_to_str(end_date, '%Y-%m-%d %H:%M:%S')
        start_date = libs.models.TZ.date_to_str(start_date, '%Y-%m-%d %H:%M:%S')
        statistic = libs.DB.get_all_where(libs.models.CustStatistic, order='id', cust_id=cust.id ,descs=True, pub_time__btw=(start_date, end_date))
        for i in statistic:
            libs.DB.delete_object(i)
            # i.curent_credit = 0
            # i.curent_credit_on_in = 0
            # libs.DB.add_object_to_session(i)
        obj = libs.DB.make_obj(libs.models.GetCounterError)
        obj.user_id = self.user.id
        obj.info = u'CART DELL CUST STATISTIC for user: %s' % (cust.name)
        libs.DB.add_object_to_session(obj)
        self.commit()
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()

    def add_right(self):
        self.m_toolBar5.ClearTools()
        self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnGrupFilter )
        self.popupmenu = wx.Menu()
        self.popupmenu1 = wx.Menu()
        if self.user.grup.right != None:
            right = self.user.grup.from_json()
            if 23 not in right['cust']:
                self.m_bpButton9.Hide()
            else:
                self.m_bpButton9.Show()
            if 18 in right['cust'] and libs.conf.POS_PRINTER_USE is True:
                item = self.popupmenu.Append(-1, gui_lib.msg.cust_print_rko)
                # self.popupmenu.SetHelpString(item.GetId(), u'test')
                self.Bind(wx.EVT_MENU, self.PrintCustRKO, item)
                self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenu)
            if 20 in right['cust']:
                rfid = self.popupmenu.Append(-1, gui_lib.msg.catd_copy)
                self.Bind(wx.EVT_MENU, self.Copy_Card, rfid)
                self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenu)
            if 9 in right['cust']:
                item2 = self.popupmenu.Append(-1, gui_lib.msg.curt_m_listCtrl2_monyback)
                # self.popupmenu.SetHelpString(item.GetId(), u'test')
                self.Bind(wx.EVT_MENU, self.monyback_noCart, item2)
                self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenu)
            if 10 in right['cust']:
                item3 = self.popupmenu.Append(-1, gui_lib.msg.curt_m_listCtrl2_talon)
                self.Bind(wx.EVT_MENU, self.talon_noCart, item3)
                self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenu)
            if 13 in right['cust']:
                item4 = self.popupmenu.Append(-1, gui_lib.msg.cust_atm)
                self.Bind(wx.EVT_MENU, self.atm_mony, item4)
                self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenu)
            if 17 in right['cust']:
                item5 = self.popupmenu.Append(-1, gui_lib.msg.cust_reserve)
                self.Bind(wx.EVT_MENU, self.reserve_emg, item5)
                self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenu)
            if 16 in right['cust']:
                item20 = self.popupmenu.Append(-1, gui_lib.msg.cust_cart_lost)
                self.Bind(wx.EVT_MENU, self.OnCleanLostCart, item20)
                self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenu)
            if 22 in right['cust']:
                cart_price_item = self.popupmenu1.Append(-1, gui_lib.msg.cart_price)
                self.Bind(wx.EVT_MENU, self.SetCartPrice, cart_price_item)
                self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenuGroup)

            if 11 in right['cust']:
                item10 = self.popupmenu1.Append(-1, gui_lib.msg.curt_del_all_talon)
                self.Bind(wx.EVT_MENU, self.CleanAllTalon, item10)
                self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenuGroup)
            if 12 in right['cust']:
                item11 = self.popupmenu1.Append(-1, gui_lib.msg.cust_group_replace_row)
                self.Bind(wx.EVT_MENU, self.SetReplaceRow, item11)
                self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenuGroup)
            if 19 in right['cust']:
                item12 = self.popupmenu1.Append(-1, gui_lib.msg.cust_del_group)
                self.Bind(wx.EVT_MENU, self.DelGrup, item12)
                self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenuGroup)
            if 1 in right['cust']:
                self.m_tool2 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.cust_main_Main_button['m_tool2'], wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/gnome-about-me.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.cust_main_Main_tooltip['m_tool2'], wx.EmptyString, None)

                self.Bind(wx.EVT_TOOL, self.OnAddCust, id=self.m_tool2.GetId())

            if 2 in right['cust']:
                self.m_tool9 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.cust_main_Main_button['m_tool9'], wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/User-Info-64.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.cust_main_Main_tooltip['m_tool9'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnEditCust, id=self.m_tool9.GetId())
            if 3 in right['cust']:
                self.m_tool3 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.cust_main_Main_button['m_tool3'], wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/system-users.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.cust_main_Main_tooltip['m_tool3'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnAddGrup, id=self.m_tool3.GetId())
                self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnEditGrup)
            if 21 in right['cust']:
                item3 = self.popupmenu1.Append(-1, gui_lib.msg.group_copy)
                self.Bind(wx.EVT_MENU, self.CopyGrup, item3)
                self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenuGroup)
            if 4 in right['cust']:
                self.m_tool4 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.cust_main_Main_button['m_tool4'], wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/Gnome-Emblem-Shared-64.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.cust_main_Main_tooltip['m_tool4'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnMonyBackPay, id=self.m_tool4.GetId())
            if 5 in right['cust']:
                self.m_tool5 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.cust_main_Main_button['m_tool5'], wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/Gnome-Emblem-Photos-64.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.cust_main_Main_tooltip['m_tool5'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnTalonPrint, id=self.m_tool5.GetId())
            if 8 in right['cust']:
                self.m_tool91 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.cust_main_Main_button['m_tool91'],
                                                             wx.Bitmap(
                                                                 libs.conf.IMG_FOLDER + u"64x64/Gnome-Printer-Printing-64.png",
                                                                 wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                             wx.ITEM_NORMAL, gui_lib.msg.cust_main_Main_tooltip['m_tool91'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.FreeTalon, id=self.m_tool91.GetId())
            if 6 in right['cust'] and libs.conf.RFID_USE_WORK is True:
                self.m_tool7 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.cust_main_Main_button['m_tool7'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/speedcrunch.png",
                                                                      wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.cust_main_Main_tooltip['m_tool7'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnMonyAdd, id=self.m_tool7.GetId())
            if 7 in right['cust']:
                self.m_tool8 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.cust_main_Main_button['m_tool8'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-Go-Jump-64.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.cust_main_Main_tooltip['m_tool8'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnPay, id=self.m_tool8.GetId())
            if 14 in right['cust']:
                self.m_listCtrl2.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnUserShow)
            elif 15 in right['cust']:
                self.m_listCtrl2.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnUserDayShow)




        self.m_tool1 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.cust_main_Main_button['m_tool1'], wx.Bitmap(
        libs.conf.IMG_FOLDER + u"64x64/dialog-error.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, gui_lib.msg.cust_main_Main_tooltip['m_tool1'], wx.EmptyString, None)
        self.Bind(wx.EVT_TOOL, self.OnClose, id=self.m_tool1.GetId())
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenu)
        # self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightMenuGroup)
        self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnGrupFilter )

        self.m_toolBar5.Realize()

    def CopyGrup(self, event):
        grup = self.m_listCtrl1.GetFirstSelected()
        grup = self.m_listCtrl1.GetItem(grup, col=0).GetText()
        if grup == gui_lib.msg.cust_main_Main_text[8]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        elif grup == gui_lib.msg.cust_main_Main_text[9]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        elif grup == gui_lib.msg.cust_main_Main_text[10]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        elif grup == gui_lib.msg.cust_main_Main_text[11]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        elif grup == gui_lib.msg.cust_main_Main_text[18]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            grup = libs.DB.get_one_where(libs.models.CustGrup, name=grup)
            dial = AddGrupNameForCopy(self, grup, self.user)
            dial.ShowModal()
            self.commit()

    def Copy_Card(self, event):
        try:
            # libs.DB.expire()
            try:
                cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            except KeyError:
                dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
                dial.ShowModal()
                return
            libs.DB.expire()
            my_row = libs.DB.get_one_where(libs.models.Config, name='cart_price')
            if my_row != None:
                my_row = json.loads(my_row.value)
            else:
                my_row = {}
                set_in_db = libs.DB.make_obj(libs.models.Config)
                set_in_db.name = 'cart_price'
                set_in_db.value = json.dumps(my_row)
                libs.DB.add_object_to_session(set_in_db)
                libs.DB.commit()
            if cust.grup.name in my_row:
                all_cust_cart = libs.DB.get_all_where(libs.models.CustCart, user_id=cust.id)
                if len(all_cust_cart) + 1 >= my_row[cust.grup.name]['count']:
                    gui_lib.msg.GET_MONY[0] = gui_lib.msg.GET_MONY[0] % {
                        'mony': "{:.2f}".format(my_row[cust.grup.name]['mony'])}
                    dial = wx.MessageDialog(self, *gui_lib.msg.GET_MONY)
                    dial.ShowModal()

            dial = AddCart(self)
            dial.cart = None
            dial.ShowModal()
            if dial.cart != None and dial.cart is not False and dial.close == False:
                cart = dial.cart
                if cart == False or cart == None:
                    return
                tmp = libs.DB.get_one_where(libs.models.CustCart, catr_id=cart)
                if tmp is not None:
                    dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
                    dial.ShowModal()
                    return
                obj = libs.DB.make_obj(libs.models.CustCart)
                obj.catr_id = cart
                obj.user_id = cust.id
                obj.pub_user_id = self.user.id
                libs.DB.add_object_to_session(obj)
                my_row = libs.DB.get_one_where(libs.models.Config, name='cart_price')
                if my_row != None:
                    my_row = json.loads(my_row.value)
                else:
                    my_row = {}
                    set_in_db = libs.DB.make_obj(libs.models.Config)
                    set_in_db.name = 'cart_price'
                    set_in_db.value = json.dumps(my_row)
                    libs.DB.add_object_to_session(set_in_db)
                if cust.grup.name in my_row:
                    libs.DB.commit()
                    all_cust_cart = libs.DB.get_all_where(libs.models.CustCart, user_id=cust.id)
                    if len(all_cust_cart) >= my_row[cust.grup.name]['count']:
                        reson = libs.DB.get_one_where(libs.models.PrihodType, name=u'Cust Cart')
                        if reson == None:
                            pr_type = libs.DB.make_obj(libs.models.PrihodType)
                            pr_type.name = u'Cust Cart'
                            pr_type.hiden = True
                            libs.DB.add_object_to_session(pr_type)
                            libs.DB.commit()
                            reson = libs.DB.get_one_where(libs.models.PrihodType, name=u'Cust Cart')
                        self.user.kasa += round(my_row[cust.grup.name]['mony'], 2)
                        obj = libs.DB.make_obj(libs.models.Prihod)
                        obj.mony = round(my_row[cust.grup.name]['mony'], 2)
                        obj.user_id = self.user.id
                        obj.info = 'system'
                        obj.reson_id = reson.id
                        libs.DB.add_object_to_session(obj)
                        # gui_lib.msg.GET_MONY[0] = gui_lib.msg.GET_MONY[0] % {'mony':"{:.2f}".format(my_row[cust.grup.name]['mony'])}
                        # dial = wx.MessageDialog(self, *gui_lib.msg.GET_MONY)
                        # dial.ShowModal()

                log = libs.DB.make_obj(libs.models.GetCounterError)
                log.user_id = self.user.id
                log.info = gui_lib.msg.catd_copy + (u': %s' % (cust.name))
                libs.DB.add_object_to_session(log)
                libs.DB.commit()
            # else:
            #     return
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA_OR_EXIST)
            dial.ShowModal()
            libs.DB.rollback()
            return

    def DelGrup(self, event):
        # libs.DB.expire()
        grup = self.m_listCtrl1.GetFirstSelected()
        grup = self.m_listCtrl1.GetItem(grup, col=0).GetText()
        if grup == gui_lib.msg.cust_main_Main_text[8]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        elif grup == gui_lib.msg.cust_main_Main_text[9]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        elif grup == gui_lib.msg.cust_main_Main_text[10]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        elif grup == gui_lib.msg.cust_main_Main_text[11]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        elif grup == gui_lib.msg.cust_main_Main_text[18]:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            grup = libs.DB.get_one_where(libs.models.CustGrup, name=grup)
            have_user = libs.DB.get_one_where(libs.models.CustUser, grup_id=grup.id)
            if have_user != None:
                dial = wx.MessageDialog(self, *gui_lib.msg.GRUP_HAVE_USER)
                dial.ShowModal()
            else:
                dlg = wx.MessageDialog(self, gui_lib.msg.cust_main_Main_text['text_del_grup'], gui_lib.msg.cust_del_group, wx.YES_NO | wx.ICON_WARNING)
                result = dlg.ShowModal()
                if result == wx.ID_YES:
                    redirect = libs.DB.get_one_where(libs.models.Config, name='replace_cust_group')
                    if redirect is not None:
                        my_row = json.loads(redirect.value)
                        for i in list(my_row.keys()):
                            if my_row[i]['from_group']==grup.name or my_row[i]['to_group'] == grup.name:
                                del my_row[i]
                        my_row = json.dumps(my_row)
                        redirect.value = my_row
                        libs.DB.add_object_to_session(redirect)
                    libs.DB.delete_object(grup)
                    self.commit()
                    self.add_grup()
                else:
                    pass



    def reserve_emg(self, event):
        try:
            cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            libs.DB.expire()
            dial = Reserve(self, cust, self.user)
            dial.ShowModal()
            # self.commit()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()

    def RightMenu(self, event):
        # def RightMenu(self, event):
            # try:
        position = self.ScreenToClient(wx.GetMousePosition())
        self.PopupMenu(self.popupmenu, position)
            # except Exception as e:
            #     print(e)
            #     libs.log.stderr_logger.critical(e, exc_info=True)

    def RightMenuGroup(self, event):
        position = self.ScreenToClient(wx.GetMousePosition())
        self.PopupMenu(self.popupmenu1, position)

    def SetCartPrice(self, event):
        libs.DB.expire()
        dial = CartPrice(self)
        dial.ShowModal()
        # self.commit()

    def FreeTalon( self, event ):
        libs.DB.expire()
        dial = FreeTalon(self, self.user)
        dial.ShowModal()
        # self.commit()

    def OnPay(self, event):
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        libs.DB.expire()
        dial = PayMony(self, self.user)
        dial.ShowModal()
        # self.commit()
        
    def OnMonyAdd(self,event):
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        libs.DB.expire()
        dial = SetMonyOnUserCart(self, self.user)
        dial.ShowModal()
        # self.commit()
        return

    
    def OnMonyBackPay(self, event):
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        libs.DB.expire()
        dial = MonyBackPay(self, self.user)
        dial.ShowModal()
        self.parent.login.panel.kasa_refresh()
        # self.commit()

    def OnTalonPrint(self, event):
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        libs.DB.expire()
        dial = TaloniPrint(self, self.user)
        dial.ShowModal()
        # self.commit()
    
    def OnAddGrup(self, event):
        libs.DB.expire()
        dial = AddGrup(self, self.user)
        dial.ShowModal()
        # self.commit()
    
    def OnEditGrup(self, event):
        try:
            group = self.group_obj[self.m_listCtrl1.GetFirstSelected()]
            libs.DB.expire()
            dial = AddGrup(self, self.user, group)
            dial.ShowModal()
            # self.commit()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        except GeneratorExit as e:
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_HAVE_RIGHT)
            dial.ShowModal()


        
    def OnAddCust(self, event):
        libs.DB.expire()
        dial = AddCust(self, self.user)
        dial.ShowModal()
        # self.commit()
    
    def OnEditCust(self, event):
        try:
            cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            libs.DB.expire(cust)
            dial = AddCust(self, self.user, cust)
            dial.ShowModal()
            # self.commit()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
    
    def OnSearch(self, event):
        sort_by = self.m_choice3.GetString(self.m_choice3.GetSelection())
        if sort_by == gui_lib.msg.cust_main_Main_text[12]:
            search = libs.DB.get_all_where_sort_bylike(libs.models.CustUser, name=self.m_searchCtrl1.GetValue())
        elif sort_by == gui_lib.msg.cust_main_Main_text[14]:
            search = libs.DB.get_all_where_sort_bylike(libs.models.CustUser, tel=self.m_searchCtrl1.GetValue())
        elif sort_by == gui_lib.msg.cust_main_Main_text[16]:
            search = libs.DB.get_all_where_sort_bylike(libs.models.CustUser, personal_cart_id=self.m_searchCtrl1.GetValue())
        elif sort_by == gui_lib.msg.cust_main_Main_text[15]:
            search = libs.DB.get_all_where_sort_bylike(libs.models.CustUser, e_mail=self.m_searchCtrl1.GetValue())
        elif sort_by == gui_lib.msg.cust_main_Main_text[13]:
            search = libs.DB.get_all_where_sort_bylike(libs.models.CustUser, personal_egn=self.m_searchCtrl1.GetValue())
        elif sort_by == 'ID':
            search = libs.DB.get_all_where(libs.models.CustUser, id=int(self.m_searchCtrl1.GetValue()))
        self.add_cust(search=search)

    def OnGrupFilter(self, event):
        grup = self.m_listCtrl1.GetFirstSelected()
        grup = self.m_listCtrl1.GetItem(grup, col=0).GetText()
        self.add_cust(group=grup)

    def OnUserDayShow(self, event, user=None):
        try:
            cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            libs.DB.expire()
            dial = ShowCust(self, cust, day=True)
            dial.ShowModal()
            # self.commit()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()

    def OnUserShow(self, event, user=None):
        try:
            cust = self.custDict[self.m_listCtrl2.GetFirstSelected()]
            libs.DB.expire()
            dial = ShowCust(self, cust, day=False)
            dial.ShowModal()
            # self.commit()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()

class CartPrice(gui.ReplaceGroupRow):
    def __init__(self, parent):
        gui.ReplaceGroupRow.__init__(self, parent)
        # if libs.conf.DEBUG is False:
        #     dial = wx.MessageDialog(self, *gui_lib.msg.IN_DEBUG_MOD)
        #     dial.ShowModal()
        #     return

        self.SetTitle(gui_lib.msg.cust_cart_price['title'])
        self.m_listCtrl4.InsertColumn(0, gui_lib.msg.cust_cart_price[1])
        self.m_listCtrl4.InsertColumn(1, gui_lib.msg.cust_cart_price[2])
        self.m_listCtrl4.InsertColumn(2, gui_lib.msg.cust_cart_price[3])
        self.width, self.height = self.GetSize()
        self.m_listCtrl4.SetColumnWidth(0, self.width * 0.50)
        self.m_listCtrl4.SetColumnWidth(1, self.width * 0.15)
        self.m_listCtrl4.SetColumnWidth(2, self.width * 0.30)
        self.set_list(None)

    def set_list(self, event=None):
        self.m_listCtrl4.DeleteAllItems()
        my_row = libs.DB.get_one_where(libs.models.Config, name='cart_price')
        if my_row != None:
            self.my_row = json.loads(my_row.value)
        else:
            self.my_row = {}
            set_in_db = libs.DB.make_obj(libs.models.Config)
            set_in_db.name = 'cart_price'
            set_in_db.value = json.dumps(self.my_row)
            libs.DB.add_object_to_session(set_in_db)
            try:
                libs.DB.commit()
            except Exception as e:
                libs.DB.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()

        index = 0
        for i in sorted(self.my_row):
            self.m_listCtrl4.InsertItem(index, i)
            self.m_listCtrl4.SetItem(index, 1, str(self.my_row[i]['count']))
            self.m_listCtrl4.SetItem(index, 2, "{:.2f}".format(self.my_row[i]['mony']))
            index += 1

    def OnClose( self, event ):
        self.Destroy()

    def OnDel( self, event ):
        try:
            name = self.m_listCtrl4.GetItemText(self.m_listCtrl4.GetFirstSelected())
        except wx._core.PyAssertionError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return

        my_row = libs.DB.get_one_where(libs.models.Config, name='cart_price')
        value = json.loads(my_row.value)
        del value[name]
        my_row.value = json.dumps(value)
        libs.DB.add_object_to_session(my_row)
        try:
            libs.DB.commit()
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            return
        self.set_list(event)

    def OnEdit( self, event ):
        name = self.m_listCtrl4.GetItemText(self.m_listCtrl4.GetFirstSelected())
        dial = SetCartPrice(self, edit=self.my_row[name])
        dial.ShowModal()
        self.set_list(event)

    def OnAdd( self, event ):
        dial = SetCartPrice(self)
        dial.ShowModal()
        self.set_list(event)

class SetCartPrice(gui.SetCartPrice, gui_lib.keybords.Keyboard):
    def __init__(self, parent, edit=False):
        gui.SetCartPrice.__init__(self, parent)
        self.parent = parent
        self.SetTitle(gui_lib.msg.cust_SetCartPrice['title'])
        self.m_staticText91.SetLabel(gui_lib.msg.cust_SetCartPrice['m_staticText91'])
        self.m_staticText92.SetLabel(gui_lib.msg.cust_SetCartPrice['m_staticText92'])
        self.m_staticText93.SetLabel(gui_lib.msg.cust_SetCartPrice['m_staticText93'])
        self.m_button27.SetLabel(gui_lib.msg.cust_SetCartPrice['m_button27'])
        self.m_button28.SetLabel(gui_lib.msg.cust_SetCartPrice['m_button28'])
        self.edit = edit
        if self.edit is not False:
            self.m_spinCtrl46.SetValue(int(self.edit['count']))
            self.m_textCtrl18.SetValue(str(self.edit['mony']))
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl46.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl18.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
        self.load_group()
        self.Fit()

    def load_group(self):
        all_group = libs.DB.get_all(libs.models.CustGrup, order='name')
        self.data = []
        selection = None
        count = 0
        for i in all_group:
            if self.edit is not False:
                if i.name == self.edit['name']:
                    selection = count
                count += 1
            self.data.append(i.name)
        self.m_choice7.SetItems(self.data)
        if self.edit is not False:
            self.m_choice7.SetSelection(selection)

    def OnGo( self, event ):
        group = self.m_choice7.GetStringSelection()
        if not group:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        if group in list(self.parent.my_row.keys()) and self.edit is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
            dial.ShowModal()
            return
        mony = self.m_textCtrl18.GetValue()
        mony = mony.replace(',', '.')
        try:
            mony = float(mony)
        except ValueError:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        count = self.m_spinCtrl46.GetValue()
        my_row = libs.DB.get_one_where(libs.models.Config, name='cart_price')
        data = json.loads(my_row.value)
        data[group] = {'count':count, 'mony':mony, 'name':group}
        my_row.value = json.dumps(data)
        libs.DB.add_object_to_session(my_row)
        try:
            libs.DB.commit()
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            return
        self.OnClose(event)

    def OnClose( self, event ):
        self.Destroy()

class AddBonus(gui.SetCartPrice):
    def __init__(self, parent, edit=None):
        self.parent = parent
        self.edit = edit
        gui.SetCartPrice.__init__(self, self.parent)
        self.m_staticText92.Hide()
        self.m_choice7.Hide()
        self.m_staticText91.SetLabel(gui_lib.msg.cust_main_AddGrup_text['count'])
        self.m_staticText93.SetLabel(gui_lib.msg.cust_main_AddGrup_text['mony'])
        self.m_button27.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_button4'])
        self.m_button28.SetLabel(gui_lib.msg.cust_main_AddGrup_button['m_button5'])
        self.SetTitle(gui_lib.msg.cust_main_AddGrup_button['m_checkBox2'])
        self.close = True
        if self.edit:
            self.m_spinCtrl46.SetValue(self.edit[1])
            self.m_textCtrl18.SetValue(str(self.edit[0]))
        else:
            self.m_spinCtrl46.SetValue(1)
        self.Fit()

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):

        if self.m_spinCtrl46.GetValue() < 1:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        d = self.m_textCtrl18.GetValue()
        try:
            d = float(d.replace(',', '.'))
            d = "{:.2f}".format(d)
        except:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        self.close = False
        self.edit = [d, self.m_spinCtrl46.GetValue()]
        self.OnClose(None)


class SelectDate(gui.SelectDate):
    def __init__(self, parent, date):
        self.parent = parent
        gui.SelectDate.__init__(self, self.parent)
        self.SetTitle(gui_lib.msg.SelectDate_Cust_statistic_DEL['name'])
        self.m_button41.SetLabel(gui_lib.msg.SelectDate_Cust_statistic_DEL['m_button41'])
        self.m_button42.SetLabel(gui_lib.msg.SelectDate_Cust_statistic_DEL['m_button42'])
        self.close = True
        self.start_date = None
        self.m_calendar3.SetDate(date)
        self.Fit()

    def OnClose(self, event):
        self.close = True
        self.Destroy()

    def OnGo( self, event ):
        self.close = False
        self.start_date = self.m_calendar3.GetDate()
        self.Destroy()