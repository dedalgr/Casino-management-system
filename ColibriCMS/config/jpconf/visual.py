#-*- coding:utf-8 -*-
from . import _gui  # @UnresolvedImport
import libs
import wx
import socket
# import helps

class VisualIP(_gui.AddIP):

    def __init__(self, parent, group, edit=None):
        _gui.AddIP.__init__(self, parent=None)
        self.parent = parent
        self.SetTitle(_(u"Визуализация"))
        self.m_staticText20.SetLabel(_(u"Ново IP"))
        self.m_button1.SetLabel(_(u"Проверка на връзката"))
        self.m_textCtrl12.SetToolTip(_(u"Въведете IP във формат 192.168.1.11"))
        self.group = group
        if edit != None:
            self.m_textCtrl12.SetValue(edit)
        self.edit = edit

    def OnGo( self, event ):
        new_ip = self.m_textCtrl12.GetValue()
        try:
            socket.inet_pton(socket.AF_INET, new_ip)
        except:
            dial = wx.MessageBox(_(u'Невалиден IP адрес!'), 'Error', wx.OK | wx.ICON_ERROR)
            return

        #all_m_ip = self.parent.GetParent().DB['smib'].keys()

        all_d_ip = list(self.parent.GetParent().DB['visual'].keys())
        ip = '192.168.%s.%s'
        reserv_ip = []
        for i in range(1, 11):
            reserv_ip.append(ip % ('0', i))
            reserv_ip.append(ip % ('1', i))
        if new_ip in reserv_ip or new_ip in all_d_ip:
            dlg = wx.MessageBox(_(u'Резервиран IP адрес!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            visual_response = libs.udp.send('VISUAL_ALIFE', visual_ip=new_ip, ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
            if visual_response == True:
                if self.group == None:

                    self.parent.GetParent().DB['visual'][new_ip] = {'group':_(u'Свободни')}

                else:

                    del self.parent.GetParent().DB['visual'][self.edit]

                    self.parent.GetParent().DB['visual'][new_ip]['group'] = self.group
                    grup = self.parent.GetParent().DB['group']

                    grup[self.group]['visual'][new_ip] = new_ip
                    del grup[self.group]['visual'][self.edit]

                    self.parent.GetParent().DB['group'] = grup


                self.Destroy()
            else:
                dlg = wx.MessageBox(_(u'Грешен IP адрес! Или липсва връзка с визуализацията!'), 'Error',
                                    wx.OK | wx.ICON_ERROR)


    def OnClose( self, event ):
        self.Destroy()

class VisualConf(_gui.VisualConf):
    def __init__(self, parent, response, ip):
        _gui.VisualConf.__init__(self, parent)
        self.ip = ip
        self.close = True
        self.parent = parent
        self.SetTitle(_(u'Настройки!'))
        self.m_staticText751.SetLabel(_(u"Шрифт"))
        self.m_button32.SetLabel(_(u"Отказ"))
        self.m_button33.SetLabel(_(u"Запис"))
        self.m_staticText73.SetLabel(_('Име'))
        self.m_staticText74.SetLabel(_('Валута'))
        self.m_spinCtrl22.SetLabel(_('Фон'))
        self.m_checkBox19.SetLabel(_('Олимекс'))
        self.m_checkBox20.SetLabel(_('Активни полета'))
        self.m_checkBox21.SetLabel(_('Събери Рейндж'))
        self.m_textCtrl38.SetValue(response['name'])
        self.m_checkBox22.SetLabel(_('Променлив код'))
        self.m_checkBox23.SetLabel(_('Цветни имена'))
        self.m_button34.SetLabel(_('Авто Ъпдейт'))
        self.m_checkBox22.SetValue(response['jump'])
        if response['mony'] == 'BGN':
            self.m_choice4.SetSelection(0)
        else:
            self.m_choice4.SetSelection(1)
        self.m_spinCtrl22.SetValue(response['background'])
        self.m_checkBox19.SetValue(response['micro'])
        self.m_checkBox20.SetValue(response['activ'])
        self.m_checkBox21.SetValue(response['sum_runner_rnage'])
        self.m_checkBox23.SetValue(response['color_name'])
        self.m_spinCtrl23.SetValue(response['font'])

    def OnClose( self, event ):
        self.Destroy()

    def SVN( self, event ):
        response = libs.udp.send('VISUAL_UPDATE', ip=libs.conf.JPSERVERIP, visual_ip=self.ip,
                                 port=libs.conf.JPSERVERPORT)
        if not response:
            dlg = wx.MessageBox(_(u'Липсва връзка с визуализацията!'), 'Error',
                                wx.OK | wx.ICON_ERROR)
        else:
            dlg = wx.MessageBox(_(u'Влиза в сила след рестарт!'), 'Info',
                                wx.OK | wx.ICON_INFORMATION)

    def OnGo( self, event ):
        self.close = False
        if self.m_choice4.GetSelection() == 0:
            mony = 'BGN'
        else:
            mony = 'EU'

        data = {'name':self.m_textCtrl38.GetValue(),
                'mony':mony,
                'iv_jump':self.m_checkBox22.GetValue(),
                'anime': self.m_spinCtrl22.GetValue(),
                'visual_micro':self.m_checkBox19.GetValue(),
                'field_active':self.m_checkBox20.GetValue(),
                'sum_runner_rnage': self.m_checkBox21.GetValue(),
                'color_name':self.m_checkBox23.GetValue(),
                'font':self.m_spinCtrl23.GetValue(),
                }
        response = libs.udp.send('VISUAL_SET_CONF', ip=libs.conf.JPSERVERIP, visual_ip=self.ip,
                                 port=libs.conf.JPSERVERPORT, **data)
        if not response:
            dlg = wx.MessageBox(_(u'Липсва връзка с визуализацията!'), 'Error',
                                wx.OK | wx.ICON_ERROR)
            return
        else:
            self.Destroy()

class Visual(_gui.AllDial):

    def __init__(self, parent):
        _gui.AllDial.__init__(self, parent)
        self.parent = parent
        self.SetTitle(_(u'Визуализации!'))

        self.m_button_add.SetLabel(_(u"Добави"))
        self.m_button_add.Show()
        self.m_button_add.SetToolTip(_(u"Добавяне на визуализация!"))

        self.m_button_del.SetLabel(_(u'Изтрий'))
        self.m_button_del.Show()
        self.m_button_del.SetToolTip(_(u"Изтриване на визуализация!"))

        self.m_button_help.SetLabel(_(u'Аудио Тест'))
        self.m_button_help.Show()
        self.m_button_help.Bind(wx.EVT_BUTTON, self.test_audio)
        self.m_button_help.SetToolTip(_(u"Проверка на звук!"))

        self.m_button_free_1.SetLabel(_(u'Рестарт'))
        self.m_button_free_1.SetToolTip(_(u"Рестартира визуализацията!"))
        self.m_button_free_1.Bind(wx.EVT_BUTTON, self.OnReboot)
        self.m_button_free_1.Show()

        self.m_button_free_2.SetLabel(_(u'Изгаси екран'))
        self.m_button_free_2.SetToolTip(_(u"Изгася визуализацията!"))
        self.m_button_free_2.Bind(wx.EVT_BUTTON, self.OnKill)
        self.m_button_free_2.Show()

        self.m_button_free_3.SetLabel(_(u'Затвори'))
        self.m_button_free_3.SetToolTip(_(u"Затваряне на текущия прозорец!"))
        self.m_button_free_3.Bind(wx.EVT_BUTTON, self.OnClose)
        self.m_button_free_3.Show()


        self.m_button_close.SetLabel(_(u'Помощ'))
        self.m_button_close.Bind(wx.EVT_BUTTON, self.OnHelp)
        self.m_button_close.Show()
        self.m_button_close.SetToolTip(_(u"Показва помощ за текущото меню"))
        self.m_treeCtrl2.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.ItemMod)
        self.add_tree_item()

        self.Fit()

    def validIP(self, address):
        parts = address.split(".")
        if len(parts) != 4:
            return False
        for item in parts:
            if not 0 <= int(item) <= 255:
                return False
        return True

    def ItemMod( self, event ):
        item = event.GetItem()
        self.select = self.m_treeCtrl2.GetItemText(item)
        select = self.select.split('.')
        for i in select:
            try:
                int(i)
            except:
                return False
        response = libs.udp.send('VISUAL_GET_CONF', ip=libs.conf.JPSERVERIP, visual_ip=self.select,
                                 port=libs.conf.JPSERVERPORT)
        if not response:
            dlg = wx.MessageBox(_(u'Липсва връзка с визуализацията!'), 'Error',
                                wx.OK | wx.ICON_ERROR)
            return
        dial = VisualConf(self,response, self.select)
        dial.ShowModal()
        if dial.close == False:
            dlg = wx.MessageBox(_(u'Влиза в сила след рестарт!'), 'Info',
                                wx.OK | wx.ICON_INFORMATION)


    def OnKill(self, event):
        ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        if self.validIP(ip) != True:
            dlg = wx.MessageBox(_(u'Изберете от списъка'), 'Error',
                                wx.OK | wx.ICON_ERROR)
        else:
            response = libs.udp.send('KILL_VISUAL', ip=libs.conf.JPSERVERIP, visual_ip=ip,
                                     port=libs.conf.JPSERVERPORT)
            if response == True:
                dlg = wx.MessageBox(_(u'Успешно свързване.'), 'Info',
                                    wx.OK | wx.ICON_INFORMATION)
            else:
                dlg = wx.MessageBox(_(u'Грешен IP адрес! Или липсва връзка с визуализацията!'), 'Error',
                                    wx.OK | wx.ICON_ERROR)
    def OnReboot(self, event):
        ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        if self.validIP(ip) != True:
            dlg = wx.MessageBox(_(u'Изберете от списъка'), 'Error',
                                wx.OK | wx.ICON_ERROR)
        else:
            response = libs.udp.send('REBOOT_VISUAL', ip=libs.conf.JPSERVERIP, visual_ip=ip,
                                     port=libs.conf.JPSERVERPORT)
            if response == True:
                dlg = wx.MessageBox(_(u'Успешно свързване.'), 'Info',
                                    wx.OK | wx.ICON_INFORMATION)
            else:
                dlg = wx.MessageBox(_(u'Грешен IP адрес! Или липсва връзка с визуализацията!'), 'Error',
                                    wx.OK | wx.ICON_ERROR)
    def test_audio(self, event):
        ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        if self.validIP(ip) != True:
            dlg = wx.MessageBox(_(u'Изберете от списъка'), 'Error',
                                wx.OK | wx.ICON_ERROR)
        else:
            response = libs.udp.send('VISUAL_AUDIO_TEST', ip=libs.conf.JPSERVERIP, visual_ip=ip, port=libs.conf.JPSERVERPORT)
            if response == True:
                dlg = wx.MessageBox(_(u'Успешно свързване.'), 'Info',
                                    wx.OK | wx.ICON_INFORMATION)
            else:
                dlg = wx.MessageBox(_(u'Грешен IP адрес! Или липсва връзка с визуализацията!'), 'Error',
                                    wx.OK | wx.ICON_ERROR)


    def add_tree_item(self):
        self.root = self.m_treeCtrl2.AddRoot('group')
        self.jp_group = list(self.parent.DB['group'].keys())
        try:
            self.jp_group.insert(0, _(u'Свободни'))
        except IndexError:
            self.jp_group = [_(u'Свободни')]
        object = {}
        for item in self.jp_group:
            object[item] =self.m_treeCtrl2.AppendItem(self.root, item)
        self.visual = list(self.parent.DB['visual'].keys())
        for item in sorted(self.visual):
            visual = self.parent.DB['visual'][item]
            try:
                self.m_treeCtrl2.AppendItem(object[visual['group']], item)
            except KeyError:
                self.m_treeCtrl2.AppendItem(object[_(u'Свободни')], item)
        self.m_treeCtrl2.ExpandAll()


    def tree_refresh(self):
        self.m_treeCtrl2.DeleteAllItems()
        self.add_tree_item()

    def has_one(self, visual):
        data = self.parent.DB['visual']

        group = self.parent.DB['group']

        has_one = False
        for item in group:
            if visual in group[item]['visual']:
                if len(group[item]['visual'])-1 > 0:
                    has_one = True

                else:
                    has_one = False
                    dlg = wx.MessageBox(_(u'Невъзможна операция!') + '\n' +
                                            _(u'Групата ще остане без визуализация!'), 'Error',
                                            wx.OK | wx.ICON_ERROR)
        return has_one

    def OnGetInfo(self, event):
        ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        response = libs.udp.send('VISUAL_ALIFE', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
        if response == True:
            dlg = wx.MessageBox(_(u'Успешно свързване.'), 'Info',
                                wx.OK | wx.ICON_INFORMATION)
        else:
            dlg = wx.MessageBox(_(u'Грешен IP адрес! Или липсва връзка с визуализацията!'), 'Error',
                                wx.OK | wx.ICON_ERROR)
    def OnAdd(self, event):

        frame = VisualIP(self, None)
        frame.ShowModal()
        self.tree_refresh()



    def OnDel(self, event):
        dlg = wx.MessageBox(_(u'Искате ли да изтриете визуализацията') + '\n'
                            + _(u'Промените ще влязат в сила незабавно!'), 'Info',
                            wx.YES_NO | wx.ICON_QUESTION)
        grup = self.parent.DB['group']
        data = self.parent.DB['visual']
        item = self.m_treeCtrl2.GetItemParent(self.m_treeCtrl2.GetSelection())
        item = self.m_treeCtrl2.GetItemText(item)

        if dlg == wx.YES:
            ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
            if self.has_one(ip) == True or item == _(u'Свободни'):

                del self.parent.DB['visual'][ip]
                for item in grup:
                    if ip in grup[item]['visual']:
                        del grup[item]['visual'][ip]
                        
                        self.parent.DB['group'] = grup
            self.tree_refresh()

    def OnClose( self, event ):
        self.DestroyChildren()
        self.Destroy()


    def OnHelp(self, event):
        if libs.conf.DOCS_DEBUG == False:
            frame = libs.helps.Help(r'%s%s/colibri/v%s/jackpot.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE, libs.conf.VERSION))
        else:
            frame = libs.helps.Help('http://127.0.0.1:5000/%s/colibri/v%s/jackpot.html' % (libs.conf.USE_LANGUAGE, libs.conf.VERSION))
