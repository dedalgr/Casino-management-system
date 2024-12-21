# -*- coding:utf-8 -*-
'''
Created on 17.10.2017 г.

@author: dedal
'''

from . import gui
import wx
import wx.aui
from . import user_report
from . import mashin_report
from . import cust_report
from . import jpreport
import gui_lib
import libs
import os
import json
# import matplotlib
# matplotlib.use('WXAgg')
# import matplotlib.backends.backend_wxagg
# import matplotlib.pyplot as plt
import plotly.offline
import plotly.graph_objs as go
import smtplib


class ReportSelect(gui.ReportSelect):
    def __init__(self, parent, **kwargs):
        gui.ReportSelect.__init__(self, parent)
        #         self.width, self.height = wx.GetDisplaySize()
        #         self.Bind( wx.EVT_SIZE, self.on_resize )
        #         self.m_listbook2.Bind(wx.EVT_SIZE, self.on_post_event)
        self.parent = parent
        self.row = [[''], ]
        self.col = []
        self.template = 'report.html'
        self.template_name = ''
        self.page_len = 0
        self.row_len = 0

        for i in sorted(list(kwargs.keys())):
            obj = kwargs[i]['class'](self.m_listbook2)
            self.m_listbook2.AddPage(obj, kwargs[i]['name'])
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.on_resize(None)

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        if event != None:
            for i in self.m_listbook2.GetChildren():
                if type(i) != wx.ListView:
                    wx.PostEvent(i, event)
        self.SetSize((self.width, self.height))
        self.m_listbook2.SetMinSize((-1, self.height * 0.63))
        if event != None:
            event.Skip()
            self.Layout()


class ListPanel(gui.ListPanel):
    def __init__(self, parent, row, col, template, template_name):
        gui.ListPanel.__init__(self, parent)
        self.parent = parent
        self.col = col
        self.row = row
        self.reverse = -1
        if template == 'report.html':
            if os.name == "posix":
                self.row_len = 34
            else:
                self.row_len = 30
        elif template == 'report_big_table.html':
            if os.name == "posix":
                self.row_len = 22
            else:
                self.row_len = 18
        elif template == 'veri_big_table.html':
            if os.name == "posix":
                self.row_len = 24
            else:
                self.row_len = 20
        self.page_len = int(len(self.row) / self.row_len)
        #raise KeyError( len(self.row), row_len)
        if len(self.row) % self.row_len > 0:
            self.page_len = self.page_len + 1

        self.template = template
        self.template_name = template_name
        #         self.width, self.height = wx.GetDisplaySize()

        count = 0
        for i in reversed(self.col):
            self.m_listCtrl1.InsertColumn(0, i)
        #             self.m_listCtrl1.SetColumnWidth(0, self.width * 0.08)
        index = 0

        for i in row:
            self.m_listCtrl1.InsertItem(index, i[0])
            #             del i[0]
            count = 1
            for b in i[1:]:
                self.m_listCtrl1.SetItem(index, count, b)
                count += 1
            index += 1
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.on_resize(None)

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        self.m_listCtrl1.SetMinSize((self.width * 0.95, self.height * 0.63))
        index = 0
        for i in reversed(self.col):
            self.m_listCtrl1.SetColumnWidth(index, wx.LIST_AUTOSIZE)
            index += 1
        if event != None:
            event.Skip()
        self.Layout()

    def OnSort(self, event):
        col = event.GetColumn()
        new_row = []
        sorted_col = []
        # last_row = self.row[-2:]
        # del self.row[-2:]
        if self.reverse != col:
            self.reverse = col
            for i in self.row:
                sorted_col.append(i[col])
            var = []
            var2 = []
            for i in sorted_col:
                try:
                    i.index('.')
                    try:
                        i = float(i)
                        var.append(i)
                    except ValueError:
                        var2.append(i)
                except ValueError:
                    try:
                        i = int(i)
                        var.append(i)
                    except ValueError:
                        var2.append(i)
            if var:
                sorted_col = var
            else:
                sorted_col = var2
            # sorted_col = sorted([int(x) for x in sorted_col])

            sorted_col.sort()
            if var:
                for i in var2:
                    var.append(i)
            var = []
            for i in sorted_col:
                if type(i) == float:
                    var.append("{:.2f}".format(i))
                else:
                    var.append(str(i))

            sorted_col = var
            for i in sorted_col:
                for b in self.row:
                    if i == b[col]:
                        new_row.append(b)
                        del self.row[self.row.index(b)]
                    else:
                        try:
                            if float(i) == float(b[col]):
                                new_row.append(b)
                                del self.row[self.row.index(b)]
                        except ValueError:
                            pass

            self.row = new_row
        else:
            self.row.reverse()
        # for i in last_row:
        #     self.row.append(i)
        self.m_listCtrl1.DeleteAllItems()
        index = 0
        for i in self.row:
            self.m_listCtrl1.InsertItem(index, str(i[0]))
            count = 1
            for b in i[1:]:
                self.m_listCtrl1.SetItem(index, count, str(b))
                count += 1
            index += 1
        self.parent.GetParent().row = self.row
        self.parent.GetParent().col = self.col


class PicPanel():
    def show(self, row, title=u'', y_title='Y Label', x_title='X Label', X=[]):
        self.row = row
        fig = go.Figure()

        # w = 50
        # h = 50
        # d = 70
        # self.plt = plt
        # self.plt.figure(figsize=(w, h), dpi=d)
        # self.plt.title(title)
        if type(self.row) == dict:
            for i in self.row:
                if X == []:
                    fig.add_trace(go.Scatter(x=range(len(self.row[i])), y=self.row[i], name=i,
                                         line=dict(width=2)))
                else:
                    fig.add_trace(go.Scatter(x=X, y=self.row[i], name=i,
                                             line=dict(width=2)))
        elif type(self.row) == list:
            # for i in range(len(self.row)):
            if X == []:
                fig.add_bar(x=range(len(self.row)), y=self.row)
            else:
                fig.add_bar(x=X, y=self.row)
        fig.layout.update(
            # template="plotly_white",
            yaxis=dict(title=y_title),
            xaxis=dict(title=x_title),
            title={
                'text': title,
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})

        plotly.offline.plot(fig)

        #     self.plt.plot(range(len(self.row[i])), self.row[i], '-', label=i)
        # self.plt.legend(loc='best')
        # self.plt.show()

    # def on_resize(self, event):
    #     self.width, self.height = self.parent.GetParent().GetParent().GetSize()
    #     self.m_bitmap1.SetMinSize((self.width*0.95, self.height * 0.68))
    #     if event != None:
    #         event.Skip()
    #         self.Layout()


#     def OnClose(self, event):
#         self.DestroyChildren()
#         self.Destroy()

class Main(gui.MainPanel):
    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.parent.help_name = 'report.html'
        self.user = self.parent.USER
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.report_main_Main_name[1])
        #         self.user = USER  # @UndefinedVariable
        gui.MainPanel.__init__(self, parent)
        # reload(libs.conf)
        #         self.width, self.height = wx.GetDisplaySize()
        #         self.Bind( wx.EVT_SIZE, self.on_resize )
        #         self.SetSize((self.width, self.height*0.95))
        #         if libs.conf.FULSCREEAN is True:
        #             self.SetWindowStyle(wx.STAY_ON_TOP)
        #         if os.name == 'posix':
        #             self.SetSize((self.width, self.height))
        #         else:
        #             self.SetSize((self.width, self.height*0.95))
        #             self.Center()
        #         self.SetSize((self.width, self.height))

        self.page = []
        self.tab = None
        self.pic = PicPanel()
        self.m_auinotebook1.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnTabChanged)
        self.m_auinotebook1.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnTabClose)
        self.row = [['', ], ]
        self.col = ['', ]
        self.page_len = 0
        self.row_len = 0
        self.template = 'report.html'
        self.template_name = ''
        self._set_right()
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.on_resize(None)

    #             self.Center()
    #         if libs.conf.FULSCREEAN is True:
    #             self.SetWindowStyle(wx.STAY_ON_TOP)

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        if event != None:
            for i in self.GetChildren():
                if type(i) == wx.aui.AuiNotebook:
                    for b in i.GetChildren():
                        if type(b) == ReportSelect:
                            wx.PostEvent(b, event)
        self.m_toolBar1.SetMinSize((self.width, -1))
        self.m_auinotebook1.SetMinSize((self.width, self.height))
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height * 0.95))
        if event != None:
            event.Skip()
            self.Layout()

    def OnTabChanged(self, event):
        #         try:
        self.tab = self.page[event.Selection]
        #         print self.tab.row[1]
        self.row = self.tab.row
        self.col = self.tab.col
        self.template = self.tab.template
        self.template_name = self.tab.template_name
        self.page_len = self.tab.page_len
        self.row_len = self.tab.row_len

    #         except wx.Exsept:
    #             pass

    def OnTabClose(self, event):
        del self.page[event.Selection]

    def _set_right(self):
        self.m_toolBar1.ClearTools()
        if self.parent.USER.grup.right != None:
            right = self.parent.USER.grup.from_json()
            if 2 in right['report']:
                self.m_tool2 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.report_main_Main_button['m_tool2'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/system-users.png",
                                                                      wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL,
                                                            gui_lib.msg.report_main_Main_tooltip['m_tool2'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnCustReport, id=self.m_tool2.GetId())

            if 3 in right['report']:
                self.m_tool3 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.report_main_Main_button['m_tool3'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/network-server.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL,
                                                            gui_lib.msg.report_main_Main_tooltip['m_tool3'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnMashinReport, id=self.m_tool3.GetId())

            if 4 in right['report']:
                self.m_tool4 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.report_main_Main_button['m_tool4'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/kopete.png",
                                                                      wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.report_main_Main_tooltip['m_tool4'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnUserReport, id=self.m_tool4.GetId())

            if 5 in right['report']:
                self.m_tool6 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.report_main_Main_button['m_tool6'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Emblem-Money-64.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL,
                                                            gui_lib.msg.report_main_Main_tooltip['m_tool6'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnJackpotReport, id=self.m_tool6.GetId())

            if 6 in right['report']:
                self.m_tool9 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.report_main_Main_button['m_tool9'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-Printer-64.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL,
                                                            gui_lib.msg.report_main_Main_tooltip['m_tool9'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnPrint, id=self.m_tool9.GetId())

            if 7 in right['report']:
                self.m_tool7 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.report_main_Main_button['m_tool7'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-Mail-Forward-64.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL,
                                                            gui_lib.msg.report_main_Main_tooltip['m_tool7'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnSendMail, id=self.m_tool7.GetId())

            if 8 in right['report']:
                self.m_tool8 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.report_main_Main_button['m_tool8'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-X-Office-Spreadsheet-64.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL,
                                                            gui_lib.msg.report_main_Main_tooltip['m_tool8'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnExport, id=self.m_tool8.GetId())

        self.m_auinotebook1.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnTabClose)

        self.m_tool1 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.report_main_Main_button['m_tool1'],
                                                    wx.Bitmap(
                                                        libs.conf.IMG_FOLDER + u"64x64/dialog-error.png",
                                                        wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                    gui_lib.msg.report_main_Main_tooltip['m_tool1'], wx.EmptyString,
                                                    None)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_TOOL, self.OnClose, id=self.m_tool1.GetId())
        self.m_toolBar1.Realize()

    def add_note_page(self, class_name, name, **kwargs):
        obj = eval(class_name)(self.m_auinotebook1, **kwargs)
        self.page.append(obj)
        self.m_auinotebook1.AddPage(self.page[-1], name)

    def OnUserReport(self, event):
        #         print self.m_notebook1.GetPage()
        self.add_note_page('ReportSelect', gui_lib.msg.report_main_Main_report_name[1],
                           r1_bill={'name': gui_lib.msg.report_main_Main_report_name[2],
                                    'class': user_report.BillReport},
                           r2_work_time={'name': gui_lib.msg.report_main_Main_report_name[3],
                                         'class': user_report.Lipsi},
                           r3_boss_get_mony={'name': gui_lib.msg.report_main_Main_report_name[4],
                                             'class': user_report.BosGetMony},
                           r4_prihod={'name': gui_lib.msg.report_main_Main_report_name[5],
                                      'class': user_report.Prigodi},
                           r5_razhod={'name': gui_lib.msg.report_main_Main_report_name[6],
                                      'class': user_report.Razhodi},
                           #                            r6_bill_get_error={'name':u"Грешки при вадене на Бил", 'class':user_report.BillGetError},
                           r6_counter_get_error={'name': gui_lib.msg.report_main_Main_report_name[7],
                                                 'class': user_report.ConterGetError},
                           r7_bonus_mony={'name': gui_lib.msg.report_main_Main_report_name[8],
                                          'class': user_report.BonusCart},
                           r8_in_out={'name': gui_lib.msg.report_main_Main_report_name[9], 'class': user_report.InOut},
                           # r9_current_login={'name':u'Влезли с системата', 'class':cust_report.Logedin}
                           #                            r8_user_order = {'name':u"Касови ордери", 'class':user_report.ConterGetError},

                           r9_user_order={'name': gui_lib.msg.report_main_Main_report_name[26],
                                          'class': user_report.WorkTime},
                           r11_user_transfer={'name': gui_lib.msg.report_main_Main_report_name[29],
                                              'class': user_report.KasaTransfer},
                           r92_user_mony_befor_order={'name': gui_lib.msg.report_main_Main_report_name[35],
                                              'class': user_report.UserMonyBeforOrder},
                           r91_user_mony_opis={'name': gui_lib.msg.order_mony_opis['title'],
                                                      'class': user_report.MonyOpis},
                           r92_egn_cheked={'name': gui_lib.msg.report_main_Main_report_name[38],
                                           'class': user_report.EGNChecked},
                           )

    def OnClose(self, event):
        #         self.m_notebook1.DestroyChildren()
        #         self.DestroyChildren()
        #         self.parent.kasa_refresh()
        self.parent.help_name = 'main.html'
        self.parent.show_panel()
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.report_main_Main_name[2])
        self.Destroy()

    def OnCustReport(self, event):
        self.add_note_page('ReportSelect', gui_lib.msg.report_main_Main_report_name[10],
                           r1_bonus_get={'name': gui_lib.msg.report_main_Main_report_name[11],
                                         'class': cust_report.BonusGet},
                           r2_mony_back_get={'name': gui_lib.msg.report_main_Main_report_name[12],
                                             'class': cust_report.MonyBackGet},
                           r3_tombula_get={'name': gui_lib.msg.report_main_Main_report_name[13],
                                           'class': cust_report.TombulaGet},
                           r4_in_out={'name': gui_lib.msg.report_main_Main_report_name[14], 'class': cust_report.InOut},
                           r5_statistic={'name': gui_lib.msg.report_main_Main_report_name[15],
                                         'class': cust_report.Statistic},
                           r6_atm={'name': gui_lib.msg.report_main_Main_report_name[30],
                                         'class': cust_report.ATM},
                           r7_cart_count={'name': gui_lib.msg.report_main_Main_report_name[32],
                                         'class': cust_report.CartCount},
                           r8_monyback_in_user={'name': gui_lib.msg.report_main_Main_report_name[33],
                                                'class':cust_report.MonyBackInUser},
                           r9_monyback_in_user={'name': gui_lib.msg.report_main_Main_report_name[34],
                                                'class': cust_report.RKO_Copy},
                           r91_mony_on_cart={'name': gui_lib.msg.report_MonyOnCart['name'],
                                                'class': cust_report.MonyOnCart},
                           r92_monyback_in_user={'name': gui_lib.msg.report_main_Main_report_name[36],
                                                'class': cust_report.DrawBackInUser},
                           r93_monyback_in_user={'name': gui_lib.msg.report_main_Main_report_name[37],
                                                 'class': cust_report.TombulaOnMonyGet},
                           )

    def OnMashinReport(self, event):
        self.add_note_page('ReportSelect', gui_lib.msg.report_main_Main_report_name[16],
                           r1_in_out={'name': gui_lib.msg.report_main_Main_report_name[17],
                                      'class': mashin_report.InOutReport},
                           r2_mony_return={'name': gui_lib.msg.report_main_Main_report_name[31],
                                           'class': mashin_report.BillGet},
                           r3_mony_return={'name': gui_lib.msg.report_main_Main_report_name[19],
                                           'class': mashin_report.MonyReturn},
                           r4_curent_state={'name': gui_lib.msg.report_main_Main_report_name[20],
                                            'class': mashin_report.Mehanic},
                           r5_day_order={'name': gui_lib.msg.report_main_Main_report_name[21],
                                         'class': mashin_report.DayOrderShow},
                           r6_day_order={'name': gui_lib.msg.report_main_Main_report_name[22],
                                         'class': mashin_report.InOutInDevice},
                           r7_SMIB_log={'name': gui_lib.msg.report_main_Main_report_name[23],
                                        'class': mashin_report.SMIBLog},
                           r8_fix_log={'name': gui_lib.msg.report_main_Main_report_name[27],
                                       'class': mashin_report.FixLog},
                           r9_fix_log={'name': gui_lib.msg.report_main_Main_report_name[28],
                                       'class': mashin_report.NullDevice},
                           )

    def OnJackpotReport(self, event):
        self.add_note_page('ReportSelect', gui_lib.msg.report_main_Main_report_name[24],
                           r1_in_out={'name': gui_lib.msg.report_main_Main_report_name[25],
                                      'class': jpreport.JPDateSelect})

    #         dial = jpreport.JPDateSelect(self)
    #         dial.ShowModal()
    #         data = dial.data
    #         self.add_note_page('ListPanel', data[0])

    def OnPrint(self, event):

        try:
            data = {'col': self.col, 'row': self.row, 'name': self.template_name, 'page': self.page_len, 'row_len':self.row_len}
            # print self.col, self.row, self.template_name, self.page_len
            # try:
            gui_lib.printer.Print(self, self.template, data)
            # except:
            #    dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_NOT_OK)
            #    dlg.ShowModal()
            # else:
            if libs.conf.PRINT_DIRECT is True:
                dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_OK)
                dlg.ShowModal()
        except Exception as e:
            dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_NOT_OK)
            dlg.ShowModal()
            raise e

    #     def mail(self, msg, to_mail):
    #         # https://www.google.com/settings/security/lesssecureapps
    #
    #         server = smtplib.SMTP('smtp.gmail.com', 587)
    #         server.starttls()
    #         server.login('grigor.kolev@gmail.com', 'Vavilon10')
    #         server.sendmail('grigor.kolev@gmail.com', to_mail, msg)
    #         server.quit()

    def OnSendMail(self, event):
        try:
            data = {'col': self.col, 'row': self.row, 'name': self.template_name, 'page': self.page_len, 'row_len':self.row_len}
            #         gui_lib.printer.Print( self, self.template ,data)
            html = gui_lib.printer.render(self.template, data)
            send_to = self.user.grup.boss_mail
            subject = self.user.grup.subject
            # subject = json.loads(subject.value)[libs.conf.ID]
            send_mail_to = send_to.split(',')
            data = []

            for i in send_mail_to:
                data.append(libs.sendmail.Gmail(html, i, subject))
            # data = libs.sendmail.Gmail(html, libs.conf.CONF.get('MAIL', 'boss', 'str'),
            #                                     libs.conf.CONF.get('MAIL', 'subject', 'str'))
            # print data
            if True in data:
                dlg = wx.MessageDialog(self, *gui_lib.msg.MAIL_SEND)
                dlg.ShowModal()
            else:
                dlg = wx.MessageDialog(self, *gui_lib.msg.MAIL_NOT_SEND)
                dlg.ShowModal()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dlg = wx.MessageDialog(self, *gui_lib.msg.MAIL_NOT_SEND)
            dlg.ShowModal()

    def OnExport(self, event):
        dial = Export(self, self.col, self.row)
        dial.ShowModal()


class Export(gui.Xls, gui_lib.keybords.Keyboard):
    def __init__(self, parent, col, row):
        gui.Xls.__init__(self, parent)
        self.col = col
        self.row = row
        self.SetTitle(gui_lib.msg.report_export['name'])
        self.m_button13.SetLabel(gui_lib.msg.report_export['m_button13'])
        self.m_button14.SetLabel(gui_lib.msg.report_export['m_button14'])
        self.m_textCtrl1.SetToolTip(gui_lib.msg.report_export['m_textCtrl1'])
        self.m_dirPicker1.SetPath('')

        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl1.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose(self, event):
        self.Destroy()

    def OnExport(self, event):
        path = self.m_dirPicker1.GetPath() + '/' + self.m_textCtrl1.GetValue() + '.xlsx'
        table = libs.xls_file.Makexls(filename=path)
        table.head(*self.col)
        for i in self.row:
            table.set_data(*i)
        table.write()
        self.OnClose(event)


if __name__ == '__main__':
    app = wx.App()
    dial = Main(None)
    dial.Show()
    app.MainLoop()
