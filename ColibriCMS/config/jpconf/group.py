#-*- coding:utf-8 -*-
from . import _gui  # @UnresolvedImport
import libs
import wx
# import helps
from . exceptions import *
from . import smib
import time
import datetime

# Implementing AddIP
class TimeGroupConfig(_gui.TimeLevelConf):
    def __init__(self, parent, grup_name):
        self.parent = parent
        _gui.TimeLevelConf.__init__(self, parent)
        self.SetTitle(_(u'Настройки група!'))
        self.m_staticText55.SetLabel(_(u'Задържане в минути'))
        self.m_staticText551.SetLabel(_(u'Минимално машини'))
        self.m_staticText5511.SetLabel(_(u'Заедно Х минути'))
        self.m_button25.SetLabel(_(u'Затвори'))
        self.m_button26.SetLabel(_(u'Запис'))

        self.grup_name = grup_name
        self.m_textCtrl26.SetValue(str(self.parent.GetParent().DB['group'][self.grup_name]['real_down_procent']*100))
        try:
            self.m_spinCtrl20.SetValue(self.parent.GetParent().DB['group'][self.grup_name]['min_mashin'])
        except KeyError:
            self.parent.GetParent().DB['group'][self.grup_name]['min_mashin'] = 0
            self.m_spinCtrl20.SetValue(self.parent.GetParent().DB['group'][self.grup_name]['min_mashin'])

        try:
            self.m_spinCtrl201.SetValue(self.parent.GetParent().DB['group'][self.grup_name]['min_mashin_play_time'])
        except KeyError:
            self.parent.GetParent().DB['group'][self.grup_name]['min_mashin_play_time'] = 1
            self.m_spinCtrl201.SetValue(self.parent.GetParent().DB['group'][self.grup_name]['min_mashin_play_time'])

        self.Fit()
#         if self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['use'] == True:
#             self.m_radioBox3.SetSelection(1)
#         else:
#             self.m_radioBox3.SetSelection(0)
#         self.OnProgresivHold(None)
        
#     def OnProgresivHold(self, event):
# #         print self.m_radioBox3.GetSelection()
#         if self.m_radioBox3.GetSelection() == 0:
#             self.m_staticText53.Hide()
#             self.m_spinCtrl19.Hide()
#             self.m_staticText531.Hide()
#             self.m_spinCtrl191.Hide()
#         elif self.m_radioBox3.GetSelection() == 1:
#             self.m_staticText53.Show()
#             self.m_spinCtrl19.Show()
#             self.m_staticText531.Show()
#             self.m_spinCtrl191.Show()
#             self.m_spinCtrl19.SetValue(self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['step'])
#             self.m_spinCtrl191.SetValue(self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['hold']*100)

    def OnClose(self, event):
        self.Destroy()
        
    def OnSave(self, event):
#         if self.m_radioBox3.GetSelection() == 0:
#             self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['use'] = False
#         else:
#             self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['use'] = True
#             self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['step'] = int(self.m_spinCtrl19.GetValue())
#             self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['hold'] = float(self.m_spinCtrl191.GetValue())*0.01
        try:
            float(self.m_textCtrl26.GetValue())
        except Exception:
            wx.MessageBox(_(u'Невалидна стойност'), 'Error', wx.OK | wx.ICON_ERROR)
            return
        if float(self.m_textCtrl26.GetValue()) >= 40 and float(self.m_textCtrl26.GetValue()) <= 1:
            wx.MessageBox(_(u'Невалидна стойност'), 'Error', wx.OK | wx.ICON_ERROR)
            return
        self.parent.GetParent().DB['group'][self.grup_name]['real_down_procent'] = float(self.m_textCtrl26.GetValue()) * 0.01
        self.parent.GetParent().DB['group'][self.grup_name]['min_mashin_play_time'] = self.m_spinCtrl201.GetValue()
        self.parent.GetParent().DB['group'][self.grup_name]['min_mashin'] = self.m_spinCtrl20.GetValue()
        self.Destroy()
        
class ClasicGroupConfig(_gui.ClasicGrupConf):
    def __init__(self, parent, grup_name):
        self.grup_name = grup_name
        self.parent = parent
        _gui.ClasicGrupConf.__init__(self, parent)
        # self.parent.GetParent().DB['group'][self.grup_name]['rotate_if_min_bet'] = False
        # self.parent.GetParent().DB['group'][self.grup_name]['activ'] = {}
        # self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation'] = {'use': False, 'step': 0.10, 'hold': 0.10}
        self.m_staticText55.SetLabel(_(u'Задържане в %'))
        self.SetTitle(_(u'Настройки на група'))
        self.m_staticText53.SetLabel(_(u'Стъпка %'))
        self.m_staticText531.SetLabel(_(u'Забавяне % на база бет'))
        self.m_radioBtn11.SetLabel(_(u'Неактивно'))
        self.m_radioBtn12.SetLabel(_(u'Активно'))
        self.m_button25.SetLabel(_(u'Затвори'))
        self.m_button26.SetLabel(_(u'Запис'))
        self.m_checkBox18.SetLabel(_(u'Глобална'))

        self.m_textCtrl26.SetValue(str(self.parent.GetParent().DB['group'][self.grup_name]['real_down_procent']*100))
        # print(self.parent.GetParent().DB['group'][self.grup_name]['global_mistery'])
        if 'global_mistery' not in self.parent.GetParent().DB['group'][self.grup_name]:
            self.parent.GetParent().DB['group'][self.grup_name]['global_mistery'] = False
        self.m_checkBox18.SetValue(self.parent.GetParent().DB['group'][self.grup_name]['global_mistery'])
        if self.parent.GetParent().DB['group'][self.grup_name]['activ'] == {}:
            self.m_checkBox8.SetValue(True)
        else:
            self.m_checkBox8.SetValue(False)
        if self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['use'] == True:
            self.m_radioBox3.SetSelection(1)
        else:
            self.m_radioBox3.SetSelection(0)
        if self.parent.GetParent().DB['group'][self.grup_name]['rotate_if_min_bet'] == False:
            self.m_radioBtn11.SetValue(True)
        else:
            self.m_radioBtn12.SetValue(True)
        self.m_checkBox8.SetLabel(_(u'Всички'))
        self.m_checkBox9.SetLabel(_(u'Понеделник'))
        self.m_checkBox91.SetLabel(_(u'Вторник'))
        self.m_checkBox911.SetLabel(_(u'Сряда'))
        self.m_checkBox912.SetLabel(_(u'Четвъртък'))
        self.m_checkBox913.SetLabel(_(u'Петък'))
        self.m_checkBox914.SetLabel(_(u'Събота'))
        self.m_checkBox915.SetLabel(_(u'Неделя'))

        self.OnProgresivHold(None)
#         self.OnAllCHK(None)
        self.ActiveSelectedEdit()
        self.Fit()
        
    def ActiveSelected(self, event):
        if self.m_checkBox9.GetValue() == True:
            self.m_checkBox8.SetValue(False)
        elif self.m_checkBox91.GetValue() == True:
            self.m_checkBox8.SetValue(False)
        elif self.m_checkBox911.GetValue() == True:
            self.m_checkBox8.SetValue(False)
        elif self.m_checkBox912.GetValue() == True:
            self.m_checkBox8.SetValue(False)
        elif self.m_checkBox913.GetValue() == True:
            self.m_checkBox8.SetValue(False)
        elif self.m_checkBox914.GetValue() == True:
            self.m_checkBox8.SetValue(False)
        elif self.m_checkBox915.GetValue() == True:
            self.m_checkBox8.SetValue(False)
        else:
            self.m_checkBox8.SetValue(True)
    
    def RemoveAllSelection(self, event):
        if self.m_checkBox8.GetValue() == True:
            self.m_checkBox9.SetValue(False)
            self.m_checkBox91.SetValue(False)
            self.m_checkBox911.SetValue(False)
            self.m_checkBox912.SetValue(False)
            self.m_checkBox913.SetValue(False)
            self.m_checkBox914.SetValue(False)
            self.m_checkBox915.SetValue(False)
        else:
            self.ActiveSelectedEdit()
            
    def ActiveSelectedEdit(self):
        # self.parent.GetParent().DB['group'][self.grup_name]['activ'] = {}
        activ = self.parent.GetParent().DB['group'][self.grup_name]['activ']
        if activ == {}:
            self.m_checkBox8.SetValue(True)
        else:
            self.m_checkBox8.SetValue(False)
            if 0 in activ:
                self.m_checkBox9.SetValue(True)
                self.m_spinCtrl3.SetValue(activ[0]['from_hour'])
                self.m_spinCtrl4.SetValue(activ[0]['to_hour'])
            if 1 in activ:
                self.m_checkBox91.SetValue(True)
                self.m_spinCtrl31.SetValue(activ[1]['from_hour'])
                self.m_spinCtrl41.SetValue(activ[1]['to_hour'])
            if 2 in activ:
                self.m_checkBox911.SetValue(True)
                self.m_spinCtrl311.SetValue(activ[2]['from_hour'])
                self.m_spinCtrl411.SetValue(activ[2]['to_hour'])
            if 3 in activ:
                self.m_checkBox912.SetValue(True)
                self.m_spinCtrl312.SetValue(activ[3]['from_hour'])
                self.m_spinCtrl412.SetValue(activ[3]['to_hour'])
            if 4 in activ:
                self.m_checkBox913.SetValue(True)
                self.m_spinCtrl313.SetValue(activ[4]['from_hour'])
                self.m_spinCtrl413.SetValue(activ[4]['to_hour'])
            if 5 in activ:
                self.m_checkBox914.SetValue(True)
                self.m_spinCtrl314.SetValue(activ[5]['from_hour'])
                self.m_spinCtrl414.SetValue(activ[5]['to_hour'])
            if 6 in activ:
                self.m_checkBox915.SetValue(True)
                self.m_spinCtrl315.SetValue(activ[6]['from_hour'])
                self.m_spinCtrl415.SetValue(activ[6]['to_hour'])

    def OnProgresivHold(self, event):
#         print self.m_radioBox3.GetSelection()
        if self.m_radioBox3.GetSelection() == 0:
            self.m_staticText53.Hide()
            self.m_spinCtrl19.Hide()
            self.m_staticText531.Hide()
            self.m_spinCtrl191.Hide()
        elif self.m_radioBox3.GetSelection() == 1:
            self.m_staticText53.Show()
            self.m_spinCtrl19.Show()
            self.m_staticText531.Show()
            self.m_spinCtrl191.Show()
            self.m_spinCtrl19.SetValue(self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['step'])
            self.m_spinCtrl191.SetValue(self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['hold']*100)
        self.Fit()
        self.Layout()
        
    def OnClose(self, event):
        self.Destroy()
    
    def OnSave(self, event):
        if self.m_checkBox8.GetValue() == True:
            self.parent.GetParent().DB['group'][self.grup_name]['activ'] = {}
        else:
            try:
                if self.m_checkBox9.GetValue() == True:
                    if self.m_spinCtrl3.GetValue() >= self.m_spinCtrl4.GetValue():
                        raise ValueError
                    val = 0
                    self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] = {'from_hour':self.m_spinCtrl3.GetValue(), 'to_hour':self.m_spinCtrl4.GetValue()}
                else:
                    val = 0
                    try:
                        del self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] 
                    except KeyError:
                        pass
                if self.m_checkBox91.GetValue() == True:
                    if self.m_spinCtrl31.GetValue() >= self.m_spinCtrl41.GetValue():
                        raise ValueError
                    val = 1
                    self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] = {'from_hour':self.m_spinCtrl31.GetValue(), 'to_hour':self.m_spinCtrl41.GetValue()}
                else:
                    val = 1
                    try:
                        del self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] 
                    except KeyError:
                        pass
                if self.m_checkBox911.GetValue() == True:
                    if self.m_spinCtrl311.GetValue() >= self.m_spinCtrl411.GetValue():
                        raise ValueError
                    val = 2
                    self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] = {'from_hour':self.m_spinCtrl311.GetValue(), 'to_hour':self.m_spinCtrl411.GetValue()}
                else:
                    val = 2
                    try:
                        del self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] 
                    except KeyError:
                        pass
                if self.m_checkBox912.GetValue() == True:
                    if self.m_spinCtrl312.GetValue() >= self.m_spinCtrl412.GetValue():
                        raise ValueError
                    val = 3
                    self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] = {'from_hour':self.m_spinCtrl312.GetValue(), 'to_hour':self.m_spinCtrl412.GetValue()}
                else:
                    val = 3
                    try:
                        del self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] 
                    except KeyError:
                        pass
                if self.m_checkBox913.GetValue() == True:
                    if self.m_spinCtrl313.GetValue() >= self.m_spinCtrl413.GetValue():
                        raise ValueError
                    val = 4
                    self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] = {'from_hour':self.m_spinCtrl313.GetValue(), 'to_hour':self.m_spinCtrl413.GetValue()}
                else:
                    val = 4
                    try:
                        del self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] 
                    except KeyError:
                        pass
                if self.m_checkBox914.GetValue() == True:
                    if self.m_spinCtrl314.GetValue() >= self.m_spinCtrl414.GetValue():
                        raise ValueError
                    val = 5
                    self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] = {'from_hour':self.m_spinCtrl314.GetValue(), 'to_hour':self.m_spinCtrl414.GetValue()}
                else:
                    val = 5
                    try:
                        del self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] 
                    except KeyError:
                        pass
                if self.m_checkBox915.GetValue() == True:
                    if self.m_spinCtrl315.GetValue() >= self.m_spinCtrl415.GetValue():
                        raise ValueError
                    val = 6
                    self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] = {'from_hour':self.m_spinCtrl315.GetValue(), 'to_hour':self.m_spinCtrl415.GetValue()}
                else:
                    val = 6
                    try:
                        del self.parent.GetParent().DB['group'][self.grup_name]['activ'][val] 
                    except KeyError:
                        pass
#                 print self.parent.GetParent().DB['group'][self.grup_name]['activ'].keys()
            except ValueError:
                wx.MessageBox(_(u'Невалидна стойност'), 'Error', wx.OK | wx.ICON_ERROR)
                return
        if self.m_radioBox3.GetSelection() == 0:
            self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['use'] = False
        else:
            self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['use'] = True
            self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['step'] = int(self.m_spinCtrl19.GetValue())
            self.parent.GetParent().DB['group'][self.grup_name]['hold_rotation']['hold'] = float(self.m_spinCtrl191.GetValue())*0.01
            
        if float(self.m_textCtrl26.GetValue()) > 70:
            wx.MessageBox(_(u'Невалидна стойност'), 'Error', wx.OK | wx.ICON_ERROR)
            return
        self.parent.GetParent().DB['group'][self.grup_name]['real_down_procent'] = float(self.m_textCtrl26.GetValue()) * 0.01

        if self.m_radioBtn11.GetValue() == True:
            self.parent.GetParent().DB['group'][self.grup_name]['rotate_if_min_bet'] = False
        else:
            self.parent.GetParent().DB['group'][self.grup_name]['rotate_if_min_bet'] = True
        if self.parent.GetParent().DB['casino_name']['ip']:
            self.parent.GetParent().DB['group'][self.grup_name]['global_mistery'] = False
            wx.MessageBox(_(u'Не може да има глобални мистерии!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            self.parent.GetParent().DB['group'][self.grup_name]['global_mistery'] = self.m_checkBox18.GetValue()
        self.OnClose(event)
            
        
class AddName(_gui.AddIP):
    def __init__(self, parent):
        _gui.AddIP.__init__(self, parent)
        self.SetTitle(_(u"Име на Група"))
        self.parent = parent
        self.m_staticText20.SetLabel(_(u"Име на Група"))

        self.m_textCtrl12.SetToolTip(_(u"Попълнете свободен текст"))

        self.m_choice1Choices = [_(u'Класичеста игра'), _(u'Игра по време'), _(u'Бомби')]

        self.m_choice2.SetItems(self.m_choice1Choices)
        self.m_choice2.SetSelection(0)
        self.m_choice2.Show()
        self.m_button1.SetLabel(_(u"Добави"))
        self.Fit()


    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        grup = list(self.parent.GetParent().DB['group'].keys())
#         grup = tcp.send('GET_ALL_JP_GRUP')
        self.grup_name = self.m_textCtrl12.GetValue()
        self.game_type = self.m_choice2.GetSelection()
        if self.game_type == 2:
            self.game_type = 1
            self.hiden_visual = True
        else:
            self.hiden_visual = False
        if self.grup_name in grup:
            dlg = wx.MessageBox(_(u'Групата съществува!'), 'Error', wx.OK | wx.ICON_ERROR)
        elif self.grup_name == u'':
            dlg = wx.MessageBox(_(u'Всички полета са задължителни'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
#             tcp.send('ADD_GRUP', grup_name=self.grup_name, game_type=self.game_type,
#                      visual={}, mashin={}, level={})
            if self.game_type == 0:
                real_down_procent = 0.4
            else:
                real_down_procent = 0.15
            self.parent.GetParent().DB['group'][self.grup_name] = {'grup_name':self.grup_name,
                                           'game_type': self.game_type,
                                           'visual':{},
                                           'mashin':{},
                                           'level':{},
                                           'real_down_procent':real_down_procent,
                                           'activ': {},
                                           'hold_rotation': {'use':False, 'step': 0.10, 'hold':0.10},
                                           'rotate_if_min_bet': False,
                                           'hiden_visual': self.hiden_visual,
                                           'min_mashin': 0,
                                           'min_mashin_play_time': 1,
                                           'global_mistery':  False
                                           }
            # dlg = wx.MessageBox(_(u'Моля добавете визуализация!'), 'Info', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()


class AddDevisToGrup(_gui.AddSMIBToGroup):
    def __init__(self, parent, grup, add_type):
        self.add_type = add_type
        self.grup = grup
        self.parent = parent
#         self.all_grup = tcp.send("GET_GRUP")
        self.all_grup = self.parent.GetParent().DB['group']
        _gui.AddSMIBToGroup.__init__(self, parent)
        self.m_button14.SetLabel(_(u'Затвори'))
        self.m_button15.SetLabel(_(u'Запис'))
        if add_type == 'visual':

            self.server_data = self.parent.GetParent().DB['visual']

        elif add_type == 'mashin':
            self.server_data = self.parent.GetParent().DB['smib']

        self.refreshFrame()

    def refreshFrame(self):
        self.m_listBox1Choices = []
        self.m_listBox2Choices = []
        if self.add_type == 'visual':
            self.SetTitle(_(u'Дабявяне на визуализация!'))
            self.m_staticText24.SetLabel(_(u'Свободни визуализации'))
            self.m_staticText26.SetLabel(_(u'Визуализации в групата'))
            try:
                self.hiden_visual = self.all_grup[self.grup]['hiden_visual']
            except KeyError:
                self.all_grup[self.grup]['hiden_visual'] = False
                self.hiden_visual = self.all_grup[self.grup]['hiden_visual']
            if self.hiden_visual == False:
                for i in sorted(list(self.server_data.keys())):
                    if self.server_data[i]['group'] == self.grup:
                        self.m_listBox2Choices.append(i)
                    elif self.server_data[i]['group'] == _(u'Свободни'):
                        self.m_listBox1Choices.append(i)
            else:
                for i in sorted(list(self.server_data.keys())):
                    if i in self.all_grup[self.grup]['visual']:
                        self.m_listBox2Choices.append(i)
                    else:
                        self.m_listBox1Choices.append(i)
                    
                
        elif self.add_type == 'mashin':
            self.SetTitle(_(u'Дабявяне на машини!'))
            self.m_staticText24.SetLabel(_(u'Всички машини'))
            self.m_staticText26.SetLabel(_(u'Машини в групата'))
            for item in sorted(list(self.server_data.keys())):
                if self.grup in self.server_data[item]['group']:
                    self.m_listBox2Choices.append(item)
                else:
                    self.m_listBox1Choices.append(item)

        self.m_listBox1.Set(self.m_listBox1Choices)
        self.m_listBox1.SetToolTip(_(u"Списък със свободни визуализации!"))
        self.m_listBox2.Set(self.m_listBox2Choices)
        self.m_listBox2.SetToolTip(_(u"Списък с визуализациите в групата!"))


    def OnShowNomInL( self, event ):
        if self.add_type == 'visual':
            return
        try:
            item = self.m_listBox1Choices[self.m_listBox1.GetSelection()]
            self.m_staticText67.SetLabel(self.server_data[item]['licenz'])
        except IndexError:
            pass


    def OnShowNomInLRight(self, event):
        if self.add_type == 'visual':
            return
        try:
            item = self.m_listBox2Choices[self.m_listBox2.GetSelection()]
            self.m_staticText67.SetLabel(self.server_data[item]['licenz'])
        except IndexError:
            pass

    def AddToGroup(self, event):
        try:
            item = self.m_listBox1Choices[self.m_listBox1.GetSelection()]
        except IndexError:
            wx.MessageBox(_(u'Моля изберете модул!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            if self.add_type == 'visual':
                if self.hiden_visual == False:

                    self.server_data[item] = {'ip': item, 'group': self.grup}
                    self.all_grup[self.grup][self.add_type][item] = item
                else:
                    self.all_grup[self.grup][self.add_type][item] = item
                    # print self.all_grup[self.grup][self.add_type]
            else:
                pr = 0
                for i in self.all_grup:
                    try:
                        for b in self.all_grup[self.grup]['level']:
                            pr = pr + self.all_grup[i]['level'][b]['procent'] + self.all_grup[i]['level'][b]['hiden']
                    except KeyError:
                        pass
                    
#                 pr = 0 
#                 for i in self.server_data[item]['group']:
#                     
#                     for b in self.all_grup[i]['level']:
#                         print self.all_grup[i]['level']
#                         pr = pr + self.all_grup[i]['level'][b]['hiden'] + self.all_grup[i]['level']['level'][b]['procent']
                        
#                     procent = var
            
#                 pr = pr + self.server_data[item]['procent']
#                 self.server_data[item]['procent'] += pr
                pr = 0 
#                 for i in self.server_data[item]['group']:
#                 print self.all_grup.keys()
                for i in self.all_grup:
#                     print item
                    if i in self.server_data[item]['group']:
                        for b in self.all_grup[i]['level']:
                            pr += self.all_grup[i]['level'][b]['hiden'] + self.all_grup[i]['level'][b]['procent']
#                 print pr
#         procent = _(u"Процен на отчисление: ")  + str(var/0.01) + '\n' + '\t' + _(u'Групи: ') + '\n'
#                 print pr
                if pr > 0.05:
                    wx.MessageBox(_(u'Невъзможна операция!\nНадвишава 5 %'), 'Error', wx.OK | wx.ICON_ERROR)
                else:
                    self.server_data[item]['procent'] = pr
                    self.server_data[item]['group'].append(self.grup)
                    # self.all_grup[self.grup][self.add_type][item] = item
        self.refreshFrame()

    def RemoveFromGroup(self, event):
        try:
            item = self.m_listBox2Choices[self.m_listBox2.GetSelection()]
        except IndexError:
            wx.MessageBox(_(u'Моля изберете модул!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            if self.add_type == 'mashin':
                del self.server_data[item]['group'][self.server_data[item]['group'].index(self.grup, )]
                # del self.server_data[item]['group'][self.server_data[item]['group'].index(self.grup, )]
                pr = 0
                # del self.all_grup[self.grup]['mashin'][item]
                for i in self.all_grup[self.grup]['level']:
                    pr = pr + self.all_grup[self.grup]['level'][i]['procent'] + self.all_grup[self.grup]['level'][i]['hiden']
                self.server_data[item]['procent'] -= pr
            elif self.add_type == 'visual':
#                 if len(self.all_grup[self.grup]['visual'])-1 < 1:
#                     dlg = wx.MessageBox(_(u'Невъзможна операция!') + '\n' +
#                                     _(u'Групата ще остане без визуализация!'), 'Error',
#                                     wx.OK | wx.ICON_ERROR)
#                 else:
                if self.hiden_visual == False:
                    self.server_data[item] = {'ip':item, 'group':_(u'Свободни')}
                del self.all_grup[self.grup]['visual'][item]
            self.refreshFrame()

    def OnGo( self, event ):
        if self.add_type == 'visual':
            self.parent.GetParent().DB['visual'] = self.server_data
            self.parent.GetParent().DB['group'] = self.all_grup
            self.Destroy()
        else:
            self.parent.GetParent().DB['smib'] = self.server_data
            self.parent.GetParent().DB['group'] = self.all_grup
            self.Destroy()

    def OnClose(self, event):
        self.Destroy()


class ClasicGame(_gui.ClasicLevel):
    def __init__(self, parent, grup, select, edit=False, edit_val=False):
        _gui.ClasicLevel.__init__(self, parent)
        self.grup = grup
        self.parent = parent
        self.select = select
        self.SetTitle(_(u'Нива'))
        self.edit = edit
        self.edit_val = edit_val

        self.m_staticText31.SetLabel(_(u'Име на ниво'))
        self.m_staticText39.SetLabel(_(u'Начална стойност'))
        self.m_staticText34.SetLabel(_(u'Обхват'))
        self.m_staticText35.SetLabel(_(u'Отчисление %'))
        self.m_staticText32.SetLabel(_(u'От сума'))
        self.m_staticText33.SetLabel(_(u'До сума'))
        self.m_staticText37.SetLabel(_(u'Отчисление %'))
        self.m_staticText38.SetLabel(_(u'Скрит %'))
        self.m_checkBox171.SetLabel(_(u'Задължителна карта'))
        self.m_checkBox171.SetToolTip(_(u'Изисква клиентска карта за да върти'))
        self.m_radioBtn3.SetLabel(_(u'Класик'))
        self.m_radioBtn4.SetLabel(_(u'Съзтезателна'))
        self.m_spinCtrl21.SetToolTip(_(u'Брой участници'))
        self.m_staticText54.SetLabel(_(u'Задържане в %'))
        self.m_staticText53.SetLabel(_(u'Текуща стойност: '))
        self.m_staticText55.SetLabel(_(u'Скрита стойност: '))
        self.m_staticText68.SetLabel(u'')
        self.m_checkBox17.SetLabel(_(u'Умножи x2'))



        self.m_button16.SetLabel(_(u'Затвори'))
        self.m_button17.SetLabel(_(u'Запис'))
        self.m_staticText56.SetLabel(_(u'Мин. Бет'))
        self.m_textCtrl32.Hide()
        if edit == False:
            self.edit_down = False
            self.m_textCtrl35.SetValue(u'0.00')
            self.m_textCtrl32.SetValue(u'0.00')
            self.m_textCtrl22.SetValue(u'0')
            self.m_textCtrl33.SetValue(u'0')
            # self.m_textCtrl35.SetValue(u'0.00')
            self.m_textCtrl16.SetValue(u'0')
            self.m_textCtrl17.SetValue(u'0')
            self.m_textCtrl20.SetValue(u'0.00')
            self.m_textCtrl21.SetValue(u'0.00')
            self.m_spinCtrl21.SetValue(3)
            self.m_checkBox17.SetValue(False)
            self.m_textCtrl332.SetValue('')
            self.m_textCtrl34.SetValue('')
            self.m_spinCtrl21.Hide()
            self.m_textCtrl332.Hide()
            self.m_textCtrl34.Hide()
            self.m_staticText68.SetLabel(u'')
        else:
            self.SetTitle(str(self.grup[edit]['level'][self.select]['name']))
            try:
                self.m_checkBox171.SetValue(self.grup[edit]['level'][self.select]['player'])
            except:
                pass
            try:
                self.edit_down = libs.conf.EDITDOWN
                self.grup[edit]['level'][self.select]['down_value']
            except:
                self.edit_down = False
            try:
                self.edit_val = libs.conf.EDITVAL
            except KeyError:
                self.edit_val = False
            try:
                self.grup[edit]['level'][self.select]['x2']
            except KeyError:
                self.grup[edit]['level'][self.select]['x2'] = False
                self.grup[edit]['level'][self.select]['x2_time'] = {'from':'', 'to':''}
            try:
                self.grup[edit]['level'][self.select]['runner_count']
            except KeyError:
                self.grup[edit]['level'][self.select]['runner_count'] = 3
            # try:
            #     self.m_checkBox171.SetValue(self.grup[edit]['level']['player'])
            # except KeyError:
            #     pass
            self.m_spinCtrl21.SetValue(self.grup[edit]['level'][self.select]['runner_count'])
            self.m_checkBox17.SetValue(self.grup[edit]['level'][self.select]['x2'])
            self.m_textCtrl332.SetValue(str(self.grup[edit]['level'][self.select]['x2_time']['from']))
            self.m_textCtrl34.SetValue(str(self.grup[edit]['level'][self.select]['x2_time']['to']))
            if self.edit_down == True:
                self.m_textCtrl331.SetValue(str(self.grup[edit]['level'][self.select]['down_value']))
                self.m_textCtrl331.Show()
                self.m_staticText63.Show()
            if self.edit_val == True:
                self.m_staticText541.Bind(wx.EVT_LEFT_DCLICK, self.OnEditVal)
                self.m_staticText561.Bind(wx.EVT_LEFT_DCLICK, self.OnEditHidenVal)
            self.m_staticText68.SetLabel(_(u'От/До Час х2'))
            edit = self.grup[edit]['level'][self.select]
            
            try:
                self.m_staticText541.SetLabel(str(round(edit['value'], 2)))
                self.m_staticText561.SetLabel(str(round(edit['hiden_value'], 5)))
            except  KeyError:
                self.m_staticText541.SetLabel(str(round(0, 2)))  
                self.m_staticText561.SetLabel(str(round(0, 5)))  
            self.select = self.edit
            self.procent = edit['procent']
            self.hiden = edit['hiden']
            
            self.m_textCtrl15.SetValue(edit['name'])
            self.m_textCtrl15.Hide()
            self.m_staticText31.Hide()
            try:
                self.m_textCtrl33.SetValue(str(edit['hold_procent']*100))
            except KeyError:
                self.m_textCtrl33.SetValue(u'0')
            self.m_textCtrl35.SetValue(str(edit['min bet']))
            self.m_textCtrl22.SetValue(str(edit['start_value']))
            self.m_textCtrl16.SetValue(str(edit['down']['from']))
            self.m_textCtrl17.SetValue(str(edit['down']['to']))
            data = round(float(edit['procent'])/0.01, 5)
            self.m_textCtrl20.SetValue(str(data))
            data = str(round(float(edit['hiden'])/0.01,5))
            self.m_textCtrl21.SetValue(data)
            self.m_radioBtn4.SetValue(edit['bet'])

            if edit['bet'] == False:
                self.m_radioBtn3.SetValue(True)
                self.m_textCtrl32.Hide()
                self.m_textCtrl32.SetValue(u'0')
                self.m_checkBox17.Show()
                self.m_spinCtrl21.Hide()
                # self.m_spinCtrl21.Show()
                if self.m_checkBox17.GetValue() == True:
                    self.m_textCtrl332.Show()
                    self.m_textCtrl34.Show()
                    self.m_staticText68.SetLabel(_(u'От/До Час х2'))
                else:
                    self.m_textCtrl332.Hide()
                    self.m_textCtrl34.Hide()
                    self.m_staticText68.SetLabel(u'')
            else:
                self.m_textCtrl32.Show()
                self.m_textCtrl35.SetValue(str(edit['runner']['from']))
                self.m_textCtrl32.SetValue(str(edit['runner']['to']))
                # self.m_checkBox17.Hide()
                self.m_spinCtrl21.Show()
                # self.m_textCtrl332.Hide()
                # self.m_textCtrl34.Hide()
                self.m_staticText56.SetLabel(_(u'Рейндж в състезание'))
                if self.m_checkBox17.GetValue() == True:
                    self.m_textCtrl332.Show()
                    self.m_textCtrl34.Show()
                    self.m_staticText68.SetLabel(_(u'От/До Час х2'))
                else:
                    self.m_textCtrl332.Hide()
                    self.m_textCtrl34.Hide()
                    self.m_staticText68.SetLabel(u'')

        self.m_textCtrl15.SetToolTip(_(u"Въведете име на игра!"))
        self.m_textCtrl22.SetToolTip(_(u'Начална стойност в пари цяло число!'))
        self.m_textCtrl16.SetToolTip(_(u"Въведете стойност в пари, цяло число!"))
        self.m_textCtrl17.SetToolTip(_(u"Въведете стойност в пари, цяло число!"))
        self.m_textCtrl20.SetToolTip(_(u"Въведете процент във формат: число с плаваща запетая, закръглено до втория знак!"))
        self.m_textCtrl21.SetToolTip(_(u"Въведете процент във формат: число с плаваща запетая, закръглено до втория знак!"))
        self.Fit()

    def OnEditHidenVal(self, event):
        dial = EditVal(self, self.m_staticText561.GetLabel())
        dial.ShowModal()
        name = self.m_textCtrl15.GetValue()
        try:

            self.grup[self.select]['level'][name]['hiden_value'] = float(dial.val)
            self.m_staticText561.SetLabel(dial.val)
        except:
            wx.MessageBox(_(u'Невалидна стойност!'), 'Error', wx.OK | wx.ICON_ERROR)

    def OnEditVal(self, event):
        dial = EditVal(self, self.m_staticText541.GetLabel())
        dial.ShowModal()
        name = self.m_textCtrl15.GetValue()
        try:

            self.grup[self.select]['level'][name]['value'] = float(dial.val)
            self.m_staticText541.SetLabel(dial.val)
            self.grup[self.select]['level'][name]['val_edit']=True
        except:
            self.grup[self.select]['level'][name]['val_edit'] = False
            wx.MessageBox(_(u'Невалидна стойност!'), 'Error', wx.OK | wx.ICON_ERROR)

    def OnX2( self, event ):
        if self.m_checkBox17.GetValue() == True:
            self.m_textCtrl332.Show()
            self.m_textCtrl34.Show()
            self.m_staticText68.SetLabel(_(u'От/До Час х2'))
        else:
            self.m_textCtrl332.Hide()
            self.m_textCtrl34.Hide()
            self.m_staticText68.SetLabel(u'')
        self.Fit()

    def OnHide(self, event):
        self.m_textCtrl32.Show()
        self.m_textCtrl32.SetValue(u'0')
        self.m_textCtrl35.SetValue(u'0')
        self.m_staticText56.SetLabel(_(u'Рейндж в състезание'))
        self.m_checkBox17.Show()
        self.m_spinCtrl21.Show()
        self.Fit()
        
    def OnShow(self, event):
        self.m_textCtrl35.Show()
        self.m_staticText56.SetLabel(_(u'Мин. Бет'))
        self.m_textCtrl32.Hide()
        self.m_checkBox17.Show()
        self.m_spinCtrl21.Hide()
        self.Fit()
          
    def OnClose( self, event ):
        self.Destroy()
        
    def OnGo( self, event ):
        name = self.m_textCtrl15.GetValue()
        try:
            if name in self.grup:
                wx.MessageBox(_(u'Името съществува'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if name == u'':
                wx.MessageBox(_(u'Името не може да остане празно!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            elif name in self.grup[self.select]['level'] and self.edit == False or name in self.grup :
                wx.MessageBox(_(u'Името съществува'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            start_value = int(self.m_textCtrl22.GetValue())
            if start_value < 0:
                wx.MessageBox(_(u'Началната стойност не може да е 0 или по малка!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            player = self.m_checkBox171.GetValue()
            down = {'from': int(self.m_textCtrl16.GetValue()), 'to': int(self.m_textCtrl17.GetValue())}
            if down['from'] > down['to'] :
                wx.MessageBox(_(u'Крайната граница на падане трябва да е по-голяма от началната!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if down['from'] > down['to'] - (down['to'] *0.10):
                wx.MessageBox(_(u'Разликата меду границите на падане трабва да е по-голяма от 10 %!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if start_value > down['to']:
                wx.MessageBox(_(u'Крайната граница не може да е по-малка от началната стойност!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if start_value > down['from']:
                wx.MessageBox(_(u'Началната граница не може да е по-голяма от началната стойност!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if self.edit_down == True:
                down_value = self.m_textCtrl331.GetValue()
                down_value = down_value.replace(',', '.')
                down_value = float(down_value)

            hold = float(self.m_textCtrl33.GetValue())
            hold = hold* 0.01
            procent = self.m_textCtrl20.GetValue()
            procent = round(float(procent.replace(',', '.')) * 0.01, 5)
            hiden = self.m_textCtrl21.GetValue()
            hiden = round(float(hiden.replace(',', '.')) * 0.01, 5)
            if procent <= hiden:
                wx.MessageBox(_(u'Скрития процент не може да е по-голям или равен на видимия!!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if procent <= 0:
                raise ValueError
            pr = 0

            if self.edit != False:
                self.grup[self.select]['level'][name]['procent'] = 0
                self.grup[self.select]['level'][name]['hiden'] = 0
            for item in self.grup[self.select]['level']:
                pr = pr + self.grup[self.select]['level'][item]['procent'] + self.grup[self.select]['level'][item]['hiden']
            if procent <= 0 or hiden < 0:
                wx.MessageBox(_(u'Невъзможна операция!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if pr + procent + hiden > 0.05:
                wx.MessageBox(_(u'Невъзможна операция!\nНадвишава 5 %'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            bet = self.m_radioBtn4.GetValue()
            if not name or not start_value or not down or not procent:
                wx.MessageBox(_(u'Всички полета са задължителни!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            
            all_smib = self.parent.GetParent().DB['smib']
            for item in all_smib:
                if self.select in all_smib[item]['group']:
                    if self.edit != False:
                        all_smib[item]['procent'] = all_smib[item]['procent'] - (self.procent + self.hiden)
                    if all_smib[item]['procent'] + procent + hiden > 0.05:
                        wx.MessageBox(_(u'Невъзможна операция!\nНадвишава 5 %'), 'Error', wx.OK | wx.ICON_ERROR)
                        raise GUIException
                    else:
                        all_smib[item]['procent'] = all_smib[item]['procent'] + procent + hiden
            if bet == True:
                runner_to = self.m_textCtrl32.GetValue()
                min_bet = self.m_textCtrl35.GetValue()
                runner_to = int(runner_to)
                min_bet = int(min_bet)
                runner = {'from': min_bet, 'to':runner_to}
                if runner['from'] < 1 or runner['to'] > 50000:
                    wx.MessageBox(_(u'Невъзможна операция!\nОбхвата в състезание трябва да е Цяло число:\n4 <от-до> 50000'), 'Error', wx.OK | wx.ICON_ERROR)
                    raise GUIException
            else:
                min_bet = self.m_textCtrl35.GetValue()
                min_bet = min_bet.replace(',', '.')
                min_bet = float(min_bet)
            x2 = self.m_checkBox17.GetValue()
            runner_count = self.m_spinCtrl21.GetValue()
            if x2 == True:
                x2_time_from = self.m_textCtrl332.GetValue()
                x2_time_to = self.m_textCtrl34.GetValue()
                try:
                    x2_time_from = int(x2_time_from)
                    x2_time_to = int(x2_time_to)
                except:
                    raise ValueError
            else:
                x2_time_from = ''
                x2_time_to = ''

        except ValueError:
            wx.MessageBox(_(u'Невалидна стойност!'), 'Error', wx.OK | wx.ICON_ERROR)
        except GUIException:
            pass
        else:
            if self.edit != False:

                self.grup[self.select]['level'][name]['name'] = name
                self.grup[self.select]['level'][name]['start_value'] = start_value
                self.grup[self.select]['level'][name]['down'] = down
                self.grup[self.select]['level'][name]['procent'] = procent
                self.grup[self.select]['level'][name]['hiden'] = hiden
                self.grup[self.select]['level'][name]['bet'] = bet
                self.grup[self.select]['level'][name]['hold_procent'] = hold
                self.grup[self.select]['level'][name]['x2'] = x2
                self.grup[self.select]['level'][name]['x2_time'] = {'from':x2_time_from, 'to':x2_time_to}
                self.grup[self.select]['level'][name]['runner_count'] = runner_count
                self.grup[self.select]['level'][name]['player'] = player
                if self.edit_down == True:
                    self.grup[self.select]['level'][name]['down_value'] = down_value
#                 self.grup[self.select]['level'][name]['last_down'] = 0
                if bet == False:
                    self.grup[self.select]['level'][name]['min bet'] = min_bet
                else:
                    self.grup[self.select]['level'][name]['min bet'] = 0
                    self.grup[self.select]['level'][name]['runner'] = runner
            else:

                if bet == False:
                    self.grup[self.select]['level'][name] = {'name':name, 'player': player, 'start_value':start_value, 'down':down, 'procent':procent,
                                                 'hiden':hiden, 'bet':bet, 'min bet':min_bet, 'hold_procent':hold,
                                                             'x2': x2, 'x2_time': {'from': x2_time_from, 'to': x2_time_to}, 'runner_count':runner_count}
                else:
                    self.grup[self.select]['level'][name] = {'name':name, 'player': player, 'start_value':start_value, 'down':down, 'procent':procent,
                                                 'hiden':hiden, 'bet':bet, 'min bet':0, 'runner':runner, 'hold_procent':hold,
                    'x2': x2, 'x2_time': {'from': x2_time_from, 'to': x2_time_to}, 'runner_count':runner_count}

            self.parent.GetParent().DB['smib'] = all_smib
            self.parent.GetParent().DB['group'] = self.grup
            self.Destroy()



class TimeGame(_gui.TimeLevel):
    def __init__(self, parent, grup, select, edit=False):
        _gui.TimeLevel.__init__(self, parent)
        self.parent = parent
        self.edit = edit
        self.grup = grup
        self.select = select
        self.SetTitle(_(u'Нива'))
        self.m_staticText51.SetLabel(_(u'Минимален бет'))
        self.m_staticText411.SetLabel(_(u'Име на ниво:'))
        self.m_checkBox1.SetLabel(_(u'Понеделник'))
        self.m_checkBox2.SetLabel(_(u'Вторник'))
        self.m_checkBox3.SetLabel(_(u'Сряда'))
        self.m_checkBox4.SetLabel(_(u'Четвъртък'))
        self.m_checkBox5.SetLabel(_(u'Петък'))
        self.m_checkBox6.SetLabel(_(u'Събота'))
        self.m_checkBox7.SetLabel(_(u'Неделя'))

        self.m_staticText37.SetLabel(_(u'Период:'))
        self.m_staticText42.SetLabel(_(u'Стойност:'))
        self.m_staticText40.SetLabel(_(u'От Час:'))
        self.m_staticText41.SetLabel(_(u'До Час:'))
        self.m_radioBtn5.SetLabel(_(u'Фиксирана стойност'))
        self.m_radioBtn6.SetLabel(_(u'С натрупване'))
        self.m_staticText45.SetLabel(_(u'Отчисление %'))
        self.chpises = [_(u"Дневен"), _(u"Седмичен")]
        self.m_choice4.SetItems(self.chpises)
        self.m_choice4.SetSelection(0)

        if self.edit != False:
            self.SetTitle(str(self.grup[edit]['level'][self.select]['name']))
            self.m_textCtrl281.SetValue(str(self.grup[edit]['level'][self.select]['min bet']))
            self.m_textCtrl241.SetValue(self.grup[edit]['level'][self.select]['name'])
            self.m_textCtrl241.Hide()
            self.m_staticText411.Hide()
            if self.grup[self.edit]['level'][self.select]['bet'] == True:
                self.m_radioBtn6.SetValue(True)
            else:
                self.m_radioBtn5.SetValue(True)
            if self.grup[self.edit]['level'][self.select]['bet'] == False:
                self.OnRemoveProcent()
            else:
                self.OnAddProcent()
            self.m_textCtrl28.SetValue(str(round(self.grup[edit]['level'][self.select]['procent']/0.01, 5)))
            
            if self.grup[edit]['level'][self.select]['day_down'][0] == -1:
                self.m_choice4.SetSelection(0)
            else:
                self.m_choice4.SetSelection(1)
                if 'day_down' in self.grup[edit]['level'][self.select]:
                    self.m_choice4.SetSelection(1)
                    for i in self.grup[edit]['level'][self.select]['day_down']:
                        if i == 0:
                            self.m_checkBox1.SetValue(True)
                        if i == 1:
                            self.m_checkBox2.SetValue(True)
                        if i == 2:
                            self.m_checkBox3.SetValue(True)
                        if i == 3:
                            self.m_checkBox4.SetValue(True)
                        if i == 4:
                            self.m_checkBox5.SetValue(True)
                        if i == 5:
                            self.m_checkBox6.SetValue(True)
                        if i == 6:
                            self.m_checkBox7.SetValue(True)
            self.OnFixFrame()
#             if self.grup[edit]['level'][self.select]['procent'] != 0:
#                 self.m_radioBtn6.SetValue(True)
#                 self.m_textCtrl28.SetValue(str(round(self.grup[edit]['level'][self.select]['procent']/0.01)))
#                 self.procent = self.grup[edit]['level'][self.select]['procent']
#                 self.OnAddProcent()
                
            self.m_textCtrl25.SetValue(str(self.grup[edit]['level'][self.select]['start_value']))
            self.m_textCtrl23.SetValue(str(self.grup[edit]['level'][self.select]['down']['from']))
            self.m_textCtrl24.SetValue(str(self.grup[edit]['level'][self.select]['down']['to']))

        self.m_textCtrl241.SetToolTip(_(u"Въведете име на игра!"))
        self.m_textCtrl25.SetToolTip(_(u"Въведете начална стойност в пари, цяло число!"))
        self.m_textCtrl23.SetToolTip(_(u"Въведете цяло число от 1 до 23.59!"))
        self.m_textCtrl24.SetToolTip(_(u"Въведете цяло число от 1 до 23.59!"))
        self.m_textCtrl28.SetToolTip(_(u"Въведете процент във формат: число с плаваща запетая, закръглено до втория знак!"))

        self.m_button16.SetLabel(_(u'Затвори'))
        self.m_button17.SetLabel(_(u'Запис'))
        self.Fit()

    def OnGo(self, event):
        level_name = self.m_textCtrl241.GetValue()
        try:
            if level_name in self.grup:
                wx.MessageBox(_(u'Името съществува!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if self.edit == False:
                if level_name in self.grup[self.select]['level'] or level_name in self.grup:
                    wx.MessageBox(_(u'Името съществува!'), 'Error', wx.OK | wx.ICON_ERROR)
                    raise GUIException
            if level_name == u'':
                wx.MessageBox(_(u'Името не може да е празно!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            bet = self.m_radioBtn6.GetValue()
            start_value = int(self.m_textCtrl25.GetValue())
            try:
                down = {
                    'from':float(self.m_textCtrl23.GetValue()),
                    'to': float(self.m_textCtrl24.GetValue())
                        }
            except ValueError:
                wx.MessageBox(_(u'Невалиден час!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if down['from'] >= down['to']:
                wx.MessageBox(_(u'Крайният час на падане не може да е равен или по-малък от началния!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if down['from'] > down['to']:
                wx.MessageBox(_(u'Рейнджа трябва да е в рамките на 24 часа! От: 1 До:24'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            min_bet = self.m_textCtrl281.GetValue()
            try:
                min_bet = float(min_bet)
            except Exception:
                raise GUIException
            else:
                if min_bet < 0:
                    raise GUIException
            if down['from'] < 1 or down['from'] > 23.59 or down['to'] < 1 or down['to'] > 23.59:
                wx.MessageBox(_(u'Невалиден час!'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
            if self.m_radioBtn6.GetValue() == False:
                procent = 0
            else:
                procent = self.m_textCtrl28.GetValue()
                procent = round(float(procent.replace(',', '.'))*0.01, 5)
                if procent <= 0:
                    raise GUIException
            hiden = 0
            if self.m_choice4.GetSelection() == 1:
                day_down = []
                if self.m_checkBox1.GetValue() == True:
                    day_down.append(0)
                if self.m_checkBox2.GetValue() == True:
                    day_down.append(1)
                if self.m_checkBox3.GetValue() == True:
                    day_down.append(2)
                if self.m_checkBox4.GetValue() == True:
                    day_down.append(3)
                if self.m_checkBox5.GetValue() == True:
                    day_down.append(4)
                if self.m_checkBox6.GetValue() == True:
                    day_down.append(5)
                if self.m_checkBox7.GetValue() == True:
                    day_down.append(6)
                if day_down == []:
                    wx.MessageBox(_(u'Моля изберете ден от седмицата!'), 'Error', wx.OK | wx.ICON_ERROR)
                    raise GUIException
            all_smib = self.parent.GetParent().DB['smib']
            pr = 0
            if self.edit == False:
                for item in self.grup[self.select]['level']:
                    pr = pr + self.grup[self.select]['level'][item]['procent']
                pr = pr + procent
                for item in self.grup[self.select]['mashin']:
                    if all_smib[item]['procent'] + procent + hiden > 0.05:
                        wx.MessageBox(_(u'Невъзможна операция!\nНадвишава 5 %'), 'Error', wx.OK | wx.ICON_ERROR)
                        raise GUIException
                    else:
                        all_smib[item]['procent'] = all_smib[item]['procent'] +procent + hiden
            else:
                self.grup[self.edit]['level'][self.select]['procent'] = procent
                for item in self.grup[self.edit]['level']:
                    pr = pr + self.grup[self.edit]['level'][item]['procent']

                for item in self.grup[self.edit]['mashin']:
                    all_smib[item]['procent'] = all_smib[item]['procent'] - procent
                    if all_smib[item]['procent'] + procent + hiden > 0.05:
                        wx.MessageBox(_(u'Невъзможна операция!\nНадвишава 5 %'), 'Error', wx.OK | wx.ICON_ERROR)
                        raise GUIException
                    else:
                        all_smib[item]['procent'] = + all_smib[item]['procent'] +procent + hiden
        
            if pr > 0.05:
                wx.MessageBox(_(u'Невъзможна операция!\nНадвишава 5 %'), 'Error', wx.OK | wx.ICON_ERROR)
                raise GUIException
        except ValueError:
            wx.MessageBox(_(u'Невалидна стойност!'), 'Error', wx.OK | wx.ICON_ERROR)

        except GUIException:
            wx.MessageBox(_(u'Неизвестна грешка!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            if self.edit == False:
                try:
                    self.grup[self.select]['level'][level_name] = {
                        'name':level_name,
                        'down':down,
                        'procent': procent,
                        'hiden':hiden,
                        'start_value':start_value,
                        'bet':bet,
                        'day_down':day_down,
                        'last_down': 0,
                        'min bet':min_bet,
                        'x2_time': {'from': '', 'to': ''},
                        }
                except UnboundLocalError:
                    self.grup[self.select]['level'][level_name] = {
                        'name':level_name,
                        'down':down,
                        'procent': procent,
                        'hiden':hiden,
                        'start_value':start_value,
                        'bet':bet,
                        'day_down':[-1,],
                        'last_down': 0,
                        'min bet':min_bet,
                        'x2_time': {'from': '', 'to': ''},
                        }
            else:
                # if 'down_value' in self.grup[self.edit]['level'][self.select]:
                #     if down['to']  <= self.grup[self.edit]['level'][self.select]['down_value']:
                #         wx.MessageBox(_(u'Крайната стойност на падане трябва да е по-голяма!'), 'Error', wx.OK | wx.ICON_ERROR)
                #         return
                try:
                    self.grup[self.edit]['level'][self.select]['down'] = down
                    self.grup[self.edit]['level'][self.select]['procent']= procent
                    self.grup[self.edit]['level'][self.select]['hiden'] = hiden
                    self.grup[self.edit]['level'][self.select]['start_value'] = start_value
                    self.grup[self.edit]['level'][self.select]['bet'] = bet
                    self.grup[self.edit]['level'][self.select]['day_down'] = day_down
                    self.grup[self.edit]['level'][self.select]['min bet'] = min_bet

                except UnboundLocalError:
                    self.grup[self.edit]['level'][self.select]['down'] = down
                    self.grup[self.edit]['level'][self.select]['procent']= procent
                    self.grup[self.edit]['level'][self.select]['hiden'] = hiden
                    self.grup[self.edit]['level'][self.select]['start_value'] = start_value
                    self.grup[self.edit]['level'][self.select]['bet'] = bet
                    self.grup[self.edit]['level'][self.select]['day_down'] = [-1]
                    self.grup[self.edit]['level'][self.select]['min bet'] = min_bet
            self.parent.GetParent().DB['smib'] = all_smib
            self.parent.GetParent().DB['group'] = self.grup
            self.Destroy()

    def OnFixFrame(self, event=None):
        select = self.m_choice4.GetSelection()
        if select == 0:
            self.m_checkBox1.Hide()
            self.m_checkBox2.Hide()
            self.m_checkBox3.Hide()
            self.m_checkBox4.Hide()
            self.m_checkBox5.Hide()
            self.m_checkBox6.Hide()
            self.m_checkBox7.Hide()
        else:
            self.m_checkBox1.Show()
            self.m_checkBox2.Show()
            self.m_checkBox3.Show()
            self.m_checkBox4.Show()
            self.m_checkBox5.Show()
            self.m_checkBox6.Show()
            self.m_checkBox7.Show()
        self.Fit()

    def OnRemoveProcent(self, event=None):
        self.m_staticText45.Hide()
        self.m_textCtrl28.Hide()
        self.Fit()

    def OnAddProcent(self, event=None):
        self.m_staticText45.Show()
        self.m_textCtrl28.Show()
        self.Fit()

    def OnClose(self, event):
        self.Destroy()

# class Rain(_gui.Rain):
#     def __init__(self, parent, grup, select, edit=False):
#         _gui.ClasicLevel.__init__(self, parent)
#         self.grup = grup
#         self.parent = parent
#         self.select = select
#         self.SetTitle(_(u'Нива'))
#         self.edit = edit
#
#     def OnClose(self, evt):
#         self.Destroy()

class EditVal(_gui.AddServer):
    def __init__(self, parent, val):
        _gui.AddServer.__init__(self, parent)
        self.val = val
        self.m_staticText60.SetLabel(_(u'Текуща стойност'))
        self.m_staticText61.Hide()
        self.m_textCtrl31.Hide()
        self.m_textCtrl30.SetValue(self.val)
        self.Layout()


    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        self.val = self.m_textCtrl30.GetValue()
        self.val = self.val.replace(',', '.')
        self.Destroy()

class DownOn(_gui.AddServer):
    def __init__(self, parent, group, level):
        self.parent = parent
        self.group = group
        self.level = level
        _gui.AddServer.__init__(self, parent)
        self.SetTitle(_(u"Падни на машина"))
        self.parent = parent
        self.m_staticText60.SetLabel(_(u"Номер на машина"))

        self.m_textCtrl30.SetToolTip(_(u"Попълнете свободен текст"))

        self.m_button29.SetLabel(_(u"Падни"))
        self.m_button28.SetLabel(_(u"Затвори"))
        self.m_staticText61.Hide()
        self.m_textCtrl31.Hide()
        self.Layout()
        
    def OnClose(self, event):
        self.Destroy()
        
    def OnGo(self, event):
        smib = self.m_textCtrl30.GetValue()
        dlg = wx.MessageBox(u'Изчакайте докато прозореца стане активен!\nGroup "%s" Level "%s" EMG "%s"' % (
        self.group, self.level, smib), 'Info',
                            wx.YES_NO | wx.ICON_QUESTION)

        if dlg == wx.NO:
            return False

        for i in self.parent.GetParent().DB['smib']:
            if smib == self.parent.GetParent().DB['smib'][i]['licenz']:
                smib = i
                break
        response = libs.udp.send('DOWN_ON', smib=smib, level=self.level, grup=self.group, ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, timeout=50)
        if response == True:
            wx.MessageBox(_(u'Успешно!'), 'Info', wx.OK | wx.ICON_INFORMATION)
            self.OnClose(event)
        elif response == 'CHECK':
            wx.MessageBox(_(u'Проверете дали операцията е успешна!\n Отключете сървъра от бутона ПУСНИ'), 'Info', wx.OK | wx.ICON_ERROR)
            self.OnClose(event)
        else:
            wx.MessageBox(_(u'Грешка!'), 'Error', wx.OK | wx.ICON_ERROR)
        self.OnClose(None)
        
class Group(_gui.AllDial):

    def __init__(self, parent):
        _gui.AllDial.__init__(self, parent)
        self.SetTitle(_(u'Джакпоти'))
        self.parent = parent
        self.m_button_add.SetLabel(_(u'Дабави'))
        self.m_button_add.Show()
        self.m_button_add.SetToolTip(_(u"Добавяне на група!"))
        self.m_treeCtrl2.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.ItemMod)

        
        if libs.conf.DOWNSELECT == True:
            self.m_button_edit.SetLabel(_(u'Падни'))
            self.m_button_edit.Show()
            self.m_button_edit.Bind( wx.EVT_BUTTON, self.down_on )
        
        self.m_button_help.SetLabel(_(u'Помощ'))
        self.m_button_help.Show()
        self.m_button_help.SetToolTip(_(u"Изваждане на помощ за текущия прозорец!"))


        self.m_button_close.SetLabel(_(u'Затвори'))
        self.m_button_close.Show()
        self.m_button_close.SetToolTip(_(u"Затваряне на текущия прозорец!"))

        self.m_treeCtrl2.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.RightMenu)
        self.add_tree_item()
        self.m_treeCtrl2.SetToolTip(_(u"Списък със съществуващите групи!"))

        self.Fit()

    def _group_menu(self):
        menu = [_(u'Редактирай група'),
                _(u'Добави визуализация'),
                _(u'Добави ниво'),
                _(u'Добави машини'),
                _(u'Изтрий Група'),
                ]
        return menu

    def _item_menu(self):
        menu = [_(u'Редактирай'), _(u'Изтрий')]
        return menu

    def _add_visual(self):
        """
        Отваря врейм за добавяне на визуализации към групи
        ползва се в GrupMod функцията
        """
        frame = AddDevisToGrup(self, self.select, 'visual')
        frame.ShowModal()
        self.refresh_tree()


    def _add_level(self):
        """
        Отваря фрейм за добавяне на нива към групи
        ползва се в GrupMod функцията
        """
        
        if self.jp_group[self.select]['game_type'] == 0:
            if len(self.jp_group[self.select]['level']) < 5:
                frame = ClasicGame(self, self.jp_group, self.select)
            else:
                wx.MessageBox(_(u'Максималния брой нива е 5!'), 'Error', wx.OK | wx.ICON_ERROR)
        elif self.jp_group[self.select]['game_type'] == 1:
            if self.jp_group[self.select]['hiden_visual'] == False:
                if len(self.jp_group[self.select]['level']) < 2:
                    frame = TimeGame(self, self.jp_group, self.select)
                else:
                    wx.MessageBox(_(u'Максималния брой нива е 2!'), 'Error', wx.OK | wx.ICON_ERROR)
            else:
                frame = TimeGame(self, self.jp_group, self.select)
        try:
            frame.ShowModal()
            self.refresh_tree()
        except UnboundLocalError:
            pass

    def _add_machine(self):
        """
        Отваря фрейм за добавяне на машини към групи
        ползва се в GrupMod функцията
        """
        frame = AddDevisToGrup(self, self.select, 'mashin')
        frame.ShowModal()
        self.refresh_tree()

    def _dell_group(self):
        """
        Изтрива дадена група от групи
        ползва се в GrupMod функцията
        """

        visual = self.parent.DB['visual']
        smib = self.parent.DB['smib']
        grup = self.parent.DB['group']
        pr = 0
        for item in grup:
            for b in grup[item]['level']:
                pr = pr + grup[item]['level'][b]['procent'] + grup[item]['level'][b]['hiden']
        for item in visual:
            if self.select == visual[item]['group']:
                visual[item]['group'] = _(u'Свободни')
        for item in smib:
            try:
                var = smib[item]['group'].index(self.select )
                del smib[item]['group'][var]
            except ValueError:
                pass

            smib[item]['procent'] = smib[item]['procent'] - pr
        # if self.select in self.parent.DB['go_down']:
        #     del self.parent.DB['go_down'][self.select]
        self.parent.DB['visual'] = visual
        self.parent.DB['smib'] = smib
        del self.parent.DB['group'][self.select]
#         print  self.parent.DB['go_down'].keys()
        try:
            del self.parent.DB['go_down'][self.select]
        except KeyError:
            pass
#         print  self.parent.DB['go_down'].keys()
        self.refresh_tree()

    def OnDel(self, event):
        self.select = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        if self.select not in self.jp_group:
            wx.MessageBox(_(u'Моля изберете група за изтриване!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            self._dell_group()
        return True

    def _edit_level(self):
        """
        Отваря фрейм за редакция на ниво на дадена група
        ползва се в ItemMod функцията
        """
        if self.jp_group[self.grup]['game_type'] == 0:
            frame = ClasicGame(self, self.jp_group, self.select, edit=self.grup)
        else:
            frame = TimeGame(self, self.jp_group, self.select, edit=self.grup)
        frame.ShowModal()
        self.refresh_tree()

    def _dell_visual(self):
        """
        Итрива визуализация от дадена група
        ползва се в ItemMod функцията
        """

        if len(self.jp_group[self.grup]['visual']) > 1:
            del self.jp_group[self.grup]['visual'][self.select]
            self.parent.DB['visual'][self.select]['group'] = _(u'Свободни')
            self.parent.DB['group'] = self.jp_group
            wx.MessageBox(_(u'Успешно премахната визуализация!'), 'Info', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(_(u'Групата не може да остане без визуализация!'), 'Error', wx.OK | wx.ICON_ERROR)
        self.refresh_tree()

    def _dell_level(self):
        """
        Изтрива ниво от дадена група
        ползва се в ItemMod функцията
        """
        pr = (self.jp_group[self.grup]['level'][self.select]['procent'] + 
              self.jp_group[self.grup]['level'][self.select]['hiden'])
        smib = self.parent.DB['smib']
        for item in smib:
            if self.grup in smib[item]['group']:
                smib[item]['procent'] = smib[item]['procent'] - pr
        try:
            if self.select in self.parent.DB['go_down'][self.grup]:
                self.parent.DB['go_down'][self.grup] = False
        except KeyError:
            pass
        except TypeError:
            pass
        del self.jp_group[self.grup]['level'][self.select]
                
        self.parent.DB['group'] = self.jp_group
        self.parent.DB['smib'] = smib
        wx.MessageBox(_(u'Успешно премахнато ниво!'), 'Info', wx.OK | wx.ICON_INFORMATION)
        self.refresh_tree()

    def RightMenu(self, event):
        item = event.GetItem()
        self.select = self.m_treeCtrl2.GetItemText(item)
        self.popupmenu = wx.Menu()
        if self.select not in self.jp_group:
            if self.select != _(u'Визуализация') and self.select!= _(u'Нива'):
                item = self.m_treeCtrl2.GetSelection()
                parent = self.m_treeCtrl2.GetItemParent(item)
                self.order = self.m_treeCtrl2.GetItemText(parent)
                parent = self.m_treeCtrl2.GetItemParent(parent)
                self.grup = self.m_treeCtrl2.GetItemText(parent)
                
                self.func = self._item_menu()
                
                for text in self.func:
                    item = self.popupmenu.Append(-1, text)
                    self.Bind(wx.EVT_MENU, self.ItemMod, item)
        else:

            self.func = self._group_menu()
            for text in self.func:
                item = self.popupmenu.Append(-1, text)
                self.Bind(wx.EVT_MENU, self.GrupMod, item)
        self.PopupMenu(self.popupmenu, event.GetPoint())

    def GrupMod(self, event):
        """
        Отваря фрейм за опциите с десен бутон в групи
        """
        item = self.popupmenu.FindItemById(event.GetId())
        text = item.GetText()
        if text == _(u'Добави визуализация'):
            self._add_visual()
        else:
            if text == _(u'Добави ниво'):
                self._add_level()
        if text == _(u'Добави машини'):
            self._add_machine()
        if text == _(u'Изтрий Група'):
            self._dell_group()
        if text == _(u'Редактирай група'):
            self._grup_edit()
    
    def _grup_edit(self):
#         pr = self.parent.DB['group'][self.select]['real_down_procent']
        if self.parent.DB['group'][self.select]['game_type'] == 0:
            dial = ClasicGroupConfig(self, self.select)
            dial.ShowModal()
        elif self.parent.DB['group'][self.select]['game_type'] == 1:
            dial = TimeGroupConfig(self, self.select)
            dial.ShowModal()

    def edit_visual(self):
        from .visual import VisualIP
        frame = VisualIP(self, self.grup, self.select)
        frame.ShowModal()
        self.refresh_tree()
    
    def _dell_smib(self, mashin):
        dlg = wx.MessageBox(_(u'Искате ли да изтриете машината') + '\n'
                            + _(u'Промените ще влязат в сила незабавно!'), 'Info',
                            wx.YES_NO | wx.ICON_QUESTION)
        
        
        if dlg == wx.YES:
            all_grup = self.parent.GetParent().DB['group']
            ip = mashin
            response = libs.udp.send('EBABLE_JP_MOD', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, work_mod=None)
            if not response:
                dlg = wx.MessageBox(_(u'Грешен IP адрес! Или липсва връзка с машината!'), 'Error', wx.OK | wx.ICON_ERROR)
            else:
                # for i in all_grup:
                #     try:
                #         del all_grup[i]['mashin'][ip]
                #     except KeyError:
                #         pass
                try:
                    del self.parent.GetParent().DB['smib'][ip]
                except KeyError:
                    wx.MessageBox(_(u'Моля изберете машина'),'Info', wx.OK | wx.ICON_ERROR)
                self.parent.GetParent().DB['grup'] = all_grup
                self.refresh_tree()
                
    def ItemMod(self, event):
        """
        Отваря фрейм за опциите с десен бутон за итемите в групите
        """
        try:
            item = self.popupmenu.FindItemById(event.GetId())
            text = item.GetText()
        except AttributeError:
            try:
                item = event.GetItem()
                self.select = self.m_treeCtrl2.GetItemText(item)
                if self.select != _(u'Визуализация') and self.select!= _(u'Нива'):
                    item = self.m_treeCtrl2.GetSelection()
                    parent = self.m_treeCtrl2.GetItemParent(item)
                    self.order = self.m_treeCtrl2.GetItemText(parent)
                    parent = self.m_treeCtrl2.GetItemParent(parent)
                    self.grup = self.m_treeCtrl2.GetItemText(parent)
                    text = _(u'Редактирай')
            except wx._core.PyAssertionError:
                return
        if text == _(u'Редактирай'):
            if self.order == _(u'Визуализация'):
                self.edit_visual()
            elif self.order == _(u'Нива'):
                self._edit_level()
            elif self.order == _(u'Машини'):
                frame = smib.EditSMIB(self, self.parent.GetParent().DB['smib'][self.select])
                frame.ShowModal()
            
        if text == _(u'Изтрий'):
            if self.order == _(u'Визуализация'):
                self._dell_visual()
            elif self.order == _(u'Нива'):
                self._dell_level()
            elif self.order == _(u'Машини'):
                self._dell_smib(self.select)


    def add_tree_item(self):
        self.root = self.m_treeCtrl2.AddRoot('group')
        self.jp_group = list(self.parent.DB['group'].keys())
        object = {}
        for item in self.jp_group:
            object[item] = self.m_treeCtrl2.AppendItem(self.root, item)
        self.jp_group = self.parent.DB['group']
        my_level = []
        for item in self.jp_group:

            visual = self.m_treeCtrl2.AppendItem(object[item], _(u'Визуализация'))
            all_level = self.m_treeCtrl2.AppendItem(object[item], _(u'Нива'))
            my_level.append(all_level)
            smib = self.m_treeCtrl2.AppendItem(object[item], _(u'Машини'))
            all_visual = self.parent.DB['visual']
            if self.jp_group[item]['hiden_visual'] == True:
                for i in self.jp_group[item]['visual']:
                    self.m_treeCtrl2.AppendItem(visual, i)
            else:
                for i in sorted(list(all_visual.keys())):
                    if item in all_visual[i]['group']:
                        self.m_treeCtrl2.AppendItem(visual, i)
            # for visual_in_grup in self.jp_group[item]['visual']:
            #     self.m_treeCtrl2.AppendItem(visual, visual_in_grup)
            for level in self.jp_group[item]['level']:
                self.m_treeCtrl2.AppendItem(all_level, level)
            all_smib = self.parent.DB['smib']
            for i in sorted(list(all_smib.keys())):
                if item in all_smib[i]['group']:
                    self.m_treeCtrl2.AppendItem(smib, i)
        self.m_treeCtrl2.CollapseAll()

        for item in self.jp_group:
            self.m_treeCtrl2.Expand(object[item])
        for item in my_level:
            self.m_treeCtrl2.Expand(item)
        # for item in object:
        # self.m_treeCtrl2.Expand(self.root)
        # self.m_treeCtrl2.Expand(all_level)

    def refresh_tree(self):
        self.m_treeCtrl2.DeleteAllItems()
        self.add_tree_item()

    def OnAdd( self, event ):
        frame = AddName(self)
        frame.ShowModal()
        self.refresh_tree()

    def OnHelp(self, event):
        if libs.conf.DOCS_DEBUG == False:
            frame = libs.helps.Help(r'%s%s/colibri/v%s/jackpot.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE, libs.conf.VERSION))
        else:
            frame = libs.helps.Help('http://127.0.0.1:5000/%s/colibri/v%s/jackpot.html' % (libs.conf.USE_LANGUAGE, libs.conf.VERSION))

    def down_on(self, event):
        
        
        try:
            self.select = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
            if self.select == _(u'Машини') or self.select == _(u'Визуализация') or self.select == _(u'Нива'):
                raise KeyError
            item = self.m_treeCtrl2.GetSelection()
            parent = self.m_treeCtrl2.GetItemParent(item)
            self.order = self.m_treeCtrl2.GetItemText(parent)
            if self.order == _(u'Нива'):
                parent = self.m_treeCtrl2.GetItemParent(parent)
                self.grup = self.m_treeCtrl2.GetItemText(parent)
#                 print self.parent.DB['group'][self.grup]
                if self.parent.DB['group'][self.grup]['game_type'] != 0:
                    raise ValueError
                elif self.parent.DB['group'][self.grup]['level'][self.select]['bet'] != False:
                    raise ValueError
            else:
                raise KeyError
        except KeyError:
            wx.MessageBox(_(u'Моля изберете ниво'),'Info', wx.OK | wx.ICON_ERROR)
        except ValueError:
            wx.MessageBox(_(u'Само класически нива'),'Info', wx.OK | wx.ICON_ERROR)
        except:
            wx.MessageBox(_(u'Невалидни данни'),'Info', wx.OK | wx.ICON_ERROR)
        else:
            level = self.select
            group = self.grup
            dial = DownOn(self, group, level)
            dial.ShowModal()
    
    def OnClose( self, event ):
        self.DestroyChildren()
        self.Destroy()

if __name__=='__main__':
    app = wx.App()
    frame = AddDevisToGrup(None, 'test', 0)
    frame.Show()
    app.MainLoop()


