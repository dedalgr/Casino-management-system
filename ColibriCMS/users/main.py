#-*- coding:utf-8 -*-
'''
Created on 31.05.2017 г.

@author: dedal
'''
import wx
from . import gui
# import db_ctrl  # @UnresolvedImport
import libs  # @UnresolvedImport
from . import task  # @UnusedImport @UnresolvedImport
import gui_lib  # @UnresolvedImport
# import __builtin__
import os
import datetime
# from __init__ import RIGHT  # @UnresolvedImport

# if libs.conf.DEBUG is True:
#     parent_frame = gui.TestDialog  # @UndefinedVariable
# else:
#     parent_frame = gui.UserConf  # @UndefinedVariable


class AddCart(gui.AddCart):  # @UndefinedVariable
    def __init__(self, parent):
        self.parent = parent
        gui.AddCart.__init__(self, parent)  # @UndefinedVariable
        self.SetTitle(gui_lib.msg.users_main_AddCart_name)
        self.m_staticText13.SetLabel(gui_lib.msg.users_main_AddCart_text['Text13'])
        self.user= self.parent.GetParent().GetParent().USER
#         self.worker = task.RFIDWork(self)  # @UndefinedVariable
        self.m_button8.SetLabel(gui_lib.msg.users_main_AddCart_button['button8'])
        self.m_button7.SetLabel(gui_lib.msg.users_main_AddCart_button['button7'])
#         try:
#         self.cart = []
        if self.parent.GetParent().GetParent().login.worker:
            self.parent.GetParent().GetParent().rfid_bind(self)
        else:
            self.worker = task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)  # @UndefinedVariable
            task.EVT_WORK_RFID_RESULT(self, self.OnCard)

    def OnCard(self, event):
        if event.data == None or event.data == self.user.cart or event.data is False:
            pass
        elif event.data == 'ERROR':
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_RFID)
            dial.ShowModal()
            self.OnTaskStop(None)
        else:
            if libs.DB.get_one_where(libs.models.User, cart=event.data) == None:
#                   print(e)vent.data
                self.parent.cart_id = event.data
                self.m_staticText13.SetLabel(gui_lib.msg.users_main_AddCart_text['remove_cart'])
                self.m_button8.SetLabel(gui_lib.msg.users_main_AddCart_button['button8'])
                self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
    #                     self.m_button8.Show()
            else:
                        
                self.m_staticText13.SetLabel(gui_lib.msg.users_main_AddCart_text['cart_in_use'])
#                     self.m_button8.Show()
        self.Fit()
        
    def OnDelCart(self, event):
        self.parent.cart_id = None
        self.OnClose(event)


    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.parent.GetParent().GetParent().login.worker:
            self.parent.GetParent().GetParent().rfid_unbind()
            return
        try:
#         if self.worker:
            self.worker.abort()
        except AttributeError:
            pass
#             self.Destroy()
            
            
    def OnClose(self, event):
#         try:
#         if  self.parent_worker is False:
#         except AttributeError:
        self.OnTaskStop(event)
        # else:
        #     self.OnTaskStop(event)
        #     self.parent.GetParent().GetParent().rfid_task_start(event)
        self.Destroy()


class AddUser(gui.AddUser, gui_lib.keybords.Keyboard):  # @UndefinedVariable
    def __init__(self, parent, edit=None, group_edit=False):
        gui.AddUser.__init__(self, parent)  # @UndefinedVariable
        self.group_edit=group_edit
        self.edit = edit
        self.parent = parent
        self.parent_worker = self.parent.GetParent().login.with_rfid_in
        self.SetTitle(gui_lib.msg.users_main_AddUser_name)
        self.m_staticText14.SetLabel(gui_lib.msg.users_main_AddUser_text['Text14'])
        self.m_staticText9.SetLabel(gui_lib.msg.users_main_AddUser_text['Text9'])
        self.m_staticText10.SetLabel(gui_lib.msg.users_main_AddUser_text['Text10'])
        self.m_radioBtn2.SetLabel(gui_lib.msg.users_main_AddUser_button['radioBtn2'])
        self.m_radioBtn3.SetLabel(gui_lib.msg.users_main_AddUser_button['radioBtn3'])
        self.m_staticText11.SetLabel(gui_lib.msg.users_main_AddUser_text['Text11'])
        self.m_button7.SetLabel(gui_lib.msg.users_main_AddUser_button['button7'])
        self.m_radioBtn2.SetToolTip(gui_lib.msg.users_main_AddUser_tolltip['radioBtn2'])
        self.m_radioBtn3.SetToolTip(gui_lib.msg.users_main_AddUser_tolltip['radioBtn3'])
        self.m_button7.SetToolTip(gui_lib.msg.users_main_AddUser_tolltip['button7'])
        #if libs.conf.RFID_USE_WORK is False:
        #    self.m_button7.Disable()
        self.m_button5.SetLabel(gui_lib.msg.users_main_AddUser_button['button5'])
        self.m_button6.SetLabel(gui_lib.msg.users_main_AddUser_button['button6'])
#         all_grup = self.parent.grup
        self.m_choice3Choices = ['']
        if self.group_edit is True:
            group = libs.DB.get_all(libs.models.UserGrup)
        else:
            group = libs.DB.get_all_where(libs.models.UserGrup, default_use=True)
        for item in group:
            self.m_choice3Choices.append(item.name)
        self.m_choice3.SetItems(self.m_choice3Choices)
        if self.edit != None:
            name = self.m_textCtrl10.SetValue(self.edit.name)  # @UnusedVariable
#             self.m_textCtrl10.SetEditable(False)
            
            self.m_textCtrl7.SetValue(self.edit.passwd)
            self.m_textCtrl8.SetValue(self.edit.passwd)
#             self.cart_id = self.edit.cart
            if self.edit.cart != None:
                self.m_staticText12.SetLabel(gui_lib.msg.users_main_AddUser_text['have_cart'])
                self.m_staticText12.Show()
                self.m_staticText12.SetForegroundColour(wx.Colour(0, 135, 11))
            else:
                self.m_staticText12.SetLabel(gui_lib.msg.users_main_AddUser_text['no_have_cart'])
                self.m_staticText12.Show()
                self.m_staticText12.SetForegroundColour(wx.Colour(199, 16, 29))
            # self.cart_block_9 = self.edit.cart_block_9
#             if self.m_choice3Choices.index(self.edit.grup.name) == 0:
#             if self.edit.grup.name not in self.m_choice3Choices:
#
#                 self.Destroy()
#                 return None
            index = self.m_choice3Choices.index(self.edit.grup.name)
            self.m_choice3.SetSelection(index) 
#             else:
#                 self.m_choice3.SetSelection(self.m_choice3Choices.index(self.edit.grup.name)-1)
            if self.edit.enable is True:
                self.m_radioBtn2.SetValue(True)
                self.m_radioBtn3.SetValue(False)
            else:
                self.m_radioBtn2.SetValue(False)
                self.m_radioBtn3.SetValue(True)
            self.cart_id = self.edit.cart
        else:
            self.add_user = libs.DB.make_obj(libs.models.User)
            self.m_staticText12.SetLabel(gui_lib.msg.users_main_AddUser_text['no_have_cart'])
            self.m_staticText12.Show()
            self.m_staticText12.SetForegroundColour(wx.Colour(199, 16, 29))
            self.m_choice3.SetSelection(0)
            self.cart_id = None
            
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl10.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl7.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)
            self.m_textCtrl8.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)
        self.SetMinSize((250, 250))
        self.Fit()
        # self.Layout()

    def OnAddCart(self, event):
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        # if self.parent_worker is False:
        #     pass
        # else:
        #     # self.OnTaskStop(event)
        #     self.parent.GetParent().rfid_task_stop(event)
        panel = AddCart(self)
        panel.ShowModal()
        if self.cart_id != None:
            self.m_staticText12.SetLabel(gui_lib.msg.users_main_AddUser_text['have_cart'])
            self.m_staticText12.Show()
            self.m_staticText12.SetForegroundColour(wx.Colour(0, 135, 11))
        else:
            self.m_staticText12.SetLabel(gui_lib.msg.users_main_AddUser_text['no_have_cart'])
            self.m_staticText12.SetForegroundColour(wx.Colour(199, 16, 29))


    def OnSave(self, event):
        name = self.m_textCtrl10.GetValue()
        passwd = self.m_textCtrl7.GetValue()
        chk_passwd = self.m_textCtrl8.GetValue()
#         if self.edit != None:
#             self.cart_id = self.edit.cart
        
#         self.m_choice3Choices = []
#         for item in self.parent.grup:
#             self.m_choice3Choices.append(item.name)
        if self.m_choice3.GetSelection() <= 0:
            dial = wx.MessageDialog(self, *gui_lib.msg.EMPTY_FIELD)
            dial.ShowModal()
            return
        grup = self.m_choice3.GetString(self.m_choice3.GetSelection())
        grup = libs.DB.get_one_where(libs.models.UserGrup, name=grup)
#         print grup.id
#         import sys
#         sys.exit()
#         import sys
#         print grup
#         sys.exit()
        enable = self.m_radioBtn2.GetValue()
        if name == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.EMPTY_FIELD)
            dial.ShowModal()
        elif passwd != chk_passwd:
            self.m_textCtrl7.SetForegroundColour(wx.Colour(199, 16, 29))
            self.m_textCtrl8.SetForegroundColour(wx.Colour(199, 16, 29))
            dial = wx.MessageDialog(self, *gui_lib.msg.PASSWD_WRONG)
            dial.ShowModal()
        elif passwd == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.EMPTY_FIELD)
            dial.ShowModal()
        else:
#             print self.edit
            if self.edit == None:
#                 user = libs.DB.get_one_where(libs.mobile.User, name=name)
#                 if 
#             self.m_textCtrl10.SetForegroundColour(wx.Colour(199, 16, 29))
#             wx.MessageBox(*gui_lib.msg.DB_HAVE_THIS_NAME)
#                 kasa = libs.DB.make_obj(libs.models.Kasa)
#                 libs.DB.add_object_to_session(kasa)

                
                self.user_add = libs.DB.make_obj(libs.models.User)
                self.user_add.name = name
                self.user_add.passwd = passwd
                self.user_add.grup_id = grup.id
                self.user_add.enable = enable

#                 if enable is True:
                self.user_add.cart = self.cart_id

#                 else:
#                     self.user_add.cart = None
#                 self.user_add.kasa_id = kasa.id
                libs.DB.add_object_to_session(self.user_add)
                err = libs.DB.make_obj(libs.models.GetCounterError)#(self.USER.id, i)
                err.user_id = self.parent.GetParent().USER.id  # @UndefinedVariable
#                 err.mashin_nom_in_l = 1
                err.info = 'USER CHANGE' + ': ' + '%s/%s' % (self.user_add.name, self.parent.GetParent().USER.name )
                libs.DB.add_object_to_session(err)
                # libs.DB.commit()
#                 response = db_ctrl.user_add(name, passwd, grup, self.cart_id, enable=enable)
            else:
                self.edit.name = name
                self.edit.passwd = passwd
                self.edit.grup_id = grup.id
#                 if enable is True:
                self.edit.cart = self.cart_id
#                 else:
#                     self.edit.cart = None
                self.edit.enable = enable 
                libs.DB.add_object_to_session(self.edit)
#                 response = db_ctrl.user_edit(self.edit, name, passwd, grup, self.cart_id, enable)
#             self.Destroy()
                err = libs.DB.make_obj(libs.models.GetCounterError)#(self.USER.id, i)
                err.user_id = self.parent.GetParent().USER.id  # @UndefinedVariable
#                 err.mashin_nom_in_l = 1
                err.info = 'USER CHANGE' + ': ' + '%s from %s.' % (self.edit.name, self.parent.GetParent().USER.name )
                libs.DB.add_object_to_session(err)
            try:
                libs.DB.commit()
                if self.parent_worker is False:
                    pass
                else:
                    # self.OnTaskStop(event)
                    self.parent.GetParent().rfid_task_start(event)
                self.Destroy()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                libs.DB.rollback()
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
                dial.ShowModal()

            
    def OnClose(self, event):
        # if self.parent_worker is False:
        #     pass
        # else:
        #     # self.OnTaskStop(event)
        #     self.parent.GetParent().rfid_task_start(event)
        self.Destroy()
        
class AddGrup(gui.AddGrup, gui_lib.keybords.Keyboard):

    def __init__(self, parent, edit=None):
        gui.AddGrup.__init__(self, parent)
        self.edit = edit
        self.parent = parent
        self.width, self.height = self.GetSize()
        # self.m_treeCtrl1.SetSize((self.width*0.4, self.height*0.5))
        # self.m_treeCtrl2.SetSize((self.width * 0.4, self.height * 0.5))
        self.SetTitle(gui_lib.msg.users_main_AddGrup_name)
        self.m_staticText1.SetLabel(gui_lib.msg.users_main_AddGrup_text['Text1'])
        self.m_staticText3.SetLabel(gui_lib.msg.users_main_AddGrup_text['Text3'])
        self.m_staticText2.SetLabel(gui_lib.msg.users_main_AddGrup_text['Text2'])
        self.m_button2.SetLabel(gui_lib.msg.users_main_AddGrup_button['button2'])
        self.m_button1.SetLabel(gui_lib.msg.users_main_AddGrup_button['button1'])
        self.m_checkBox71.SetLabel(gui_lib.msg.users_main_AddGrup_button['checkBox71'])
        self.m_checkBox71.SetToolTip(gui_lib.msg.users_main_AddGrup_tolltip['checkBox71'])
        self.m_bpButton2.SetToolTip(gui_lib.msg.users_main_AddGrup_tolltip['bpButton2'])
        self.m_bpButton3.SetToolTip(gui_lib.msg.users_main_AddGrup_tolltip['bpButton3'])

        self.m_checkBox51.SetLabel(gui_lib.msg.users_main_AddGrup_button['m_checkBox51'])
        self.m_checkBox2.SetLabel(gui_lib.msg.users_main_AddGrup_button['m_checkBox2'])
        self.m_checkBox3.SetLabel(gui_lib.msg.users_main_AddGrup_button['m_checkBox3'])
        # self.m_checkBox4.SetLabel(gui_lib.msg.users_main_AddGrup_button['m_checkBox4'])
        self.m_checkBox5.SetLabel(gui_lib.msg.users_main_AddGrup_button['m_checkBox5'])

        self.m_textCtrl9.SetToolTip(gui_lib.msg.users_main_AddGrup_button['m_textCtrl9t'])
        self.m_textCtrl10.SetToolTip(gui_lib.msg.users_main_AddGrup_button['m_textCtrl10t'])

        if self.edit != None:
            self.m_textCtrl1.SetValue(self.edit.name)
            self.m_checkBox71.SetValue(self.edit.default_use)
            self.m_checkBox2.SetValue(self.edit.bill_disable)
            self.m_checkBox3.SetValue(self.edit.get_all_bill)
            self.m_textCtrl8.SetValue(self.edit.subject)
            # self.m_checkBox4.SetValue(self.edit.add_bonus_hold)
            self.m_checkBox5.SetValue(self.edit.auto_mail)
            self.m_checkBox51.SetValue(self.edit.rko_auto_mail)
            self.m_textCtrl9.SetValue(self.edit.boss_mail)
            self.m_textCtrl10.SetValue(self.edit.service_mail)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl1.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl9.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl10.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl8.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
        self._refresh_frame()
        self.Fit()

    def _refresh_frame(self, grup=None):
        self.full_root = self.m_treeCtrl1.AddRoot('full_root')
        self.group_root = self.m_treeCtrl2.AddRoot('group_root')
        self.all_right = {}
        self.group_right = {}
        for item in gui_lib.msg.right_group_name:
            self.all_right[item] = self.m_treeCtrl1.AppendItem(self.full_root, gui_lib.msg.right_group_name[item])

        for item in gui_lib.right.RIGHT:
            for b in gui_lib.right.RIGHT[item]:
                self.m_treeCtrl1.AppendItem(self.all_right[item], gui_lib.right.RIGHT[item][b])

        if self.edit != None:
            if self.edit.right != None:
                right = self.edit.from_json()
                # print right
                for item in right:
                    if right[item] != []:
                        self.group_right[item] = self.m_treeCtrl2.AppendItem(self.group_root,gui_lib.msg.right_group_name[item])
                        for b in gui_lib.right.RIGHT[item]:
                            # print item, b
                            if b in right[item]:
                                self.m_treeCtrl2.AppendItem(self.group_right[item], gui_lib.right.RIGHT[item][b])

    def OnAddRight(self, event):
        selected = self.m_treeCtrl1.GetItemText(self.m_treeCtrl1.GetSelection())
        if selected == 'full_root':
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return
        my_parent = self.m_treeCtrl1.GetItemParent(self.m_treeCtrl1.GetSelection())
        parent = self.m_treeCtrl1.GetItemText(my_parent)

        if parent == 'full_root':
            if selected in gui_lib.msg.right_group_name.values():
                index = list(gui_lib.msg.right_group_name.values()).index(selected)
                index = list(gui_lib.msg.right_group_name.keys())[index]
                # print index,self.group_right[index]
                if index in self.group_right:
                    self.m_treeCtrl2.DeleteChildren(self.group_right[index])
                else:
                    self.group_right[index] = self.m_treeCtrl2.AppendItem(self.group_root,
                                                                          gui_lib.msg.right_group_name[index])

                for b in gui_lib.right.RIGHT[index]:
                    self.m_treeCtrl2.AppendItem(self.group_right[index], gui_lib.right.RIGHT[index][b])
        else:
            index = list(gui_lib.msg.right_group_name.values()).index(parent)
            index = list(gui_lib.msg.right_group_name.keys())[index]

            new_index = list(gui_lib.right.RIGHT[index].values()).index(selected)
            new_index = list(gui_lib.right.RIGHT[index].keys())[new_index]
            all_list = []
            try:
                item, cookie = self.m_treeCtrl2.GetFirstChild(self.group_right[index])
            except KeyError:
                self.group_right[index] = self.m_treeCtrl2.AppendItem(self.group_root,
                                                                      gui_lib.msg.right_group_name[index])
                self.m_treeCtrl2.AppendItem(self.group_right[index], gui_lib.right.RIGHT[index][new_index])

            else:
                all_list.append(self.m_treeCtrl1.GetItemText(item))
                while True:
                    item, cookie = self.m_treeCtrl2.GetNextChild(self.group_right[index], cookie)
                    try:
                        all_list.append(self.m_treeCtrl1.GetItemText(item))
                    except wx._core.PyAssertionError:
                        break
                if gui_lib.right.RIGHT[index][new_index] not in all_list:
                    self.m_treeCtrl2.AppendItem(self.group_right[index], gui_lib.right.RIGHT[index][new_index])

    def OnDelRight(self, event):
        selected = self.m_treeCtrl2.GetSelection()
        selected = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        if selected == 'group_root':
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return
        index = self.m_treeCtrl2.GetItemText(self.m_treeCtrl2.GetSelection())
        if index in gui_lib.msg.right_group_name.values():
            index = list(gui_lib.msg.right_group_name.values()).index(index)
            index = list(gui_lib.msg.right_group_name.keys())[index]

        if index in self.group_right:
            self.m_treeCtrl2.DeleteChildren(self.m_treeCtrl2.GetSelection())
            self.m_treeCtrl2.Delete(self.m_treeCtrl2.GetSelection())
            del self.group_right[index]
        else:
            parent = self.m_treeCtrl2.GetItemParent(self.m_treeCtrl2.GetSelection())
            self.m_treeCtrl2.Delete(self.m_treeCtrl2.GetSelection())
            try:
                item, cookie = self.m_treeCtrl2.GetFirstChild(parent)
                self.m_treeCtrl2.GetItemText(item)
            except wx._core.PyAssertionError:
                name = self.m_treeCtrl2.GetItemText(parent)
                # print parent
                if name in gui_lib.msg.right_group_name.values():
                    index = list(gui_lib.msg.right_group_name.values()).index(name)
                    index = list(gui_lib.msg.right_group_name.keys())[index]
                    del self.group_right[index]
                    self.m_treeCtrl2.Delete(parent)

    def OnSave(self, event):
        name = self.m_textCtrl1.GetValue()
        if name == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.EMPTY_FIELD)
            dial.ShowModal()
            return
        var = []
        obj = []
        try:
            item, cookie = self.m_treeCtrl2.GetFirstChild(self.group_root)
        except KeyError:
            pass
        else:
            right = {}
            # var = []
            # print item
            try:
                var.append(list(gui_lib.msg.right_group_name.values()).index(self.m_treeCtrl2.GetItemText(item)))
                # print gui_lib.msg.right_group_name.values()
                # return

                while True:
                    try:
                        obj.append(item)
                        item, cookie = self.m_treeCtrl2.GetNextChild(self.group_root, cookie)

                        # print self.m_treeCtrl1.GetItemText(item)
                        var.append(list(gui_lib.msg.right_group_name.values()).index(self.m_treeCtrl2.GetItemText(item)))
                    except wx._core.PyAssertionError:
                        break
            except wx._core.PyAssertionError:
                pass
            # print var, len(obj)
            for i in var:
                right[list(gui_lib.msg.right_group_name.keys())[i]] = {}
                # right[gui_lib.msg.right_group_name.keys().index(i)] = {}
            # print right
            # print len(obj)
            for item in obj:
                right_in_group = []
                # i, cookie = self.m_treeCtrl2.GetFirstChild(item)
                # print item #self.m_treeCtrl2.GetItemText(item)
                group = list(gui_lib.msg.right_group_name.values()).index(self.m_treeCtrl2.GetItemText(item))
                group = list(gui_lib.msg.right_group_name.keys())[group]
                new_light = []
                i, cookie = self.m_treeCtrl2.GetFirstChild(item)
                new_light.append(list(gui_lib.right.RIGHT[group].values()).index(self.m_treeCtrl2.GetItemText(i)))
                while True:
                    try:
                        i, cookie = self.m_treeCtrl2.GetNextChild(item, cookie)
                        new_light.append(list(gui_lib.right.RIGHT[group].values()).index(self.m_treeCtrl2.GetItemText(i)))
                    except wx._core.PyAssertionError:
                        break
                    # except Exception as e:
                    #     print self.m_treeCtrl2.GetItemText(i)
                    #     return
                # print new_light
                my_new = []
                for i in new_light:
                    my_new.append(list(gui_lib.right.RIGHT[group].keys())[i])
                right[group] = my_new
            if 'main' not in right:
                right['main'] = []
            if 'cust' not in right:
                right['cust'] = []
            if 'config' not in right:
                right['config'] = []
            if 'order' not in right:
                right['order'] = []
            if 'user' not in right:
                right['user'] = []
            if 'mashin' not in right:
                right['mashin'] = []
            if 'diff' not in right:
                right['diff'] = []
            if 'report' not in right:
                right['report'] = []
            if self.edit == None:
                self.edit = libs.DB.make_obj(libs.models.UserGrup)
                self.edit.name = name
            self.edit.right = right
            self.edit.to_json()
            self.edit.default_use = self.m_checkBox71.GetValue()
            self.edit.auto_mail = self.m_checkBox5.GetValue()
            self.edit.rko_auto_mail = self.m_checkBox51.GetValue()
            self.edit.bill_disable = self.m_checkBox2.GetValue()
            self.edit.get_all_bill = self.m_checkBox3.GetValue()
            self.edit.subject =self.m_textCtrl8.GetValue()
            # self.edit.add_bonus_hold = self.m_checkBox4.GetValue()
            self.edit.boss_mail = self.m_textCtrl9.GetValue()
            self.edit.service_mail = self.m_textCtrl10.GetValue()
            libs.DB.add_object_to_session(self.edit)
            err = libs.DB.make_obj(libs.models.GetCounterError)  # (self.USER.id, i)
            err.user_id = self.parent.GetParent().USER.id  # @UndefinedVariable
            err.info = 'GROUP CHANGE' + ': ' + u'%s/%s.' % (name, self.parent.GetParent().USER.name )
            libs.DB.add_object_to_session(err)
            try:
                libs.DB.commit()
                self.Destroy()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                libs.DB.rollback()
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
                dial.ShowModal()

    def OnClose(self, event):
        # libs.DB.rollback()
        self.Destroy()

class HoldUserMony(gui.HoldMony, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user, my_user):
        self.parent = parent
        self.user = user
        self.my_user = my_user
        gui.HoldMony.__init__(self, self.parent)
        # start_times = libs.DB.get_one_where(libs.models.DayReport, day_report=False, descs=True, order='id')
        # if start_times == None:
        #     start_times = '2001-01-01 00:00:00'
        # else:
        #     start_times = libs.models.TZ.date_to_str(start_times.pub_time- datetime.timedelta(days=367), '%Y-%m-%d %H:%M:%S')
        # end_times = datetime.datetime.now()
        # end_times = libs.models.TZ.date_to_str(end_times, '%Y-%m-%d %H:%M:%S')
        # self.lipsi_sum = 0
        # self.db_row = libs.DB.get_all_where(libs.models.Lipsi,
        #                                     pub_time__btw=(start_times, end_times),
        #                                     user_id=user.id,
        #                                     order='id',
        #                                     descs=True, chk=True)
        #
        # for i in self.db_row:
        #     self.lipsi_sum += i.mony

        self.SetTitle(gui_lib.msg.user_HOLD_mony['name'])
        self.m_staticText10.SetLabel(gui_lib.msg.user_HOLD_mony['m_staticText10'])
        self.m_staticText11.SetLabel(gui_lib.msg.user_HOLD_mony['m_staticText11'] + ': ' + self.user.name)
        self.m_staticText12.SetLabel(gui_lib.msg.user_HOLD_mony['m_staticText12'] + ': ' + "{:.2f}".format(self.user.lipsi))
        self.m_button9.SetLabel(gui_lib.msg.user_HOLD_mony['m_button9'])
        self.m_button10.SetLabel(gui_lib.msg.user_HOLD_mony['m_button10'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl1.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)


    def OnGo(self, event):
        obj = libs.DB.make_obj(libs.models.Lipsi)
        obj.user_id = self.user.id
        obj.mony = self.m_spinCtrl1.GetValue()
        if obj.mony < 0:
            obj.mony = obj.mony * -1
        if self.user.lipsi > 0:
            self.user.lipsi -= self.m_spinCtrl1.GetValue()
        else:
            self.user.lipsi = 0
        obj.if_lipsa = False
        obj.chk = True
        libs.DB.add_object_to_session(obj)
        cant_unlock = libs.DB.make_obj(libs.models.GetCounterError)
        cant_unlock.user_id = self.user.id
        cant_unlock.info = u'USER CLEAN MISSING MONY: for user: %s, mony: %s' % (self.user.name, self.m_spinCtrl1.GetValue())
        libs.DB.add_object_to_session(cant_unlock)
        libs.DB.add_object_to_session(self.user)
        try:
            libs.DB.commit()
            self.OnClose(event)
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            libs.DB.rollback()
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()

    def OnClose( self, event ):
        self.Destroy()

class UserConf(gui.UserPanel):  # @UndefinedVariable
    def __init__(self, parent):
        gui.UserPanel.__init__(self, parent)
        self.parent = parent
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.users_main_UserConf_name[1])
        self.width, self.height = self.parent.GetSize()
        self.Bind( wx.EVT_SIZE, self.on_resize )
        self.resize = True
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.users = libs.DB.get_all(libs.models.User)

        self.m_listCtrl1.InsertColumn(0, gui_lib.msg.users_main_UserConf_text[1])
        self.m_listCtrl1.InsertColumn(1, gui_lib.msg.users_main_UserConf_text[2])

        self.m_listCtrl2.InsertColumn(0, gui_lib.msg.users_main_UserConf_text[3])
        self.m_listCtrl2.InsertColumn(1, gui_lib.msg.users_main_UserConf_text[4])
        self.group_edit = False
        self._add_grup_list()
        self._add_user_list()
        
        self._set_right()
        self.on_resize(None)
        self.m_listCtrl1.Select(0)
        self.m_listCtrl1.SetToolTip(gui_lib.msg.users_main_UserConf_tolltip['listCtrl1'])
        self.m_listCtrl2.SetToolTip(gui_lib.msg.users_main_UserConf_tolltip['listCtrl2'])

#             self.Center()
#         if libs.conf.FULSCREEAN is True:
#             self.SetWindowStyle(wx.STAY_ON_TOP)
#         self.Fit()
    
    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        self.m_toolBar5.SetMinSize((self.width, -1))
        self.m_listCtrl1.SetMinSize((self.width//2, self.height * 0.75))
        self.m_listCtrl1.SetColumnWidth(1, self.width*0.44)
        self.m_listCtrl2.SetMinSize((self.width//2, self.height * 0.75))
        self.m_listCtrl2.SetColumnWidth(1, (self.width*0.425))
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height*0.95))
        if event != None:
            event.Skip() 
            self.Layout()
            
    def _set_right(self):
        self.m_toolBar5.ClearTools()
        if self.parent.USER.grup.right != None:
            right = self.parent.USER.grup.from_json()
            # print right
            if 1 in right['user']:
                self.group_edit = True
                self.m_tool2 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.users_main_UserConf_button['tool2'], wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/kopete.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.users_main_UserConf_tolltip['tool2'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnAddGrup, id=self.m_tool2.GetId())
                self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnEditGrup)
            if 2 in right['user']:
                self.m_tool3 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.users_main_UserConf_button['tool3'], wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/Gnome-Stock-Person-64.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.users_main_UserConf_tolltip['tool3'], wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnAddUser, id=self.m_tool3.GetId())
                self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnEditUser)
            if 3 in right['user']:
                self.m_tool4 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.users_main_UserConf_button['tool4'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/User-Info-64.png",
                                                                      wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL, gui_lib.msg.users_main_UserConf_tolltip['tool4'],
                                                            wx.EmptyString, None)

                self.Bind(wx.EVT_TOOL, self.OnActive, id=self.m_tool4.GetId())
            if 4 in right['user']:
                self.m_tool5 = self.m_toolBar5.AddTool(wx.ID_ANY,  gui_lib.msg.users_main_UserConf_button['tool5'],
                                                            wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/kontact.png", wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString,
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnHoldMissing, id=self.m_tool5.GetId())

        self.m_tool1 = self.m_toolBar5.AddTool(wx.ID_ANY, gui_lib.msg.users_main_UserConf_button['tool1'], wx.Bitmap(
        libs.conf.IMG_FOLDER + u"64x64/dialog-error.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, gui_lib.msg.users_main_UserConf_tolltip['tool1'], wx.EmptyString, None)
        self.Bind(wx.EVT_TOOL, self.OnClose, id=self.m_tool1.GetId())
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.m_toolBar5.Realize()

    def OnHoldMissing( self, event ):
        try:
            user = self.userListDict[self.m_listCtrl2.GetFirstSelected()]
            dial = HoldUserMony(self, user, self.parent.USER)
            dial.ShowModal()
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()

    def _add_grup_list(self):
        collor = False
        self.grup = libs.DB.get_all(libs.models.UserGrup)
        self.m_listCtrl1.InsertItem(0, str(1))
        self.m_listCtrl1.SetItem(0, 1, gui_lib.msg.users_main_UserConf_text[5])
        self.m_listCtrl1.InsertItem(1, str(2))
        self.m_listCtrl1.SetItem(1, 1, gui_lib.msg.users_main_UserConf_text[6])
        self.m_listCtrl1.InsertItem(2, str(3))
        self.m_listCtrl1.SetItem(2, 1, gui_lib.msg.users_main_UserConf_text[7])
        index = 3
        self.grupListDict = {}
        for item in self.grup:
            self.m_listCtrl1.InsertItem(index, str(index + 1))
            self.m_listCtrl1.SetItem(index, 1, item.name)
            if collor is True:
                self.m_listCtrl1.SetItemBackgroundColour(
                    item=index, col=wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
                collor = False
            else:
                self.m_listCtrl1.SetItemBackgroundColour(
                    item=index, col=wx.Colour(229, 229, 229))
                collor = True
            self.grupListDict[index] = item
            index += 1


    def _refresh_grup_list(self):
        self.m_listCtrl1.DeleteAllItems()
        self._add_grup_list()

    def _add_user_list(self, grup=None, active=None):
#         collor = True
        index = 0
        self.userListDict = {}
        if grup == None and active == None:
            self.users = libs.DB.get_all(libs.models.User)
        elif grup == None and active != None:
            self.users = libs.DB.get_all_where(libs.models.User, enable=active)
        else:
            self.users = libs.DB.get_all_where(libs.models.User, grup_id=grup.id)
        
        for item in self.users:
            self.m_listCtrl2.InsertItem(index, str(index + 1))
            self.m_listCtrl2.SetItem(index, 1, item.name)
            if item.enable is True:
                self.m_listCtrl2.SetItemTextColour(
                    item=index, col=wx.Colour(0, 135, 11))
            else:
                self.m_listCtrl2.SetItemTextColour(
                    item=index, col=wx.Colour(199, 16, 29))
            self.userListDict[index] = item
            index += 1

    def _refresh_user_list(self, grup=None, active=None):
        self.m_listCtrl2.DeleteAllItems()
        self._add_user_list(grup, active)

    def OnShowUserInGrup(self, event):
#         grup = self.m_listCtrl1.GetFirstSelected()
        try:
            grup = self.m_listCtrl1.GetFirstSelected()
            grup = self.m_listCtrl1.GetItem(grup, col=1).GetText()
            if grup == gui_lib.msg.users_main_UserConf_text[5]:
                self._refresh_user_list()
            elif grup == gui_lib.msg.users_main_UserConf_text[6]:
                self._refresh_user_list(active=True)
            elif grup == gui_lib.msg.users_main_UserConf_text[7]:
                self._refresh_user_list(active=False)
            else:  
#                 print self.m_listCtrl1.GetFirstSelected() - 3
                grup = self.grup[self.m_listCtrl1.GetFirstSelected()-3]
                self._refresh_user_list(grup)
#         except IndexError:
#             try:
#                 grup = grup = self.m_listCtrl1.GetFirstSelected()
#                 grup = self.m_listCtrl1.GetItem(grup, col=1).GetText()
        except wx._core.PyAssertionError:
            self._refresh_user_list()
#             else:
# #                 print grup
#                 if grup == _(u'Всички Потребители'):
#                     self._refresh_user_list()
#                 elif grup == _(u'Активни Потребители'):
#                     self._refresh_user_list(active=True)
#                 elif grup == _(u'Неактивни Потребители'):
#                     self._refresh_user_list(active=False)
#         else:
            

    def OnAddGrup(self, event):
        panel = AddGrup(self)
        panel.ShowModal()
        self._refresh_grup_list()

    def OnEditGrup(self, event):
        currentItem = event.GetIndex()
        # raise KeyError(currentItem)
        if currentItem > 2:
            grup = self.grupListDict[currentItem]
            panel = AddGrup(self, edit=grup)
            panel.ShowModal()
            self.OnShowUserInGrup(event)

    def OnEditUser(self, event):
        currentItem = event.GetIndex()
        user = self.userListDict[currentItem]
        if self.group_edit is False:
            group = libs.DB.get_all_where(libs.models.UserGrup, default_use=True)
            if group == []:
                dial = wx.MessageDialog(None, *gui_lib.msg.NO_HAVE_RIGHT)
                dial.ShowModal()
        else:
            group = libs.DB.get_all(libs.models.UserGrup, order='name')
        var = []
        for i in group:
            var.append(i.name)
        if user.grup.name not in var:
            dial = wx.MessageDialog(None, *gui_lib.msg.NO_HAVE_RIGHT)
            dial.ShowModal()
        else:
            self.panel = AddUser(self, edit=user, group_edit=self.group_edit)
            self.panel.ShowModal()
            self.OnShowUserInGrup(event)
        
        
    def OnAddUser(self, event):
        panel = AddUser(self, group_edit=self.group_edit)
        panel.ShowModal()
#         if self.parent == None:
#             self.Destroy()
#         try:
        self.OnShowUserInGrup(event)
#         self.OnShowUserInGrup()
#         except:
#             pass

    def OnClose(self, event):
        self.parent.login_user_refresh()
        self.parent.OnConfig(None)
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.users_main_UserConf_name[2])
        self.Destroy()

    def OnActive(self, event):
        dial = LogedInUser(self)
        dial.ShowModal()
        

class LogedInUser(gui.LogedInUser):
    def __init__(self, parent):
        self.parent = parent
        gui.LogedInUser.__init__(self, parent)
        self.SetTitle(gui_lib.msg.users_main_LogedInUser_name)
        self.m_listCtrl3.InsertColumn(0, gui_lib.msg.users_main_LogedInUser_text['list_column'])
        self.m_button9.SetLabel(gui_lib.msg.users_main_LogedInUser_button['button9'])
        self.m_listCtrl3.SetToolTip(gui_lib.msg.users_main_LogedInUser_tolltip['Ctrl3'])
        self.width, self.height = self.GetSize()
        self.m_listCtrl3.SetColumnWidth(0, self.width * 0.70)
        self._refresh_user_list()


    def _add_user_list(self):
        self.userListDict = {}
        index = 0
        self.user = libs.DB.get_all_where(libs.models.User, login=True)
        for i in self.user:
            self.m_listCtrl3.InsertItem(index, i.name)
            self.userListDict[index] = i
            index += 1


    def _refresh_user_list(self):
        self.m_listCtrl3.DeleteAllItems()
        self._add_user_list()


    def OnClose( self, event ):
        self.Destroy()

    def OnOut( self, event ):
        currentItem = event.GetIndex()
        user = self.userListDict[currentItem]
        user.login = False
        libs.DB.add_object_to_session(user)
        libs.DB.commit()
        self._refresh_user_list()
