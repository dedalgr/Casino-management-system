#-*- coding:utf-8 -*-
'''
Created on 26.03.2017 г.

@author: dedal
'''
from . import _gui
import libs
import wx
# import helps
        
    
class LogSelector(_gui.SelectLog):
    def __init__(self, parent):
        _gui.SelectLog.__init__(self, parent)
        self.parent = parent
        self.SetTitle(_(u'Покажи лог'))
        self.m_staticText53.SetLabel(_(u'От Дата'))
        self.m_staticText54.SetLabel(_(u'До Дата'))

        self.m_button23.SetLabel(_(u'Затвори'))
        self.m_button24.SetLabel(_(u'Изтегли'))
#         self.grup = udp.send('GET_LOG_GRUP')
#         self.m_chises = ['']
#         for i in self.grup:
#             self.m_chises.append(i)
#         self.m_choice4.SetItems(self.m_chises)
#         self.m_choice4.SetSelection(0)
        
    def OnClose(self, event):
        self.Destroy()
    
    def OnGo(self, event):
        self.Hide()
        grup = None
#         grup = self.m_choice4.GetString(self.m_choice4.GetSelection())
        start_date = self.m_calendar5.GetDate()
        start_date = start_date.Format('%Y-%m-%d')
        
        end_date = self.m_calendar6.GetDate()
        end_date = end_date.Format('%Y-%m-%d')
#         try:
#             if grup == '' or grup == None:
#                 dlg = wx.MessageBox(_(u'ГМоля изберете група!'), 'Error', wx.OK | wx.ICON_ERROR)
#                 raise IOError
#             
#         except IOError as e:
#             print(e)
#         else:
        dial = Log(self, from_date=start_date, to_date=end_date)
        dial.ShowModal()
        
    
    
class Log(_gui.AllDial):
    def __init__(self, parent, from_date, to_date):
        self.log = libs.udp.send('GET_LOG', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, from_date=from_date, to_date=to_date)
        _gui.AllDial.__init__(self, parent)
        self.parent = parent
        self.m_richText2.Show()
        
        self.m_button_close.SetLabel(_(u'Затвори'))
        self.m_button_close.Show()
        self.m_button_help.SetLabel(_(u'Помощ'))
        self.m_button_help.Show()
        self.add_tree()
        self.m_treeCtrl2.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnGetInfo)
        self.Fit()
    
    def OnGetInfo(self, event):
        item = event.GetItem()
        parent = self.m_treeCtrl2.GetItemParent(item)
        parent = self.m_treeCtrl2.GetItemText(parent)
#         self.order = self.m_treeCtrl2.GetItemText(parent)
        item = self.m_treeCtrl2.GetItemText(item)
        text = '-'*50 + '\n'
        for i in range(len(self.response[parent][item])):
            text = (text + _(u'Час') + ':' + str(self.response[parent][item][i]['hour']) + '\n'
                    + _(u'Машина') + ': ' + str(self.response[parent][item][i]['mashin'])
                    + '\n' + _(u'Ниво') + ': ' + self.response[parent][item][i]['down'] + '\n'
                    + _(u'Сума') + ': ' + str(round(self.response[parent][item][i]['sum'], 2)) + '\n' + '-' * 50 + '\n')
        self.m_richText2.SetValue(text)
    
    def add_tree(self):
        self.response = self.log
        object = {}
        self.root = self.m_treeCtrl2.AddRoot('log')
        var = []
        for item in self.response:
            object[item] = self.m_treeCtrl2.AppendItem(self.root, item)
            for b in sorted(list(self.response[item].keys())):
                date = self.m_treeCtrl2.AppendItem(object[item], b)

    
    def OnClose(self, event):
#         self.parent.OnClose()
        self.Destroy()
        self.parent.OnClose(event)
        
    def OnHelp( self, event ):
        if libs.conf.DOCS_DEBUG == False:
            frame = libs.helps.Help(r'%s%s/colibri/v%s/jackpot.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE, libs.conf.VERSION))
        else:
            frame = libs.helps.Help('http://127.0.0.1:5000/%s/colibri/v%s/jackpot.html' % (libs.conf.USE_LANGUAGE, libs.conf.VERSION))
