#-*- coding:utf-8 -*-
'''
Created on 21.06.2017 г.

@author: dedal
'''
import wx
import libs  # @UnresolvedImport
import gui_lib  # @UnresolvedImport
import datetime
from . import gui
import json
 
class InOutReson(gui.Lipsi, gui_lib.keybords.Keyboard):
    def __init__(self, parent, types, edit=None, user=None):
        self.edit = edit
        gui.Lipsi.__init__(self, parent)
        self.types = types
        self.parent = parent
        try:
            if user == None:
                user = self.parent.GetParent().GetParent().USER  # @UndefinedVariable
        except AttributeError:
            if user == None:
                self.user = self.parent.GetParent().USER
        self.user = user
        self.m_button2.SetLabel(gui_lib.msg.mony_main_InOutReson_button['m_button2'])
        self.m_button3.SetLabel(gui_lib.msg.mony_main_InOutReson_button['m_button3'])
        self.m_radioBtn1.SetLabel(gui_lib.msg.mony_main_InOutReson_button['m_radioBtn1'])
        self.m_radioBtn2.SetLabel(gui_lib.msg.mony_main_InOutReson_button['m_radioBtn2'])
        if self.types == 'IN':
            if libs.conf.USE_VIRTUAL_KEYBORD is True:
                self.m_textCtrl1.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.SetTitle(gui_lib.msg.mony_main_InOutReson_name['prihod'])
            self.m_staticText3.SetLabel(gui_lib.msg.mony_main_InOutReson_text['m_staticText3_1'])
            self.m_radioBtn1.Hide()
            self.m_radioBtn2.Hide()
        elif self.types == 'OUT':
            if libs.conf.USE_VIRTUAL_KEYBORD is True:
                self.m_textCtrl1.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.SetTitle(gui_lib.msg.mony_main_InOutReson_name['razhod'])
            self.m_staticText3.SetLabel(gui_lib.msg.mony_main_InOutReson_text['m_staticText3_2'])
            self.m_radioBtn1.Hide()
            self.m_radioBtn2.Hide()
        elif self.types == 'LIPSI':
            if libs.conf.USE_VIRTUAL_KEYBORD is True:
                self.m_textCtrl1.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.SetTitle(gui_lib.msg.mony_main_InOutReson_name['lipsi'])
            self.m_staticText3.SetLabel(gui_lib.msg.mony_main_InOutReson_text['m_staticText3'])
        # if libs.conf.USE_VIRTUAL_KEYBORD is True:
        #     self.m_textCtrl1.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
        self.Fit()
        
    def OnGo(self, event):
        name = self.m_textCtrl1.GetValue()
        libs.DB.expire(self.user)
        if self.types == 'IN':
            obj = libs.DB.make_obj(libs.models.PrihodType)
            obj.name = name
            libs.DB.add_object_to_session(obj)
        elif self.types == 'OUT':
            obj = libs.DB.make_obj(libs.models.RazhodType)
            obj.name = name
            libs.DB.add_object_to_session(obj)
        elif self.types == 'LIPSI':
            name = name.replace(',', '.')
            try:
                name = float(name)
                mony = name
            except ValueError:
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                dial.ShowModal()
                return
            else:
                obj = libs.DB.make_obj(libs.models.Lipsi)
                
                obj.user_id = self.user.id
                if self.m_radioBtn1.GetValue() is True:

                    if mony < 0:
                        mony = mony *-1
                    # else:
                    if self.user.lipsi + mony > 0:
                        self.user.lipsi += mony
                    obj.if_lipsa = True
                    self.user.kasa -= round(mony, 2)
                else:
                    if mony < 0:
                        mony = mony * -1
                    if self.user.lipsi - mony > 0:
                        self.user.lipsi -= mony
                    obj.if_lipsa = False
                    self.user.kasa += round(mony, 2)
                obj.mony = mony
                libs.DB.add_object_to_session(obj)
                libs.DB.add_object_to_session(self.user)
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            libs.DB.rollback()
            return
        self.Destroy()
        
    def OnClose(self, event):
        self.Destroy()
        
class MonyInOut(gui.MonyInOut, gui_lib.keybords.Keyboard):
    def __init__(self, parent, types, edit=None, user=None):
        gui.MonyInOut.__init__(self, parent)
        self.types = types
        self.edit = edit
        self.parent = parent
        if user == None:
            user = self.parent.GetParent().USER
        self.user = user
        self._set_right()
        self.m_bpButton2.SetToolTip(gui_lib.msg.mony_main_MonyInOut_tooltip['m_bpButton2'])
        self.m_bpButton1.SetToolTip(gui_lib.msg.mony_main_MonyInOut_tooltip['m_bpButton1'])
        self.m_listCtrl1.SetToolTip(gui_lib.msg.mony_main_MonyInOut_tooltip['m_listCtrl1'])
        self.m_button4.SetLabel(gui_lib.msg.mony_main_MonyInOut_tooltip['m_button4'])
        self.m_button1.SetLabel(gui_lib.msg.mony_main_MonyInOut_tooltip['m_button1'])

        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl2.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl3.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
        self.m_staticText1.SetLabel(gui_lib.msg.mony_main_MonyInOut_text['m_staticText1'])
        if self.types == 'IN':
            self.m_listCtrl1.InsertColumn(0, gui_lib.msg.mony_main_MonyInOut_text['m_listCtrl1'])
            self.SetTitle(gui_lib.msg.mony_main_MonyInOut_name['prihod'])
            self.m_staticText2.SetLabel(gui_lib.msg.mony_main_MonyInOut_text['m_staticText2'])

        elif self.types == 'OUT':
            self.m_listCtrl1.InsertColumn(0, gui_lib.msg.mony_main_MonyInOut_text['m_listCtrl1_1'])
            self.SetTitle(gui_lib.msg.mony_main_MonyInOut_name['razhod'])
            self.m_staticText2.SetLabel(gui_lib.msg.mony_main_MonyInOut_text['m_listCtrl1_1'])
        self._add_list()
        if self.edit != None:
            self.m_textCtrl2.SetValue(str(self.edit.mony))
            self.m_textCtrl3.SetValue(str(self.edit.info))
            
        self.width, self.height = wx.GetDisplaySize()
        self.m_listCtrl1.SetColumnWidth(0, self.width // 3)
        time_chk = libs.chk_time()
        if time_chk is not True:
            MyFrame = wx.MessageDialog(None, gui_lib.msg.bad_rtc_server+time_chk, gui_lib.msg.on_run_error, wx.OK| wx.ICON_ERROR)
            MyFrame.ShowModal()
            self.OnClose(None)
        
        
    def _set_right(self):
        self.m_bpButton1.Hide()
        self.m_bpButton2.Hide()
        if self.user.grup.right != None:
            right = self.user.grup.from_json()
            if self.types == 'IN':
                if 11 in right['order']:
                    self.m_bpButton1.Show()
                    self.m_bpButton2.Show()
                    self.m_bpButton1.Bind(wx.EVT_BUTTON, self.OnMonyInType)
                    self.m_bpButton2.Bind(wx.EVT_BUTTON, self.OnMonyInHide)
            elif self.types == 'OUT':
                if 12 in right['order']:
                    self.m_bpButton1.Show()
                    self.m_bpButton2.Show()
                    self.m_bpButton1.Bind(wx.EVT_BUTTON, self.OnMonyOutType)
                    self.m_bpButton2.Bind(wx.EVT_BUTTON, self.OnMonyOutHide)
    
    def _add_list(self):
        self.listDict = {}
        data = []
        if self.types == 'IN':
            data = libs.DB.get_all_where(libs.models.PrihodType, hiden=False, order='name')
        elif self.types == 'OUT':
            data = libs.DB.get_all_where(libs.models.RazhodType, hiden=False, order='name')
        index = 0
        for item in data:
            if item.name == u'SAS Bonus Cart':
                pass
            elif item.name == u'Cust Cart':
                pass
            elif item.name == u'AFT Bonus':
                pass
            if item.name == u'MonyBack':
                pass
            else:
                self.m_listCtrl1.InsertItem(index, item.name)
                self.listDict[index] = item
                index += 1
    
    def list_refresh(self):
        self.m_listCtrl1.DeleteAllItems()
        self._add_list()

    def OnMonyInHide(self, event):
        try:
            reson = self.listDict[self.m_listCtrl1.GetFirstSelected()]
        except (wx._core.PyAssertionError, KeyError) as e:
            #                 wx.MessageBox(*gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return
        reson.hiden = True
        libs.DB.add_object_to_session(reson)
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            libs.DB.rollback()
            return
        self.list_refresh()

    def OnMonyOutHide(self, event):
        try:
            reson = self.listDict[self.m_listCtrl1.GetFirstSelected()]
        except (wx._core.PyAssertionError, KeyError) as e:
            #                 wx.MessageBox(*gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return
        reson.hiden = True
        libs.DB.add_object_to_session(reson)
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            libs.DB.rollback()
            return
        self.list_refresh()

    def OnMonyInType(self, event):
        frame = InOutReson(self, 'IN')
        frame.ShowModal()
        self.list_refresh()

    def OnMonyOutType(self, event):
        frame = InOutReson(self, 'OUT')
        frame.ShowModal()
        self.list_refresh()
    
    def OnGo(self, event):
        mony = self.m_textCtrl2.GetValue()
        mony = mony.replace(',', '.')
        info = self.m_textCtrl3.GetValue()
        libs.DB.expire(self.user)
        try:
            mony = float(mony)
        except ValueError:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        else:
            try:
                reson = self.listDict[self.m_listCtrl1.GetFirstSelected()]
            except (wx._core.PyAssertionError, KeyError) as e:
                dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
                dial.ShowModal()
                return
            else:
                if self.edit == None:
                    if self.types == 'IN':
                        self.user.kasa = round(self.user.kasa + mony, 2)
                        obj = libs.DB.make_obj(libs.models.Prihod)
                        obj.mony = round(mony, 2)
                        obj.user_id = self.user.id
                        obj.info = info
                        obj.reson_id = reson.id
                    elif self.types == 'OUT':
                        self.user.kasa = round(self.user.kasa - mony, 2)
                        obj = libs.DB.make_obj(libs.models.Razhod)
                        obj.mony = round(mony, 2)
                        obj.user_id = self.user.id
                        obj.info = info
                        obj.reson_id = reson.id

                    libs.DB.add_object_to_session(self.user)
                    libs.DB.add_object_to_session(obj)
                else:
                    if self.types == 'IN':
                        self.user.kasa = round(self.user.kasa - self.edit.mony, 2)
                        self.user.kasa = round(self.user.kasa + mony, 2)
                    elif self.types == 'OUT':
                        self.user.kasa = round(self.user.kasa + self.edit.mony, 2)
                        self.user.kasa = round(self.user.kasa - mony, 2)
                    if self.edit.old_data == None:
                        self.edit.old_data = json.dumps([{'mony': self.edit.mony, 'info':self.edit.info, 'reson':self.edit.reson.id}])
                    else:
                        data = json.loads(self.edit.old_data)
                        data.append({'mony': self.edit.mony, 'info':self.edit.info, 'reson':self.edit.reson.id})
                        self.edit.old_data = json.dumps(data)
                    self.edit.mony = mony
                    self.edit.info = info
                    self.edit.reson_id = reson.id

                    self.edit.last_edit_time = datetime.datetime.now()
                    self.edit.last_edit_by_id = self.user.id
                    libs.DB.add_object_to_session(self.user)
                    libs.DB.add_object_to_session(self.edit)

                try:
                    libs.DB.commit()
                    self.Destroy()
                except Exception as e:
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
                    libs.DB.rollback()
                    dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                    dial.ShowModal()
                    # libs.DB.rollback()
    
    def OnClose(self, event):
        self.Destroy()

class TransverPassword(gui.TransverPassword, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user, mony):
        gui.TransverPassword.__init__(self, parent)
        self.on_close = True
        self.user = user
        self.m_staticText7.SetLabel(gui_lib.msg.mony_main_TransverPassword_text['Text7'] + u': ')
        self.m_staticText11.SetLabel(gui_lib.msg.mony_main_TransverPassword_text['Text11'] + u': ')
        self.SetTitle(gui_lib.msg.mony_main_TransverPassword_name)
        self.m_button7.SetLabel(gui_lib.msg.mony_main_TransverPassword_button['button7'])
        self.m_button8.SetLabel(gui_lib.msg.mony_main_TransverPassword_button['button8'])
        self.m_textCtrl6.SetToolTip(gui_lib.msg.mony_main_TransverPassword_tolltip['Ctrl6'])
        self.m_staticText12.SetLabel(self.user.name)
        self.m_staticText9.SetLabel("{:.2f}".format(mony))
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl6.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        passwd =self.m_textCtrl6.GetValue()
        if passwd != self.user.passwd:
            dial = wx.MessageDialog(self, *gui_lib.msg.PASSWD_WRONG)
            dial.ShowModal()
            return
        self.on_close = False
        self.OnClose(event)


class MonyTransfer(gui.MonyTransfer, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user, chk_for_mony=True):
        self.parent = parent
        self.user = user
        self.chk_for_mony = chk_for_mony
        gui.MonyTransfer.__init__(self, parent)
        self.SetTitle(gui_lib.msg.mony_main_MonyTransfer_name)
        self.m_textCtrl6.SetValue("{:.2f}".format(self.user.kasa))
        self.m_staticText15.SetLabel(gui_lib.msg.mony_main_MonyTransfer_text['m_staticText15'])
        self.m_staticText16.SetLabel(gui_lib.msg.mony_main_MonyTransfer_text['m_staticText16'])
        self.m_staticText14.SetLabel(gui_lib.msg.mony_main_MonyTransfer_text['m_staticText14'])

        self.m_button26.SetLabel(gui_lib.msg.mony_main_MonyTransfer_button['m_button26'])
        self.m_button27.SetLabel(gui_lib.msg.mony_main_MonyTransfer_button['m_button27'])

        self.m_radioBtn3.SetLabel(gui_lib.msg.mony_main_MonyTransfer_button['m_radioBtn3'])
        self.m_radioBtn4.SetLabel(gui_lib.msg.mony_main_MonyTransfer_button['m_radioBtn4'])
        self.m_radioBtn5.SetLabel(gui_lib.msg.mony_main_MonyTransfer_button['m_radioBtn5'])
        self.m_radioBtn6.SetLabel(gui_lib.msg.mony_main_MonyTransfer_button['m_radioBtn6'])
        self.error = False
        self.m_radioBtn3.SetValue(True)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl6.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl5.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
        # self.m_textCtrl6.SetToolTip(gui_lib.msg.mony_main_MonyTransfer_text['m_textCtrl5'])
        self.set_user_list()
        self.Layout()
        # self.Fit()

    def set_user_list(self):
        self.all_user = libs.DB.get_all_where(libs.models.User, enable=True, order='name')
        my_user_list = ['']
        for i in range(len(self.all_user)):
            if self.all_user[i].name == self.user.name:
                pass
            else:
                my_user_list.append(self.all_user[i].name)
        self.m_choice3.SetItems(my_user_list)


    def OnShowInfo( self, event ):
        self.m_textCtrl5.Show()
        self.Fit()

    def OnHideInfo( self, event ):
        self.m_textCtrl5.Hide()
        self.Fit()

    def OnClose( self, event ):
        self.error = True
        self.Destroy()

    def OnGo( self, event ):
        to_user = self.m_choice3.GetString(self.m_choice3.GetSelection())
        to_user = libs.DB.get_one_where(libs.models.User, name=to_user)
        libs.DB.expire(self.user)
        if to_user == None:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            self.error = True
            return

        mony = self.m_textCtrl6.GetValue()
        mony = mony.replace(',', '.')
        try:
            mony = float(mony)
        except ValueError:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            self.error = True
            return
        if self.chk_for_mony is True:
            if mony > round(self.user.kasa,2):
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_MONY)
                dial.ShowModal()
                self.error = True
                return
        dial = TransverPassword(self, to_user, mony)
        dial.ShowModal()
        if dial.on_close is True:
            self.error = True
            return
        info = self.m_textCtrl5.GetValue()
        reson = 0
        if self.m_radioBtn3.GetValue() is True:
            reson = 0
        elif self.m_radioBtn4.GetValue() is True:
            reson = 1
        elif self.m_radioBtn5.GetValue() is True:
            reson = 2
        elif self.m_radioBtn6.GetValue() is True:
            reson = 3
        self.user.kasa -= mony
        to_user.kasa += mony
        self.user.kasa = round(self.user.kasa, 2)
        to_user.kasa = round(to_user.kasa, 2)
        libs.DB.add_object_to_session(self.user)
        libs.DB.add_object_to_session(to_user)
        obj = libs.DB.make_obj(libs.models.KasaTransfer)
        obj.mony = mony
        obj.info = info
        obj.reson = reson
        obj.to_user_id = to_user.id
        obj.from_user_id = self.user.id
        obj.chk = False
        obj.chk_to = False
        libs.DB.add_object_to_session(obj)
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            libs.DB.rollback()
            return
        self.Destroy()
