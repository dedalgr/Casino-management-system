#-*- coding:utf-8 -*-

import wx
from . import _gui  # @UnresolvedImport
import libs  # @UnresolvedImport
import socket
# import helps  # @UnresolvedImport @UnusedImport

        
        
# Implementing AddIP
class AddIP(_gui.AddIP):
    def __init__(self, parent):
        _gui.AddIP.__init__(self, parent)
        self.parent = parent
        self.SetTitle(_(u"Ново IP"))
        self.m_staticText20.SetLabel(_(u"IP на SMIB модула"))
        self.m_button1.SetLabel(_(u"Проверка на връзката"))
        self.m_textCtrl12.SetToolTip(_(u"Въведете IP във формат 192.168.1.11"))

    # Handlers for AddIP events.
    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        new_ip = self.m_textCtrl12.GetValue()
        try:
            socket.inet_pton(socket.AF_INET, new_ip)
        except:
            dial = wx.MessageBox(_(u'Невалиден IP адрес!'), 'Error', wx.OK | wx.ICON_ERROR)
            return
        all_m_ip = list(self.parent.GetParent().DB['smib'].keys())
#         all_m_ip = tcp.send('ALL_MASHIN')
#         all_d_ip = tcp.send('ALL_VISUAL')
#         all_d_ip = self.parent.GetParent().DB['visual'].keys()
        ip = '192.168.%s.%s'
        reserv_ip = []
        for i in range(1, 8):
            reserv_ip.append(ip % ('0', i))
            reserv_ip.append(ip % ('1', i))
        if new_ip in reserv_ip or new_ip in all_m_ip:
            wx.MessageBox(_(u'Резервиран IP адрес!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            self.smib = libs.udp.send('SMIB_WHO', new_ip=new_ip, ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
            if self.smib is None:
                wx.MessageBox(_(u'Грешен IP адрес! Или липсва връзка с машината!'), 'Error', wx.OK | wx.ICON_ERROR)
                return
            response = libs.udp.send('EBABLE_JP_MOD', new_ip=new_ip, ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT )    
            self.smib['ip'] = new_ip
            if not self.smib or not response or self.smib == True:
                wx.MessageBox(_(u'Грешен IP адрес! Или липсва връзка с машината!'), 'Error', wx.OK | wx.ICON_ERROR)
                self.smib = None
            else:
                self.Destroy()


class SetPr(_gui.AddIP):
    def __init__(self, parent, ip):
        _gui.AddIP.__init__(self, parent)
        self.parent = parent
        self.SetTitle(_(u"Процент"))
        self.m_staticText20.SetLabel(_(u"Процент"))
        self.m_button1.SetLabel(_(u"Запис на процент"))
        self.m_textCtrl12.SetToolTip(_(u"Въведете > 0 или <= 1"))
        self.m_textCtrl12.SetValue('1')
        self.ip = ip

    # Handlers for AddIP events.
    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        pr = self.m_textCtrl12.GetValue()
        pr = pr.replace(',', '.')
        try:
            pr = float(pr)
        except:
            wx.MessageBox(_(u'Невалидна стойност!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            if pr <= 0 or pr > 1:
                wx.MessageBox(_(u'Невалидна стойност!'), 'Error', wx.OK | wx.ICON_ERROR)
            else:
                response = libs.udp.send('CHANGE_PR', new_ip=self.ip, pr=pr, ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
                if response == False or response == None:
                    wx.MessageBox(_(u'Неуспешна операция!'), 'Error', wx.OK | wx.ICON_ERROR)
                else:
                    wx.MessageBox(_(u'Успешна операция!'), 'Error', wx.OK | wx.ICON_INFORMATION)
                    self.Destroy() 
# Implementing AddSMIB
class AddSMIB(_gui.AddSMIB):
    def __init__(self, parent, smib):
        _gui.AddSMIB.__init__(self, parent)
        self.parent = parent
        self.smib = smib
        self.SetTitle(_(u'Добавяне на нова машина'))


        self.m_staticText26.SetLabel(u"IP: " + smib['ip'])
        self.m_staticText27.SetLabel(u"SN: " + smib['hw_id'])
        self.m_staticText28.SetLabel(_(u'Версия: ') + smib['version'])

        self.m_radioBtn1.SetLabel(_(u'SAS Протокол'))
        self.m_radioBtn1.SetValue(True)

        self.m_radioBtn2.SetLabel(_(u'Механични броячи'))
        self.m_radioBtn2.SetValue(False)

        self.m_staticText35.SetLabel(_(u'Номер в зала'))

        self.m_staticText33.SetLabel(_(u'Модел на машина'))

        self.m_staticText34.SetLabel(_(u"Сериен номер"))
        self.Fit()

    # Handlers for AddSMIB events.
    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        # tcp.send('ENABLE_EVENT', ip=self.smib['ip'])
        self.smib['mashin_sn'] = self.m_textCtrl23.GetValue()
        self.smib['licenz'] = self.m_textCtrl21.GetValue()
        try:
            int(self.smib['licenz'])
        except ValueError:
            wx.MessageBox(_(u'Невалидна стойност!'), 'Error', wx.OK | wx.ICON_ERROR)
            return
        self.smib['model'] = self.m_textCtrl22.GetValue()
        self.smib['sas'] = self.m_radioBtn1.GetValue()
        self.smib['group'] = []
#         self.smib['procent'] = 0.00

        if self.smib['mashin_sn'] == u'' or self.smib['licenz'] == u"" or self.smib['model'] == u'':
            wx.MessageBox(_(u'Всички полета са задължителни!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
#             tcp.send('ADD_MSHIN', **self.smib)
            self.parent.GetParent().DB['smib'][self.smib['ip']] = self.smib
#             dlg = wx.MessageBox(_(u'Рестартирайте SMIB модула!'), 'Info', wx.OK | wx.ICON_ERROR)
#             tcp.send('EBABLE_JP_MOD', ip=self.smib['ip'])
            #tcp.send('REBOOT', ip=self.smib['ip'])
            self.Destroy()

class EditSMIB(AddSMIB):
    def __init__(self, parent, smib):
        AddSMIB.__init__(self, parent, smib)
        self.parent = parent
        self.m_textCtrl23.SetValue(smib['mashin_sn'])
        self.m_textCtrl21.SetValue(smib['licenz'])
        self.m_textCtrl22.SetValue(smib['model'])
        if smib['sas'] == True:
            self.m_radioBtn1.SetValue(True)
        else:
            self.m_radioBtn1.SetValue(False)
            self.m_radioBtn2.SetValue(True)

# Implementing AllDial
class SMIB(_gui.AllDial):
    def __init__(self, parent):
        _gui.AllDial.__init__(self, parent)
        self.parent = parent
        self.SetTitle(_(u'Машини'))

        self.m_button_add.SetLabel(_(u'Добави'))
        self.m_button_add.Show()

        self.m_button_edit.SetLabel(_(u'Редакция'))
        self.m_button_edit.Show()

        self.m_button_del.SetLabel(_(u'Изтрий'))
        self.m_button_del.Show()

        self.m_button_help.SetLabel(_(u'Помощ'))
        self.m_button_help.Show()

        self.m_button_free_3.SetLabel(_(u'Затвори'))
        self.m_button_free_3.Show()
        
        self.m_button_free_1.SetLabel(_(u'Процент'))
        self.m_button_free_1.Show()
        
        self.m_button_free_2.SetLabel(_(u'Изключи Игра'))
        self.m_button_free_2.Show()
        
        self.add_tree_item()
        self.m_richText2.Show()
        self.m_richText2.SetValue(_(u'Кликнете два пъти върху машината \nза да видите информация за нея')+"\n\n")
        
        self.m_treeCtrl2.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnGetInfo)
        self.m_treeCtrl2.Bind( wx.EVT_TREE_SEL_CHANGED, self.OnGetMachin )
        self.m_button_free_3.Bind( wx.EVT_BUTTON, self.OnClose)
        self.m_button_free_2.Bind( wx.EVT_BUTTON, self.DisableGame)
        self.m_button_free_1.Bind(wx.EVT_BUTTON, self.OnProcentChange)
        self.Fit()
    
    def OnProcentChange(self, event):
        ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        ip = self.parent.DB['smib'][ip]['ip']
        dial = SetPr(self, ip)
        dial.ShowModal()
    
    def add_tree_item(self):
        self.mashin = self.m_treeCtrl2.AddRoot(_(u'Машини'))
        self.response = list(self.parent.DB['smib'].keys())
        for item in sorted(self.response):
            self.m_treeCtrl2.AppendItem(self.mashin, item.encode('utf-8'))
        self.m_treeCtrl2.ExpandAll()

    def refresh_tree(self):
        self.m_treeCtrl2.DeleteAllItems()
        self.add_tree_item()

    def OnClose(self, event):
        self.DestroyChildren()
        self.Destroy()

    def OnAdd(self, event):
        frame = AddIP(self)
        frame.ShowModal()
        try:
            smib = frame.smib
            if smib != None:
                frame = AddSMIB(self, smib)
                frame.ShowModal()
                self.refresh_tree()
        except AttributeError:
            pass
        except TypeError:
            pass

    def OnGetInfo(self, event):
        ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        ip = self.parent.DB['smib'][ip]
        grup = self.parent.DB['group']
        try:
            ip['hw_id']
        except:
            ip['hw_id'] = ip['hw_uuid']
            del ip['hw_uuid']
        head = _(u'Информация за машина: ') + ip['ip'] + '\n\n'
        licenz = _(u'Номер в зала: ') + ip['licenz'] + '\n'
        mashin_sn = _(u'Сериен номер на машина: ') + ip['mashin_sn'] + "\n"
        model = _(u'Модел: ') + ip['model'] + "\n"
        smib_sn = _(u'SMIB: ') + ip['hw_id'] + "\n"
        smib_v =  _(u'Версия на SMIB: ') + ip['version'] + "\n"
        if ip['sas'] == True:
            sas = _(u"SAS Протокол: Наличен") + '\n'
        else:
            sas = _(u"SAS Протокол: Липсва") + '\n'
        var = 0 
        for i in ip['group']:
            for b in grup[i]['level']:
                var = var + grup[i]['level'][b]['hiden'] + grup[i]['level'][b]['procent']
                
        procent = _(u"Процент на отчисление: ")  + str(var/0.01) + '\n' + '\t' + _(u'Групи: ') + '\n'
        for i in ip['group']:
            var = 0 
            for b in grup[i]['level']:
                var = var + grup[i]['level'][b]['hiden'] + grup[i]['level'][b]['procent']
                 
            procent = procent + '\t\t' + i + '= '+ str(var/0.01) + ' %\n'

        response = libs.udp.send('SMIB_WHO', new_ip=ip['ip'], ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
        if response == None:
            status = _(u'Статус: Няма връзка с машината') + '\n'
            br = _(u'Броячи:') + '\n' + _(u'Липсва информация!')
            text = status + br
        else:
            status = _(u'Статус: OK') + '\n'
            br = libs.udp.send('GET_MULTI_METER', new_ip=ip['ip'], ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
            if br == None:
                text = _(u'Моля опитайте отново. Машината зарежда!')
            if br == False:
                text = _(u'Моля опитайте отново. Машината зарежда!')
            else:
                var = _(u'Броячи:') + '\n'
                ins = _(u'Вход: ') + str(br['in']) + '\n'
                out = _(u'Изход: ') + str(br['out']) + '\n'
                total = _(u'Тотал: ') + str(br['in']-br['out']) + '\n'
                won = _(u'Печалба в игра: ') + str(br['won']) + '\n'
                bet = _(u'Залог: ') + str(br['bet']) + '\n'
                games_played = _(u'Изиграни игри: ') + str(br['games played']) + '\n'

                br = var + '\t' + ins + '\t' + out + '\t' + total +'\t' + won + '\t' + bet + '\t' + \
                     games_played +'\t'
                text = head + licenz + mashin_sn + model + smib_sn + smib_v + sas + status + procent + br
        self.m_richText2.SetValue(text)

    def OnEdit(self, event):
        ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())

        ip = self.parent.DB['smib'][ip]
        frame = EditSMIB(self, ip)
        frame.ShowModal()

    def OnDel(self, event):
        dlg = wx.MessageBox(_(u'Искате ли да изтриете машината') + '\n'
                            + _(u'Промените ще влязат в сила незабавно!'), 'Info',
                            wx.YES_NO | wx.ICON_QUESTION)
        
        if dlg == wx.YES:

            all_grup = self.parent.DB['group']
            ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
            response = libs.udp.send('DISABLE_JP_MOD', new_ip=ip, ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
            if not response:
                dlg = wx.MessageBox(_(u'Грешен IP адрес! Или липсва връзка с машината!'), 'Error', wx.OK | wx.ICON_ERROR)
  
            for i in all_grup:
                try:
                    del all_grup[i]['mashin'][ip]
                except KeyError:
                    pass

            try:
                del self.parent.DB['smib'][ip]
            except KeyError:
                wx.MessageBox(_(u'Моля изберете машина'),'Info', wx.OK | wx.ICON_ERROR)

            self.parent.DB['grup'] = all_grup
            self.refresh_tree()
    
    def OnGetMachin(self, event):
        ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        ip = self.parent.DB['smib'][ip]
        grup = self.parent.DB['group']
        try:
            ip['hw_id']
        except:
            ip['hw_id'] = ip['hw_uuid']
        head = _(u'Информация за машина: ') + ip['ip'] + '\n\n'
        licenz = _(u'Номер в зала: ') + ip['licenz'] + '\n'
        mashin_sn = _(u'Сериен номер на машина: ') + ip['mashin_sn'] + "\n"
        model = _(u'Модел: ') + ip['model'] + "\n"
        smib_sn = _(u'SMIB: ') + ip['hw_id'] + "\n"
        smib_v =  _(u'Версия на SMIB: ') + ip['version'] + "\n"
        if ip['sas'] == True:
            sas = _(u"SAS Протокол: Наличен") + '\n'
        else:
            sas = _(u"SAS Протокол: Липсва") + '\n'
        var = 0 
        for i in ip['group']:
            try:
                for b in grup[i]['level']:
                    var = var + grup[i]['level'][b]['hiden'] + grup[i]['level'][b]['procent']
            except KeyError:
                pass
                
        procent = _(u"Процент на отчисление: ")  + str(var/0.01) + '\n' + '\t' + _(u'Групи: ') + '\n'
        for i in ip['group']:
            var = 0
            try:
                for b in grup[i]['level']:
                    var = var + grup[i]['level'][b]['hiden'] + grup[i]['level'][b]['procent']

                procent = procent + '\t\t' + i + '= '+ str(var/0.01) + ' %\n'
            except KeyError:
                pass
        text = head + licenz + mashin_sn + model + smib_sn + smib_v + sas + procent
        self.m_richText2.SetValue(text)
        
    def OnHelp(self, event):
        if libs.conf.DOCS_DEBUG == False:
            frame = libs.helps.Help(r'%s%s/colibri/v%s/jackpot.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE, libs.conf.VERSION))
        else:
            frame = libs.helps.Help('http://127.0.0.1:5000/%s/colibri/v%s/jackpot.html' % (libs.conf.USE_LANGUAGE, libs.conf.VERSION))
    
    def DisableGame(self, event):
        ip = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        ip = self.parent.DB['smib'][ip]
        response = libs.udp.send('DISABLE_GAME', new_ip=ip, ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
        if response == True:
            wx.MessageBox(_(u'Информацията е записана успешно!'), 'Info', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(_(u'Грешка при запис на информация!'), 'Error', wx.OK | wx.ICON_ERROR)
