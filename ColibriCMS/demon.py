#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on 3.07.2018 г.

@author: dedal
'''
import os
import sys
import wx
import json
from queue import Queue
from sqlalchemy.exc import OperationalError
import time
from datetime import datetime
import libs
import libs.log
from make_order import MakeOrder
import gui
import gui_lib
import task
import users
import report
import config
import cust
import licenz
import order
import mashin
import servises
from pygame import mixer

try:
    mixer.init()
except Exception as e:
    print(e)
    mixer = 'No Device'

def stop_player():
    global mixer
    if mixer == 'No Device':
        return
    try:
        mixer.music.stop()
        mixer.quit()
    except Exception:
        pass

def play_sound(music='asdl1_tone2.wav'):
    global mixer
    if mixer == 'No Device':
        return
    try:
        mixer.init()
        mixer.music.load(music)
        mixer.music.play()
    except Exception:
        mixer = 'No Device'

class BugReport(gui.BugReport, gui_lib.keybords.Keyboard):
    def __init__(self, parent, device):
        gui.BugReport.__init__(self, parent)
        self.SetTitle(gui_lib.msg.main_BugReport_name)
        self.m_staticText17.SetLabel(gui_lib.msg.main_BugReport_text['text17'])
        self.m_button29.SetLabel(gui_lib.msg.main_BugReport_button['button29'])
        self.m_button30.SetLabel(gui_lib.msg.main_BugReport_button['button30'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl7.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
        self.device = device
        self.diagnostic = libs.udp.send('diagnostic', self.device.ip)
        time.sleep(0.2)
        self.status = libs.udp.send('status', self.device.ip)
        # time.sleep(0.2)
        # self.log = libs.udp.send('get_log', self.device.ip)

    def mail_send(self):
        conf = libs.DB.get_one_where(libs.models.Config, name='object_info')
        value = json.loads(conf.value)
        libs.sendmail.Gmail(self.log, 'grigor.kolev@gmail.com', value['object name'] + value['object adress'])
        return True

    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        log = u'<br>Статус:<br>' + str(self.status) + '<br><br>' + u'Диагностика:<br>' + str(
            self.diagnostic) + '<br><br>' + u'Лог:<br>' + str(self.log)
        msg = self.m_textCtrl7.GetValue()
        self.log = u'nom_in_l: ' + str(
            self.device.nom_in_l) + u'<br>IP: ' + self.device.ip + u'<br>Описание:<br>' + msg + '<br><br>' + log
        self.mail_send()
        self.Destroy()


class NewServer(gui.NewServer, gui_lib.keybords.Keyboard):  # @UndefinedVariable
    def __init__(self, parent):
        self.parent = parent
        gui.NewServer.__init__(self, parent)  # @UndefinedVariable
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl4.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl5.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
        self._localize()

    def _localize(self):
        self.SetLabel(gui_lib.msg.main_NewServer_name)
        self.m_staticText9.SetLabel(gui_lib.msg.main_NewServer_text['text9'])
        self.m_staticText10.SetLabel(gui_lib.msg.main_NewServer_text['text10'])
        self.m_textCtrl5.SetToolTip(gui_lib.msg.main_NewServer_tolltip['Ctrl5'])
        self.m_button17.SetLabel(gui_lib.msg.main_NewServer_button['button17'])
        self.m_button16.SetLabel(gui_lib.msg.main_NewServer_button['button16'])

    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        name = self.m_textCtrl4.GetValue()
        ip = self.m_textCtrl5.GetValue()
        kwargs = {name: ip}
        if name == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.EMPTY_FIELD)
            dial.ShowModal()
        elif ip == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.EMPTY_FIELD)
            dial.ShowModal()
        else:
            try:
                exec('%s = None' % (name))
            except SyntaxError:
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                dial.ShowModal()
            else:
                libs.conf.CONF.add_option('SERVER', **kwargs)
                libs.conf.ALL_SERVER[name] = ip
                self.Destroy()


class ServerSelect(gui.Server):  # @UndefinedVariable
    def __init__(self, parent):
        gui.Server.__init__(self, parent)  # @UndefinedVariable
        self.parent = parent
        self.m_checkBox3.SetValue(libs.conf.DB_IPTABLES)
        self.m_checkBox4.SetValue(libs.conf.TCP)
        self.m_checkBox5.SetValue(libs.conf.UDP_IV_JUMP)
        # self.m_checkBox4.SetValue(libs.conf.DINAMIC_IP)
        # reload(libs.conf)
        #         if libs.conf.FULSCREEAN is True:
        #         self.ShowFullScreen(libs.conf.FULSCREEAN )
        self._chouce()
        self._localize()

    def _localize(self):
        self.SetLabel(gui_lib.msg.main_ServerSelect_name)
        self.m_staticText5.SetLabel(gui_lib.msg.main_ServerSelect_text['Text5'])
        self.m_button6.SetLabel(gui_lib.msg.main_ServerSelect_button['button6'])
        self.m_checkBox3.SetLabel(gui_lib.msg.main_ServerSelect_button['checkBox3'])
        self.m_checkBox5.SetLabel(gui_lib.msg.main_ServerSelect_button['m_checkBox5'])
        self.m_bpButton3.SetToolTip(gui_lib.msg.main_ServerSelect_tolltip['button3'])
        self.m_checkBox3.SetToolTip(gui_lib.msg.main_ServerSelect_tolltip['checkBox3'])
        # self.m_checkBox4.SetToolTip(gui_lib.msg.main_ServerSelect_tolltip['m_checkBox4'])
        # self.m_checkBox4.SetLabel(gui_lib.msg.main_ServerSelect_button['m_checkBox4'])

    def _chouce(self):
        self.choices = ['']
        for i in libs.conf.ALL_SERVER:
            self.choices.append(i)
        self.m_choice1.SetItems(sorted(self.choices))
        self.m_choice1.SetSelection(0)

    def OnClose(self, event):
        # if libs.conf.DB_TUNNEL is True:
        #     libs.TUNNEL_SERVER.abort()
        #     time.sleep(1)
        # time.sleep(5)
        # libs.TUNNEL_SERVER[1].terminate()
        if self.parent != None:
            self.parent.m_checkBox1.SetValue(False)
        self.Destroy()

    def OnAdd(self, event):
        frame = NewServer(self)
        frame.ShowModal()
        # reload(libs.conf)
        self._chouce()

    def OnGo(self, event):
        ip = self.m_choice1.GetString(self.m_choice1.GetSelection())
        #         try:

        if ip == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return

        #         print ip
        #         except IndexError:
        #             dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
        #             dial.ShowModal()
        else:
            ip = libs.conf.CONF.get('SERVER', ip)
            #             print ip
            libs.conf.CONF.update_option('SERVER', use_server=ip)
            libs.conf.CONF.update_option('SYSTEM', db_iptables=self.m_checkBox3.GetValue())
            libs.conf.CONF.update_option('UDP', tcp=self.m_checkBox4.GetValue())
            libs.conf.CONF.update_option('UDP', iv_jump=self.m_checkBox5.GetValue())
            # libs.conf.CONF.update_option('SYSTEM', use_dinamic_ip=self.m_checkBox4.GetValue())
            libs.conf.DB_IPTABLES = self.m_checkBox3.GetValue()
            libs.restart_program()


class MessageDialog(wx.Dialog):
    def __init__(self, parent, message, title):
        wx.Dialog.__init__(self, parent, -1, title, size=(300, 120), style=wx.STAY_ON_TOP)
        self.CenterOnScreen(wx.BOTH)
        self.close = False
        ok = wx.Button(self, wx.ID_OK, "OK")
        ok.SetDefault()
        text = wx.StaticText(self, -1, message)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(text, 1, wx.ALIGN_CENTER|wx.TOP, 10)
        vbox.Add(ok, 1, wx.ALIGN_CENTER|wx.BOTTOM, 10)
        self.SetSizer(vbox)

    def OnClose(self, event):
        self.close = True
        self.Destroy()

class MainFrame(gui.MainFrame):

    def __init__(self, parent):
        self.parent = parent
        gui.MainFrame.__init__(self, parent)
        libs.conf.PARNET = self
        self.Maximize(True)
        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width * 0.85, self.height * 0.85))
        self.SetMinSize((self.width * 0.85, self.height * 0.85))
        self.USER = None
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Bind(wx.EVT_MAXIMIZE, self.on_resize)
        self.Bind(wx.EVT_SET_FOCUS, self.on_resize)
        self.ocr_run = False
        self.login_one_time = libs.DB.get_one_where(libs.models.Config, name='loggin')

        self.ocr_data = False
        client_id = libs.DB.get_one_where(libs.models.Config, name='nra_client_id')
        token = libs.DB.get_one_where(libs.models.Config, name='nra_token')
        if not client_id or not token:
            self.senf_to_nra = False
        elif not client_id.value or not token.value:
            self.senf_to_nra = False
        else:
            self.senf_to_nra = True
        self.ocr_worker = None
        if libs.conf.OCR_USE and libs.conf.OCR_LOCK is False:
            dlg = wx.MessageBox(gui_lib.msg.START_OCT, 'Info',
                                wx.YES_NO | wx.ICON_QUESTION)
            if dlg == wx.YES:
                self.OnOCRTaskStart(None)
        elif libs.conf.OCR_USE and libs.conf.OCR_LOCK is True:
            self.OnOCRTaskStart(None)
        self.help_name = ''
        self.all_ln = libs.chk_license()
        f1_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnHelp, id=f1_id)

        f2_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.reset_login_user, id=f2_id)
        f3_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.kill, id=f3_id)
        f4_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnOCRTaskStart, id=f4_id)
        f5_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnSSH, id=f5_id)
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('q'), f2_id),
                                         (wx.ACCEL_NORMAL, wx.WXK_F1, f1_id),
                                         (wx.ACCEL_NORMAL, wx.WXK_ESCAPE, f3_id),
                                         (wx.ACCEL_NORMAL, wx.WXK_HOME, f4_id),
                                         (wx.ACCEL_CTRL, ord('t'), f5_id),])
        self.SetAcceleratorTable(accel_tbl)
        self.SetFocus()

        self.SetTitle(libs.conf.CASINO_NAME)
        if libs.conf.FULSCREEAN is True:
            self.ShowFullScreen(True)
            self.SetWindowStyle(wx.STAY_ON_TOP)

        self.login = LoginPanel(self)
        self.login.Time_set_start()
        self.login.Show()

    def kill(self, event):
        try:
            self.login.Time_set_stop()
            self.OnOCRTaskStop(event)
        except:
            pass
        for sizerItem in self.GetChildren():
            if (
                    type(sizerItem) == MainPanel or
                    type(sizerItem) == report.mashin_report.RealTimeLock or
                    type(sizerItem) == report.mashin_report.BonusLock or
                    type(sizerItem) == order.main.Order or
                    type(sizerItem) == config.main.MainConf or
                    type(sizerItem) == report.main.Main or
                    type(sizerItem) == order.mex_chk.MexCheck or
                    type(sizerItem) == cust.main.Main or
                    type(sizerItem) == users.main.UserConf or
                    type(sizerItem) == mashin.main.Mashin or
                    type(sizerItem) == config.main.Sys or
                    type(sizerItem) == licenz.main.Licenz or
                    type(sizerItem) == servises.main.Main

            ):
                try:
                    sizerItem.Destroy()
                except:
                    pass
        self.Destroy()
        sys.exit(9)

    def OnSSH(self, event):
        if os.name == 'posix':
            if os.uname()[-1] == 'armv7l':
                cmd = "lxterminal -t %s -e ssh -p 44554 colibri@%s" % (libs.conf.CASINO_NAME ,libs.conf.SERVER)
            else:
                cmd = "mate-terminal -t %s -x ssh -p 44554 colibri@%s" % (libs.conf.CASINO_NAME ,libs.conf.SERVER)
            os.popen(cmd)
        return True

    def OnOCRTaskStart(self, event):
        if libs.conf.OCR_USE is True and not self.ocr_worker:
            if event:
                dial = wx.MessageDialog(self, *gui_lib.msg.OCR_START)
                dial.ShowModal()
            self.ocr_worker = task.OCTRead(self, port=libs.conf.OCR_PORT)
            task.EVT_OCR_DATA(self, self.OnOCRData)


    def OnOCRTaskStop(self, event):
        if libs.conf.OCR_USE is True and self.ocr_worker:
            try:
                self.ocr_worker.abort()
            except:
                pass

    def OnOCRData(self, event):
        # print event.data
        self.ocr_data = event.data
        if self.ocr_data == False or self.ocr_run is True:
            pass
        elif self.ocr_data[0] == 'CANT_PLAY':
            # dial = MessageDialog(self, gui_lib.msg.CANT_PLAY[0], gui_lib.msg.conf_NRA['name'])
            # wx.CallLater(5000, dial.Destroy)
            # dial.ShowModal()
            play_sound()
            self.ocr_run = True
            dial = wx.MessageDialog(self, *gui_lib.msg.CANT_PLAY)
            dial.ShowModal()
            self.ocr_run = False
        elif self.ocr_data[0] == 'EXPIRED':
            play_sound()
            dial = wx.MessageDialog(self, *gui_lib.msg.CART_EXPIRED)
            dial.ShowModal()
        elif self.ocr_data[0] == 'DISABLE' and self.senf_to_nra is True:
            # dial = MessageDialog(self, gui_lib.msg.IN_NRA[0], gui_lib.msg.conf_NRA['name'])
            # wx.CallLater(5000, dial.Destroy)
            # dial.ShowModal()
            play_sound()
            self.ocr_run = True
            dial = wx.MessageDialog(self, *gui_lib.msg.IN_NRA)
            dial.ShowModal()
            self.ocr_run = False
        elif self.ocr_data[0] == 'LITLE':
            play_sound()
            # dial = MessageDialog(self, gui_lib.msg.EGN_NO_YEARS[0], gui_lib.msg.conf_NRA['name'])
            # wx.CallLater(5000, dial.Destroy)
            # dial.ShowModal()
            self.ocr_run = True
            dial = wx.MessageDialog(self, *gui_lib.msg.EGN_NO_YEARS)
            dial.ShowModal()
            self.ocr_run = False
        elif self.ocr_data[0] == 'ERROR' and self.senf_to_nra is True:
            play_sound('alarm_ringing_2.wav')
            # dial = MessageDialog(self, gui_lib.msg.IN_NRA_ERROR[0], gui_lib.msg.conf_NRA['name'])
            # wx.CallLater(5000, dial.Destroy)
            # dial.ShowModal()
            self.ocr_run = True
            dial = wx.MessageDialog(self, *gui_lib.msg.IN_NRA_ERROR)
            dial.ShowModal()
            self.ocr_run = False

        else:
            if self.senf_to_nra is True:
                self.ocr_run = True
                dial = MessageDialog(self, gui_lib.msg.NOT_IN_NRA[0], gui_lib.msg.conf_NRA['name'])
                wx.CallLater(5000, dial.Destroy)
                dial.ShowModal()
                self.ocr_run = False
        # print self.ocr_data
        # print self.ocr_data, 'event'

    def mashin_list_refresh(self):
        self.login.panel.mashin_list_refresh()

    def reset_login_user(self, event):
        # print 1
        cleen_login = CleanLogedIn(self)
        cleen_login.ShowModal()

    def OnHelp(self, event):
        # wx.LaunchDefaultApplication('docs/%s/index.html' % (libs.conf.USE_LANGUAGE))
        if libs.conf.DOCS_DEBUG is False:
            if self.help_name == '':
                frame = libs.helps.Help(r'%s%s/index.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE))
            else:
                frame = libs.helps.Help(r'%s%s/colibri/v%s/%s' % (
                libs.conf.DOCS, libs.conf.USE_LANGUAGE, libs.conf.VERSION, self.help_name))
        else:
            if self.help_name == '':
                frame = libs.helps.Help('http://127.0.0.1:5000/%s/index.html' % (libs.conf.USE_LANGUAGE))
            else:
                frame = libs.helps.Help('http://127.0.0.1:5000/%s/colibri_v2/v%s/%s' % (
                libs.conf.USE_LANGUAGE, libs.conf.VERSION, self.help_name))

    def Login_chk(self, event):
        # if self.login_one_time.value == 'True':
        # libs.DB.expire(self.USER)
        if event.data is True:
            if self.USER != None:
                self.login.panel.OnLogOut(event)
                self.all_close(event)
                self.login_show()

        # self.hide_panel()
        # self.login.panel.OnClose()
        # self.show_panel()
        # self.parent.show_panel()

    def show_panel(self):
        try:
            self.login.panel.Show()
            self.SetLabel(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.main_MainPanel_name)
        except Exception:
            pass

    def hide_panel(self):
        try:
            self.login._user_choice()
            self.login.panel.Hide()
        except Exception:
            pass

    def all_mashin(self):
        try:
            return self.login.panel.all_mashin
        except Exception:
            pass

    def rfid_task_start(self, event):
        self.login.OnTaskRun(event)

    def rfid_task_stop(self, event):
        self.login.OnTaskStop(event)

    def rfid_unbind(self):
        self.login.read_cart = True

    def rfid_bind(self, obj):
        self.login.read_cart = obj

    def rfid_task(self):
        try:
            return self.login.worker
        except AttributeError:
            return None

    def OnConfig(self, event):
        try:
            self.login.panel.OnConfig(event)
        except Exception:
            pass

    def login_user_refresh(self):
        #         libs.DB.expire()
        try:
            self.login.m_textCtrl5.SetValue('')
            self.login._user_choice()
        except Exception:
            pass

    def login_user_choiser(self):
        try:
            return self.login.m_choice1Choices
        except Exception:
            pass

    def all_mashin_refresh(self):
        #         libs.DB.expire()
        try:
            self.login.panel.mashin_list_refresh()
        except Exception:
            pass

    def login_show(self):
        try:
            self.login.Time_set_start()
            self.login.Show()
        except Exception:
            pass

    def login_hide(self):
        try:
            self.login.Time_set_stop()
            self.login.Hide()
        except Exception:
            pass

    def panel_kasa_refresh(self):
        libs.DB.expire()
        try:
            self.login.panel.kasa_refresh()
        except Exception:
            pass

    def on_resize(self, event):
        for sizerItem in self.GetChildren():
            # try:
            #     wx.PostEvent(sizerItem, event)
            # except TypeError:
            #     pass
            if (type(sizerItem) == LoginPanel or
                    type(sizerItem) == MainPanel or
                    type(sizerItem) == report.mashin_report.RealTimeLock or
                    type(sizerItem) == report.mashin_report.BonusLock or
                    type(sizerItem) == order.main.Order or
                    type(sizerItem) == config.main.MainConf or
                    type(sizerItem) == report.main.Main or
                    type(sizerItem) == order.mex_chk.MexCheck or
                    type(sizerItem) == cust.main.Main or
                    type(sizerItem) == users.main.UserConf or
                    type(sizerItem) == mashin.main.Mashin or
                    type(sizerItem) == config.main.Sys or
                    type(sizerItem) == licenz.main.Licenz or
                    type(sizerItem) == servises.main.Main

            ):
                wx.PostEvent(sizerItem, event)
        event.Skip()

    def all_close(self, event):
        # try:
        #     if self.login_one_time.value == 'True':
        #         self.login.panel.login_worker.abort()
        #         self.login.panel.login_worker.LOGIN_EVENT.set()
        # except AttributeError:
        #     pass
        if self.USER != None:
            self.USER.login = False
            libs.DB.add_object_to_session(self.USER)
            try:
                libs.DB.commit()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
        for sizerItem in self.GetChildren():
            if (
                    type(sizerItem) == MainPanel or
                    type(sizerItem) == report.mashin_report.RealTimeLock or
                    type(sizerItem) == report.mashin_report.BonusLock or
                    type(sizerItem) == order.main.Order or
                    type(sizerItem) == config.main.MainConf or
                    type(sizerItem) == report.main.Main or
                    type(sizerItem) == order.mex_chk.MexCheck or
                    type(sizerItem) == cust.main.Main or
                    type(sizerItem) == users.main.UserConf or
                    type(sizerItem) == mashin.main.Mashin or
                    type(sizerItem) == config.main.Sys or
                    type(sizerItem) == licenz.main.Licenz or
                    type(sizerItem) == servises.main.Main

            ):
                sizerItem.OnClose(event)
        self.login_show()

    def OnClose(self, event):
        self.OnOCRTaskStop(event)
        try:
            self.login.Time_set_stop()
            self.login.panel.login_worker.abort()
            self.login.panel.login_worker.LOGIN_EVENT.set()
        except AttributeError:
            pass
        try:
            if self.USER != None:
                self.USER.login = False
                libs.DB.add_object_to_session(self.USER)
            libs.udp.send('pos_inactive', ip=libs.conf.SERVER, pos_id=libs.conf.ID, timeout=5)
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
        for sizerItem in self.GetChildren():
            # try:
            #     wx.PostEvent(sizerItem, wx.EVT_CLOSE)
            # except TypeError:
            #     pass
            if (type(sizerItem) == LoginPanel or
                    type(sizerItem) == MainPanel or
                    type(sizerItem) == report.mashin_report.RealTimeLock or
                    type(sizerItem) == report.mashin_report.BonusLock or
                    type(sizerItem) == order.main.Order or
                    type(sizerItem) == config.main.MainConf or
                    type(sizerItem) == report.main.Main or
                    type(sizerItem) == order.mex_chk.MexCheck or
                    type(sizerItem) == cust.main.Main or
                    type(sizerItem) == users.main.UserConf or
                    type(sizerItem) == mashin.main.Mashin or
                    type(sizerItem) == config.main.Sys or
                    type(sizerItem) == licenz.main.Licenz or
                    type(sizerItem) == servises.main.Main

            ):
                try:
                    sizerItem.OnClose(event)
                except Exception as e:
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
        #         #                     pass
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
        # event.Veto()
        # time.sleep(5)
        # libs.TUNNEL_SERVER[1].terminate()
        # if libs.conf.DB_TUNNEL is True:
        #     time.sleep(1)
        #     libs.TUNNEL_SERVER.abort()
        self.Destroy()
        # self.Close()


class LoginPanel(gui.LoginPanel, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        gui.LoginPanel.__init__(self, parent)
        #         self.width, self.height = wx.GetDisplaySize()
        #         self.SetSize((self.width, self.height))
        self.parent = parent
        self.parent.help_name = 'login.html'
        self._user_choice()
        self.read_cart = True
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl5.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)
        self.with_rfid_in = libs.conf.RFID_LOGIN
        self.worker = None
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.m_button7.Disable()
        if libs.conf.RFID_USE_WORK is False:
            self.m_button7.Hide()

        if self.with_rfid_in is True:
            self.m_button7.SetToolTip(gui_lib.msg.main_LoginPanel_tolltip['m_button7_1'])
            self.m_staticText5.Hide()
            self.m_choice1.Hide()
            self.m_textCtrl5.Hide()
            self.m_button6.Hide()
            # self.m_button7.SetLabel(_(u'Вход с парола'))
            # self.m_staticText6.SetLabel(_(u'Моля поставете карта'))
            self.OnTaskRun(None)
        else:
            self.m_button7.SetToolTip(gui_lib.msg.main_LoginPanel_tolltip['m_button7'])
            self.m_staticText5.Show()
            self.m_choice1.Show()
            self.m_textCtrl5.Show()
            self.m_button6.Show()
            # self.m_button7.SetLabel(_(u'Вход с карта'))
            # self.m_staticText6.SetLabel(_(u'Парола'))
        self._localize()
        self.cart_error = 0

        #         self.Layout()
        self.on_resize(None)
        # self.Time_set_start()

    def Time_set_stop(self):
        self.set_timeworker.abort()

    def Time_set_start(self):
        self.set_timeworker = task.SetTime(self)
        # self.set_timeworker.start()
        task.EVT_SET_TIME(self, self.OnAddTime)

    #         self.DBResycle()
    #         self.Fit()
    def OnAddTime(self, event):
        # print(e)vent.data
        self.m_staticText61.SetLabel(event.data)

    def _localize(self):
        self.parent.SetTitle(libs.conf.CASINO_NAME)
        self.m_staticText5.SetLabel(gui_lib.msg.main_LoginPanel_text['Text5'])
        self.m_button6.SetLabel(gui_lib.msg.main_LoginPanel_button['button6'])
        self.m_checkBox1.SetLabel(gui_lib.msg.main_LoginPanel_button['checkBox1'])
        self.m_checkBox1.SetToolTip(gui_lib.msg.main_LoginPanel_tolltip['checkBox1'])
        # self.m_choice1.SetToolTip(gui_lib.msg.login_tooltip_m_choice1)
        # self.m_textCtrl5.SetToolTip(gui_lib.msg.login_tooltip_m_textCtrl5)
        # self.m_button6.SetToolTip(gui_lib.msg.login_tooltip_m_button6)
        if self.with_rfid_in is False:
            self.m_button7.SetLabel(gui_lib.msg.main_LoginPanel_button['button7'])
            # self.m_button7.SetToolTip(gui_lib.msg.login_tooltip_m_button7)
            self.m_staticText6.SetLabel(gui_lib.msg.main_LoginPanel_text['Text6'])
        else:
            self.m_staticText6.SetLabel(gui_lib.msg.main_LoginPanel_text['Text6_1'])
            self.m_button7.SetLabel(gui_lib.msg.main_LoginPanel_button['button7_1'])
            # self.m_button7.SetLabel(gui_lib.msg.login_rfid_m_button7)
            # self.m_button7.SetToolTip(gui_lib.msg.login_tooltip_rfid_m_button7)
            # self.m_staticText6.SetLabel(gui_lib.msg.login_rfid_m_staticText6)

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        self.SetSize((self.width, self.height))
        self.SetMinSize((self.width, self.height))

        #         for sizerItem in self.GetChildren():
        #             if type(sizerItem) == MainPanel:
        #                 wx.PostEvent(sizerItem, event)
        if event != None:
            event.Skip()
            self.Layout()

    def _user_choice(self):
        libs.DB.expire()
        self.users_obj = libs.DB.get_all_where(libs.models.User, order='name', enable=True)
        self.m_choice1Choices = ['']
        for i in self.users_obj:
            self.m_choice1Choices.append(i.name)
        #         self.m_choice1Choices = self.m_choice1Choices
        self.m_choice1.SetItems(self.m_choice1Choices)
        self.m_choice1.SetSelection(0)
        self.Fit()

    def OnClose(self, event):
        self.parent.help_name = ''
        self.OnTaskStop(event)
        self.Time_set_stop()
        # try:
        libs.DB.commit()
        # except Exception as e:
        #     print(e)
        # libs.DB.close()
        self.Destroy()

    def OnIn(self, event):
        libs.DB.expire()
        self.parent.login_one_time = libs.DB.get_one_where(libs.models.Config, name='loggin')
        time_chk = libs.chk_time()
        if time_chk is not True:
            MyFrame = wx.MessageDialog(None, gui_lib.msg.bad_rtc_server + time_chk, gui_lib.msg.on_run_error,
                                       wx.OK | wx.ICON_ERROR)
            MyFrame.ShowModal()
            dial = SetMyTime(self)
            dial.ShowModal()
            return False
        self.parent.all_ln = libs.chk_license()
        chk = self.parent.all_ln['base']
        if chk == 'NO':
            dial = wx.MessageDialog(None, *gui_lib.msg.NO_LICENSE)
            dial.ShowModal()
            dial = licenz.main.Active(None)
            dial.ShowModal()
            return False
        elif chk == 'END':
            dial = wx.MessageDialog(None, *gui_lib.msg.LICENSE_END_TIME)
            dial.ShowModal()
            dial = licenz.main.Active(None)
            dial.ShowModal()
            return False
        elif chk == 'BAD NAME':
            dial = wx.MessageDialog(None, *gui_lib.msg.BAD_LICENSE_NAME)
            dial.ShowModal()
            dial = licenz.main.Active(None)
            dial.ShowModal()
            return False
        # elif chk == 'END_TIME':
        #     dial = wx.MessageDialog(None, *gui_lib.msg.END_LICENSE_TIME)
        #     dial.ShowModal()
        else:
            pass
        valid_to = libs.DB.get_one_where(libs.models.Config, name='nra_token_valid')
        if valid_to:
            if valid_to.value:
                date = valid_to.value
                date = libs.models.TZ.str_to_date(date, '%Y-%m-%d')
                date = libs.models.TZ.go_back_from_date(date, back=15)
                new_date = libs.models.TZ.now()
                # raise KeyError (date, new_date)
                if date <= new_date:
                    dial = wx.MessageDialog(None, *gui_lib.msg.TOKEN_END)
                    dial.ShowModal()
        for i in self.parent.all_ln:
            # print self.parent.all_ln[i], i
            if self.parent.all_ln[i] == 'END_TIME':
                dial = wx.MessageDialog(None, *gui_lib.msg.END_LICENSE_TIME)
                dial.ShowModal()
                break
        pos = libs.DB.get_pos()
        # libs.DB.expire(pos)
        if pos != None:
            pos = json.loads(pos.value)
            if libs.conf.ID not in pos:
                MyFrame = RegisterKey(None, libs.conf.ID)
                MyFrame.ShowModal()
                libs.restart_program()
        else:
            pos = libs.DB.make_obj(libs.models.Config)
            # libs.DB.expire(pos)
            pos.name = 'pos'
            pos.value = json.dumps({libs.conf.ID: 'INIT'})
            libs.DB.add_object_to_session(pos)
            libs.DB.commit()
        rev = libs.DB.get_one_where(libs.models.Config, name='MinGuiRev')
        # libs.DB.expire(rev)
        if rev == None:
            rev = libs.DB.make_obj(libs.models.Config)
            rev.name = 'MinGuiRev'
            rev.value = '0'
            libs.DB.add_object_to_session(rev)
            libs.DB.commit()
        if int(libs.conf.REV) < int(rev.value):
            dial = wx.MessageDialog(None, *gui_lib.msg.SYSTEM_UPDATE)
            dial.ShowModal()
            # print 'update'
            if os.name == 'posix':
                if os.uname()[-1] == 'armv7l':
                    local_folder = '/home/olimex/.colibri_v2'
                    svn_folder = 'svn://NEW_SVN_IP/home/svn/ColibriCMS_BIN/2_1/ARM/'
                else:
                    import platform
                    local_folder = '/home/%s/.colibri_v2' % (os.environ['USER'])
                    # if platform.architecture()[0] == '64bit':
                    svn_folder = 'svn://NEW_SVN_IP/home/svn/ColibriCMS_BIN/2_1/Linux_64/'
                    # else:
                    #     svn_folder = 'svn://NEW_SVN_IP/home/svn/ColibriCMS_BIN/2_1/Linux_32/'
            else:
                from os.path import expanduser
                home = expanduser("~")
                local_folder = home + r'/colibri_v2'
                svn_folder = 'svn://NEW_SVN_IP/home/svn/ColibriCMS_BIN/2_1/Windows/'

            svn = libs.subversion.SubVersion(local_folder, svn_folder, 'smib', 'smib_update')

            if os.name == 'posix':
                svn.checkout()
                revision = svn.update(rev=(rev.value))
            else:
                revision = rev.value
            libs.conf.CONF.update_option('SYSTEM', rev=revision)
            err = libs.DB.make_obj(libs.models.GetCounterError)
            if os.name == 'posix':
                err.info = 'UPDATE POS' + ': ' + u'POS %s UPDATE min %s revision %s' % (
                    libs.conf.ID, rev.value, libs.conf.REV)
            else:
                err.info = 'UPDATE POS' + ': ' + u'POS %s UPDATE min %s FROM revision %s' % (
                    libs.conf.ID, rev.value, libs.conf.REV)
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            if os.name == 'posix':
                dial = wx.MessageDialog(None, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
                libs.restart_program()
            else:

                dial = wx.MessageDialog(None, *gui_lib.msg.RUN_PROGRAM)
                dial.ShowModal()

                import subprocess
                subprocess.run(local_folder + r'\Update.exe %s' % (rev.value), shell=True)
                self.parent.OnClose(None)
                return
        else:
            if self.with_rfid_in is False:
                user = self.m_choice1.GetString(self.m_choice1.GetSelection())
                passwd = self.m_textCtrl5.GetValue()
                if user == '':
                    dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
                    dial.ShowModal()
                else:
                    user = libs.DB.get_one_where(libs.models.User, name=user)
                    if user.passwd != passwd:
                        dial = wx.MessageDialog(self, *gui_lib.msg.PASSWD_WRONG)
                        dial.ShowModal()
                    elif user.login is True and self.parent.login_one_time.value == 'True':
                        dial = wx.MessageDialog(self, *gui_lib.msg.USER_IS_LOGIN)
                        dial.ShowModal()
                    else:
                        user.login = True
                        libs.DB.add_object_to_session(user)
                        libs.DB.commit()
                        self.parent.USER = user
                        self.Time_set_stop()
                        self.Hide()
                        self.panel = MainPanel(self.parent)
                        self.panel.Show()

            else:
                if self.parent.USER == None:
                    try:
                        if event.data == None:
                            event.data = ''
                        self.parent.USER = libs.DB.get_one_where(libs.models.User, cart=event.data, enable=True)
                    except SyntaxError:
                        pass
                    else:
                        if self.parent.USER == None:
                            try:
                                self.parent.all_close(event)
                                self.Show()
                            except AttributeError:
                                pass
                        else:
                            self.Time_set_stop()
                            self.Hide()
                            # self.OnTaskStop(None)
                            self.panel = MainPanel(self.parent)
                            self.panel.Show()

    def OnCard(self, event):
        # print(e)vent.data
        if self.read_cart is not True and self.parent.USER.cart != event.data:
            self.read_cart.OnCard(event)

        else:
            if self.parent.USER != None:
                if event.data == 'ERROR':
                    pass
                elif not event.data:
                    self.parent.USER = None
                    self.OnIn(event)
                else:
                    self.OnIn(event)
                    if self.parent.USER.cart != event.data:  # @UndefinedVariable
                        # self.cart_error += 1
                        # if self.cart_error > 3:
                        libs.DB.commit()
                        libs.DB.expire()
                        self.parent.USER = None
                            #                         self.Show()
                            #                         libs.DB.close()
                        self.OnIn(event)
                    # else:
                    #     self.cart_error = 0
            else:
                if event.data != None:
                    self.cart_error = 0
                    self.OnIn(event)

    def OnInWithCart(self, event):
        if self.with_rfid_in is False:
            self.m_button7.SetToolTip(gui_lib.msg.main_LoginPanel_tolltip['m_button7_1'])
            libs.conf.CONF.update_option('RFID', login=True)
            self.with_rfid_in = True
        else:
            libs.conf.CONF.update_option('RFID', login=False)
            self.m_button7.SetToolTip(gui_lib.msg.main_LoginPanel_tolltip['m_button7'])
            self.with_rfid_in = False

        if self.with_rfid_in is True:
            self.m_staticText5.Hide()
            self.m_choice1.Hide()
            self.m_textCtrl5.Hide()
            self.m_button6.Hide()

            self.m_staticText6.SetLabel(gui_lib.msg.main_LoginPanel_text['Text6_1'])
            self.m_button7.SetLabel(gui_lib.msg.main_LoginPanel_button['button7_1'])
            self.OnTaskRun(event)
        elif self.with_rfid_in is False:
            self.OnTaskStop(event)
            self.m_staticText5.Show()
            self.m_choice1.Show()
            self.m_textCtrl5.Show()
            self.m_button6.Show()

            self.m_button7.SetLabel(gui_lib.msg.main_LoginPanel_button['button7'])
            self.m_staticText6.SetLabel(gui_lib.msg.main_LoginPanel_text['Text6'])
        self._localize()
        self.Fit()
        # self.Layout()

    #     def DBResycle(self):
    #         self.db_recycle = task.DBConnectionRecycle(q)

    def OnTaskRun(self, event):
        self.worker = users.task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT, post_false=True)
        users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)

    # def OnCartBing(self, obj, function):
    #     users.task.EVT_WORK_RFID_RESULT(self, self.Empty)
    #     users.task.EVT_WORK_RFID_RESULT(obj, function)
    #
    # def Empty(self, event):
    #     event.Skip()
    #
    # def OnCartUnBing(self):
    #     users.task.EVT_WORK_RFID_RESULT(self, self.OnCard)

    def OnTaskStop(self, event):
        """Stop Computation."""
        # Flag the worker thread to stop if running
        if self.worker:
            self.worker.abort()
        self.worker = None

    def OnServer(self, event):
        dialog = ServerSelect(self)
        dialog.ShowModal()


class KSChangeGuage(gui.KSChangeGuage):
    def __init__(self, parent, mashin, cart, user_id):
        self.parent = parent
        self.user_id = user_id
        gui.KSChangeGuage.__init__(self, self.parent)
        self.SetTitle(gui_lib.msg.main_KSChangeGuage_name)
        self.m_button21.SetLabel(gui_lib.msg.main_KSChangeGuage_button['button21'])
        self.m_staticText16.SetLabel(gui_lib.msg.main_KSChangeGuage_text['Text16'] + u': ')
        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width // 2, -1))
        self.m_gauge1.SetMinSize((self.width // 2, -1))
        self.cart = cart
        self.mashin = mashin
        self.SetTitle(gui_lib.msg.main_MainPanel_text[21])
        self.m_gauge1.SetRange(len(self.mashin))
        # self.m_button21.Disable()
        self.loop = 0
        self.worker = task.WorkStart(self, self.mashin, self.cart, self.user_id)  # @UndefinedVariable
        task.EVT_KS_CHANGE(self, self.GetCount)

    def GetCount(self, event):
        if type(event.data) == int:
            self.loop = self.loop + 1
            # self.m_staticText16.SetLabel(gui_lib.msg.main_KSChangeGuage_text['Text16'] + u': ')
            self.m_staticText16.SetLabel(
                gui_lib.msg.main_KSChangeGuage_text['Text16'] + u': ' + str(event.data) + ' ' +
                gui_lib.msg.main_KSChangeGuage_text['msg_ok'])
            self.m_gauge1.SetValue(self.loop)
        if type(event.data) == list:
            self.loop = self.loop + 1
            self.m_staticText16.SetLabel(
                gui_lib.msg.main_KSChangeGuage_text['Text16'] + u': ' + str(event.data[0]) + ' ' +
                gui_lib.msg.main_KSChangeGuage_text['no_ok'])
            self.m_gauge1.SetValue(self.loop)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            # self.m_button21.Enable()

    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.worker.is_alive():
            self.worker.abort()

    def OnClose(self, event):
        self.OnTaskStop(event)
        self.Destroy()


# class GetBonusCartLog(gui.Diagnostic):
#     def __init__(self, parent, mashin):
#         self.parent = parent
#         gui.Diagnostic.__init__(self, parent)
#         self.width, self.height = self.parent.GetParent().GetSize()
#         self.SetSize((self.width*0.4, self.width*0.4))
#         self.m_richText2.SetMinSize((self.width*0.38, self.width*0.33))
#         self.info = libs.udp.send('BONUS_CART_GET_LOG', ip=mashin.ip)
#         text = ''
#         if self.info != None:
#             for i in self.info:
#                 text += i + ' : ' + self.info['mony'] + '\n'
#         else:
#             text = _(u'Няма връзка!')
#
#         self.m_richText2.SetValue(text)
# #         print self.info
#
#     def OnClose(self, event):
#         self.Destroy()

# class Diagnostic(gui.Diagnostic):
#     def __init__(self, parent, mashin):
#         self.parent = parent
#         gui.Diagnostic.__init__(self, parent)
#         self.width, self.height = self.parent.GetParent().GetSize()
#         self.SetSize((self.width*0.4, self.width*0.4))
#         self.m_richText2.SetMinSize((self.width*0.38, self.width*0.33))
#         self.info = libs.udp.send('diagnostic', ip=mashin.ip)
#         if self.info != None:
#             text = 'Status: ' + str(self.info[0]) + '\n'
#             text = text + 'TEMP: ' + str(self.info[1]['TEMP']) + '\n'
#             text = text + 'POWER V: ' + str(self.info[1]['POWER V']) + '\n'
#             text = text + 'POWER A: ' + str(self.info[1]['POWER A']) + '\n'
#
#             text = text + 'SAS PROC: ' + str(self.info[1]['SAS PROC']) + '\n'
#             text = text + 'SAS EVENT: ' + str(self.info[1]['SAS EVENT']) + '\n'
#             text = text + 'SAS CONNECTION: ' + str(self.info[1]['SAS CONNECTION']) + '\n'
#
#             text = text + 'RFID PROC: ' + str(self.info[1]['RFID PROC']) + '\n'
#             text = text + 'RFID EVENT: ' + str(self.info[1]['RFID EVENT']) + '\n'
#             text = text + 'RFID CONNECTED: ' + str(self.info[1]['RFID CONECTED']) + '\n'
#
#             text = text + 'KEY SYSTEM PROC: ' + str(self.info[1]['KEY SISTEM PROK']) + '\n'
#             text = text + 'KEY SYSTEM EVENT: ' + str(self.info[1]['KEY SISTEM EVENT']) + '\n'
#             text = text + 'RELAY CONNEECTED: ' + str(self.info[1]['RELAY CONNEECTED']) + '\n'
#
#             text = text + 'BONUS CART PROC: ' + str(self.info[1]['BONUS CART PROC']) + '\n'
#             text = text + 'BONUS CART EVENT: ' + str(self.info[1]['BONUS CART EVENT']) + '\n'
#         else:
#             text = _(u'Няма връзка!')
#
#         self.m_richText2.SetValue(text)
# #         print self.info
#
#     def OnClose(self, event):
#         self.Destroy()

class PasswdChange(users.gui.AddUser, gui_lib.keybords.Keyboard):
    def __init__(self, parent, user):
        self.parent = parent
        self.user = user
        users.gui.AddUser.__init__(self, parent)
        self.m_textCtrl10.SetEditable(False)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl7.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)
            self.m_textCtrl8.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)
        self.m_radioBtn3.Hide()
        self.m_staticText11.Hide()
        self.m_choice3.Hide()
        self.m_button7.Hide()
        self.SetTitle(gui_lib.msg.main_PasswdChange_name)
        self.m_staticText14.SetLabel(gui_lib.msg.main_PasswdChange_text['Text14'])
        self.m_staticText9.SetLabel(gui_lib.msg.main_PasswdChange_text['Text9'])
        self.m_staticText10.SetLabel(gui_lib.msg.main_PasswdChange_text['Text10'])

        self.m_textCtrl10.SetValue(self.user.name)
        self.m_textCtrl8.Bind(wx.EVT_TEXT_ENTER, self.OnSave)
        self.Layout()

    def OnClose(self, event):
        self.Destroy()

    def OnSave(self, event):
        pass_1 = self.m_textCtrl7.GetValue()
        pass_2 = self.m_textCtrl8.GetValue()
        if pass_1 != pass_2:
            self.m_textCtrl7.SetForegroundColour(wx.Colour(199, 16, 29))
            self.m_textCtrl8.SetForegroundColour(wx.Colour(199, 16, 29))
            #             wx.MessageBox(*gui_lib.msg.PASSWD_WRONG)
            dial = wx.MessageDialog(self, *gui_lib.msg.PASSWD_WRONG)
            dial.ShowModal()
        elif pass_1 == '':
            #             wx.MessageBox(*gui_lib.msg.EMPTY_FIELD)
            dial = wx.MessageDialog(self, *gui_lib.msg.EMPTY_FIELD)
            dial.ShowModal()
        else:
            self.user.passwd = pass_1
            libs.DB.add_object_to_session(self.user)
            try:
                libs.DB.commit()
                self.OnClose(event)
                return True
            except Exception as e:
                libs.DB.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
            return False


class MainPanel(gui.MainPanel):  # @UndefinedVariable
    def __init__(self, parent):
        gui.MainPanel.__init__(self, parent)  # @UndefinedVariable
        self.parent = parent
        self.parent.help_name = 'main.html'
        self._localize()
        self.resize = True

        self._set_right()
        # self.m_button7.Hide()
        # self.m_button13.Hide()
        # self._localize()
        self.width, self.height = self.parent.GetSize()
        self.mashin_list_refresh(None)
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.m_listCtrl4.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['m_listCtrl4'])
        # self.parent.USER.session = time.time()
        if self.parent.login_one_time.value == 'True':
            self.login_worker = task.LogOut(self, self.parent.USER.id)
            task.EVT_LOGOUT(self, self.parent.Login_chk)
        passwd_change_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnPasswordChange, id=passwd_change_id)
        select_all = wx.NewId()
        self.Bind(wx.EVT_MENU, self.SelectAll, id=select_all)

        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('a'), select_all),
                                         (wx.ACCEL_CTRL, ord('p'), passwd_change_id)])
        self.SetAcceleratorTable(accel_tbl)
        # accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('a'), select_all)])
        # self.SetAcceleratorTable(accel_tbl)
        # self.Fit()

    # def login_check(self):
    #     if self.parent.login_one_time.value == 'True':
    #         libs.DB.expire(self.parent.USER)
    #         if self.parnet.USER.login is True:

    def SelectAll(self, event):
        for i in range(self.m_listCtrl4.GetItemCount()):
            self.m_listCtrl4.Select(i)

    def OnPasswordChange(self, event):
        dial = PasswdChange(self, self.parent.USER)
        dial.ShowModal()

    def OnShowMSG(self, event):
        libs.DB.expire()
        dial = order.main.MSGAdd(self, edit=False)
        dial.ShowModal()
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()

    def _localize(self):
        self.m_staticText10.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['text10'])
        msg = libs.DB.get_one_where(libs.models.Config, name='admin_msg')
        if msg == None:
            self.m_staticText15.SetLabel(u'')
        elif msg.value == None or msg.value == u'':
            self.m_staticText15.SetLabel(u'')
        else:
            self.m_staticText15.SetLabel(
                gui_lib.msg.main_MainPanel_text[15] + u': ' + str(gui_lib.msg.main_MainPanel_text['yes']))
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.main_MainPanel_name)
        self.m_staticText10.SetLabel(
            gui_lib.msg.main_MainPanel_text[1] + u' ID ' + str(self.parent.USER.id) + u': ' + self.parent.USER.name)
        if self.parent.USER.flor_id == None:  # @UndefinedVariable
            self.m_staticText11.SetLabel(
                gui_lib.msg.main_MainPanel_text[2] + u': ' + gui_lib.msg.main_MainPanel_text[4])
        else:
            #             self.flor = mashin.db_ctrl.flor_get_id(USER.flor)  # @UndefinedVariable
            self.m_staticText11.SetLabel(gui_lib.msg.main_MainPanel_text[2] + u': ' + self.parent.USER.flor.name)
        self.m_staticText8.SetLabel(gui_lib.msg.main_MainPanel_text[3] + u': ' + str(self.parent.USER.kasa))

        self.m_listCtrl4.InsertColumn(0, gui_lib.msg.main_MainPanel_text[5])
        self.m_listCtrl4.InsertColumn(1, gui_lib.msg.main_MainPanel_text[6])
        self.m_listCtrl4.InsertColumn(2, gui_lib.msg.main_MainPanel_text[7])
        self.m_listCtrl4.InsertColumn(3, gui_lib.msg.main_MainPanel_text[8])
        self.m_listCtrl4.InsertColumn(4, gui_lib.msg.main_MainPanel_text[9])
        self.m_listCtrl4.InsertColumn(5, gui_lib.msg.main_MainPanel_text[10])

        self.Fit()

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        self.m_toolBar2.SetMinSize((self.width, -1))
        self.m_listCtrl4.SetMinSize((self.width * 0.80, self.height * 0.58))
        # self.m_listCtrl4.AlwaysShowScrollbars()
        # self.m_listCtrl4.EnsureVisible(self.m_listCtrl4.GetItemCount() - 1)
        self.m_scrolledWindow1.SetMinSize((self.width * 0.17, self.height * 0.58))
        self.m_listCtrl4.SetColumnWidth(0, self.width * 0.05)
        self.m_listCtrl4.SetColumnWidth(1, self.width * 0.12)
        self.m_listCtrl4.SetColumnWidth(2, self.width * 0.15)
        self.m_listCtrl4.SetColumnWidth(3, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(4, self.width * 0.08)
        self.m_listCtrl4.SetColumnWidth(5, self.width * 0.29)
        #         self.mashin_list_refresh(None)
        if os.name == 'posix':
            self.SetSize((self.width, self.height*0.95))
        else:
            self.SetSize((self.width, self.height * 0.95))
        if event != None:
            event.Skip()
        # self.Fit()
        self.Layout()

    def kasa_refresh(self):
        # libs.DB.expire()
        self.parent.USER = libs.DB.get_one_where(libs.models.User, id=self.parent.USER.id)
        self.m_staticText8.SetLabel(gui_lib.msg.main_MainPanel_text[3] + u': ' + "{:.2f}".format(self.parent.USER.kasa))

    #         self.parent.USER = self.user

    def OnBugReport(self, event):
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            dial = BugReport(self, item)
            dial.ShowModal()

    def OnMashinStartCHK(self, event):
        self.mashin_list_refresh(None)
        self.m_button9.Bind(wx.EVT_BUTTON, self.OnMashinStopCHK)
        self.m_button9.SetLabel(gui_lib.msg.main_MainPanel_button['button9_2'])
        self.chk_mashin_worker = task.MashinCHK(self, self.all_mashin)  # @UndefinedVariable
        task.EVT_MASHIN_CHK(self, self.OnChkMashin)

    def OnMashinStopCHK(self, event):
        self.m_button9.Bind(wx.EVT_BUTTON, self.OnMashinStartCHK)
        self.m_button9.SetLabel(gui_lib.msg.main_MainPanel_button['button9_1'])
        self.chk_mashin_worker.abort()

    def OnChkMashin(self, event):
        try:
            if event.data == 'Done':
                self.m_button9.SetLabel(gui_lib.msg.main_MainPanel_button['button9_1'])
                self.m_button9.Bind(wx.EVT_BUTTON, self.OnMashinStartCHK)
            else:
                self.mashin_list_refresh(event)
                # self.m_button9.SetLabel(gui_lib.msg.main_MainPanel_button['button9_2'])
                self.m_button9.Bind(wx.EVT_BUTTON, self.OnMashinStopCHK)
        except Exception:
            pass

    #         self.m_button9.Enable()

    def SetEMGTime(self, event):
        selection = []
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return
        else:
            current = -1
            while True:
                next = self.m_listCtrl4.GetNextSelected(current)
                if next == -1:
                    break
                selection.append(self.mashinDict[next])
                current = next
        # try:
        #     item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        # except KeyError:
        #     dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
        #     dial.ShowModal()
        # else:
        dial = SetEMGTume(self, selection)
        dial.ShowModal()

    def OnServiseSet(self, event):
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            dial = servises.main.NewTask(self.parent, self.parent.USER, item)
            dial.ShowModal()

    def OnService(self, event):
        self.Hide()
        dial = servises.main.Main(self.parent, self.parent.USER, all_mashin=self.mashinDict)
        dial.Show()
        self.kasa_refresh()

    def _set_right(self):
        self.m_toolBar2.ClearTools()
        if self.parent.USER.grup.right != None:
            right = self.parent.USER.grup.from_json()

            if 2 in right['main']:
                self.m_tool9 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool9'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Emblem-Money-64.png",
                                                                wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.main_MainPanel_tolltip['tool9'], wx.EmptyString,
                                                            None)
                self.Bind(wx.EVT_TOOL, self.OnOrder, id=self.m_tool9.GetId())
                # self.m_tool9.SetToolTip()

            if 6 in right['main']:
                self.m_tool102 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool102'],
                                                              wx.Bitmap(
                                                                  libs.conf.IMG_FOLDER + u"64x64/system-users.png",
                                                                  wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                              wx.ITEM_NORMAL,
                                                              gui_lib.msg.main_MainPanel_tolltip['tool102'],
                                                              wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnClient, id=self.m_tool102.GetId())

            if 20 in right['main']:
                self.m_tool91 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool91'],
                                                             wx.Bitmap(
                                                                 libs.conf.IMG_FOLDER + u"64x64/Accessories-Dictionary-64.png",
                                                                 wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                             gui_lib.msg.main_MainPanel_tolltip['tool91'],
                                                             wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnOt4et, id=self.m_tool91.GetId())

            if 7 in right['main']:
                self.m_tool101 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool101'],
                                                              wx.Bitmap(
                                                                  libs.conf.IMG_FOLDER + u"64x64/Gnome-Appointment-New-64.png",
                                                                  wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                              wx.ITEM_NORMAL,
                                                              gui_lib.msg.main_MainPanel_tolltip['tool101'],
                                                              wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnWorkStartNow, id=self.m_tool101.GetId())

            if 4 in right['main']:
                self.m_tool8 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool8'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-System-Search-64.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.main_MainPanel_tolltip['tool8'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnMexCHK, id=self.m_tool8.GetId())

            if 1 in right['main']:
                self.m_tool3 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool3'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/network-server-database.png",
                                                                wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.main_MainPanel_tolltip['tool3'], wx.EmptyString,
                                                            None)
                self.Bind(wx.EVT_TOOL, self.OnFlor, id=self.m_tool3.GetId())

            if 5 in right['main']:
                self.m_tool10 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool10'],
                                                             wx.Bitmap(
                                                                 libs.conf.IMG_FOLDER + u"64x64/Gnome-X-Office-Presentation-64.png",
                                                                 wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                             wx.ITEM_NORMAL,
                                                             gui_lib.msg.main_MainPanel_tolltip['tool10'],
                                                             wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnReport, id=self.m_tool10.GetId())

            if 28 in right['main']:
                self.m_tool103 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_m_tool103,
                                                              wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/okular.png",
                                                                        wx.BITMAP_TYPE_ANY),
                                                              wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString,
                                                              wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.PrinrFreeRKO, id=self.m_tool103.GetId())

            if 3 in right['main']:
                self.m_tool5 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool5'],
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/Gnome-Applications-System-64.png",
                                                                wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.main_MainPanel_tolltip['tool5'],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnConfig, id=self.m_tool5.GetId())

            if 23 in right['main']:
                self.m_listCtrl4.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnServiseSet)

            if 9 in right['main']:
                self.m_button25.SetLabel(gui_lib.msg.main_MainPanel_button['button25'])
                self.m_button25.Show()
                self.m_button25.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button25'])
            if 8 in right['main']:
                self.m_button9.SetLabel(gui_lib.msg.main_MainPanel_button['button9_1'])
                self.m_button9.Show()
                self.m_button9.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button9'])
            if 10 in right['main']:
                self.m_button26.SetLabel(gui_lib.msg.main_MainPanel_button['button26'])
                self.m_button26.Show()
                self.m_button26.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button26'])
            if 11 in right['main']:
                self.m_button7.SetLabel(gui_lib.msg.main_MainPanel_button['button7'])
                self.m_button7.Show()
                self.m_button7.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button7'])
            if 12 in right['main']:
                self.m_button6.SetLabel(gui_lib.msg.main_MainPanel_button['button6'])
                self.m_button6.Show()
                self.m_button6.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button6'])
            if 13 in right['main']:
                self.m_button30.SetLabel(gui_lib.msg.main_MainPanel_button['button30'])
                self.m_button30.Show()
                self.m_button30.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button30'])
            if 14 in right['main']:
                self.m_button12.SetLabel(gui_lib.msg.main_MainPanel_button['button12'])
                self.m_button12.Show()
                self.m_button12.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button12'])
            if 15 in right['main']:
                self.m_button13.SetLabel(gui_lib.msg.main_MainPanel_button['button13'])
                self.m_button13.Show()
                self.m_button13.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button13'])
            if 16 in right['main']:
                self.m_button15.SetLabel(gui_lib.msg.main_MainPanel_button['button15'])
                self.m_button15.Show()
                self.m_button15.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button15'])
            if 17 in right['main']:
                self.m_button21.SetLabel(gui_lib.msg.main_MainPanel_button['button21'])
                self.m_button21.Show()
                self.m_button21.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button21'])
            if 18 in right['main']:
                self.m_button22.SetLabel(gui_lib.msg.main_MainPanel_button['button22'])
                self.m_button22.Show()
                self.m_button22.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button22'])
            if 19 in right['main']:
                self.m_button251.SetLabel(gui_lib.msg.main_MainPanel_button['button251'])
                self.m_button251.Show()
                self.m_button251.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button251'])
            if 22 in right['main']:
                self.m_button301.SetLabel(gui_lib.msg.main_MainPanel_button['button301'])
                self.m_button301.Show()
                self.m_button301.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button301'])
            if 25 in right['main']:
                self.m_button32.SetLabel(gui_lib.msg.main_MainPanel_button['m_button32'])
                self.m_button32.Show()
                self.m_button32.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['m_button32'])
            if 26 in right['main']:
                self.m_button35.SetLabel(gui_lib.msg.main_MainPanel_button['m_button35'])
                self.m_button35.Show()
                self.m_button35.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['m_button35'])
            if 24 in right['main']:
                self.m_tool103 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool103'],
                                                              wx.Bitmap(
                                                                  libs.conf.IMG_FOLDER + u"64x64/Gnome-Applications-Engineering-64.png",
                                                                  wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                              wx.ITEM_NORMAL,
                                                              gui_lib.msg.main_MainPanel_tolltip['tool103'],
                                                              wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnService, id=self.m_tool103.GetId())

        if libs.conf.KS_JUMP is True:
            self.m_button8.Show()
            self.m_button8.SetLabel(gui_lib.msg.main_m_button8)
            self.m_button8.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['button8'])

        if not self.parent.login.worker:
            self.m_tool21 = self.m_toolBar2.AddTool(wx.ID_ANY, gui_lib.msg.main_MainPanel_tool['tool21'],
                                                             wx.Bitmap(
                                                                 libs.conf.IMG_FOLDER + u"64x64/Gnome-Application-Exit-64.png",
                                                                 wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                             gui_lib.msg.main_MainPanel_tolltip['tool21'],
                                                             wx.EmptyString, None)
            self.Bind(wx.EVT_TOOL, self.OnLogOut, id=self.m_tool21.GetId())


        self.Bind(wx.EVT_CLOSE, self.OnLogOut)
        self.m_toolBar2.Realize()

    def PrintRKO(self, data):
        template = 'rko.html'
        data['my_copy'] = False
        html = gui_lib.printer.render(template, data)
        if os.name == 'posix':
            tmp_folder = '/tmp/'
        else:
            tmp_folder = r'C:/Users/Public/'
        # gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp1.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
        # gui_lib.printer.PDFPrint(tmp_folder + 'tmp1.pdf', default=libs.conf.DEFAULT_POS_PRINTER)
        gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp1.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
        if libs.conf.PRINT_DIRECT_POS is True:
            gui_lib.printer.PDFPrint(tmp_folder + 'tmp1.pdf', default=libs.conf.DEFAULT_POS_PRINTER, pos=True)
        else:
            cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp1.pdf'
            os.system(cmd)

    def PrinrFreeRKO(self, event):
        if libs.conf.POS_PRINTER_USE is True:
            try:
                casino = libs.DB.get_one_where(libs.models.Config, name='pos_printer_info')
                if casino == None:
                    objects = gui_lib.msg.cust_main_TaloniPrint_text[9]
                    sity = gui_lib.msg.cust_main_TaloniPrint_text[9]
                    objects_adress = gui_lib.msg.cust_main_TaloniPrint_text[9]
                else:
                    casino = json.loads(casino.value)
                    objects = casino['object']
                    sity = casino['sity']
                    objects_adress = casino['adress']
                object_info = libs.DB.get_one_where(libs.models.Config, name='object_info')
                object_info = json.loads(object_info.value)
                EIK = object_info['EIK']
                company = object_info['company']
                # mony = []
                egn = '.' * 45
                cust_name = '.' * 45
                user_id = str(self.parent.USER.id)
                dates = libs.models.TZ.date_to_str(formats='%d.%m.%Y')
                id = libs.DB.get_one(libs.models.CashOutPrinted, order='id', descs=True)
                if id == None:
                    ID = 1
                else:
                    ID = id.id + 1
                ID = str(ID)
                ID = ('0' * (9 - len(ID))) + ID
                cust_sity = '.' * 45
                cust_adress = '.' * 45
                mony = ['.' * 25]
                rko_data = {'company': company, 'EIK': EIK, 'objects': objects, 'sity': sity,
                            'objects_adress': objects_adress,
                            'name': cust_name, 'egn': egn, 'mony': mony, 'user_id': user_id, 'ID': [ID],
                            'dates': dates,
                            'cust_sity': cust_sity,
                            'cust_adress': cust_adress, 'count': 1, 'ID': [ID]}
                rko = libs.DB.make_obj(libs.models.CashOutPrinted)
                rko.mony = 0
                # rko.cust_id = cust.id
                rko.pub_user_id = self.parent.USER.id
                libs.DB.add_object_to_session(rko)
                libs.DB.commit()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                libs.DB.rollback()
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
                return
            self.PrintRKO(rko_data)
            # self.rko_data = None

    def PlayerReset(self, event):
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            # for i in range(3):
            libs.udp.send('reset_player', ip=item.ip)
            data = libs.udp.send('server_reset_player', libs.conf.SERVER)
            if data is True:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
                dial.ShowModal()

    def OnMSG(self, event):
        dial = order.main.MSGAdd(self, edit=True)
        dial.ShowModal()
        msg = libs.DB.get_one_where(libs.models.Config, name='admin_msg')
        if msg == None:
            self.m_staticText15.SetLabel(u'')
        elif msg.value == None or msg.value == u'':
            self.m_staticText15.SetLabel(u'')
        else:
            self.m_staticText15.SetLabel(
                gui_lib.msg.main_MainPanel_text[15] + u': ' + str(gui_lib.msg.main_MainPanel_text['yes']))

    def OnOut(self, event):
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            ip = item.ip
            # respone = libs.udp.send(libs.smib.SAS_F_METER_SINGLE, command='player_reset_hand_pay', ip=ip, forbiden=False)
            # if respone != True:
            #     dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            #     dial.ShowModal()
            #     return
            respone = libs.udp.send('sas.get_out_from_emg', ip=ip, forbiden=False)
            if respone == None or respone is False:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
                dial.ShowModal()
                return
            if respone[u'Transfer status'] == u'Full transfer successful':
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
            elif respone[u'Transfer status'] == 'Gaming machine unable to perform transfers at this time (door open, tilt, disabled, cashout in progress, etc.)':
                respone = libs.udp.send(libs.smib.SAS_F_METER_SINGLE, command='player_reset_hand_pay', ip=ip,
                                        forbiden=False)
                if respone != True:
                    dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
                    dial.ShowModal()
                    return
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
                dial.ShowModal()
                # return

    def UnLoockSMIB(self, event):
        selection = []
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
            return
        else:
            current = -1
            while True:
                next = self.m_listCtrl4.GetNextSelected(current)
                if next == -1:
                    break
                selection.append(self.mashinDict[next])
                current = next
        for i in selection:
            libs.udp.send('security_reload', ip=i.ip)
            err = libs.DB.make_obj(libs.models.GetCounterError)  # (self.USER.id, i)
            err.user_id = self.parent.USER.id  # @UndefinedVariable
            err.mashin_nom_in_l = i.nom_in_l
            err.info = 'security_reload' + ': ' + gui_lib.msg.main_MainPanel_text[16] + self.parent.USER.name
            libs.DB.add_object_to_session(err)
        libs.DB.commit()
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()

    def OnFlor(self, event, unitest=False):
        dialog = mashin.main.FlorSelect(self.parent)
        dialog.m_button1.SetLabel(gui_lib.msg.main_MainPanel_button['floar_button'])
        dialog.SetTitle(gui_lib.msg.main_MainPanel_text[12])
        dialog.m_bpButton1.SetToolTip(gui_lib.msg.main_MainPanel_tolltip['region_bpButton1'])
        if libs.conf.UNITEST:
            wx.CallLater(250, dialog.EndModal, wx.ID_OK)
        dialog.ShowModal()
        if dialog.close is False:
            self.mashin_list_refresh()
            if self.parent.USER.flor_id != None:
                self.m_staticText11.SetLabel(gui_lib.msg.main_MainPanel_text[2] + u': ' + self.parent.USER.flor.name)
            else:
                self.m_staticText11.SetLabel(
                    gui_lib.msg.main_MainPanel_text[2] + u': ' + gui_lib.msg.main_MainPanel_text[4])
        return dialog.close

    def OnLogOut(self, event):
        # print(e)vent.data
        self.parent.help_name = 'loging.html'
        if self.parent.login_one_time.value == 'True':
            try:
                self.login_worker.abort()
                self.login_worker.LOGIN_EVENT.set()
            except AttributeError:
                pass
        self.parent.USER.login = False
        libs.DB.add_object_to_session(self.parent.USER)
        libs.DB.commit()
        self.parent.USER = None
        self.parent.login_user_refresh()
        # if self.parent.login.with_rfid_in is True:
        #     self.parent.rfid_task_start(None)
        self.parent.login_show()
        self.parent.SetTitle(libs.conf.CASINO_NAME)
        self.OnClose(event)

    def OnClose(self, event):
        self.parent.help_name = 'login.html'
        self.Destroy()
        try:
            self.chk_mashin_worker.abort()
        except AttributeError:
            pass
        try:
            if self.parent.login_one_time.value == 'True':
                self.login_worker.abort()
                self.login_worker.LOGIN_EVENT.set()
        except AttributeError:
            pass

    def OnOrder(self, event):
        self.Hide()
        panel = order.main.Order(self.parent)
        panel.Show()

    def _set_mashin(self, event=None):
        if event == None:
            if self.parent.USER.flor_id == None:  # @UndefinedVariable
                self.all_mashin = libs.DB.get_all_where(libs.models.Device, enable=True, sas=True, order='nom_in_l')
                #                 self.all_mashin = all_mashin
            else:
                self.all_mashin = libs.DB.get_all_where(libs.models.Device, enable=True, sas=True,
                                                        flor_id=self.parent.USER.flor_id, order='nom_in_l')
            #                 self.all_mashin = all_mashin
        else:
            try:
                self.all_mashin = event.all_mashin
                #                 self.all_mashin = all_mashin
            except AttributeError:
                pass
        self.mashinDict = {}
        index = 0
        for item in self.all_mashin:
            self.m_listCtrl4.InsertItem(index, str(item.nom_in_l))
            self.m_listCtrl4.SetItem(index, 1, str(item.ip))
            self.m_listCtrl4.SetItem(index, 2, str(item.model.name))
            self.m_listCtrl4.SetItem(index, 3, gui_lib.msg.main_MainPanel_text[12])
            self.m_listCtrl4.SetItem(index, 4, gui_lib.msg.main_MainPanel_text[12])
            self.m_listCtrl4.SetItem(index, 5, gui_lib.msg.main_MainPanel_text[11])
            # data = libs.udp.send(libs.smib.ALIFE, item.ip)
            if event == None:
                self.m_listCtrl4.SetItem(index, 3, gui_lib.msg.main_MainPanel_text[12])
                self.m_listCtrl4.SetItem(index, 4, gui_lib.msg.main_MainPanel_text[12])
                self.m_listCtrl4.SetItem(index, 5, gui_lib.msg.main_MainPanel_text[11])
            else:
                try:

                    if event.data[item.ip][0] != None:
                        self.m_listCtrl4.SetItemTextColour(item=index, col=wx.Colour(0, 135, 11))
                        self.m_listCtrl4.SetItem(index, 3, gui_lib.msg.main_MainPanel_text[13])
                        self.m_listCtrl4.SetItem(index, 4, str(event.data[item.ip][0]))
                        if event.data[item.ip][1] == None or event.data[item.ip][1] is False:
                            self.m_listCtrl4.SetItem(index, 5, gui_lib.msg.main_MainPanel_text[11])
                        else:
                            self.m_listCtrl4.SetItem(index, 5, event.data[item.ip][1])
                            self.m_listCtrl4.SetItemTextColour(item=index, col=wx.Colour(6, 0, 255))
                        # if event.data[item.ip][0] == -1:
                        #     self.m_listCtrl4.SetItem(index, 3, gui_lib.msg.main_MainPanel_text[12])
                        #     self.m_listCtrl4.SetItem(index, 4, gui_lib.msg.main_MainPanel_text[12])
                        #     self.m_listCtrl4.SetItem(index, 5, gui_lib.msg.main_MainPanel_text[11])
                    if event.data[item.ip][1] == None or event.data[item.ip][1] is False:
                        if event.data[item.ip][0] == 0:
                            self.m_listCtrl4.SetItemTextColour(item=index, col=wx.Colour(199, 16, 255))
                            self.m_listCtrl4.SetItem(index, 3, gui_lib.msg.main_MainPanel_text[13])
                            self.m_listCtrl4.SetItem(index, 4, str(event.data[item.ip][0]))
                            self.m_listCtrl4.SetItem(index, 5, gui_lib.msg.main_MainPanel_text[11])
                        elif event.data[item.ip][0] == -1:
                            self.m_listCtrl4.SetItemTextColour(item=index, col=wx.Colour(255, 130, 0))
                            self.m_listCtrl4.SetItem(index, 3, gui_lib.msg.main_MainPanel_text[12])
                            self.m_listCtrl4.SetItem(index, 4, gui_lib.msg.main_MainPanel_text[12])
                            self.m_listCtrl4.SetItem(index, 5, gui_lib.msg.main_MainPanel_text[11])
                        elif event.data[item.ip][0] == None:
                            self.m_listCtrl4.SetItemTextColour(item=index, col=wx.Colour(199, 16, 29))
                            self.m_listCtrl4.SetItem(index, 3, gui_lib.msg.main_MainPanel_text[12])
                            self.m_listCtrl4.SetItem(index, 4, gui_lib.msg.main_MainPanel_text[12])
                            self.m_listCtrl4.SetItem(index, 5, gui_lib.msg.main_MainPanel_text[11])

                except AttributeError:
                    self.m_listCtrl4.SetItem(index, 3, gui_lib.msg.main_MainPanel_text[12])
                    self.m_listCtrl4.SetItem(index, 4, gui_lib.msg.main_MainPanel_text[12])
                    self.m_listCtrl4.SetItem(index, 5, gui_lib.msg.main_MainPanel_text[11])
            self.mashinDict[index] = item
            index += 1

    def mashin_list_refresh(self, event=None):
        self.m_listCtrl4.DeleteAllItems()
        self._set_mashin(event)

    def OnConfig(self, event):
        self.Hide()
        panel = config.main.MainConf(self.parent)
        panel.Show()
        self.on_resize(event)

    def OnGetBill(self, event):
        libs.DB.expire()
        start_work = libs.DB.get_one_where(libs.models.StartWork, user_id=self.parent.USER.id, start=True)
        if start_work != None:
            dialog = order.main.BillGet(self.parent, False, user=self.parent.USER)
            dialog.ShowModal()
            try:
                libs.DB.commit()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                dial.ShowModal()
            self.kasa_refresh()
            self.mashin_list_refresh()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.WORK_NOT_START)
            dial.ShowModal()

    def OnOt4et(self, event):
        object_info = libs.DB.get_one_where(libs.models.Config, name='object_info')
        if object_info == None:
            dial = wx.MessageDialog(self, *gui_lib.msg.SET_CASINO_DATA)
            dial.ShowModal()
        else:
            dial = MakeOrder(self, object_info)
            dial.ShowModal()

    def OnReport(self, event):
        self.Hide()
        panel = report.main.Main(self.parent)
        panel.Show()

    #         if libs.conf.FULSCREEAN is True:
    #             panel.ShowFullScreen(True,  style=wx.FULLSCREEN_NOCAPTION)
    #         else:
    #             panel.ShowModal()

    def OnMexCHK(self, event):
        self.Hide()
        libs.DB.expire()
        panel = order.mex_chk.MexCheck(self.parent)
        panel.Show()


    def OnWorkStartNow(self, event):
        obj = libs.DB.get_one_where(libs.models.StartWork, user_id=self.parent.USER.id, start=True)
        if obj != None:
            dial = wx.MessageDialog(self, *gui_lib.msg.WORK_IS_START)
            dial.ShowModal()
            return
        close = self.OnFlor(event)
        if close is False:

            obj = libs.DB.make_obj(libs.models.StartWork)
            obj.user_id = self.parent.USER.id
            obj.start = True
            libs.DB.add_object_to_session(obj)
            libs.DB.commit()
            #         print self.user.cart, libs.conf.KS_JUMP
            if libs.conf.KS_JUMP is True and self.parent.USER.cart != None:  # @UndefinedVariable
                dialog = KSChangeGuage(self, self.all_mashin, self.parent.USER.cart, user_id=self.parent.USER.id)
                dialog.ShowModal()
            dial = wx.MessageDialog(self, *gui_lib.msg.WORK_START_OK)
            dial.ShowModal()

    def OnCreditNotWork(self, event):
        selection = []
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            if self.parent.USER.cart == None:
                dial = wx.MessageDialog(self, *gui_lib.msg.USER_NOT_HAVE_CART)
                dial.ShowModal()
            else:
                current = -1
                while True:
                    next = self.m_listCtrl4.GetNextSelected(current)
                    if next == -1:
                        break
                    selection.append(self.mashinDict[next])
                    current = next

                #         try:
                #             item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
                #         except KeyError:
                #             dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
                #             dial.ShowModal()
                for item in selection:
                    if self.parent.USER.cart != None:
                        #                 print libs.smib.KS_CHANGE_KEY, item.ip, self.user.cart
                        add_key = libs.udp.send(libs.smib.KS_CHANGE_KEY, ip=item.ip, credit_id=self.parent.USER.cart)
                        #                 if add_key != None:
                        #                     dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                        #                     dial.ShowModal()
                        err = libs.DB.make_obj(libs.models.GetCounterError)  # (self.USER.id, i)
                        err.user_id = self.parent.USER.id  # @UndefinedVariable
                        err.mashin_nom_in_l = item.nom_in_l
                        err.info = 'KREDIT KEY CHANGE' + ': ' + gui_lib.msg.main_MainPanel_text[
                            17] + self.parent.USER.name
                        libs.DB.add_object_to_session(err)
                libs.DB.commit()
                #                 else:
                #                     dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
                #                     dial.ShowModal()

                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()

    def OnBilHalt(self, event):
        selection = []
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            current = -1
            while True:
                next = self.m_listCtrl4.GetNextSelected(current)
                if next == -1:
                    break
                selection.append(self.mashinDict[next])
                current = next
                #             bill_start = []
            for i in selection:
                data = libs.udp.send(libs.smib.SAS_F_METER_SINGLE, ip=i.ip, command='halt bill')
                err = libs.DB.make_obj(libs.models.GetCounterError)  # (self.USER.id, i)
                err.user_id = self.parent.USER.id  # @UndefinedVariable
                err.mashin_nom_in_l = i.nom_in_l
                err.info = 'BILL HALT' + ': ' + gui_lib.msg.main_MainPanel_text[18] + self.parent.USER.name
                libs.DB.add_object_to_session(err)
                if data == None or data is False:
                    err = libs.DB.make_obj(libs.models.GetCounterError)  # (self.USER.id, i)
                    err.user_id = self.parent.USER.id  # @UndefinedVariable
                    err.mashin_nom_in_l = i.nom_in_l
                    err.info = 'BILL NOT STOP' + ': ' + self.parent.USER.name
                    libs.DB.add_object_to_session(err)
                #             try:
                #                 bill_start.index(None)
                #             except ValueError:
            libs.DB.commit()
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()

    def OnNotBillStart(self, event):
        selection = []
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            current = -1
            while True:
                next = self.m_listCtrl4.GetNextSelected(current)
                if next == -1:
                    break
                selection.append(self.mashinDict[next])
                current = next
            #             bill_start = []
            for i in selection:
                data = libs.udp.send(libs.smib.SAS_F_METER_SINGLE, ip=i.ip, command='start bill')
                err = libs.DB.make_obj(libs.models.GetCounterError)  # (self.USER.id, i)
                err.user_id = self.parent.USER.id  # @UndefinedVariable
                err.mashin_nom_in_l = i.nom_in_l
                err.info = 'BILL START' + ': ' + gui_lib.msg.main_MainPanel_text[19] + self.parent.USER.name
                libs.DB.add_object_to_session(err)
                if data == None or data is False:
                    err = libs.DB.make_obj(libs.models.GetCounterError)  # (self.USER.id, i)
                    err.user_id = self.parent.USER.id  # @UndefinedVariable
                    err.mashin_nom_in_l = i.nom_in_l
                    err.info = 'BILL NOT START' + ': ' + self.parent.USER.name
                    libs.DB.add_object_to_session(err)
            #             try:
            #                 bill_start.index(None)
            #             except ValueError:
            libs.DB.commit()
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()

    #             else:
    #                 dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
    #                 dial.ShowModal()

    def OnRezerve(self, event):
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            try:
                item.reserve
            except AttributeError:
                item.reserve = False

            if item.reserve is False:
                item.reserve = True
                reserve = libs.udp.send(libs.smib.SAS_F_METER_SINGLE, ip=item.ip, command=libs.smib.SAS_C_SINGLE_HALT)

            else:
                item.reserve = False
                reserve = libs.udp.send(libs.smib.SAS_F_METER_SINGLE, ip=item.ip, command=libs.smib.SAS_C_SINGLE_START)
            if reserve != None:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
                dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)  # (self.USER.id, i)
            err.user_id = self.parent.USER.id  # @UndefinedVariable
            err.mashin_nom_in_l = item.nom_in_l
            err.info = 'ATENDAT LOCK EMG' + ': ' + gui_lib.msg.main_MainPanel_text[20] + self.parent.USER.name
            libs.DB.add_object_to_session(err)
            libs.DB.commit()

    def OnReboot(self, event):
        cust_panel = Reboot(self.parent)
        cust_panel.ShowModal()
        if cust_panel.close is False:
            reboot_time = int(cust_panel.m_spinCtrl2.GetValue())
            soft = cust_panel.m_radioBtn3.GetValue()
            selection = []
            try:
                item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
            except KeyError:
                dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
                dial.ShowModal()
            else:
                current = -1
                while True:
                    next = self.m_listCtrl4.GetNextSelected(current)
                    if next == -1:
                        break
                    selection.append(self.mashinDict[next])
                    current = next
            if selection != []:
                dial = config.main.RebootSMIB(self, selection, self.parent.USER, reboot_time=reboot_time, soft=soft)
                dial.ShowModal()

    def OnBonusLog(self, event):
        self.Hide()
        libs.DB.expire()
        panel = report.mashin_report.BonusLock(self.parent)
        panel.Show()

    def OnRealTimeLook(self, event):
        dial = report.mashin_report.MCurenState(self.parent)
        dial.ShowModal()
        coll = dial.col
        refresh_time = dial.refresh_time
        #         row = dial.row
        if coll != None:
            selection = []
            try:
                item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
            except KeyError:
                dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
                dial.ShowModal()
            else:
                current = -1
                while True:
                    next = self.m_listCtrl4.GetNextSelected(current)
                    if next == -1:
                        break
                    selection.append(self.mashinDict[next])
                    current = next
                self.Hide()
                if int(refresh_time) == 0:
                    refresh_time = 0.2
                panel = report.mashin_report.RealTimeLock(self.parent, selection, coll, float(refresh_time))
                panel.Show()
                # self.Layout()
        # return

    def OnClient(self, event):
        self.Hide()
        cust_panel = cust.main.Main(self.parent)
        cust_panel.Show()

    def HoldRill(self, event):
        try:
            item = self.mashinDict[self.m_listCtrl4.GetFirstSelected()]
        except KeyError:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:

            ip = item.ip
            cust_panel = HoldRill(self.parent, ip)
            cust_panel.ShowModal()
            if cust_panel.close is False:
                err = libs.DB.make_obj(libs.models.GetCounterError)
                err.user_id = self.parent.USER.id  # @UndefinedVariable
                err.mashin_nom_in_l = item.nom_in_l
                err.info = 'EMG GAME DELAY' + ': ' + gui_lib.msg.main_HoldRill_name + self.parent.USER.name
                libs.DB.add_object_to_session(err)
                libs.DB.commit()


class Reboot(gui.HoldRill, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        gui.HoldRill.__init__(self, parent)
        self.SetTitle(gui_lib.msg.main_Reboot_name)
        self.m_staticText11.SetLabel(gui_lib.msg.main_Reboot_text['Text11'])
        self.m_staticText12.SetLabel(gui_lib.msg.main_Reboot_text['Text12'])
        self.m_button19.SetLabel(gui_lib.msg.main_Reboot_button['button19'])
        self.m_button20.SetLabel(gui_lib.msg.main_Reboot_button['button20'])
        self.m_spinCtrl2.SetValue(1)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl2.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
        self.m_radioBtn3.Show()
        self.m_radioBtn3.SetLabel(gui_lib.msg.main_Reboot_button['radioBtn3'])
        self.m_radioBtn3.SetToolTip(gui_lib.msg.main_Reboot_tolltip['radioBtn3'])
        self.m_radioBtn4.Show()
        self.m_radioBtn4.SetLabel(gui_lib.msg.main_Reboot_button['radioBtn4'])
        self.m_radioBtn4.SetToolTip(gui_lib.msg.main_Reboot_tolltip['radioBtn4'])
        self.m_spinCtrl2.SetToolTip(gui_lib.msg.main_Reboot_tolltip['spinCtrl2'])
        self.close = True
        self.SetMinSize((250, 220))
        self.SetSize((250, 220))
        self.Layout()

    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        self.close = False
        self.OnClose(event)


class HoldRill(gui.HoldRill, gui_lib.keybords.Keyboard):
    def __init__(self, parent, mashin_ip):
        gui.HoldRill.__init__(self, parent)
        self.close = False
        self.ip = mashin_ip
        self.SetTitle(gui_lib.msg.main_HoldRill_name)
        self.m_staticText11.SetLabel(gui_lib.msg.main_HoldRill_text['Text11'])
        self.m_staticText12.SetLabel(gui_lib.msg.main_HoldRill_text['Text12'])
        self.m_button19.SetLabel(gui_lib.msg.main_HoldRill_button['button19'])
        self.m_button20.SetLabel(gui_lib.msg.main_HoldRill_button['button20'])
        self.m_spinCtrl2.SetToolTip(gui_lib.msg.main_HoldRill_tolltip['spinCtrl2'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl2.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

    def OnClose(self, event):
        self.close = True
        self.Destroy()

    def OnGo(self, event):
        try:
            delay = int(self.m_spinCtrl2.GetValue())
        except ValueError as e:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        data = libs.udp.send('sas.delay_game', ip=self.ip, delay_time=delay)
        if data is not True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            return
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()
        self.Destroy()


class CleanLogedIn(gui.SetPosID, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        self.parent = parent
        gui.SetPosID.__init__(self, self.parent)
        self._user_choice()
        self.m_staticText18.Hide()
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl6.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)

        self.SetTitle(gui_lib.msg.clean_user_loged_in['name'])
        self.m_staticText16.SetLabel(gui_lib.msg.clean_user_loged_in['m_staticText16'])
        self.m_staticText17.SetLabel(gui_lib.msg.clean_user_loged_in['m_staticText17'])
        self.m_button30.SetLabel(gui_lib.msg.clean_user_loged_in['m_button30'])
        self.m_button31.SetLabel(gui_lib.msg.clean_user_loged_in['m_button31'])
        self.m_textCtrl7.Hide()

    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        user = self.m_choice4.GetString(self.m_choice4.GetSelection())
        passwd = self.m_textCtrl6.GetValue()
        if user == '':
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            user = libs.DB.get_one_where(libs.models.User, name=user)
            if user.passwd != passwd:
                dial = wx.MessageDialog(self, *gui_lib.msg.PASSWD_WRONG)
                dial.ShowModal()
            else:
                right = user.grup.from_json()
                if 27 not in right['main']:
                    dial = wx.MessageDialog(self, *gui_lib.msg.NO_HAVE_RIGHT)
                    dial.ShowModal()
                else:
                    # users = libs.DB.get_all_where(libs.models.User, enable=True)
                    for i in self.users_obj:
                        i.login = False
                        libs.DB.add_object_to_session(i)
                    libs.DB.commit()
                    # libs.DB.expire()
                    self.OnClose(event)

    def _user_choice(self):
        self.users_obj = self.parent.login.users_obj
        self.m_choice1Choices = self.parent.login.m_choice1Choices
        # for i in self.users_obj:
        #     self.m_choice1Choices.append(i.name)
        #         self.m_choice1Choices = self.m_choice1Choices
        self.m_choice4.SetItems(self.m_choice1Choices)
        self.m_choice4.SetSelection(0)


class SetPosID(gui.SetPosID, gui_lib.keybords.Keyboard):
    def __init__(self, parent, pos_id):
        gui.SetPosID.__init__(self, parent)
        self.parent = parent
        self.pos_id = pos_id
        self.users_obj = None
        self._user_choice()
        self.SetTitle(gui_lib.msg.main_SetPosID['name'])
        self.m_staticText16.SetLabel(gui_lib.msg.main_SetPosID['m_staticText16'])
        self.m_staticText17.SetLabel(gui_lib.msg.main_SetPosID['m_staticText17'])
        self.m_staticText18.SetLabel(gui_lib.msg.main_SetPosID['m_staticText18'])
        self.m_button30.SetLabel(gui_lib.msg.main_SetPosID['m_button30'])
        self.m_button31.SetLabel(gui_lib.msg.main_SetPosID['m_button31'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl6.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)
            self.m_textCtrl7.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

    def OnClose(self, event):
        self.Destroy()

    def _user_choice(self):
        self.users_obj = libs.udp.send('get_all_user', ip=libs.conf.SERVER)
        if not self.users_obj:
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_DB_CONNECTION)
            dial.ShowModal()
            self.OnClose(None)
        else:
            self.m_choice1Choices = ['']
            for i in self.users_obj:
                self.m_choice1Choices.append(i)
                # self.m_choice1Choices = self.m_choice1Choices
            self.m_choice4.SetItems(self.m_choice1Choices)
            self.m_choice4.SetSelection(0)

    def OnGo(self, event):
        user = self.m_choice4.GetString(self.m_choice4.GetSelection())
        passwd = self.m_textCtrl6.GetValue()
        name = self.m_textCtrl7.GetValue()
        # print user
        if not user:
            dial = wx.MessageDialog(self, *gui_lib.msg.MSG_NOT_SELECT_ITEM)
            dial.ShowModal()
        else:
            pos = libs.udp.send('set_pos', ip=libs.conf.SERVER, pos_id=libs.conf.ID, name=name, user=user,
                                passwd=passwd)
            if pos == 'BAD NAME' or pos == 'BAD POS ID':
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                dial.ShowModal()
            elif pos == 'BAD PASSWD':
                dial = wx.MessageDialog(self, *gui_lib.msg.PASSWD_WRONG)
                dial.ShowModal()
            elif pos == 'NO RIGHT':
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_HAVE_RIGHT)
                dial.ShowModal()
            else:
                libs.restart_program()
            # user = libs.DB.get_one_where(libs.models.User, name=user)
            # if user.passwd != passwd:
            #
            #
            # else:
            #     right = user.grup.from_json()
            #     if 5 not in right['config']:
            #
            #     else:
            #
            #         if name == u'':
            #             dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            #             dial.ShowModal()
            #         else:

            # pos = libs.DB.get_one_where(libs.models.Config, name='pos')
            # new_data = json.loads(pos.value)
            # if name in new_data.values():
            #     dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            #     dial.ShowModal()
            # else:
            #     new_data[self.pos_id] = name
            #     pos.value = json.dumps(new_data)
            #     libs.DB.add_object_to_session(pos)
            #     libs.DB.commit()


class RegisterKey(gui.RegisterKey):

    def __init__(self, parent, key):
        gui.RegisterKey.__init__(self, parent)
        self.m_textCtrl5.SetValue(key)
        self.key = key
        self.SetTitle(gui_lib.msg.main_RegisterKey_name)
        self.m_staticText10.SetLabel(gui_lib.msg.main_RegisterKey_text['Text10'])
        self.m_button18.SetLabel(gui_lib.msg.main_RegisterKey_button['button18'])
        self.m_button30.SetLabel(gui_lib.msg.main_RegisterKey_button['button30'])
        self.m_textCtrl5.SetToolTip(gui_lib.msg.main_RegisterKey_tolltip['textCtrl5'])
        if libs.conf.ALL_POS_REGISTER is False:
            self.m_button18.Hide()
        # self.Fit()

    def OnRevert(self, event):
        dial = ServerSelect(None)
        dial.ShowModal()

    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        dial = SetPosID(self, self.key)
        if dial.users_obj:
            dial.ShowModal()

class SetMyTime(gui.SetTime, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        gui.SetTime.__init__(self, parent)
        self.SetTitle(gui_lib.msg.set_emg_time['name'])
        self.m_staticText11.SetLabel(gui_lib.msg.set_emg_time['m_staticText11'])
        self.m_staticText12.SetLabel(gui_lib.msg.set_emg_time['m_staticText12'])
        self.m_staticText111.SetLabel(gui_lib.msg.set_emg_time['m_staticText111'])
        self.m_staticText121.SetLabel(gui_lib.msg.set_emg_time['m_staticText121'])
        self.m_button19.SetLabel(gui_lib.msg.set_emg_time['m_button19'])
        self.m_button20.SetLabel(gui_lib.msg.set_emg_time['m_button20'])
        self.m_textCtrl8.SetValue(libs.models.TZ.date_to_str(datetime.now(), formats='%Y-%m-%d'))
        self.m_textCtrl9.SetValue(libs.models.TZ.date_to_str(datetime.now(), formats='%H:%M'))
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl8.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl9.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        try:
            times = self.m_textCtrl9.GetValue()
            dates = self.m_textCtrl8.GetValue()
        except ValueError as e:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        dial = config.main.SudoPasswd(self)
        dial.ShowModal()
        passwd = dial.passwd
        if passwd != None:
            libs.rtc.set_rtc(dates, times, passwd)
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()
        self.Destroy()

class SetEMGTume(gui.SetTime, gui_lib.keybords.Keyboard):
    def __init__(self, parent, device):
        self.device = device
        gui.SetTime.__init__(self, parent)
        self.SetTitle(gui_lib.msg.set_emg_time['name'])
        self.m_staticText11.SetLabel(gui_lib.msg.set_emg_time['m_staticText11'])
        self.m_staticText12.SetLabel(gui_lib.msg.set_emg_time['m_staticText12'])
        self.m_staticText111.SetLabel(gui_lib.msg.set_emg_time['m_staticText111'])
        self.m_staticText121.SetLabel(gui_lib.msg.set_emg_time['m_staticText121'])
        self.m_button19.SetLabel(gui_lib.msg.set_emg_time['m_button19'])
        self.m_button20.SetLabel(gui_lib.msg.set_emg_time['m_button20'])
        self.m_textCtrl8.SetValue(libs.models.TZ.date_to_str(datetime.now(), formats='%m.%d.%Y'))
        self.m_textCtrl9.SetValue(libs.models.TZ.date_to_str(datetime.now(), formats='%H:%M'))
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl8.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl9.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        try:
            times = self.m_textCtrl9.GetValue()
            dates = self.m_textCtrl8.GetValue()
        except ValueError as e:
            dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
            dial.ShowModal()
            return
        for i in self.device:
            libs.udp.send('sas.set_date_time', ip=i.ip, dates=dates, times=times)
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()
        self.Destroy()


def run():
    try:
        a = open(os.path.dirname(os.path.abspath(libs.conf.ROOT_PATH))+ '/tmp_rev', 'r').read()
        if a:
            libs.conf.CONF.update_option('SYSTEM', rev=a)
            libs.conf.REV = a
        # os.remove('tmp_rev')
    except:
        pass
    app = wx.App(redirect=libs.conf.DEBUG)
    if libs.CONNECTION_ERROR is True:
        dial = wx.MessageDialog(None, *gui_lib.msg.NO_DB_CONNECTION)
        dial.ShowModal()
        MyFrame = ServerSelect(None)
        MyFrame.Show()
    else:
        if libs.DEVISE_ERROR == 'INSTALL':
            # raise KeyError
            MyFrame = RegisterKey(None, libs.conf.ID)
            MyFrame.Show()
        else:
            try:
                if libs.conf.USE_RTC is True:
                    dates = libs.rtc.get_date_time()
                    if dates is False:
                        MyFrame = wx.MessageDialog(None, gui_lib.msg.main_cant_connect_with_rtc,
                                                   gui_lib.msg.on_run_error,
                                                   wx.OK | wx.ICON_ERROR)
                        MyFrame.ShowModal()
                        MyFrame = ServerSelect(None)
                        MyFrame.Show()
                base = libs.DB.get_one_where(libs.models.LN, name='base')
                # print datetime.strptime(json.loads(base.value)['end_time'],  '%d.%m.%Y')
                if base == None:
                    dial = wx.MessageDialog(None, *gui_lib.msg.NO_LICENSE)
                    dial.ShowModal()
                    dial = licenz.main.Active(None)
                    dial.ShowModal()
                    return
                elif datetime.strptime(json.loads(base.value)['end_time'], '%d.%m.%Y') < datetime.now():
                    dial = wx.MessageDialog(None, *gui_lib.msg.LICENSE_END_TIME)
                    dial.ShowModal()
                    dial = licenz.main.Active(None)
                    dial.ShowModal()
                    if dial.close is False:
                        return
                    else:
                        MyFrame = ServerSelect(None)
                        MyFrame.Show()
                # elif json.loads(base.value)['work'] is False:
                #     dial = wx.MessageDialog(None, *gui_lib.msg.LICENSE_CANT_WORK)
                #     dial.ShowModal()
                #     dial = licenz.main.Active(None)
                #     dial.ShowModal()
                #     return
                if json.loads(base.value)['name'] != base.name:
                    dial = wx.MessageDialog(None, *gui_lib.msg.BAD_LICENSE_NAME)
                    dial.ShowModal()
                    dial = licenz.main.Active(None)
                    dial.ShowModal()
                    return
            except OperationalError:
                dial = wx.MessageDialog(None, *gui_lib.msg.NO_DB_CONNECTION)
                dial.ShowModal()
                MyFrame = ServerSelect(None)
                MyFrame.Show()
            else:
                if libs.DB.get_one_where(libs.models.Config, name='nra_client_id') == None:
                    obj = libs.DB.make_obj(libs.models.Config)
                    obj.name = 'nra_client_id'
                    obj.value = ''
                    obj2 = libs.DB.make_obj(libs.models.Config)
                    obj2.name = 'nra_token'
                    obj2.value = ''
                    libs.DB.add_object_to_session(obj)
                    libs.DB.add_object_to_session(obj2)
                    obj3 = libs.DB.make_obj(libs.models.Config)
                    obj3.name = 'nra_token_valid'
                    obj3.value = ''
                    libs.DB.add_object_to_session(obj3)
                    libs.DB.commit()
                if libs.conf.DEBUG is False:
                    if libs.DB.get_one_where(libs.models.Config, name='user_have_mony') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'user_have_mony'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()
                    if libs.DB.get_one_where(libs.models.Config, name='user_name_on_day_report') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'user_name_on_day_report'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()
                    if libs.DB.get_one_where(libs.models.Config, name='print_cust_rko') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'print_cust_rko'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()
                    if libs.DB.get_one_where(libs.models.Config, name='loggin') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'loggin'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()
                    if libs.DB.get_one_where(libs.models.Config, name='bonus_cart_hold') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'bonus_cart_hold'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()
                    # if libs.DB.get_one_where(libs.models.Config, name='block_cust_if_print_tombula') == None:
                    #     obj = libs.DB.make_obj(libs.models.Config)
                    #     obj.name = 'block_cust_if_print_tombula'
                    #     obj.value = 'False'
                    #     libs.DB.add_object_to_session(obj)
                    #     libs.DB.commit()
                    MyFrame = MainFrame(None)
                    if libs.conf.FULSCREEAN is True:
                        MyFrame.ShowFullScreen(True, style=wx.FULLSCREEN_NOCAPTION)
                    else:
                        MyFrame.Show()
                else:
                    if libs.DB.get_one_where(libs.models.Config, name='user_have_mony') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'user_have_mony'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()

                    if libs.DB.get_one_where(libs.models.Config, name='user_name_on_day_report') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'user_name_on_day_report'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()
                    if libs.DB.get_one_where(libs.models.Config, name='print_cust_rko') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'print_cust_rko'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()
                    if libs.DB.get_one_where(libs.models.Config, name='loggin') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'loggin'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()
                    if libs.DB.get_one_where(libs.models.Config, name='bonus_cart_hold') == None:
                        obj = libs.DB.make_obj(libs.models.Config)
                        obj.name = 'bonus_cart_hold'
                        obj.value = 'False'
                        libs.DB.add_object_to_session(obj)
                        libs.DB.commit()
                    # if libs.DB.get_one_where(libs.models.Config, name='block_cust_if_print_tombula') == None:
                    #     obj = libs.DB.make_obj(libs.models.Config)
                    #     obj.name = 'block_cust_if_print_tombula'
                    #     obj.value = 'False'
                    #     libs.DB.add_object_to_session(obj)
                    #     libs.DB.commit()
                    MyFrame = MainFrame(None)
                    MyFrame.Show()

    app.MainLoop()
    # if libs.conf.DB_TUNNEL is True:
    #     time.sleep(1)
    #     libs.TUNNEL_SERVER.abort()
    # time.sleep(5)
    # libs.TUNNEL_SERVER[1].terminate()
