#-*- coding:utf-8 -*-
'''
Created on 15.11.2018 г.

@author: dedal
'''
from . import gui
import wx
import wx.aui
import gui_lib  # @UnresolvedImport
import libs  # @UnresolvedImport
import datetime

class JPDateSelect(gui.JPDateSelect):
    def __init__(self, parent):
        gui.JPDateSelect.__init__(self, parent)
        self.parent = parent
        self.m_staticText6.SetLabel(gui_lib.msg.cust_report_JPDateSelect_text['m_staticText6'])
        self.m_staticText7.SetLabel(gui_lib.msg.cust_report_JPDateSelect_text['m_staticText7'])
        self.m_button11.SetLabel(gui_lib.msg.cust_report_JPDateSelect_text['m_button11'])

    
    def OnClose(self, event):
        self.Destroy()
        
    def OnGo(self, event):
        start_date = self.m_calendar7.GetDate()
        start_date = start_date.Format('%Y-%m-%d')
        
        end_date = self.m_calendar8.GetDate()
        end_date = end_date.Format('%Y-%m-%d')
        
        self.data = libs.udp.send(ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, evt='GET_LOG', from_date=start_date, to_date=end_date)

        start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(
            start_date + ' 00:00:00', start_date + ' 23:59:59'))
        if start_times == None:
            start_times = ' 09:00:00'
        else:
            start_times = libs.models.TZ.date_to_str(start_times.pub_time, '%H:%M:%S')

        end_times = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
                                          pub_time__btw=(end_date + ' 00:00:00', end_date + ' 23:59:59'))
        if end_times == None:
            end_times = libs.models.TZ.now()
            end_times = libs.models.TZ.date_to_str(end_times, '%H:%M:%S')
        else:
            end_times = libs.models.TZ.date_to_str(end_times.pub_time, '%H:%M:%S')

        # print self.data.keys()
        template = 'report.html'
        template_name = gui_lib.msg.cust_report_JPDateSelect_text['table_name'] + u': (%s/%s)' % (start_date, end_date)
        col = [gui_lib.msg.cust_report_JPDateSelect_text[1],
               gui_lib.msg.cust_report_JPDateSelect_text[2],
               gui_lib.msg.cust_report_JPDateSelect_text[3],
               gui_lib.msg.cust_report_JPDateSelect_text[4],
               gui_lib.msg.cust_report_JPDateSelect_text[5],
               gui_lib.msg.cust_report_JPDateSelect_text[6]]
        row = []
        sums = [u'', u'', u'', u'', gui_lib.msg.cust_report_JPDateSelect_text[7], 0]
        for i in self.data:
            for b in self.data[i]:
#                 print self.data[i][b]
                for c in range(len(self.data[i][b])):
                    # print i, b, self.data[i][b][c]['hour'], start_times
                    if b == start_date and self.data[i][b][c]['hour'] < start_times:
                        pass
                    elif b == end_date and self.data[i][b][c]['hour'] > end_times:
                        pass
                    else:
                        sums[5] += round(self.data[i][b][c]['sum'],2)
                        var = [str(i),
                               str(self.data[i][b][c]['hour']),
                               str(self.data[i][b][c]['mashin']),
                               str(b),
                               str(self.data[i][b][c]['down']),
                               str(round(self.data[i][b][c]['sum'],2)),
                               ]
                        row.append(var)
        row.append([u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10, u'-'*10])
        sums[5] = str(sums[5])
        row.append(sums)
#         self.data = [template_name, row, col, template_name, template]
#         self.Destroy()
        self.parent.GetParent().GetParent().GetParent().add_note_page('ListPanel', template_name, row=row, col=col, template_name=template_name, template=template)
#                     var.append(b)
#         self.Destroy()
        