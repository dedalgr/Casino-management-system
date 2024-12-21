#-*- coding:utf-8 -*-
'''
Created on 21.10.2017 г.

@author: dedal
'''

import wx
import libs  # @UnresolvedImport
import gui_lib  # @UnresolvedImport
from . import gui
import os

class MexEdit(gui.MexEdit, gui_lib.keybords.Keyboard):
    def __init__(self, parent, index):
        self.parent = parent
        
        self.index = index
        gui.MexEdit.__init__(self, parent)
        self.width, self.height = wx.GetDisplaySize()
        # print gui_lib.msg.order_mex_chk_MexEdit_name + u': ' + str(self.parent.mashin[self.index].nom_in_l)
        self.SetTitle(gui_lib.msg.order_mex_chk_MexEdit_name + u': ' + str(self.parent.mashin[self.index].nom_in_l))
        self.m_button10.SetLabel(gui_lib.msg.order_mex_chk_MexEdit_button['m_button10'])
        self.m_button11.SetLabel(gui_lib.msg.order_mex_chk_MexEdit_button['m_button11'])
        self.m_staticText12.SetLabel(gui_lib.msg.order_mex_chk_MexEdit_text['m_staticText12'])
        self.m_staticText13.SetLabel(gui_lib.msg.order_mex_chk_MexEdit_text['m_staticText13'])
        self.SetSize((self.width*0.3, -1))
        self.m_textCtrl4.SetMinSize((self.width*0.3, -1))
        self.m_textCtrl5.SetMinSize((self.width*0.3, -1))
        self.m_textCtrl4.SetValue(str(self.parent.mashin[self.index].mex_in))
        self.m_textCtrl5.SetValue(str(self.parent.mashin[self.index].mex_out))
        self.editet = False
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl4.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl5.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
        self.SetMinSize((350, 250))
        self.Fit()
        
    def OnGo(self, event):
        self.editet = True
        self.parent.mashin[self.index].mex_in = int(self.m_textCtrl4.GetValue())
        self.parent.mashin[self.index].mex_out = int(self.m_textCtrl5.GetValue())
        self.Destroy()
        
    def OnClose(self, event):
        self.Destroy()
        
class MexCheck(gui.MexCheck):
    def __init__(self, parent):
        self.parent = parent
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.order_mex_chk_MexCheck_name[1])
        gui.MexCheck.__init__(self, parent)
        self.Bind( wx.EVT_SIZE, self.on_resize )
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
#         self.width, self.height = wx.GetDisplaySize()
#         self.SetSize((self.width, self.height))
        self.m_listCtrl6.SetToolTip(gui_lib.msg.order_mex_chk_MexCheck_tooltip['m_listCtrl6'])
        self.m_button9.SetLabel(gui_lib.msg.order_mex_chk_MexCheck_button['m_button9'])
        self.m_button7.SetLabel(gui_lib.msg.order_mex_chk_MexCheck_button['m_button7'])
        self.m_button8.SetLabel(gui_lib.msg.order_mex_chk_MexCheck_button['m_button8'])
        self.m_listCtrl6.InsertColumn(0, gui_lib.msg.order_mex_chk_MexCheck_text[1])
        
        self.m_listCtrl6.InsertColumn(1, gui_lib.msg.order_mex_chk_MexCheck_text[2])
        
        self.m_listCtrl6.InsertColumn(2, gui_lib.msg.order_mex_chk_MexCheck_text[3])
        
        self.m_listCtrl6.InsertColumn(3, gui_lib.msg.order_mex_chk_MexCheck_text[4])
        
        self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, order='nom_in_l')
        for i in self.mashin:
            i.editet = False
        self._tree_add()
        
#             self.Center()
#         if libs.conf.FULSCREEAN is True:
#             self.SetWindowStyle(wx.STAY_ON_TOP)
        self.on_resize(None)
        # self.Layout()
    
    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height*0.95))
        self.m_listCtrl6.SetMinSize((self.width*0.90, self.height*0.90))
        self.m_listCtrl6.SetColumnWidth(0, self.width * 0.1)
        self.m_listCtrl6.SetColumnWidth(1, self.width * 0.30)
        self.m_listCtrl6.SetColumnWidth(2, self.width * 0.18)
        self.m_listCtrl6.SetColumnWidth(3, self.width * 0.18)
        if event != None:
            self.Layout()
            event.Skip()

        
        
    def _tree_add(self):
        
        index=0
#         self.mashinDict = {}
        for item in self.mashin:
            self.m_listCtrl6.InsertItem(index, str(item.nom_in_l))
            self.m_listCtrl6.SetItem(index, 1, str(item.model.name))
            self.m_listCtrl6.SetItem(index, 2, str(item.mex_in))
            self.m_listCtrl6.SetItem(index, 3, str(item.mex_out))
            if item.editet is True:
                self.m_listCtrl6.SetItemTextColour(item=index, col=wx.Colour(199, 16, 29))
            else:
                self.m_listCtrl6.SetItemTextColour(item=index, col=wx.Colour(0, 135, 11))
#             self.mashinDict[index] = item
            index += 1
            
        
    def tree_refresh(self):
        self.m_listCtrl6.DeleteAllItems()
        self._tree_add()
        
    def OnEdit(self, event):
        # print()
        curentIndex = event.GetIndex()
        dialog = MexEdit(self, curentIndex)
        dialog.ShowModal()
        self.mashin[curentIndex].editet = dialog.editet
        self.tree_refresh()
        
        
    def OnClose(self, event):
        self.parent.show_panel()
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.order_mex_chk_MexCheck_name[2])
        self.Destroy()
        
    def OnGo(self, event):
        for i in self.mashin:
            libs.DB.add_object_to_session(i)
        try:
            libs.DB.commit()
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_OK)
            dial.ShowModal()
            # self.tree_refresh()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
        
    def OnPrint(self, event):
        data = {'row':{}}
        for i in self.mashin:
            data['row'][i.nom_in_l] = {'in':i.mex_in, 'out':i.mex_out}
        gui_lib.printer.Print( self, 'mex_chk.html' ,data)
        if libs.conf.PRINT_DIRECT is True:
            dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_OK)
            dlg.ShowModal()
