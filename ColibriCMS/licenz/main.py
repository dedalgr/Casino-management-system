#-*- coding:utf-8 -*-
import wx
from . import gui
import libs
import gui_lib
import os
import pickle
import json

class Active(gui.Activ):
    def __init__(self, parent):
        #         width, height = wx.GetDisplaySize()
        gui.Activ.__init__(self, parent)  # @UndefinedVariable
        self.parent = parent
        self.SetTitle(gui_lib.msg.licenz_main_Active_name)
        self.m_staticText1.SetLabel(gui_lib.msg.licenz_main_Active_text['m_staticText1'])
        self.m_staticText2.SetLabel(gui_lib.msg.licenz_main_Active_text['m_staticText2'])
        self.m_filePicker1.SetToolTip(gui_lib.msg.licenz_main_Active_tooltip['m_filePicker1'])
        get_base_code = libs.udp.send('get_soft_id', ip=libs.conf.SERVER)
        if get_base_code == None:
            get_base_code = gui_lib.msg.licenz_main_Active_text[1]
        # print get_base_code
        self.close = False
        self.m_textCtrl1.SetValue(get_base_code)

    def OnClose( self, event ):
        self.close = True
        self.Destroy()

    def OnGo( self, event ):
        tmp = open(self.m_filePicker1.GetPath(), 'rb')
        my_key = pickle.load(tmp)
        tmp.close()
        # my_key = shelve.open()
        signature = my_key['signature']
        data = my_key['data']
        response = None
        for i in range(3):
            if response is True:
                break
            else:
                response = libs.udp.send('mod_active', ip=libs.conf.SERVER, data=data,
                                         signature=signature)
        if response is True:
            data = json.loads(data)
            obj = libs.DB.get_one_where(libs.models.LN, name=data['name'])
            if obj == None:
                obj = libs.DB.make_obj(libs.models.LN)
                obj.name = data['name']
            obj.value = my_key['data']
            obj.signature = signature
            libs.DB.add_object_to_session(obj)
            try:
                libs.DB.commit()
            except Exception as e:
                libs.DB.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                return
            dial = wx.MessageDialog(self, *gui_lib.msg.ACTIVE_OK)
            dial.ShowModal()
            if self.parent != None:
                self.parent.GetParent().all_ln = libs.chk_license()
            self.OnClose(event)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()

class Licenz(gui.LicenzPanel):  # @UndefinedVariable
    def __init__(self, parent):
#         width, height = wx.GetDisplaySize()
        gui.LicenzPanel.__init__(self, parent)  # @UndefinedVariable
        self.parent = parent
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.licenz_main_Licenz_name)
        # print gui_lib.msg.licenz_main_Licenz_name
        self.m_listCtrl1.SetToolTip(gui_lib.msg.licenz_main_Licenz_tooltip['m_listCtrl1'])
        self.width, self.height = self.parent.GetSize()
        self.Bind( wx.EVT_SIZE, self.on_resize )
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)

#         self.m_listCtrl1 = wx.SortableListCtrl(self)

        self.m_listCtrl1.InsertColumn(0, gui_lib.msg.licenz_main_Licenz_text[2])
        self.m_listCtrl1.InsertColumn(1, gui_lib.msg.licenz_main_Licenz_text[3])
        self.m_listCtrl1.InsertColumn(2, gui_lib.msg.licenz_main_Licenz_text[4])

        self.m_listCtrl1.Arrange()
        self.load_data()
        self._add_toll()
        self.on_resize(None)

    def load_data(self):
        all_ln = libs.DB.get_all(libs.models.LN)
        index = 0
        self.licenseDict = {}
        for i in all_ln:
            self.m_listCtrl1.InsertItem(index, str(i.id))
            self.m_listCtrl1.SetItem(index, 1, str(i.name))
            self.m_listCtrl1.SetItem(index, 2, str(json.loads(i.value)['end_time']))
            self.licenseDict[index] = i
            index += 1

    def list_refresh(self):
        self.m_listCtrl1.DeleteAllItems()
        self.load_data()

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        self.m_listCtrl1.SetMinSize((self.width*0.95, self.height*0.75))
        self.m_toolBar1.SetMinSize((self.width, -1))
        self.m_listCtrl1.SetColumnWidth(1, self.width*0.40)
        self.m_listCtrl1.SetColumnWidth(2, self.width*0.40)
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height*0.95))
        if event != None:
            event.Skip()
            self.Layout()

    def OnClose(self, event):
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.config_BonusCart['name'][1])
        self.parent.OnConfig(None)
        self.Destroy()

    def _add_toll(self):
        self.m_toolBar1.ClearTools()
        self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, gui_lib.msg.licenz_main_Licenz_button['m_tool3'], wx.Bitmap( libs.conf.IMG_FOLDER + u"64x64/xarchiver-add.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, gui_lib.msg.licenz_main_Licenz_tooltip['m_tool3'], wx.EmptyString, None )
        self.m_tool4 = self.m_toolBar1.AddTool( wx.ID_ANY, gui_lib.msg.licenz_main_Licenz_button['m_tool4'], wx.Bitmap( libs.conf.IMG_FOLDER + u"64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, gui_lib.msg.licenz_main_Licenz_tooltip['m_tool4'], wx.EmptyString, None )
        self.Bind( wx.EVT_CLOSE, self.OnClose )
        self.Bind( wx.EVT_TOOL, self.OnAdd, id = self.m_tool3.GetId() )
        self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool4.GetId() )
        self.m_toolBar1.Realize()

    def OnAdd(self, event):
        dial = Active(self)
        dial.ShowModal()
        self.list_refresh()

    def OnCheck( self, event ):
        my_license = self.licenseDict[self.m_listCtrl1.GetFirstSelected()]
        signature = my_license.signature
        data = my_license.value
        response = libs.udp.send('license_chk', ip=libs.conf.SERVER, data=data, signature=signature)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.ACTIVE_OK)
            dial.ShowModal()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.LICENSE_END_TIME)
            dial.ShowModal()




