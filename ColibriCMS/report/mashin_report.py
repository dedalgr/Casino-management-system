#-*- coding:utf-8 -*-
'''
Created on 2.11.2017 г.

@author: dedal
'''
import wx
import libs
from . import gui
import gui_lib
from . import task
import datetime
import os
import json
from . import cust_report

class BonusLock(gui.RealTimeLock):
    def __init__(self, parent):
        self.parent = parent
        gui.RealTimeLock.__init__(self, parent)
        self.m_button20.SetLabel(gui_lib.msg.mashin_report_BonusLock['m_button20'])
        hold_bonus = libs.DB.get_one_where(libs.models.Config, name='bonus_cart_hold').value

        row = libs.DB.get_all_where(libs.models.BonusCartLog,  
                                                       user_id=None,
                                                       descs=True
                                                       )
        row2 = libs.DB.get_all_where(libs.models.ClienBonusHold,
                                                       user_id=None,
                                                       descs=True
                                                       )
        row3 = libs.DB.get_all_where(libs.models.BonusPay,
                                     last=True, descs=True
                                     )

        for i in row2:
            row.append(i)

        for i in row3:
            row.append(i)

        col = [gui_lib.msg.mashin_report_BonusLock[1],
               gui_lib.msg.mashin_report_BonusLock[2],
               gui_lib.msg.mashin_report_BonusLock[3],
               gui_lib.msg.mashin_report_BonusLock[4],
               gui_lib.msg.mashin_report_BonusLock[9],
               gui_lib.msg.mashin_report_BonusLock[5],
               gui_lib.msg.mashin_report_BonusLock[11],
               gui_lib.msg.mashin_report_BonusLock[6],
               gui_lib.msg.mashin_report_BonusLock[7]]
        index = 0
        for i in col:
            self.m_listCtrl3.InsertColumn(index, i)
            index += 1
        sums = [u'',u'',u'', u'', u'', gui_lib.msg.mashin_report_BonusLock[8], 0, 0]
        index = 0
        for i in row:
            self.m_listCtrl3.InsertItem(index, str(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S')))
            try:
                self.m_listCtrl3.SetItem(index, 1, str(i.cart.name))
            except AttributeError:
                try:
                    self.m_listCtrl3.SetItem(index, 1, str(i.cust.name))
                except AttributeError:
                    self.m_listCtrl3.SetItem(index, 1, str(''))
            # self.m_listCtrl3.SetItem(index, 2, str(i.user.name))
            try:
                self.m_listCtrl3.SetItem(index, 2, str(i.mashin.nom_in_l))
                self.m_listCtrl3.SetItem(index, 3, str(i.mashin.model.name))
            except AttributeError:
                self.m_listCtrl3.SetItem(index, 2, str(i.device.nom_in_l))
                self.m_listCtrl3.SetItem(index, 3, str(i.device.model.name))
            try:
                self.m_listCtrl3.SetItem(index, 4, str(i.cust.name))
            except AttributeError:
                try:
                    self.m_listCtrl3.SetItem(index, 4, str(i.cart.name))
                except AttributeError:
                    self.m_listCtrl3.SetItem(index, 4, '')
            try:
                if i.bonus_hold is True:
                    self.m_listCtrl3.SetItem(index, 5, gui_lib.msg.mashin_report_BonusLock[5])
                else:
                    self.m_listCtrl3.SetItem(index, 5, str(''))
                self.m_listCtrl3.SetItem(index, 6, str(''))
                if i.bonus_hold is True and hold_bonus == 'True':
                    self.m_listCtrl3.SetItem(index, 7, "{:.2f}".format(i.bonus))
                    self.m_listCtrl3.SetItem(index, 8, "{:.2f}".format(i.bonus))
                    sums[6] = sums[6] + i.bonus
                    sums[7] = sums[7] + i.bonus
                else:
                    self.m_listCtrl3.SetItem(index, 7, "{:.2f}".format(i.bonus))
                    self.m_listCtrl3.SetItem(index, 8, "{:.2f}".format(i.mony))
                    sums[6] = sums[6] + i.bonus
                    sums[7] = sums[7] + i.mony
            except AttributeError:
                try:
                    if i.activ is True:
                        self.m_listCtrl3.SetItem(index, 5, gui_lib.msg.mashin_report_BonusLock[10])
                    else:
                        self.m_listCtrl3.SetItem(index, 5, str(''))
                except AttributeError:
                    self.m_listCtrl3.SetItem(index, 5, str(''))
                if i.from_redirect is False:
                    self.m_listCtrl3.SetItem(index, 6, str(''))
                else:
                    try:
                        self.m_listCtrl3.SetItem(index, 6, str(i.from_redirect_name))
                    except AttributeError:
                        self.m_listCtrl3.SetItem(index, 6, gui_lib.msg.mashin_report_BonusLock[12])
                self.m_listCtrl3.SetItem(index, 7, "{:.2f}".format(i.mony))
                self.m_listCtrl3.SetItem(index, 8, "{:.2f}".format(0))
                sums[6] = sums[6] + i.mony

            # sums[7] = sums[7] + i.mony
            # sums[6] = sums[6] + i.bonus
            index += 1
        self.m_listCtrl3.InsertItem(index, u'-'*15)
        self.m_listCtrl3.SetItem(index, 1, u'-'*15)
        self.m_listCtrl3.SetItem(index, 2, u'-'*15)
        self.m_listCtrl3.SetItem(index, 3, u'-'*15)
        self.m_listCtrl3.SetItem(index, 4, u'-'*15)
        self.m_listCtrl3.SetItem(index, 5, u'-'*15)
        self.m_listCtrl3.SetItem(index, 6, u'-'*15)
        self.m_listCtrl3.SetItem(index, 7, u'-' * 15)
        self.m_listCtrl3.SetItem(index, 8, u'-' * 15)
#         self.m_listCtrl3.SetItem(index, 6, u'-'*20)
        index += 1
        self.m_listCtrl3.InsertItem(index, u'')
        self.m_listCtrl3.SetItem(index, 1, u'')
        self.m_listCtrl3.SetItem(index, 2, u'')
        self.m_listCtrl3.SetItem(index, 3, u'')
        self.m_listCtrl3.SetItem(index, 4, u'')
        self.m_listCtrl3.SetItem(index, 5, u'')
#         self.m_listCtrl3.SetItem(index, 3, u'-'*20)
        self.m_listCtrl3.SetItem(index, 6, gui_lib.msg.mashin_report_BonusLock[8])
        self.m_listCtrl3.SetItem(index, 7, "{:.2f}".format(sums[6]))
        self.m_listCtrl3.SetItem(index, 8, "{:.2f}".format(sums[7]))
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind( wx.EVT_SIZE, self.on_resize )
        self.on_resize(None)
        
    def OnClose(self, event):
        self.parent.show_panel()
#         self.curent_state_get.abort()
        self.Destroy()
        
    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        # self.width, self.height = self.parent.GetSize()
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height*0.95))
            
        self.m_listCtrl3.SetMinSize((self.width*0.88, self.height * 0.90))
        self.m_listCtrl3.SetSize((self.width * 0.88, self.height * 0.90))
        self.m_listCtrl3.SetColumnWidth(0, self.width * 0.13)
        self.m_listCtrl3.SetColumnWidth(1, self.width * 0.13)
        self.m_listCtrl3.SetColumnWidth(2, self.width * 0.05)
        self.m_listCtrl3.SetColumnWidth(3, self.width * 0.1)
        self.m_listCtrl3.SetColumnWidth(4, self.width * 0.13)
        self.m_listCtrl3.SetColumnWidth(5, self.width * 0.1)
        self.m_listCtrl3.SetColumnWidth(6, self.width * 0.1)
        self.m_button20.SetMinSize((self.width*0.1, -1))
        if event != None:
            # event.Skip()
            self.Layout()
#         self.m_listCtrl3.SetColumnWidth(6, self.width * 0.1)
        
class RealTimeLock(gui.RealTimeLock):
    def __init__(self, parent, row, col, refresh_time):
        self.parent = parent
        gui.RealTimeLock.__init__(self, parent)
        self.row = row
        self.col = col
        self.refresh_time = refresh_time
        for i in reversed(self.col):
            self.m_listCtrl3.InsertColumn(0, i)
        
        index = 0
        for i in self.row:
            self.m_listCtrl3.InsertItem(index, str(i.nom_in_l))
            self.m_listCtrl3.SetItem(index, 1, str(i.model.name))
            for b in range(len(self.col)-2):
                self.m_listCtrl3.SetItem(index, b +2, gui_lib.msg.mashin_report_RealTimeLock[1])
            index += 1
        self.width, self.height = self.parent.GetSize()
        self.Bind( wx.EVT_SIZE, self.on_resize )
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.on_resize(None)
        self.curent_state_get = task.CurentState(self, self.col[2:], self.row, self.refresh_time)  # @UndefinedVariable
        task.CURENT_STATE(self, self.OnState)
#         self.worker = task.CurentState(self, self.col, self.row)
#         task.EVT_STATE(self, self.OnState)
     
    def OnState(self, event):
        index = 0
        self.m_listCtrl3.DeleteAllItems()
        for i in event.data:
            count = 2
            self.m_listCtrl3.InsertItem(index, str(i[0]))
            self.m_listCtrl3.SetItem(index, 1, i[1])
            for b in i[2:]:
                self.m_listCtrl3.SetItem(index, count, b)
                count +=1
            index += 1
#             self.m_listCtrl3.SetItem(index, 2, i[2])
            
    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height*0.95))
        self.m_listCtrl3.SetMinSize((self.width*0.88, self.height * 0.90))
        self.m_listCtrl3.SetColumnWidth(0, self.width * 0.05)
        self.m_listCtrl3.SetColumnWidth(1, self.width * 0.1)
        count = 2
        for i in self.col[2:]:  # @UnusedVariable
            self.m_listCtrl3.SetColumnWidth(count, self.width * 0.07)
            count += 1
        self.m_button20.SetMinSize((self.width*0.1, -1))
        if event != None:
            event.Skip() 
            self.Layout()
            
    def OnClose(self, event):
        self.parent.show_panel()
        self.curent_state_get.abort()
        self.Destroy()
        

class Report(gui.MashinReport):
    def __init__(self, parent):
        gui.MashinReport.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn9.SetLabel(gui_lib.msg.mashin_report_Report[1])
        self.m_radioBtn41.SetLabel(gui_lib.msg.mashin_report_Report[4])
        self.m_radioBtn8.SetLabel(gui_lib.msg.mashin_report_Report[6])
        self.m_radioBtn21.SetLabel(gui_lib.msg.mashin_report_Report[5])

        self.m_radioBtn28.SetLabel(gui_lib.msg.mashin_report_Report['m_radioBtn28'])
        self.m_radioBtn29.SetLabel(gui_lib.msg.mashin_report_Report['m_radioBtn29'])
        self.m_radioBtn10.SetLabel(gui_lib.msg.mashin_report_Report['m_radioBtn10'])
        self.m_radioBtn7.SetLabel(gui_lib.msg.mashin_report_Report['m_radioBtn7'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.mashin_report_Report['m_radioBtn15'])
        self.m_radioBtn42.SetLabel(gui_lib.msg.mashin_report_Report['m_radioBtn42'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.mashin_report_Report['m_radioBtn14'])
        self.m_radioBtn16.SetLabel(gui_lib.msg.mashin_report_Report['m_radioBtn16'])
        self.m_radioBtn17.SetLabel(gui_lib.msg.mashin_report_Report['m_radioBtn17'])
        self.m_button6.SetLabel(gui_lib.msg.mashin_report_Report['m_button6'])

        self.m_calendar1.SetToolTip(gui_lib.msg.mashin_report_Report['m_calendar1'])
        self.m_calendar2.SetToolTip(gui_lib.msg.mashin_report_Report['m_calendar2'])
        self.m_button6.SetToolTip(gui_lib.msg.mashin_report_Report['m_button6_tooltip'])

        self.add_choice()
        self.width, self.height = self.parent.GetSize()
        self.Bind( wx.EVT_SIZE, self.on_resize )
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.on_resize(None)
        
    def table_report(self):
        pass
    
    def pic_report(self):
        pass
    
    def sort_by_nom_in_l(self, row_dict):
        sort_by_nom = {}
        data = {}
        for i in row_dict:
            if int(row_dict[i][0]) not in sort_by_nom:
                sort_by_nom[int(row_dict[i][0])] = row_dict[i]
            else:
                if sort_by_nom[int(row_dict[i][0])][-1] == row_dict[i]:
                    sort_by_nom[int(row_dict[i][0])] = row_dict[i]
                else:
                    if int(row_dict[i][0]) in data:
                        data[int(row_dict[i][0])]+=0.1
                    else:
                        data[int(row_dict[i][0])] = 0.1
                    sort_by_nom[int(row_dict[i][0])+data[int(row_dict[i][0])]] = row_dict[i]
        sorted_data = {}
        for i in sort_by_nom:
            sorted_data[i] = sort_by_nom[i][:-1]
        return sorted_data
                
    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetParent().GetParent().GetParent().GetParent().GetSize()
        self.m_choice3.SetMinSize((self.width*0.48, -1))
        self.SetSize((self.width, self.height))
        if event != None:
            event.Skip() 
            self.Layout()
            
    def add_choice(self):
        choise = [gui_lib.msg.mashin_report_Report[1]]
        
        if self.m_radioBtn9.GetValue() is True:
            data = libs.DB.get_all(libs.models.Maker)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_Report[2])
        elif self.m_radioBtn8.GetValue() is True:
            data = libs.DB.get_all(libs.models.Model)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_Report[3])
        elif self.m_radioBtn41.GetValue() is True:
            data = libs.DB.get_all(libs.models.Flor)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_Report[4])
        elif self.m_radioBtn21.GetValue() is True:
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_Report[5])
            data = libs.DB.get_all(libs.models.User)
        
        for i in data:
            choise.append(i.name)
        self.m_choice3.SetItems(choise)
        self.m_choice3.SetSelection(0)
        
    def OnRadioButton(self, event):
        self.add_choice()
        
    def OnTableMaket(self, event):
        event.Skip()
        # if self.m_radioBtn17.GetValue() is True:
        #     self.m_choice3.Disable()
        # else:
        #     self.m_choice3.Enable()
    
    def OnGo(self, event):
        self.db_row = []
        self.start_date = self.m_calendar1.GetDate()
        self.start_date = self.start_date.Format('%Y-%m-%d')
        
        self.end_date = self.m_calendar2.GetDate()
        self.end_date = self.end_date.Format('%Y-%m-%d')
        
#         start_date = start_date + ' ' + str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
        start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(self.start_date + ' 00:00:00', self.start_date + ' 23:59:59'))
        if start_times == None:
            start_times = ' 09:00:00'
        else:
            start_times = libs.models.TZ.date_to_str(start_times.pub_time, ' %H:%M:%S')
        self.start_date = self.start_date + ' ' + start_times
#         self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
#         self.start_date = libs.models.TZ.go_up_from_date(self.start_date, 1)
#         self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
# #             
#         end_date = end_date + ' ' + str(self.m_spinCtrl3.GetValue()) + ':' + str(self.m_spinCtrl4.GetValue())
        end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(self.end_date + ' 00:00:00', self.end_date + ' 23:59:59'))
        if end_times == None:
            end_times = libs.models.TZ.now()
            end_times = libs.models.TZ.date_to_str(end_times, ' %H:%M:%S')
        else:
            end_times = libs.models.TZ.date_to_str(end_times.pub_time, ' %H:%M:%S')
#         end_date = end_date + ' ' + libs.models.TZ.date_to_str(end_times, '%H:%M')
        self.end_date = self.end_date + ' ' + end_times
        
        choiser =  self.m_choice3.GetString(self.m_choice3.GetSelection())
        if choiser == gui_lib.msg.mashin_report_Report[1] :
            self.db_row = libs.DB.get_all_where(libs.models.Order, pub_time__btw=(self.start_date, self.end_date), order='id')
        else:
            if self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_Report[2]:
                data = libs.DB.get_one_where(libs.models.Maker, name=choiser)
                self.db_row = []
                data = libs.DB.get_all_where(libs.models.Device, maker_id=data.id)
                for i in data:
                    var = libs.DB.get_all_where(libs.models.Order, mashin_id=i.id, pub_time__btw=(self.start_date, self.end_date), order='id')
                    for b in var:
                        self.db_row.append(b)
                        
            elif self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_Report[6]:
                data = libs.DB.get_one_where(libs.models.Model, name=choiser)
                self.db_row = []
                data = libs.DB.get_all_where(libs.models.Device, model_id=data.id)
                for i in data:
                    var = libs.DB.get_all_where(libs.models.Order, mashin_id=i.id, pub_time__btw=(self.start_date, self.end_date), order='id')
                    for b in var:
                        self.db_row.append(b)
            elif self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_Report[4]:
                data = libs.DB.get_one_where(libs.models.Flor, name=choiser)
                self.db_row = libs.DB.get_all_where(libs.models.Order, flor_id=data.id, pub_time__btw=(self.start_date, self.end_date), order='id')
            elif self.m_staticText7.GetLabel() ==  gui_lib.msg.mashin_report_Report[5]:
                data = libs.DB.get_one_where(libs.models.User, name=choiser)
                self.db_row = libs.DB.get_all_where(libs.models.Order, user_id=data.id, pub_time__btw=(self.start_date, self.end_date), order='id')
        # print self.start_date, self.end_date
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()
    
class InOutReport(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn28.Hide()
        self.m_radioBtn29.Hide()
        self.m_radioBtn15.SetValue(True)

            
    def add_choice(self):
        choise = [gui_lib.msg.mashin_report_InOutReport[20]]
        if self.m_radioBtn9.GetValue() is True:
            data = libs.DB.get_all(libs.models.Maker)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_InOutReport[1])
        elif self.m_radioBtn8.GetValue() is True:
            data = libs.DB.get_all(libs.models.Model)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_InOutReport[8])
        elif self.m_radioBtn41.GetValue() is True:
            data = libs.DB.get_all(libs.models.Flor)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_InOutReport[3])
        elif self.m_radioBtn21.GetValue() is True:
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_InOutReport[4])
            data = libs.DB.get_all(libs.models.User)

        for i in data:
            choise.append(i.name)
        self.m_choice3.SetItems(choise)
        self.m_choice3.SetSelection(0)
    
    def table_report(self):
        template = 'report.html'

        template_name = gui_lib.msg.mashin_report_InOutReport['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            template = 'veri_big_table.html'
            col = [
                   gui_lib.msg.mashin_report_InOutReport[5],
                   gui_lib.msg.mashin_report_InOutReport[21],
                   gui_lib.msg.mashin_report_InOutReport[6],
                   gui_lib.msg.mashin_report_InOutReport[7],
                   gui_lib.msg.mashin_report_InOutReport[8],
                   gui_lib.msg.mashin_report_InOutReport[9],
                   gui_lib.msg.mashin_report_InOutReport[10],
                   gui_lib.msg.mashin_report_InOutReport[11],
                   gui_lib.msg.mashin_report_InOutReport[12],
                   gui_lib.msg.mashin_report_InOutReport[13],
                   gui_lib.msg.mashin_report_InOutReport[14],
                   gui_lib.msg.mashin_report_InOutReport[15],
                   gui_lib.msg.mashin_report_InOutReport[16],
                   gui_lib.msg.mashin_report_InOutReport[17],
                   gui_lib.msg.mashin_report_InOutReport[18]]
            row = []
            sums = [u'', u'', u'', u'', u'', u'', u'', u'',u'', u'', gui_lib.msg.mashin_report_InOutReport[19], 0, 0, 0, 0]
            for i in self.db_row:
#                 if i.mashin.nom_in_l == 1:
#                     print (i.new_enter - i.old_enter)*i.mashin.el_coef, libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S')
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(i.user.name)
                var.append(str(i.mashin.nom_in_l))
                var.append(str(i.mashin.serial))
                var.append(i.mashin.model.name)
                
                
                var.append(str(i.old_enter))
                var.append(str(i.old_exit))
                var.append(str(i.new_enter))
                var.append(str(i.new_exit))
                var.append(str(i.bill_old))
                var.append(str(i.bill_new))
                
                var.append("{:.2f}".format(i.bill_new - i.bill_old))
                sums[11] = sums[11] + (i.bill_new - i.bill_old)
                
                var.append("{:.2f}".format((i.new_enter - i.old_enter)*i.mashin.el_coef))
                sums[12] = sums[12] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                
                var.append("{:.2f}".format((i.new_exit - i.old_exit)*i.mashin.el_coef))
                sums[13] = sums[13] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                
                
                
                total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                
                sums[14] = sums[14] + (((i.new_enter - i.old_enter)*i.mashin.el_coef)- ((i.new_exit - i.old_exit)*i.mashin.el_coef))
                var.append("{:.2f}".format(total))
                
                row.append(var)
#                 print row[-1]
            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10,])
            sums[11] = "{:.2f}".format(sums[11])
            sums[12] = "{:.2f}".format(sums[12])
            sums[13] = "{:.2f}".format(sums[13])
            sums[14] = "{:.2f}".format(sums[14])
            row.append(sums)
        elif self.m_radioBtn15.GetValue() is True:
            template = 'report_big_table.html'
            col = [gui_lib.msg.mashin_report_InOutReport[6],
                   gui_lib.msg.mashin_report_InOutReport[8],
                   gui_lib.msg.mashin_report_InOutReport[9],
                   gui_lib.msg.mashin_report_InOutReport[10],
                   gui_lib.msg.mashin_report_InOutReport[11],
                   gui_lib.msg.mashin_report_InOutReport[12],
                   gui_lib.msg.mashin_report_InOutReport[13],
                   gui_lib.msg.mashin_report_InOutReport[14],
                   gui_lib.msg.mashin_report_InOutReport[15],
                   gui_lib.msg.mashin_report_InOutReport[16],
                   gui_lib.msg.mashin_report_InOutReport[17],
                   gui_lib.msg.mashin_report_InOutReport[18]]
            row = []
            var_dict = {}
            sums = [u'', u'', u'', u'', u'', u'', u'', gui_lib.msg.mashin_report_InOutReport[19], 0, 0, 0, 0]
            for i in self.db_row:
                var = []
                if i.mashin_id not in var_dict:
                    var.append(str(i.mashin.nom_in_l))
                    var.append(i.mashin.model.name)
                    var.append(str(i.old_enter))
                    var.append(str(i.old_exit))
                    var.append(str(i.new_enter))
                    var.append(str(i.new_exit))
                    var.append(str(i.bill_old))
                    var.append(str(i.bill_new))
                    var.append(i.bill_new - i.bill_old)
                    var.append((i.new_enter - i.old_enter)*i.mashin.el_coef)
                    var.append((i.new_exit - i.old_exit)*i.mashin.el_coef)
                    total = ((i.new_enter - i.old_enter)*i.mashin.el_coef) - ((i.new_exit - i.old_exit)*i.mashin.el_coef)
                    var.append(total)
                    var.append(i.mashin_id)
                    
                    sums[8] = sums[8] + (i.bill_new - i.bill_old)
                    sums[9] = sums[9] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                    sums[10] = sums[10] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                    sums[11] = sums[11] + total
                    var_dict[i.mashin_id] = var
                else:
                    var_dict[i.mashin_id][4] = str(i.new_enter)
                    var_dict[i.mashin_id][5] = str(i.new_exit)
#                     var_dict[i.mashin_id][4] = str(i.new_enter)
                    var_dict[i.mashin_id][7] = str(i.bill_new)
                    
                    var_dict[i.mashin_id][8] = var_dict[i.mashin_id][8] + (i.bill_new - i.bill_old)
                    sums[8] = sums[8] + (i.bill_new - i.bill_old)
                    
                    var_dict[i.mashin_id][9] = var_dict[i.mashin_id][9] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                    sums[9] = sums[9] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                    
                    var_dict[i.mashin_id][10] = var_dict[i.mashin_id][10] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                    sums[10] = sums[10] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                    
                    
                    
                    total = ((i.new_enter - i.old_enter)*i.mashin.el_coef) - ((i.new_exit - i.old_exit)*i.mashin.el_coef)
                    var_dict[i.mashin_id][11] = var_dict[i.mashin_id][11] + total
                    sums[11] = sums[11] + total
            sort_by_nom = self.sort_by_nom_in_l(var_dict)
            # raise KeyError, sort_by_nom
#             for i in var_dict:
#                 sort_by_nom[int(var_dict[i][0])] = var_dict[i]
                
            for i in sorted(list(sort_by_nom.keys())):
#                 sort_by_nom[i][4] = sort_by_nom[i][4]
#                 sort_by_nom[i][5] = sort_by_nom[i][5]
                sort_by_nom[i][8] = "{:.2f}".format(sort_by_nom[i][8])
                sort_by_nom[i][9] = "{:.2f}".format(sort_by_nom[i][9])
                sort_by_nom[i][10] = "{:.2f}".format(sort_by_nom[i][10])
                sort_by_nom[i][11] = "{:.2f}".format(sort_by_nom[i][11])
                row.append(sort_by_nom[i])
            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10])
            sums[8] = "{:.2f}".format(sums[8])
            sums[9] = "{:.2f}".format(sums[9])
            sums[10] = "{:.2f}".format(sums[10])
            sums[11] = "{:.2f}".format(sums[11])
            row.append(sums)
            
        elif self.m_radioBtn14.GetValue() is True:
            col = [gui_lib.msg.mashin_report_InOutReport[1],
                   gui_lib.msg.mashin_report_InOutReport[16],
                   gui_lib.msg.mashin_report_InOutReport[17],
                   gui_lib.msg.mashin_report_InOutReport[15],
                   gui_lib.msg.mashin_report_InOutReport[18]]
            row = []
            sums = [gui_lib.msg.mashin_report_InOutReport[19], 0, 0, 0, 0]
            var_dict = {}
            
            for i in self.db_row:
                var = []
                if i.mashin.maker.name not in var_dict:
                    var.append(i.mashin.maker.name)
#                     var.append(i.mashin.model.name)
                    var.append((i.new_enter - i.old_enter)*i.mashin.el_coef)
                    sums[1] = sums[1] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                    
                    var.append((i.new_exit - i.old_exit)*i.mashin.el_coef)
                    sums[2] = sums[2] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                    
                    var.append(i.bill_new - i.bill_old)
                    sums[3] = sums[3] + (i.bill_new - i.bill_old)
                    
                    total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                    var.append(total)
                    sums[4] = sums[4] + total
                    
                    var_dict[i.mashin.maker.name] = var
                else:
                    var_dict[i.mashin.maker.name][1] = var_dict[i.mashin.maker.name][1] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                    sums[1] = sums[1] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                    
                    var_dict[i.mashin.maker.name][2] = var_dict[i.mashin.maker.name][2] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                    sums[2] = sums[2] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                    
                    var_dict[i.mashin.maker.name][3] = var_dict[i.mashin.maker.name][3] + (i.bill_new - i.bill_old)
                    sums[3] = sums[3] + (i.bill_new - i.bill_old)
                    
                    total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                    var_dict[i.mashin.maker.name][4] = var_dict[i.mashin.maker.name][4] + total
                    sums[4] = sums[4] + total
                    
            for i in sorted(list(var_dict.keys())):
                var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
                var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
                var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
                var_dict[i][4] = "{:.2f}".format(var_dict[i][4])
                row.append(var_dict[i])
            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10])
            sums[1] = "{:.2f}".format(sums[1])
            sums[2] = "{:.2f}".format(sums[2])
            sums[3] = "{:.2f}".format(sums[3])
            sums[4] = "{:.2f}".format(sums[4])
            row.append(sums)
            
        elif self.m_radioBtn7.GetValue() is True:
            col = [gui_lib.msg.mashin_report_InOutReport[5],
                   gui_lib.msg.mashin_report_InOutReport[16],
                   gui_lib.msg.mashin_report_InOutReport[17],
                   gui_lib.msg.mashin_report_InOutReport[18]]
            row = []
            sums = [gui_lib.msg.mashin_report_InOutReport[19], 0, 0, 0, 0]

            var_dict = {}
            sum_all = 0
            sum_in = 0
            sum_out = 0
            self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
            #             self.start_date = libs.models.TZ.go_up_from_date(self.start_date, 1)
            self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d')

            self.end_date = libs.models.TZ.str_to_date(self.end_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = libs.models.TZ.go_up_from_date(self.end_date, 1)
            self.end_date = libs.models.TZ.date_to_str(self.end_date, '%Y-%m-%d')

            self.db_row = libs.DB.get_all_where(libs.models.DayReport, day_report=True,
                                                pub_time__btw=(self.start_date, self.end_date), order='id')
            for i in self.db_row:
                var = []
                doc_data = json.loads(i.doc_data)
                sum_in += float(doc_data['total_in'])
                sum_out += float(doc_data['total_out'])
                sum_all += float(doc_data['sum_all_total'])
                var_dict[doc_data['doc_date']] = [doc_data['doc_date'], doc_data['total_in'], doc_data['total_out'],
                                                  doc_data['sum_all_total']]

            for i in sorted(list(var_dict.keys())):
                row.append(var_dict[i])
            # raise KeyError, var_dict
            row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10])
            row.append([gui_lib.msg.mashin_report_InOutReport[19], "{:.2f}".format(sum_in), "{:.2f}".format(sum_out),
                        "{:.2f}".format(sum_all)])
        #             sums)
            
        elif self.m_radioBtn42.GetValue() is True:
            col = [gui_lib.msg.mashin_report_InOutReport[3],
                   gui_lib.msg.mashin_report_InOutReport[16],
                   gui_lib.msg.mashin_report_InOutReport[17],
                   gui_lib.msg.mashin_report_InOutReport[15],
                   gui_lib.msg.mashin_report_InOutReport[18]]
            row = []
            sums = [gui_lib.msg.mashin_report_InOutReport[19], 0, 0, 0, 0]
            var_dict = {}
            flor = libs.DB.get_all(libs.models.Flor)
            var_dict = {}
            for i in flor:
                var_dict[i.id] = [i.name, 0, 0, 0, 0]
            for i in self.db_row:
                var = []
                if i.flor_id not in var_dict:
                    var.append(flor)
#                     var.append(i.mashin.model.name)
                    var.append((i.new_enter - i.old_enter)*i.mashin.el_coef)
                    sums[1] = sums[1] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                    
                    var.append((i.new_exit - i.old_exit)*i.mashin.el_coef)
                    sums[2] = sums[2] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                    
                    var.append(i.bill_new - i.bill_old)
                    sums[3] = sums[3] + (i.bill_new - i.bill_old)
                    
                    total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                    sums[4] = sums[4] + total
                    var.append(total)
                    # var.append(i.mashin_id)
                    var_dict[i.flor_id] = var
                else:
                    var_dict[i.flor_id][1] = var_dict[i.flor_id][1] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                    sums[1] = sums[1] + (i.new_enter - i.old_enter)*i.mashin.el_coef
                    
                    var_dict[i.flor_id][2] = var_dict[i.flor_id][2] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                    sums[2] = sums[2] + (i.new_exit - i.old_exit)*i.mashin.el_coef
                    
                    var_dict[i.flor_id][3] = var_dict[i.flor_id][3] + (i.bill_new - i.bill_old)
                    sums[3] = sums[3] + (i.bill_new - i.bill_old)
                    
                    total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                    var_dict[i.flor_id][4] = var_dict[i.flor_id][4] + total
                    sums[4] = sums[4] + total
                    
            for i in sorted(list(var_dict.keys())):
                var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
                var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
                var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
                var_dict[i][4] = "{:.2f}".format(var_dict[i][4])
                row.append(var_dict[i])
            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10])
            sums[1] = "{:.2f}".format(sums[1])
            sums[2] = "{:.2f}".format(sums[2])
            sums[3] = "{:.2f}".format(sums[3])
            sums[4] = "{:.2f}".format(sums[4])
            row.append(sums)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.mashin_report_InOutReport['name'], row=row, col=col, template_name=template_name, template=template)
    
    def pic_report(self):
        row = {}
        y_label = 'TOTAL'
        x_label = 'Date'
        X = []
        template_name = gui_lib.msg.mashin_report_InOutReport['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            for i in self.db_row:
                total = ((i.new_enter - i.old_enter) * i.mashin.el_coef) - (
                        (i.new_exit - i.old_exit) * i.mashin.el_coef)
                # if total != 0:
                if i.mashin.nom_in_l not in row:
                    row[i.mashin.nom_in_l] = [total]
                else:
                    row[i.mashin.nom_in_l].append(total)
            tmp = []
            for i in row:
                X.append(i)
                total = 0
                for b in row[i]:
                    total += b
                tmp.append(total)
            row = tmp
        elif self.m_radioBtn15.GetValue() is True:
            for i in self.db_row:
                total = ((i.new_enter - i.old_enter) * i.mashin.el_coef) - (
                            (i.new_exit - i.old_exit) * i.mashin.el_coef)
                # if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                #     X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if i.mashin.nom_in_l not in row:
                    row[i.mashin.nom_in_l] = [total]
                else:
                    row[i.mashin.nom_in_l].append(total)
            tmp = []
            for i in row:
                X.append(i)
                total = 0
                for b in row[i]:
                    total += b
                tmp.append(total)
            row = tmp
        elif self.m_radioBtn14.GetValue() is True:
            for i in self.db_row:
                total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if i.mashin.maker.name not in row:
                    row[i.mashin.maker.name] = [total]
                else:
                    row[i.mashin.maker.name].append(total)

        elif self.m_radioBtn7.GetValue() is True:
            # x_label = 'Count'
            for i in self.db_row:
                total = (i.new_enter - i.old_enter) * i.mashin.el_coef - (i.new_exit - i.old_exit) * i.mashin.el_coef
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in row:
                    # X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                    row[libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d')] = [total]
                else:
                    row[libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d')].append(total)
            tmp = []
            for i in row:
                X.append(i)
                total = 0
                for b in row[i]:
                    total += b
                tmp.append(total)
            row = tmp
        elif self.m_radioBtn42.GetValue() is True:
            for i in self.db_row:
                total = (i.new_enter - i.old_enter) * i.mashin.el_coef - (i.new_exit - i.old_exit) * i.mashin.el_coef
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if i.mashin.flor.name not in row:
                    row[i.mashin.flor.name] = [total]
                else:
                    row[i.mashin.flor.name].append(total)
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name, y_title=y_label, x_title=x_label, X=X)

    
class Mehanic(InOutReport):
    def __init__(self, parent):
        InOutReport.__init__(self, parent)
        self.m_radioBtn7.Hide()
    
    def table_report(self):
        template = 'report.html'
#         template_name = u'Механични IN, OUT'
        template_name = gui_lib.msg.mashin_report_Mehanic['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            template = 'report_big_table.html'
            col = [gui_lib.msg.mashin_report_Mehanic[1],
                   gui_lib.msg.mashin_report_Mehanic[2],
                   gui_lib.msg.mashin_report_Mehanic[3],
                   gui_lib.msg.mashin_report_Mehanic[4],
                   gui_lib.msg.mashin_report_Mehanic[5],
                   gui_lib.msg.mashin_report_Mehanic[6],
                   gui_lib.msg.mashin_report_Mehanic[7],
                   gui_lib.msg.mashin_report_Mehanic[8],
                   gui_lib.msg.mashin_report_Mehanic[9],
                   gui_lib.msg.mashin_report_Mehanic[10]]
            row = []
            sums = [u'', u'', u'', u'', u'', u'', gui_lib.msg.mashin_report_Mehanic[11], 0, 0, 0]
            for i in self.db_row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(str(i.mashin.nom_in_l))
                var.append(i.mashin.model.name)
                
                var.append(str(i.mex_old_enter))
                var.append(str(i.mex_old_exit))
                var.append(str(i.mex_new_enter))
                var.append(str(i.mex_new_exit))
#                 var.append(str(i.bill_old))
#                 var.append(str(i.bill_new))
                
#                 var.append("{:.2f}".format(i.bill_new - i.bill_old))
#                 sums[9] = sums[9] + (i.bill_new - i.bill_old)
                
                var.append("{:.2f}".format((i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef))
                sums[7] = sums[7] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                
                var.append("{:.2f}".format((i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef))
                sums[8] = sums[8] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                
                
                
                total = (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef - (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                
                sums[9] = sums[9] + (((i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef)- ((i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef))
                var.append("{:.2f}".format(total))
                
                row.append(var)
#                 print row[-1]
            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10,])
            sums[7] = "{:.2f}".format(sums[7])
            sums[8] = "{:.2f}".format(sums[8])
            sums[9] = "{:.2f}".format(sums[9])
#             sums[12] = "{:.2f}".format(sums[12])
            row.append(sums)
        elif self.m_radioBtn15.GetValue() is True:
            template = 'report_big_table.html'
            col = [gui_lib.msg.mashin_report_Mehanic[2],
                   gui_lib.msg.mashin_report_Mehanic[3],
                   gui_lib.msg.mashin_report_Mehanic[4],
                   gui_lib.msg.mashin_report_Mehanic[5],
                   gui_lib.msg.mashin_report_Mehanic[6],
                   gui_lib.msg.mashin_report_Mehanic[7],
                   gui_lib.msg.mashin_report_Mehanic[8],
                   gui_lib.msg.mashin_report_Mehanic[9],
                   gui_lib.msg.mashin_report_Mehanic[10]]
            row = []
            var_dict = {}
            sums = [u'', u'', u'', u'', u'', gui_lib.msg.mashin_report_Mehanic[11], 0, 0, 0]
            for i in self.db_row:
                var = []
                if i.mashin_id not in var_dict:
                    var.append(str(i.mashin.nom_in_l))
                    var.append(i.mashin.model.name)
                    var.append(str(i.mex_old_enter))
                    var.append(str(i.mex_old_exit))
                    var.append(str(i.mex_new_enter))
                    var.append(str(i.mex_new_exit))
                    var.append((i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef)
                    var.append((i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef)
                    total = ((i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef) - ((i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef)
                    var.append(total)
                    var.append(i.mashin_id)
                    
                    sums[6] = sums[6] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                    sums[7] = sums[7] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    sums[8] = sums[8] + total
                    var_dict[i.mashin_id] = var
                else:
                    var_dict[i.mashin_id][4] = str(i.mex_new_enter)
                    var_dict[i.mashin_id][5] = str(i.mex_new_exit)
                    
                    var_dict[i.mashin_id][6] = var_dict[i.mashin_id][6] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                    sums[6] = sums[6] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                    
                    var_dict[i.mashin_id][7] = var_dict[i.mashin_id][7] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    sums[7] = sums[7] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    
                    
                    
                    total = ((i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef) - ((i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef)
                    var_dict[i.mashin_id][8] = var_dict[i.mashin_id][8] + total
                    sums[8] = sums[8] + total
            sort_by_nom = self.sort_by_nom_in_l(var_dict)
                
            for i in sorted(list(sort_by_nom.keys())):
                sort_by_nom[i][6] = "{:.2f}".format(sort_by_nom[i][6])
                sort_by_nom[i][7] = "{:.2f}".format(sort_by_nom[i][7])
                sort_by_nom[i][8] = "{:.2f}".format(sort_by_nom[i][8])
#                 sort_by_nom[i][11] = "{:.2f}".format(sort_by_nom[i][11])
                row.append(sort_by_nom[i])
            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10])
            sums[6] = "{:.2f}".format(sums[6])
            sums[7] = "{:.2f}".format(sums[7])
            sums[8] = "{:.2f}".format(sums[8])
#             sums[11] = "{:.2f}".format(sums[11])
            row.append(sums)
            
        elif self.m_radioBtn14.GetValue() is True:
            col = [gui_lib.msg.mashin_report_Mehanic[12],
                   gui_lib.msg.mashin_report_Mehanic[8],
                   gui_lib.msg.mashin_report_Mehanic[9],
                   gui_lib.msg.mashin_report_Mehanic[10]]
            row = []
            sums = [gui_lib.msg.mashin_report_Mehanic[11], 0, 0, 0]
            var_dict = {}
            
            for i in self.db_row:
                var = []
                if i.mashin.maker.name not in var_dict:
                    var.append(i.mashin.maker.name)
#                     var.append(i.mashin.model.name)
                    var.append((i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef)
                    sums[1] = sums[1] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                    
                    var.append((i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef)
                    sums[2] = sums[2] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    
#                     var.append(i.bill_new - i.bill_old)
#                     sums[3] = sums[3] + (i.bill_new - i.bill_old)
                    
                    total = (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef - (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    var.append(total)
                    sums[3] = sums[3] + total
                    
                    var_dict[i.mashin.maker.name] = var
                else:
                    var_dict[i.mashin.maker.name][1] = var_dict[i.mashin.maker.name][1] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                    sums[1] = sums[1] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                    
                    var_dict[i.mashin.maker.name][2] = var_dict[i.mashin.maker.name][2] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    sums[2] = sums[2] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    
#                     var_dict[i.mashin.maker.name][3] = var_dict[i.mashin.maker.name][3] + (i.bill_new - i.bill_old)
#                     sums[3] = sums[3] + (i.bill_new - i.bill_old)
                    
                    total = (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef - (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    var_dict[i.mashin.maker.name][3] = var_dict[i.mashin.maker.name][3] + total
                    sums[3] = sums[3] + total
                    
            for i in sorted(list(var_dict.keys())):
                var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
                var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
                var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
#                 var_dict[i][4] = "{:.2f}".format(var_dict[i][4])
                row.append(var_dict[i])
            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10])
            sums[1] = "{:.2f}".format(sums[1])
            sums[2] = "{:.2f}".format(sums[2])
            sums[3] = "{:.2f}".format(sums[3])
            row.append(sums)
            
        elif self.m_radioBtn42.GetValue() is True:
            col = [gui_lib.msg.mashin_report_Mehanic[13],
                   gui_lib.msg.mashin_report_Mehanic[8],
                   gui_lib.msg.mashin_report_Mehanic[9],
                   gui_lib.msg.mashin_report_Mehanic[10]]
            row = []
            sums = [gui_lib.msg.mashin_report_Mehanic[11], 0, 0, 0]
            var_dict = {}
            flor = libs.DB.get_all(libs.models.Flor)
            var_dict = {}
            for i in flor:
                var_dict[i.id] = [i.name, 0, 0, 0]
            for i in self.db_row:
                var = []
                if i.flor_id not in var_dict:
                    var.append(i)
#                     var.append(i.mashin.model.name)
                    var.append((i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef)
                    sums[1] = sums[1] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                    
                    var.append((i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef)
                    sums[2] = sums[2] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    
#                     var.append(i.bill_new - i.bill_old)
#                     sums[3] = sums[3] + (i.bill_new - i.bill_old)
                    
                    total = (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef - (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    sums[3] = sums[3] + total
                    var.append(total)
                    var_dict[i.flor_id] = var
                else:
                    var_dict[i.flor_id][1] = var_dict[i.flor_id][1] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                    sums[1] = sums[1] + (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef
                    
                    var_dict[i.flor_id][2] = var_dict[i.flor_id][2] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    sums[2] = sums[2] + (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    
#                     var_dict[i.flor_id][3] = var_dict[i.flor_id][3] + (i.bill_new - i.bill_old)
#                     sums[3] = sums[3] + (i.bill_new - i.bill_old)
                    
                    total = (i.mex_new_enter - i.mex_old_enter)*i.mashin.mex_coef - (i.mex_new_exit - i.mex_old_exit)*i.mashin.mex_coef
                    var_dict[i.flor_id][3] = var_dict[i.flor_id][3] + total
                    sums[3] = sums[3] + total

            for i in sorted(list(var_dict.keys())):
                var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
                var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
                var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
#                 var_dict[i][4] = "{:.2f}".format(var_dict[i][4])
                row.append(var_dict[i])
            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10])
            sums[1] = "{:.2f}".format(sums[1])
            sums[2] = "{:.2f}".format(sums[2])
            sums[3] = "{:.2f}".format(sums[3])
#             sums[4] = "{:.2f}".format(sums[4])
            row.append(sums)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.mashin_report_Mehanic['name'], row=row, col=col, template_name=template_name, template=template)
        

    def pic_report(self):
        row = {}
        y_label = 'TOTAL'
        x_label = 'Date'
        X = []
        template_name = gui_lib.msg.mashin_report_Mehanic['name'] + u':(%s/%s)' % (
            self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            for i in self.db_row:
                total = ((i.mex_new_enter - i.mex_old_enter) * i.mashin.mex_coef) - (
                        (i.mex_new_exit - i.mex_old_exit) * i.mashin.mex_coef)
                # if total != 0:
                if i.mashin.nom_in_l not in row:
                    row[i.mashin.nom_in_l] = [total]
                else:
                    row[i.mashin.nom_in_l].append(total)
            tmp = []
            for i in row:
                X.append(i)
                total = 0
                for b in row[i]:
                    total += b
                tmp.append(total)
            row = tmp
        elif self.m_radioBtn15.GetValue() is True:
            for i in self.db_row:
                total = ((i.mex_new_enter - i.mex_old_enter) * i.mashin.mex_coef) - (
                        (i.mex_new_exit - i.mex_old_exit) * i.mashin.mex_coef)
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if i.mashin.nom_in_l not in row:
                    row[i.mashin.nom_in_l] = [total]
                else:
                    row[i.mashin.nom_in_l].append(total)
            tmp = []
            for i in row:
                X.append(i)
                total = 0
                for b in row[i]:
                    total += b
                tmp.append(total)
            row = tmp
        elif self.m_radioBtn14.GetValue() is True:
            for i in self.db_row:
                total = ((i.mex_new_enter - i.mex_old_enter) * i.mashin.mex_coef) - (
                        (i.mex_new_exit - i.mex_old_exit) * i.mashin.mex_coef)
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if i.mashin.maker.name not in row:
                    row[i.mashin.maker.name] = [total]
                else:
                    row[i.mashin.maker.name].append(total)

        elif self.m_radioBtn7.GetValue() is True:
            # x_label = 'Count'
            for i in self.db_row:
                total = ((i.mex_new_enter - i.mex_old_enter) * i.mashin.mex_coef) - (
                        (i.mex_new_exit - i.mex_old_exit) * i.mashin.mex_coef)
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in row:
                    # X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                    row[libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d')] = [total]
                else:
                    row[libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d')].append(total)
            tmp = []
            for i in row:
                X.append(i)
                total = 0
                for b in row[i]:
                    total += b
                tmp.append(total)
            row = tmp
        elif self.m_radioBtn42.GetValue() is True:
            for i in self.db_row:
                total = ((i.mex_new_enter - i.mex_old_enter) * i.mashin.mex_coef) - (
                        (i.mex_new_exit - i.mex_old_exit) * i.mashin.mex_coef)
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if i.mashin.flor.name not in row:
                    row[i.mashin.flor.name] = [total]
                else:
                    row[i.mashin.flor.name].append(total)
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name, y_title=y_label, x_title=x_label,
                                                                 X=X)
# class NoFinishReport(Report):
#     def __init__(self, parent):
#         pass
    
class MonyReturn(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_checkBox15.SetLabel(gui_lib.msg.mashin_report_MonyReturn['m_checkBox15'])
        self.m_checkBox15.SetToolTip(gui_lib.msg.mashin_report_MonyReturn['m_checkBox15t'])
        self.m_radioBtn21.Hide()
        self.m_calendar1.Hide()
        self.m_calendar2.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn42.Hide()
        self.m_radioBtn9.SetLabel(gui_lib.msg.mashin_report_MonyReturn[2])
        self.m_checkBox15.Show()
        self.add_choice()

    def CalendarShow( self, event ):
        if self.m_checkBox15.GetValue() is False:
            self.m_calendar1.Hide()
            self.m_calendar2.Hide()
        else:
            self.m_calendar1.Show()
            self.m_calendar2.Show()
        self.Layout()

    def OnGo(self, event):
        self.db_row = []
        if self.m_checkBox15.GetValue() is False:
            choiser = self.m_choice3.GetString(self.m_choice3.GetSelection())
            if choiser == gui_lib.msg.mashin_report_MonyReturn[1]:
                self.db_row = libs.DB.get_all_where(libs.models.Device, enable=True,
                                                    order='id')
            else:
                if self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_MonyReturn[2]:
                    data = libs.DB.get_one_where(libs.models.Maker, name=choiser)
                    # self.db_row = []
                    self.db_row = libs.DB.get_all_where(libs.models.Device, maker_id=data.id, enable=True)
                    # for i in data:
                    #     self.db_row.append(b)

                elif self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_MonyReturn[3]:
                    data = libs.DB.get_one_where(libs.models.Model, name=choiser)
                    self.db_row = []
                    self.db_row = libs.DB.get_all_where(libs.models.Device, model_id=data.id, enable=True)
                    # for i in data:
                    #     self.db_row.append(b)
                elif self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_MonyReturn[4]:
                    data = libs.DB.get_one_where(libs.models.Flor, name=choiser)
                    self.db_row = libs.DB.get_all_where(libs.models.Device, flor_id=data.id,
                                                        enable=True, order='id')
        else:
            self.start_date = self.m_calendar1.GetDate()
            self.start_date = self.start_date.Format('%Y-%m-%d')

            self.end_date = self.m_calendar2.GetDate()
            self.end_date = self.end_date.Format('%Y-%m-%d')

            #         start_date = start_date + ' ' + str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
            start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
            self.start_date + ' 00:00:00', self.start_date + ' 23:59:59'))
            if start_times == None:
                start_times = ' 09:00:00'
            else:
                start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')
            self.start_date = self.start_date + ' ' + start_times
            #         self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
            #         self.start_date = libs.models.TZ.go_up_from_date(self.start_date, 1)
            #         self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
            # #
            #         end_date = end_date + ' ' + str(self.m_spinCtrl3.GetValue()) + ':' + str(self.m_spinCtrl4.GetValue())
            end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
                                              pub_time__btw=(self.end_date + ' 00:00:00', self.end_date + ' 23:59:59'))
            if end_times == None:
                end_times = libs.models.TZ.now()
                end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
            else:
                end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')
            #         end_date = end_date + ' ' + libs.models.TZ.date_to_str(end_times, '%H:%M')
            self.end_date = self.end_date + ' ' + end_times

            choiser = self.m_choice3.GetString(self.m_choice3.GetSelection())
            if choiser == gui_lib.msg.mashin_report_Report[1]:
                self.db_row = libs.DB.get_all_where(libs.models.Order, pub_time__btw=(self.start_date, self.end_date),
                                                    order='id')
            else:
                if self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_MonyReturn[2]:
                    data = libs.DB.get_one_where(libs.models.Maker, name=choiser)
                    self.db_row = []
                    data = libs.DB.get_all_where(libs.models.Device, maker_id=data.id)
                    for i in data:
                        var = libs.DB.get_all_where(libs.models.Order, mashin_id=i.id,
                                                    pub_time__btw=(self.start_date, self.end_date), order='id')
                        for b in var:
                            self.db_row.append(b)

                elif self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_MonyReturn[3]:
                    data = libs.DB.get_one_where(libs.models.Model, name=choiser)
                    self.db_row = []
                    data = libs.DB.get_all_where(libs.models.Device, model_id=data.id)
                    for i in data:
                        var = libs.DB.get_all_where(libs.models.Order, mashin_id=i.id,
                                                    pub_time__btw=(self.start_date, self.end_date), order='id')
                        for b in var:
                            self.db_row.append(b)
                elif self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_MonyReturn[4]:
                    data = libs.DB.get_one_where(libs.models.Flor, name=choiser)
                    self.db_row = libs.DB.get_all_where(libs.models.Order, flor_id=data.id,
                                                        pub_time__btw=(self.start_date, self.end_date), order='id')
                # elif self.m_staticText7.GetLabel() == gui_lib.msg.mashin_report_Report[5]:
                #     data = libs.DB.get_one_where(libs.models.User, name=choiser)
                #     self.db_row = libs.DB.get_all_where(libs.models.Order, user_id=data.id,
                #                                         pub_time__btw=(self.start_date, self.end_date), order='id')
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def add_choice(self):
        choise = [gui_lib.msg.mashin_report_MonyReturn[1]]

        if self.m_radioBtn9.GetValue() is True:
            data = libs.DB.get_all(libs.models.Maker)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_MonyReturn[2])
        elif self.m_radioBtn8.GetValue() is True:
            data = libs.DB.get_all(libs.models.Model)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_MonyReturn[3])
        elif self.m_radioBtn41.GetValue() is True:
            data = libs.DB.get_all(libs.models.Flor)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_MonyReturn[4])
        for i in data:
            choise.append(i.name)
        self.m_choice3.SetItems(choise)
        self.m_choice3.SetSelection(0)
    
    
    def table_report(self):
        template = 'report.html'
#         template_name = u'Възвръщаемост' 
        template_name = gui_lib.msg.mashin_report_MonyReturn['name']
        if self.m_checkBox15.GetValue() is False:
            if self.m_radioBtn10.GetValue() is True:

                if self.m_radioBtn28.GetValue() is False:
                    col = [gui_lib.msg.mashin_report_MonyReturn[5],
                           gui_lib.msg.mashin_report_MonyReturn[6],
                           gui_lib.msg.mashin_report_MonyReturn[7],
                           gui_lib.msg.mashin_report_MonyReturn[8],
                           gui_lib.msg.mashin_report_MonyReturn[9]]
                else:
                    col = [gui_lib.msg.mashin_report_MonyReturn[5],
                           gui_lib.msg.mashin_report_MonyReturn[6],
                           gui_lib.msg.mashin_report_MonyReturn[10],
                           gui_lib.msg.mashin_report_MonyReturn[11],
                           gui_lib.msg.mashin_report_MonyReturn[12]]
                row = []
                sums = [u'', gui_lib.msg.mashin_report_MonyReturn[13], 0, 0, 0]

                for i in self.db_row:
                    var = []
                    # var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                    var.append(str(i.nom_in_l))
                    var.append(i.model.name)
                    if self.m_radioBtn28.GetValue() is False:

                        var.append(i.el_out*i.el_coef)
                        sums[2] = sums[2] + (i.el_out*i.el_coef)

                        var.append(i.el_in *i.el_coef)
                        sums[3] = sums[3] + (i.el_in *i.el_coef)

                    else:
                        var.append(i.won*i.el_coef)
                        sums[2] = sums[2] + (i.won *i.el_coef)

                        var.append(i.bet*i.el_coef)
                        sums[3] = sums[3] + (i.bet*i.el_coef)
    #                 total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
    #                 var.append("{:.2f}".format(total))
                    row.append(var)
                for i in row:
                    try:
                        i.append("{:.2f}".format((i[2] / i[3]) * 100))
                    except ZeroDivisionError:
                        i.append('0.00')

                    i[2] = "{:.2f}".format(i[2])
                    i[3] = "{:.2f}".format(i[3])
                try:
                    sums[4] = sums[4] + (sums[2] / sums[3]) * 100
                except ZeroDivisionError:
                    pass
                row.append([u'-'*15, u'-'*15, u'-'*15, u'-'*15, u'-'*15])
                sums[2] = "{:.2f}".format(sums[2])
                sums[3] = "{:.2f}".format(sums[3])
                sums[4] = "{:.2f}".format(sums[4])
                row.append(sums)

            elif self.m_radioBtn15.GetValue() is True:
                if self.m_radioBtn28.GetValue() is False:
                    col = [gui_lib.msg.mashin_report_MonyReturn[5],
                           gui_lib.msg.mashin_report_MonyReturn[6],
                           gui_lib.msg.mashin_report_MonyReturn[7],
                           gui_lib.msg.mashin_report_MonyReturn[8],
                           gui_lib.msg.mashin_report_MonyReturn[9]]
                else:
                    col = [gui_lib.msg.mashin_report_MonyReturn[5],
                           gui_lib.msg.mashin_report_MonyReturn[6],
                           gui_lib.msg.mashin_report_MonyReturn[10],
                           gui_lib.msg.mashin_report_MonyReturn[11],
                           gui_lib.msg.mashin_report_MonyReturn[12]]
                row = []
                sums = [u'', gui_lib.msg.mashin_report_MonyReturn[13], 0, 0, 0]
                var_dict = {}
                for i in self.db_row:
                    var = []
                    if i.id not in var_dict:
                        var.append(str(i.nom_in_l))
                        var.append(i.model.name)

                        if self.m_radioBtn28.GetValue() is True:
                            var.append(i.won*i.el_coef)
                            sums[2] = sums[2] + (i.won*i.el_coef)

                            var.append(i.bet*i.el_coef)
                            sums[3] = sums[3] + (i.bet*i.el_coef)

                        else:
                            var.append(i.el_out*i.el_coef)
                            sums[2] = sums[2] + (i.el_out*i.el_coef)

                            var.append(i.el_in*i.el_coef)
                            sums[3] = sums[3] + (i.el_in*i.el_coef)
    #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                        var.append(i.id)
                        var_dict[i.id] = var
                    else:
                        if self.m_radioBtn28.GetValue() is False:
                            var_dict[i.id][2] = var_dict[i.id][2] + (i.el_out*i.el_coef)
                            sums[2] = sums[2] + (i.el_out*i.el_coef)

                            var_dict[i.id][3] = var_dict[i.id][3] + (i.el_in*i.el_coef)
                            sums[3] = sums[3] + (i.el_in*i.el_coef)



                        else:
                            var_dict[i.id][2] = var_dict[i.id][2] + (i.won*i.el_coef)
                            sums[2] = sums[2] + (i.won*i.el_coef)

                            var_dict[i.id][3] = var_dict[i.id][3] + (i.bet*i.el_coef)
                            sums[3] = sums[3] + (i.bet*i.el_coef)
    #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
    #                     var_dict[i.mashin.nom_in_l][4] = var_dict[i.mashin.nom_in_l][4] + total
                var_dict = self.sort_by_nom_in_l(var_dict)
                for i in sorted(list(var_dict.keys())):
                    try:
                        var_dict[i].append("{:.2f}".format((var_dict[i][2] / var_dict[i][3]) * 100))
    #                     sums[5] = sums[5] + (i[3] / i[4]) * 100
                    except ZeroDivisionError:
                        var_dict[i].append( '0.00')
                    var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
                    var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
    #                 var_dict[i][4] = "{:.2f}".format(var_dict[i][4])
                    row.append(var_dict[i])
                try:
                    sums[4] = (sums[2] / sums[3]) * 100
                except ZeroDivisionError:
                    pass
                row.append([u'-'*15, u'-'*15, u'-'*15, u'-'*15, u'-'*15])
                sums[2] = "{:.2f}".format(sums[2])
                sums[3] = "{:.2f}".format(sums[3])
                sums[4] = "{:.2f}".format(sums[4])
                row.append(sums)

            elif self.m_radioBtn14.GetValue() is True:
                if self.m_radioBtn28.GetValue() is False:
                    col = [gui_lib.msg.mashin_report_MonyReturn[2],
                           gui_lib.msg.mashin_report_MonyReturn[7],
                           gui_lib.msg.mashin_report_MonyReturn[8],
                           gui_lib.msg.mashin_report_MonyReturn[9]]
                else:
                    col = [gui_lib.msg.mashin_report_MonyReturn[2],
                           gui_lib.msg.mashin_report_MonyReturn[10],
                           gui_lib.msg.mashin_report_MonyReturn[11],
                           gui_lib.msg.mashin_report_MonyReturn[12]]
                row = []
                sums = [gui_lib.msg.mashin_report_MonyReturn[13], 0, 0, 0]
                var_dict = {}
                for i in self.db_row:
                    var = []
                    if i.maker.name not in var_dict:
                        var.append(i.maker.name)
    #                     var.append(i.mashin.model.name)
                        if self.m_radioBtn28.GetValue() is False:
                            var.append(i.el_out*i.el_coef)
                            sums[1] = sums[1] + (i.el_out*i.el_coef)

                            var.append(i.el_in*i.el_coef)
                            sums[2] = sums[2] + (i.el_in*i.el_coef)

                        else:
                            var.append(i.won*i.el_coef)
                            sums[1] = sums[1] + (i.won*i.el_coef)

                            var.append(i.bet*i.el_coef)
                            sums[2] = sums[2] + (i.bet*i.el_coef)
    #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
    #                     var.append(total)
                        var_dict[i.maker.name] = var
                    else:
                        if self.m_radioBtn28.GetValue() is False:
                            var_dict[i.maker.name][1] = var_dict[i.maker.name][1] + (i.el_out*i.el_coef)
                            sums[1] = sums[1] + (i.el_out*i.el_coef)

                            var_dict[i.maker.name][2] = var_dict[i.maker.name][2] + (i.el_in*i.el_coef)
                            sums[2] = sums[2] + (i.el_in*i.el_coef)

                        else:
                            var_dict[i.maker.name][1] = var_dict[i.maker.name][1] + (i.won*i.el_coef)
                            sums[1] = sums[1] + (i.won*i.el_coef)

                            var_dict[i.maker.name][2] = var_dict[i.maker.name][2] + (i.bet*i.el_coef)
                            sums[2] = sums[2] + (i.bet*i.el_coef)
    #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
    #                     var_dict[i.mashin.maker.name][3] = var_dict[i.mashin.maker.name][3] + total

                for i in sorted(list(var_dict.keys())):
                    try:
                        var_dict[i].append("{:.2f}".format((var_dict[i][1] / var_dict[i][2]) * 100))
                    except ZeroDivisionError:
                        var_dict[i].append('0.00')
                    var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
                    var_dict[i][2] = "{:.2f}".format(var_dict[i][2])

                    row.append(var_dict[i])
                try:
                    sums[3] = (sums[1] / sums[2])*100
                except ZeroDivisionError:
                    pass
                row.append([u'-'*15, u'-'*15, u'-'*15, u'-'*15])
                sums[1] = "{:.2f}".format(sums[1])
                sums[2] = "{:.2f}".format(sums[2])
                sums[3] = "{:.2f}".format(sums[3])
                row.append(sums)


    #         elif self.m_radioBtn42.GetValue() is True:
    #             if self.m_radioBtn28.GetValue() is False:
    #                 col = [gui_lib.msg.mashin_report_MonyReturn[4],
    #                        gui_lib.msg.mashin_report_MonyReturn[7],
    #                        gui_lib.msg.mashin_report_MonyReturn[8],
    #                        gui_lib.msg.mashin_report_MonyReturn[9]]
    #             else:
    #                 col = [gui_lib.msg.mashin_report_MonyReturn[4],
    #                        gui_lib.msg.mashin_report_MonyReturn[10],
    #                        gui_lib.msg.mashin_report_MonyReturn[11],
    #                        gui_lib.msg.mashin_report_MonyReturn[12]]
    #             row = []
    #             sums = [gui_lib.msg.mashin_report_MonyReturn[13], 0, 0, 0]
    #             var_dict = {}
    #
    #             flor = libs.DB.get_all(libs.models.Flor)
    #             var_dict = {'':[gui_lib.msg.mashin_report_MonyReturn[13], 0, 0, 0]}
    #             for i in flor:
    #                 var_dict[i.name] = [i.name, 0, 0, 0]
    #             for i in self.db_row:
    #                 print i.flor.name
    #                 var = []
    # #                 if i.flor_id == None:
    # #                     flor = _(u"Всички")
    # #                 else:
    # #                     flor = libs.DB.get_one_where(libs.models.Flor, id=i.flor_id).name
    #                 if i.flor.name not in var_dict:
    #                     var.append(i.flor.name)
    # #                     var.append(i.mashin.model.name)
    #                     if self.m_radioBtn28.GetValue() is False:
    #                         var.append(i.el_out*i.el_coef)
    #                         sums[1] = sums[1] + (i.el_out*i.el_coef)
    #
    #                         var.append(i.el_in*i.el_coef)
    #                         sums[2] = sums[2] + (i.el_in*i.el_coef)
    #
    #                     else:
    #                         var.append(i.won*i.el_coef)
    #                         sums[1] = sums[1] + (i.won*i.el_coef)
    #
    #                         var.append(i.bet*i.el_coef)
    #                         sums[2] = sums[2] + (i.bet*i.el_coef)
    # #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
    # #                     var.append(total)
    #                     var_dict[i.flor.name] = var
    #                 else:
    #                     if self.m_radioBtn28.GetValue() is False:
    #
    #                         var_dict[i.flor.name][1] = var_dict[i.flor.name][1] + (i.el_out*i.el_coef)
    #                         sums[1] = sums[1] + (i.el_out*i.el_coef)
    #
    #                         var_dict[i.flor.name][2] = var_dict[i.flor.name][2] + (i.el_in*i.el_coef)
    #                         sums[2] = sums[2] + (i.el_in*i.el_coef)
    #
    #
    #                     else:
    #                         var_dict[i.flor.name][1] = var_dict[i.flor.name][1] + (i.won*i.el_coef)
    #                         sums[1] = sums[1] + (i.won*i.el_coef)
    #
    #                         var_dict[i.flor.name][2] = var_dict[i.flor.name][2] + (i.bet*i.el_coef)
    #                         sums[2] = sums[2] + (i.bet*i.el_coef)
    # #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
    # #                     var_dict[flor][3] = var_dict[flor][3] + total
    #             for i in sorted(var_dict.keys()):
    #                 try:
    #                     var_dict[i].append("{:.2f}".format((var_dict[i][1] / var_dict[i][2]) * 100))
    #                 except ZeroDivisionError:
    #                     var_dict[i].append('0.00')
    #                 var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
    #                 var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
    #                 var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
    #                 row.append(var_dict[i])
    #             row.append([u'-'*15, u'-'*15, u'-'*15, u'-'*15])
    #             try:
    #                 sums[3] = (sums[1] / sums[2]) * 100
    #             except ZeroDivisionError:
    #                 pass
    #             sums[1] = "{:.2f}".format(sums[1])
    #             sums[2] = "{:.2f}".format(sums[2])
    #             sums[3] = "{:.2f}".format(sums[3])
    #             row.append(sums)
        else:
            if self.m_radioBtn10.GetValue() is True:
                if self.m_radioBtn28.GetValue() is False:
                    col = [gui_lib.msg.mashin_report_MonyReturn[16],
                           gui_lib.msg.mashin_report_MonyReturn[5],
                           gui_lib.msg.mashin_report_MonyReturn[6],
                           gui_lib.msg.mashin_report_MonyReturn[7],
                           gui_lib.msg.mashin_report_MonyReturn[8],
                           gui_lib.msg.mashin_report_MonyReturn[15],
                           gui_lib.msg.mashin_report_MonyReturn[9],
                           ]
                else:
                    col = [gui_lib.msg.mashin_report_MonyReturn[16],
                           gui_lib.msg.mashin_report_MonyReturn[5],
                           gui_lib.msg.mashin_report_MonyReturn[6],
                           gui_lib.msg.mashin_report_MonyReturn[10],
                           gui_lib.msg.mashin_report_MonyReturn[11],
                           gui_lib.msg.mashin_report_MonyReturn[15],
                           gui_lib.msg.mashin_report_MonyReturn[12],
                           ]
                row = []
                sums = [u'', u'', gui_lib.msg.mashin_report_MonyReturn[13], 0, 0, 0, 0]

                for i in self.db_row:
                    var = []
                    var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                    var.append(str(i.mashin.nom_in_l))
                    var.append(i.mashin.model.name)
                    if self.m_radioBtn28.GetValue() is False:

                        var.append((i.new_exit - i.old_exit) * i.mashin.el_coef)
                        sums[3] = sums[3] + (i.new_exit - i.old_exit) * i.mashin.el_coef

                        var.append((i.new_enter - i.old_enter) * i.mashin.el_coef)
                        sums[4] = sums[4] + (i.new_enter - i.old_enter) * i.mashin.el_coef
                        total = (i.new_enter - i.old_enter) * i.mashin.el_coef - (i.new_exit - i.old_exit) * i.mashin.el_coef
                        var.append("{:.2f}".format(total))
                        sums[5] += total

                    else:
                        var.append((i.new_won - i.old_won) * i.mashin.el_coef)
                        sums[3] = sums[3] + (i.new_won - i.old_won) * i.mashin.el_coef

                        var.append((i.new_bet - i.old_bet) * i.mashin.el_coef)
                        sums[4] = sums[4] + (i.new_bet - i.old_bet) * i.mashin.el_coef
                        total = (i.new_bet - i.old_bet) * i.mashin.el_coef - (
                                    i.new_won - i.old_won) * i.mashin.el_coef
                        var.append("{:.2f}".format(total))
                        sums[5] += total
                    #                 total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                    #                 var.append("{:.2f}".format(total))
                    row.append(var)
                for i in row:
                    try:
                        i.append("{:.2f}".format((i[3] / i[4]) * 100))
                    except ZeroDivisionError:
                        i.append('0.00')

                    i[3] = "{:.2f}".format(i[3])
                    i[4] = "{:.2f}".format(i[4])
                try:
                    sums[6] = sums[6] + (sums[3] / sums[4]) * 100
                except ZeroDivisionError:
                    pass
                row.append([u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15])
                sums[3] = "{:.2f}".format(sums[3])
                sums[4] = "{:.2f}".format(sums[4])
                sums[5] = "{:.2f}".format(sums[5])
                sums[6] = "{:.2f}".format(sums[6])
                row.append(sums)

            elif self.m_radioBtn15.GetValue() is True:
                if self.m_radioBtn28.GetValue() is False:
                    col = [gui_lib.msg.mashin_report_MonyReturn[5],
                           gui_lib.msg.mashin_report_MonyReturn[6],
                           gui_lib.msg.mashin_report_MonyReturn[7],
                           gui_lib.msg.mashin_report_MonyReturn[8],
                           gui_lib.msg.mashin_report_MonyReturn[15],
                           gui_lib.msg.mashin_report_MonyReturn[9],
                           ]
                else:
                    col = [gui_lib.msg.mashin_report_MonyReturn[5],
                           gui_lib.msg.mashin_report_MonyReturn[6],
                           gui_lib.msg.mashin_report_MonyReturn[10],
                           gui_lib.msg.mashin_report_MonyReturn[11],
                           gui_lib.msg.mashin_report_MonyReturn[15],
                           gui_lib.msg.mashin_report_MonyReturn[12],
                           ]
                row = []
                sums = [u'', gui_lib.msg.mashin_report_MonyReturn[13], 0, 0, 0, 0]
                var_dict = {}
                for i in self.db_row:
                    var = []
                    if i.mashin_id not in var_dict:
                        var.append(str(i.mashin.nom_in_l))
                        var.append(i.mashin.model.name)

                        if self.m_radioBtn28.GetValue() is False:
                            var.append((i.new_exit - i.old_exit) * i.mashin.el_coef)
                            sums[2] = sums[2] + (i.new_exit - i.old_exit) * i.mashin.el_coef

                            var.append((i.new_enter - i.old_enter) * i.mashin.el_coef)
                            sums[3] = sums[3] + (i.new_enter - i.old_enter) * i.mashin.el_coef
                            total = (i.new_enter - i.old_enter) * i.mashin.el_coef - (i.new_exit - i.old_exit) * i.mashin.el_coef
                            var.append(total)
                            var.append(i.mashin_id)
                            sums[4] += total

                        else:
                            var.append((i.new_won - i.old_won) * i.mashin.el_coef)
                            sums[2] = sums[2] + (i.new_won - i.old_won) * i.mashin.el_coef

                            var.append((i.new_bet - i.old_bet) * i.mashin.el_coef)
                            sums[3] = sums[3] + (i.new_bet - i.old_bet) * i.mashin.el_coef
                            total = (i.new_bet - i.old_bet) * i.mashin.el_coef - (
                                    i.new_won - i.old_won) * i.mashin.el_coef
                            var.append(total)
                            var.append(i.mashin_id)
                            sums[4] += total
                        #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                        #                     var.append(total)
                        var_dict[i.mashin_id] = var
                    else:
                        if self.m_radioBtn28.GetValue() is False:
                            var_dict[i.mashin_id][2] = var_dict[i.mashin_id][2] + (
                                        i.new_exit - i.old_exit) * i.mashin.el_coef
                            sums[2] = sums[2] + (i.new_exit - i.old_exit) * i.mashin.el_coef

                            var_dict[i.mashin_id][3] = var_dict[i.mashin_id][3] + (
                                        i.new_enter - i.old_enter) * i.mashin.el_coef
                            sums[3] = sums[3] + (i.new_enter - i.old_enter) * i.mashin.el_coef
                            total = (i.new_enter - i.old_enter) * i.mashin.el_coef - (
                                        i.new_exit - i.old_exit) * i.mashin.el_coef
                            var_dict[i.mashin_id][4]+=total
                            sums[4] += total


                        else:
                            var_dict[i.mashin_id][2] = var_dict[i.mashin_id][2] + (
                                        i.new_won - i.old_won) * i.mashin.el_coef
                            sums[2] = sums[2] + (i.new_won - i.old_won) * i.mashin.el_coef

                            var_dict[i.mashin_id][3] = var_dict[i.mashin_id][3] + (
                                        i.new_bet - i.old_bet) * i.mashin.el_coef
                            sums[3] = sums[3] + (i.new_bet - i.old_bet) * i.mashin.el_coef
                            total = (i.new_bet - i.old_bet) * i.mashin.el_coef - (
                                    i.new_won - i.old_won) * i.mashin.el_coef
                            var_dict[i.mashin_id][4] += total
                            sums[4] += total
                #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                #                     var_dict[i.mashin.nom_in_l][4] = var_dict[i.mashin.nom_in_l][4] + total
                var_dict = self.sort_by_nom_in_l(var_dict)
                for i in sorted(list(var_dict.keys())):
                    try:
                        var_dict[i].append("{:.2f}".format((var_dict[i][2] / var_dict[i][3]) * 100))
                    #                     sums[5] = sums[5] + (i[3] / i[4]) * 100
                    except ZeroDivisionError:
                        var_dict[i].append('0.00')
                    var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
                    var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
                    var_dict[i][4] = "{:.2f}".format(var_dict[i][4])
                    #                 var_dict[i][4] = "{:.2f}".format(var_dict[i][4])
                    row.append(var_dict[i])
                try:
                    sums[5] = (sums[2] / sums[3]) * 100
                except ZeroDivisionError:
                    pass
                row.append([u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15])
                sums[2] = "{:.2f}".format(sums[2])
                sums[3] = "{:.2f}".format(sums[3])
                sums[4] = "{:.2f}".format(sums[4])
                sums[5] = "{:.2f}".format(sums[5])
                row.append(sums)

            elif self.m_radioBtn14.GetValue() is True:
                if self.m_radioBtn28.GetValue() is False:
                    col = [gui_lib.msg.mashin_report_MonyReturn[2],
                           gui_lib.msg.mashin_report_MonyReturn[7],
                           gui_lib.msg.mashin_report_MonyReturn[8],
                           gui_lib.msg.mashin_report_MonyReturn[9],
                           gui_lib.msg.mashin_report_MonyReturn[15]]
                else:
                    col = [gui_lib.msg.mashin_report_MonyReturn[2],
                           gui_lib.msg.mashin_report_MonyReturn[10],
                           gui_lib.msg.mashin_report_MonyReturn[11],
                           gui_lib.msg.mashin_report_MonyReturn[12],
                           gui_lib.msg.mashin_report_MonyReturn[15]]
                row = []
                sums = [gui_lib.msg.mashin_report_MonyReturn[13], 0, 0, 0, 0]
                var_dict = {}
                for i in self.db_row:
                    var = []
                    if i.mashin.maker.name not in var_dict:
                        var.append(i.mashin.maker.name)
                        #                     var.append(i.mashin.model.name)
                        if self.m_radioBtn28.GetValue() is False:
                            var.append((i.new_exit - i.old_exit) * i.mashin.el_coef)
                            sums[1] = sums[1] + (i.new_exit - i.old_exit) * i.mashin.el_coef

                            var.append((i.new_enter - i.old_enter) * i.mashin.el_coef)
                            sums[2] = sums[2] + (i.new_enter - i.old_enter) * i.mashin.el_coef
                            total = (i.new_enter - i.old_enter) * i.mashin.el_coef - (
                                        i.new_exit - i.old_exit) * i.mashin.el_coef
                            try:
                                var.append(var[1] / var[2] * 100)
                            except ZeroDivisionError:
                                var.append(0.0)
                            var.append(total)
                            sums[4] += total

                        else:
                            var.append((i.new_won - i.old_won) * i.mashin.el_coef)
                            sums[1] = sums[1] + (i.new_won - i.old_won) * i.mashin.el_coef

                            var.append((i.new_bet - i.old_bet) * i.mashin.el_coef)
                            sums[2] = sums[2] + (i.new_bet - i.old_bet) * i.mashin.el_coef
                            total = (i.new_bet - i.old_bet) * i.mashin.el_coef - (
                                    i.new_won - i.old_won) * i.mashin.el_coef
                            try:
                                var.append(var[1]/var[2]*100)
                            except ZeroDivisionError:
                                var.append(0.0)
                            # var.append(total * 100)
                            var.append(total)
                            sums[4] += total
                        #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                        #                     var.append(total)
                        var_dict[i.mashin.maker.name] = var
                    else:
                    #     # print var_dict[i.mashin.maker.name][3]
                        if self.m_radioBtn28.GetValue() is False:
                            var_dict[i.mashin.maker.name][1] += var_dict[i.mashin.maker.name][1] + (
                                        i.new_exit - i.old_exit) * i.mashin.el_coef
                            sums[1] = sums[1] + (i.new_exit - i.old_exit) * i.mashin.el_coef
                    #
                            var_dict[i.mashin.maker.name][2] += var_dict[i.mashin.maker.name][2] + (
                                        i.new_enter - i.old_enter) * i.mashin.el_coef
                            # var_dict[i.mashin.maker.name][3] = (var_dict[i.mashin.maker.name][1] / var_dict[i.mashin.maker.name][2]) * 100
                            sums[2] = sums[2] + (i.new_enter - i.old_enter) * i.mashin.el_coef
                            total = (i.new_enter - i.old_enter) * i.mashin.el_coef - (
                                    i.new_exit - i.old_exit) * i.mashin.el_coef
                            try:
                                var_dict[i.mashin.maker.name][3] = (var_dict[i.mashin.maker.name][1] / var_dict[i.mashin.maker.name][2]) * 100
                            except ZeroDivisionError:
                                pass
                            var_dict[i.mashin.maker.name][4] += total
                            sums[4] += total
                    #
                        else:
                            var_dict[i.mashin.maker.name][1] = var_dict[i.mashin.maker.name][1] + (
                                        i.new_won - i.old_won) * i.mashin.el_coef
                            sums[1] = sums[1] + (i.new_won - i.old_won) * i.mashin.el_coef

                            var_dict[i.mashin.maker.name][2] = var_dict[i.mashin.maker.name][2] + (
                                        i.new_bet - i.old_bet) * i.mashin.el_coef
                            sums[2] = sums[2] + (i.new_bet - i.old_bet) * i.mashin.el_coef
                            total = (i.new_bet - i.old_bet) * i.mashin.el_coef - (
                                    i.new_won - i.old_won) * i.mashin.el_coef
                            try:
                                var_dict[i.mashin.maker.name][3] = (var_dict[i.mashin.maker.name][1] / var_dict[i.mashin.maker.name][2]) * 100
                            except ZeroDivisionError:
                                pass
                            var_dict[i.mashin.maker.name][4] += total
                            sums[4] += total
                                    # total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                                    # var_dict[i.mashin.maker.name][3] = var_dict[i.mashin.maker.name][3] + total
                # print var_dict[i.mashin.maker.name]
                for i in sorted(list(var_dict.keys())):
                    var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
                    var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
                    var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
                    var_dict[i][4] = "{:.2f}".format(var_dict[i][4])
                    # var_dict[i][5] = "{:.2f}".format(var_dict[i][5])
                    row.append(var_dict[i])
                # print var_dict[i]
                try:
                    sums[3] = (sums[1] / sums[2]) * 100
                except ZeroDivisionError:
                    pass
                row.append([u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15])
                sums[1] = "{:.2f}".format(sums[1])
                sums[2] = "{:.2f}".format(sums[2])
                sums[3] = "{:.2f}".format(sums[3])
                sums[4] = "{:.2f}".format(sums[4])
                row.append(sums)
            # elif self.m_radioBtn7.GetValue() is True:
            #     if self.m_radioBtn28.GetValue() is False:
            #         col = [u'Дата', u'Изход', u'Вход', u'Задържани пари %']
            #     else:
            #         col = [u'Дата', u'Печалба', u'Залог', u'Задържани пари %']
            #     row = []
            #     sums = [_(u'Общо'), 0, 0, 0]
            #     var_dict = {}
            #     for i in self.db_row:
            #         var = []
            #         if libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y') not in var_dict:
            #             var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y'))
            #             #                     var.append(i.mashin.model.name)
            #             if self.m_radioBtn28.GetValue() is False:
            #
            #                 var.append((i.new_exit - i.old_exit) * i.mashin.el_coef)
            #                 sums[1] = sums[1] + (i.new_exit - i.old_exit) * i.mashin.el_coef
            #
            #                 var.append((i.new_enter - i.old_enter) * i.mashin.el_coef)
            #                 sums[2] = sums[2] + (i.new_enter - i.old_enter) * i.mashin.el_coef
            #
            #
            #             else:
            #                 var.append((i.new_won - i.old_won) * i.mashin.el_coef)
            #                 sums[1] = sums[1] + (i.new_won - i.old_won) * i.mashin.el_coef
            #
            #                 var.append((i.new_bet - i.old_bet) * i.mashin.el_coef)
            #                 sums[2] = sums[2] + (i.new_bet - i.old_bet) * i.mashin.el_coef
            #             #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
            #             #                     var.append(total)
            #             var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')] = var
            #         else:
            #             if self.m_radioBtn28.GetValue() is False:
            #                 var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][1] = \
            #                 var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][1] + (
            #                             i.new_exit - i.old_exit) * i.mashin.el_coef
            #                 sums[1] = sums[1] + (i.new_exit - i.old_exit) * i.mashin.el_coef
            #
            #                 var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][2] = \
            #                 var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][2] + (
            #                             i.new_enter - i.old_enter) * i.mashin.el_coef
            #                 sums[2] = sums[2] + (i.new_enter - i.old_enter) * i.mashin.el_coef
            #
            #             else:
            #                 var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][1] = \
            #                 var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][1] + (
            #                             i.new_won - i.old_won) * i.mashin.el_coef
            #                 sums[1] = sums[1] + (i.new_won - i.old_won) * i.mashin.el_coef
            #
            #                 var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][2] = \
            #                 var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][2] + (
            #                             i.new_bet - i.old_bet) * i.mashin.el_coef
            #                 sums[2] = sums[2] + (i.new_bet - i.old_bet) * i.mashin.el_coef
            #     #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
            #     #                     var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][3] = var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][3] + total
            #
            #     for i in sorted(var_dict.keys()):
            #         try:
            #             var_dict[i].append("{:.2f}".format((var_dict[i][1] / var_dict[i][2]) * 100))
            #         except ZeroDivisionError:
            #             var_dict[i].append('0.00')
            #
            #         var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
            #         var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
            #         #                 var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
            #         row.append(var_dict[i])
            #     try:
            #         sums[3] = (sums[1] / sums[2]) * 100
            #     except ZeroDivisionError:
            #         pass
            #     row.append([u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15])
            #     sums[1] = "{:.2f}".format(sums[1])
            #     sums[2] = "{:.2f}".format(sums[2])
            #     sums[3] = "{:.2f}".format(sums[3])
            #     row.append(sums)

            # elif self.m_radioBtn42.GetValue() is True:
            #     if self.m_radioBtn28.GetValue() is False:
            #         col = [u'Регион', u'Изход', u'Вход', u'Задържани пари %']
            #     else:
            #         col = [u'Регион', u'Печалба', u'Залог', u'Задържани пари %']
            #     row = []
            #     sums = [_(u'Общо'), 0, 0, 0]
            #     var_dict = {}
            #
            #     flor = libs.DB.get_all(libs.models.Flor)
            #     var_dict = {None: [_(u'Общо'), 0, 0, 0]}
            #     for i in flor:
            #         var_dict[i.name] = [i.name, 0, 0, 0]
            #
            #     for i in self.db_row:
            #         var = []
            #         #                 if i.flor_id == None:
            #         #                     flor = _(u"Всички")
            #         #                 else:
            #         #                     flor = libs.DB.get_one_where(libs.models.Flor, id=i.flor_id).name
            #         if i.mashin.flor.name not in var_dict:
            #             var.append(i.mashin.flor.name)
            #             #                     var.append(i.mashin.model.name)
            #             if self.m_radioBtn28.GetValue() is False:
            #                 var.append((i.new_exit - i.old_exit) * i.mashin.el_coef)
            #                 sums[1] = sums[1] + (i.new_exit - i.old_exit) * i.mashin.el_coef
            #
            #                 var.append((i.new_enter - i.old_enter) * i.mashin.el_coef)
            #                 sums[2] = sums[2] + (i.new_enter - i.old_enter) * i.mashin.el_coef
            #
            #             else:
            #                 var.append((i.new_won - i.old_won) * i.mashin.el_coef)
            #                 sums[1] = sums[1] + (i.new_won - i.old_won) * i.mashin.el_coef
            #
            #                 var.append((i.new_bet - i.old_bet) * i.mashin.el_coef)
            #                 sums[2] = sums[2] + (i.new_bet - i.old_bet) * i.mashin.el_coef
            #             #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
            #             #                     var.append(total)
            #             var_dict[i.mashin.flor.name] = var
            #         else:
            #             if self.m_radioBtn28.GetValue() is False:
            #
            #                 var_dict[i.mashin.flor.name][1] = var_dict[i.mashin.flor.name][1] + (
            #                             i.new_exit - i.old_exit) * i.mashin.el_coef
            #                 sums[1] = sums[1] + (i.new_exit - i.old_exit) * i.mashin.el_coef
            #
            #                 var_dict[i.mashin.flor.name][2] = var_dict[i.mashin.flor.name][2] + (
            #                             i.new_enter - i.old_enter) * i.mashin.el_coef
            #                 sums[2] = sums[2] + (i.new_enter - i.old_enter) * i.mashin.el_coef
            #
            #
            #             else:
            #                 var_dict[i.mashin.flor.name][1] = var_dict[i.mashin.flor.name][1] + (
            #                             i.new_won - i.old_won) * i.mashin.el_coef
            #                 sums[1] = sums[1] + (i.new_won - i.old_won) * i.mashin.el_coef
            #
            #                 var_dict[i.mashin.flor.name][2] = var_dict[i.mashin.flor.name][2] + (
            #                             i.new_bet - i.old_bet) * i.mashin.el_coef
            #                 sums[2] = sums[2] + (i.new_bet - i.old_bet) * i.mashin.el_coef
            #     #                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
            #     #                     var_dict[flor][3] = var_dict[flor][3] + total
            #
            #     for i in sorted(var_dict.keys()):
            #         try:
            #             var_dict[i].append("{:.2f}".format((var_dict[i][1] / var_dict[i][2]) * 100))
            #         except ZeroDivisionError:
            #             var_dict[i].append('0.00')
            #         var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
            #         var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
            #         var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
            #         row.append(var_dict[i])
            #     row.append([u'-' * 15, u'-' * 15, u'-' * 15, u'-' * 15])
            #     try:
            #         sums[3] = (sums[1] / sums[2]) * 100
            #     except ZeroDivisionError:
            #         pass
            #     sums[1] = "{:.2f}".format(sums[1])
            #     sums[2] = "{:.2f}".format(sums[2])
            #     sums[3] = "{:.2f}".format(sums[3])
            #     row.append(sums)

        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.mashin_report_MonyReturn['name'], row=row, col=col, template_name=template_name, template=template)

    def pic_report(self):
        template_name = gui_lib.msg.mashin_report_MonyReturn['name']
        row = {}
        X = []
        y_title = 'Total %'
        x_title = 'Date'
        if self.m_checkBox15.GetValue() is False:
            X = []
            row=[]
            y_title = 'Total %'
            x_title = 'Device'
            # row = []
            for i in self.db_row:
                if i.nom_in_l not in X:
                    X.append(i.nom_in_l)
                if self.m_radioBtn28.GetValue() is True:
                    won = (i.won*i.el_coef)
                    bet = (i.bet*i.el_coef)
                    try:
                        total = (won / bet)*100
                    except ZeroDivisionError:
                        total = 0
                else:
                    ins = (i.el_in * i.el_coef)
                    out = (i.el_out * i.el_coef)
                    try:
                        total = (out / ins) * 100
                    except ZeroDivisionError:
                        total = 0
                row.append("{:.2f}".format(total))


        else:
            if self.m_radioBtn10.GetValue() is True:

                for i in self.db_row:
                    if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                        X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                    if self.m_radioBtn28.GetValue() is True:

                        if i.mashin.serial not in row:
                            try:
                                row[i.mashin.serial] = [((i.new_won - i.old_won) * i.mashin.el_coef) / (
                                            (i.new_enter - i.old_enter) * i.mashin.el_coef) * 100]
                            except ZeroDivisionError:
                                row[i.mashin.serial] = [0.0]
                        else:
                            try:
                                row[i.mashin.serial].append(((i.new_won - i.old_won) * i.mashin.el_coef) / (
                                            (i.new_enter - i.old_enter) * i.mashin.el_coef) * 100)
                            except ZeroDivisionError:
                                row[i.mashin.serial].append(0.0)
                    else:
                        if i.mashin.serial not in row:
                            try:
                                row[i.mashin.serial] = [((i.new_exit - i.old_exit) * i.mashin.el_coef) / (
                                            (i.new_enter - i.old_enter) * i.mashin.el_coef) * 100]
                            except ZeroDivisionError:
                                row[i.mashin.serial] = [0.0]
                        else:
                            try:
                                row[i.mashin.serial].append(((i.new_won - i.old_won) * i.mashin.el_coef) / (
                                            (i.new_enter - i.old_enter) * i.mashin.el_coef) * 100)
                            except ZeroDivisionError:
                                row[i.mashin.serial].append(0.0)

            elif self.m_radioBtn15.GetValue() is True:

                for i in self.db_row:
                    if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                        X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                    if self.m_radioBtn28.GetValue() is True:

                        if i.mashin.nom_in_l not in row:
                            try:
                                row[i.mashin.nom_in_l] = [((i.new_won - i.old_won) * i.mashin.el_coef)/((i.new_enter - i.old_enter) * i.mashin.el_coef)*100]
                            except ZeroDivisionError:
                                row[i.mashin.nom_in_l] = [0.0]
                        else:
                            try:
                                row[i.mashin.nom_in_l].append(((i.new_won - i.old_won) * i.mashin.el_coef)/((i.new_enter - i.old_enter) * i.mashin.el_coef)*100)
                            except ZeroDivisionError:
                                row[i.mashin.nom_in_l].append(0.0)
                    else:

                        if i.mashin.nom_in_l not in row:
                            try:
                                row[i.mashin.nom_in_l] = [((i.new_exit - i.old_exit) * i.mashin.el_coef)/((i.new_enter - i.old_enter) * i.mashin.el_coef)*100]
                            except ZeroDivisionError:
                                row[i.mashin.nom_in_l] = [0.0]
                        else:
                            try:
                                row[i.mashin.nom_in_l].append(((i.new_won - i.old_won) * i.mashin.el_coef)/((i.new_enter - i.old_enter) * i.mashin.el_coef)*100)
                            except ZeroDivisionError:
                                row[i.mashin.nom_in_l].append(0.0)
            elif self.m_radioBtn14.GetValue() is True:

                for i in self.db_row:
                    if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                        X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                    if self.m_radioBtn28.GetValue() is False:
                        if i.mashin.maker.name not in row:
                            try:
                                row[i.mashin.maker.name] = [((i.new_exit - i.old_exit) * i.mashin.el_coef)/((i.new_enter - i.old_enter) * i.mashin.el_coef)*100]
                            except ZeroDivisionError:
                                row[i.mashin.maker.name] = [0.0]
                        else:
                            try:
                                row[i.mashin.maker.name].append(((i.new_exit - i.old_exit) * i.mashin.el_coef)/((i.new_enter - i.old_enter) * i.mashin.el_coef)*100)
                            except ZeroDivisionError:
                                row[i.mashin.maker.name].append(0.0)
                    else:
                        if i.mashin.maker.name not in row:
                            try:
                                row[i.mashin.maker.name] = [((i.new_won - i.old_won) * i.mashin.el_coef)/((i.new_bet - i.old_bet) * i.mashin.el_coef)*100]
                            except ZeroDivisionError:
                                row[i.mashin.maker.name] = [0.0]
                        else:
                            try:
                                row[i.mashin.maker.name].append(((i.new_won - i.old_won) * i.mashin.el_coef)/((i.new_bet - i.old_bet) * i.mashin.el_coef)*100)
                            except ZeroDivisionError:
                                row[i.mashin.maker.name].append(0.0)
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name, x_title=x_title, y_title=y_title, X=X)

    
class BillGet(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn28.Hide()
        self.m_radioBtn29.Hide()
#         self.m_radioBtn21.Hide()
        
    def add_choice(self):
        choise = [gui_lib.msg.mashin_report_BillGet[1]]
        if self.m_radioBtn9.GetValue() is True:
            data = libs.DB.get_all(libs.models.Maker)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_BillGet[2])
        elif self.m_radioBtn8.GetValue() is True:
            data = libs.DB.get_all(libs.models.Model)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_BillGet[3])
        elif self.m_radioBtn41.GetValue() is True:
            data = libs.DB.get_all(libs.models.Flor)
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_BillGet[4])
        elif self.m_radioBtn21.GetValue() ==  True:
            self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_BillGet[5])
            data = libs.DB.get_all(libs.models.User)
        for i in data:
            choise.append(i.name)
        self.m_choice3.SetItems(choise)
        self.m_choice3.SetSelection(0)     
    
    def table_report(self):
        template = 'report.html'
#         template_name = u'Изваден Бил' 
        template_name = gui_lib.msg.mashin_report_BillGet['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.mashin_report_BillGet[6],
                   gui_lib.msg.mashin_report_BillGet[7],
                   gui_lib.msg.mashin_report_BillGet[8],
                   gui_lib.msg.mashin_report_BillGet[9]]
            row = []
            sums = [u'', u'', gui_lib.msg.mashin_report_BillGet[10], 0]
            for i in self.db_row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(str(i.mashin.nom_in_l))
                var.append(i.mashin.model.name)
                var.append("{:.2f}".format(i.bill_new - i.bill_old))
                sums[3] = sums[3] + (i.bill_new - i.bill_old)
#                 var.append("{:.2f}".format((i.new_exit - i.old_exit)*i.mashin.el_coef))
#                 total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
#                 var.append("{:.2f}".format(total))
                row.append(var)
            row.append([u'-'*15, u'-'*15, u'-'*15,u'-'*15])
            sums[3] = "{:.2f}".format(sums[3])
            row.append(sums)
        elif self.m_radioBtn15.GetValue() is True:
            col = [gui_lib.msg.mashin_report_BillGet[7],
                   gui_lib.msg.mashin_report_BillGet[8],
                   gui_lib.msg.mashin_report_BillGet[9]]
            sums = [u'', gui_lib.msg.mashin_report_BillGet[10], 0]
            row = []
            var_dict = {}
            for i in self.db_row:
                var = []
                if i.mashin_id not in var_dict:
                    var.append(str(i.mashin.nom_in_l))
                    var.append(i.mashin.model.name)
                    var.append(i.bill_new - i.bill_old)
                    sums[2] = sums[2] + (i.bill_new - i.bill_old)
#                     var.append((i.new_exit - i.old_exit)*i.mashin.el_coef)
#                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
                    var.append(i.mashin.id)
                    var_dict[i.mashin_id] = var
                else:
                    var_dict[i.mashin_id][2] = var_dict[i.mashin_id][2] + (i.bill_new - i.bill_old)
                    sums[2] = sums[2] + (i.bill_new - i.bill_old)
#                     var_dict[i.mashin.nom_in_l][3] = var_dict[i.mashin.nom_in_l][3] + (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     var_dict[i.mashin.nom_in_l][4] = var_dict[i.mashin.nom_in_l][4] + total
            var_dict = self.sort_by_nom_in_l(var_dict)
            for i in sorted(list(var_dict.keys())):
                var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
#                 var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
#                 var_dict[i][4] = "{:.2f}".format(var_dict[i][4])
                row.append(var_dict[i])
            row.append([u'-'*15, u'-'*15, u'-'*15])
            sums[2] = "{:.2f}".format(sums[2])
            row.append(sums)
        elif self.m_radioBtn14.GetValue() is True:
            col = [gui_lib.msg.mashin_report_BillGet[2],
                   gui_lib.msg.mashin_report_BillGet[9]]
            sums = [gui_lib.msg.mashin_report_BillGet[10], 0]
            row = []
            var_dict = {}
            for i in self.db_row:
                var = []
                if i.mashin.maker.name not in var_dict:
                    var.append(i.mashin.maker.name)
#                     var.append(i.mashin.model.name)
                    var.append(i.bill_new - i.bill_old)
                    sums[1] = sums[1] + (i.bill_new - i.bill_old)
#                     var.append((i.new_exit - i.old_exit)*i.mashin.el_coef)
#                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     var.append(total)
                    var_dict[i.mashin.maker.name] = var
                else:
                    var_dict[i.mashin.maker.name][1] = var_dict[i.mashin.maker.name][1] + (i.bill_new - i.bill_old)
                    sums[1] = sums[1] + (i.bill_new - i.bill_old)
#                     var_dict[i.mashin.maker.name][2] = var_dict[i.mashin.maker.name][2] + (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     var_dict[i.mashin.maker.name][3] = var_dict[i.mashin.maker.name][3] + total
                    
            for i in sorted(list(var_dict.keys())):
                var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
#                 var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
#                 var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
                row.append(var_dict[i])
            row.append([u'-'*15, u'-'*15])
            sums[1] = "{:.2f}".format(sums[1])
            row.append(sums)
        elif self.m_radioBtn7.GetValue() is True:
            col = [gui_lib.msg.mashin_report_BillGet[6],
                   gui_lib.msg.mashin_report_BillGet[9]]
            row = []
            sums = [gui_lib.msg.mashin_report_BillGet[10], 0]
            var_dict = {}
            for i in self.db_row:
                var = []
                if libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y') not in var_dict:
                    var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y'))
#                     var.append(i.mashin.model.name)
                    var.append(i.bill_new - i.bill_old)
                    sums[1] = sums[1] + (i.bill_new - i.bill_old)
#                     var.append((i.new_exit - i.old_exit)*i.mashin.el_coef)
#                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     var.append(total)
                    var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')] = var
                else:
                    var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][1] = var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][1] + (i.bill_new - i.bill_old)
                    sums[1] = sums[1] + (i.bill_new - i.bill_old)
#                     var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][2] = var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][2] + (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][3] = var_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][3] + total
                    
            for i in sorted(list(var_dict.keys())):
                var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
#                 var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
#                 var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
                row.append(var_dict[i])
            row.append([u'-'*15, u'-'*15])
            sums[1] = "{:.2f}".format(sums[1])
            row.append(sums)
        elif self.m_radioBtn42.GetValue() is True:
            col = [gui_lib.msg.mashin_report_BillGet[4],
                   gui_lib.msg.mashin_report_BillGet[9]]
            row = []
            sums = [gui_lib.msg.mashin_report_BillGet[10], 0]
            var_dict = {}
            for i in self.db_row:
                var = []
                if i.flor_id == None:
                    flor = gui_lib.msg.mashin_report_BillGet[1]
                else:
                    flor = libs.DB.get_one_where(libs.models.Flor, id=i.flor_id).name
                if flor not in var_dict:
                    var.append(flor)
#                     var.append(i.mashin.model.name)
                    var.append(i.bill_new - i.bill_old)
                    sums[1] = sums[1] + (i.bill_new - i.bill_old)
#                     var.append((i.new_exit - i.old_exit)*i.mashin.el_coef)
#                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     var.append(total)
                    var_dict[flor] = var
                else:
                    var_dict[flor][1] = var_dict[flor][1] + (i.bill_new - i.bill_old)
                    sums[1] = sums[1] + (i.bill_new - i.bill_old)
#                     var_dict[flor][2] = var_dict[flor][2] + (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     total = (i.new_enter - i.old_enter)*i.mashin.el_coef - (i.new_exit - i.old_exit)*i.mashin.el_coef
#                     var_dict[flor][3] = var_dict[flor][3] + total
                    
            for i in sorted(list(var_dict.keys())):
                var_dict[i][1] = "{:.2f}".format(var_dict[i][1])
#                 var_dict[i][2] = "{:.2f}".format(var_dict[i][2])
#                 var_dict[i][3] = "{:.2f}".format(var_dict[i][3])
                row.append(var_dict[i])
            row.append([u'-'*15, u'-'*15])
            sums[1] = "{:.2f}".format(sums[1])
            row.append(sums)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.mashin_report_BillGet['name'], row=row, col=col, template_name=template_name, template=template)
    
    def pic_report(self):
        template_name = gui_lib.msg.mashin_report_BillGet['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        row = {}
        y_label = 'BILL'
        x_label = 'Date'
        X = []
        if self.m_radioBtn10.GetValue() is True:
            for i in self.db_row:
                total =(i.bill_new - i.bill_old)
                # if total != 0:
                if i.mashin.nom_in_l not in row:
                    row[i.mashin.nom_in_l] = [total]
                else:
                    row[i.mashin.nom_in_l].append(total)
            tmp = []
            for i in row:
                X.append(i)
                total = 0
                for b in row[i]:
                    total += b
                tmp.append(total)
            row = tmp
        elif self.m_radioBtn15.GetValue() is True:
            for i in self.db_row:
                total =(i.bill_new - i.bill_old)
                # if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                #     X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if i.mashin.nom_in_l not in row:
                    row[i.mashin.nom_in_l] = [total]
                else:
                    row[i.mashin.nom_in_l].append(total)
            tmp = []
            for i in row:
                X.append(i)
                total = 0
                for b in row[i]:
                    total += b
                tmp.append(total)
            row = tmp
        elif self.m_radioBtn14.GetValue() is True:
            for i in self.db_row:
                total =(i.bill_new - i.bill_old)
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if i.mashin.maker.name not in row:
                    row[i.mashin.maker.name] = [total]
                else:
                    row[i.mashin.maker.name].append(total)

        elif self.m_radioBtn7.GetValue() is True:
            # x_label = 'Count'
            for i in self.db_row:
                total =(i.bill_new - i.bill_old)
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in row:
                    # X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                    row[libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d')] = [total]
                else:
                    row[libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d')].append(total)
            tmp = []
            for i in row:
                X.append(i)
                total = 0
                for b in row[i]:
                    total += b
                tmp.append(total)
            row = tmp
        elif self.m_radioBtn42.GetValue() is True:
            for i in self.db_row:
                total =(i.bill_new - i.bill_old)
                if libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d') not in X:
                    X.append(libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d'))
                if i.mashin.flor.name not in row:
                    row[i.mashin.flor.name] = [total]
                else:
                    row[i.mashin.flor.name].append(total)
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name, y_title=y_label, x_title=x_label,
                                                                 X=X)
        # self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)

class MCurenState(gui.MCurenState):
    def __init__(self, parent):
        gui.MCurenState.__init__(self, parent)
        self.parent = parent
        self.SetTitle(gui_lib.msg.mashin_report_MCurenState['name'])
        self.m_checkBox9.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_checkBox9'])
        self.m_checkBox3.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_checkBox3'])
        self.m_checkBox4.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_checkBox4'])
        self.m_checkBox81.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_checkBox81'])
        self.m_checkBox5.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_checkBox5'])
        self.m_checkBox7.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_checkBox7'])
        self.m_checkBox6.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_checkBox6'])
        self.m_checkBox8.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_checkBox8'])
        self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_staticText7'])
        self.m_staticText5.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_staticText5'])
        self.m_staticText4.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_staticText4'])
        self.m_button8.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_button8'])
        self.m_button6.SetLabel(gui_lib.msg.mashin_report_MCurenState['m_button6'])
        if self.parent.USER.grup.right != None:
            right = self.parent.USER.grup.from_json()
            if 2 in right['diff']:
                self.m_checkBox8.Show()
            else:
                self.m_checkBox8.SetValue(False)
                self.m_checkBox8.Hide()
        self.col = None
        self.refresh_time = 2
        self.add_choice()
               
    def add_choice(self):
        
        choise = []
        for i in range(11):
            choise.append(str(i))
        self.m_choice3.SetItems(choise)
        self.m_choice3.SetSelection(0)
       
       
    def OnGo(self, event):
        self.col = [gui_lib.msg.mashin_report_MCurenState[1],
                    gui_lib.msg.mashin_report_MCurenState[2],
                    gui_lib.msg.mashin_report_MCurenState[3]]
#         self.col.append()
        if self.m_checkBox9.GetValue() is True:
            self.col.append(gui_lib.msg.mashin_report_MCurenState['m_checkBox9'])
        if self.m_checkBox6.GetValue() is True:
            self.col.append(gui_lib.msg.mashin_report_MCurenState['m_checkBox6'])
        if self.m_checkBox7.GetValue() is True:
            self.col.append(gui_lib.msg.mashin_report_MCurenState['m_checkBox7'])
        if self.m_checkBox3.GetValue() is True:
            self.col.append(gui_lib.msg.mashin_report_MCurenState['m_checkBox3'])
        if self.m_checkBox4.GetValue() is True:
            self.col.append(gui_lib.msg.mashin_report_MCurenState['m_checkBox4'])
        if self.m_checkBox81.GetValue() is True:
            self.col.append(gui_lib.msg.mashin_report_MCurenState['m_checkBox81'])
        if self.m_checkBox5.GetValue() is True:
            self.col.append(gui_lib.msg.mashin_report_MCurenState['m_checkBox5'])
        if self.m_checkBox8.GetValue() is True:
            self.col.append(gui_lib.msg.mashin_report_MCurenState['m_checkBox8'])
        
        if len(self.col) == 0:
            dial = wx.MessageDialog(self, *gui_lib.msg.COL_SELECT_IN_REPORT_CURENTSTATE)
            dial.ShowModal()
            return
        self.refresh_time =  self.m_choice3.GetString(self.m_choice3.GetSelection())
        self.Destroy()

    def OnClose(self, event):
        self.col = None
        self.Destroy()

class EditN(gui.Xls):
    def __init__(self, parent, nom):
        self.parent = parent
        gui.Xls.__init__(self, self.parent)
        self.m_dirPicker1.Hide()
        self.nom = nom
        self.m_textCtrl1.SetValue(self.nom)
        self.SetTitle(gui_lib.msg.EditOrderNom['name'])
        self.m_button14.SetLabel(gui_lib.msg.EditOrderNom['m_button14'])
        self.m_button13.SetLabel(gui_lib.msg.EditOrderNom['m_button13'])
        self.m_textCtrl1.SetToolTip(gui_lib.msg.EditOrderNom['m_textCtrl1'])
        self.Fit()

    def OnClose( self, event ):
        self.Destroy()

    def OnExport( self, event ):
        self.nom = int(self.m_textCtrl1.GetValue())
        self.OnClose(event)

class EditDate(gui.Xls):
    def __init__(self, parent, dates):
        self.parent = parent
        gui.Xls.__init__(self, self.parent)
        self.m_dirPicker1.Hide()
        self.dates = dates
        self.m_textCtrl1.SetValue(self.dates)
        self.SetTitle(gui_lib.msg.EditOrderDates['name'])
        self.m_button14.SetLabel(gui_lib.msg.EditOrderDates['m_button14'])
        self.m_button13.SetLabel(gui_lib.msg.EditOrderDates['m_button13'])
        self.m_textCtrl1.SetToolTip(gui_lib.msg.EditOrderDates['m_textCtrl1'])
        self.close = True
        self.Fit()

    def OnClose( self, event ):
        self.Destroy()

    def OnExport( self, event ):
        self.dates = self.m_textCtrl1.GetValue()
        self.close = False
        self.OnClose(event)

class OrderEdit(gui.EditOrder):
    def __init__(self, parent, infos):
        gui.EditOrder.__init__(self, parent)
        self.parent = parent
        self.SetTitle(gui_lib.msg.mashin_report_OrderEdit['name'])
        self.m_button7.SetLabel(gui_lib.msg.mashin_report_OrderEdit['m_button7'])
        self.m_button8.SetLabel(gui_lib.msg.mashin_report_OrderEdit['m_button8'])
        self.m_button12.SetLabel(gui_lib.msg.mashin_report_OrderEdit['m_button12'])
        self.m_button9.SetLabel(gui_lib.msg.mashin_report_OrderEdit['m_button9'])
        self.m_button17.SetLabel(gui_lib.msg.mashin_report_OrderEdit['m_button17'])
        self.m_button18.SetLabel(gui_lib.msg.mashin_report_OrderEdit['m_button18'])
        self.m_button19.SetLabel(gui_lib.msg.mashin_report_OrderEdit['m_button19'])
        self.m_button20.SetLabel(gui_lib.msg.mashin_report_OrderEdit['m_button20'])
        self.info = infos
        self.user = self.parent.GetParent().GetParent().GetParent().GetParent().GetParent().USER

        if self.user.grup.right != None:
            right = self.user.grup.from_json()
            if 1 in right['report']:
                self.m_listCtrl4.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnChange)
                self.m_button7.Show()
                self.m_button17.Show()
                self.m_button18.Show()
                self.m_button19.Show()
                self.m_button20.Show()

        self.m_listCtrl4.InsertColumn(0, gui_lib.msg.mashin_report_OrderEdit[1])
        self.m_listCtrl4.InsertColumn(1, gui_lib.msg.mashin_report_OrderEdit[2])
        self.m_listCtrl4.InsertColumn(2, gui_lib.msg.mashin_report_OrderEdit[3])
        self.m_listCtrl4.InsertColumn(3, gui_lib.msg.mashin_report_OrderEdit[4])
        self.m_listCtrl4.InsertColumn(4, gui_lib.msg.mashin_report_OrderEdit[5])
        self.m_listCtrl4.InsertColumn(5, gui_lib.msg.mashin_report_OrderEdit[6])
        self.m_listCtrl4.InsertColumn(6, gui_lib.msg.mashin_report_OrderEdit[7])
        self.m_listCtrl4.InsertColumn(7, gui_lib.msg.mashin_report_OrderEdit[8])
        self.m_listCtrl4.InsertColumn(8, gui_lib.msg.mashin_report_OrderEdit[9])
        self.OrderDict = {}

#         self.row = {}
        self.add_info()
        self.N = self.info.doc_data_json['nom']
        self.Dates = self.info.doc_data_json['doc_date']
        self._resize(None)

    def OnDell( self, event ):
        libs.DB.delete_object(self.info)
        libs.DB.commit()
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()
        self.OnClose(event)


    def OnFixRow(self, event):
        try:
            dial = EditN(self, str(len(self.info.doc_data_json['ram_clear_count'])))
            dial.ShowModal()
        except:
            return
        data = dial.nom
        ram = []
        for i in range(data):
            ram.append(i)
        self.info.doc_data_json['ram_clear_count'] = ram
        # print self.info.doc_data_json['ram_clear_count']

    def OnDate( self, event ):
        dial = EditDate(self, self.info.doc_data_json['doc_date'])
        dial.ShowModal()
        if dial.close is False:
            self.info.doc_data_json['doc_date'] = dial.dates
        if 'for_mounth' in self.info.doc_data_json and dial.close is False:
            self.info.doc_data_json['doc_year'] = self.info.doc_data_json['doc_date'][6:]
            self.info.doc_data_json['for_mounth'] = gui_lib.msg.mounths[self.info.doc_data_json['doc_date'][3:5]]

    def OnN( self, event ):
        dial = EditN(self, str(self.info.doc_data_json['nom']))
        dial.ShowModal()
        self.info.doc_data_json['nom'] = dial.nom
        self.info.doc_nom = dial.nom

    def add_info(self, doc_data=None):
        self.m_listCtrl4.DeleteAllItems()
        if doc_data == None:
            self.info.doc_data_json = json.loads(self.info.doc_data)
        else:
            self.info.doc_data_json = doc_data
        index = 0
        tmp = {}
        for i in  self.info.doc_data_json['row']:
            try:
                tmp[int(i)] =  self.info.doc_data_json['row'][i]
            except ValueError:
                tmp[float(i)] = self.info.doc_data_json['row'][i]
        
        for i in sorted(tmp):
            self.m_listCtrl4.InsertItem(index, str(i))
            self.m_listCtrl4.SetItem(index, 1, str(tmp[i]['serial']))
            self.m_listCtrl4.SetItem(index, 2, str(tmp[i]['new_el_in']))
            self.m_listCtrl4.SetItem(index, 3, str(tmp[i]['new_el_out']))
            self.m_listCtrl4.SetItem(index, 4, str(tmp[i]['new_mex_in']))
            self.m_listCtrl4.SetItem(index, 5, str(tmp[i]['new_mex_out']))
            self.m_listCtrl4.SetItem(index, 6, str(tmp[i]['total_in']))
            self.m_listCtrl4.SetItem(index, 7, str(tmp[i]['total_out']))
            self.m_listCtrl4.SetItem(index, 8, str(tmp[i]['total']))
            index += 1
        
#         self.info.doc_data['row'] = tmp
        
    def _resize(self, event):
        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width*0.85, self.height*0.85))
        self.m_listCtrl4.SetMinSize((self.width*0.75, self.height*0.75))
        self.m_listCtrl4.SetColumnWidth(0, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(1, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(2, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(3, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(4, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(5, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(6, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(7, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(8, self.width * 0.08)
        self.Layout()
    
    def data_format(self):
        data = {}
        if self.info.day_report is True:
            data['doc_tupe'] = gui_lib.msg.mashin_report_OrderEdit[10]
        else:
            data['doc_tupe'] = gui_lib.msg.mashin_report_OrderEdit[11]
        tmp = {}
        for i in  self.info.doc_data_json['row']:
            try:
                tmp[int(i)] =  self.info.doc_data_json['row'][i]
            except ValueError:
                tmp[float(i)] = self.info.doc_data_json['row'][i]
        data['nom'] = str(self.info.doc_nom)
        data['doc_date'] = self.info.doc_data_json['doc_date']
        data['doc_type'] = self.info.doc_data_json['doc_type']
        data['nom'] = self.info.doc_data_json['nom']
        data['row'] = tmp
        data['total'] = self.info.doc_data_json['total']
        data['sum_all_total'] = self.info.doc_data_json['sum_all_total']
        data['total_in'] = self.info.doc_data_json['total_in']
        data['total_out'] = self.info.doc_data_json['total_out']
        data['casino_info'] = self.info.doc_data_json['casino_info']
        data['manager'] = self.info.doc_data_json['manager']
        if 'user_name' in self.info.doc_data_json:
            data['user_name'] = self.info.doc_data_json['user_name']
        if 'new_order' in self.info.doc_data_json:
            data['new_order'] = self.info.doc_data_json['new_order']
        if 'for_mounth' in self.info.doc_data_json:
            data['for_mounth'] = self.info.doc_data_json['for_mounth']
            data['doc_year'] = self.info.doc_data_json['doc_year']
        try:
            data['ram_clear_time'] = self.info.doc_data_json['ram_clear_time']
            data['ram_clear'] = self.info.doc_data_json['ram_clear']
        except Exception as e:
            pass
        try:
            data['ram_clear_count'] = self.info.doc_data_json['ram_clear_count']
        except:
            pass
        try:
            data['jp_down'] = self.info.doc_data_json['jp_down']
            data['jp_monu'] = self.info.doc_data_json['jp_monu']
        except:
            pass
        return data
    
    def OnSendMail(self, event):
        try:
            data = self.data_format()
        
            html = gui_lib.printer.render('day_report.html', data)
            send_to = self.user.grup.boss_mail
            send_mail_to = send_to.split(',')
            subject = self.user.grup.subject
            # subject = json.loads(subject.value)[libs.conf.ID]
            for i in send_mail_to:
                libs.sendmail.Gmail(html, i, subject)
            dlg = wx.MessageDialog(self, *gui_lib.msg.MAIL_SEND)
            dlg.ShowModal()
        except Exception as e:
            dlg = wx.MessageDialog(self, *gui_lib.msg.MAIL_NOT_SEND)
            dlg.ShowModal()
            raise e
            

    def OnPrint(self, event):
        try:
            data = self.data_format()
            if libs.conf.PRINT_DIRECT is True:
                ranges = 2
            else:
                ranges = 1
            gui_lib.printer.Print( self, 'day_report.html' ,data, ranges)
            if libs.conf.PRINT_DIRECT is True:
                dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_OK)
                dlg.ShowModal()
        except Exception as e:
            dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_NOT_OK)
            dlg.ShowModal()
            raise e
#         self.Destroy()

    def OnChange( self, event ):
        nom_in_l = self.m_listCtrl4.GetItemText(self.m_listCtrl4.GetFirstSelected())
        data = self.info.doc_data_json['row'][nom_in_l]
        dial = EditDayReportMashin(self, data, nom_in_l)
        dial.ShowModal()
        dial_mashin =  dial.mashin
        if dial.mashin != None:
            self.info.doc_data_json['row'][nom_in_l] = dial_mashin
            total_out = 0
            total_in = 0
            total = 0
            for i in self.info.doc_data_json['row']:
                total_in += float(self.info.doc_data_json['row'][i]['total_in'])
                total_out += float(self.info.doc_data_json['row'][i]['total_out'])
                total += float(self.info.doc_data_json['row'][i]['total'])
            self.info.doc_data_json['total_in'] = "{0:.2f}".format(total_in)
            self.info.doc_data_json['total_out'] = "{0:.2f}".format(total_out)
            self.info.doc_data_json['total'] = "{0:.2f}".format(total)
            self.info.doc_data_json['sum_all_total'] = "{0:.2f}".format(total)
            self.add_info(self.info.doc_data_json)
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()


    def OnSave(self, event):
        if self.info.doc_data_json['doc_tupe'] == gui_lib.msg.mashin_report_OrderEdit[10]:
            all_ord = libs.DB.get_all_where(libs.models.DayReport, id__gte=self.info.id, day_report=True)
        else:
            all_ord = libs.DB.get_all_where(libs.models.DayReport, id__gte=self.info.id, day_report=False)
        my_change = self.info.doc_data_json.copy()

        for item in all_ord:
            item.doc_data = json.loads(item.doc_data)
            item.doc_data['total_in'] = 0
            item.doc_data['total_out'] = 0
            item.doc_data['total'] = 0
            item.doc_data['sum_all_total'] = 0

            for b in item.doc_data['row']:
                item.doc_data['row'][b]['total_in'] = float(item.doc_data['row'][b]['total_in'])
                item.doc_data['row'][b]['total_out'] = float(item.doc_data['row'][b]['total_out'])
                item.doc_data['row'][b]['total'] = float(item.doc_data['row'][b]['total'])

                item.doc_data['row'][b]['total_in'] = (item.doc_data['row'][b]['new_el_in'] - my_change['row'][b]['new_el_in']) * my_change['row'][b]['coef']
                item.doc_data['row'][b]['total_out'] = (item.doc_data['row'][b]['new_el_out'] - my_change['row'][b]['new_el_out']) * my_change['row'][b]['coef']
                item.doc_data['row'][b]['total'] = item.doc_data['row'][b]['total_in'] - item.doc_data['row'][b]['total_out']
                item.doc_data['total_in'] += item.doc_data['row'][b]['total_in']
                item.doc_data['total_out'] += item.doc_data['row'][b]['total_out']
                item.doc_data['total'] += item.doc_data['row'][b]['total']
                item.doc_data['sum_all_total'] += item.doc_data['row'][b]['total']

            for b in item.doc_data['row']:
                item.doc_data['row'][b]['total_in'] = "{:.2f}".format(item.doc_data['row'][b]['total_in'])
                item.doc_data['row'][b]['total_out'] = "{:.2f}".format(item.doc_data['row'][b]['total_out'])
                item.doc_data['row'][b]['total'] = "{:.2f}".format(item.doc_data['row'][b]['total'])

            item.doc_data['sum_all_total'] = "{:.2f}".format(item.doc_data['sum_all_total'] )
            item.doc_data['total_in'] = "{:.2f}".format(item.doc_data['total_in'])
            item.doc_data['total_out'] = "{:.2f}".format(item.doc_data['total_out'])
            item.doc_data['total'] = "{:.2f}".format(item.doc_data['total'])
            my_change = item.doc_data.copy()
            item.doc_data = json.dumps(item.doc_data)
            libs.DB.add_object_to_session(item)
                # item.doc_data['row'][b]['old_el_in'] = my_change['row'][b]['new_el_in']
                # item.doc_data['row'][b]['old_el_out'] = my_change['row'][b]['new_el_out']
                # item.doc_data['row'][b]['old_mex_in'] = my_change['row'][b]['new_mex_in']
                # item.doc_data['row'][b]['old_mex_out'] = my_change['row'][b]['new_mex_out']

        if self.N != self.info.doc_data_json['nom']:
            self.info.doc_nom = self.info.doc_data_json['nom']
        # print self.Dates, self.info.doc_data_json['doc_date']
        if self.Dates != self.info.doc_data_json['doc_date']:
            my_date = libs.models.TZ.str_to_date(self.info.doc_data_json['doc_date'], '%d-%m-%Y')
            self.info.pub_time = libs.models.TZ.date_to_str(my_date, '%Y-%m-%d') + ' ' + libs.models.TZ.date_to_str(self.info.pub_time, '%H:%M:%S')
        self.info.doc_data = json.dumps(self.info.doc_data_json)
        libs.DB.add_object_to_session(self.info)
        obj = libs.DB.make_obj(libs.models.GetCounterError)
        obj.user_id = self.user.id
        obj.info = 'DAY OR MOUNTH ORDER EDIT: %s' % (self.info.id)
        libs.DB.add_object_to_session(obj)
        libs.DB.commit()
        self.OnClose(event)

    def OnClose(self, event):
        self.Destroy()    

class EditDayReportMashin(gui.EditDayReportMashin, gui_lib.keybords.Keyboard):

    def __init__(self, parent, mashin, nom_in_l):
        gui.EditDayReportMashin.__init__(self, parent)
        self.parent = parent
        self.SetTitle(gui_lib.msg.mashin_report_EditDayReportMashin['name'])
        self.m_staticText15.SetLabel(gui_lib.msg.mashin_report_EditDayReportMashin['m_staticText15'])
        self.m_staticText16.SetLabel(gui_lib.msg.mashin_report_EditDayReportMashin['m_staticText16'])
        self.m_staticText18.SetLabel(gui_lib.msg.mashin_report_EditDayReportMashin['m_staticText18'])
        self.m_staticText20.SetLabel(gui_lib.msg.mashin_report_EditDayReportMashin['m_staticText20'])
        self.m_staticText181.SetLabel(gui_lib.msg.mashin_report_EditDayReportMashin['m_staticText181'])
        self.m_staticText22.SetLabel(gui_lib.msg.mashin_report_EditDayReportMashin['m_staticText22'])
        self.m_button6.SetLabel(gui_lib.msg.mashin_report_EditDayReportMashin['m_button6'])
        self.m_button7.SetLabel(gui_lib.msg.mashin_report_EditDayReportMashin['m_button7'])

        self.mashin = mashin
        # print mashin.keys()
        self.nom_in_l = nom_in_l
        self.m_staticText161.SetLabel(str(nom_in_l))
        self.m_textCtrl8.SetValue(str(self.mashin['new_el_in']))
        self.m_textCtrl9.SetValue(str(self.mashin['new_el_out']))
        self.m_textCtrl10.SetValue(str(self.mashin['new_mex_in']))
        self.m_textCtrl6.SetValue(str(self.mashin['new_mex_out']))
        self.m_staticText22.SetLabel((str(self.mashin['total'])))
        self.m_textCtrl61.SetValue(str(self.mashin['total_in']))
        self.m_textCtrl7.SetValue(str(self.mashin['total_out']))
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl8.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl9.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl10.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl6.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl61.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl7.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
        self.Fit()

    def OnMathIn( self, event ):
        if self.m_textCtrl8.GetValue() == '':
            return
        ins = int(self.m_textCtrl8.GetValue())
        total_in = float(self.mashin['total_in'])
        total = float(self.mashin['total'])
        if ins == 0:
            total_in = 0
        elif ins < self.mashin['new_el_in']:
            total_in -= (self.mashin['new_el_in']-ins)*self.mashin['coef']
            # total -= total_in
        elif ins > self.mashin['new_el_in']:
            total_in += (ins - self.mashin['new_el_in']) * self.mashin['coef']
            # total += total_in
        # self.m_staticText22.SetLabel("{0:.2f}".format(total))
        self.m_textCtrl61.SetValue("{0:.2f}".format(total_in))
        self.TotalCalc()
        self.Fit()

    def OnMathOut( self, event ):
        # print self.m_textCtrl9.GetValue()
        if self.m_textCtrl9.GetValue() == '':
            return
        out = int(self.m_textCtrl9.GetValue())
        total_out = float(self.mashin['total_out'])
        total = float(self.mashin['total'])
        if out == 0:
            total_out=0
        elif out < self.mashin['new_el_out']:
            total_out -= (self.mashin['new_el_out'] - out) * self.mashin['coef']
            # total += total_out
        elif out > self.mashin['new_el_out']:
            total_out += (out - self.mashin['new_el_out']) * self.mashin['coef']
            # total -= total_out
        # self.m_staticText22.SetLabel("{0:.2f}".format(total))
        self.m_textCtrl7.SetValue("{0:.2f}".format(total_out))
        self.TotalCalc()
        self.Fit()

    def TotalCalc(self, event=None):

        try:
            out = float(self.m_textCtrl7.GetValue().replace(',', '.'))
            ins = float(self.m_textCtrl61.GetValue().replace(',', '.'))
            self.m_staticText22.SetLabel("{0:.2f}".format(ins-out))
        except ValueError:
            pass

    def OnClose( self, event ):
        self.mashin = None
        self.Destroy()

    def OnGo( self, event ):
        self.mashin['new_el_in'] = int(self.m_textCtrl8.GetValue())
        self.mashin['new_el_out'] = int(self.m_textCtrl9.GetValue())
        self.mashin['new_mex_in'] = int(self.m_textCtrl10.GetValue())
        self.mashin['new_mex_out'] = int(self.m_textCtrl6.GetValue())
        self.mashin['total'] = self.m_staticText22.GetLabel()
        self.mashin['total_in'] = "{0:.2f}".format(float(self.m_textCtrl61.GetValue().replace(',', '.')))
        self.mashin['total_out'] = "{0:.2f}".format(float(self.m_textCtrl7.GetValue().replace(',', '.')))
        self.Destroy()


class DayOrderShow(gui.RowSelect):
    def __init__(self, parent):
        self.parent = parent
        gui.RowSelect.__init__(self, parent)
        self.m_listCtrl2.InsertColumn(0, gui_lib.msg.mashin_report_DayOrderShow[5])
        self.m_listCtrl2.InsertColumn(1, gui_lib.msg.mashin_report_DayOrderShow[6])
        self.m_listCtrl2.InsertColumn(2, gui_lib.msg.mashin_report_DayOrderShow[7])
        self.m_listCtrl2.InsertColumn(3, gui_lib.msg.mashin_report_DayOrderShow[8])
        self.m_listCtrl2.InsertColumn(4, gui_lib.msg.mashin_report_DayOrderShow[9])
        self.m_listCtrl2.InsertColumn(5, gui_lib.msg.mashin_report_DayOrderShow[10])
        self.OrderDict = {}
        # m_radioBox1Choices = [u"Дневен", u"Месечен", u"Ордер"]
        self.m_radioBox1.SetString(0, gui_lib.msg.mashin_report_DayOrderShow[1])
        self.m_radioBox1.SetString(1, gui_lib.msg.mashin_report_DayOrderShow[2])
        self.m_radioBox1.SetString(2, gui_lib.msg.mashin_report_DayOrderShow[3])
        self.m_button6.SetLabel(gui_lib.msg.mashin_report_DayOrderShow['m_button6'])
        self._resize(None)


    def _resize(self, event):
        self.width, self.height = self.parent.GetParent().GetParent().GetParent().GetSize()
        # self.m_calendar1.SetMinSize((-1, self.height * 0.18))
        # self.m_calendar2.SetMinSize((-1, self.height * 0.18))
        self.m_scrolledWindow1.SetSize((self.width*0.6, self.height * 0.4))
        self.m_scrolledWindow1.SetMinSize((self.width * 0.6, self.height * 0.4))
        self.m_listCtrl2.SetMinSize((self.width*0.5, self.height * 0.50))
        self.m_listCtrl2.SetColumnWidth(0, self.width * 0.03)
        self.m_listCtrl2.SetColumnWidth(1, self.width * 0.08)
        self.m_listCtrl2.SetColumnWidth(2, self.width * 0.04)
        self.m_listCtrl2.SetColumnWidth(3, self.width * 0.10)
        self.m_listCtrl2.SetColumnWidth(4, self.width * 0.08)
        self.m_listCtrl2.SetColumnWidth(5, self.width * 0.12)
    
    def _get_order(self, start_date, end_date):
        data = self.m_radioBox1.GetSelection()
        if data == 0:
            data = True
        elif data == 1:
            data = False
        else:
            data = None
        if data != None:
            order = libs.DB.get_all_where(libs.models.DayReport, day_report=data, pub_time__btw=(start_date, end_date), order='id')
        else:
            order = libs.DB.get_all_where(libs.models.MonyRKO, pub_time__btw=(start_date, end_date), order='id')
        self.OrderDict = {}
        index = 0
        sum_all = 0
#         if order != None:
        for i in order:
            if data != None:
                doc_data = json.loads(i.doc_data)
                self.m_listCtrl2.InsertItem(index, str(i.id))
                self.m_listCtrl2.SetItem(index, 1, doc_data['doc_date'])
                self.m_listCtrl2.SetItem(index, 2, str(i.doc_nom))
                self.m_listCtrl2.SetItem(index, 3, str(i.user.name))
                self.m_listCtrl2.SetItem(index, 4, str(doc_data['sum_all_total']))
                self.m_listCtrl2.SetItem(index, 5, libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d %H:%M:%S'))
                self.OrderDict[index] = i
                sum_all += float(doc_data['sum_all_total'])
                index += 1
            else:
                doc_data = json.loads(i.rko_data)
                self.m_listCtrl2.InsertItem(index, str(i.id))
                self.m_listCtrl2.SetItem(index, 1, libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d %H:%M:%S'))
                self.m_listCtrl2.SetItem(index, 2, str(i.id))
                self.m_listCtrl2.SetItem(index, 3, str(i.user.name))
                self.m_listCtrl2.SetItem(index, 4, str(doc_data['total']))
                self.m_listCtrl2.SetItem(index, 5, libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d %H:%M:%S'))
                self.OrderDict[index] = i
                sum_all += float(doc_data['total'])
                index += 1

        self.m_listCtrl2.InsertItem(index, '-'*10)
        self.m_listCtrl2.SetItem(index, 1, '-'*10)
        self.m_listCtrl2.SetItem(index, 2, '-'*10)
        self.m_listCtrl2.SetItem(index, 3, '-'*10)
        self.m_listCtrl2.SetItem(index, 4, '-'*10)
        self.m_listCtrl2.SetItem(index, 5, '-' * 10)
        index += 1
        self.m_listCtrl2.InsertItem(index, '')
        self.m_listCtrl2.SetItem(index, 1, '')
        self.m_listCtrl2.SetItem(index, 2, '')
        self.m_listCtrl2.SetItem(index, 3, gui_lib.msg.mashin_report_DayOrderShow[4])
        self.m_listCtrl2.SetItem(index, 4, str(sum_all))
        self.m_listCtrl2.SetItem(index, 5, '')

    def refresh_order(self, start_date, end_date):
        self.m_listCtrl2.DeleteAllItems()
        self._get_order(start_date, end_date)
    
    def OnGo(self, event):
        start_date = self.m_calendar1.GetDate()
        start_date = start_date.Format('%Y-%m-%d')
        if self.m_radioBox1.GetSelection() < 2:
            start_date = libs.models.TZ.go_up_from_date(libs.models.TZ.str_to_date(start_date, '%Y-%m-%d'), 1)
            start_date = libs.models.TZ.date_to_str(start_date, '%Y-%m-%d')
        else:
            start_date = libs.models.TZ.str_to_date(start_date, '%Y-%m-%d')
            start_date = libs.models.TZ.date_to_str(start_date, '%Y-%m-%d')
            start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
                start_date + ' 00:00:00', start_date + ' 23:59:59'))
            if start_times == None:
                start_times = ' 09:00:00'
            else:
                start_times = libs.models.TZ.date_to_str(start_times.pub_time, ' %H:%M:%S')
            start_date = start_date + ' ' + start_times

#         print start_date
#         start_date = start_date.Format('%Y-%m-%d') + ' 00:00:00'
        
        end_date = self.m_calendar2.GetDate()
        end_date = end_date.Format('%Y-%m-%d') + ' 23:59:59'
        self.refresh_order(start_date, end_date)
    
    def OnEdit(self, event):
        try:
            item = self.OrderDict[self.m_listCtrl2.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            if self.m_radioBox1.GetSelection() == 2:
                doc_data = json.loads(item.rko_data)
                gui_lib.printer.Print(self, 'mony_order.html', doc_data)
                if libs.conf.PRINT_DIRECT is True:
                    dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_OK)
                    dlg.ShowModal()
            else:
                dialog = OrderEdit(self, item)
                dialog.ShowModal()
                self.OnGo(event)



#         self.OnGo(event)
    
    def OnClose(self, event):
        self.col = None
        self.Destroy()
        
        
        
# class H24(gui.H24):
#     def __init__(self, parent):
#         gui.H24.__init__(self, parent)
#         self.parent = parent
#         self.total_table = {}
#         self.m_checkBox141.SetLabel(gui_lib.msg.mashin_report_H24['m_checkBox141'])
#         self.m_checkBox14.SetLabel(gui_lib.msg.mashin_report_H24['m_checkBox14'])
#         self.m_checkBox181.SetLabel(gui_lib.msg.mashin_report_H24['m_checkBox181'])
#         self.m_checkBox6.SetLabel(gui_lib.msg.mashin_report_H24['m_checkBox6'])
#         self.m_checkBox17.SetLabel(gui_lib.msg.mashin_report_H24['m_checkBox17'])
#         self.m_button6.SetLabel(gui_lib.msg.mashin_report_H24['m_button6'])
#
#     def get_date(self):
#         self.start_date = self.m_calendar1.GetDate()
#         self.start_date = self.start_date.Format('%Y-%m-%d')
#
#         self.end_date = self.m_calendar2.GetDate()
#         self.end_date = self.end_date.Format('%Y-%m-%d')
#
#         #         start_date = start_date + ' ' + str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
#         start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
#             self.start_date + ' 00:00:00', self.start_date + ' 23:59:59'))
#         if start_times == None:
#             start_times = ' 09:00:00'
#         else:
#             start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')
#         self.start_date = self.start_date + ' ' + start_times
#         #         self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
#         #         self.start_date = libs.models.TZ.go_up_from_date(self.start_date, 1)
#         #         self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
#         # #
#         #         end_date = end_date + ' ' + str(self.m_spinCtrl3.GetValue()) + ':' + str(self.m_spinCtrl4.GetValue())
#         end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
#                                           pub_time__btw=(self.end_date + ' 00:00:00', self.end_date + ' 23:59:59'))
#         if end_times == None:
#             end_times = libs.models.TZ.now()
#             end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
#         else:
#             end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')
#         # end_date = end_date + ' ' + libs.models.TZ.date_to_str(end_times, '%H:%M')
#         self.end_date = self.end_date + ' ' + end_times
#
#     def sort_by_nom_in_l(self, row_dict):
#         sort_by_nom = {}
#         for i in row_dict:
#             sort_by_nom[int(row_dict[i][0])] = row_dict[i]
#         return sort_by_nom
#
#     def prihod_razhod(self, row):
#         # row.append(
#         #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#         # row.append(
#         #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#         row.append([gui_lib.msg.mashin_report_H24[1], u'', u'',
#                     gui_lib.msg.mashin_report_H24[2], u'', u'',
#                     gui_lib.msg.mashin_report_H24[3], u'', u'',
#                     gui_lib.msg.mashin_report_H24[4],
#                     u'', u''])
#         row.append([u'-' * 10, u'-' * 10, u'', u'-' * 10, u'-' * 10, u'', u'-' * 10, u'-' * 10, u'',
#                     u'-'*10, u'-'*10, u''])
#         row.append([gui_lib.msg.mashin_report_H24[5],
#                     gui_lib.msg.mashin_report_H24[6], u'',
#                     gui_lib.msg.mashin_report_H24[5],
#                     gui_lib.msg.mashin_report_H24[6], u'',
#                     gui_lib.msg.mashin_report_H24[7],
#                     gui_lib.msg.mashin_report_H24[6], u'',
#                     gui_lib.msg.mashin_report_H24[7],
#                     gui_lib.msg.mashin_report_H24[8], u''])
#         row.append([u'-' * 10, u'-' * 10, u'', u'-' * 10, u'-' * 10, u'', u'-' * 10, u'-' * 10, u'',
#                     u'-'*10, u'-'*10, u''])
#
#         bill = libs.DB.get_all_where(libs.models.BillTake,
#                                        pub_time__btw=(self.start_date, self.end_date),
#                                        order='id',
#                                        descs=False)
#
#         prihod = libs.DB.get_all_where(libs.models.Prihod,
#                                        pub_time__btw=(self.start_date, self.end_date),
#                                        order='id',
#                                        descs=False)
#
#         razhod = libs.DB.get_all_where(libs.models.Razhod,
#                                        pub_time__btw=(self.start_date, self.end_date),
#                                        order='id',
#                                        descs=False)
#
#
#         mony_back = libs.DB.get_all_where(libs.models.MonuBackPay, pub_time__btw=(self.start_date, self.end_date), order='id',
#                               descs=False)
#
#
#         bill_dict = {}
#         bill_get_total = 0
#         bill_row = []
#         for i in bill:
#             if i.user.name not in bill_dict:
#                 bill_dict[i.user.name] = i.mony
#             else:
#                 bill_dict[i.user.name] += i.mony
#             bill_get_total += i.mony
#         for i in sorted(bill_dict.keys()):
#             var = []
#             var.append(i)
#             var.append("{:.2f}".format(bill_dict[i]))
#             bill_row.append(var)
#
#         mony_back_dict = {}
#         mony_back_total = 0
#         mony_back_row = []
#         for i in mony_back:
#             if i.pub_user.name not in mony_back_dict:
#                 mony_back_dict[i.pub_user.name] = i.mony
#             else:
#                 mony_back_dict[i.pub_user.name] += i.mony
#             mony_back_total += i.mony
#         for i in sorted(mony_back_dict.keys()):
#             var = []
#             var.append(i)
#             var.append("{:.2f}".format(mony_back_dict[i]))
#             mony_back_row.append(var)
#
#
#         row_dict_prihod = {}
#         prihod_total = 0
#         prihod_row = []
#         for i in prihod:
#             if i.reson.name not in row_dict_prihod:
#                 row_dict_prihod[i.reson.name] = i.mony
#             else:
#                 row_dict_prihod[i.reson.name] = row_dict_prihod[i.reson.name] + i.mony
#             prihod_total += i.mony
#         for i in sorted(row_dict_prihod.keys()):
#             var = []
#             var.append(i)
#             var.append("{:.2f}".format(row_dict_prihod[i]))
#             prihod_row.append(var)
#
#         row_dict_razhod = {}
#         razhod_total = 0
#         razhod_row = []
#         for i in razhod:
#             if i.reson.name not in row_dict_razhod:
#                 row_dict_razhod[i.reson.name] = i.mony
#             else:
#                 row_dict_razhod[i.reson.name] = row_dict_razhod[i.reson.name] + i.mony
#             razhod_total += i.mony
#         for i in sorted(row_dict_razhod.keys()):
#             var = []
#             var.append(i)
#             var.append("{:.2f}".format(row_dict_razhod[i]))
#             razhod_row.append(var)
#
#         if len(prihod_row) > len(razhod_row):
#             for b in range(len(prihod_row) - len(razhod_row)):
#                 razhod_row.append([u'', u''])
#         elif len(prihod_row) < len(razhod_row):
#             for b in range(len(razhod_row) - len(prihod_row)):
#                 prihod_row.append([u'', u''])
#         if len(mony_back_row) > len(prihod_row):
#             for b in range(len(mony_back_row) - len(prihod_row)):
#                 prihod_row.append([u'', u''])
#                 razhod_row.append([u'', u''])
#         elif len(mony_back_row) < len(prihod_row):
#             for b in range(len(prihod_row) - len(mony_back_row)):
#                 mony_back_row.append([u'', u''])
#
#         if len(bill_row) > len(prihod_row):
#             for b in range(len(bill_row) - len(prihod_row)):
#                 prihod_row.append([u'', u''])
#                 razhod_row.append([u'', u''])
#                 mony_back_row.append([u'', u''])
#         elif len(bill_row) < len(prihod_row):
#             for b in range(len(prihod_row) - len(bill_row)):
#                 bill_row.append([u'', u''])
#
#         for i in range(len(razhod_row)):
#             row.append([prihod_row[i][0], prihod_row[i][1], u'', razhod_row[i][0], razhod_row[i][1],
#                          u'', mony_back_row[i][0], mony_back_row[i][1], u'', bill_row[i][0], bill_row[i][1], u''
#                         ])
#         row.append([u'-' * 10, u'-' * 10, u'', u'-' * 10, u'-' * 10, u'', u'-' *10, u'-'*10, u'',
#                     u'-'*10, u'-'*10, u''])
#         self.total_table['prihod'] = prihod_total
#         self.total_table['razhod'] = razhod_total
#         self.total_table['mony_back'] = mony_back_total
#         self.total_table['bill_get'] = bill_get_total
#         row.append([gui_lib.msg.mashin_report_H24[9], "{:.2f}".format(prihod_total),  u'', gui_lib.msg.mashin_report_H24[9], "{:.2f}".format(razhod_total),
#                     u'', gui_lib.msg.mashin_report_H24[9], "{:.2f}".format(mony_back_total), u'', gui_lib.msg.mashin_report_H24[9], "{:.2f}".format(bill_get_total), u''
#                     ])
#         row = self.mony_transfer(row)
#         return row
#
#     def jp_server(self, row):
#         # row.append(
#         #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#         # row.append(
#         #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#         row.append([gui_lib.msg.mashin_report_H24[10], u'', u'', u'', u'', u'', u'', gui_lib.msg.mashin_report_H24[11], u'', u'',
#                     u'', u''])
#         row.append([u'-' * 10, u'-' * 10, u'-'*10, u'-' * 10, u'-' * 10, u'-'*10, u'', u'-' * 10, u'-'*10,
#                    u'', u'', u''])
#         row.append([gui_lib.msg.mashin_report_H24[12],
#                     gui_lib.msg.mashin_report_H24[13],
#                     gui_lib.msg.mashin_report_H24[14],
#                     gui_lib.msg.mashin_report_H24[15],
#                     gui_lib.msg.mashin_report_H24[16],
#                     gui_lib.msg.mashin_report_H24[6], u'',
#                     gui_lib.msg.mashin_report_H24[7],
#                     gui_lib.msg.mashin_report_H24[6],
#                     u'', u'', u''])
#         row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'', u'-' * 10, u'-' * 10,
#                     u'', u'', u''])
#         lipsi = libs.DB.get_all_where(libs.models.BonusCartLog,
#                                                        pub_time__btw=(self.start_date, self.end_date),
#                                                        order='id',
#                                                        descs=False)
#         start_date = self.m_calendar1.GetDate()
#         start_date = start_date.Format('%Y-%m-%d')
#
#         end_date = self.m_calendar2.GetDate()
#         end_date = end_date.Format('%Y-%m-%d')
#         start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
#             start_date + ' 00:00:00', start_date + ' 23:59:59'))
#         if start_times == None:
#             start_times = ' 09:00:00'
#         else:
#             start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')
#
#         end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
#                                           pub_time__btw=(end_date + ' 00:00:00', end_date + ' 23:59:59'))
#         if end_times == None:
#             end_times = libs.models.TZ.now()
#             end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
#         else:
#             end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')
#
#         jp = self.data = libs.udp.send(ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, evt='GET_LOG', from_date=start_date, to_date=end_date)
#         jp_row = []
#         jp_row_sums = 0
#         for i in jp:
#             for b in jp[i]:
#                 #                 print self.data[i][b]
#                 for c in range(len(jp[i][b])):
#                     # print start_date, b, self.data[i][b][c]['hour'], start_times
#                     if b == start_date and jp[i][b][c]['hour'] < start_times:
#                         pass
#                     elif b == end_date and jp[i][b][c]['hour'] > end_times:
#                         pass
#                     else:
#                         jp_row_sums += round(jp[i][b][c]['sum'], 2)
#                         var = [str(b),
#                                str(jp[i][b][c]['hour']),
#                                str(jp[i][b][c]['mashin']),
#                                str(i),
#                                str(jp[i][b][c]['down']),
#                                str(round(jp[i][b][c]['sum'], 2)),
#                                ]
#                         jp_row.append(var)
#         self.total_table['jp'] = jp_row_sums
#
#         lipsi_total = 0
#         hold_nonus = 0
#         lipsi_row = []
#         lipsi_dict = {}
#         for i in lipsi:
#             if i.user.name not in lipsi_dict:
#                 lipsi_dict[i.user.name] = i.mony
#             else:
#                 lipsi_dict[i.user.name] += i.mony
#             if i.bonus_hold is True:
#                 hold_nonus += i.mony
#             lipsi_total += i.mony
#
#         for i in sorted(lipsi_dict.keys()):
#             var = []
#             var.append(i)
#             var.append("{:.2f}".format(lipsi_dict[i]))
#             lipsi_row.append(var)
#         self.total_table['bonus_cart'] = lipsi_total
#         self.total_table['bonus_hold'] = hold_nonus
#
#         if len(jp_row) > len(lipsi_row):
#             for b in range(len(jp_row) - len(lipsi_row)):
#                 lipsi_row.append([u'', u''])
#         else:
#             for b in range(len(lipsi_row) - len(jp_row)):
#                 lipsi_row.append([u'', u'', u'', u'', u'', u''])
#
#         for i in range(len(jp_row)):
#             row.append([jp_row[i][0], jp_row[i][1], jp_row[i][2], jp_row[i][3], jp_row[i][4],
#                          jp_row[i][5], u'', lipsi_row[i][0], lipsi_row[i][1], u'', u'', u''])
#         row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'', u'-' * 10, u'-' * 10,
#                     u'', u'', u''])
#         row.append([u'', u'', u'', u'', gui_lib.msg.mashin_report_H24[9], "{:.2f}".format(jp_row_sums), u'', gui_lib.msg.mashin_report_H24[9], "{:.2f}".format(lipsi_total),
#                     u'', u'', u''])
#         return row
#
#
#     def cust_bonus(self, row):
#         # row.append(
#         #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#         # row.append(
#         #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#         row.append([gui_lib.msg.mashin_report_H24[17],
#                     gui_lib.msg.mashin_report_H24[12],
#                     gui_lib.msg.mashin_report_H24[18],
#                     gui_lib.msg.mashin_report_H24[14],
#                     gui_lib.msg.mashin_report_H24[19],
#                     gui_lib.msg.mashin_report_H24[6], u'', u'', u'', u'',
#                     u'', u''])
#         row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'', u'', u'', u'',
#                     u'', u''])
#         cust = libs.DB.get_all_where(libs.models.BonusPay,
#                                        pub_time__btw=(self.start_date, self.end_date),
#                                        order='id',
#                                        descs=False)
#         cust_total = 0
#         count = 0
#
#         for i in cust:
#             count += 1
#             cust_total += i.mony
#             row.append([str(count), libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'),
#                         i.cust.name, str(i.device.nom_in_l), i.device.model.name, "{:.2f}".format(i.mony),
#                         u'', u'', u'', u'',u'', u''])
#
#         self.total_table['cust_bonus'] = cust_total
#         row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'', u'', u'', u'',
#                     u'', u''])
#         row.append([u'', u'', u'', u'', gui_lib.msg.mashin_report_H24[9], "{:.2f}".format(cust_total), u'', u'', u'', u'', u'', u''])
#         return row
#
#     def mony_transfer(self, row):
#         # row.append(
#         #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#         # row.append(
#         #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#         row.append([gui_lib.msg.mashin_report_H24[20], u'', u'', u'',
#                     gui_lib.msg.mashin_report_H24[21], u'', u'', u'', u'', u'',
#                     u'', u''])
#         row.append([u'-' * 10, u'-' * 10, u'-'*10, u'', u'-' * 10, u'-'*10, u'', u'', u'',
#                     u'', u'', u''])
#         row.append([gui_lib.msg.mashin_report_H24[22],
#                     gui_lib.msg.mashin_report_H24[23],
#                     gui_lib.msg.mashin_report_H24[6], u'',
#                     gui_lib.msg.mashin_report_H24[7],
#                     gui_lib.msg.mashin_report_H24[6], u'', u'', u'',
#                     u'', u'', u''])
#         row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'', u'-' * 10, u'-' * 10, u'', u'', u'',
#                     u'', u'', u''])
#
#         mony_transfer = libs.DB.get_all_where(libs.models.KasaTransfer, pub_time__btw=(self.start_date, self.end_date), order='id',
#                               descs=False)
#         lipsi = libs.DB.get_all_where(libs.models.Lipsi, pub_time__btw=(self.start_date, self.end_date), order='id',
#                               descs=False)
#         lipsi_total = 0
#         lipsi_row = []
#         lipsi_dict = {}
#         for i in lipsi:
#             if i.user.name not in lipsi_dict:
#                 lipsi_dict[i.user.name] = i.mony
#             else:
#                 lipsi_dict[i.user.name] += i.mony
#             lipsi_total += i.mony
#
#         for i in sorted(lipsi_dict.keys()):
#             var = []
#             var.append(i)
#             var.append("{:.2f}".format(lipsi_dict[i]))
#             lipsi_row.append(var)
#         self.total_table['lipsi'] = lipsi_total
#
#         transfer_total = 0
#         transfer_row = []
#         transfer_dict = {}
#         for i in mony_transfer:
#             transfer_dict[i.id] = [i.from_user.name, i.to_user.name, i.mony]
#             transfer_total += i.mony
#
#         for i in sorted(lipsi_dict.keys()):
#             var = []
#             var.append(i)
#             var.append("{:.2f}".format(lipsi_dict[i]))
#             lipsi_row.append(var)
#         self.total_table['transfer'] = transfer_total
#         return row
#
#     def mashin_in_out(self, row):
#         row.append([gui_lib.msg.mashin_report_H24[14],
#                     gui_lib.msg.mashin_report_H24[19],
#                     gui_lib.msg.mashin_report_H24[24],
#                     gui_lib.msg.mashin_report_H24[25],
#                     gui_lib.msg.mashin_report_H24[26],
#                     gui_lib.msg.mashin_report_H24[27],
#                     gui_lib.msg.mashin_report_H24[28],
#                     gui_lib.msg.mashin_report_H24[29],
#                     gui_lib.msg.mashin_report_H24[30],
#                     gui_lib.msg.mashin_report_H24[31],
#                     gui_lib.msg.mashin_report_H24[32],
#                     gui_lib.msg.mashin_report_H24[33]])
#         row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10,
#                     u'-' * 10, u'-' * 10, u'-' * 10])
#         var_dict = {}
#         self.db_row = libs.DB.get_all_where(libs.models.Order, pub_time__btw=(self.start_date, self.end_date),
#                                             order='id')
#         sums = [u'', u'', u'', u'', u'', u'', u'', gui_lib.msg.mashin_report_H24[9], 0, 0, 0, 0]
#         for i in self.db_row:
#             var = []
#             if i.mashin_id not in var_dict:
#                 var.append(str(i.mashin.nom_in_l))
#                 var.append(i.mashin.model.name)
#                 var.append(str(i.old_enter))
#                 var.append(str(i.old_exit))
#                 var.append(str(i.new_enter))
#                 var.append(str(i.new_exit))
#                 var.append(str(i.bill_old))
#                 var.append(str(i.bill_new))
#                 var.append(i.bill_new - i.bill_old)
#                 var.append((i.new_enter - i.old_enter) * i.mashin.el_coef)
#                 var.append((i.new_exit - i.old_exit) * i.mashin.el_coef)
#                 total = ((i.new_enter - i.old_enter) * i.mashin.el_coef) - (
#                     (i.new_exit - i.old_exit) * i.mashin.el_coef)
#                 var.append(total)
#
#                 sums[8] = sums[8] + (i.bill_new - i.bill_old)
#                 sums[9] = sums[9] + (i.new_enter - i.old_enter) * i.mashin.el_coef
#                 sums[10] = sums[10] + (i.new_exit - i.old_exit) * i.mashin.el_coef
#                 sums[11] = sums[11] + total
#                 var_dict[i.mashin_id] = var
#             else:
#                 var_dict[i.mashin_id][4] = str(i.new_enter)
#                 var_dict[i.mashin_id][5] = str(i.new_exit)
#                 #                     var_dict[i.mashin_id][4] = str(i.new_enter)
#                 var_dict[i.mashin_id][7] = str(i.bill_new)
#
#                 var_dict[i.mashin_id][8] = var_dict[i.mashin_id][8] + (i.bill_new - i.bill_old)
#                 sums[8] = sums[8] + (i.bill_new - i.bill_old)
#
#                 var_dict[i.mashin_id][9] = var_dict[i.mashin_id][9] + (i.new_enter - i.old_enter) * i.mashin.el_coef
#                 sums[9] = sums[9] + (i.new_enter - i.old_enter) * i.mashin.el_coef
#
#                 var_dict[i.mashin_id][10] = var_dict[i.mashin_id][10] + (i.new_exit - i.old_exit) * i.mashin.el_coef
#                 sums[10] = sums[10] + (i.new_exit - i.old_exit) * i.mashin.el_coef
#
#                 total = ((i.new_enter - i.old_enter) * i.mashin.el_coef) - (
#                     (i.new_exit - i.old_exit) * i.mashin.el_coef)
#                 var_dict[i.mashin_id][11] = var_dict[i.mashin_id][11] + total
#                 sums[11] = sums[11] + total
#         sort_by_nom = self.sort_by_nom_in_l(var_dict)
#         #             for i in var_dict:
#         #                 sort_by_nom[int(var_dict[i][0])] = var_dict[i]
#
#         for i in sorted(sort_by_nom.keys()):
#             #                 sort_by_nom[i][4] = sort_by_nom[i][4]
#             #                 sort_by_nom[i][5] = sort_by_nom[i][5]
#             sort_by_nom[i][8] = "{:.2f}".format(sort_by_nom[i][8])
#             sort_by_nom[i][9] = "{:.2f}".format(sort_by_nom[i][9])
#             sort_by_nom[i][10] = "{:.2f}".format(sort_by_nom[i][10])
#             sort_by_nom[i][11] = "{:.2f}".format(sort_by_nom[i][11])
#             row.append(sort_by_nom[i])
#         row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10,
#                     u'-' * 10, u'-' * 10, u'-' * 10])
#
#         self.total_table['total'] = round(sums[11], 2)
#         self.total_table['bill'] = sums[8]
#         self.total_table['in'] = sums[9]
#         self.total_table['out'] = sums[10]
#
#         sums[8] = "{:.2f}".format(sums[8])
#         sums[9] = "{:.2f}".format(sums[9])
#         sums[10] = "{:.2f}".format(sums[10])
#         sums[11] = "{:.2f}".format(sums[11])
#
#         row.append(sums)
#         return row
#         # row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10,
#         # u'-' * 10, u'-' * 10, u'-' * 10])
#         # print self.m_checkBox6.GetValue()
#
#
#     def OnGo( self, event ):
#         self.get_date()
#         template = 'veri_big_table.html'
#         template_name = gui_lib.msg.mashin_report_H24['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
#         self.col = [u'-', u'-', u'-', u'-', u'-', u'-', u'-',u'-',u'-', u'-', u'-', u'-']
#         row = []
#
#             # row.append(
#             #     [u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10,
#             #      u'-' * 10, u'-' * 10, u'-' * 10])
#         if self.m_checkBox181.GetValue() is False:
#             if self.m_checkBox141.GetValue() is True:
#                 row = self.mashin_in_out(row)
#
#             if self.m_checkBox6.GetValue() is True:
#                 row = self.prihod_razhod(row)
#
#             if self.m_checkBox14.GetValue() is True:
#                 row = self.jp_server(row)
#
#             if self.m_checkBox17.GetValue() is True:
#                 row = self.cust_bonus(row)
#
#         elif self.m_checkBox181.GetValue() is True and self.m_checkBox141.GetValue() is True or self.m_checkBox6.GetValue() is True or self.m_checkBox14.GetValue() is True or self.m_checkBox17.GetValue() is True:
#             row = self.mashin_in_out(row)
#             row = self.prihod_razhod(row)
#             row = self.jp_server(row)
#             row = self.cust_bonus(row)
#             # row.append(
#             #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#             # row.append(
#             #     [u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u''])
#             row.append([gui_lib.msg.mashin_report_H24[34],
#                         gui_lib.msg.mashin_report_H24[35],
#                         gui_lib.msg.mashin_report_H24[33],
#                         gui_lib.msg.mashin_report_H24[1],
#                         gui_lib.msg.mashin_report_H24[2],
#                         gui_lib.msg.mashin_report_H24[36],
#                         gui_lib.msg.mashin_report_H24[37],
#                         gui_lib.msg.mashin_report_H24[21],
#                         gui_lib.msg.mashin_report_H24[10],
#                         gui_lib.msg.mashin_report_H24[39],
#                         gui_lib.msg.mashin_report_H24[40],
#                         gui_lib.msg.mashin_report_H24[41]])
#
#             row.append(["{:.2f}".format(self.total_table['in']),
#                         "{:.2f}".format(self.total_table['out']),
#                         "{:.2f}".format(self.total_table['total']),
#                         "{:.2f}".format(self.total_table['prihod']),
#                         "{:.2f}".format(self.total_table['razhod']),
#                         "{:.2f}".format(self.total_table['bill_get']),
#                         "{:.2f}".format(self.total_table['bill'] - self.total_table['bill_get']),
#                         "{:.2f}".format(self.total_table['lipsi']),
#                         "{:.2f}".format(self.total_table['jp']),
#                         "{:.2f}".format(self.total_table['bonus_cart'] + self.total_table['cust_bonus']),
#                         "{:.2f}".format(self.total_table['mony_back']),
#                         "{:.2f}".format(self.total_table['total'] + self.total_table['prihod'] - self.total_table['razhod'] -
#                                         self.total_table['bill'] + self.total_table['bill_get'] + self.total_table['bonus_hold'])
#                         ])
#
#         else:
#             template = 'report_big_table.html'
#
#             self.col = [gui_lib.msg.mashin_report_H24[2],
#                         gui_lib.msg.mashin_report_H24[6],
#                         gui_lib.msg.mashin_report_H24[1],
#                         gui_lib.msg.mashin_report_H24[6],
#                         gui_lib.msg.mashin_report_H24[21],
#                         gui_lib.msg.mashin_report_H24[6],
#                         gui_lib.msg.mashin_report_H24[39],
#                         gui_lib.msg.mashin_report_H24[6],
#                         gui_lib.msg.mashin_report_H24[10],
#                         gui_lib.msg.mashin_report_H24[6]]
#             self.mashin_in_out(row)
#             template_name = gui_lib.msg.mashin_report_H24[33] + u' %s:(%s/%s)' % (self.total_table['total'],self.start_date[:-3], self.end_date[:-3])
#             row = []
#
#             cust = libs.DB.get_all_where(libs.models.BonusPay,
#                                          pub_time__btw=(self.start_date, self.end_date),
#                                          order='id',
#                                          descs=False)
#
#             bill = libs.DB.get_all_where(libs.models.BillTake,
#                                          pub_time__btw=(self.start_date, self.end_date),
#                                          order='id',
#                                          descs=False)
#
#             prihod = libs.DB.get_all_where(libs.models.Prihod,
#                                            pub_time__btw=(self.start_date, self.end_date),
#                                            order='id',
#                                            descs=False)
#
#             razhod = libs.DB.get_all_where(libs.models.Razhod,
#                                            pub_time__btw=(self.start_date, self.end_date),
#                                            order='id',
#                                            descs=False)
#
#             mony_back = libs.DB.get_all_where(libs.models.MonuBackPay, pub_time__btw=(self.start_date, self.end_date),
#                                               order='id',
#                                               descs=False)
#             lipsi = libs.DB.get_all_where(libs.models.Lipsi, pub_time__btw=(self.start_date, self.end_date), order='id',
#                                           descs=False)
#
#
#
#         self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.mashin_report_H24['name'], row=row, col=self.col,
#                                                                       template_name=template_name, template=template)

class SMIBLog(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn9.Hide()
        self.m_radioBtn8.Hide()
        self.m_radioBtn41.Hide()
        self.m_radioBtn21.Hide()
        self.m_radioBtn28.Hide()
        self.m_radioBtn29.Hide()
        self.m_radioBtn17.Hide()

        self.m_radioBtn10.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn15.Hide()
        self.m_radioBtn42.Hide()
        self.m_radioBtn14.Hide()
        self.m_staticText7.SetLabel(gui_lib.msg.mashin_report_SMIBLog[12])
        self.add_choice()

    def add_choice(self):
        choise = [gui_lib.msg.mashin_report_SMIBLog[1], u'DEBUG', u'INFO', u'WARNING', u'ERROR', u'CRITICAL']
        self.m_choice3.SetItems(choise)
        self.m_choice3.SetSelection(0)

    def OnGo(self, event):
        self.db_row = []
        self.start_date = self.m_calendar1.GetDate()
        self.start_date = self.start_date.Format('%Y-%m-%d')

        self.end_date = self.m_calendar2.GetDate()
        self.end_date = self.end_date.Format('%Y-%m-%d')

        #         start_date = start_date + ' ' + str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
        start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
        self.start_date + ' 00:00:00', self.start_date + ' 23:59:59'))
        if start_times == None:
            start_times = ' 09:00:00'
        else:
            start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')
        self.start_date = self.start_date + ' ' + start_times
        #         self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
        #         self.start_date = libs.models.TZ.go_up_from_date(self.start_date, 1)
        #         self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
        # #
        #         end_date = end_date + ' ' + str(self.m_spinCtrl3.GetValue()) + ':' + str(self.m_spinCtrl4.GetValue())
        end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
                                          pub_time__btw=(self.end_date + ' 00:00:00', self.end_date + ' 23:59:59'))
        if end_times == None:
            end_times = libs.models.TZ.now()
            end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
        else:
            end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')
            #         end_date = end_date + ' ' + libs.models.TZ.date_to_str(end_times, '%H:%M')
        self.end_date = self.end_date + ' ' + end_times

        choiser = self.m_choice3.GetString(self.m_choice3.GetSelection())
        # raise KeyError, (self.start_date, self.end_date)
        if choiser == gui_lib.msg.mashin_report_SMIBLog[1]:
            self.db_row = libs.DB.get_all_where(libs.models.Log, pub_time__btw=(self.start_date, self.end_date),
                                                order='id')
        else:
            self.db_row = libs.DB.get_all_where(libs.models.Log, pub_time__btw=(self.start_date, self.end_date),
                                                order='id', level=choiser)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'veri_big_table.html'
        template_name = gui_lib.msg.mashin_report_SMIBLog['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        row = []
        col = [gui_lib.msg.mashin_report_SMIBLog[2],
               gui_lib.msg.mashin_report_SMIBLog[3],
               gui_lib.msg.mashin_report_SMIBLog[4],
               gui_lib.msg.mashin_report_SMIBLog[5],
               gui_lib.msg.mashin_report_SMIBLog[12],
               gui_lib.msg.mashin_report_SMIBLog[7],
               gui_lib.msg.mashin_report_SMIBLog[8],
               gui_lib.msg.mashin_report_SMIBLog[9],
               gui_lib.msg.mashin_report_SMIBLog[10],
               gui_lib.msg.mashin_report_SMIBLog[11]]
        for i in self.db_row:
            var = []
            var.append(str(i.id))
            var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
            var.append(str(i.device.nom_in_l))
            var.append(str(i.msg_text))
            var.append(str(i.level))
            var.append(str(i.name))
            var.append(str(i.proces_name))
            var.append(str(i.func_name))
            var.append(str(i.lineno))
            var.append(str(i.text))

            row.append(var)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.mashin_report_SMIBLog['name'], row=row,
                                                                      col=col,
                                                                      template_name=template_name, template=template)

class FixLog(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn9.Hide()
        self.m_radioBtn8.Hide()
        self.m_radioBtn41.Hide()
        self.m_radioBtn21.Hide()
        self.m_radioBtn28.Hide()
        self.m_radioBtn29.Hide()
        self.m_radioBtn17.Hide()

        self.m_radioBtn10.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn15.Hide()
        self.m_radioBtn42.Hide()
        self.m_radioBtn14.Hide()
        self.m_staticText7.Hide()
        self.m_choice3.Hide()
        # self.add_choice()

    def OnGo(self, event):
        self.db_row = []
        self.start_date = self.m_calendar1.GetDate()
        self.start_date = self.start_date.Format('%Y-%m-%d')

        self.end_date = self.m_calendar2.GetDate()
        self.end_date = self.end_date.Format('%Y-%m-%d')

        #         start_date = start_date + ' ' + str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
        start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
        self.start_date + ' 00:00:00', self.start_date + ' 23:59:59'))
        if start_times == None:
            start_times = ' 09:00:00'
        else:
            start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')
        self.start_date = self.start_date + ' ' + start_times
        #         self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
        #         self.start_date = libs.models.TZ.go_up_from_date(self.start_date, 1)
        #         self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
        # #
        #         end_date = end_date + ' ' + str(self.m_spinCtrl3.GetValue()) + ':' + str(self.m_spinCtrl4.GetValue())
        end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
                                          pub_time__btw=(self.end_date + ' 00:00:00', self.end_date + ' 23:59:59'))
        if end_times == None:
            end_times = libs.models.TZ.now()
            end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
        else:
            end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')
            #         end_date = end_date + ' ' + libs.models.TZ.date_to_str(end_times, '%H:%M')
        self.end_date = self.end_date + ' ' + end_times

        # maker = self.m_choice3.GetString(self.m_choice3.GetSelection())
        # if maker == gui_lib.msg.report_mashin_FixLog[2]:
        self.db_row = libs.DB.get_all_where(libs.models.EMGService, is_fix=True, pub_time__btw=(self.start_date, self.end_date),
                                                order='id')
        # else:
            # maker = libs.DB.get_one_where(libs.models.Maker, name=maker)
            # self.db_row = libs.DB.get_all_where(libs.models.Log, asctime__btw=(self.start_date, self.end_date),
            #                                     order='id', level=maker)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report_big_table.html'
        template_name = gui_lib.msg.report_mashin_FixLog['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        row = []
        col = [gui_lib.msg.report_mashin_FixLog[3],
               gui_lib.msg.report_mashin_FixLog[4],
               gui_lib.msg.report_mashin_FixLog[5],
               gui_lib.msg.report_mashin_FixLog[6],
               gui_lib.msg.report_mashin_FixLog[7],
               gui_lib.msg.report_mashin_FixLog[8],
               gui_lib.msg.report_mashin_FixLog[9],
               gui_lib.msg.report_mashin_FixLog[10],
               gui_lib.msg.report_mashin_FixLog[11],
               gui_lib.msg.report_mashin_FixLog[12],
               gui_lib.msg.report_mashin_FixLog[13],
               ]
        total_sum = 0
        for i in self.db_row:
            tmp = []
            tmp.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
            tmp.append(str(i.user.name))
            tmp.append(str(i.info))
            if i.mashin_id != None:
                tmp.append(str(i.mashin.nom_in_l))
                tmp.append(str(i.mashin.model.name))
                tmp.append(str(i.mashin.serial))
            else:
                tmp.append(u'')
                tmp.append(u'')
                tmp.append(u'')
            tmp.append(libs.models.TZ.date_to_str(i.fix_time, '%d.%m.%Y %H:%M:%S'))
            tmp.append(str(i.fix_info))
            if i.is_ram_clear is True:
                tmp.append(gui_lib.msg.report_mashin_FixLog[15])
            else:
                tmp.append(u'')
            tmp.append(str(i.user_fix.name))
            total_sum += i.part_mony
            tmp.append("{:.2f}".format(i.part_mony))
            row.append(tmp)
        row.append([u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5,u'-'*5])
        row.append([u'',u'',u'',u'',u'',u'',u'',u'',u'', gui_lib.msg.report_mashin_FixLog[14] ,"{:.2f}".format(total_sum)])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.report_mashin_FixLog['name'],
                                                                      row=row,
                                                                      col=col,
                                                                      template_name=template_name, template=template)


class NullDevice(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn9.Hide()
        self.m_radioBtn8.Hide()
        self.m_radioBtn41.Hide()
        self.m_radioBtn21.Hide()
        self.m_radioBtn28.Hide()
        self.m_radioBtn29.Hide()
        self.m_radioBtn17.Hide()

        self.m_radioBtn10.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn15.Hide()
        self.m_radioBtn42.Hide()
        self.m_radioBtn14.Hide()
        self.m_staticText7.Hide()
        self.m_choice3.Hide()
        # self.add_choice()

    def OnGo(self, event):
        self.db_row = []
        self.start_date = self.m_calendar1.GetDate()
        self.start_date = self.start_date.Format('%Y-%m-%d')

        self.end_date = self.m_calendar2.GetDate()
        self.end_date = self.end_date.Format('%Y-%m-%d')

        #         start_date = start_date + ' ' + str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
        start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
            self.start_date + ' 00:00:00', self.start_date + ' 23:59:59'))
        if start_times == None:
            start_times = ' 09:00:00'
        else:
            start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')
        self.start_date = self.start_date + ' ' + start_times
        #         self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
        #         self.start_date = libs.models.TZ.go_up_from_date(self.start_date, 1)
        #         self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
        # #
        #         end_date = end_date + ' ' + str(self.m_spinCtrl3.GetValue()) + ':' + str(self.m_spinCtrl4.GetValue())
        end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
                                          pub_time__btw=(self.end_date + ' 00:00:00', self.end_date + ' 23:59:59'))
        if end_times == None:
            end_times = libs.models.TZ.now()
            end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
        else:
            end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')
            #         end_date = end_date + ' ' + libs.models.TZ.date_to_str(end_times, '%H:%M')
        self.end_date = self.end_date + ' ' + end_times

        # maker = self.m_choice3.GetString(self.m_choice3.GetSelection())
        # if maker == gui_lib.msg.report_mashin_FixLog[2]:
        self.db_row = libs.DB.get_all_where(libs.models.RamClear, pub_time__btw=(self.start_date, self.end_date),
                                            order='id')
        # else:
        # maker = libs.DB.get_one_where(libs.models.Maker, name=maker)
        # self.db_row = libs.DB.get_all_where(libs.models.Log, asctime__btw=(self.start_date, self.end_date),
        #                                     order='id', level=maker)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report_big_table.html'
        template_name = gui_lib.msg.report_mashin_NullDevice['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        row = []
        col = [gui_lib.msg.report_mashin_NullDevice[3],
               gui_lib.msg.report_mashin_NullDevice[4],
               gui_lib.msg.report_mashin_NullDevice[5],
               gui_lib.msg.report_mashin_NullDevice[6],
               gui_lib.msg.report_mashin_NullDevice[7],
               gui_lib.msg.report_mashin_NullDevice[8],
               gui_lib.msg.report_mashin_NullDevice[9],
               gui_lib.msg.report_mashin_NullDevice[10],
               gui_lib.msg.report_mashin_NullDevice[11],
               gui_lib.msg.report_mashin_NullDevice[12],
               ]
        for i in self.db_row:
            tmp = []
            tmp.append(str(i.mashin.nom_in_l))
            tmp.append(str(i.mashin.model.name))
            tmp.append(str(i.mashin.serial))
            tmp.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
            tmp.append(str(i.el_in))
            tmp.append(str(i.el_out))
            tmp.append(str(i.mex_in))
            tmp.append(str(i.mex_out))
            tmp.append(str(i.bill))
            row.append(tmp)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                          gui_lib.msg.report_mashin_NullDevice['name'],
                                                                          row=row,
                                                                          col=col,
                                                                          template_name=template_name,
                                                                          template=template)

class InOutInDevice(Report):

    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn42.Hide()
        self.m_radioBtn15.Hide()
        self.m_radioBtn17.Hide()
        self.m_radioBtn41.Hide()
        self.m_radioBtn28.Hide()
        self.m_radioBtn29.Hide()
        self.m_radioBtn9.Hide()
        self.m_radioBtn8.Hide()
        self.m_radioBtn21.SetValue(True)
        self.m_radioBtn10.SetValue(True)
        self.add_choice()
        self.m_radioBtn10.SetLabel(gui_lib.msg.report_InOut_text['m_radioBtn10'])
        self.m_radioBtn7.SetLabel(gui_lib.msg.report_InOut_text['m_radioBtn14'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.report_InOut_text['m_radioBtn15'])
        self.parent = parent

    def get_date(self):
        self.start_date = self.m_calendar1.GetDate()
        self.start_date = self.start_date.Format('%Y-%m-%d')

        self.end_date = self.m_calendar2.GetDate()
        self.end_date = self.end_date.Format('%Y-%m-%d')

        #         start_date = start_date + ' ' + str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
        start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
            self.start_date + ' 00:00:00', self.start_date + ' 23:59:59'))
        if start_times == None:
            start_times = ' 09:00:00'
        else:
            start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')
        self.start_date = self.start_date + ' ' + start_times
        #         self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
        #         self.start_date = libs.models.TZ.go_up_from_date(self.start_date, 1)
        #         self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
        # #
        #         end_date = end_date + ' ' + str(self.m_spinCtrl3.GetValue()) + ':' + str(self.m_spinCtrl4.GetValue())
        end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
                                          pub_time__btw=(self.end_date + ' 00:00:00', self.end_date + ' 23:59:59'))
        if end_times == None:
            end_times = libs.models.TZ.now()
            end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
        else:
            end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')
        # end_date = end_date + ' ' + libs.models.TZ.date_to_str(end_times, '%H:%M')
        self.end_date = self.end_date + ' ' + end_times

    def OnGo(self, event):
        self.row = []
        self.get_date()
        choiser = self.m_choice3.GetString(self.m_choice3.GetSelection())
        if choiser == gui_lib.msg.mashin_report_Report[1]:
            if self.m_radioBtn10.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.InOut, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True)
            elif self.m_radioBtn7.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.InOut, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True, out=False)
            elif self.m_radioBtn14.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.InOut, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True, out=True)
        else:
            data = libs.DB.get_one_where(libs.models.User, name=choiser)
            if self.m_radioBtn10.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.InOut, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True, user_id=data.id)
            elif self.m_radioBtn7.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.InOut, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True, out=False, user_id=data.id)
            elif self.m_radioBtn14.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.InOut, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True, out=True, user_id=data.id)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report_big_table.html'
        template_name = gui_lib.msg.report_InOut_text['table_name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        row = []
        sums = [u'', u'', u'', u'', u'', u'', gui_lib.msg.report_InOut_text[15], 0, 0, 0, 0]
        col = [gui_lib.msg.report_InOut_text[1],
               gui_lib.msg.report_InOut_text[2],
               gui_lib.msg.report_InOut_text[3],
               gui_lib.msg.report_InOut_text[9],
               gui_lib.msg.report_InOut_text[10],
               gui_lib.msg.report_InOut_text[13],
               gui_lib.msg.report_InOut_text[8],
               gui_lib.msg.report_InOut_text[6],
               gui_lib.msg.report_InOut_text[4],
               gui_lib.msg.report_InOut_text[5],
               gui_lib.msg.report_InOut_text[11],
               ]
        for i in self.row:
            var = []
            var.append(str(i.id))
            var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
            var.append(str(i.device.nom_in_l))
            var.append(str(i.device.flor.name))
            var.append(str(i.device.model.name))
            if i.user_id != None:
                var.append(i.user.name)
            else:
                var.append('')
            if i.player_id:
                var.append(i.player.name)
            else:
                var.append('')
            if i.out is False:
                if i.bill is True:
                    var.append(gui_lib.msg.report_InOut_text[12])
                    sums[7] += i.mony
                else:
                    var.append(gui_lib.msg.report_InOut_text[7])
            else:
                var.append('')
            if i.out is False:
                var.append("{:.2f}".format(i.mony))
                var.append('')
                var.append('0.00')
                sums[8] += i.mony
            else:
                var.append('')
                var.append("{:.2f}".format(i.mony))
                var.append("{:.2f}".format(i.mony - int(i.mony)))
                sums[9] += i.mony
                sums[10] += round(i.mony - int(i.mony), 2)
            row.append(var)
        row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, ])
        sums[7] = "{:.2f}".format(sums[7])
        sums[8] = "{:.2f}".format(sums[8])
        sums[9] = "{:.2f}".format(sums[9])
        sums[10] = "{:.2f}".format(sums[10])
        row.append(sums)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.report_InOut_text['table_name'],
                                                                      row=row,
                                                                      col=col,
                                                                      template_name=template_name, template=template)


if __name__ == '__main__':
    pass
