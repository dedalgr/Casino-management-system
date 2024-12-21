#-*- coding:utf-8 -*-
'''
Created on 04.04.2019

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


class Report(gui.UserReport):
    def __init__(self, parent):
        gui.UserReport.__init__(self, parent)
        self.parent = parent
        #         self.parent = parent
        self.m_radioBtn17.Hide()
        # self.parent.GetParent().GetParent().GetParent().GetParent().SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.cust_report_Report_name)
        # self.add_choice()
        self.m_staticText7.Hide()
        self.m_choice3.Hide()
        self.m_checkBox6.Hide()
        self.m_radioBtn9.Hide()
        self.m_radioBtn8.Hide()
        # self.m_radioBtn9.Hide()
        # self.m_radioBtn8.Hide()
        self.m_staticText7.SetLabel(gui_lib.msg.cust_report_Report_text['m_staticText7'])
        self.m_radioBtn9.SetLabel(gui_lib.msg.cust_report_Report_button['m_radioBtn9'])
        self.m_radioBtn8.SetLabel(gui_lib.msg.cust_report_Report_button['m_radioBtn8'])
        self.m_radioBtn10.SetLabel(gui_lib.msg.cust_report_Report_button['m_radioBtn10'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.cust_report_Report_button['m_radioBtn14'])
        self.m_radioBtn7.SetLabel(gui_lib.msg.cust_report_Report_button['m_radioBtn7'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.cust_report_Report_button['m_radioBtn15'])
        self.m_checkBox6.SetLabel(gui_lib.msg.cust_report_Report_button['m_checkBox6'])
        self.m_radioBtn16.SetLabel(gui_lib.msg.cust_report_Report_button['m_radioBtn16'])
        self.m_radioBtn17.SetLabel(gui_lib.msg.cust_report_Report_button['m_radioBtn17'])
        self.m_button6.SetLabel(gui_lib.msg.cust_report_Report_button['m_button6'])

        self.m_calendar1.SetToolTip(gui_lib.msg.cust_report_Report_tooltim['m_calendar1'])
        self.m_calendar2.SetToolTip(gui_lib.msg.cust_report_Report_tooltim['m_calendar2'])
        # self.m_radioBtn14.SetLabel(u'Обобщи по крупие')
        self.row = []
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.on_resize(None)

    def table_report(self):
        pass

    def pic_report(self):
        pass

    # def sort_by_nom_in_l(self, row_dict):
    #     sort_by_nom = {}
    #     for i in row_dict:
    #         sort_by_nom[int(row_dict[i][0])] = row_dict[i]
    #     return sort_by_nom

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetParent().GetParent().GetParent().GetParent().GetSize()
        self.m_choice3.SetMinSize((self.width * 0.48, -1))
        self.SetSize((self.width, self.height))
        if event != None:
            event.Skip()
            self.Layout()

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
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

class BonusGet(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn15.SetLabel(gui_lib.msg.cust_report_BonusGet_text['m_radioBtn15'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.cust_report_BonusGet_text['m_radioBtn14'])
        self.m_radioBtn10.SetValue(True)
        self.m_checkBox6.Show()
        self.m_checkBox6.SetLabel(gui_lib.msg.cust_report_BonusGet_text['m_checkBox6'])


    def OnGo(self, event):
        self.get_date()
        self.activ = self.m_radioBtn8.GetValue()
        self.row = []
        if self.m_checkBox6.GetValue() is False:
            self.row = libs.DB.get_all_where(libs.models.BonusPay, pub_time__btw=(self.start_date, self.end_date),
                                             order='id', descs=False, use_it=True)
        else:
            self.row = libs.DB.get_all_where(libs.models.BonusPay, pub_time__btw=(self.start_date, self.end_date),
                                             order='id', descs=False, use_it=False)

        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def table_report(self):
        template = 'report_big_table.html'
        template_name = gui_lib.msg.cust_report_BonusGet_text['table_name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        row = []
        col = []
        if self.m_radioBtn10.GetValue() is True:
            template = 'veri_big_table.html'
            show_forbiden = self.m_checkBox6.GetValue()
            if show_forbiden is False:
                col = [gui_lib.msg.cust_report_BonusGet_text[1],
                       gui_lib.msg.cust_report_BonusGet_text[2],
                       gui_lib.msg.cust_report_BonusGet_text[3],
                       gui_lib.msg.cust_report_BonusGet_text[4],
                       gui_lib.msg.cust_report_BonusGet_text[5],
                       gui_lib.msg.cust_report_BonusGet_text[16],
                       gui_lib.msg.cust_report_BonusGet_text[17],
                       gui_lib.msg.cust_report_BonusGet_text[13],
                       gui_lib.msg.cust_report_BonusGet_text[14],
                       gui_lib.msg.cust_report_BonusGet_text[6],
                       ]
            else:
                col = [gui_lib.msg.cust_report_BonusGet_text[1],
                       gui_lib.msg.cust_report_BonusGet_text[2],
                       gui_lib.msg.cust_report_BonusGet_text[3],
                       gui_lib.msg.cust_report_BonusGet_text[4],
                       gui_lib.msg.cust_report_BonusGet_text[5],
                       gui_lib.msg.cust_report_BonusGet_text[16],
                       gui_lib.msg.cust_report_BonusGet_text[17],
                       gui_lib.msg.cust_report_BonusGet_text[13],
                       gui_lib.msg.cust_report_BonusGet_text[14],
                       gui_lib.msg.cust_report_BonusGet_text[6],
                       ]
            sums = [u'', u'', u'', u'', u'', u'', u'', u'', gui_lib.msg.cust_report_BonusGet_text[7], 0, ]
            row = []

            for i in self.row:
                var = []
                if show_forbiden is False:
                    if i.activ is True:
                        pass
                    else:
                        var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                        var.append(str(i.cust.name))
                        var.append(str(i.device.nom_in_l))
                        var.append(str(i.device.model.name))
                        var.append(str(i.cust.grup.name))

                        if i.from_redirect is False:
                            var.append(u'')
                            var.append(u'')
                        else:
                            var.append(gui_lib.msg.cust_report_BonusGet_text[16])
                            try:
                                var.append(str(i.from_redirect_name))
                            except:
                                var.append(u'')
                        if i.initial_on_device_id == None:
                            var.append(u'')
                            # var.append(u'')
                        else:
                            var.append(str(i.initial_on_device.nom_in_l))
                        if i.initial_pub_time != None:
                                var.append(libs.models.TZ.date_to_str(i.initial_pub_time, '%d.%m.%Y %H:%M:%S'))
                        else:
                            var.append(u'')
                        var.append("{:.2f}".format(i.mony))
                        sums[9] += i.mony
                        row.append(var)
                else:
                    var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                    var.append(str(i.cust.name))
                    var.append(str(i.device.nom_in_l))
                    var.append(str(i.device.model.name))
                    var.append(str(i.cust.grup.name))
                    if i.from_redirect is False:
                        var.append(u'')
                        var.append(u'')
                    else:
                        var.append(gui_lib.msg.cust_report_BonusGet_text[12])
                        try:
                            var.append(str(i.from_redirect_name))
                        except:
                            var.append(u'')
                    if i.initial_on_device_id == None:
                        var.append(u'')
                        # var.append(u'')
                    else:
                        var.append(str(i.initial_on_device.nom_in_l))
                        # var.append(libs.models.TZ.date_to_str(i.initial_pub_time, '%d.%m.%Y %H:%M:%S'))
                    if i.initial_pub_time != None:
                        var.append(libs.models.TZ.date_to_str(i.initial_pub_time, '%d.%m.%Y %H:%M:%S'))
                    else:
                        var.append(u'')
                    var.append("{:.2f}".format(i.mony))
                    sums[9] += i.mony
                    row.append(var)
            row.append([u'-'*15, u'-'*15, u'-'*15, u'-'*15, u'-'*15, u'-'*15, u'-'*15, u'-'*15, u'-'*15, u'-'*15])
            sums[9] = "{:.2f}".format(sums[9])
            row.append(sums)
        elif self.m_radioBtn14.GetValue() is True:
            col = [ gui_lib.msg.cust_report_BonusGet_text[1],
                    gui_lib.msg.cust_report_BonusGet_text[2],
                    gui_lib.msg.cust_report_BonusGet_text[3],
                    gui_lib.msg.cust_report_BonusGet_text[5],
                    gui_lib.msg.cust_report_BonusGet_text[15],
                    gui_lib.msg.cust_report_BonusGet_text[10]]
            sums = [u'', u'', u'', u'', gui_lib.msg.cust_report_BonusGet_text[7], 0]
            my_row = {}
            row = []
            tmp = []
            for i in self.row:
                if i.activ is True:
                    pass
                else:
                    if i.cust_id not in my_row:
                        tmp.append(i.id)
                        my_row[i.cust_id] = [libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M'),
                                             i.cust.name,
                                             str(i.device.nom_in_l),
                                             i.cust.grup.name,
                                             1,
                                             i.mony, i.id]
                    else:
                        my_row[i.cust_id][5] += i.mony
                        my_row[i.cust_id][4] += 1
                    sums[5] += i.mony
            tmp = sorted(tmp)
            for b in tmp:
                for i in my_row:
                    if b == my_row[i][6]:
                        row.append([my_row[i][0], my_row[i][1], my_row[i][2], my_row[i][3], str(my_row[i][4]), "{:.2f}".format(my_row[i][5])])
            row.append([u'-'*20, u'-'*20, u'-'*20, u'-'*20, u'-'*20, u'-'*20])
            row.append([u'', u'', u'', u'', sums[4], "{:.2f}".format(sums[5])])
        elif self.m_radioBtn7.GetValue() is True:
            col = [gui_lib.msg.cust_report_BonusGet_text[1],gui_lib.msg.cust_report_BonusGet_text[6]]
            sums = [gui_lib.msg.cust_report_BonusGet_text[7], 0]
            my_row = {}
            row = []
            self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
            # self.start_date = self.start_date - datetime.timedelta(minutes=1)
            # self.start_date = libs.DB.get_one_where(libs.models.DayReport, pub_time__lte=libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S'), descs=True)
            self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = libs.models.TZ.str_to_date(self.end_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = self.end_date + datetime.timedelta(days=1)
            # self.end_date = libs.DB.get_one_where(libs.models.DayReport,
            #                                         pub_time__gte=libs.models.TZ.date_to_str(self.end_date,
            #                                                                                 '%Y-%m-%d %H:%M:%S'))
            self.end_date = libs.models.TZ.date_to_str(self.end_date, '%Y-%m-%d %H:%M:%S')
            db_row = libs.DB.get_all_where(libs.models.DayReport, day_report=True,
                                           pub_time__btw=(self.start_date, self.end_date), order='id', descs=False)
            for i in self.row:
                for b in db_row:
                    try:
                        index = db_row[db_row.index(b) - 1]
                    except IndexError:
                        index = b
                    doc_data = json.loads(b.doc_data)
                    if i.activ is True:
                        pass
                    elif i.pub_time < b.pub_time and i.pub_time > index.pub_time:
                        if doc_data['doc_date'] not in my_row:
                            my_row[doc_data['doc_date']] = i.mony
                        else:
                            my_row[doc_data['doc_date']] += i.mony
                        sums[1] += i.mony
                    else:
                        pass
            for i in sorted(list(my_row.keys())):
                row.append([i, "{:.2f}".format(my_row[i])])
            row.append([u'-' * 20, u'-' * 20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        elif self.m_radioBtn15.GetValue() is True:
            col = [gui_lib.msg.cust_report_BonusGet_text[3], gui_lib.msg.cust_report_BonusGet_text[4], gui_lib.msg.cust_report_BonusGet_text[6]]
            sums = [u'', gui_lib.msg.cust_report_BonusGet_text[7], 0]
            my_row = {}
            row = []
            for i in self.row:
                if i.activ is True:
                    pass
                else:
                    if i.device.nom_in_l not in my_row:
                        my_row[i.device.nom_in_l] = [i.device.model.name, i.mony]
                    else:
                        my_row[i.device.nom_in_l][1] += i.mony
                    sums[2] += i.mony
            for i in sorted(list(my_row.keys())):
                row.append([str(i), str(my_row[i][0]), "{:.2f}".format(my_row[i][1])])
            row.append([u'-' * 20, u'-' * 20, u'-'*20])
            sums[2] = "{:.2f}".format(sums[2])
            row.append(sums)

        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.cust_report_BonusGet_text['table_name'], row=row, col=col,
                                                                      template_name=template_name, template=template)

class MonyBackGet(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn15.SetLabel(gui_lib.msg.cust_report_MonyBackGet_text['m_radioBtn15'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.cust_report_MonyBackGet_text['m_radioBtn14'])
        self.parent = parent

    def OnGo(self, event):
        self.get_date()
        self.row = []
        self.activ = self.m_radioBtn8.GetValue()
        self.row = libs.DB.get_all_where(libs.models.MonuBackPay, pub_time__btw=(self.start_date, self.end_date), order='id', descs=True)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.cust_report_MonyBackGet_text['table_name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        row = []
        col = []
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.cust_report_MonyBackGet_text[1],
                   gui_lib.msg.cust_report_MonyBackGet_text[2],
                   gui_lib.msg.cust_report_MonyBackGet_text[3],
                   gui_lib.msg.cust_report_MonyBackGet_text[4]]
            sums = [u'', u'', gui_lib.msg.cust_report_MonyBackGet_text[5], 0]
            row = []
            for i in self.row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(str(i.cust.name))
                if i.pub_user_id:
                    var.append(str(i.pub_user.name))
                else:
                    var.append('AFT')
                var.append("{:.2f}".format(i.mony))
                sums[3] += i.mony
                row.append(var)

            row.append([u'-'*20, u'-'*20, u'-'*20, u'-'*20])
            sums[3] = "{:.2f}".format(sums[3])
            row.append(sums)
        elif self.m_radioBtn14.GetValue() is True:
            col = [ gui_lib.msg.cust_report_MonyBackGet_text[2], gui_lib.msg.cust_report_MonyBackGet_text[4]]
            sums = [gui_lib.msg.cust_report_MonyBackGet_text[5], 0]
            row = []
            my_row = {}
            for i in self.row:
                if i.cust_id not in my_row:
                    my_row[i.cust_id] = [str(i.cust.name), i.mony]
                else:
                    my_row[i.cust_id][1] += i.mony
                sums[1] += i.mony
            for i in my_row:
                row.append([my_row[i][0], "{:.2f}".format(my_row[i][1])])
            row.append([u'-'*20, u'-'*20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        elif self.m_radioBtn7.GetValue() is True:
            col = [gui_lib.msg.cust_report_MonyBackGet_text[1], gui_lib.msg.cust_report_MonyBackGet_text[4]]
            sums = [gui_lib.msg.cust_report_MonyBackGet_text[5], 0]
            my_row = {}
            row = []
            self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
            # self.start_date = self.start_date - datetime.timedelta(minutes=1)
            # self.start_date = libs.DB.get_one_where(libs.models.DayReport, pub_time__lte=libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S'), descs=True)
            self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = libs.models.TZ.str_to_date(self.end_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = self.end_date + datetime.timedelta(days=1)
            # self.end_date = libs.DB.get_one_where(libs.models.DayReport,
            #                                         pub_time__gte=libs.models.TZ.date_to_str(self.end_date,
            #                                                                                 '%Y-%m-%d %H:%M:%S'))
            self.end_date = libs.models.TZ.date_to_str(self.end_date, '%Y-%m-%d %H:%M:%S')
            db_row = libs.DB.get_all_where(libs.models.DayReport, day_report=True,
                                           pub_time__btw=(self.start_date, self.end_date), order='id', descs=False)
            for i in self.row:
                for b in db_row:
                    try:
                        index = db_row[db_row.index(b) - 1]
                    except IndexError:
                        index = b
                    doc_data = json.loads(b.doc_data)
                    if i.pub_time < b.pub_time and i.pub_time > index.pub_time:
                        if doc_data['doc_date'] not in my_row:
                            my_row[doc_data['doc_date']] = i.mony
                        else:
                            my_row[doc_data['doc_date']] += i.mony
                        sums[1] += i.mony
                    else:
                        pass
            for i in sorted(list(my_row.keys())):
                row.append([i, "{:.2f}".format(my_row[i])])
            row.append([u'-' * 20, u'-' * 20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        elif self.m_radioBtn15.GetValue() is True:
            col = [gui_lib.msg.cust_report_MonyBackGet_text[3], gui_lib.msg.cust_report_MonyBackGet_text[4]]
            sums = [gui_lib.msg.cust_report_MonyBackGet_text[5], 0]
            row = []
            my_row = {}
            for i in self.row:
                if i.pub_user_id:
                    if i.pub_user_id not in my_row:
                        my_row[i.pub_user_id] = [str(i.pub_user.name), i.mony]
                    else:
                        my_row[i.pub_user_id][1] += i.mony
                else:
                    if 'AFT' not in my_row:
                        my_row['AFT'] = ['AFT', i.mony]
                    else:
                        my_row['AFT'][1] += i.mony
                sums[1] += i.mony
            for i in my_row:
                row.append([my_row[i][0], "{:.2f}".format(my_row[i][1])])
            row.append([u'-' * 20, u'-' * 20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.cust_report_MonyBackGet_text['table_name'], row=row, col=col,
                                                                      template_name=template_name, template=template)

class TombulaGet(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn15.SetLabel(gui_lib.msg.cust_report_TombulaGet_text['m_radioBtn15'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.cust_report_TombulaGet_text['m_radioBtn14'])
        self.parent = parent

    def OnGo(self, event):
        self.get_date()
        self.row = []
        self.activ = self.m_radioBtn8.GetValue()
        self.row = libs.DB.get_all_where(libs.models.TombulaPrinted, pub_time__btw=(self.start_date, self.end_date), order='id', descs=True)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.cust_report_TombulaGet_text['table_name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        row = []
        col = []
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.cust_report_TombulaGet_text[1],
                   gui_lib.msg.cust_report_TombulaGet_text[2],
                   gui_lib.msg.cust_report_TombulaGet_text[3],
                   gui_lib.msg.cust_report_TombulaGet_text[4]]
            sums = [u'', u'', gui_lib.msg.cust_report_TombulaGet_text[5], 0]
            row = []
            for i in self.row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(str(i.cust.name))
                var.append(str(i.pub_user.name))
                var.append("{:.2f}".format(i.tombula_count))
                sums[3] += i.tombula_count
                row.append(var)

            row.append([u'-'*20, u'-'*20, u'-'*20, u'-'*20])
            sums[3] = "{:.2f}".format(sums[3])
            row.append(sums)
        elif self.m_radioBtn14.GetValue() is True:
            col = [ gui_lib.msg.cust_report_TombulaGet_text[2], gui_lib.msg.cust_report_TombulaGet_text[4]]
            sums = [gui_lib.msg.cust_report_TombulaGet_text[5], 0]
            row = []
            my_row = {}
            for i in self.row:
                if i.cust_id not in my_row:
                    my_row[i.cust_id] = [str(i.cust.name), i.tombula_count]
                else:
                    my_row[i.cust_id][1] += i.tombula_count
                sums[1] += i.tombula_count
            for i in my_row:
                row.append([my_row[i][0], "{:.2f}".format(my_row[i][1])])
            row.append([u'-'*20, u'-'*20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        elif self.m_radioBtn7.GetValue() is True:
            col = [gui_lib.msg.cust_report_TombulaGet_text[1], gui_lib.msg.cust_report_TombulaGet_text[4]]
            sums = [gui_lib.msg.cust_report_TombulaGet_text[5], 0]
            my_row = {}
            row = []
            self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
            # self.start_date = self.start_date - datetime.timedelta(minutes=1)
            # self.start_date = libs.DB.get_one_where(libs.models.DayReport, pub_time__lte=libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S'), descs=True)
            self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = libs.models.TZ.str_to_date(self.end_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = self.end_date + datetime.timedelta(days=1)
            # self.end_date = libs.DB.get_one_where(libs.models.DayReport,
            #                                         pub_time__gte=libs.models.TZ.date_to_str(self.end_date,
            #                                                                                 '%Y-%m-%d %H:%M:%S'))
            self.end_date = libs.models.TZ.date_to_str(self.end_date, '%Y-%m-%d %H:%M:%S')
            db_row = libs.DB.get_all_where(libs.models.DayReport, day_report=True,
                                           pub_time__btw=(self.start_date, self.end_date), order='id', descs=False)

            for i in self.row:
                for b in db_row:
                    try:
                        index = db_row[db_row.index(b) - 1]
                    except IndexError:
                        index = b
                    doc_data = json.loads(b.doc_data)
                    if i.pub_time < b.pub_time and i.pub_time > index.pub_time:
                        if doc_data['doc_date'] not in my_row:
                            my_row[doc_data['doc_date']] = i.tombula_count
                        else:
                            my_row[doc_data['doc_date']] += i.tombula_count
                        sums[1] += i.tombula_count
                    else:
                        pass
            for i in sorted(list(my_row.keys())):
                row.append([i, "{:.2f}".format(my_row[i])])
            row.append([u'-' * 20, u'-' * 20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        elif self.m_radioBtn15.GetValue() is True:
            col = [gui_lib.msg.cust_report_TombulaGet_text[3], gui_lib.msg.cust_report_TombulaGet_text[4]]
            sums = [gui_lib.msg.cust_report_TombulaGet_text[5], 0]
            row = []
            my_row = {}
            for i in self.row:
                if i.pub_user_id not in my_row:
                    my_row[i.pub_user_id] = [str(i.pub_user.name), i.tombula_count]
                else:
                    my_row[i.pub_user_id][1] += i.tombula_count
                sums[1] += i.tombula_count
            for i in my_row:
                row.append([my_row[i][0], "{:.2f}".format(my_row[i][1])])
            row.append([u'-' * 20, u'-' * 20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.cust_report_TombulaGet_text['table_name'], row=row, col=col,
                                                                      template_name=template_name, template=template)

class TombulaOnMonyGet(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn15.SetLabel(gui_lib.msg.cust_report_TombulaOnMonyGet_text['m_radioBtn15'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.cust_report_TombulaOnMonyGet_text['m_radioBtn14'])
        self.parent = parent

    def OnGo(self, event):
        self.get_date()
        self.row = []
        self.activ = self.m_radioBtn8.GetValue()
        self.row = libs.DB.get_all_where(libs.models.PointInMonyPrinted, pub_time__btw=(self.start_date, self.end_date),
                                         order='id', descs=True)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.cust_report_TombulaOnMonyGet_text['table_name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        row = []
        col = []
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.cust_report_TombulaOnMonyGet_text[1],
                   gui_lib.msg.cust_report_TombulaOnMonyGet_text[2],
                   gui_lib.msg.cust_report_TombulaOnMonyGet_text[3],
                   gui_lib.msg.cust_report_TombulaOnMonyGet_text[4]]
            sums = [u'', u'', gui_lib.msg.cust_report_TombulaOnMonyGet_text[5], 0]
            row = []
            for i in self.row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                var.append(str(i.cust.name))
                var.append(str(i.pub_user.name))
                var.append("{:.2f}".format(i.point_sum))
                sums[3] += i.point_sum
                row.append(var)

            row.append([u'-' * 20, u'-' * 20, u'-' * 20, u'-' * 20])
            sums[3] = "{:.2f}".format(sums[3])
            row.append(sums)
        elif self.m_radioBtn14.GetValue() is True:
            col = [gui_lib.msg.cust_report_TombulaOnMonyGet_text[2], gui_lib.msg.cust_report_TombulaOnMonyGet_text[4]]
            sums = [gui_lib.msg.cust_report_TombulaOnMonyGet_text[5], 0]
            row = []
            my_row = {}
            for i in self.row:
                if i.cust_id not in my_row:
                    my_row[i.cust_id] = [str(i.cust.name), i.point_sum]
                else:
                    my_row[i.cust_id][1] += i.point_sum
                sums[1] += i.point_sum
            for i in my_row:
                row.append([my_row[i][0], "{:.2f}".format(my_row[i][1])])
            row.append([u'-' * 20, u'-' * 20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        elif self.m_radioBtn7.GetValue() is True:
            col = [gui_lib.msg.cust_report_TombulaOnMonyGet_text[1], gui_lib.msg.cust_report_TombulaOnMonyGet_text[4]]
            sums = [gui_lib.msg.cust_report_TombulaOnMonyGet_text[5], 0]
            my_row = {}
            row = []
            self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
            # self.start_date = self.start_date - datetime.timedelta(minutes=1)
            # self.start_date = libs.DB.get_one_where(libs.models.DayReport, pub_time__lte=libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S'), descs=True)
            self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = libs.models.TZ.str_to_date(self.end_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = self.end_date + datetime.timedelta(days=1)
            # self.end_date = libs.DB.get_one_where(libs.models.DayReport,
            #                                         pub_time__gte=libs.models.TZ.date_to_str(self.end_date,
            #                                                                                 '%Y-%m-%d %H:%M:%S'))
            self.end_date = libs.models.TZ.date_to_str(self.end_date, '%Y-%m-%d %H:%M:%S')
            db_row = libs.DB.get_all_where(libs.models.DayReport, day_report=True,
                                           pub_time__btw=(self.start_date, self.end_date), order='id', descs=False)

            for i in self.row:
                for b in db_row:
                    try:
                        index = db_row[db_row.index(b) - 1]
                    except IndexError:
                        index = b
                    doc_data = json.loads(b.doc_data)
                    if i.pub_time < b.pub_time and i.pub_time > index.pub_time:
                        if doc_data['doc_date'] not in my_row:
                            my_row[doc_data['doc_date']] = i.point_sum
                        else:
                            my_row[doc_data['doc_date']] += i.point_sum
                        sums[1] += i.point_sum
                    else:
                        pass
            for i in sorted(list(my_row.keys())):
                row.append([i, "{:.2f}".format(my_row[i])])
            row.append([u'-' * 20, u'-' * 20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        elif self.m_radioBtn15.GetValue() is True:
            col = [gui_lib.msg.cust_report_TombulaGet_text[3], gui_lib.msg.cust_report_TombulaOnMonyGet_text[4]]
            sums = [gui_lib.msg.cust_report_TombulaGet_text[5], 0]
            row = []
            my_row = {}
            for i in self.row:
                if i.pub_user_id not in my_row:
                    my_row[i.pub_user_id] = [str(i.pub_user.name), i.point_sum]
                else:
                    my_row[i.pub_user_id][1] += i.point_sum
                sums[1] += i.point_sum
            for i in my_row:
                row.append([my_row[i][0], "{:.2f}".format(my_row[i][1])])
            row.append([u'-' * 20, u'-' * 20])
            row.append([sums[0], "{:.2f}".format(sums[1])])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.cust_report_TombulaOnMonyGet_text[
                                                                          'table_name'], row=row, col=col,
                                                                      template_name=template_name, template=template)

class Statistic(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.parent = parent
        self.m_radioBtn8.Hide()
        self.m_radioBtn17.Hide()
        # self.m_radioBtn15.Hide()
        # self.m_radioBtn14.Hide()
        self.m_radioBtn7.SetLabel(gui_lib.msg.cust_report_Statistic_text['m_radioBtn7'])
        self.m_radioBtn7.SetValue(True)
        self.m_radioBtn14.SetLabel(gui_lib.msg.cust_report_Statistic_text['m_radioBtn14'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.cust_report_Statistic_text['m_radioBtn15'])

    def OnGo(self, event):
        self.get_date()
        self.row = []
        self.row = libs.DB.get_all_where(libs.models.CustStatistic, pub_time__btw=(self.start_date, self.end_date), order='id', descs=False)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def table_report(self):
        template = 'veri_big_table.html'
        template_name = gui_lib.msg.cust_report_Statistic_text['table_name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        row = []
        col = []

        if self.m_radioBtn10.GetValue() is True:
            row = []
            col = [gui_lib.msg.cust_report_Statistic_text[1],
                   gui_lib.msg.cust_report_Statistic_text[16],
                   gui_lib.msg.cust_report_Statistic_text[2],
                   gui_lib.msg.cust_report_Statistic_text[3],
                   gui_lib.msg.cust_report_Statistic_text[4],
                   gui_lib.msg.cust_report_Statistic_text[5],
                   gui_lib.msg.cust_report_Statistic_text[6],
                   gui_lib.msg.cust_report_Statistic_text[7],
                   gui_lib.msg.cust_report_Statistic_text[8],
                   gui_lib.msg.cust_report_Statistic_text[9],
                   gui_lib.msg.cust_report_Statistic_text[10],
                   gui_lib.msg.cust_report_Statistic_text[11],
                   gui_lib.msg.cust_report_Statistic_text[13],
                   gui_lib.msg.cust_report_Statistic_text[12]]
            for i in self.row:
                var = []
                var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                if i.come_on_emg_time != None:
                    var.append(libs.models.TZ.date_to_str(i.come_on_emg_time, '%d.%m.%Y %H:%M:%S'))
                else:
                    var.append(u'')
                var.append(str(i.device.nom_in_l))
                var.append(str(i.cust.name))
                if i.cust.use_group_conf is False:
                    var.append(u'')
                else:
                    var.append(str(i.cust.grup.name))

                var.append("{:.2f}".format(i.ins+i.curent_credit_on_in))
                var.append("{:.2f}".format(i.out+i.curent_credit))
                var.append("{:.2f}".format((i.ins+i.curent_credit_on_in) - (i.out+i.curent_credit)))
                var.append("{:.2f}".format(i.bill))
                var.append("{:.2f}".format(i.won))
                var.append("{:.2f}".format(i.bet))
                try:
                    var.append("{:.2f}".format(i.bet/i.game_played))
                except ZeroDivisionError:
                    var.append('0.0')
                var.append("{:.2f}".format(i.curent_credit))
                var.append("{:.2f}".format(i.curent_credit_on_in))
                row.append(var)
        elif self.m_radioBtn7.GetValue() is True:
            row = []
            numer = 1
            sums = [u'', u'', u'', gui_lib.msg.cust_report_Statistic_text[20], 0, 0, 0, 0, 0, 0, 0, u'0']
            col = [gui_lib.msg.cust_report_Statistic_text[15],
                   gui_lib.msg.cust_report_Statistic_text[1],
                   gui_lib.msg.cust_report_Statistic_text[3],
                   gui_lib.msg.cust_report_Statistic_text[4],
                   gui_lib.msg.cust_report_Statistic_text[8],
                   gui_lib.msg.cust_report_Statistic_text[13],
                   gui_lib.msg.cust_report_Statistic_text[12],
                   gui_lib.msg.cust_report_Statistic_text[5],
                   gui_lib.msg.cust_report_Statistic_text[6],
                   gui_lib.msg.cust_report_Statistic_text[7],
                   gui_lib.msg.cust_report_Statistic_text[14],
                   gui_lib.msg.cust_report_Statistic_text[11]]
            sort = {}
            total_bet = {}
            total_gamae = {}
            for i in self.row:
                if i.cust.name not in sort:
                    bonus = libs.DB.get_all_where(libs.models.BonusPay, pub_time__btw=(self.start_date, self.end_date), cust_id=i.cust_id, use_it=True)
                    my_mony = 0
                    for my_bonus in bonus:
                        sums[10] += my_bonus.mony
                        my_mony += my_bonus.mony
                    sort[i.cust.name] = []
                    sort[i.cust.name].append(str(0))
                    # numer += 1
                    sort[i.cust.name].append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
                    sort[i.cust.name].append(str(i.cust.name))
                    if i.cust.use_group_conf is False:
                        sort[i.cust.name].append(u'')
                    else:
                        sort[i.cust.name].append(str(i.cust.grup.name))
                    sort[i.cust.name].append(i.bill)
                    sums[4] += i.bill

                    # sort[i.cust.name].append(i.won)
                    # sort[i.cust.name].append(i.bet)
                    sort[i.cust.name].append(i.curent_credit)
                    sums[5] += i.curent_credit
                    sort[i.cust.name].append(i.curent_credit_on_in)
                    sums[6] += i.curent_credit_on_in
                    sort[i.cust.name].append(i.ins+i.curent_credit_on_in)
                    sums[7] += i.ins+i.curent_credit_on_in
                    sort[i.cust.name].append(i.out+i.curent_credit)
                    sums[8] += i.out+i.curent_credit
                    sort[i.cust.name].append((i.ins+i.curent_credit_on_in) - (i.out+i.curent_credit))
                    sums[9] += (i.ins+i.curent_credit_on_in) - (i.out+i.curent_credit)
                    total_bet[i.cust.name] = i.bet
                    total_gamae[i.cust.name] = i.game_played
                    sort[i.cust.name].append(my_mony)
                else:
                    sort[i.cust.name][4] += i.bill
                    sums[4] += i.bill
                    # sort[i.cust.name][5] += i.won
                    # sort[i.cust.name][6] += i.bet
                    #
                    # sort[i.cust.name][7] += i.curent_credit

                    sort[i.cust.name][5] += i.curent_credit
                    sums[5] += i.curent_credit
                    sort[i.cust.name][6] += i.curent_credit_on_in
                    sums[6] += i.curent_credit_on_in
                    sort[i.cust.name][7] += i.ins+i.curent_credit_on_in
                    sums[7] += i.ins + i.curent_credit_on_in
                    sort[i.cust.name][8] += i.out+i.curent_credit
                    sums[8] += i.out + i.curent_credit
                    sort[i.cust.name][9] += (i.ins+i.curent_credit_on_in) - (i.out+i.curent_credit)
                    sums[9] += (i.ins + i.curent_credit_on_in) - (i.out + i.curent_credit)
                    total_bet[i.cust.name] += i.bet
                    total_gamae[i.cust.name] += i.game_played
            for i in sort:
                try:
                    sort[i].append(total_bet[i]/total_gamae[i])
                except ZeroDivisionError:
                    sort[i].append(0)
            numer = 1
            for i in sorted(list(sort.keys())):
                sort[i][0] = str(numer)
                numer += 1
                sort[i][4] = "{:.2f}".format(sort[i][4])
                sort[i][5] = "{:.2f}".format(sort[i][5])
                sort[i][6] = "{:.2f}".format(sort[i][6])
                sort[i][7] = "{:.2f}".format(sort[i][7])
                sort[i][8] = "{:.2f}".format(sort[i][8])
                sort[i][9] = "{:.2f}".format(sort[i][9])
                sort[i][10] = "{:.2f}".format(sort[i][10])
                sort[i][11] = "{:.2f}".format(sort[i][11])
                # sort[i][11] = "{:.2f}".format(sort[i][11])
                # sort[i][12] = "{:.2f}".format(sort[i][12])
                row.append(sort[i])
            sums[4] = "{:.2f}".format(sums[4])
            sums[5] = "{:.2f}".format(sums[5])
            sums[6] = "{:.2f}".format(sums[6])
            sums[7] = "{:.2f}".format(sums[7])
            sums[8] = "{:.2f}".format(sums[8])
            sums[9] = "{:.2f}".format(sums[9])
            sums[10] = "{:.2f}".format(sums[10])
            # sums[11] = "{:.2f}".format(sums[11])
            row.append([u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5, u'-'*5])
            row.append(sums)
        elif self.m_radioBtn14.GetValue() is True:
            row = []
            col = [gui_lib.msg.cust_report_Statistic_text[2],
                   # gui_lib.msg.cust_report_Statistic_text[17],
                   gui_lib.msg.cust_report_Statistic_text[5],
                   gui_lib.msg.cust_report_Statistic_text[6],
                   gui_lib.msg.cust_report_Statistic_text[7],
                   gui_lib.msg.cust_report_Statistic_text[8],
                   gui_lib.msg.cust_report_Statistic_text[10],
                   gui_lib.msg.cust_report_Statistic_text[9],
                   gui_lib.msg.cust_report_Statistic_text[18],
                   gui_lib.msg.cust_report_Statistic_text[11],
                   gui_lib.msg.cust_report_Statistic_text[14],
                   ]
            my_sum = 0
            my_dict = {}
            for i in self.row:
                if i.cust.id not in my_dict:
                    bonus = libs.DB.get_all_where(libs.models.BonusPay, pub_time__btw=(self.start_date, self.end_date),
                                                  cust_id=i.cust_id, use_it=True)
                    my_mony = 0
                    for my_bonus in bonus:
                        my_mony += my_bonus.mony
                    my_dict[i.cust.id] = [i.cust.name, i.ins, i.out, i.ins - i.out, i.bill, i.bet, i.won, i.game_played, my_mony]
                else:
                    my_dict[i.cust.id][1] += (i.ins+i.curent_credit_on_in)
                    my_dict[i.cust.id][2] += (i.out+i.curent_credit)
                    my_dict[i.cust.id][3] += (i.ins+i.curent_credit_on_in) - (i.out+i.curent_credit)
                    my_dict[i.cust.id][4] += i.bill
                    my_dict[i.cust.id][5] += i.bet
                    my_dict[i.cust.id][6] += i.won
                    my_dict[i.cust.id][7] += i.game_played
            for i in sorted(list(my_dict.keys())):
                try:
                    tmp = [str(my_dict[i][0]),
                           # my_dict[i][1],
                           "{:.2f}".format(my_dict[i][1]),
                           "{:.2f}".format(my_dict[i][2]),
                           "{:.2f}".format(my_dict[i][3]),
                           "{:.2f}".format(my_dict[i][4]),
                           "{:.2f}".format(my_dict[i][5]),
                           "{:.2f}".format(my_dict[i][6]),
                           str(my_dict[i][7]),
                           "{:.2f}".format(my_dict[i][5]/my_dict[i][7]),
                           "{:.2f}".format(my_dict[i][8]),
                           ]
                except ZeroDivisionError:
                    tmp = [str(my_dict[i][0]),
                           # my_dict[i][1],
                           "{:.2f}".format(my_dict[i][1]),
                           "{:.2f}".format(my_dict[i][2]),
                           "{:.2f}".format(my_dict[i][3]),
                           "{:.2f}".format(my_dict[i][4]),
                           "{:.2f}".format(my_dict[i][5]),
                           "{:.2f}".format(my_dict[i][6]),
                           str(my_dict[i][7]),
                           "{:.2f}".format(0),
                           "{:.2f}".format(8)
                           ]
                row.append(tmp)
        elif self.m_radioBtn15.GetValue() is True:
            row = []
            col = [gui_lib.msg.cust_report_Statistic_text[19],
                   gui_lib.msg.cust_report_Statistic_text[5],
                   gui_lib.msg.cust_report_Statistic_text[6],
                   gui_lib.msg.cust_report_Statistic_text[7],
                   gui_lib.msg.cust_report_Statistic_text[8],
                   gui_lib.msg.cust_report_Statistic_text[10],
                   gui_lib.msg.cust_report_Statistic_text[9],
                   gui_lib.msg.cust_report_Statistic_text[18],
                   gui_lib.msg.cust_report_Statistic_text[11],
                   ]
            my_sum = 0
            my_dict = {}
            self.start_date = libs.models.TZ.str_to_date(self.start_date, '%Y-%m-%d %H:%M:%S')
            # self.start_date = self.start_date - datetime.timedelta(minutes=1)
            # self.start_date = libs.DB.get_one_where(libs.models.DayReport, pub_time__lte=libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S'), descs=True)
            self.start_date = libs.models.TZ.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = libs.models.TZ.str_to_date(self.end_date, '%Y-%m-%d %H:%M:%S')
            self.end_date = self.end_date + datetime.timedelta(days=1)
            # self.end_date = libs.DB.get_one_where(libs.models.DayReport,
            #                                         pub_time__gte=libs.models.TZ.date_to_str(self.end_date,
            #                                                                                 '%Y-%m-%d %H:%M:%S'))
            self.end_date = libs.models.TZ.date_to_str(self.end_date, '%Y-%m-%d %H:%M:%S')
            db_row = libs.DB.get_all_where(libs.models.DayReport, day_report=True,
                                           pub_time__btw=(self.start_date, self.end_date), order='id', descs=False)
            for i in self.row:
                for b in db_row:
                    try:
                        index = db_row[db_row.index(b) - 1]
                    except IndexError:
                        index = b
                    doc_data = json.loads(b.doc_data)
                    if i.pub_time < b.pub_time and i.pub_time > index.pub_time:
                        if doc_data['doc_date'] not in my_dict:
                            my_dict[doc_data['doc_date']] = [libs.models.TZ.date_to_str(b.pub_time, '%d.%m.%Y'), (i.ins+i.curent_credit_on_in), (i.out+i.curent_credit), (i.ins+i.curent_credit_on_in) - (i.out+i.curent_credit), i.bill,
                                                    i.bet, i.won, i.game_played]
                        else:
                            my_dict[doc_data['doc_date']][1] += (i.ins+i.curent_credit_on_in)
                            my_dict[doc_data['doc_date']][2] += (i.out+i.curent_credit)
                            my_dict[doc_data['doc_date']][3] += (i.ins+i.curent_credit_on_in) - (i.out+i.curent_credit)
                            my_dict[doc_data['doc_date']][4] += i.bill
                            my_dict[doc_data['doc_date']][5] += i.bet
                            my_dict[doc_data['doc_date']][6] += i.won
                            my_dict[doc_data['doc_date']][7] += i.game_played
                    else:
                        pass

            for i in sorted(list(my_dict.keys())):
                try:
                    tmp = [str(my_dict[i][0]),
                           "{:.2f}".format(my_dict[i][1]),
                           "{:.2f}".format(my_dict[i][2]),
                           "{:.2f}".format(my_dict[i][3]),
                           "{:.2f}".format(my_dict[i][4]),
                           "{:.2f}".format(my_dict[i][5]),
                           "{:.2f}".format(my_dict[i][6]),
                           str(my_dict[i][7]),
                           "{:.2f}".format(my_dict[i][6] / my_dict[i][7])
                           ]
                except ZeroDivisionError:
                    tmp = [str(my_dict[i][0]),
                           "{:.2f}".format(my_dict[i][1]),
                           "{:.2f}".format(my_dict[i][2]),
                           "{:.2f}".format(my_dict[i][3]),
                           "{:.2f}".format(my_dict[i][4]),
                           "{:.2f}".format(my_dict[i][5]),
                           "{:.2f}".format(my_dict[i][6]),
                           str(my_dict[i][7]),
                           "{:.2f}".format(0)
                           ]
                row.append(tmp)
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.cust_report_Statistic_text['table_name'], row=row, col=col,
                                                                      template_name=template_name, template=template)

class InOut(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn9.Hide()
        self.m_radioBtn8.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.cust_report_InOut_text['m_radioBtn10'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.cust_report_InOut_text['m_radioBtn14'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.cust_report_InOut_text['m_radioBtn15'])
        self.parent = parent

    def OnGo(self, event):
        self.row = []
        self.get_date()
        if self.m_radioBtn10.GetValue() is True:
            self.row = libs.DB.get_all_where(libs.models.CustInOutAFT, pub_time__btw=(self.start_date, self.end_date), order='id', descs=True)
        elif self.m_radioBtn14.GetValue() is True:
            self.row = libs.DB.get_all_where(libs.models.CustInOutAFT, pub_time__btw=(self.start_date, self.end_date),
                                             order='id', descs=True, out=False)
        elif self.m_radioBtn15.GetValue() is True:
            self.row = libs.DB.get_all_where(libs.models.CustInOutAFT, pub_time__btw=(self.start_date, self.end_date),
                                             order='id', descs=True, out=True)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.cust_report_InOut_text['table_name'] + u':(%s/%s)' % (self.start_date[:-3], self.end_date[:-3])
        row = []
        sum_in = 0
        sum_out = 0
        col = [gui_lib.msg.cust_report_InOut_text[1],
               gui_lib.msg.cust_report_InOut_text[2],
               gui_lib.msg.cust_report_InOut_text[3],
               gui_lib.msg.cust_report_InOut_text[4],
               gui_lib.msg.cust_report_InOut_text[5],
               gui_lib.msg.cust_report_InOut_text[6],
               gui_lib.msg.cust_report_InOut_text[7],
               gui_lib.msg.cust_report_InOut_text[8]]
        for i in self.row:
            var = []
            var.append(str(i.id))
            var.append(libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'))
            var.append(str(i.device.nom_in_l))
            var.append(str(i.cust.name))
            var.append(str(i.cust.grup.name))
            if i.out is False:
                sum_in += i.mony
                var.append("{:.2f}".format(i.mony))
                var.append('')
            else:
                var.append('')
                sum_out += i.mony
                var.append("{:.2f}".format(i.mony))
            if i.user_id != None:
                var.append(i.user.name)
            else:
                var.append('')
            row.append(var)
        row.append([u'-' * 20, u'-' * 20, u'-' * 20, u'-' * 20, u'-' * 20, u'-' * 20, u'-' * 20, u'-' * 20])
        row.append([u'', u'', u'', u'', gui_lib.msg.cust_report_InOut_text['total'] , "{:.2f}".format(sum_in), "{:.2f}".format(sum_out), u''])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', gui_lib.msg.cust_report_InOut_text['table_name'], row=row,
                                                                      col=col,
                                                                      template_name=template_name, template=template)



class ATM(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn7.SetLabel(gui_lib.msg.report_atm['m_radioBtn7'])
        self.m_radioBtn14.SetLabel(gui_lib.msg.report_atm['m_radioBtn14'])
        self.m_radioBtn15.SetLabel(gui_lib.msg.report_atm['m_radioBtn15'])
        self.parent = parent
        self.m_radioBtn14.SetValue(True)
        # self.m_radioBtn7.Show()
        # self.m_radioBtn15.Hide()

    def OnGo(self, event):
        self.get_date()
        self.row = []
        self.row = libs.DB.get_all_where(libs.models.BankTransfer, pub_time__btw=(self.start_date, self.end_date),
                                         order='id', descs=False)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.report_atm['name'] + u':(%s/%s)' % (
        self.start_date[:-3], self.end_date[:-3])
        col = []
        row = []
        if self.m_radioBtn10.GetValue() is True:
            row = []
            sums = [u'', u'', gui_lib.msg.report_atm[6], 0]

            col = [
                   gui_lib.msg.report_atm[2],
                   gui_lib.msg.report_atm[3],
                   gui_lib.msg.report_atm[4],
                   gui_lib.msg.report_atm[5],]
            my_sum = 0
            for i in self.row:
                var = [
                    libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M:%S'),
                    str(i.user.name),
                    str(i.cust.name),
                    "{:.2f}".format(i.mony)
                ]
                my_sum += i.mony
                row.append(var)
            sums[3] = "{:.2f}".format(my_sum)
            row.append([u'-' * 20, u'-' * 20, u'-' * 20, u'-' * 20])
            row.append(sums)
        elif self.m_radioBtn14.GetValue() is True:
            row = []
            sums = [gui_lib.msg.report_atm[6], 0]

            col = [
                gui_lib.msg.report_atm[3],
                gui_lib.msg.report_atm[5],
                ]
            my_sum = 0
            my_row = {}
            for i in self.row:
                if i.cust.name not in my_row:
                    my_row[i.cust.name] = i.mony
                else:
                    my_row[i.cust.name] += i.mony
                my_sum += i.mony
            for i in list(my_row.keys()):
                tmp = [i, "{:.2f}".format(my_row[i])]
                row.append(tmp)
            sums[1] = "{:.2f}".format(my_sum)
            row.append([ u'-' * 20, u'-' * 20])
            row.append(sums)

        elif self.m_radioBtn7.GetValue() is True:
            row = []
            sums = [gui_lib.msg.report_atm[6], 0]

            col = [
                gui_lib.msg.report_atm[4],
                gui_lib.msg.report_atm[5],
            ]
            my_sum = 0
            my_row = {}
            for i in self.row:
                if i.user.name not in my_row:
                    my_row[i.user.name] = i.mony
                else:
                    my_row[i.user.name] += i.mony
                my_sum += i.mony
            for i in list(my_row.keys()):
                tmp = [i, "{:.2f}".format(my_row[i])]
                row.append(tmp)
            sums[1] = "{:.2f}".format(my_sum)
            row.append([u'-' * 20, u'-' * 20])
            row.append(sums)
        elif self.m_radioBtn15.GetValue()==True:
            row = []
            sums = [gui_lib.msg.report_atm[6], 0]

            col = [
                gui_lib.msg.report_atm[2],
                gui_lib.msg.report_atm[5],
            ]
            my_sum = 0
            my_row = {}
            for i in self.row:
                if libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y') not in my_row:
                    my_row[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')] = i.mony
                else:
                    my_row[libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')] += i.mony
                my_sum += i.mony
            for i in list(my_row.keys()):
                tmp = [i, "{:.2f}".format(my_row[i])]
                row.append(tmp)
            sums[1] = "{:.2f}".format(my_sum)
            row.append([u'-' * 20, u'-' * 20])
            row.append(sums)

        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.report_atm['name'], row=row, col=col,
                                                                      template_name=template_name, template=template)


class CartCount(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn10.SetLabel(gui_lib.msg.report_custCount[1])
        self.m_calendar1.SetToolTip(gui_lib.msg.report_custCount[9])
        self.m_calendar2.SetToolTip(gui_lib.msg.report_custCount[9])
        # self.m_radioBtn14.Hide()
        self.m_radioBtn7.SetLabel(gui_lib.msg.report_custCount[5])
        self.m_radioBtn15.Hide()
        # self.m_radioBtn14.SetLabel(gui_lib.msg.report_atm['m_radioBtn14'])
        # self.m_radioBtn15.SetLabel(gui_lib.msg.report_atm['m_radioBtn15'])
        self.parent = parent

    def OnGo(self, event):
        self.row = libs.DB.get_all(libs.models.CustCart)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.report_custCount['name']
        row = []
        col = []
        if self.m_radioBtn10.GetValue() is True:
            col = [gui_lib.msg.report_custCount[2],
                   gui_lib.msg.report_custCount[3],
                   ]
            tmp = {}
            for i in self.row:
                if i.user_id != None:
                    if i.user_id not in tmp:
                        tmp[i.user_id] = [i.user.name, 1]
                    else:
                        tmp[i.user_id][1] += 1
            all_count = 0
            for i in tmp:
                row.append([tmp[i][0], str(tmp[i][1])])
                all_count += tmp[i][1]
            row.append([u'-'*10, u'-'*10])
            row.append([gui_lib.msg.report_custCount[4], str(all_count)])
        elif self.m_radioBtn7.GetValue() is True:
            col = [
                gui_lib.msg.report_custCount[2],
                gui_lib.msg.report_custCount[7],
                gui_lib.msg.report_custCount[8],
                gui_lib.msg.report_custCount[6],
            ]
            for i in self.row:
                if i.user_id != None:
                    tmp = [i.user.name, i.catr_id, i.pub_user.name, libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y')]
                    row.append(tmp)
        elif self.m_radioBtn14.GetValue() is True:
            col = [gui_lib.msg.report_custCount[8],
                   gui_lib.msg.report_custCount[3],
                   ]
            tmp = {}
            for i in self.row:
                if i.pub_user_id != None:
                    if i.pub_user_id not in tmp:
                        tmp[i.pub_user_id] = [i.pub_user.name, 1]
                    else:
                        tmp[i.pub_user_id][1] += 1
            all_count = 0
            for i in tmp:
                row.append([tmp[i][0], str(tmp[i][1])])
                all_count += tmp[i][1]
            row.append([u'-' * 10, u'-' * 10])
            row.append([gui_lib.msg.report_custCount[4], str(all_count)])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.report_custCount['name'], row=row, col=col,
                                                                      template_name=template_name, template=template)

class MonyBackInUser(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn14.Hide()
        self.m_radioBtn15.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.MonyBackInUser['m_radioBtn10'])
        self.m_radioBtn7.SetLabel(gui_lib.msg.MonyBackInUser['m_radioBtn7'])
        self.m_radioBtn17.Hide()
        self.m_calendar1.Hide()
        self.m_calendar2.Hide()


    def OnGo(self, event):
        if self.m_radioBtn10.GetValue() is True:
            self.row = libs.DB.get_all(libs.models.CustUser, order='total_mony_back', descs=True)
        else:
            self.row = libs.DB.get_all(libs.models.CustUser, order='name', descs=False)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.MonyBackInUser['name']
        row = []
        col = [
            gui_lib.msg.MonyBackInUser[1],
            gui_lib.msg.MonyBackInUser[2],
        ]
        sums = 0
        for i in self.row:
            tmp = [i.name, "{:.2f}".format(i.total_mony_back)]
            row.append(tmp)
            sums += i.total_mony_back
        row.append([u'-' * 10, u'-' * 10])
        row.append([gui_lib.msg.MonyBackInUser[3], "{:.2f}".format(sums)])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.MonyBackInUser['name'], row=row,
                                                                      col=col,
                                                                      template_name=template_name, template=template)

class RKO_Copy(gui.RowSelect):
    def __init__(self, parent):
        self.parent = parent
        gui.RowSelect.__init__(self, parent)
        self.m_radioBox1.Hide()
        self.m_button6.SetLabel(gui_lib.msg.RKO_Copy['m_button6'])
        self.m_listCtrl2.InsertColumn(0, gui_lib.msg.RKO_Copy[1])
        self.m_listCtrl2.InsertColumn(1, gui_lib.msg.RKO_Copy[2])
        self.m_listCtrl2.InsertColumn(2, gui_lib.msg.RKO_Copy[3])
        self.m_listCtrl2.InsertColumn(3, gui_lib.msg.RKO_Copy[4])
        self.m_listCtrl2.InsertColumn(4, gui_lib.msg.RKO_Copy[5])
        self.OrderDict = {}
        self._resize(None)

    def refresh_order(self, start_date, end_date):
        self.m_listCtrl2.DeleteAllItems()
        self._get_order(start_date, end_date)

    def _get_order(self, start_date, end_date):
        data = self.m_radioBox1.GetSelection()
        self.OrderDict = {}
        index = 0
        obj = libs.DB.get_all_where(libs.models.CashOutPrinted, pub_time__btw=(start_date, end_date), order='id')
        for i in obj:
            if i.cust_id != None:
                ID = str(i.id)
                ID = ('0' * (9 - len(ID))) + ID
                self.m_listCtrl2.InsertItem(index, str(ID))
                self.m_listCtrl2.SetItem(index, 1, libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M'))
                self.m_listCtrl2.SetItem(index, 2, str(i.cust.name))
                self.m_listCtrl2.SetItem(index, 3, str(i.pub_user.name))
                self.m_listCtrl2.SetItem(index, 4, str("{:.2f}".format(i.mony)))
                self.OrderDict[index] = i
                index += 1
            # else:
            #     ID = str(i.id)
            #     ID = ('0' * (9 - len(ID))) + ID
            #     self.m_listCtrl2.InsertItem(index, str(ID))
            #     self.m_listCtrl2.SetItem(index, 1, libs.models.TZ.date_to_str(i.pub_time, '%d.%m.%Y %H:%M'))
            #     self.m_listCtrl2.SetItem(index, 2, '')
            #     self.m_listCtrl2.SetItem(index, 3, '')
            #     self.m_listCtrl2.SetItem(index, 4, '')
            #     self.OrderDict[index] = i
            #     index += 1



    def _resize(self, event):
        self.width, self.height = self.parent.GetParent().GetParent().GetParent().GetSize()
        # self.m_calendar1.SetMinSize((-1, self.height * 0.18))
        # self.m_calendar2.SetMinSize((-1, self.height * 0.18))
        self.m_scrolledWindow1.SetSize((self.width*0.6, self.height * 0.4))
        self.m_scrolledWindow1.SetMinSize((self.width * 0.6, self.height * 0.4))
        self.m_listCtrl2.SetMinSize((self.width*0.5, self.height * 0.50))
        self.m_listCtrl2.SetColumnWidth(0, self.width * 0.1)
        self.m_listCtrl2.SetColumnWidth(1, self.width * 0.08)
        self.m_listCtrl2.SetColumnWidth(2, self.width * 0.08)
        self.m_listCtrl2.SetColumnWidth(3, self.width * 0.08)
        self.m_listCtrl2.SetColumnWidth(4, self.width * 0.08)

    def OnClose(self, event):
        self.col = None
        self.Destroy()

    def PrintRKO(self, data):
        template = 'rko.html'
        data['my_copy'] = True
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

    def OnEdit(self, event):
        try:
            item = self.OrderDict[self.m_listCtrl2.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            if libs.conf.POS_PRINTER_USE is True:

                if libs.conf.PRINT_DIRECT_POS is True and libs.conf.DEFAULT_POS_PRINTER == '':
                    dial = wx.MessageDialog(self, *gui_lib.msg.NO_POS_PRINTER)
                    dial.ShowModal()
                    return
                ID = str(item.id)
                ID = ('0' * (9 - len(ID))) + ID
                ID = ID
                # cust_sity = item.cust.persona_sity.name
                if item.cust.persona_sity_id:
                    cust_sity = item.cust.persona_sity.name
                else:
                    cust_sity = ''
                cust_adress = item.cust.personal_addres
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
                mony = str("{:.2f}".format(item.mony))
                egn = item.cust.personal_egn
                cust_name = item.cust.name
                user_id = str(item.pub_user.id)
                dates = libs.models.TZ.date_to_str(item.pub_time, formats='%d.%m.%Y %H:%M:%S')

                rko_data = {'company': company, 'EIK': EIK, 'objects': objects, 'sity': sity,
                            'objects_adress': objects_adress,
                            'name': cust_name, 'egn': egn, 'mony': mony, 'user_id': user_id, 'ID': [ID],
                            'dates': dates,
                            'cust_sity': cust_sity,
                            'cust_adress': cust_adress, 'count': 1, 'ID': [ID]}
                self.PrintRKO(rko_data)
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()

    def OnGo(self, event):
        start_date = self.m_calendar1.GetDate()
        start_date = start_date.Format('%Y-%m-%d')
        # if self.m_radioBox1.GetSelection() < 2:
        start_date = libs.models.TZ.go_up_from_date(libs.models.TZ.str_to_date(start_date, '%Y-%m-%d'), 1)
        start_date = libs.models.TZ.date_to_str(start_date, '%Y-%m-%d')
        # else:
        #     start_date = libs.models.TZ.str_to_date(start_date, '%Y-%m-%d')
        #     start_date = libs.models.TZ.date_to_str(start_date, '%Y-%m-%d')
        #     start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
        #         start_date + ' 00:00:00', start_date + ' 23:59:59'))
        #     if start_times == None:
        #         start_times = ' 09:00:00'
        #     else:
        #         start_times = libs.models.TZ.date_to_str(start_times.pub_time, ' %H:%M:%S')
        #     start_date = start_date + ' ' + start_times

        #         print start_date
        #         start_date = start_date.Format('%Y-%m-%d') + ' 00:00:00'

        end_date = self.m_calendar2.GetDate()
        end_date = end_date.Format('%Y-%m-%d') + ' 23:59:59'
        self.refresh_order(start_date, end_date)

class MonyOnCart(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn10.SetLabel(gui_lib.msg.report_MonyOnCart['name'])
        self.m_calendar1.SetToolTip(gui_lib.msg.report_custCount[9])
        self.m_calendar2.SetToolTip(gui_lib.msg.report_custCount[9])
        self.m_radioBtn14.Hide()
        self.m_radioBtn7.Hide()
        self.m_radioBtn15.Hide()
        self.m_calendar1.Hide()
        self.m_calendar2.Hide()
        # self.m_radioBtn14.SetLabel(gui_lib.msg.report_atm['m_radioBtn14'])
        # self.m_radioBtn15.SetLabel(gui_lib.msg.report_atm['m_radioBtn15'])
        self.parent = parent

    def OnGo(self, event):
        self.row = libs.DB.get_all(libs.models.CustUser)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.report_custCount['name']
        row = []
        col = [gui_lib.msg.report_MonyOnCart[1],
               gui_lib.msg.report_MonyOnCart[2],
               ]
        tmp = {}
        sum = 0
        for i in self.row:
            sum += i.curent_mony
            row.append([i.name, "{:.2f}".format(i.curent_mony)])
        row.append(['-'*20, '-'*20])
        row.append([gui_lib.msg.report_MonyOnCart[3], "{:.2f}".format(sum)])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.report_custCount['name'], row=row,
                                                                      col=col,
                                                                      template_name=template_name, template=template)


class DrawBackInUser(Report):
    def __init__(self, parent):
        Report.__init__(self, parent)
        self.m_radioBtn14.Hide()
        self.m_radioBtn15.Hide()
        self.m_radioBtn10.SetLabel(gui_lib.msg.MonyBackInUser['m_radioBtn10'])
        self.m_radioBtn7.SetLabel(gui_lib.msg.MonyBackInUser['m_radioBtn7'])
        self.m_radioBtn17.Hide()
        self.m_calendar1.Hide()
        self.m_calendar2.Hide()

    def OnGo(self, event):
        if self.m_radioBtn10.GetValue() is True:
            self.row = libs.DB.get_all(libs.models.CustUser, order='total_tombula', descs=True)
        else:
            self.row = libs.DB.get_all(libs.models.CustUser, order='name', descs=False)
        if self.m_radioBtn16.GetValue() is True:
            self.table_report()
        else:
            self.pic_report()

    def pic_report(self):
        pass

    def table_report(self):
        template = 'report.html'
        template_name = gui_lib.msg.report_main_Main_report_name[36]
        row = []
        col = [
            gui_lib.msg.MonyBackInUser[1],
            gui_lib.msg.MonyBackInUser[2],
        ]
        sums = 0
        for i in self.row:
            tmp = [i.name, str(int(i.total_tombula))]
            row.append(tmp)
            sums += i.total_tombula
        row.append([u'-' * 10, u'-' * 10])
        row.append([gui_lib.msg.MonyBackInUser[3], str(int(sums))])
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel',
                                                                      gui_lib.msg.report_main_Main_report_name[36], row=row,
                                                                      col=col,
                                                                      template_name=template_name, template=template)

