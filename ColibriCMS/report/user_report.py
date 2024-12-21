#-*- coding:utf-8 -*-
'''
Created on 28.10.2017 г.

@author: dedal
'''
from . import gui
import libs  # @UnresolvedImport
import gui_lib  # @UnresolvedImport
import wx
import datetime
import json

class Report(gui.UserReport):
    def __init__(self, parent):
        gui.UserReport.__init__(self, parent)
        self.parent = parent
#         self.parent = parent
#         self.parent.GetParent().GetParent().GetParent().GetParent().SetTitle(u'Справки/Потребители')
        self.m_radioBtn9.SetLabel(gui_lib.msg.user_report_Report_button['m_radioBtn9'])
        self.m_radioBtn8.SetLabel(gui_lib.msg.user_report_Report_button['m_radioBtn8'])
        self.m_radioBtn10.SetLabel(gui_lib.msg.user_report_Report_button['m_radioBtn10'])
        self.m_radioBtn7.SetLabel(gui_lib.msg.user_report_Report_button['m_radioBtn7'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.user_report_Report_button['m_radioBtn14'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.user_report_Report_button['m_radioBtn15'])
        self.m_checkBox6.SetLabel(gui_lib.msg.user_report_Report_button['m_checkBox6'])
        self.m_radioBtn16.SetLabel(gui_lib.msg.user_report_Report_button['m_radioBtn16'])
        self.m_radioBtn17.SetLabel(gui_lib.msg.user_report_Report_button['m_radioBtn17'])
        self.m_button6.SetLabel(gui_lib.msg.user_report_Report_button['m_button6'])
        self.m_calendar1.SetToolTip(gui_lib.msg.user_report_Report_tooltip['m_calendar1'])
        self.m_calendar2.SetToolTip(gui_lib.msg.user_report_Report_tooltip['m_calendar2'])
        self.m_staticText7.SetLabel(gui_lib.msg.user_report_Report_text['m_staticText7'])
        self.add_user_choice()
        self.width, self.height = self.parent.GetSize()
        self.Bind( wx.EVT_SIZE, self.on_resize )
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.on_resize(None)

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
                        data[int(row_dict[i][0])] += 0.1
                    else:
                        data[int(row_dict[i][0])] = 0.1
                    sort_by_nom[int(row_dict[i][0]) + data[int(row_dict[i][0])]] = row_dict[i]
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
            
    def add_user_choice(self):
        userchoise = [gui_lib.msg.user_report_Report_text[1]]
        user = libs.DB.get_all_where(libs.models.User, enable = self.m_radioBtn9.GetValue())
        for i in user:
            userchoise.append(i.name)
        self.m_choice3.SetItems(userchoise)
        self.m_choice3.SetSelection(0)
        
    def OnRadioButtonUser(self, event):
        self.add_user_choice()
    
    def OnTableMaket(self, event):
        if self.m_radioBtn17.GetValue() is True:
            self.m_choice3.Disable()
#             self.m_choice4.Disable()
            self.m_checkBox6.Disable()
        else:
            self.m_choice3.Enable()
#             self.m_choice4.Enable()
            self.m_checkBox6.Enable()
    
    def get_conf_selection(self):
        start_date = self.m_calendar1.GetDate()
        start_date = start_date.Format('%Y-%m-%d')
        end_date = self.m_calendar2.GetDate()
        end_date = end_date.Format('%Y-%m-%d')
        
        start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(start_date + ' 00:00:00', start_date + ' 23:59:59'))
        if start_times == None:
            start_times = ' 09:00:00'
        else:
            start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')
        self.start_date = start_date + ' ' + start_times
        
        
#         last_order = libs.DB.get_one_where(libs.models.BosGetMony, pub_time__lte=self.start_date)
#         if last_order == None:
#             start_times = datetime.datetime.now()
#             start_times = libs.models.TZ.date_to_str(start_times, '%H:%M:%S')
#         else:
#             start_times = libs.models.TZ.date_to_str(last_order.pub_time, '%H:%M:%S')
#         self.start_date = start_date + ' ' + start_times
        
        end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(end_date + ' 00:00:00', end_date + ' 23:59:59'))
        if end_times == None:
            end_times = libs.models.TZ.now()
            end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
        else:
            end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')
        self.end_date = end_date + ' ' + end_times
        
#         last_order = libs.DB.get_one_where(libs.models.BosGetMony, pub_time__lte=self.end_date)
#         if last_order == None:
#             end_times = datetime.datetime.now()
#             end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
#         else:
#             end_times = libs.models.TZ.date_to_str(last_order.pub_time, '%H:%M:%S')
#         self.end_date = end_date + ' ' + end_times
        
#         print self.start_date
#         print self.end_date
        self.user_name =  self.m_choice3.GetString(self.m_choice3.GetSelection())
        self.desk = self.m_checkBox6.GetValue()
            
class BonusCart(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.parent = parent
        self.m_checkBox6.SetLabel(gui_lib.msg.user_report_BonusCart_text[6])
        self.m_radioBtn17.Hide()
            
    def table_report(self):
        template = 'report_big_table.html'
#         template_name = u'Бонус Карти: Потребители' 
        template_name = gui_lib.msg.user_report_BonusCart_text['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.user_report_BonusCart_text[1],
                   gui_lib.msg.user_report_BonusCart_text[2],
                   gui_lib.msg.user_report_BonusCart_text[3],
                   gui_lib.msg.user_report_BonusCart_text[13],
                   gui_lib.msg.user_report_BonusCart_text[4],
                   gui_lib.msg.user_report_BonusCart_text[5],
                   gui_lib.msg.user_report_BonusCart_text[6],
                   gui_lib.msg.user_report_BonusCart_text[7],
                   gui_lib.msg.user_report_BonusCart_text[8],
                   gui_lib.msg.user_report_BonusCart_text[9]]
            sums = [u'',u'',u'', u'', u'', u'', gui_lib.msg.user_report_BonusCart_text[10], 0, 0, 0]
            row = []
            for i in self.db_row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(i.cart.name)
                # if i.user_id == None:
                #     var.append('')
                # else:
                var.append(i.user.name)
                try:
                    # if i.cust_id == None:
                    #     var.append('')
                    # else:
                    var.append(str(i.cust.name))
                except AttributeError:
                    try:
                        var.append(str(i.cart.name))
                    except AttributeError:
                        var.append('')
                # var.append(i.user.name)
                var.append(str(i.mashin.nom_in_l))
                var.append(i.mashin.model.name)
                if i.bonus_hold is True:
                    var.append(gui_lib.msg.user_report_BonusCart_text[6])
                else:
                    var.append('')
                var.append("{:.2f}".format(i.bonus))
                var.append("{:.2f}".format(i.mony))
                if i.bonus_hold is True:
                    var.append("{:.2f}".format(i.credit))
                else:
                    var.append('')
#                 print var
                sums[8] = sums[8] + i.mony
                sums[7] = sums[7] + i.bonus
                if i.credit != None:
                    sums[9] = sums[9] + i.credit
                else:
                    sums[9] += 0
                row.append(var)
            row.append([u'-'*20, u'-'*20, u'-'*20, u'-'*20, u'-'*20, u'-'*20, u'-'*20, u'-'*20, u'-'*20, u'-'*20])
            sums[8] = "{:.2f}".format(sums[8])
            sums[7] = "{:.2f}".format(sums[7])
            sums[9] = "{:.2f}".format(sums[9])
            row.append(sums)
        elif self.m_radioBtn15.GetValue() is True:
            col = [ gui_lib.msg.user_report_BonusCart_text[4],
                    gui_lib.msg.user_report_BonusCart_text[5],
                    gui_lib.msg.user_report_BonusCart_text[11],
                    gui_lib.msg.user_report_BonusCart_text[8]]
            sums = [u'',gui_lib.msg.user_report_BonusCart_text[10], 0, 0]
            row = []
            row_dict = {}
            for i in self.db_row:
                if i.mashin_id not in row_dict:
                    row_dict[i.mashin_id] = [str(i.mashin.nom_in_l), str(i.mashin.model.name), i.bonus, i.mony, i.mashin_id]
                    sums[3] = sums[3] + i.mony
                    sums[2] = sums[2] + i.bonus
                else:
                    row_dict[i.mashin_id][3] = row_dict[i.mashin_id][3] + i.mony
                    sums[3] = sums[3] + i.mony
                    row_dict[i.mashin_id][2] = row_dict[i.mashin_id][2] + i.bonus
                    sums[2] = sums[2] + i.bonus
            row_dict = self.sort_by_nom_in_l(row_dict)
            for i in sorted(list(row_dict.keys())):
                var = []
                var.append(row_dict[i][0])
                var.append(row_dict[i][1])
                var.append("{:.2f}".format(row_dict[i][2]))
                var.append("{:.2f}".format(row_dict[i][3]))
                row.append(var)
            row.append([u'-'*20, u'-'*20, u'-'*20, u'-'*20])
            sums[2] = "{:.2f}".format(sums[2])
            sums[3] = "{:.2f}".format(sums[3])
            row.append(sums)
        elif self.m_radioBtn14.GetValue() is True:
            col = [gui_lib.msg.user_report_BonusCart_text[3],
                   gui_lib.msg.user_report_BonusCart_text[11],
                   gui_lib.msg.user_report_BonusCart_text[8]]
            row = []
            sums = [gui_lib.msg.user_report_BonusCart_text[10], 0, 0]
            row_dict = {}
            for i in self.db_row:
                if i.user.name not in row_dict:
                    row_dict[i.user.name] = [i.user.name, i.bonus, i.mony]
                    sums[1] = sums[1] + i.mony
                    sums[2] = sums[2] + i.mony
                else:
                    row_dict[i.user.name][2] = row_dict[i.user.name][2] + i.mony
                    sums[2] = sums[2] + i.mony
                    row_dict[i.user.name][1] = row_dict[i.user.name][1] + i.bonus
                    sums[1] = sums[1] + i.bonus
            for i in sorted(list(row_dict.keys())):
                var = []
                var.append(row_dict[i][0])
                var.append("{:.2f}".format(row_dict[i][1]))
                var.append("{:.2f}".format(row_dict[i][2]))
                row.append(var)
            row.append([u'-'*20, u'-'*20, u'-'*20])
            sums[1] = "{:.2f}".format(sums[1])
            sums[2] = "{:.2f}".format(sums[2])
            row.append(sums)
                
        elif self.m_radioBtn7.GetValue() is True:
            col = [gui_lib.msg.user_report_BonusCart_text[1],
                   gui_lib.msg.user_report_BonusCart_text[11],
                   gui_lib.msg.user_report_BonusCart_text[8]]
            row = []
            sums = [gui_lib.msg.user_report_BonusCart_text[10], 0, 0]
            row_dict = {}
            for i in self.db_row:
                if libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y') not in row_dict:
                    row_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')] = [i.mony, i.bonus]
                    sums[2] = sums[2] + i.mony
                    sums[1] = sums[1] + i.bonus
                else:
                    row_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][0] = row_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][0] + i.bonus
                    row_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][1] = row_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][1] + i.mony
                    
                    sums[1] = sums[1] + i.bonus
                    sums[2] = sums[2] + i.mony
            for i in sorted(list(row_dict.keys())):
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i][0]))
                var.append("{:.2f}".format(row_dict[i][1]))
                row.append(var)
            row.append([u'-'*20, u'-'*20, u'-'*20])
            sums[1] = "{:.2f}".format(sums[1])
            sums[2] = "{:.2f}".format(sums[2])
            row.append(sums)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.user_report_BonusCart_text['name'], row=row, col=col, template_name=template_name, template=template)
    
    def pic_report(self):
        row = {}
        template_name = gui_lib.msg.user_report_BonusCart_text['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        y_label = 'TOTAL'
        x_label = 'Date'
        X = []
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)

    
    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        if self.user_name == gui_lib.msg.user_report_BonusCart_text[12]:
            self.db_row = libs.DB.get_all_where(libs.models.BonusCartLog, 
                                                       pub_time__btw=(self.start_date, self.end_date), 
                                                       user_id__gte=0,
                                                       bonus_hold=self.m_checkBox6.GetValue(),
                                                       )
            db_row = libs.DB.get_all_where(libs.models.ClienBonusHold,
                                           pub_time__btw=(self.start_date, self.end_date),
                                           user_id__gte=0,
                                           bonus_hold=self.m_checkBox6.GetValue(),
                                           )
            for i in db_row:
                self.db_row.append(i)
        else:
            user = libs.DB.get_one_where(libs.models.User, name=self.user_name)
            self.db_row = libs.DB.get_all_where(libs.models.BonusCartLog, 
                                                       pub_time__btw=(self.start_date, self.end_date),
                                                       user_id=user.id,
                                                       bonus_hold=self.m_checkBox6.GetValue(),
                                                       )
            db_row = libs.DB.get_all_where(libs.models.ClienBonusHold,
                                           pub_time__btw=(self.start_date, self.end_date),
                                           user_id=user.id,
                                           bonus_hold=self.m_checkBox6.GetValue(),
                                           )
            for i in db_row:
                self.db_row.append(i)

        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()
        
    
class BillReport(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn17.Hide()

            
    def table_report(self):
        template = 'report.html'
#         template_name = u'Изваден бил: Потребители' 
        template_name = gui_lib.msg.user_report_BillReport_text['name'] + ':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
#         order_by = self.order_by[self.m_choice4.GetString(self.m_choice4.GetSelection())]
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.user_report_BillReport_text[1],
                   gui_lib.msg.user_report_BillReport_text[2],
                   gui_lib.msg.user_report_BillReport_text[3],
                   gui_lib.msg.user_report_BillReport_text[4],
                   gui_lib.msg.user_report_BillReport_text[5]]
            sums = [u'',u'',u'', gui_lib.msg.user_report_BillReport_text[6], 0]
            row = []
            for i in self.db_row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(i.user.name)
                var.append(str(i.mashin.nom_in_l))
                var.append(i.mashin.model.name)
                var.append("{:.2f}".format(i.mony))
                sums[4] = sums[4] + i.mony
                row.append(var)
            row.append([u'-'*20, u'-'*20, u'-'*20, u'-'*20, u'-'*20])
            sums[4] = "{:.2f}".format(sums[4])
            row.append(sums)
        elif self.m_radioBtn15.GetValue() is True:
            col = [ gui_lib.msg.user_report_BillReport_text[3],
                    gui_lib.msg.user_report_BillReport_text[4],
                    gui_lib.msg.user_report_BillReport_text[5]]
            sums = [u'', gui_lib.msg.user_report_BillReport_text[6], 0]
            row = []
            row_dict = {}
            for i in self.db_row:
                if i.mashin_id not in row_dict:
                    row_dict[i.mashin_id] = [str(i.mashin.nom_in_l), i.mashin.model.name, i.mony, i.mashin_id]
                    sums[2] = sums[2] + i.mony
                else:
                    row_dict[i.mashin_id][2] = row_dict[i.mashin_id][2] + i.mony
                    sums[2] = sums[2] + i.mony
            row_dict = self.sort_by_nom_in_l(row_dict)
            for i in sorted(list(row_dict.keys())):
                var = []
                var.append(row_dict[i][0])
                var.append(row_dict[i][1])
                var.append("{:.2f}".format(row_dict[i][2]))
                row.append(var)
            row.append([u'-'*20, u'-'*20, u'-'*20])
            sums[2] = "{:.2f}".format(sums[2])
            row.append(sums)
        elif self.m_radioBtn14.GetValue() is True:
            col = [gui_lib.msg.user_report_BillReport_text[2],
                   gui_lib.msg.user_report_BillReport_text[5]]
            row = []
            sums = [gui_lib.msg.user_report_BillReport_text[6], 0]
            row_dict = {}
            for i in self.db_row:
                if i.user.name not in row_dict:
                    row_dict[i.user.name] = [i.user.name, i.mony]
                    sums[1] = sums[1] + i.mony
                else:
                    row_dict[i.user.name][1] = row_dict[i.user.name][1] + i.mony
                    sums[1] = sums[1] + i.mony
            for i in sorted(list(row_dict.keys())):
                var = []
                var.append(row_dict[i][0])
                var.append("{:.2f}".format(row_dict[i][1]))
                row.append(var)
            row.append([u'-'*20, u'-'*20])
            sums[1] = "{:.2f}".format(sums[1])
            row.append(sums)
                
        elif self.m_radioBtn7.GetValue() is True:
            col = [gui_lib.msg.user_report_BillReport_text[1],
                   gui_lib.msg.user_report_BillReport_text[5]]
            row = []
            sums = [gui_lib.msg.user_report_BillReport_text[6], 0]
            row_dict = {}
            for i in self.db_row:
                if libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y') not in row_dict:
                    row_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')] = [i.mony]
                    sums[1] = sums[1] + i.mony
                else:
                    row_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][0] = row_dict[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')][0] + i.mony
                    sums[1] = sums[1] + i.mony
            for i in sorted(list(row_dict.keys())):
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i][0]))
                row.append(var)
            row.append([u'-'*20, u'-'*20])
            sums[1] = "{:.2f}".format(sums[1])
            row.append(sums)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.user_report_BillReport_text['name'], row=row, col=col, template_name=template_name, template=template)

    def pic_report(self):
        row = {}
        template_name = gui_lib.msg.user_report_BillReport_text['name'] + ':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)
    
    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        if self.user_name == gui_lib.msg.user_report_BillReport_text[7]:
            self.db_row = libs.DB.get_all_where(libs.models.BillTake, 
                                                       pub_time__btw=(self.start_date, self.end_date), 
#                                                        order=self.order_by[order_by],
                                                        descs=self.desk
                                                       )
        else:
            user = libs.DB.get_one_where(libs.models.User, name=self.user_name)
            self.db_row = libs.DB.get_all_where(libs.models.BillTake, 
                                                       pub_time__btw=(self.start_date, self.end_date),
                                                       user_id=user.id, 
#                                                        order=self.order_by[order_by],
                                                        descs=self.desk
                                                       )
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()
    
    
class Lipsi(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn17.Hide()
        
#         self.m_choice4.SetMinSize((self.width*0.6, -1))
#         self.m_staticText9.Hide()
#         self.m_choice4.Hide()
        self.m_radioBtn14.SetValue(True)
        self.m_radioBtn15.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.user_report_Lipsi_text['m_radioBtn10'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.user_report_Lipsi_text['m_radioBtn14'])

    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        if self.user_name == gui_lib.msg.user_report_Lipsi_text[1]:
            self.db_row = libs.DB.get_all_where(libs.models.Lipsi, 
                                                       pub_time__btw=(self.start_date, self.end_date), 
                                                       order='id',
                                                       descs=self.desk)
        else:
            user = libs.DB.get_one_where(libs.models.User, name=self.user_name)
            self.db_row = libs.DB.get_all_where(libs.models.Lipsi, 
                                                       pub_time__btw=(self.start_date, self.end_date),
                                                       user_id=user.id, 
                                                       order='id',
                                                       descs=self.desk)
             
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        row = {}
        template_name =   gui_lib.msg.user_report_Lipsi_text['name']+ u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)
    
    def table_report(self):
        template = 'report.html'
#         template_name = u'Справка Липси' 
        template_name =   gui_lib.msg.user_report_Lipsi_text['name']+ u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.user_report_Lipsi_text[2],
                   gui_lib.msg.user_report_Lipsi_text[3],
                   gui_lib.msg.user_report_Lipsi_text[4],
                   gui_lib.msg.user_report_Lipsi_text[5]]
            row = []
            for i in self.db_row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(i.user.name)
                var.append("{:.2f}".format(i.mony))
                if i.if_lipsa is True:
                    var.append(gui_lib.msg.user_report_Lipsi_text[6])
                else:
                    var.append(gui_lib.msg.user_report_Lipsi_text[7])
                row.append(var)
        elif self.m_radioBtn14.GetValue() is True:
            col = [ gui_lib.msg.user_report_Lipsi_text[3],
                    gui_lib.msg.user_report_Lipsi_text[4]]
            row = []
            row_dict = {}
            for i in self.db_row:
                # print i.if_lipsa, i.user.name, i.mony
                if i.user.name not in row_dict:

                    if i.if_lipsa is True:
                        row_dict[i.user.name] = i.mony
                    else:
                        row_dict[i.user.name] = i.mony*-1
                else:
                    if i.if_lipsa is True:
                        row_dict[i.user.name] = row_dict[i.user.name] + i.mony
                    else:
                        row_dict[i.user.name] = row_dict[i.user.name] - i.mony
                # print row_dict[i.user.name]

            for i in sorted(list(row_dict.keys()), reverse=self.m_checkBox6.GetValue()):
                # if row_dict[i] < 0:
                #     row_dict[i] = 0
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i]))
                row.append(var)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.user_report_Lipsi_text['name'], row=row, col=col, template_name=template_name, template=template)


class BosGetMony(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn17.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.user_report_BosGetMony_text['m_radioBtn10'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.user_report_BosGetMony_text['m_radioBtn15'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.user_report_BosGetMony_text['m_radioBtn14'])

    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        if self.user_name == gui_lib.msg.user_report_BosGetMony_text[1]:
            self.db_row = libs.DB.get_all_where(libs.models.BosGetMony, 
                                                       pub_time__btw=(self.start_date, self.end_date), 
                                                       order='id',
                                                       descs=self.desk)
        else:
            user = libs.DB.get_one_where(libs.models.User, name=self.user_name)
            self.db_row = libs.DB.get_all_where(libs.models.BosGetMony, 
                                                       pub_time__btw=(self.start_date, self.end_date),
                                                       user_id=user.id, 
                                                       order='id',
                                                       descs=self.desk)
             
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        row = {}
        template_name = gui_lib.msg.user_report_BosGetMony_text['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)
    
    def table_report(self):
        template = 'report.html'
#         template_name = u'Отчетени пари' 
        template_name = gui_lib.msg.user_report_BosGetMony_text['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.user_report_BosGetMony_text[2],
                   gui_lib.msg.user_report_BosGetMony_text[3],
                   gui_lib.msg.user_report_BosGetMony_text[4],
                   gui_lib.msg.user_report_BosGetMony_text[5]]
            row = []
            sum_mony = 0
            for i in self.db_row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(i.user.name)
                if i.flor_id == None:
                    var.append(gui_lib.msg.user_report_BosGetMony_text[1])
                else:
                    flor = libs.DB.get_one_where(libs.models.Flor, id=i.flor_id)
                    var.append(flor.name)
                sum_mony += i.mony
                var.append("{:.2f}".format(i.mony))
                row.append(var)
            row.append([u'-' * 20, u'-' * 20, u'-' * 20, u'-' * 20])
            row.append([u'', u'', gui_lib.msg.user_report_BosGetMony_text['total'], "{:.2f}".format(sum_mony)])
        elif self.m_radioBtn15.GetValue() is True:
            col = [ gui_lib.msg.user_report_BosGetMony_text[3],
                    gui_lib.msg.user_report_BosGetMony_text[5]]
            sum_mony = 0
            row = []
            row_dict = {}
            for i in self.db_row:
                if i.user.name not in row_dict:
                    row_dict[i.user.name] = i.mony
                    sum_mony += i.mony
                else:
                    row_dict[i.user.name] = row_dict[i.user.name] + i.mony
                    sum_mony += i.mony
            for i in sorted(list(row_dict.keys()), reverse=self.m_checkBox6.GetValue()):
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i]))
                row.append(var)
            row.append([u'-' * 20, u'-' * 20])
            row.append([gui_lib.msg.user_report_BosGetMony_text['total'], "{:.2f}".format(sum_mony)])

                
        elif self.m_radioBtn14.GetValue() is True:
            col = [ gui_lib.msg.user_report_BosGetMony_text[4],
                    gui_lib.msg.user_report_BosGetMony_text[5]]
            row = []
            sum_mony = 0
            row_dict = {}
            for i in self.db_row:
                if i.flor_id == None:
                    flor =gui_lib.msg.user_report_BosGetMony_text[1]
                    if flor not in row_dict:
                        row_dict[flor] = i.mony
                        sum_mony += i.mony
                    else:
                        row_dict[flor] = row_dict[flor] + i.mony
                        sum_mony += i.mony
                else:
                    flor = libs.DB.get_one_where(libs.models.Flor, id=i.flor_id)
                    if flor.name not in row_dict:
                        row_dict[flor.name] = i.mony
                        sum_mony += i.mony
                    else:
                        row_dict[flor.name] = row_dict[flor.name] + i.mony
                        sum_mony += i.mony
            for i in sorted(list(row_dict.keys()), reverse=self.m_checkBox6.GetValue()):
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i]))
                row.append(var)
            row.append([u'-' * 20, u'-' * 20])
            row.append([gui_lib.msg.user_report_BosGetMony_text['total'], "{:.2f}".format(sum_mony)])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.user_report_BosGetMony_text['name'], row=row, col=col, template_name=template_name, template=template)
    
class Prigodi(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn7.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.user_report_Prigodi_text['m_radioBtn10'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.user_report_Prigodi_text['m_radioBtn15'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.user_report_Prigodi_text['m_radioBtn14'])
        self.m_radioBtn14.SetValue(True)
        self.m_radioBtn17.Hide()

    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        if self.user_name == gui_lib.msg.user_report_Prigodi_text[1]:
            self.db_row = libs.DB.get_all_where(libs.models.Prihod, 
                                                       pub_time__btw=(self.start_date, self.end_date), 
                                                       order='id',
                                                       descs=self.desk)
            mony_on_cart = libs.DB.get_all_where(libs.models.MonyOnCart, pub_time__btw=(self.start_date, self.end_date), out=False)
            bonus_cart = libs.DB.get_all_where(libs.models.BonusCartLog, pub_time__btw=(self.start_date, self.end_date))
            cust_bonus_cart = libs.DB.get_all_where(libs.models.ClienBonusHold, pub_time__btw=(self.start_date, self.end_date))
            virtual_in = libs.DB.get_all_where(libs.models.CustInOutAFT, pub_time__btw=(self.start_date, self.end_date), out=True)
            lipsi = libs.DB.get_all_where(libs.models.Lipsi, pub_time__btw=(self.start_date, self.end_date), chk=True, if_lipsa=False)

        else:
            user = libs.DB.get_one_where(libs.models.User, name=self.user_name)
            self.db_row = libs.DB.get_all_where(libs.models.Prihod, 
                                                       pub_time__btw=(self.start_date, self.end_date),
                                                       user_id=user.id, 
                                                       order='id',
                                                       descs=self.desk)
            mony_on_cart = libs.DB.get_all_where(libs.models.MonyOnCart, pub_time__btw=(self.start_date, self.end_date), pub_user_id=user.id, out=False)
            bonus_cart = libs.DB.get_all_where(libs.models.BonusCartLog,
                                               pub_time__btw=(self.start_date, self.end_date), user_id=user.id)
            cust_bonus_cart = libs.DB.get_all_where(libs.models.ClienBonusHold,
                                                    pub_time__btw=(self.start_date, self.end_date), user_id=user.id)
            virtual_in = libs.DB.get_all_where(libs.models.CustInOutAFT, pub_time__btw=(self.start_date, self.end_date),
                                               out=True, user_id=user.id)
            lipsi = libs.DB.get_all_where(libs.models.Lipsi, pub_time__btw=(self.start_date, self.end_date), chk=True, user_id=user.id, if_lipsa=False)


        self.hold_bonus = libs.DB.get_one_where(libs.models.Config, name='bonus_cart_hold').value
        # self.hold_bonus = self.hold_bonus.value
        for i in lipsi:
            # if i.mony < 0:
            i.it_is = 'Lipsi'
                # print i.mony
            self.db_row.append(i)
        for i in cust_bonus_cart:
            bonus_cart.append(i)

        for i in virtual_in:
            if i.user_id != None:
                i.it_is = 'VirtualOut'
                self.db_row.append(i)

        for i in bonus_cart:
            if i.user_id != None:
                if i.bonus_hold is False:
                    i.it_is = 'BonusCart'
                else:
                    i.it_is = 'BonusCartHold'
                self.db_row.append(i)
        #
        for i in mony_on_cart:
            i.it_is = 'MonyOnCart'
            self.db_row.append(i)

        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        row = {}
        template_name = gui_lib.msg.user_report_Prigodi_text['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)
    
    def table_report(self):
        template = 'report.html'
#         template_name = u'Приходи' 
        template_name = gui_lib.msg.user_report_Prigodi_text['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        total = 0.0
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.user_report_Prigodi_text[2],
                   gui_lib.msg.user_report_Prigodi_text[3],
                   gui_lib.msg.user_report_Prigodi_text[4],
                   gui_lib.msg.user_report_Prigodi_text[5],
                   gui_lib.msg.user_report_Prigodi_text[6]]
            row = []
            for i in self.db_row:
                var = []
                try:
                    i.reson_id
                    var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                    var.append(i.user.name)
                    var.append(i.reson.name)
                    total += i.mony
                    if i.info != None:
                        var.append(i.info)
                    else:
                        var.append(u'')
                    var.append("{:.2f}".format(i.mony))
                except AttributeError:
                    if i.it_is == 'MonyOnCart':
                        total += i.mony
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.pub_user.name)
                        var.append(gui_lib.msg.cust_MonyOnCart_IN)
                        var.append(i.cust.name)
                        var.append("{:.2f}".format(i.mony))
                    elif i.it_is == 'VirtualOut':
                        total += i.mony
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.user.name)
                        var.append(gui_lib.msg.aft_out)
                        var.append(i.cust.name)
                        var.append("{:.2f}".format(i.mony))
                    elif i.it_is == 'BonusCart':
                        total += i.mony
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.user.name)
                        var.append(gui_lib.msg.bonus_cart)
                        var.append(u'')
                        var.append("{:.2f}".format(i.mony))
                    elif i.it_is == 'BonusCartHold' and self.hold_bonus == 'True':
                        total += i.bonus
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.user.name)
                        var.append(gui_lib.msg.bonus_cart_hold)
                        var.append(u'')
                        var.append("{:.2f}".format(i.bonus))
                    elif i.it_is == 'Lipsi':
                        total += i.mony
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.user.name)
                        var.append(gui_lib.msg.order_m_tool4)
                        var.append(u'')
                        var.append("{:.2f}".format(i.mony))
                if var != []:
                    row.append(var)

            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10])
            row.append([u'', u'', u'', gui_lib.msg.user_report_Prigodi_text[7], "{:.2f}".format(total)])
        elif self.m_radioBtn15.GetValue() is True:
            col = [ gui_lib.msg.user_report_Prigodi_text[3],
                    gui_lib.msg.user_report_Prigodi_text[6]]
            row = []
            row_dict = {}
            for i in self.db_row:
                try:
                    i.user.name
                    try:
                        i.it_is
                        if i.it_is == 'BonusCartHold' and self.hold_bonus == 'True':
                            if i.user.name not in row_dict:
                                row_dict[i.user.name] = i.bonus
                            else:
                                row_dict[i.user.name] = row_dict[i.user.name] + i.bonus
                            total += i.bonus
                        elif i.it_is != 'BonusCartHold':
                            if i.user.name not in row_dict:
                                row_dict[i.user.name] = i.mony
                            else:
                                row_dict[i.user.name] = row_dict[i.user.name] + i.mony
                            total += i.mony
                        # elif i.it_is != 'Lipsi':
                        #     if i.user.name not in row_dict:
                        #         row_dict[i.user.name] = i.mony
                        #     else:
                        #         row_dict[i.user.name] = row_dict[i.user.name] + i.mony
                        #     total += i.mony
                    except AttributeError:
                        if i.user.name not in row_dict:
                            row_dict[i.user.name] = i.mony
                        else:
                            row_dict[i.user.name] = row_dict[i.user.name] + i.mony
                        total += i.mony
                except AttributeError:
                    if i.it_is == 'BonusCartHold' and self.hold_bonus == 'True':
                        if i.pub_user.name not in row_dict:
                            row_dict[i.pub_user.name] = i.bonus
                        else:
                            row_dict[i.pub_user.name] = row_dict[i.pub_user.name] + i.bonus
                        total += i.bonus
                    elif i.it_is != 'BonusCartHold':
                        if i.pub_user.name not in row_dict:
                            row_dict[i.pub_user.name] = i.mony
                        else:
                            row_dict[i.pub_user.name] = row_dict[i.pub_user.name] + i.mony
                        total += i.mony
                
            for i in sorted(list(row_dict.keys()), reverse=self.m_checkBox6.GetValue()):
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i]))
                row.append(var)
            row.append([u'-'*10, u'-'*10])
            row.append([gui_lib.msg.user_report_Prigodi_text[7], "{:.2f}".format(total)])
            
        elif self.m_radioBtn14.GetValue() is True:
            col = [ gui_lib.msg.user_report_Prigodi_text[4],
                    gui_lib.msg.user_report_Prigodi_text[6]]
            row = []
            row_dict = {}
            for i in self.db_row:
                try:
                    i.reson_id
                    total += i.mony
                    if i.reson.name not in row_dict:
                        row_dict[i.reson.name] = i.mony
                    else:
                        row_dict[i.reson.name] = row_dict[i.reson.name] + i.mony
                except AttributeError:
                    if i.it_is == 'MonyOnCart':
                        if gui_lib.msg.cust_MonyOnCart_IN not in row_dict:
                            row_dict[gui_lib.msg.cust_MonyOnCart_IN] = i.mony
                        else:
                            row_dict[gui_lib.msg.cust_MonyOnCart_IN] += i.mony
                        total += i.mony
                    elif i.it_is == 'BonusCart':
                        if gui_lib.msg.bonus_cart not in row_dict:
                            row_dict[gui_lib.msg.bonus_cart] = i.mony
                        else:
                            row_dict[gui_lib.msg.bonus_cart] += i.mony
                        total += i.mony
                    elif i.it_is == 'BonusCartHold' and self.hold_bonus == 'True':
                        if gui_lib.msg.bonus_cart_hold not in row_dict:
                            row_dict[gui_lib.msg.bonus_cart_hold] = i.bonus
                        else:
                            row_dict[gui_lib.msg.bonus_cart_hold] += i.bonus
                        total += i.bonus
                    elif i.it_is ==  'VirtualOut':
                        if gui_lib.msg.aft_out not in row_dict:
                            row_dict[gui_lib.msg.aft_out] = i.mony
                        else:
                            row_dict[gui_lib.msg.aft_out] += i.mony
                        total += i.mony
                    elif i.it_is ==  'Lipsi':
                        if gui_lib.msg.order_m_tool4 not in row_dict:
                            row_dict[gui_lib.msg.order_m_tool4] = i.mony
                        else:
                            row_dict[gui_lib.msg.order_m_tool4] += i.mony
                        total += i.mony
            for i in sorted(list(row_dict.keys()), reverse=self.m_checkBox6.GetValue()):
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i]))
                row.append(var)
            row.append([u'-'*10, u'-'*10])
            row.append([gui_lib.msg.user_report_Prigodi_text[7], "{:.2f}".format(total)])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.user_report_Prigodi_text['name'], row=row, col=col, template_name=template_name, template=template)
        
        
class Razhodi(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn7.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.user_report_Razhodi_text['m_radioBtn10'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.user_report_Razhodi_text['m_radioBtn15'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.user_report_Razhodi_text['m_radioBtn14'])
        self.m_radioBtn14.SetValue(True)
        self.m_radioBtn17.Hide()

    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        if self.user_name == gui_lib.msg.user_report_Razhodi_text[1]:
            self.db_row = libs.DB.get_all_where(libs.models.Razhod, 
                                                       pub_time__btw=(self.start_date, self.end_date), 
                                                       order='id',
                                                       descs=self.desk)
            mony_on_cart = libs.DB.get_all_where(libs.models.MonyOnCart, pub_time__btw=(self.start_date, self.end_date),
                                                 out=True)
            atm = libs.DB.get_all_where(libs.models.BankTransfer, pub_time__btw=(self.start_date, self.end_date))
            mony_back = libs.DB.get_all_where(libs.models.MonuBackPay,  pub_time__btw=(self.start_date, self.end_date))
            virtual_in = libs.DB.get_all_where(libs.models.CustInOutAFT, pub_time__btw=(self.start_date, self.end_date),
                                               out=False)
            lipsi = libs.DB.get_all_where(libs.models.Lipsi, pub_time__btw=(self.start_date, self.end_date), chk=True, if_lipsa=True)
        else:
            user = libs.DB.get_one_where(libs.models.User, name=self.user_name)
            self.db_row = libs.DB.get_all_where(libs.models.Razhod, 
                                                       pub_time__btw=(self.start_date, self.end_date),
                                                       user_id=user.id, 
                                                       order='id',
                                                       descs=self.desk)
            mony_on_cart = libs.DB.get_all_where(libs.models.MonyOnCart, pub_time__btw=(self.start_date, self.end_date),
                                                 pub_user_id=user.id, out=True)
            atm = libs.DB.get_all_where(libs.models.BankTransfer, pub_time__btw=(self.start_date, self.end_date), user_id=user.id, )
            mony_back = libs.DB.get_all_where(libs.models.MonuBackPay, pub_time__btw=(self.start_date, self.end_date), pub_user_id=user.id)
            virtual_in = libs.DB.get_all_where(libs.models.CustInOutAFT, pub_time__btw=(self.start_date, self.end_date),
                                               out=False, user_id=user.id)
            lipsi = libs.DB.get_all_where(libs.models.Lipsi, pub_time__btw=(self.start_date, self.end_date), chk=True, user_id=user.id, if_lipsa=True)

        for i in lipsi:
            # if i.mony > 0:
            i.it_is = 'Lipsi'
            self.db_row.append(i)

        for i in virtual_in:
            if i.user_id != None:
                i.it_is = 'VirtualIn'
                self.db_row.append(i)

        for i in mony_on_cart:
            i.it_is = 'MONY_ON_CART'
            self.db_row.append(i)
        for i in atm:
            i.it_is = 'ATM'
            self.db_row.append(i)
        for i in mony_back:
            if not i.pub_user_id:
                pass
            else:
                i.it_is = 'MonyBack'
                self.db_row.append(i)

        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        row = {}
        template_name = gui_lib.msg.user_report_Razhodi_text['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)
    
    def table_report(self):
        template = 'report.html'
#         template_name = u'Разходи' 
        template_name = gui_lib.msg.user_report_Razhodi_text['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        total = 0.0
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.user_report_Razhodi_text[2],
                   gui_lib.msg.user_report_Razhodi_text[3],
                   gui_lib.msg.user_report_Razhodi_text[4],
                   gui_lib.msg.user_report_Razhodi_text[5],
                   gui_lib.msg.user_report_Razhodi_text[6]]
            row = []
            for i in self.db_row:
                # print(i)
                var = []
                try:
                    i.reson_id
                    var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                    var.append(i.user.name)
                    var.append(i.reson.name)
                    if i.info != None:
                        var.append(i.info)
                    else:
                        var.append(u'')
                    var.append("{:.2f}".format(i.mony))
                    # row.append(var)
                    total += i.mony
                except AttributeError:

                    if i.it_is == 'ATM':
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.user.name)
                        var.append(gui_lib.msg.cust_atm)
                        var.append(i.cust.name)
                        var.append("{:.2f}".format(i.mony))
                        # row.append(var)
                    elif i.it_is == 'VirtualIn':
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.user.name)
                        var.append(gui_lib.msg.aft_in)
                        var.append(i.cust.name)
                        var.append("{:.2f}".format(i.mony))
                        # row.append(var)
                    elif i.it_is == 'MonyBack':
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.pub_user.name)
                        var.append(gui_lib.msg.cust_MonyBack)
                        var.append(i.cust.name)
                        var.append("{:.2f}".format(i.mony))
                    elif i.it_is == 'Lipsi':
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.user.name)
                        var.append(gui_lib.msg.order_m_tool4)
                        var.append('')
                        var.append("{:.2f}".format(i.mony))
                    elif i.it_is == 'MONY_ON_CART':
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(i.pub_user.name)
                        var.append(gui_lib.msg.cust_main_Main_text[5])
                        var.append('')
                        var.append("{:.2f}".format(i.mony))
                    total += i.mony
                row.append(var)
                # print (row)
            row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10])
            row.append([u'', u'', u'', gui_lib.msg.user_report_Razhodi_text[7], "{:.2f}".format(total)])
        elif self.m_radioBtn15.GetValue() is True:
            col = [gui_lib.msg.user_report_Razhodi_text[3],
                    gui_lib.msg.user_report_Razhodi_text[6]]
            row = []
            row_dict = {}
            for i in self.db_row:
                try:
                    if i.user.name not in row_dict:
                        row_dict[i.user.name] = i.mony
                    else:
                        row_dict[i.user.name] = row_dict[i.user.name] + i.mony
                except AttributeError:
                    if i.it_is == 'ATM':
                        pass
                    else:
                        if i.pub_user.name not in row_dict:
                            row_dict[i.pub_user.name] = i.mony
                        else:
                            row_dict[i.pub_user.name] = row_dict[i.pub_user.name] + i.mony
                total += i.mony
            for i in sorted(list(row_dict.keys()), reverse=self.m_checkBox6.GetValue()):
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i]))
                row.append(var)
            row.append([u'-'*10, u'-'*10])
            row.append([gui_lib.msg.user_report_Razhodi_text[7], "{:.2f}".format(total)])
        elif self.m_radioBtn14.GetValue() is True:
            col = [gui_lib.msg.user_report_Razhodi_text[4],
                    gui_lib.msg.user_report_Razhodi_text[6]]
            row = []
            row_dict = {}
            for i in self.db_row:
                try:
                    if i.reson.name not in row_dict:
                        row_dict[i.reson.name] = i.mony
                    else:
                        row_dict[i.reson.name] = row_dict[i.reson.name] + i.mony
                except AttributeError:
                    if i.it_is == 'ATM':
                        if gui_lib.msg.cust_atm not in row_dict:
                            row_dict[gui_lib.msg.cust_atm] = i.mony
                        else:
                            row_dict[gui_lib.msg.cust_atm] = row_dict[gui_lib.msg.cust_atm] + i.mony
                    elif i.it_is == 'VirtualIn':
                        if gui_lib.msg.aft_in not in row_dict:
                            row_dict[gui_lib.msg.aft_in] = i.mony
                        else:
                            row_dict[gui_lib.msg.aft_in] = row_dict[gui_lib.msg.aft_in] + i.mony
                    elif i.it_is == 'MonyBack':
                        if gui_lib.msg.cust_MonyBack not in row_dict:
                            row_dict[gui_lib.msg.cust_MonyBack] = i.mony
                        else:
                            row_dict[gui_lib.msg.cust_MonyBack] = row_dict[gui_lib.msg.cust_MonyBack] + i.mony
                    elif i.it_is == 'Lipsi':
                        if gui_lib.msg.order_m_tool4 not in row_dict:
                            row_dict[gui_lib.msg.order_m_tool4] = i.mony
                        else:
                            row_dict[gui_lib.msg.order_m_tool4] = row_dict[gui_lib.msg.order_m_tool4] + i.mony
                    else:
                        if gui_lib.msg.cust_MonyOnCart_OUT not in row_dict:
                            row_dict[gui_lib.msg.cust_MonyOnCart_OUT] = i.mony
                        else:
                            row_dict[gui_lib.msg.cust_MonyOnCart_OUT] = row_dict[gui_lib.msg.cust_MonyOnCart_OUT] + i.mony

                total += i.mony
            for i in sorted(list(row_dict.keys()), reverse=self.m_checkBox6.GetValue()):
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i]))
                row.append(var)
            row.append([u'-'*10, u'-'*10])
            row.append([gui_lib.msg.user_report_Razhodi_text[7], "{:.2f}".format(total)])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.user_report_Razhodi_text['name'], row=row, col=col, template_name=template_name, template=template)
        
class KasaTransfer(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn7.Hide()
        self.m_radioBtn10.Hide()
        self.m_radioBtn15.Hide()
        self.m_radioBtn14.Hide()
        self.m_radioBtn17.Hide()

    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        if self.user_name == gui_lib.msg.cust_report_Transfer_text[1]:
            self.db_row = libs.DB.get_all_where(libs.models.KasaTransfer,
                                                pub_time__btw=(self.start_date, self.end_date),
                                                order='id',
                                                descs=self.desk)
        else:
            user = libs.DB.get_one_where(libs.models.User, name=self.user_name)
            db_row1 = libs.DB.get_all_where(libs.models.KasaTransfer,
                                                pub_time__btw=(self.start_date, self.end_date),
                                                from_user_id=user.id,
                                                order='id',
                                                descs=self.desk)
            db_row2 = libs.DB.get_all_where(libs.models.KasaTransfer,
                                                pub_time__btw=(self.start_date, self.end_date),
                                                to_user_id=user.id,
                                                order='id',
                                                descs=self.desk)
            for i in db_row1:
                self.db_row.append(i)
            for i in db_row2:
                self.db_row.append(i)

        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        row = {}
        template_name = gui_lib.msg.cust_report_Transfer_text['name'] + u':(%s/%s)' % (
            self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.cust_report_Transfer_text['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        total = 0.0
        col = [gui_lib.msg.cust_report_Transfer_text[2],
               gui_lib.msg.cust_report_Transfer_text[3],
               gui_lib.msg.cust_report_Transfer_text[4],
               gui_lib.msg.cust_report_Transfer_text[5],
               gui_lib.msg.cust_report_Transfer_text[6],
               gui_lib.msg.cust_report_Transfer_text[7]]
        row = []
        for i in self.db_row:
            tmp = []
            tmp.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
            tmp.append(str(i.from_user.name))
            tmp.append(str(i.to_user.name))
            if i.reson == 0:
                tmp.append(gui_lib.msg.cust_report_Transfer_text[9])
            elif i.reson == 1:
                tmp.append(gui_lib.msg.cust_report_Transfer_text[10])
            elif i.reson == 2:
                tmp.append(gui_lib.msg.cust_report_Transfer_text[11])
            else:
                tmp.append(gui_lib.msg.cust_report_Transfer_text[12])
            if i.info == None:
                tmp.append(u'')
            else:
                tmp.append(str(i.info))
            total += i.mony
            tmp.append("{:.2f}".format(i.mony))
            row.append(tmp)
        row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10])
        row.append([u'', u'', u'', u'', gui_lib.msg.cust_report_Transfer_text[8], "{:.2f}".format(total)])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.cust_report_Transfer_text['name'],
                                                                      row=row, col=col, template_name=template_name,
                                                                      template=template)




class ConterGetError( Report ):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn15.Hide()
        self.m_radioBtn14.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn17.Hide()
#         
    def OnGo(self, event):
        self.db_row = []
        db_row = []
        template = 'report.html'
#         template_name = u'Грешки при отчитане' 
        
        col = [gui_lib.msg.user_report_ConterGetError_text[1],
               gui_lib.msg.user_report_ConterGetError_text[2],
               gui_lib.msg.user_report_ConterGetError_text[3],
               gui_lib.msg.user_report_ConterGetError_text[4]]
        row = []
        start_date = self.m_calendar1.GetDate()
        start_date = start_date.Format('%Y-%m-%d')
        end_date = self.m_calendar2.GetDate()
        end_date = end_date.Format('%Y-%m-%d')
        template_name = gui_lib.msg.user_report_ConterGetError_text['name'] + ': (%s/%s)' % (start_date[:-3], end_date[:-3])
#         start_date = start_date + ' ' + str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
        start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(start_date + ' 00:00:00', start_date + ' 23:59:59'))
        if start_times == None:
            start_times = ' 09:00:00'
        else:
            start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')
        start_date = start_date + ' ' + start_times
         
#         end_date = end_date + ' ' + str(self.m_spinCtrl3.GetValue()) + ':' + str(self.m_spinCtrl4.GetValue())
        end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(end_date + ' 00:00:00', end_date + ' 23:59:59'))
        if end_times == None:
            end_times = libs.models.TZ.now()
            end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
        else:
            end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')
#         end_date = end_date + ' ' + libs.models.TZ.date_to_str(end_times, '%H:%M')
        end_date = end_date + ' ' + end_times
         
        user_name =  self.m_choice3.GetString(self.m_choice3.GetSelection())
        desk = self.m_checkBox6.GetValue()
        user_name =  self.m_choice3.GetString(self.m_choice3.GetSelection())
        if user_name == gui_lib.msg.user_report_ConterGetError_text[5]:
            db_row = libs.DB.get_all_where(libs.models.GetCounterError, 
                                                       pub_time__btw=(start_date, end_date),
                                                       order='id')
        else:
            user = libs.DB.get_one_where(libs.models.User, name=user_name)
            db_row = libs.DB.get_all_where(libs.models.GetCounterError, 
                                                       pub_time__btw=(start_date, end_date),
                                                       user_id=user.id, )
        for item in db_row:
            var = []
            var.append(libs.models.TZ.date_to_str(item.pub_time, '%d.%m.%Y %H:%M:%S'))
            if item.user_id!= None:
                var.append(item.user.name)
            else:
                var.append('')
            if item.mashin_nom_in_l != None:
                var.append(str(item.mashin_nom_in_l))
            else:
                var.append('')
            var.append(item.info)
            row.append(var)
#         print row
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.user_report_ConterGetError_text['name'], row=row, col=col, template_name=template_name, template=template)

class InOut(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn9.Hide()
        self.m_radioBtn8.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.user_report_InOut_text['m_radioBtn10'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.user_report_InOut_text['m_radioBtn14'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.user_report_InOut_text['m_radioBtn15'])
        self.m_radioBtn17.Hide()
        self.m_checkBox6.Hide()
        self.parent = parent

    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        self.row = []
        user_name = self.m_choice3.GetString(self.m_choice3.GetSelection())
        if user_name == gui_lib.msg.user_report_InOut_text[8]:
            if self.m_radioBtn10.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.MonyOnCart, pub_time__btw=(self.start_date, self.end_date), order='id', descs=True)
            elif self.m_radioBtn14.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.CustInOutAFT, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True, out=False)
            elif self.m_radioBtn15.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.CustInOutAFT, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True, out=True)
        else:
            user_id = libs.DB.get_one_where(libs.models.User, name=user_name)
            if self.m_radioBtn10.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.MonyOnCart, pub_user_id=user_id.id, pub_time__btw=(self.start_date, self.end_date), order='id', descs=True)
            elif self.m_radioBtn14.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.CustInOutAFT, user_id=user_id.id, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True, out=False)
            elif self.m_radioBtn15.GetValue() is True:
                self.row = libs.DB.get_all_where(libs.models.CustInOutAFT, user_id=user_id.id, pub_time__btw=(self.start_date, self.end_date),
                                                 order='id', descs=True, out=True)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        row = {}
        y_label = ''
        x_label = ''
        X = []
        template_name = gui_lib.msg.user_report_InOut_text['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name, y_title=y_label, x_title=x_label, X=X)

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.user_report_InOut_text['name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        row = []
        col = [gui_lib.msg.user_report_InOut_text[1],
               gui_lib.msg.user_report_InOut_text[2],
               gui_lib.msg.user_report_InOut_text[3],
               gui_lib.msg.user_report_InOut_text[4],
               gui_lib.msg.user_report_InOut_text[5],
               gui_lib.msg.user_report_InOut_text[6],
               gui_lib.msg.user_report_InOut_text[7],
               gui_lib.msg.report_InOut_text[11]]
        total_out = 0
        total_in = 0
        gornica_sum = 0
        for i in self.row:
            var = []
            var.append(str(i.id))
            var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
            try:
                var.append(str(i.pub_user.name))
            except AttributeError:
                var.append(str(i.user.name))
            var.append(str(i.cust.name))
            var.append(str(i.cust.grup.name))

            if i.out is False:
                total_in += i.mony
                var.append("{:.2f}".format(i.mony))
                var.append('')
                var.append('')
            else:
                total_out += i.mony
                gornica_sum += i.mony - int(i.mony)
                var.append('')
                var.append("{:.2f}".format(i.mony))
                var.append("{:.2f}".format(i.mony - int(i.mony)))
            row.append(var)
        row.append([u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10, u'-' * 10])
        row.append([u'', u'', u'', u'', gui_lib.msg.user_report_InOut_text[9], "{:.2f}".format(total_in) , "{:.2f}".format(total_out), "{:.2f}".format(gornica_sum)])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.user_report_InOut_text['name'], row=row,
                                                                      col=col,
                                                                      template_name=template_name, template=template)

class WorkTime(Report):
    def __init__(self, parent):
        self.parent = parent
        Report.__init__(self, parent)
        self.m_radioBtn14.Hide()
        self.m_radioBtn15.Hide()
        self.m_checkBox6.Hide()
        self.m_radioBtn7.SetLabel(gui_lib.msg.report_WorkTime[1])
        self.m_radioBtn10.SetLabel(gui_lib.msg.report_WorkTime[7])
        self.m_radioBtn7.SetValue(True)
        self.m_radioBtn10.SetValue(False)
        self.m_radioBtn17.Hide()
        # self.format_date = libs.models.TZ()

    def OnGo( self, event ):
        self.get_conf_selection()
        self.db_row = []
        user_name = self.m_choice3.GetString(self.m_choice3.GetSelection())
        if user_name != gui_lib.msg.report_WorkTime[2]:
            users = libs.DB.get_all_where(libs.models.User, enable=self.m_radioBtn9.GetValue())
            for i in users:
                row = libs.DB.get_all_where(libs.models.StartWork, user_id=i.id, pub_time__btw=(self.start_date, self.end_date), start=False)
                for b in row:
                    self.db_row.append(b)

        else:
            # users = libs.DB.get_one_where(libs.models.User, name=user_name)
            self.db_row = libs.DB.get_all_where(libs.models.StartWork, pub_time__btw=(self.start_date, self.end_date), start=False)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        row = {}
        template_name = gui_lib.msg.report_WorkTime['name'] + u':(%s/%s)' % (
            self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.report_WorkTime['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])

        row = []
        tmp = {}
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.report_WorkTime[3],
                   gui_lib.msg.report_WorkTime[4],
                   gui_lib.msg.report_WorkTime[5],
                   gui_lib.msg.report_WorkTime[6],
                   ]
            for i in self.db_row:
                if i.end_time is not None:
                    a = (i.end_time - i.pub_time)
                    # b = int(a.seconds/60.0/60.0)
                    b = divmod(a.seconds, 3600)
                    c = divmod(a.seconds, 60)
                    d = '%s' % (b[0])
                    m = '%s' % (c[0]-b[0]*60)
                    if len(m) == 1:
                        d = d + '.0' + m
                    else:
                        d = d + '.' + m
                        # b+=(int(a.seconds/60.0)*0.001)
                    row.append([str(i.user.name),
                                str(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S')),
                                str(libs.models.TZ.date_to_str(i.end_time, '%d.%m.%Y %H:%M:%S')),
                                "{:.2f}".format(float(d))
                                ])

        else:
            col = [gui_lib.msg.report_WorkTime[3],
                   gui_lib.msg.report_WorkTime[6],
                   ]
            for i in self.db_row:
                if i.end_time is not None:
                    if i.user_id not in tmp:
                        a = (i.end_time - i.pub_time)
                        b = divmod(a.seconds, 3600)
                        c = divmod(a.seconds, 60)
                        # d = '%s' % (b[0])
                        # m = '%s' % (c[0] - b[0] * 60)
                        # if len(m) == 1:
                        #     d = d + '.0' + m
                        # else:
                        #     d = d + '.' + m
                        tmp[i.user_id] = [i.user.name, b[0], c[0]]
                    else:
                        a = (i.end_time - i.pub_time)
                        b = divmod(a.seconds, 3600)
                        c = divmod(a.seconds, 60)
                        tmp[i.user_id][1] += b[0]
                        tmp[i.user_id][2] += c[0]
            for i in tmp:
                d = '%s' % (tmp[i][1])
                m = '%s' % (tmp[i][2] - tmp[i][1] * 60)
                if len(m) == 1:
                    d = d + '.0' + m
                else:
                    d = d + '.' + m
                row.append(
                    [tmp[i][0],
                    "{:.2f}".format(float(d))])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                          gui_lib.msg.report_WorkTime['name'],
                                                                          row=row,
                                                                          col=col,
                                                                          template_name=template_name,
                                                                          template=template)

class UserMonyBeforOrder(BosGetMony):
    def __init__(self, parent):
        BosGetMony.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn14.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.user_report_MonyBeforOdrer_text['m_radioBtn10'])
        self.m_radioBtn7.SetLabel(gui_lib.msg.user_report_MonyBeforOdrer_text['m_radioBtn15'])
        self.m_radioBtn14.Hide()
        self.m_radioBtn17.Hide()
        self.m_radioBtn15.Hide()

    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        if self.user_name == gui_lib.msg.user_report_MonyBeforOdrer_text[1]:
            self.db_row = libs.DB.get_all_where(libs.models.UserHaveMony,
                                                pub_time__btw=(self.start_date, self.end_date),
                                                order='id',
                                                descs=self.desk)
        else:
            user = libs.DB.get_one_where(libs.models.User, name=self.user_name)
            self.db_row = libs.DB.get_all_where(libs.models.UserHaveMony,
                                                pub_time__btw=(self.start_date, self.end_date),
                                                user_id=user.id,
                                                order='id',
                                                descs=self.desk)

        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        row = {}
        template_name = gui_lib.msg.user_report_MonyBeforOdrer_text['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            pass
        elif self.m_radioBtn15.GetValue() is True:
            pass
        elif self.m_radioBtn14.GetValue() is True:
            pass
        elif self.m_radioBtn7.GetValue() is True:
            pass
        self.parent.GetParent().GetParent().GetParent().pic.show(row, template_name)

    def table_report(self):
        template = 'report.html'
            #         template_name = u'Отчетени пари'
        template_name = gui_lib.msg.user_report_MonyBeforOdrer_text['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.user_report_MonyBeforOdrer_text[2],
                       gui_lib.msg.user_report_MonyBeforOdrer_text[3],
                       gui_lib.msg.user_report_MonyBeforOdrer_text[5]]
            row = []
            for i in self.db_row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(i.user.name)

                var.append("{:.2f}".format(i.mony))
                row.append(var)
        elif self.m_radioBtn7.GetValue() is True:
            col = [gui_lib.msg.user_report_BosGetMony_text[3],
                       gui_lib.msg.user_report_BosGetMony_text[5]]
            row = []
            row_dict = {}
            for i in self.db_row:
                if i.user.name not in row_dict:
                    row_dict[i.user.name] = i.mony
                else:
                    row_dict[i.user.name] = row_dict[i.user.name] + i.mony
            for i in sorted(list(row_dict.keys()), reverse=self.m_checkBox6.GetValue()):
                var = []
                var.append(i)
                var.append("{:.2f}".format(row_dict[i]))
                row.append(var)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                          gui_lib.msg.user_report_MonyBeforOdrer_text[
                                                                              'name'], row=row, col=col,
                                                                          template_name=template_name,
                                                                          template=template)

class MonyOpis(Report):
    def __init__(self, parent):
        self.parent = parent
        Report.__init__(self, parent)
        self.m_radioBtn14.Hide()
        self.m_radioBtn15.Hide()
        self.m_checkBox6.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.report_mony_Opis[1])
        # self.m_radioBtn7.SetValue(True)
        self.m_radioBtn10.SetValue(True)
        self.m_radioBtn17.Hide()

    def OnGo( self, event ):
        self.get_conf_selection()
        self.db_row = []
        user_name = self.m_choice3.GetString(self.m_choice3.GetSelection())
        if user_name != gui_lib.msg.report_mony_Opis[2]:
            users = libs.DB.get_all_where(libs.models.User, enable=self.m_radioBtn9.GetValue())
            for i in users:
                row = libs.DB.get_all_where(libs.models.MonyOrder, user_id=i.id, pub_time__btw=(self.start_date, self.end_date))
                for b in row:
                    self.db_row.append(b)

        else:
            # users = libs.DB.get_one_where(libs.models.User, name=user_name)
            self.db_row = libs.DB.get_all_where(libs.models.MonyOrder, pub_time__btw=(self.start_date, self.end_date))
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.report_mony_Opis['name'] + u':(%s/%s)' % (
            self.start_date[:-3], self.end_date[:-3])

        row = []
        col = [gui_lib.msg.report_mony_Opis[9],
               gui_lib.msg.report_mony_Opis[3],
               gui_lib.msg.report_mony_Opis[4],
               gui_lib.msg.report_mony_Opis[5],
               gui_lib.msg.report_mony_Opis[6],
               gui_lib.msg.report_mony_Opis[7],
               gui_lib.msg.report_mony_Opis[8],
               ]
        for i in self.db_row:

            opis = json.loads(i.data)
            key = list(opis.keys())
            tmp = {}
            for c in key:
                tmp[float(c)] = float(opis[c])
            for b in sorted(tmp, reverse=True):
                var = []
                var.append(str(i.id))
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(i.user.name)
                var.append("{:.2f}".format(i.total))
                var.append(str(tmp[b]))
                var.append(str(b))
                var.append("{:.2f}".format(tmp[b]*b))
                row.append(var)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.report_mony_Opis['name'],
                                                                      row=row,
                                                                      col=col,
                                                                      template_name=template_name,
                                                                      template=template)


class EGNChecked(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn7.Hide()
        self.m_radioBtn14.Hide()
        self.m_radioBtn15.Hide()
        self.m_radioBtn17.Hide()

    def OnGo(self, event):
        self.get_conf_selection()
        self.db_row = []
        if self.user_name == gui_lib.msg.egn_checked[1]:
            self.db_row = libs.DB.get_all_where(libs.models.EGNCheck,
                                                pub_time__btw=(self.start_date, self.end_date),
                                                #                                                        order=self.order_by[order_by],
                                                descs=self.desk
                                                )
        else:
            user = libs.DB.get_one_where(libs.models.User, name=self.user_name)
            self.db_row = libs.DB.get_all_where(libs.models.EGNCheck,
                                                pub_time__btw=(self.start_date, self.end_date),
                                                user_id=user.id,
                                                #                                                        order=self.order_by[order_by],
                                                descs=self.desk
                                                )
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.egn_checked['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        row = []
        col = [gui_lib.msg.egn_checked[2],
               gui_lib.msg.egn_checked[3],
               gui_lib.msg.egn_checked[4],
               gui_lib.msg.egn_checked[5],
               gui_lib.msg.egn_checked[6],
               gui_lib.msg.egn_checked[7],
               ]
        count = 0
        for i in self.db_row:
            count += 1
            var = []
            var.append(str(count))
            var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
            if i.user_id:
                var.append(i.user.name)
            else:
                var.append('')
            var.append(i.egn)
            if i.player_id:
                var.append(i.player.name)
            else:
                var.append('')
            if i.by_hand is True:
                var.append(gui_lib.msg.egn_checked[8])
            else:
                var.append('')
            row.append(var)
        row.append([u'-' * 12, u'-' * 12, u'-' * 12, u'-' * 12, u'-' * 12, u'-' * 12])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.egn_checked['name'],
                                                                      row=row,
                                                                      col=col,
                                                                      template_name=template_name, template=template)

if __name__ == '__main__':
    pass
