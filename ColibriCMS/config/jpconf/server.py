#-*- coding:utf-8 -*-
from . import _gui  # @UnresolvedImport
import libs
import time
import wx
import socket
from . import activ  # @UnresolvedImport
# import helps  # @UnresolvedImport @UnusedImport
import datetime
# import conf  # @UnresolvedImport

class Name(_gui.GlobalServer):
    def __init__(self, parent):
        _gui.GlobalServer.__init__(self, parent)
        self.parent = parent
        self.SetTitle(_(u"Глобален Сървър"))
        self.m_staticText20.SetLabel(_(u"IP на сървър"))
        self.m_button1.SetLabel(_(u"Запис"))
        self.m_textCtrl12.SetToolTip(_(u"IP на глобалния сървър!"))
        self.m_staticText201.SetLabel(_(u'Име на казино'))
        self.m_textCtrl121.SetToolTip(_(u"Свободен текст. Показва се на визуализация!"))
        self.m_button32.SetLabel(_(u'Затвори'))
        try:
            self.m_textCtrl12.SetValue(self.parent.GetParent().DB['casino_name']['ip'])
        except:
            self.parent.GetParent().DB['casino_name']['ip'] = ''
            self.m_textCtrl12.SetValue(self.parent.GetParent().DB['casino_name']['ip'])
        try:
            self.m_textCtrl121.SetValue(self.parent.GetParent().DB['casino_name']['name'])
        except:
            self.parent.GetParent().DB['casino_name']['name'] = ''
            self.m_textCtrl121.SetValue(self.parent.GetParent().DB['casino_name']['name'])

    # Handlers for AddIP events.
    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        ip = self.m_textCtrl12.GetValue()
        if ip:
            try:
                socket.inet_pton(socket.AF_INET, ip)
            except:
                dial = wx.MessageBox(_(u'Невалиден IP адрес!'), 'Error', wx.OK | wx.ICON_ERROR)
                return
        name = self.m_textCtrl121.GetValue()
        # libs.udp.send('SET_NAME', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, name=name)  # @UndefinedVariable
        self.parent.GetParent().DB['casino_name'] = {'name':name, 'ip':ip}
        self.Destroy()
        
# class SelectLanguage(_gui.AddIP):
#     def __init__(self, parent):
#         self.parent = parent
#         self.all_lang = conf.CONF.get('language')
#         for i in self.all_lang:
#             self.all_lang[i] = self.all_lang[i].decode('utf-8')
# #         self.all_lang = all_lang
#         _gui.AddIP.__init__(self, parent)
#         self.SetTitle('Language!')
#         self.m_staticText20.Hide()
#         self.m_textCtrl12.Hide()
#         self.m_choice2.Show()
#         self.m_button1.SetLabel('Save')
#         var = []
#         del self.all_lang['use_language']
#         for i in self.all_lang:
#             var.append(self.all_lang[i])
#         self.m_choice1Choices = var
#         self.m_choice2.SetItems(self.m_choice1Choices)
#         self.m_choice2.SetSelection(0)
#         self.Layout()
#     
#     def OnClose(self, parent):
#         self.Destroy()
#         
#     def OnGo(self, event):
#         select = self.m_choice2.GetSelection()
#         select = self.m_choice1Choices[select]
#         for i in self.all_lang:
#             if select == self.all_lang[i]:
#                 lang = i
#         try:
#             conf.CONF.add_option('language', use_language='bg')  # @UndefinedVariable
#         except conf.ConfWarning:
#             conf.CONF.update_option('language', use_language=lang)  # @UndefinedVariable
#         wx.MessageBox(u'Reboot System!', 'Error', wx.OK | wx.ICON_ERROR)
#         self.Destroy()
        
class DateTime(_gui.DateTime): 
    def __init__(self, parent):
        self.parent = parent
        _gui.DateTime.__init__(self, parent) 
        self.m_staticText45.SetLabel(_(u'Час'))
        import datetime
        local_date=libs.models.TZ.now()
        self.m_spinCtrl2.SetValue(local_date.hour)
        self.m_spinCtrl1.SetValue(local_date.minute)
        
    def OnClose(self, event):
        self.Destroy()
    
    def OnGo(self, event):
        date = self.m_calendar2.GetDate()
        date = '%s-%s-%s' % (date.Year, date.Month, date.Day)
        time = '%s:%s:00' % (self.m_spinCtrl2.GetValue(), self.m_spinCtrl1.GetValue())
        libs.udp.send('SET_DATE_TIME', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, dates=date, times=time)
        self.Destroy()

class Server(_gui.AllDial):

    def __init__(self, parent):
        _gui.AllDial.__init__(self, parent)
        self.parent = parent
        self.m_treeCtrl2.Hide()
        self.m_richText2.Show()
        
        self.m_button_del.SetLabel(_(u'CRC'))
        self.m_button_del.Show()
        self.m_button_del.SetToolTip(_(u"Проверка на CRC!"))
        
        self.m_button_free_2.SetLabel(_(u'Помощ'))
        self.m_button_free_2.Show()
        self.m_button_free_2.SetToolTip(_(u"Изваждане на помощ за текущия прозорец !"))
        
        self.m_button_show.SetLabel(_(u'Глобален'))
        self.m_button_show.Show()
         
        self.m_button_add.SetLabel(_(u'Активирай'))
        self.m_button_add.Show()
        self.m_button_add.SetToolTip(_(u"Активация на програмата!"))

        self.m_button_free_3.SetLabel(_(u'Отчисляващ'))
        self.m_button_free_3.Show()
        self.m_button_free_3.SetToolTip(_(u"Проверява дали сървъра върти и отчислява!"))
        
        self.m_button_free_4.SetLabel(_(u'Затвори'))
        self.m_button_free_4.Show()
        self.m_button_free_4.SetToolTip(_(u"Затваряне на текущия прозорец!"))
        
#         self.m_button_free_1.SetLabel(u'language')
#         self.m_button_free_1.Show()
#         self.m_button_free_1.SetToolTip(u'change language')
        
        
        response = libs.udp.send('WHO', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
        text = _(u'Информация за сървъра!') + '\n\n'
        text = text + _(u'Сериен номер:') + '\n' + response['soft_uuid'] + '\n'
        text = text + _(u'Версия:') + response['version'][:-2] + '\n'
        init_time = time.gmtime(response['init_time'])
        init_time = u'%s-%s-%s %s:%s' % (init_time.tm_mday, 
                                         init_time.tm_mon, 
                                         init_time.tm_year,
                                         init_time.tm_hour,
                                         init_time.tm_min
                                         )
        text = text + _(u'Инициализация: ') + init_time + '\n'
        response = libs.udp.send('GET_WORK', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
        if response['work_to'] != None:
            
            work_to = datetime.datetime.fromtimestamp(response['work_to'])
            work_to = u'%s-%s-%s' % (work_to.day, 
                                         work_to.month, 
                                         work_to.year,
                                         )
            text = text + _(u'Активиран до: ') + work_to + '\n'
        else:
            text = text + _(u'Активиран до: ') + _(u'Без лимит') + '\n'
        try:
            text = text + _(u'Глобален сървър: ') + self.GetParent().DB['casino_name']['ip'] + '\n'
        except KeyError:
            text = text + _(u'Глобален сървър: ') + '' + '\n'
        try:
            text = text + _(u'Име за глобален сървър: ') + self.GetParent().DB['casino_name']['name'] + '\n'
        except KeyError:
            text = text + _(u'Име за глобален сървър: ') + '' + '\n'
        self.m_richText2.SetValue(text)
        
        self.m_button_add.Bind( wx.EVT_BUTTON, self.OnActiv )
        self.m_button_del.Bind( wx.EVT_BUTTON, self.OnCRC )
        self.m_button_show.Bind( wx.EVT_BUTTON, self.OnAddName)
        self.m_button_free_4.Bind( wx.EVT_BUTTON, self.OnClose)
        self.m_button_free_2.Bind( wx.EVT_BUTTON, self.OnHelp)
        self.m_button_free_3.Bind(wx.EVT_BUTTON, self.OnChkRotation)
#         self.m_button_free_1.Bind(wx.EVT_BUTTON, self.Language)
        self.Fit()

    def OnAddName(self, event):
        frame = Name(self)
        frame.ShowModal()

    def OnChkRotation(self, event):
        response = libs.udp.send('CHK_STOP_ROTATION_STATUS', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
        # print response
        if response == False:
            wx.MessageBox(_(u'Сървърът отчислява!'), 'Info',  wx.OK | wx.ICON_INFORMATION)
        elif response == True:
            wx.MessageBox(_(u'Сървърът не отчислява!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox(_(u'Няма връзка или липсва информация!'), 'Error', wx.OK | wx.ICON_ERROR)

    # def OnDate(self, event):
    #     frame = DateTime(self)
    #     frame.ShowModal()

    def OnHelp(self, event):
        if libs.conf.DOCS_DEBUG == False:
            frame = libs.helps.Help(r'%s%s/colibri/v%s/jackpot.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE, libs.conf.VERSION))
        else:
            frame = libs.helps.Help('http://127.0.0.1:5000/%s/colibri/v%s/jackpot.html' % (libs.conf.USE_LANGUAGE, libs.conf.VERSION))
    
    def OnCRC(self, event):
        response = libs.udp.send('CHK_CRC', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
        if response == True:
            crc_response = libs.udp.send('GET_CRC', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
            crc_response = hex(crc_response)[2:].upper()
            crc_response = crc_response.replace('L', '')
            text = _(u"Текущо CRC на софтуера") + u': ' + crc_response + '\n'
            text = text + _(u'CRC Отговаря на софтуерната версия!')
            wx.MessageBox(text, 'Info',
                                    wx.OK | wx.ICON_INFORMATION)
        else:
            response = libs.udp.send('GET_REAL_CRC', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
            response = hex(response)[2:].upper()
            response = response.replace('L', '')
            text = _(u"Текущо CRC на софтуера") + u': ' + response + '\n'
            text = text + _(u'Внимание грешна CRC стойност!')
            wx.MessageBox(text, 'Error', wx.OK | wx.ICON_ERROR)
        
    
    def OnActiv(self, event):
        frame = activ.Activ(self)
        response = libs.udp.send('BASE_KEY', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, err=4)
        frame.m_textCtrl1.SetValue(response)
        frame.m_textCtrl2.SetToolTip(_(u"Въведете код за активация!"))
        frame.ShowModal()
    
    def OnClose( self, event ):
        self.Destroy()
        
