#-*- coding:utf-8 -*-
"""Subclass of User, which is generated by wxFormBuilder."""

import wx
from . import _gui  # @UnresolvedImport
import libs  # @UnresolvedImport
from .activ import Activ  # @UnresolvedImport
# import __builtin__  # @UnusedImport
from .main_gui import Main  # @UnresolvedImport
# import helps  # @UnusedImport @UnresolvedImport
        
class Login(_gui.Login):
    def __init__(self, parent):
        _gui.Login.__init__(self, parent)
        self.parent = parent
        self.SetTitle(_(u'Вход'))
        self.m_staticText7.SetLabel(_(u'Потребител'))
        self.m_textCtrl7.SetToolTip(_(u"Въведете потребителско име!"))
        self.m_staticText8.SetLabel(_(u'Парола'))
        self.m_textCtrl8.SetToolTip(_(u"Въведете парола!"))
        
    # Handlers for Login events.
    def OnClose(self, event):
#         udp.send('STOP_ROTATION', command=False)
        self.Destroy()

    def OnGo(self, event):
        user = self.m_textCtrl7.GetValue()
        passwd = self.m_textCtrl8.GetValue()
        response =  libs.udp.send('LOGIN', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, user=user, passwd=passwd)
        if response == True:
#             udp.send('STOP_ROTATION', command=True)
#             if user == 'root':
#                 frame = AddUser(self)
#                 frame.ShowModal()
#                 self.m_textCtrl7.SetValue('')
#                 self.m_textCtrl8.SetValue('')
#                 self.m_textCtrl7.SetFocus()
#             else:
#                 __builtin__.USER = user
            self.Hide()
            frame = Main(self)
            frame.ShowModal()
            self.m_textCtrl7.SetValue('')
            self.m_textCtrl8.SetValue('')
            self.m_textCtrl7.SetFocus()
        elif response == False:
            wx.MessageBox(_(u'Грешен потребител или парола!'), 'Error', wx.OK | wx.ICON_ERROR)
        elif response ==  None:
            wx.MessageBox(_(u'Няма връзка със сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
        elif response[0] == 'ACTIV':
#             self.Hide()
            frame = Activ(self)
            frame.m_textCtrl1.SetValue(response[1])
            frame.ShowModal()
            self.m_textCtrl7.SetValue('')
            self.m_textCtrl8.SetValue('')
            self.m_textCtrl7.SetFocus()
        else:
            wx.MessageBox(_(u'Невалидна команда!'), 'Error', wx.OK | wx.ICON_ERROR)


# Implementing AddUser
class AddUser( _gui.AddUser ):
    def __init__( self, parent ):
        _gui.AddUser.__init__( self, parent )
        self.parent = parent
        self.SetTitle(_(u'Добави потребител'))
        self.m_staticText5.SetLabel(_(u'Потребител:'))
        self.m_textCtrl5.SetToolTip(_(u"Въведете пoтребител!"))
        self.m_staticText6.SetLabel(_(u'Име:'))
        self.m_textCtrl6.SetToolTip(_(u"Въведете пълно име и фамилия разделени с интервал!"))
        self.m_staticText7.SetLabel(_(u'Парола:'))
        self.m_textCtrl7.SetToolTip(_(u"Въведете парола!"))
        self.m_staticText8.SetLabel(_(u'Парола:'))
        self.m_textCtrl8.SetToolTip(_(u"Въведете парола отново!"))

    # Handlers for AddUser events.
    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        username = self.m_textCtrl5.GetValue()
        name = self.m_textCtrl6.GetValue()
        passwd = self.m_textCtrl7.GetValue()
        chk_passwd = self.m_textCtrl8.GetValue()
        
#         self.response = udp.send('ALL_USER')
#         if self.response  == None:
#             dlg = wx.MessageBox(_(u'Няма връзка със сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
#         else:
#         if 'root' in self.parent.GetParent().DB['users']:
#                 response = udp.send('DEL_USER', user='root')
#             del self.parent.GetParent().DB['users']['root']
#                 if response == False:
#                     wx.MessageBox(_(u'Неуспешно деактивиране на root!'), 'Error', wx.OK | wx.ICON_ERROR)
        if passwd != chk_passwd:
            wx.MessageBox(_(u'Паролите не съвпадат!'), 'Error', wx.OK | wx.ICON_ERROR)
        elif username in  self.parent.GetParent().DB['users']:
            wx.MessageBox(_(u'Потребителят съществува!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
#             response = udp.send('ADD_USER', user=username, name=name, passwd=passwd )
            self.parent.GetParent().DB['users'][username] = {'user':username, 'name':name, 'passwd':passwd}
#             self.parent.GetParent().DB['users'][username] =
            
            
#             if response == True:
#                 if 'root' in self.response:
#                     DB = udp.send('GET_DB')
#                     if DB == None:
#                         dlg = wx.MessageBox(_(u'Няма връзка със сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
#                     else:
#                         
#                     wx.MessageBox(_(u'Моля рестартирайте програмата!'), 'Info', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
#             else:
#                 wx.MessageBox(_(u'Неуспешно добавяне на потребител!'), 'Error', wx.OK | wx.ICON_ERROR)
        
        self.m_staticText5.SetLabel(_(u'Потребител:'))
        self.m_staticText6.SetLabel(_(u'Име:'))
        self.m_staticText7.SetLabel(_(u'Парола:'))
        self.m_staticText8.SetLabel(_(u'Парола:'))



class User(_gui.AllDial):
    def __init__(self, parent):
        _gui.AllDial.__init__(self, parent)
        self.SetTitle(_(u"Потребители"))
        self.parent = parent
        self.m_button_add.SetLabel(_(u"Добави"))
        self.m_button_add.Show()
        self.m_button_add.SetToolTip(_(u"Добавяне на потребител!"))

        self.m_button_del.SetLabel(_(u"Изтрий"))
        self.m_button_del.Show()
        self.m_button_del.SetToolTip(_(u"Изтриване на потребител!"))

        self.m_button_help.SetLabel(_(u"Помощ"))
        self.m_button_help.Show()
        self.m_button_help.SetToolTip(_(u"Изваждане на помощ за текущия прозорец!"))

        self.m_button_close.SetLabel(_(u"Затвори"))
        self.m_button_close.Show()
        self.m_button_close.SetToolTip(_(u"Затваряне на текущия прозорец!"))

        self.Fit()
        self.add_tree_item()


    def add_tree_item(self):
        self.users = self.m_treeCtrl2.AddRoot(_(u'Потребители'))
        self.m_treeCtrl2.SetToolTip(_(u'Списък с текущите потребители'))
#         self.response = udp.send('ALL_USER')
        for item in self.parent.DB['users']:
            if item != 'MistralCMS':
                self.m_treeCtrl2.AppendItem(self.users, item.encode('utf-8'))
        self.m_treeCtrl2.ExpandAll()

    def tree_refresh(self):
        self.m_treeCtrl2.DeleteAllItems()
        self.add_tree_item()


    def OnClose(self, event):
        self.Destroy()

    def OnAdd(self, event):
        frame = AddUser(self)
        frame.ShowModal()
        self.tree_refresh()

    def OnDel(self, event):
        user =  self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        if user in self.parent.DB['users']:
            dlg = wx.MessageBox(_(u'Искате ли да изтриете потребителя') + '\n'
                                + _(u'Промените ще влязат в сила незабавно!'), 'Info',
                                wx.YES_NO | wx.ICON_QUESTION)
            if dlg == wx.YES:
#                 udp.send('DEL_USER', user=user)
                del self.parent.DB['users'][user]
                self.tree_refresh()
        else:
            wx.MessageBox(_(u'Неуспешно премахване на потребител!'), 'Error', wx.OK | wx.ICON_ERROR)

    def OnHelp(self, event):
        if libs.conf.DOCS_DEBUG == False:
            frame = libs.helps.Help(r'%s%s/colibri/v%s/jackpot.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE, libs.conf.VERSION))
        else:
            frame = libs.helps.Help('http://127.0.0.1:5000/%s/colibri/v%s/jackpot.html' % (libs.conf.USE_LANGUAGE, libs.conf.VERSION))
