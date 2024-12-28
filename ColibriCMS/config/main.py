# -*- coding:utf-8 -*-
'''
Created on 23.06.2017 г.

@author: dedal
Прозорец за настройки.
'''

import wx
import libs
import gui_lib
import mashin
import users
from . import gui
import licenz
import datetime
import os
from . import jpmain
import json
import time
from . import sas_tester
from subprocess import Popen, PIPE

if os.name == 'posix':
    import cups  # Ако системата е Linux връща всички принтери добавени в cups към системата използва се в настройки на печат @UnresolvedImport
from serial import SerialException
from . import task


class DellOld(gui.KSGuage):
    def __init__(self, parent, user, date, table):
        self.parent = parent
        self.user = user
        self.table = table
        self.date = date
        gui.KSGuage.__init__(self, parent)
        self.SetTitle(gui_lib.msg.del_old_data['name'])
        self.m_button23.SetLabel(gui_lib.msg.del_old_data['m_button23'])
        self.m_button23.Disable()
        self.m_button23.Bind(wx.EVT_BUTTON, self.OnGo)
        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width * 0.47, self.height * 0.15))
        self.m_gauge1.SetMinSize((self.width * 0.45, -1))
        self.m_gauge1.SetRange(len(self.table))
        self.worker = task.DelOld(self, user=self.user, date=self.date, table=self.table)
        task.EVT_DEL_RESULT(self, self.SetData)
        self.loop = 0
        self.Layout()

    def SetData(self, event):
        if type(event.data) == int:
            self.loop = self.loop + event.data
            self.m_gauge1.SetValue(self.loop)
        elif event.data == 'DONE':
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            self.m_button23.Enable()

    def OnGo(self, event):
        import sqlalchemy
        from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
        DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
        DB.connect()
        DB.close_all_session()
        engine = sqlalchemy.create_engine('postgresql://%s:%s@%s:%s/%s' %
                                          (libs.conf.DB_USER, libs.conf.DB_PASS, libs.conf.SERVER, libs.conf.DB_PORT,
                                           libs.conf.DB_NAME),
                                          echo=libs.conf.DB_DEBUG,
                                          echo_pool=False,
                                          pool_reset_on_return=True,
                                          connect_args={'connect_timeout': 30}
                                          )
        connection = engine.raw_connection()
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute("VACUUM FULL")

        DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
        DB.connect()
        DB.close_all_session()
        cmd = 'PGPASSWORD="%s" reindexdb -h %s -p %s -U %s -d %s' % (
            libs.conf.DB_PASS, libs.conf.SERVER, libs.conf.DB_PORT, libs.conf.DB_USER, libs.conf.DB_NAME)
        os.system(cmd)
        libs.udp.send('soft_reboot_server', ip='192.168.1.6')
        # dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        # dial.ShowModal()
        libs.restart_program()


class RebootSMIB(gui.KSGuage):
    def __init__(self, parent, mashin, user, reboot_time, soft=False, **kwargs):
        '''
            Конструктор:
            Създава елементите
            Добавя дължина на лентата
            Ако броя на машините е 50 дължината на лентата е 50 като започне от 0
        '''
        self.parent = parent
        self.user = user
        gui.KSGuage.__init__(self, parent)
        self.SetTitle(gui_lib.msg.config_RebootSMIB['name'])
        self.m_button23.SetLabel(gui_lib.msg.config_RebootSMIB['m_button23'])

        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width * 0.47, self.height * 0.15))
        self.m_gauge1.SetMinSize((self.width * 0.45, -1))
        self.mashin = mashin
        self.reboot_time = reboot_time
        self.m_gauge1.SetRange(len(self.mashin))
        self.worker = task.Reboot(self, mashin=mashin, user=self.user, reboot_time=self.reboot_time, soft=soft)
        task.EVT_REBOOT_RESULT(self, self.SetData)
        self.loop = 0
        self.Layout()

    def SetData(self, event):
        '''
            Когато командата мине позицията на лентата се премества с 1
            Ако броя на машините е 50 и са минали 10
            Лентата за прогреса се мести на позиция 10 или 10 % от общата дължина на процеса
        '''
        if type(event.data) == int:
            self.loop = self.loop + event.data
            self.m_gauge1.SetValue(self.loop)
        elif event.data == 'DONE':
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()

    def OnClose(self, event):
        '''
            Затваря прозореца като спира препрограмирането на кей системите
        '''
        self.worker.abort()
        self.Destroy()


class UpdateSMIB(gui.KSGuage):
    def __init__(self, parent, user, mashin, rev, **kwargs):
        '''
            Конструктор:
            Създава елементите
            Добавя дължина на лентата
            Ако броя на машините е 50 дължината на лентата е 50 като започне от 0
        '''
        self.parent = parent
        self.user = user
        # main_reboot = kwargs['reboot']
        gui.KSGuage.__init__(self, parent)
        self.SetTitle(gui_lib.msg.config_UpdateSMIB['name'])
        self.m_button23.SetLabel(gui_lib.msg.config_UpdateSMIB['m_button23'])
        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width * 0.47, self.height * 0.15))
        self.m_gauge1.SetMinSize((self.width * 0.45, -1))
        self.mashin = mashin
        self.m_gauge1.SetRange(len(self.mashin))
        self.rev = rev
        self.worker = task.UpdateSMIB(self, mashin=mashin, user=self.user, rev=self.rev, **kwargs)
        task.EVT_REBOOT_RESULT(self, self.SetData)
        self.loop = 0
        self.Layout()

    def SetData(self, event):
        '''
            Когато командата мине позицията на лентата се премества с 1
            Ако броя на машините е 50 и са минали 10
            Лентата за прогреса се мести на позиция 10 или 10 % от общата дължина на процеса
        '''
        if type(event.data) == int:
            self.loop = self.loop + event.data
            self.m_gauge1.SetValue(self.loop)
        elif event.data == 'DONE':
            dial = wx.MessageDialog(self, *gui_lib.msg.UPDATE_SMIB_AFTER_REBOOT)
            dial.ShowModal()

    def OnClose(self, event):
        '''
            Затваря прозореца като спира препрограмирането на кей системите
        '''
        self.worker.abort()
        self.Destroy()


class SystemConf(gui.SystemConf, gui_lib.keybords.Keyboard):
    '''
        изгражда таб: Система в бутона Система
    '''

    def __init__(self, parent):
        '''
            Конструктур:
            Създава всички елементи в таб система.
            Прочита лога на програмата, версията и серийния номер
        '''
        gui.SystemConf.__init__(self, parent)
        self.parent = parent
        self.m_button3.SetLabel(gui_lib.msg.config_SystemConf['m_button3'])
        self.m_button3.SetToolTip(gui_lib.msg.config_SystemConf['m_button3t'])

        # self.m_staticText78.SetLabel(gui_lib.msg.config_SystemConf['m_staticText78'])
        self.m_staticText13.SetLabel(gui_lib.msg.config_SystemConf['m_staticText13'])
        self.m_checkBox61.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox61'])
        self.m_staticText122.SetLabel(gui_lib.msg.config_SystemConf['m_staticText122'])
        self.m_staticText131.SetLabel(gui_lib.msg.config_SystemConf['m_staticText131'])
        self.m_staticText141.SetLabel(gui_lib.msg.config_SystemConf['m_staticText141'])
        self.m_staticText151.SetLabel(gui_lib.msg.config_SystemConf['m_staticText151'])
        self.m_staticText1511.SetLabel(gui_lib.msg.config_SystemConf['m_staticText1511'])
        self.m_button58.SetLabel(gui_lib.msg.config_SystemConf['m_button58'])
        # self.m_staticText33.SetLabel(gui_lib.msg.config_SystemConf['m_staticText33'])
        # self.m_staticText67.SetLabel(gui_lib.msg.config_SystemConf['m_staticText67'])
        self.m_checkBox1.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox1'])
        self.m_checkBox11.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox11'])
        self.m_checkBox2.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox2'])
        self.m_checkBox56.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox56'])
        self.m_checkBox561.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox561'])
        self.m_checkBox4.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox4'])
        self.m_checkBox50.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox50'])
        self.m_staticText79.SetLabel(gui_lib.msg.config_SystemConf['m_staticText79'])
        # self.m_checkBox56.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox56'])
        # self.m_checkBox13.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox13'])
        # self.m_checkBox33.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox33'])
        self.m_checkBox35.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox35'])
        self.m_checkBox38.SetLabel(gui_lib.msg.config_SystemConf['m_checkBox38'])
        self.m_button6.SetLabel(gui_lib.msg.config_SystemConf['m_button6'])

        self.m_checkBox1.SetToolTip(gui_lib.msg.config_SystemConf['m_checkBox1t'])
        self.m_checkBox11.SetToolTip(gui_lib.msg.config_SystemConf['m_checkBox11t'])
        self.m_checkBox2.SetToolTip(gui_lib.msg.config_SystemConf['m_checkBox2t'])
        self.m_checkBox4.SetToolTip(gui_lib.msg.config_SystemConf['m_checkBox4t'])
        self.m_checkBox56.SetToolTip(gui_lib.msg.config_SystemConf['m_checkBox56t'])
        self.m_checkBox561.SetToolTip(gui_lib.msg.config_SystemConf['m_checkBox561t'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl2.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl3.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl4.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl5.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl14.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl26.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl1.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl2.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

        self.m_spinCtrl1.SetValue(libs.models.TZ.now().hour)
        self.m_spinCtrl2.SetValue(libs.models.TZ.now().minute)

        self.m_checkBox1.SetValue(libs.conf.DEBUG)
        self.m_checkBox11.SetValue(libs.conf.DB_DEBUG)
        self.m_checkBox2.SetValue(libs.conf.FULSCREEAN)
        # self.m_checkBox56.SetValue(libs.conf.USER_NAME_ON_DAY_ORDER)
        self.m_checkBox4.SetValue(libs.conf.USE_VIRTUAL_KEYBORD)
        # self.m_checkBox41.SetValue(libs.conf.BLOCK_BILL_ON_ORDER)
        if libs.DB.get_one_where(libs.models.Config, name='user_name_on_day_report').value == 'True':
            self.m_checkBox56.SetValue(True)
        else:
            self.m_checkBox56.SetValue(False)
        # if libs.DB.get_one_where(libs.models.Config, name='block_cust_if_print_tombula').value == 'True':
        #     self.m_checkBox61.SetValue(True)
        # else:
        #     self.m_checkBox61.SetValue(False)
        self.m_checkBox61.Hide()
        if libs.DB.get_one_where(libs.models.Config, name='user_have_mony').value == 'True':
            self.m_checkBox561.SetValue(True)
        else:
            self.m_checkBox561.SetValue(False)

        if libs.DB.get_one_where(libs.models.Config, name='print_cust_rko').value == 'True':
            self.m_checkBox50.SetValue(True)
        else:
            self.m_checkBox50.SetValue(False)

        if libs.DB.get_one_where(libs.models.Config, name='bonus_cart_hold').value == 'True':
            self.m_checkBox35.SetValue(True)
        else:
            self.m_checkBox35.SetValue(False)
        # self.m_checkBox13.SetValue(libs.conf.CONF.get('MAIL', 'auto', 'bool'))

        # self.m_textCtrl15.SetValue(libs.conf.CONF.get('MAIL', 'subject', 'str'))
        self.login = libs.DB.get_one_where(libs.models.Config, name='loggin')

        if self.login.value == 'True':
            self.m_checkBox38.SetValue(True)
        else:
            self.m_checkBox38.SetValue(False)
        # self.m_checkBox33.SetValue(libs.conf.BILL_OUT_DEFOUT)

        #         self.m_staticText121.SetLabel(os.name)

        self.choises = []
        for i in libs.conf.ALL_LANGUAGE:
            self.choises.append(libs.conf.ALL_LANGUAGE[i])
        self.m_choice2.SetItems(self.choises)
        self.m_choice2.SetSelection(self.choises.index(libs.conf.ALL_LANGUAGE[libs.conf.USE_LANGUAGE]))

        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl2.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl3.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl4.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl5.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl14.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl26.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl1.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl2.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
        self.object_info = libs.DB.get_one_where(libs.models.Config, name='object_info')
        if self.object_info != None:
            object_info = json.loads(self.object_info.value)
            self.m_textCtrl2.SetValue(object_info['company'])
            self.m_textCtrl3.SetValue(object_info['company adress'])
            self.m_textCtrl4.SetValue(object_info['object name'])
            self.m_textCtrl5.SetValue(object_info['object adress'])
            if 'EIK' in object_info:
                self.m_textCtrl26.SetValue(object_info['EIK'])
            if 'manager' in object_info:
                self.m_textCtrl14.SetValue(object_info['manager'])

            # self.m_textCtrl24.SetValue(libs.conf.CONF.get('MAIL', 'service', 'str'))
            # self.m_textCtrl141.SetValue(libs.conf.CONF.get('MAIL', 'boss', 'str'))
        # self.Bind(wx.EVT_SIZE, self.on_resize)
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.on_resize(None)
        self.Layout()

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        self.SetSize((self.width, self.height * 0.8))
        self.m_scrolledWindow2.SetMinSize((self.width * 0.6, self.height * 0.75))
        self.m_choice2.SetMinSize((self.width * 0.25, -1))
        self.m_textCtrl2.SetMinSize((self.width * 0.15, -1))
        self.m_textCtrl3.SetMinSize((self.width * 0.15, -1))
        self.m_textCtrl4.SetMinSize((self.width * 0.15, -1))
        self.m_textCtrl5.SetMinSize((self.width * 0.15, -1))
        self.m_calendar2.SetMinSize((self.width * 0.465, -1))
        self.m_spinCtrl1.SetMinSize((self.width * 0.2, self.height * 0.03))
        self.m_spinCtrl2.SetMinSize((self.width * 0.2, self.height * 0.03))
        if event != None:
            event.Skip()
            self.Layout()

    def OnNRA( self, event ):
        dial = NRA(self)
        dial.ShowModal()

    def OnSave(self, event):
        '''
            Запаметява всички промени в конфигурационния файл
        '''
        self.parent.GetParent().reboot = True
        if self.object_info == None:
            object_info = {}
            object_info['company'] = self.m_textCtrl2.GetValue()
            object_info['company adress'] = self.m_textCtrl3.GetValue()
            object_info['object name'] = self.m_textCtrl4.GetValue()
            object_info['object adress'] = self.m_textCtrl5.GetValue()
            object_info['EIK'] = self.m_textCtrl26.GetValue()
            #             if self.m_textCtrl14.GetValue() != '':
            object_info['manager'] = self.m_textCtrl14.GetValue()
            if (object_info['company'] == '' or object_info['company adress'] == ''
                    or object_info['object name'] == '' or object_info['object adress'] == ''):
                dial = wx.MessageDialog(self, *gui_lib.msg.INVALID_DATA)
                dial.ShowModal()
                return
            else:
                self.object_info = libs.DB.make_obj(libs.models.Config)
                self.object_info.name = 'object_info'
                object_info = json.dumps(object_info)
                self.object_info.value = object_info
                libs.DB.add_object_to_session(self.object_info)
                # try:
                #     libs.DB.commit()
                # except Exception as e:
                #     print(e)
                #     libs.DB.rollback()
                #     dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                #     dial.ShowModal()
                #     return
        else:

            object_info = json.loads(self.object_info.value)
            if 'EIK' not in object_info:
                object_info['EIK'] = ''
            if 'manager' not in object_info:
                object_info['manager'] = ''
            #             print 'save', object_info
            if (object_info['company'] != self.m_textCtrl2.GetValue() or
                    object_info['company adress'] != self.m_textCtrl3.GetValue() or
                    object_info['object name'] != self.m_textCtrl4.GetValue() or
                    object_info['object adress'] != self.m_textCtrl5.GetValue() or
                    object_info['manager'] != self.m_textCtrl14.GetValue() or
                    object_info['EIK'] != self.m_textCtrl26.GetValue()
            ):
                # libs.conf.CONF.update_option('MAIL', boss=self.m_textCtrl141.GetValue())
                # libs.conf.CONF.update_option('MAIL', service=self.m_textCtrl24.GetValue())
                #                 if self.m_textCtrl14.GetValue() == '' and 'manager' in object_info:
                #                     del object_info['manager']
                #                 else:
                object_info['EIK'] = self.m_textCtrl26.GetValue()
                object_info['manager'] = self.m_textCtrl14.GetValue()
                object_info['company'] = self.m_textCtrl2.GetValue()
                object_info['company adress'] = self.m_textCtrl3.GetValue()
                object_info['object name'] = self.m_textCtrl4.GetValue()
                object_info['object adress'] = self.m_textCtrl5.GetValue()
                self.object_info.value = json.dumps(object_info)
                libs.DB.add_object_to_session(self.object_info)
                # try:
                #     libs.DB.commit()
                # except Exception as e:
                #     print(e)
                #     libs.DB.rollback()
                #     dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
                #     dial.ShowModal()
                #     return

        libs.conf.CONF.update_option('SYSTEM', debug=self.m_checkBox1.GetValue())
        libs.conf.CONF.update_option('SYSTEM', db_debug=self.m_checkBox11.GetValue())
        libs.conf.CONF.update_option('SYSTEM', fulscreen=self.m_checkBox2.GetValue())
        # libs.conf.CONF.update_option('SYSTEM', user_name=self.m_checkBox56.GetValue())
        libs.conf.CONF.update_option('KEYBORD', virtual=self.m_checkBox4.GetValue())
        # libs.conf.CONF.update_option('SYSTEM', bill_block = self.m_checkBox41.GetValue())
        # libs.conf.CONF.update_option('MAIL', auto=self.m_checkBox13.GetValue())
        # libs.conf.CONF.update_option('MAIL', subject=self.m_textCtrl15.GetValue())
        # libs.conf.CONF.update_option('SYSTEM', bill_out_default=self.m_checkBox33.GetValue())
        # libs.conf.CONF.update_option('SYSTEM', hold_bonus_cart=self.m_checkBox35.GetValue())
        print_cust_rko = libs.DB.get_one_where(libs.models.Config, name='print_cust_rko')
        if self.m_checkBox50.GetValue() is True:

            print_cust_rko.value = 'True'
        else:
            print_cust_rko.value = 'False'
        libs.DB.add_object_to_session(print_cust_rko)

        # block_cust_if_print_tombula = libs.DB.get_one_where(libs.models.Config, name='block_cust_if_print_tombula')
        # if self.m_checkBox61.GetValue() is True:
        #     block_cust_if_print_tombula.value = 'True'
        # else:
        #     block_cust_if_print_tombula.value = 'False'
        # libs.DB.add_object_to_session(block_cust_if_print_tombula)

        user_name_on_day_report = libs.DB.get_one_where(libs.models.Config, name='user_name_on_day_report')
        if self.m_checkBox56.GetValue() is True:
            user_name_on_day_report.value = 'True'
        else:
            user_name_on_day_report.value = 'False'
        libs.DB.add_object_to_session(user_name_on_day_report)

        user_have_mony = libs.DB.get_one_where(libs.models.Config, name='user_have_mony')
        if self.m_checkBox561.GetValue() is True:
            user_have_mony.value = 'True'
        else:
            user_have_mony.value = 'False'
        libs.DB.add_object_to_session(user_have_mony)

        hold_bonus = libs.DB.get_one_where(libs.models.Config, name='bonus_cart_hold')
        if self.m_checkBox35.GetValue() is True:
            hold_bonus.value = 'True'
        else:
            # hold_bonus = libs.DB.get_one_where(libs.models.Config, name='bonus_cart_hold')
            hold_bonus.value = 'False'
        libs.DB.add_object_to_session(hold_bonus)

        if self.m_checkBox38.GetValue() is True and self.login.value == 'False':
            self.login.value = 'True'
            libs.DB.add_object_to_session(self.login)
            # libs.DB.commit()
        elif self.m_checkBox38.GetValue() is False and self.login.value == 'True':
            self.login.value = 'False'
            libs.DB.add_object_to_session(self.login)
            # libs.DB.commit()

        lang = self.m_choice2.GetString(self.m_choice2.GetSelection())
        for i in libs.conf.ALL_LANGUAGE:
            if libs.conf.ALL_LANGUAGE[i] == lang:
                lang = i
        try:
            libs.DB.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            libs.DB.rollback()
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            return
        libs.conf.CONF.update_option('LANGUAGE', use_lang=lang)
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()

    def OnClockSet(self, event):
        '''
            Сверява часовника на компютъра
        '''
        # dial = wx.MessageDialog(self, *gui_lib.msg.IN_TEST)
        # dial.ShowModal()
        # return
        if os.name == 'posix':
            dial = SudoPasswd(self)
            dial.ShowModal()
            passwd = dial.passwd
            if passwd and dial.close == False:
                dates = self.m_calendar2.GetDate()
                times = str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
                libs.rtc.set_rtc(dates.Format('%Y-%m-%d'), times, passwd)
        elif os.name == 'win32':
            dates = self.m_calendar2.GetDate()
            dates.Format('%Y-%m-%d')
            times = str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
            libs.rtc.set_rtc(dates, times, None)
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()


class SudoPasswd(gui.SudoPasswd, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        self.parent = parent
        gui.SudoPasswd.__init__(self, parent)
        self.m_textCtrl25.SetValue('')
        self.passwd = None
        self.close = False
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl25.Bind(wx.EVT_LEFT_UP, self.OnIntWithPass)

    def OnClose(self, event):
        self.close = True
        self.Destroy()

    def OnGo(self, event):
        self.passwd = self.m_textCtrl25.GetValue()
        self.OnClose(event)


class PosPrinterConf(gui.PosPrinterConf, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        self.parent = parent
        gui.PosPrinterConf.__init__(self, parent)

        self.SetTitle(gui_lib.msg.config_PosPrinterConf['name'])
        self.m_staticText69.SetLabel(gui_lib.msg.config_PosPrinterConf['m_staticText69'])
        self.m_staticText70.SetLabel(gui_lib.msg.config_PosPrinterConf['m_staticText70'])
        self.m_staticText71.SetLabel(gui_lib.msg.config_PosPrinterConf['m_staticText71'])
        self.m_button50.SetLabel(gui_lib.msg.config_PosPrinterConf['m_button50'])
        self.m_button51.SetLabel(gui_lib.msg.config_PosPrinterConf['m_button51'])

        self.casino = libs.DB.get_one_where(libs.models.Config, name='pos_printer_info')
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl15.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl16.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl17.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
        if self.casino == None:
            self.m_textCtrl15.SetValue('')
            self.m_textCtrl16.SetValue('')
            self.m_textCtrl17.SetValue('')
        else:
            casino = json.loads(self.casino.value)
            self.m_textCtrl15.SetValue(str(casino['object']))
            self.m_textCtrl16.SetValue(str(casino['sity']))
            self.m_textCtrl17.SetValue(str(casino['adress']))

    def OnClose(self, event):
        self.Destroy()

    def OnGo(self, event):
        casino = {'object': self.m_textCtrl15.GetValue(),
                  'sity': self.m_textCtrl16.GetValue(),
                  'adress': self.m_textCtrl17.GetValue()
                  }
        if self.casino == None:
            self.casino = libs.DB.make_obj(libs.models.Config)
            self.casino.name = 'pos_printer_info'
        self.casino.value = json.dumps(casino)
        libs.DB.add_object_to_session(self.casino)
        try:
            libs.DB.commit()
            self.OnClose(event)
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            libs.DB.rollback()
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            return


class PrinterRFIDConf(gui.PrinterRFIDConf, gui_lib.keybords.Keyboard):
    '''
        Таб за настройки на принтерите и картовите четци
    '''

    def __init__(self, parent):
        '''
            Конструктор.
            Създава елементите в прозореца
        '''
        gui.PrinterRFIDConf.__init__(self, parent)
        self.parent = parent
        self.m_checkBox6.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_checkBox6'])
        self.m_checkBox39.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_checkBox39'])
        # self.m_staticText16.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_staticText16'])
        self.m_staticText18.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_staticText18'])
        self.m_checkBox51.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_checkBox51'])
        self.m_checkBox52.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_checkBox52'])
        self.m_staticText68.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_staticText68'])
        self.m_staticText69.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_staticText69'])
        self.m_button47.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_button47'])
        self.m_button471.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_button471'])

        self.m_checkBox76.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_checkBox76'])
        self.m_staticText85.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_staticText85'])

        self.m_checkBox58.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_checkBox58'])
        self.m_staticText20.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_staticText20'])
        self.m_staticText26.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_staticText26'])
        self.m_staticText27.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_staticText27'])
        self.m_staticText22.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_staticText22'])
        self.m_checkBox44.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_checkBox44'])
        self.m_button6.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_button6'])
        self.m_checkBox8.SetLabel(gui_lib.msg.config_PrinterRFIDConf['m_checkBox8'])

        self.m_textCtrl28.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_textCtrl28t'])
        self.m_textCtrl29.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_textCtrl28t'])
        if os.name == 'posix':
            self.m_textCtrl28.Hide()
            self.m_textCtrl29.Hide()
            self.m_choice2.Show()
            self.m_choice15.Show()
        else:
            self.m_textCtrl28.Show()
            self.m_textCtrl29.Show()
            self.m_choice2.Hide()
            self.m_choice15.Hide()

        self.m_checkBox44.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_checkBox44t'])
        self.m_checkBox8.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_checkBox8t'])
        self.m_checkBox6.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_checkBox6t'])
        self.m_checkBox39.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_checkBox39t'])
        self.m_textCtrl6.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_textCtrl6t'])
        self.m_button47.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_button47t'])
        self.m_button471.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_button471t'])
        # self.m_checkBox7.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_checkBox7t'])
        self.m_choice3.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_choice3t'])
        self.m_spinCtrl5.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_spinCtrl5t'])
        self.m_spinCtrl3.SetToolTip(gui_lib.msg.config_PrinterRFIDConf['m_spinCtrl3t'])

        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl6.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_spinCtrl24.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl25.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl7.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_spinCtrl5.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl3.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

        self.m_textCtrl6.SetValue(libs.conf.PDF_PROGRAM)
        if os.name == 'posix':
            conn = cups.Connection()
            printers = conn.getPrinters()
            self.all_printer = ['']
            for printer in printers:
                self.all_printer.append(printer)
            try:
                self.m_choice2.SetItems(self.all_printer)
                self.m_choice2.SetSelection(self.all_printer.index(libs.conf.PRINTER_DEFAULT))
            except ValueError:
                self.m_choice2.SetSelection(0)
            try:
                self.m_choice15.SetItems(self.all_printer)
                self.m_choice15.SetSelection(self.all_printer.index(libs.conf.DEFAULT_POS_PRINTER))
            except ValueError:
                self.m_choice15.SetSelection(0)
        else:
            self.m_textCtrl28.SetValue(libs.conf.PRINTER_DEFAULT)
            self.m_textCtrl29.SetValue(libs.conf.DEFAULT_POS_PRINTER)
        self.m_checkBox39.SetValue(libs.conf.POS_PRINTER_USE)
        self.m_checkBox58.SetValue(libs.conf.MONYBACK_ON_POS)
        self.m_spinCtrl24.SetValue(libs.conf.POS_PRINTER_SIZE[0])
        self.m_spinCtrl25.SetValue(libs.conf.POS_PRINTER_SIZE[1])
        self.m_checkBox44.SetValue(libs.conf.PRINT_ON_SERVER)
        self.m_checkBox51.SetValue(libs.conf.PRINT_DIRECT_POS)
        self.m_checkBox52.SetValue(libs.conf.PRINT_ON_SERVER_POS)
        self.m_checkBox76.SetValue(libs.conf.OCR_USE)
        self.m_textCtrl30.SetValue(libs.conf.OCR_PORT)
        self.m_checkBox78.SetValue(libs.conf.OCR_DESKO)
        # self.m_checkBox5.SetValue(libs.conf.PRINTER_USE_PDF)
        self.m_checkBox6.SetValue(libs.conf.PRINT_DIRECT)

        self.serialSpeed = ['2400', '4800', '7200', '9600', '14400', '19200', '38400', '57600', '115200']
        self.m_choice3.SetItems(self.serialSpeed)
        self.m_choice3.SetSelection(self.serialSpeed.index(str(libs.conf.RFID_BAUD)))

        self.m_checkBox8.SetValue(libs.conf.RFID_USE_WORK)
        # self.m_checkBox8.SetValue(libs.conf.RFID_USE_CUST)

        self.m_textCtrl7.SetValue(libs.conf.RFID_WORK_PORT)
        #         self.m_textCtrl9.SetValue(libs.conf.RFID_CUST_PORT)

        self.m_spinCtrl3.SetValue(libs.conf.RFID_SCAN_TIME)

        self.m_spinCtrl5.SetValue(libs.conf.RFID_TIMEOUT)

        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.on_resize(None)

    def PortChange( self, event ):
        if self.m_checkBox78.GetValue() is True:
            self.m_textCtrl30.SetValue('/dev/ocrd')
        else:
            self.m_textCtrl30.SetValue('/dev/ocr')

    def UpdateRFID(self, event):
        update_img = self.m_filePicker3.GetPath()
        if update_img == '' or update_img == None or update_img is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.EMPTY_FIELD)
            dial.ShowModal()
            return
        if self.m_checkBox8.GetValue() is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        port = self.m_textCtrl7.GetValue()
        while True:
            try:
                update = libs.rfid_update.UpdateRFID(port=port, timeout=0, baudrate=19200)
                break
            except libs.rfid_update.SerialException:
                pass
            except Exception as e:
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_RFID)
                dial.ShowModal()
                raise e
        while 1:
            var = update.read()
            if var == 'C':
                break
        update.update(img=update_img)
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        self.SetSize((self.width, self.height * 0.8))
        self.m_scrolledWindow3.SetSize((self.width * 0.90, self.height * 0.65))
        self.m_scrolledWindow3.SetMinSize((self.width * 0.90, self.height * 0.65))
        self.m_textCtrl6.SetMinSize((self.width * 0.3, -1))
        self.m_choice2.SetMinSize((self.width * 0.3, -1))
        self.m_choice3.SetMinSize((self.width * 0.3, -1))
        self.m_spinCtrl5.SetSize((self.width * 0.3, -1))
        self.m_spinCtrl3.SetSize((self.width * 0.3, -1))
        self.m_textCtrl7.SetMinSize((self.width * 0.30, -1))
        #         self.m_textCtrl9.SetMinSize((self.width*0.4, -1))
        if event != None:
            event.Skip()
        self.Layout()

    def OnGo(self, event):
        '''
            Записва всички промени в конфигурационния файл на програselfмата
        '''
        self.parent.GetParent().reboot = True
        libs.conf.CONF.update_option('PRINTER', pdf_soft=self.m_textCtrl6.GetValue())
        # libs.conf.CONF.update_option('PRINTER', use_pdf=self.m_checkBox5.GetValue())
        libs.conf.CONF.update_option('PRINTER', print_direct=self.m_checkBox6.GetValue())
        libs.conf.CONF.update_option('PRINTER', pos_printer_use=self.m_checkBox39.GetValue())
        libs.conf.CONF.update_option('PRINTER', pos_printer_x=self.m_spinCtrl24.GetValue())
        libs.conf.CONF.update_option('PRINTER', pos_printer_y=self.m_spinCtrl25.GetValue())
        libs.conf.CONF.update_option('PRINTER', printer_on_server=self.m_checkBox44.GetValue())
        libs.conf.CONF.update_option('PRINTER', printer_on_server_pos=self.m_checkBox52.GetValue())
        libs.conf.CONF.update_option('PRINTER', print_direct_pos=self.m_checkBox51.GetValue())
        libs.conf.CONF.update_option('PRINTER', mony_back_on_pos=self.m_checkBox58.GetValue())

        libs.conf.CONF.update_option('RFID', use_work_port=self.m_checkBox8.GetValue())
        # libs.conf.CONF.update_option('RFID', use_cust_port=self.m_checkBox8.GetValue())
        libs.conf.CONF.update_option('RFID', worker_port=self.m_textCtrl7.GetValue())
        #         libs.conf.CONF.update_option('RFID', cust_port=self.m_textCtrl9.GetValue())
        libs.conf.CONF.update_option('RFID', scan_time=self.m_spinCtrl3.GetValue())
        libs.conf.CONF.update_option('RFID', timeout=self.m_spinCtrl5.GetValue())
        libs.conf.CONF.update_option('OCR', use=self.m_checkBox76.GetValue())
        libs.conf.CONF.update_option('OCR', desko=self.m_checkBox78.GetValue())
        libs.conf.CONF.update_option('OCR', worker_port=self.m_textCtrl30.GetValue())


        speed = self.m_choice3.GetString(self.m_choice3.GetSelection())
        libs.conf.CONF.update_option('RFID', baudrate=int(speed))
        if self.m_checkBox8.GetValue() is True:
            cmd = 'mt' + str(self.m_spinCtrl3.GetValue())
            try:
                if self.m_textCtrl7.GetValue() != libs.conf.RFID_SCAN_TIME:
                    try:
                        if self.parent.GetParent().GetParent().login.with_rfid_in is True:
                            self.parent.GetParent().GetParent().rfid_task_stop(None)

                        cart = libs.rfid.RFID(self.m_textCtrl7.GetValue(), int(speed),
                                              timeout=self.m_spinCtrl5.GetValue())
                        cart.open()
                        cart.scan_time(self.m_spinCtrl3.GetValue())
                        cart.close()
                        if self.parent.GetParent().GetParent().login.with_rfid_in is True:
                            self.parent.GetParent().GetParent().rfid_task_start(event)

                    except libs.rfid.RFIDOpenError as e:
                        print(e)
                        libs.log.stderr_logger.critical(e, exc_info=True)
            except SerialException as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
        if os.name == 'posix':
            printer = self.m_choice2.GetString(self.m_choice2.GetSelection())
            pos_printer = self.m_choice15.GetString(self.m_choice15.GetSelection())

        else:
            printer = self.m_textCtrl28.GetValue()
            pos_printer = self.m_textCtrl29.GetValue()
        libs.conf.CONF.update_option('PRINTER', default_printer=printer)
        libs.conf.CONF.update_option('PRINTER', default_pos_printer=pos_printer)
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()

    def OnAddPosPrinterInfo(self, info):
        dial = PosPrinterConf(self)
        dial.ShowModal()

    def OnPosPrinterTest(self, event):
        pos_printer_x = self.m_spinCtrl24.GetValue()
        pos_printer_y = self.m_spinCtrl25.GetValue()
        size = (pos_printer_x, pos_printer_y)
        pos_printer = self.m_choice15.GetString(self.m_choice15.GetSelection())
        template = 'pos_print_tombula.html'
        dates = libs.models.TZ.now()
        dates = libs.models.TZ.date_to_str(dates)
        name = u'Colibri Test User'
        for i in range(2, 10):
            name = name.replace(' ' * i, '')
        br_index = 0
        for i in name:
            if i == ' ':
                br_index += 1
        name = name.replace(' ', '<br>')
        if br_index == 1:
            name += '<br>&nbsp;'
        elif br_index == 0:
            name += '<br>&nbsp;<br>&nbsp;'
        elif br_index == 3:
            name = name[0:-4]
        casino = libs.DB.get_one_where(libs.models.Config, name='pos_printer_info')
        if casino == None:
            object = u'None'
            sity = u'None'
            adress = u'None'
        else:
            casino = json.loads(casino.value)
            object = casino['object']
            sity = casino['sity']
            adress = casino['adress']
        data = {'count': 4, 'name': name, 'dates': dates, 'ID': 0, 'len': len(name), 'adress': adress, 'object': object,
                'sity': sity, 'copy': False}
        html = gui_lib.printer.render(template, data)
        if os.name == 'posix':
            tmp_folder = '/tmp/'
        else:
            tmp_folder = r'C:/Users/Public/'
        gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp2.pdf', pos=True, size=size)
        if libs.conf.PRINT_DIRECT_POS is True:
            gui_lib.printer.PDFPrint(tmp_folder + 'tmp2.pdf', default=libs.conf.DEFAULT_POS_PRINTER, pos=True)
        else:
            # gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp2.pdf', pos=True, size=libs.conf.POS_PRINTER_SIZE)
            cmd = libs.conf.PDF_PROGRAM + ' ' + tmp_folder + 'tmp2.pdf'
            os.system(cmd)
        # gui_lib.printer.pdf_mk(html, tmp_folder + 'tmp2.pdf', pos=True, size=size)
        # gui_lib.printer.PDFPrint(tmp_folder + 'tmp2.pdf', default=pos_printer, pos=True)


class NetworkConf(gui.NetworkConf, gui_lib.keybords.Keyboard):
    '''
        Настройки на интернет комуникациите.
        В момента най-често се използва трансфер сървър.
        Така се вързвъм към базата за разработки но използвам машините на спартак за тест
    '''

    def __init__(self, parent):
        '''
            Конструктор.
            Изгражда елементите на прозореца като задава последните стойности от конфигурацията
        '''
        gui.NetworkConf.__init__(self, parent)
        self.parent = parent
        self.m_checkBox38.SetLabel(gui_lib.msg.config_NetworkConf['m_checkBox38'])
        self.m_staticText32.SetLabel(gui_lib.msg.config_NetworkConf['m_staticText32'])
        self.m_staticText33.SetLabel(gui_lib.msg.config_NetworkConf['m_staticText33'])
        self.m_checkBox10.SetLabel(gui_lib.msg.config_NetworkConf['m_checkBox10'])
        self.m_checkBox54.SetLabel(gui_lib.msg.config_NetworkConf['m_checkBox54'])
        self.m_button3.SetLabel(gui_lib.msg.config_NetworkConf['m_button3'])
        self.m_button11.SetLabel(gui_lib.msg.config_NetworkConf['m_button11'])
        self.m_staticText75.SetLabel(gui_lib.msg.config_NetworkConf['m_staticText75'])

        self.m_checkBox38.SetToolTip(gui_lib.msg.config_NetworkConf['m_checkBox38t'])
        self.m_spinCtrl7.SetToolTip(gui_lib.msg.config_NetworkConf['m_spinCtrl7t'])
        self.m_spinCtrl8.SetToolTip(gui_lib.msg.config_NetworkConf['m_spinCtrl8t'])
        self.m_checkBox10.SetToolTip(gui_lib.msg.config_NetworkConf['m_checkBox10t'])
        self.m_checkBox77.SetLabel(gui_lib.msg.config_NetworkConf['m_checkBox77'])

        self.m_button3.SetToolTip(gui_lib.msg.config_NetworkConf['m_button3t'])
        self.m_choice17.SetToolTip(gui_lib.msg.config_NetworkConf['m_choice17'])

        # self.m_checkBox39.SetLabel(gui_lib.msg.config_NetworkConf['m_checkBox39'])
        self.m_checkBox40.SetLabel(gui_lib.msg.config_NetworkConf['m_checkBox40'])
        self.m_checkBox42.SetLabel(gui_lib.msg.config_NetworkConf['m_checkBox42'])
        # self.m_checkBox41.SetLabel(gui_lib.msg.config_NetworkConf['m_checkBox41'])
        self.m_button48.SetLabel(gui_lib.msg.config_NetworkConf['m_button48'])
        self.m_button49.SetLabel(gui_lib.msg.config_NetworkConf['m_button49'])

        # self.m_checkBox39.SetToolTip(gui_lib.msg.config_NetworkConf['m_checkBox39t'])
        self.m_checkBox40.SetToolTip(gui_lib.msg.config_NetworkConf['m_checkBox40t'])
        # self.m_checkBox41.SetToolTip(gui_lib.msg.config_NetworkConf['m_checkBox41t']
        self.m_checkBox74.SetLabel(gui_lib.msg.config_NetworkConf['m_checkBox74'])
        self.m_checkBox74.SetToolTip(gui_lib.msg.config_NetworkConf['m_checkBox74t'])
        self.m_button48.SetToolTip(gui_lib.msg.config_NetworkConf['m_button48t'])
        self.m_button49.SetToolTip(gui_lib.msg.config_NetworkConf['m_button49t'])
        self.m_textCtrl18.SetToolTip(gui_lib.msg.config_NetworkConf['m_textCtrl18t'])
        self.m_textCtrl19.SetToolTip(gui_lib.msg.config_NetworkConf['m_textCtrl19t'])
        self.m_checkBox42.SetToolTip(gui_lib.msg.config_NetworkConf['m_checkBox42t'])

        self.m_radioBox2.SetString(0, gui_lib.msg.config_NetworkConf[1])
        self.m_radioBox2.SetString(1, gui_lib.msg.config_NetworkConf[2])
        self.m_radioBox2.SetString(2, gui_lib.msg.config_NetworkConf[3])

        self.on_resize(None)
        self.m_checkBox10.SetValue(libs.conf.USE_RTC)
        self.m_checkBox38.SetValue(libs.conf.DB_IPTABLES)
        #         print libs.conf.UDP_PORT, libs.conf.UDP_BUFFER
        #         self.m_spinCtrl6.SetValue(libs.conf.UDP_PORT)
        self.m_spinCtrl7.SetValue(libs.conf.UDP_BUFFER)
        self.m_spinCtrl8.SetValue(libs.conf.UDP_TIMEOUT)
        self.m_checkBox54.Hide()

        dates = libs.models.TZ.now()
        self.m_spinCtrl1.SetValue(dates.hour)
        self.m_spinCtrl2.SetValue(dates.minute)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl7.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl8.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl18.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl19.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

            self.m_spinCtrl1.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl2.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

    def OnVNCPasswd( self, event ):
        dial = SudoPasswd(self)
        dial.m_textCtrl25.SetMaxLength(8)
        dial.ShowModal()
        if dial.close == True:
            return
        passwd = dial.passwd
        if not passwd:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            return
        data = libs.udp.send('change_vnc_passwd', libs.conf.SERVER, passwd=passwd)
        if data != True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            return
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()

    def OnLoadConf(self, event):
        data = libs.udp.send('cms_load_conf', libs.conf.SERVER)
        all_printer = libs.udp.send('get_printer', libs.conf.SERVER)
        if data == None or all_printer == None:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            return
        self.m_checkBox39.SetValue(data['tcp'])
        self.m_checkBox40.SetValue(data['rtc'])
        self.m_checkBox75.SetValue(data['nra_debug'])
        # self.m_checkBox41.SetValue(data['gmail'])
        self.m_checkBox42.SetValue(data['log_server'])
        self.m_textCtrl18.SetValue(data['mail_to'])
        self.m_textCtrl19.SetValue(data['mail_subject'])
        self.m_checkBox74.SetValue(data['iv_jump'])
        self.m_checkBox77.SetValue(data['ocr_use'])
        # self.m_checkBox54.SetValue(data['thread'])
        if data['tcp'] is True:
            self.m_checkBox54.Hide()
            self.m_checkBox54.SetValue(False)
        else:
            self.m_checkBox54.Hide()
            self.m_checkBox54.SetValue(False)
        if data['iptables'] is True:
            self.m_radioBox2.SetSelection(0)
        elif data['ban'] is True:
            self.m_radioBox2.SetSelection(1)
        else:
            self.m_radioBox2.SetSelection(2)

        self.m_choice17.SetItems(all_printer[0])
        self.m_choice17.SetSelection(all_printer[0].index(all_printer[1]))
        self.m_choice19.SetItems(all_printer[0])
        self.m_choice19.SetSelection(all_printer[0].index(all_printer[2]))

    def OnTCP(self, event):
        if self.m_checkBox39.GetValue() is True:
            self.m_checkBox54.Hide()
            self.m_checkBox54.SetValue(False)
        else:
            self.m_checkBox54.Hide()
            self.m_checkBox54.SetValue(False)

    def OnSaveConf(self, event):

        if self.m_radioBox2.GetSelection() == 0:
            iptables = True
            ban = False
        elif self.m_radioBox2.GetSelection() == 1:
            ban = True
            iptables = False
        else:
            ban = False
            iptables = False
        tmp = {
            # 'gmail': self.m_checkBox41.GetValue(),
            'tcp': self.m_checkBox39.GetValue(),
            'iptables': iptables,
            'ban': ban,
            'log_server': self.m_checkBox42.GetValue(),
            'rtc': self.m_checkBox40.GetValue(),
            'mail_to': self.m_textCtrl18.GetValue(),
            'mail_subject': self.m_textCtrl19.GetValue(),
            'thread': self.m_checkBox54.GetValue(),
            'iv_jump':self.m_checkBox74.GetValue(),
            'nra_debug': self.m_checkBox75.GetValue(),
            'ocr_use': self.m_checkBox77.GetValue(),
        }
        data = libs.udp.send('cms_save_conf', libs.conf.SERVER, data=tmp)
        printer = self.m_choice17.GetString(self.m_choice17.GetSelection())
        printer_pos = self.m_choice19.GetString(self.m_choice19.GetSelection())
        tmp = libs.udp.send('set_printer', libs.conf.SERVER, printer=printer, printer_pos=printer_pos)
        if data is not True or tmp is not True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            return

        if self.m_checkBox39.GetValue() != libs.conf.TCP or self.m_checkBox74.GetValue() != libs.conf.UDP_IV_JUMP:
            # if self.m_checkBox74.GetValue() != libs.conf.UDP_IV_JUMP:
            all_device = libs.DB.get_all_where(libs.models.Device, sas=True, enable=True)
            my_device = []
            data = self.m_checkBox74.GetValue()
            for i in all_device:
                my_device.append(i.ip)
            dialog = IfJump(self, my_device, data)
            dialog.ShowModal()
            libs.conf.CONF.update_option('UDP', tcp=self.m_checkBox39.GetValue())
            libs.conf.CONF.update_option('UDP', iv_jump=self.m_checkBox74.GetValue())
            libs.udp.send('soft_reboot_server', libs.conf.SERVER, timeout=4)
            libs.restart_program()
        libs.udp.send('soft_reboot_server', libs.conf.SERVER, timeout=4)
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()


    def on_resize(self, event):
        '''
            При преоразмеряване на основния прозорец преоразмерява всички елементи
        '''
        self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        self.SetSize((self.width, self.height * 0.8))
        self.m_scrolledWindow5.SetSize((self.width, self.height * 0.6))
        self.m_scrolledWindow5.SetMinSize((self.width, self.height * 0.6))

        #         self.m_spinCtrl6.SetSize((self.width*0.45, -1))
        self.m_spinCtrl7.SetSize((self.width * 0.45, -1))
        self.m_spinCtrl8.SetSize((self.width * 0.45, -1))
        #         self.m_spinCtrl9.SetSize((self.width*0.45, -1))
        #         self.m_textCtrl12.SetMinSize((self.width*0.45, -1))
        #         self.m_textCtrl121.SetMinSize((self.width*0.45, -1))
        self.m_spinCtrl1.SetMinSize((self.width * 0.2, -1))
        self.m_spinCtrl2.SetMinSize((self.width * 0.2, -1))
        if event != None:
            event.Skip()
            self.Fit()

    def OnClockSet(self, event):
        if self.m_checkBox10.GetValue() is False:
            return
        ip = libs.conf.JPSERVERIP
        port = libs.conf.JPSERVERPORT
        dates = self.m_calendar1.GetDate()
        times = str(self.m_spinCtrl1.GetValue()) + ':' + str(self.m_spinCtrl2.GetValue())
        data = libs.rtc.set_date_time(dates.Format('%Y-%m-%d'), times)
        if data is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
        dial.ShowModal()

    def OnGo(self, event):
        '''
            Записва всички промени в конфигурационнен файл
        '''
        # libs.conf.CONF.update_option('UDP', rtansfer_server=self.m_checkBox12.GetValue())
        self.parent.GetParent().reboot = True
        libs.conf.CONF.update_option('SYSTEM', use_rtc=self.m_checkBox10.GetValue())
        # self.m_checkBox38.SetValue(libs.conf.DB_TUNNEL)
        libs.conf.CONF.update_option('SYSTEM', db_iptables=self.m_checkBox38.GetValue())
        #         libs.conf.CONF.update_option('UDP', port=self.m_spinCtrl6.GetValue())
        libs.conf.CONF.update_option('UDP', buffer=self.m_spinCtrl7.GetValue())
        libs.conf.CONF.update_option('UDP', timeout=self.m_spinCtrl8.GetValue())
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()
        # if self.m_checkBox29.GetValue() is True:
        #     libs.conf.CONF.update_option('UDP', protocol='TCP')
        # else:
        #     libs.conf.CONF.update_option('UDP', protocol='UDP')


#         libs.conf.CONF.update_option('SYSTEM', rtc_port=self.m_spinCtrl9.GetValue())
#         libs.conf.CONF.update_option('SYSTEM', RTC=self.m_textCtrl121.GetValue())
# libs.conf.CONF.update_option('UDP', rtansfer_server_ip=self.m_textCtrl121.GetValue())

class POSInstall(gui.POSInstall, gui_lib.keybords.Keyboard):
    '''
        Разрешава или забранява на програмите да се свързвът с базата данни и с машините в казиното
    '''

    def __init__(self, parent):
        '''
            Добавя програма която може да се свърже с базата данни и машините в казиното
        '''
        gui.POSInstall.__init__(self, parent)
        self.parent = parent
        self.SetTitle(gui_lib.msg.config_POSInstall['name'])
        self.m_staticText30.SetLabel(gui_lib.msg.config_POSInstall['m_staticText30'])
        self.m_staticText29.SetLabel(gui_lib.msg.config_POSInstall['m_staticText29'])
        self.m_button9.SetLabel(gui_lib.msg.config_POSInstall['m_button9'])
        self.m_button10.SetLabel(gui_lib.msg.config_POSInstall['m_button10'])

        self.m_textCtrl11.SetToolTip(gui_lib.msg.config_POSInstall['m_textCtrl11'])
        self.m_textCtrl10.SetToolTip(gui_lib.msg.config_POSInstall['m_textCtrl10'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl11.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_textCtrl10.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

    def OnClose(self, event):
        '''
            Затваря диалоговия прозорец без да прави промени
        '''
        self.Destroy()

    def OnGo(self, event):
        '''
            Записва всички промени в базата и затваря диалоговия прозорец
        '''
        pos_id = self.m_textCtrl10.GetValue()
        pos_name = self.m_textCtrl11.GetValue()
        self.parent.treeValue[pos_id] = pos_name
        self.parent.tree.value = json.dumps(self.parent.treeValue)
        libs.DB.add_object_to_session(self.parent.tree)
        err = libs.DB.make_obj(libs.models.GetCounterError)
        err.user_id = self.parent.GetParent().GetParent().GetParent().USER.id
        #             err.mashin_nom_in_l = 1
        err.info = 'POS INSTALL' + ': ' + gui_lib.msg.config_POSInstall[1] % (pos_name)
        libs.DB.add_object_to_session(err)

        try:
            libs.DB.commit()
            self.Destroy()
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()


class POS(gui.POS):
    '''
        Прозорец за инсталирани софтуери в базата
        Погазва сериен номер и име на програмата която има право да използва базата и машините в казиното
    '''

    def __init__(self, parent):
        '''
            Конструктор:
            Взима от базата всички инсталирани програми и фи показва в лист
            Изгражда бутоните като им казва какво точно трябва да прави всеки бутон.
        '''
        gui.POS.__init__(self, parent)
        self.parent = parent
        self.m_button7.SetLabel(gui_lib.msg.config_POS['m_button7'])
        self.m_button8.SetLabel(gui_lib.msg.config_POS['m_button8'])
        self.m_button20.SetLabel(gui_lib.msg.config_POS['m_button20'])
        self.m_button7.SetToolTip(gui_lib.msg.config_POS['m_button7t'])
        self.m_button8.SetToolTip(gui_lib.msg.config_POS['m_button8t'])
        self.m_button20.SetToolTip(gui_lib.msg.config_POS['m_button20t'])

        self.m_listCtrl1.InsertColumn(0, gui_lib.msg.config_POS[1])

        self.m_listCtrl1.InsertColumn(1, gui_lib.msg.config_POS[2])

        self._add_tree()
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.on_resize(None)

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        self.SetSize((self.width, self.height * 0.8))
        self.m_listCtrl1.SetMinSize((self.width * 0.84, self.height * 0.7))
        self.m_listCtrl1.SetColumnWidth(0, self.width * 0.40)
        self.m_listCtrl1.SetColumnWidth(1, self.width * 0.20)

        if event != None:
            event.Skip()
            self.Layout()

    def _add_tree(self):
        '''
           Създава трея като рефрешва елементите
           Ако се добави нова програма която да може да се свързва
           Опреснява елементите и я показва в прозореца.
           Държи всички елементи в текущо състояние
        '''
        self.tree = libs.DB.get_one_where(libs.models.Config, name='pos')
        self.treeValue = json.loads(self.tree.value)
        index = 0
        for i in self.treeValue:
            self.m_listCtrl1.InsertItem(index, i)
            self.m_listCtrl1.SetItem(index, 1, self.treeValue[i])
            index += 1

    def tree_refresh(self):
        '''
            Премахва старите елементи от трея.
            И ги заменя с нови ( След промяна )
        '''
        self.m_listCtrl1.DeleteAllItems()
        self._add_tree()

    def OnInstall(self, event):
        '''
            Стартира диалог за инсталиране на нова програма в базата
        '''
        dial = POSInstall(self)
        dial.ShowModal()
        self.tree_refresh()

    def OnRemove(self, event):
        '''
            Премахва програма от базата
        '''
        data = self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFirstSelected(), 0)
        del self.treeValue[data]
        self.tree.value = json.dumps(self.treeValue)
        libs.DB.add_object_to_session(self.tree)
        try:
            libs.DB.commit()
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dial.ShowModal()
            return
        self.tree_refresh()

    def OnReset(self, event):
        '''
            Премахва всички програми от базата
            създава ново ID на текущата програма и я записва
            В този случай единственната програма с достъп до казиното ще е текущата.
            Използва се в случай че администратора се обърка кое ID на кой управител е
        '''
        # new_soft_id = {'INIT':libs._uuid.mk_soft_id()}
        # libs.conf.CONF.update_option('SYSTEM', soft_id=new_soft_id['INIT'])
        pos = libs.DB.get_one_where(libs.models.Config, name='pos')
        libs.DB.delete_object(pos)
        libs.restart_program(user_clean=True)
        # pos.value = json.dumps(new_soft_id)
        # libs.DB.add_object_to_session(pos)
        # if libs.DB.commit() is True:
        #     dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_OK)
        #     dial.ShowModal()
        # else:
        #     dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
        #     dial.ShowModal()
        # self.tree_refresh()

    # def OnMakeID(self, event):
    #     '''
    #        Променя ID на текущата програма
    #        За повторно свързване на тази програма ще изисква инсталация в базата
    #        Направено е с цел ако някой ми е копирал ID мога да си го сменя
    #        Да си инсталирам моя си софтуер а на другото копие достапът ще бъде отнет
    #     '''
    #     libs.conf.CONF.update_option('SYSTEM', soft_id=libs._uuid.mk_soft_id())
    #     dial = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_OK)
    #     dial.ShowModal()


class UpdateRev(gui.UpdateRev, gui_lib.keybords.Keyboard):
    def __init__(self, parent):
        gui.UpdateRev.__init__(self, parent)
        self.close = False
        self.rev = None
        self.SetTitle(gui_lib.msg.config_UpdateRev['name'])
        self.m_staticText68.SetLabel(gui_lib.msg.config_UpdateRev['m_staticText68'])
        self.m_button41.SetLabel(gui_lib.msg.config_UpdateRev['m_button41'])
        self.m_button42.SetLabel(gui_lib.msg.config_UpdateRev['m_button42'])
        self.m_textCtrl16.SetToolTip(gui_lib.msg.config_UpdateRev['m_textCtrl16'])

        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl16.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

    def OnGo(self, event):
        rev = self.m_textCtrl16.GetValue()
        try:
            rev = int(rev)
            self.rev = rev
            self.Destroy()
        except ValueError:
            self.Destroy()

    def OnClose(self, event):
        self.close = True
        self.Destroy()


class Update(gui.Update):
    '''
        Ъпдейтване на програмата за отчет, Нодовете и визуализациите
    '''

    def __init__(self, parent):
        self.parent = parent
        gui.Update.__init__(self, parent)
        self.m_checkBox43.SetLabel(gui_lib.msg.config_Update['m_checkBox43'])
        self.m_checkBox43.SetToolTip(gui_lib.msg.config_Update['m_checkBox43t'])
        self.m_checkBox54.SetLabel(gui_lib.msg.config_Update['m_checkBox54'])
        self.m_checkBox54.SetToolTip(gui_lib.msg.config_Update['m_checkBox54t'])
        #         self.Bind( wx.EVT_SIZE, self.on_resize )
        if os.name != 'posix':
            self.m_button421.Hide()
            self.m_filePicker2.Hide()
        self.on_resize(None)

    def on_resize(self, event):
        self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        self.SetMinSize((self.width, self.height))
        self.m_filePicker2.SetMinSize((self.width, -1))
        self.m_filePicker2.SetSize((self.width, -1))
        self.m_button421.SetMinSize((self.width, -1))
        self.m_button421.SetSize((self.width, -1))
        self.m_button29.SetMinSize((self.width, -1))
        self.m_button29.SetSize((self.width, -1))
        # self.m_filePicker2.SetMinSize((self.width, -1))
        self.m_button31.SetMinSize((self.width, -1))
        self.m_button41.SetMinSize((self.width, -1))
        self.m_button31.SetSize((self.width, -1))
        self.m_button41.SetSize((self.width, -1))
        if event != None:
            event.Skip()
            self.Layout()

    # def SMIBUnixUpdate( self, event ):
    #
    #     dial = wx.MessageDialog(self, *gui_lib.msg.IN_TEST)
    #     dial.ShowModal()

    def OnMainAutoUpdate(self, event):
        self.m_button31.Disable()
        dial = UpdateRev(self)
        dial.ShowModal()

        if dial.close is True:
            self.m_button31.Enable()
            return
        rev = dial.rev

        if os.name == 'posix':
            if os.uname()[-1] == 'armv7l':
                local_folder = '/home/olimex/.colibri_v2/'
                svn_folder = 'svn://NEW_SVN_IP/home/svn/ColibriCMS_BIN/2_1/ARM/'
            else:
                import platform
                local_folder = '/home/%s/.colibri_v2/' % (os.environ['USER'])
                if platform.architecture()[0] == '64bit':
                    svn_folder = 'svn://NEW_SVN_IP/home/svn/ColibriCMS_BIN/2_1/Linux_64/'
                else:
                    svn_folder = 'svn://NEW_SVN_IP/home/svn/ColibriCMS_BIN/2_1/Linux_32/'
        else:
            dlg = wx.MessageBox(gui_lib.msg.POS_SYSTEM_UPDATE, 'Warning',
                                wx.YES_NO | wx.ICON_QUESTION)
            if dlg == wx.NO:
                return
            from os.path import expanduser
            home = expanduser("~")
            local_folder = home + r'\\colibri_v2\\'
            # os.system('cacls "%s" /e /p Everyone:F /T ' % (local_folder))
            svn_folder = 'svn://NEW_SVN_IP/home/svn/ColibriCMS_BIN/2_1/Windows/'
            # os.system("del /f %s" % (local_folder + 'Colibri.exe'))
        svn = libs.subversion.SubVersion(local_folder, svn_folder, 'smib', 'smib_update')
        if os.name == 'posix':
            svn.checkout()
            revision = svn.update(rev=rev)
            if rev != None:
                revision = rev
        else:
            if rev != None:
                revision = rev
            else:
                revision = svn.info()
        # pos = libs.DB.get_pos()
        # pos = json.loads(pos.value)
        libs.conf.CONF.update_option('SYSTEM', rev=revision)
        err = libs.DB.make_obj(libs.models.GetCounterError)
        err.user_id = self.parent.GetParent().GetParent().USER.id
        if os.name == 'posix':
            err.info = 'UPDATE POS' + ': ' + u'POS %s UPDATE REVISION: %s min %s' % (
            libs.conf.ID, revision, str(self.m_checkBox43.GetValue()))
        else:
            err.info = 'UPDATE POS' + ': ' + u'POS %s UPDATE FROM REVISION: %s min %s' % (
            libs.conf.ID, revision, str(self.m_checkBox43.GetValue()))
        libs.DB.add_object_to_session(err)
        if self.m_checkBox43.GetValue() is True:
            min_rev = libs.DB.get_one_where(libs.models.Config, name='MinGuiRev')
            min_rev.value = str(revision)
            libs.DB.add_object_to_session(min_rev)
        libs.DB.commit()

        if os.name == 'posix':
            dial = wx.MessageDialog(None, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            if self.m_checkBox43.GetValue() is True:
                libs.restart_program(user_clean=True)
            else:
                libs.restart_program(user=self.parent.GetParent().GetParent().USER, user_clean=True)
        else:
            dial = wx.MessageDialog(None, *gui_lib.msg.RUN_PROGRAM)
            dial.ShowModal()
            # if self.m_checkBox43.GetValue() is True:
            #     libs.restart_program(user_clean=True)
            # else:
            #     libs.restart_program(user=self.parent.GetParent().GetParent().USER, user_clean=True)

            import subprocess
            if rev != None:
                subprocess.run(local_folder + r'\Update.exe %s' % (rev), shell=True)
            else:
                subprocess.run(local_folder + r'\Update.exe', shell=True)
            self.parent.GetParent().GetParent().OnClose(event)
            # self.parent.GetParent().GetParent().Close()
        # self.m_button31.Enable()

    def SMIBAutoUpdate(self, event):
        self.m_button29.Disable()
        dial = UpdateRev(self)
        dial.ShowModal()
        if dial.close is True:
            self.m_button29.Enable()
            return

        rev = dial.rev
        user = self.parent.GetParent().GetParent().USER
        mashin = libs.DB.get_all_where(libs.models.Device, enable=True, sas=True)

        dlg = wx.MessageBox(gui_lib.msg.REBOOT_YES_NO, 'Info',
                            wx.YES_NO | wx.ICON_QUESTION)
        if dlg == wx.YES:
            reboot = True
        else:
            reboot = False
        dial = UpdateSMIB(self, user, mashin, rev, reboot=reboot)
        dial.ShowModal()
        self.m_button29.Enable()

    def OnRedirectUpdate(self, event):
        self.m_button41.Disable()
        dial = UpdateRev(self)
        dial.ShowModal()

        if dial.close is True:
            self.m_button41.Enable()
            return
        rev = dial.rev
        if self.m_checkBox54.GetValue() is True:
            dlg = wx.MessageDialog(self, gui_lib.msg.config_Update['make_backup'],
                                   gui_lib.msg.config_Update['yes_on_backup'], wx.YES_NO | wx.ICON_WARNING)
            result = dlg.ShowModal()
            if result == wx.ID_NO:
                self.m_button41.Enable()
                return
            else:
                DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                        dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
                DB.connect()
                DB.close_all_session()
        # dial = wx.MessageDialog(self, *gui_lib.msg.IN_TEST)
        # dial.ShowModal()
        response = None

        response = libs.udp.send('update_redirect', ip=libs.conf.SERVER, migrate=self.m_checkBox54.GetValue(), rev=rev)
        if response and self.m_checkBox54.GetValue() is False:
            # response = libs.udp.send('soft_reboot_server', ip=libs.conf.SERVER)
            # time.sleep(30)
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.info = 'UPDATE REDIRECT: %s' % (response)
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            dial = wx.MessageDialog(None, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            self.m_button41.Enable()
            return
        # if self.m_checkBox54.GetValue() is False:
        dial = wx.MessageDialog(None, *gui_lib.msg.PROCES_FINISH_NOT_OK)
        dial.ShowModal()
        self.m_button41.Enable()
        return response

    # def OnVisualUpdate( self, event ):
    #
    #     dial = wx.MessageDialog(self, *gui_lib.msg.IN_TEST)
    #     dial.ShowModal()
    #
    # def OnJPUpdate(self, event):
    #
    #     dial = wx.MessageDialog(self, *gui_lib.msg.IN_TEST)
    #     dial.ShowModal()


class IfJump(gui.KSGuage):
    def __init__(self, parent, mashin, data):
        self.parent = parent
        self.data = data
        gui.KSGuage.__init__(self, parent)
        self.SetTitle(gui_lib.msg.config_IvJump['name'])
        self.m_button23.SetLabel(gui_lib.msg.config_IvJump['m_button23'])
        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width * 0.47, self.height * 0.15))
        self.m_gauge1.SetMinSize((self.width * 0.45, -1))
        self.mashin = mashin
        self.m_gauge1.SetRange(len(self.mashin))
        self.worker = task.IvJump(self, devise=mashin, data=self.data)
        task.EVT_IVJUMP_CONFIG_RESULT(self, self.SetData)
        self.loop = 0
        self.Layout()

    def SetData(self, event):
        '''
            Когато командата мине позицията на лентата се премества с 1
            Ако броя на машините е 50 и са минали 10
            Лентата за прогреса се мести на позиция 10 или 10 % от общата дължина на процеса
        '''
        if type(event.data) == int:
            self.loop = self.loop + event.data
            self.m_gauge1.SetValue(self.loop)
        elif event.data == 'DONE':
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()

    def OnClose(self, event):
        '''
            Затваря прозореца като спира препрограмирането на кей системите
        '''
        self.worker.abort()
        self.Destroy()

    def OnSave(self, event):
        # if  self.parent.with_rfid_in is False:
        #         except AttributeError:
        self.OnTaskStop(event)
        # else:
        #     self.OnTaskStop(event)
        #     self.parent.rfid_task_start(event)
        self.Destroy()

class KSGuage(gui.KSGuage):
    '''
        Вади лентичката която показва до къде с препрограмирането на кей системите е стигнало и колко остава още
    '''

    def __init__(self, parent, mashin, evt, command, user, **kwargs):
        '''
            Конструктор:
            Създава елементите
            Добавя дължина на лентата
            Ако броя на машините е 50 дължината на лентата е 50 като започне от 0
        '''
        self.parent = parent
        self.user = user
        gui.KSGuage.__init__(self, parent)
        self.SetTitle(gui_lib.msg.config_KSGuage['name'])
        self.m_button23.SetLabel(gui_lib.msg.config_KSGuage['m_button23'])
        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width * 0.47, self.height * 0.15))
        self.m_gauge1.SetMinSize((self.width * 0.45, -1))
        self.mashin = mashin
        self.m_gauge1.SetRange(len(self.mashin))
        self.worker = task.KsSendCommand(self, user=self.user, mashin=mashin, evt=evt, command=command, **kwargs)
        task.EVT_KS(self, self.SetData)
        self.loop = 0
        self.Layout()

    def SetData(self, event):
        '''
            Когато командата мине позицията на лентата се премества с 1
            Ако броя на машините е 50 и са минали 10
            Лентата за прогреса се мести на позиция 10 или 10 % от общата дължина на процеса
        '''
        if type(event.data) == int:
            self.loop = self.loop + event.data
            self.m_gauge1.SetValue(self.loop)
        elif event.data == 'DONE':
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()

    def OnClose(self, event):
        '''
            Затваря прозореца като спира препрограмирането на кей системите
        '''
        self.worker.abort()
        self.Destroy()

    def OnSave(self, event):
        # if  self.parent.with_rfid_in is False:
        #         except AttributeError:
        self.OnTaskStop(event)
        # else:
        #     self.OnTaskStop(event)
        #     self.parent.rfid_task_start(event)
        self.Destroy()


class KeySystem(gui.KeySystem):
    '''
        Управление на кей системата
    '''

    def __init__(self, parent):
        '''
            Конструктор
            Изгражда елементите на прозореца
        '''
        self.parent = parent
        gui.KeySystem.__init__(self, parent)
        self.m_checkBox10.SetLabel(gui_lib.msg.config_KeySystem['m_checkBox10'])
        # self.m_button55.SetLabel(gui_lib.msg.config_KeySystem['m_button55'])
        self.m_button24.SetLabel(gui_lib.msg.config_KeySystem['m_button24'])
        self.m_staticText34.SetLabel(gui_lib.msg.config_KeySystem['m_staticText34'])
        self.m_button14.SetLabel(gui_lib.msg.config_KeySystem['m_button14'])
        self.m_button12.SetLabel(gui_lib.msg.config_KeySystem['m_button12'])
        self.m_choice6.SetToolTip(gui_lib.msg.config_KeySystem['m_choice6'])
        self.m_checkBox59.SetToolTip(gui_lib.msg.config_KeySystem['m_checkBox59'])
        self.m_checkBox10.SetToolTip(gui_lib.msg.config_KeySystem['m_checkBox10t'])
        #         self.width, self.height = wx.GetDisplaySize()
        self.user = self.parent.GetParent().GetParent().USER
        var = [gui_lib.msg.config_KeySystem[1]]
        for i in self.parent.GetParent().GetParent().all_mashin():
            var.append(str(i.nom_in_l))
        self.m_choice6.SetItems(var)
        self.m_choice6.SetSelection(0)

        #         self.m_choice4.SetItems(self.parent.GetParent().GetParent().login_user_choiser())
        #         self.m_choice5.SetItems(self.parent.GetParent().GetParent().login_user_choiser())

        #         self.m_spinCtrl10.SetValue(libs.conf.KS_BLOCK)
        self.m_checkBox10.SetValue(libs.conf.KS_JUMP)
        self.m_checkBox59.SetValue(libs.conf.CHANGE_KS_ON_ORDER)
        #         self.m_checkBox11.SetValue(libs.conf.KS_USE_BLOCK)
        #         self.m_checkBox12.SetValue(libs.conf.KS_RANDUM_BLOCK)

        self.owner = None
        self.credit = None
        self.relay_change = False

        #         self.Bind( wx.EVT_SIZE, self.on_resize )
        self.on_resize(None)

    def on_resize(self, event):
        '''
            Преоразмерява елементите спрямо основния прозорец
        '''
        self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        self.SetMinSize((self.width, self.height * 0.8))
        #         self.m_choice6.SetMinSize((self.width*0.3, -1))
        #         self.m_spinCtrl10.SetSize((self.width*0.45, -1))
        #         self.m_choice4.SetMinSize((self.width*0.3, -1))
        #         self.m_choice5.SetMinSize((self.width*0.3, -1))

        self.m_button12.SetMinSize((self.width * 0.2, -1))
        self.m_button14.SetMinSize((self.width * 0.2, -1))
        #         self.m_button18.SetMinSize((self.width*0.4, -1))
        #         self.m_button19.SetMinSize((self.width*0.4, -1))

        if event != None:
            event.Skip()
            self.Layout()

    def get_mashin(self):
        '''
            Взима всички машини и ги добавя в падащо меню
            В случай че искаме да сменим карта на само една машина
        '''
        if self.m_choice6.GetString(self.m_choice6.GetSelection()) == gui_lib.msg.config_KeySystem[1]:
            mashin = self.parent.GetParent().GetParent().login.panel.all_mashin
        else:
            for i in self.parent.GetParent().GetParent().login.panel.all_mashin:
                if i.nom_in_l == int(self.m_choice6.GetString(self.m_choice6.GetSelection())):
                    mashin = [i]
        return mashin

    def OnReset(self, event):
        dialog = KSGuage(self, user=self.user, mashin=self.get_mashin(), evt='ks_reset',
                         command='KEY SYSTEM RESET', cart=self.credit)
        dialog.ShowModal()
        err = libs.DB.make_obj(libs.models.GetCounterError)
        err.user_id = self.parent.GetParent().GetParent().USER.id
        #             err.mashin_nom_in_l = 1
        if self.m_choice6.GetString(self.m_choice6.GetSelection()) == gui_lib.msg.config_KeySystem[1]:
            err.info = 'KEYSYSTEM' + ': ' + gui_lib.msg.config_KeySystem[2] + ' ' + gui_lib.msg.config_KeySystem[1]
        else:
            err.info = 'KEYSYSTEM' + ': ' + gui_lib.msg.config_KeySystem[2]
        libs.DB.add_object_to_session(err)
        libs.DB.commit()

    def OnAddCredit(self, event):
        '''
            Променя картата за кредит с тази на избрания потребител от падащото меню
            На една избрана машина или на всички
        '''
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        dialog = ReadBonusCart(self.parent.GetParent().GetParent())
        dialog.ShowModal()
        self.credit = dialog.cart_id
        if self.credit != None and self.credit is not False:
            dialog = KSGuage(self, user=self.user, mashin=self.get_mashin(), evt='keysystem_change',
                             command='KREDIT KEY CHANGE', cart=self.credit)
            dialog.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            #             err.mashin_nom_in_l = 1
            if self.m_choice6.GetString(self.m_choice6.GetSelection()) == gui_lib.msg.config_KeySystem[1]:
                err.info = 'KEYSYSTEM' + ': ' + gui_lib.msg.config_KeySystem[2] + ' ' + gui_lib.msg.config_KeySystem[1]
            else:
                err.info = 'KEYSYSTEM' + ': ' + gui_lib.msg.config_KeySystem[2]
            libs.DB.add_object_to_session(err)
            libs.DB.commit()

    def OnAddOwner(self, event):
        '''
            Променя картата за оунър с тази на избрания потребител от падащото меню
            На една избрана машина или на всички
        '''
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        dialog = ReadBonusCart(self.parent.GetParent().GetParent())
        dialog.ShowModal()
        self.owner = dialog.cart_id
        if self.owner != None and self.owner is not False:
            dialog = KSGuage(self, user=self.user, evt='keysystem_change', mashin=self.get_mashin(),
                             command='OWNER KEY CHANGE', cart=self.owner)
            dialog.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            #             err.mashin_nom_in_l = 1
            if self.m_choice6.GetString(self.m_choice6.GetSelection()) == gui_lib.msg.config_KeySystem[1]:
                err.info = 'KEYSYSTEM' + ': ' + gui_lib.msg.config_KeySystem[3] + ' ' + gui_lib.msg.config_KeySystem[1]
            else:
                err.info = 'KEYSYSTEM' + ': ' + gui_lib.msg.config_KeySystem[3]
            libs.DB.add_object_to_session(err)
            libs.DB.commit()

    #     def OnChangeRelay(self, event):
    #         '''
    #             решава дали ще се сменя порта на релето
    #         '''
    #         self.relay_change = True
    #
    #     def OnSendBlockAndPort(self, event):
    #         '''
    #             Променя изпол;звания блок на картата или порта на релето
    #             На всички машини или само на избраната от падащото меню
    #         '''
    # #         if self.m_spinCtrl10.GetValue() != libs.conf.KS_BLOCK:
    # #             libs.conf.KS_BLOCK = self.m_spinCtrl10.GetValue()
    # #             libs.conf.CONF.update_option('KEYSYSTEM', block=self.m_spinCtrl10.GetValue())
    # #             dialog = KSGuage(self, evt=libs.smib.KS_BLOCK, mashin=self.get_mashin(), command='KS_BLOCK',
    # #                              use_block=self.m_checkBox11.GetValue(), block=self.m_spinCtrl10.GetValue())
    # #             dialog.ShowModal()
    #         if self.relay_change is True:
    #             dialog = KSGuage(self, evt=libs.smib.KS_RELAY_PORT, mashin=self.get_mashin(), command='KS_RELAY_PORT',
    #                              port=self.m_spinCtrl101.GetValue())
    #             dialog.ShowModal()

    def OnChangeConf(self, event):
        '''
            Определя дали ще се използва скачащ код, блокове, скачащи блокове
            При скачащ код кода на активната карта се сменя в зависимост от крупието ( Най-бързо и препоръчително )

            при използване на блок не се използва вградения в картата номер а собственно генериран като се променя при старт на смяна

            При скачащ блок на случаен принцип се избира от 1-17 на кой точно блок е генериран новия кода (бавно, най-сигурно)
            кода се генерира на блока при започване на смяна
        '''
        # self.parent.GetParent().reboot = True
        if self.m_checkBox10.GetValue() != libs.conf.KS_JUMP:
            libs.conf.KS_JUMP = self.m_checkBox10.GetValue()
            libs.conf.CONF.update_option('KEYSYSTEM', jump=self.m_checkBox10.GetValue())
        if self.m_checkBox10.GetValue() is True:
            # print self.m_checkBox59.GetValue()
            libs.conf.CHANGE_KS_ON_ORDER = self.m_checkBox59.GetValue()
            libs.conf.CONF.update_option('KEYSYSTEM', change_on_order=self.m_checkBox59.GetValue())
        else:
            self.m_checkBox59.SetValue(False)
            libs.conf.CHANGE_KS_ON_ORDER = False
            libs.conf.CONF.update_option('KEYSYSTEM', change_on_order=False)

            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            #             err.mashin_nom_in_l = 1
            err.info = 'KEYSYSTEM' + ': ' + gui_lib.msg.config_KeySystem[4]
            libs.DB.add_object_to_session(err)
            try:
                libs.DB.commit()
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
                return
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                libs.DB.rollback()
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
        dial.ShowModal()


class DB(gui.DB):
    '''
        Настройки на базата данни
    '''

    def __init__(self, parent):
        gui.DB.__init__(self, parent)
        self.parent = parent
        self.m_staticText7.SetLabel(gui_lib.msg.config_DB['m_staticText7'])
        self.m_button48.SetLabel(gui_lib.msg.config_DB['m_button48'])
        self.m_button49.SetLabel(gui_lib.msg.config_DB['m_button49'])
        self.m_button43.SetLabel(gui_lib.msg.config_DB['m_button43'])
        self.m_button46.SetLabel(gui_lib.msg.config_DB['m_button46'])
        self.m_button47.SetLabel(gui_lib.msg.config_DB['m_button47'])
        self.m_button50.SetLabel(gui_lib.msg.config_DB['m_button50'])

        self.m_dirPicker2.SetToolTip(gui_lib.msg.config_DB['m_dirPicker2'])
        self.m_filePicker4.SetToolTip(gui_lib.msg.config_DB['m_filePicker4'])
        self.m_button43.SetToolTip(gui_lib.msg.config_DB['m_button43t'])
        self.m_button46.SetToolTip(gui_lib.msg.config_DB['m_button46t'])
        self.m_button47.SetToolTip(gui_lib.msg.config_DB['m_button47t'])
        self.m_button50.SetToolTip(gui_lib.msg.config_DB['m_button50t'])

    def on_resize(self, event):
        pass

    def SMIBLogClean(self, event):
        # self.parent.GetParent().GetParent().login.login_worker.LOGIN_EVENT.clear()
        DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
        DB.connect()
        DB.close_all_session()
        # libs.udp.send('soft_reboot_server', libs.conf.SERVER)
        DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
        DB.connect()
        # DB.close_all_session()

        DB.db.execute('TRUNCATE system_log;')
        DB.db.execute('ALTER SEQUENCE system_log_id_seq RESTART WITH 1')
        DB.db.execute('TRUNCATE get_counter_error;')
        DB.db.execute('ALTER SEQUENCE get_counter_error_id_seq RESTART WITH 1')
        DB.db.execute('TRUNCATE in_out;')
        DB.db.execute('ALTER SEQUENCE in_out_id_seq RESTART WITH 1')
        DB.commit()
        libs.udp.send('soft_reboot_server', libs.conf.SERVER)
        # obj = libs.DB.make_obj(libs.models.GetCounterError)
        # obj.user_id = self.parent.GetParent().USER.id
        # obj.info = 'DEL LOG TABLE'
        # raise Exception, 'test 1'
        # libs.DB.add_object_to_session(obj)
        # libs.DB.commit()

        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()

        libs.restart_program()

    def OnVakum(self, event):
        # self.parent.GetParent().GetParent().login.panel.login_worker.LOGIN_EVENT.clear()
        import sqlalchemy
        from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
        DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
        DB.connect()
        DB.close_all_session()
        engine = sqlalchemy.create_engine('postgresql://%s:%s@%s:%s/%s' %
                                          (libs.conf.DB_USER, libs.conf.DB_PASS, libs.conf.SERVER, libs.conf.DB_PORT,
                                           libs.conf.DB_NAME),
                                          echo=libs.conf.DB_DEBUG,
                                          echo_pool=False,
                                          pool_reset_on_return=True,
                                          connect_args={'connect_timeout': 30}
                                          )
        connection = engine.raw_connection()
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute("VACUUM FULL")
        cursor.execute("VACUUM ANALYZE")
        libs.udp.send('soft_reboot_server', libs.conf.SERVER)
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()
        libs.restart_program()

    def OnReindex(self, event):
        DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
        DB.connect()
        DB.close_all_session()
        if os.name == 'posix':
            cmd = 'PGPASSWORD="%s" reindexdb -h %s -p %s -U %s -d %s' % (
            libs.conf.DB_PASS, libs.conf.SERVER, libs.conf.DB_PORT, libs.conf.DB_USER, libs.conf.DB_NAME)
        else:
            cmd = r'SET "PGPASSWORD=%s & bin\\reindexdb.exe -h %s -p %s -U %s -d %s' % (
            libs.conf.DB_PASS, libs.conf.SERVER, libs.conf.DB_PORT, libs.conf.DB_USER, libs.conf.DB_NAME)
            # os.system('SET "PGPASSWORD=%s"' % (libs.conf.DB_PASS))
        os.system(cmd)
        libs.udp.send('soft_reboot_server', libs.conf.SERVER)
        dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
        dial.ShowModal()
        libs.restart_program()

    def OnCleanOldData(self, event):
        dlg = wx.MessageBox(gui_lib.msg.config_DB['cleaan_old_data_warning'], 'Info',
                            wx.YES_NO | wx.ICON_QUESTION)
        if dlg == wx.YES:
            my_time = libs.models.TZ.now() - datetime.timedelta(days=367)
            all_tables = [libs.models.KasaTransfer, libs.models.Prihod, libs.models.Razhod,
                          libs.models.Lipsi, libs.models.BosGetMony,
                          libs.models.Order, libs.models.BillTake,
                          libs.models.MonyRKO,
                          libs.models.DayReport, libs.models.BonusCartLog,
                          libs.models.StartWork, libs.models.CustStatistic,
                          libs.models.MonuBackPay, libs.models.BonusPay,
                          libs.models.TombulaPrinted, libs.models.MonyOnCart,
                          libs.models.CustInOutAFT,
                          libs.models.EMGService, libs.models.ClienBonusHold,
                          libs.models.RamClear, libs.models.BankTransfer, libs.models.UserHaveMony,
                          ]
            libs.udp.send('soft_reboot_server', libs.conf.SERVER, timeout=4)
            dial = DellOld(self, user=self.parent.GetParent().USER, table=all_tables,
                           date=libs.models.TZ.date_to_str(my_time, '%Y-%m-%d %H:%M:%S'))
            dial.ShowModal()
        else:
            return

    def OnBackup(self, event):
        dlg = wx.MessageBox(gui_lib.msg.config_DB['long_time'], 'Info',
                            wx.YES_NO | wx.ICON_QUESTION)
        if dlg == wx.NO:
            return
        backup_path = self.m_dirPicker2.GetPath()

        obj = libs.DB.make_obj(libs.models.GetCounterError)
        obj.user_id = self.parent.GetParent().USER.id
        obj.info = 'DB BACKUP'
        libs.DB.add_object_to_session(obj)
        libs.DB.commit()
        DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
        DB.connect()

        data = DB._backup(backup_path)
        if data is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_COPY_OK)
            dial.ShowModal()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_COPY_NOT_OK)
            dial.ShowModal()

    def OnRestory(self, event):
        dlg = wx.MessageBox(gui_lib.msg.config_DB['long_time'], 'Info',
                            wx.YES_NO | wx.ICON_QUESTION)
        if dlg == wx.NO:
            return
        try:
            backup_path = self.m_filePicker4.GetPath()
            if backup_path == '' or backup_path == None or backup_path is False:
                raise KeyError
            elif backup_path[-7:] != '.backup':
                raise KeyError
            user_id = self.parent.GetParent().USER.id
            DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                    dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
            DB.connect()
            # libs.DB.close()
            DB.close_all_session()
            DB = libs.db.PostgreSQL(host=libs.conf.SERVER, user=libs.conf.DB_USER, passwd=libs.conf.DB_PASS,
                                    dbname=libs.conf.DB_NAME, port=libs.conf.DB_PORT)
            DB.connect()
            DB.drop_tables()
            data = DB._restore(backup_path)

            if data is True:
                cur = DB.conn.cursor()
                info = r'DB RESTORY: %s' % (backup_path)
                cmd = r'''INSERT INTO get_counter_error ("user_id", "info", "pub_time") VALUES (%s, '%s', '%s');''' % (
                user_id, str(info), libs.models.TZ.now())
                cur.execute(cmd)
                libs.udp.send('soft_reboot_server', libs.conf.SERVER, timeout=4)
                dial = gui_lib.msg.show(self, gui_lib.msg.DB_RESTORY_OK)
                libs.restart_program()
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_RESTORY_NOT_OK)
                dial.ShowModal()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.DB_RESTORY_NOT_OK)
            dial.ShowModal()


class ShowLog(gui.ShowLog):
    def __init__(self, parent, device):
        self.parent = parent
        self.device = device
        gui.ShowLog.__init__(self, self.parent)
        self.SetTitle(gui_lib.msg.config_ShowLog['name'])
        self.m_button42.SetLabel(gui_lib.msg.config_ShowLog['m_button42'])
        # revision = libs.udp.send('svn_info', self.device.ip)
        # log = libs.udp.send('get_log', self.device.ip)
        diagnostic = libs.udp.send('diagnostic', self.device.ip)
        status = libs.udp.send('status', self.device.ip)

        log = str(status) + '\n\n' + str(diagnostic)
        self.m_richText1.SetValue(log)

    def OnClose(self, event):
        self.Destroy()

class SaveSection(gui.SaveSection):
    def __init__(self, parent):
        gui.SaveSection.__init__(self, parent)
        self.SetTitle(gui_lib.msg.SMIB_SaveSection['name'])
        self.m_button58.SetLabel(gui_lib.msg.SMIB_SaveSection['m_button58'])
        self.m_button59.SetLabel(gui_lib.msg.SMIB_SaveSection['m_button59'])
        self.all_section = {'SAS': False, 'Jackpot':False, 'Keysystem':False, 'Client':False, 'Bonus':False, 'System':False, 'Mail Send':False,
                            'Log Server':False, 'Log Config':False, 'PROC':False, 'RFID':False}
        self.close = True

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        self.close = False
        self.all_section['SAS'] = self.m_checkBox66.GetValue()
        self.all_section['Jackpot'] = self.m_checkBox67.GetValue()
        self.all_section['Keysystem'] = self.m_checkBox72.GetValue()
        self.all_section['Client'] = self.m_checkBox68.GetValue()
        self.all_section['Bonus'] = self.m_checkBox69.GetValue()
        self.all_section['System'] = self.m_checkBox73.GetValue()
        self.all_section['Mail Send'] = self.m_checkBox70.GetValue()
        self.all_section['Log Server'] = self.m_checkBox71.GetValue()
        self.all_section['Log Config'] = self.m_checkBox74.GetValue()
        self.all_section['PROC'] = self.m_checkBox75.GetValue()
        self.all_section['RFID'] = self.m_checkBox76.GetValue()
        self.Destroy()

class AllSMIBConf(gui.KSGuage):
    def __init__(self, parent, user, conf, mashin, **kwargs):
        self.parent = parent
        self.user = user
        self.conf = conf
        self.mashin = mashin
        self.save = kwargs['save_section']
        gui.KSGuage.__init__(self, self.parent)
        self.SetTitle(gui_lib.msg.config_AllSMIBConf['name'])
        self.m_button23.SetLabel(gui_lib.msg.config_AllSMIBConf['m_button23'])
        self.width, self.height = wx.GetDisplaySize()
        self.SetSize((self.width * 0.47, self.height * 0.15))
        self.m_gauge1.SetMinSize((self.width * 0.45, -1))
        self.m_gauge1.SetRange(len(self.mashin))
        # raise KeyError, kwargs
        self.worker = task.SmibConfig(self, user=self.user, mashin=mashin, conf=conf, **kwargs)
        task.EVT_SMIB_CONFIG_RESULT(self, self.SetData)
        self.loop = 0
        self.Layout()

    def SetData(self, event):
        '''
            Когато командата мине позицията на лентата се премества с 1
            Ако броя на машините е 50 и са минали 10
            Лентата за прогреса се мести на позиция 10 или 10 % от общата дължина на процеса
        '''
        if type(event.data) == int:
            self.loop = self.loop + event.data
            self.m_gauge1.SetValue(self.loop)
        elif event.data == 'DONE':
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()

    def OnClose(self, event):
        '''
            Затваря прозореца като спира препрограмирането на кей системите
        '''
        self.worker.abort()
        self.Destroy()

    def OnSave(self, event):
        if self.parent_worker == None:
            #         except AttributeError:
            self.OnTaskStop(event)
        else:
            self.OnTaskStop(event)
            self.parent.rfid_task_start(event)
        self.Destroy()


class SMIB(gui.SMIB, gui_lib.keybords.Keyboard):
    '''
        Настройки на нодовете
    '''

    def __init__(self, parent):
        gui.SMIB.__init__(self, parent)
        self.parent = parent
        self.m_staticText33.SetLabel(gui_lib.msg.config_SMIB['m_staticText33'])

        self.m_staticText801.SetLabel(gui_lib.msg.config_SMIB['m_staticText801'])
        self.choises = []
        for i in libs.conf.ALL_LANGUAGE:
            self.choises.append(libs.conf.ALL_LANGUAGE[i])
        self.m_choice181.SetItems(self.choises)
        self.m_choice181.SetSelection(
            self.choises.index(libs.conf.ALL_LANGUAGE[libs.conf.USE_LANGUAGE]))

        self.m_staticText77.SetLabel(gui_lib.msg.config_SMIB['m_staticText77'])
        self.m_checkBox21.SetLabel(gui_lib.msg.config_SMIB['m_checkBox21'])
        self.m_checkBox62.SetLabel(gui_lib.msg.config_SMIB['m_checkBox62'])
        self.m_checkBox56.SetLabel(gui_lib.msg.config_SMIB['m_checkBox56'])
        self.m_checkBox56.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox56t'])
        self.m_checkBox25.SetLabel(gui_lib.msg.config_SMIB['m_checkBox25'])
        self.m_checkBox22.SetLabel(gui_lib.msg.config_SMIB['m_checkBox22'])
        self.m_checkBox20.SetLabel(gui_lib.msg.config_SMIB['m_checkBox20'])
        self.m_checkBox24.SetLabel(gui_lib.msg.config_SMIB['m_checkBox24'])
        self.m_checkBox23.SetLabel(gui_lib.msg.config_SMIB['m_checkBox23'])
        self.m_checkBox42.SetLabel(gui_lib.msg.config_SMIB['m_checkBox42'])
        self.m_staticText79.SetLabel(gui_lib.msg.config_SMIB['m_staticText522'])
        self.m_staticText81.SetLabel(gui_lib.msg.config_SMIB['m_staticText81'])
        self.m_checkBox79.SetLabel(gui_lib.msg.config_SMIB['m_checkBox79'])

        self.m_checkBox54.SetLabel(gui_lib.msg.config_SMIB['m_checkBox54'])
        self.m_staticText802.SetLabel(gui_lib.msg.config_SMIB['m_staticText802'])

        self.m_checkBox47.SetLabel(gui_lib.msg.config_SMIB['m_checkBox47'])
        self.m_checkBox48.SetLabel(gui_lib.msg.config_SMIB['m_checkBox48'])
        self.m_checkBox50.SetLabel(gui_lib.msg.config_SMIB['m_checkBox50'])

        self.m_checkBox51.SetLabel(gui_lib.msg.config_SMIB['m_checkBox51'])
        self.m_checkBox51.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox51t'])

        self.m_textCtrl26.SetToolTip(gui_lib.msg.config_SMIB['m_textCtrl26t'])
        self.m_textCtrl24.SetToolTip(gui_lib.msg.config_SMIB['m_textCtrl24'])
        self.m_textCtrl23.SetToolTip(gui_lib.msg.config_SMIB['m_textCtrl23'])
        self.m_checkBox21.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox21t'])
        self.m_checkBox25.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox25t'])
        self.m_checkBox22.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox22t'])
        self.m_checkBox20.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox20t'])
        self.m_checkBox24.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox24t'])
        self.m_checkBox23.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox23t'])

        self.m_checkBox42.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox42t'])
        self.m_spinCtrl26.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl26t'])
        self.m_spinCtrl27.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl27t'])
        self.m_textCtrl22.SetToolTip(gui_lib.msg.config_SMIB['m_textCtrl22'])

        self.m_checkBox47.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox47t'])
        self.m_checkBox48.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox48t'])
        self.m_checkBox50.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox50t'])

        self.m_checkBox27.SetLabel(gui_lib.msg.config_SMIB['m_checkBox27'])
        self.m_checkBox311.SetLabel(gui_lib.msg.config_SMIB['m_checkBox311'])
        # self.m_checkBox37.SetLabel(gui_lib.msg.config_SMIB['m_checkBox37'])
        self.m_checkBox39.SetLabel(gui_lib.msg.config_SMIB['m_checkBox39'])
        self.m_checkBox26.SetLabel(gui_lib.msg.config_SMIB['m_checkBox26'])
        self.m_checkBox28.SetLabel(gui_lib.msg.config_SMIB['m_checkBox28'])
        self.m_checkBox281.SetLabel(gui_lib.msg.config_SMIB['m_checkBox281'])
        self.m_checkBox391.SetLabel(gui_lib.msg.config_SMIB['m_checkBox391'])

        self.m_checkBox27.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox27t'])
        self.m_checkBox311.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox311t'])
        # self.m_checkBox37.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox37t'])
        self.m_checkBox39.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox39t'])
        self.m_checkBox26.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox26t'])
        self.m_checkBox28.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox28t'])
        self.m_checkBox281.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox281t'])
        self.m_checkBox391.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox391t'])

        self.m_checkBox31.SetLabel(gui_lib.msg.config_SMIB['m_checkBox31'])
        self.m_checkBox57.SetLabel(gui_lib.msg.config_SMIB['m_checkBox57'])
        self.m_checkBox29.SetLabel(gui_lib.msg.config_SMIB['m_checkBox29'])
        self.m_staticText37.SetLabel(gui_lib.msg.config_SMIB['m_staticText37'])
        self.m_staticText38.SetLabel(gui_lib.msg.config_SMIB['m_staticText38'])

        self.m_checkBox31.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox31t'])
        self.m_checkBox29.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox29t'])
        self.m_spinCtrl13.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl13t'])
        self.m_spinCtrl14.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl14t'])

        self.m_checkBox30.SetLabel(gui_lib.msg.config_SMIB['m_checkBox30'])
        self.m_checkBox321.SetLabel(gui_lib.msg.config_SMIB['m_checkBox321'])
        self.m_staticText522.SetLabel(gui_lib.msg.config_SMIB['m_staticText522'])
        self.m_staticText682.SetLabel(gui_lib.msg.config_SMIB['m_staticText682'])

        self.m_checkBox30.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox30t'])
        self.m_checkBox321.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox321t'])
        self.m_spinCtrl201.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl201t'])
        self.m_spinCtrl211.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl211t'])

        self.m_staticText43.SetLabel(gui_lib.msg.config_SMIB['m_staticText43'])
        self.m_staticText67.SetLabel(gui_lib.msg.config_SMIB['m_staticText67'])
        self.m_staticText68.SetLabel(gui_lib.msg.config_SMIB['m_staticText68'])
        self.m_button391.SetLabel(gui_lib.msg.config_SMIB['m_button391'])
        self.m_staticText42.SetLabel(gui_lib.msg.config_SMIB['m_staticText42'])
        self.m_checkBox341.SetLabel(gui_lib.msg.config_SMIB['m_checkBox341'])
        self.m_staticText681.SetLabel(gui_lib.msg.config_SMIB['m_staticText681'])
        self.m_checkBox80.SetLabel(gui_lib.msg.config_SMIB['m_checkBox80'])

        self.m_spinCtrl19.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl19t'])
        self.m_spinCtrl22.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl22t'])
        self.m_spinCtrl23.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl23t'])
        self.m_button391.SetToolTip(gui_lib.msg.config_SMIB['m_button391t'])
        self.m_spinCtrl18.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl18t'])
        self.m_checkBox341.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox341t'])
        self.m_spinCtrl24.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl24t'])

        self.m_staticText80.SetLabel(gui_lib.msg.config_SMIB['m_staticText80'])
        self.m_checkBox35.SetLabel(gui_lib.msg.config_SMIB['m_checkBox35'])
        self.m_staticText54.SetLabel(gui_lib.msg.config_SMIB['m_staticText54'])
        self.m_staticText521.SetLabel(gui_lib.msg.config_SMIB['m_staticText521'])

        self.m_checkBox35.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox35t'])
        self.m_textCtrl14.SetToolTip(gui_lib.msg.config_SMIB['m_textCtrl14t'])
        self.m_choice16.SetToolTip(gui_lib.msg.config_SMIB['m_choice16t'])

        self.m_checkBox32.SetLabel(gui_lib.msg.config_SMIB['m_checkBox32'])
        self.m_checkBox33.SetLabel(gui_lib.msg.config_SMIB['m_checkBox33'])
        self.m_staticText39.SetLabel(gui_lib.msg.config_SMIB['m_staticText39'])
        self.m_staticText40.SetLabel(gui_lib.msg.config_SMIB['m_staticText40'])
        self.m_button431.SetLabel(gui_lib.msg.config_SMIB['m_button431'])

        self.m_button431.SetToolTip(gui_lib.msg.config_SMIB['m_button431t'])
        self.m_spinCtrl15.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl15t'])
        self.m_spinCtrl16.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl16t'])
        self.m_checkBox33.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox33t'])
        self.m_checkBox32.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox32t'])
        self.m_spinCtrl30.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl30'])

        self.m_checkBox34.SetLabel(gui_lib.msg.config_SMIB['m_checkBox34'])
        self.m_staticText44.SetLabel(gui_lib.msg.config_SMIB['m_staticText44'])
        self.m_staticText45.SetLabel(gui_lib.msg.config_SMIB['m_staticText45'])

        self.m_checkBox34.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox34t'])
        self.m_spinCtrl20.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl20t'])
        self.m_spinCtrl21.SetToolTip(gui_lib.msg.config_SMIB['m_spinCtrl21t'])

        self.m_button38.SetLabel(gui_lib.msg.config_SMIB['m_button38'])
        self.m_button42.SetLabel(gui_lib.msg.config_SMIB['m_button42'])
        self.m_button37.SetLabel(gui_lib.msg.config_SMIB['m_button37'])
        self.m_button36.SetLabel(gui_lib.msg.config_SMIB['m_button36'])
        self.m_button39.SetLabel(gui_lib.msg.config_SMIB['m_button39'])
        self.m_button40.SetLabel(gui_lib.msg.config_SMIB['m_button40'])
        self.m_button41.SetLabel(gui_lib.msg.config_SMIB['m_button41'])
        self.m_button43.SetLabel(gui_lib.msg.config_SMIB['m_button43'])
        self.m_checkBox49.SetLabel(gui_lib.msg.config_SMIB['m_checkBox49'])

        self.m_checkBox49.SetToolTip(gui_lib.msg.config_SMIB['m_checkBox49t'])
        self.m_button38.SetToolTip(gui_lib.msg.config_SMIB['m_button38t'])
        self.m_button42.SetToolTip(gui_lib.msg.config_SMIB['m_button42t'])
        self.m_button37.SetToolTip(gui_lib.msg.config_SMIB['m_button37t'])
        self.m_button36.SetToolTip(gui_lib.msg.config_SMIB['m_button36t'])
        self.m_button39.SetToolTip(gui_lib.msg.config_SMIB['m_button39t'])
        self.m_button40.SetToolTip(gui_lib.msg.config_SMIB['m_button40t'])
        self.m_button41.SetToolTip(gui_lib.msg.config_SMIB['m_button41t'])
        self.m_button43.SetToolTip(gui_lib.msg.config_SMIB['m_button43t'])

        self.m_staticText48.SetLabel(gui_lib.msg.config_SMIB['m_staticText48'])
        self.m_staticText46.SetLabel(gui_lib.msg.config_SMIB['m_staticText46'])
        self.m_staticText50.SetLabel(gui_lib.msg.config_SMIB['m_staticText50'])
        self.m_staticText52.SetLabel(gui_lib.msg.config_SMIB['m_staticText52'])
        self.m_staticText49.SetLabel(gui_lib.msg.config_SMIB['m_staticText49'])
        self.m_staticText47.SetLabel(gui_lib.msg.config_SMIB['m_staticText47'])
        self.m_staticText51.SetLabel(gui_lib.msg.config_SMIB['m_staticText51'])
        self.m_staticText53.SetLabel(gui_lib.msg.config_SMIB['m_staticText53'])

        self.m_staticText89.SetLabel(gui_lib.msg.config_SMIB['m_staticText89'])
        self.m_staticText90.SetLabel(gui_lib.msg.config_SMIB['m_staticText90'])
        self.m_staticText92.SetLabel(gui_lib.msg.config_SMIB['m_staticText92'])

        self.m_button35.SetLabel(gui_lib.msg.config_SMIB['m_button35'])
        my_list = [u'', gui_lib.msg.config_SMIB['list_1'], gui_lib.msg.config_SMIB['list_2'],
                   gui_lib.msg.config_SMIB['list_3'], gui_lib.msg.config_SMIB['list_4'],
                   gui_lib.msg.config_SMIB['list_5'], gui_lib.msg.config_SMIB['list_6'],
                   gui_lib.msg.config_SMIB['list_7'], gui_lib.msg.config_SMIB['list_8'],
                   gui_lib.msg.config_SMIB['list_9']]
        try:
            self.m_choice18.SetItems(my_list)
        except:
            self.m_choice18.SetItems([u''])
        self.m_choice18.SetSelection(0)

        # self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        self.all_ln = self.parent.GetParent().GetParent().all_ln
        if self.all_ln['base'] is not True:
            self.m_checkBox21.Hide()
            self.m_checkBox20.Hide()
        if self.all_ln['keysystem'] is not True:
            self.m_checkBox22.Hide()
        if self.all_ln['bonus_cart'] is not True:
            self.m_checkBox23.Hide()
        if self.all_ln['client'] is not True:
            self.m_checkBox24.Hide()
        if self.all_ln['jackpot'] is not True:
            self.m_checkBox25.Hide()
        #         print self.width, self.height
        self.load_all_smib()
        self.set_log_level()
        self.on_resize(None)
        self.conf = {'SYSTEM': {},
                     'JP_SERVER': {},
                     'LOGGING_SERVER': {},
                     'RFID': {},
                     'KEYSYSTEM': {},
                     'BONUS': {},
                     'LOGGING_FILE': {},
                     'SAS': {},
                     'WATCHDOG': {},
                     'LOGGING_LEVEL': {},
                     'PLAYER': {}}
        self.m_choice10.SetSelection(3)
        self.m_choice11.SetSelection(3)
        self.m_choice8.SetSelection(3)
        self.m_choice9.SetSelection(3)
        self.m_choice12.SetSelection(3)
        self.m_choice13.SetSelection(3)
        self.m_choice14.SetSelection(3)
        self.m_choice15.SetSelection(3)
        self.m_choice16.SetSelection(3)
        self.m_textCtrl14.SetValue(u'192.168.1.6')
        if self.m_checkBox341.GetValue() is True:
            self.m_spinCtrl24.Show()
        self.m_checkBox52.SetValue(True)
        self.m_checkBox52.Hide()
        # self.resize = True
        # self.Bind(wx.EVT_SIZE, self.on_resize)
        # self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.on_resize(None)
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl23.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl26.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl27.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl22.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl24.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl13.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl14.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

            self.m_spinCtrl201.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl211.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl28.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl29.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl231.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)

            self.m_spinCtrl19.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl18.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl22.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl23.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl24.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl14.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

            self.m_spinCtrl15.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl16.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_textCtrl26.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl20.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl21.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
        right = self.parent.GetParent().GetParent().USER.grup.from_json()
        if 8 not in right['config']:
            self.m_button62.Hide()


    def SAS_Tester( self, event ):
        if not self.device:
            return
        response = None
        for i in range(3):
            response = libs.udp.send('sas_stop', self.device.ip)
            if response:
                break
        dial = sas_tester.SasTester(self, self.device)
        dial.ShowModal()
        response = None
        for i in range(3):
            response = libs.udp.send('sas_start', self.device.ip, disconnect=True)
            if response:
                break

    def OnConfig(self, event):
        selected_conf = self.m_choice18.GetSelection()
        if selected_conf == 0:
            pass
        elif selected_conf == 1 or selected_conf == 2 or selected_conf == 8 or selected_conf == 9:
            self.m_checkBox27.SetValue(True)
            self.m_checkBox311.SetValue(True)
            self.m_checkBox28.SetValue(True)
            # self.m_checkBox26.SetValue(True)
            self.m_checkBox56.SetValue(False)
            self.m_textCtrl23.SetValue(u'0.04')
            self.m_checkBox62.SetValue(True)
            self.m_checkBox39.SetValue(False)
            self.m_checkBox391.SetValue(False)
            self.m_checkBox42.SetValue(False)
            self.m_textCtrl22.SetValue('00')
            self.m_textCtrl24.SetValue('2')
            # if self.m_choice7.GetSelection() > 0:
            #     libs.udp.send('conf_update', ip=self.device.ip, section='SAS', aft_won=True, impera=False, timeout=5)
        elif selected_conf == 3:
            self.m_checkBox27.SetValue(False)
            self.m_checkBox311.SetValue(False)
            self.m_checkBox28.SetValue(True)
            # self.m_checkBox26.SetValue(False)
            self.m_checkBox56.SetValue(True)
            self.m_textCtrl23.SetEditable(True)
            self.m_textCtrl23.SetValue(u'0.04')
            self.m_checkBox62.SetValue(True)
            self.m_checkBox39.SetValue(False)
            self.m_checkBox391.SetValue(True)
            self.m_checkBox42.SetValue(False)
            self.m_textCtrl22.SetValue('01')
            self.m_textCtrl24.SetValue('2')
            # if self.m_choice7.GetSelection() > 0:
            #     libs.udp.send('conf_update', ip=self.device.ip, section='SAS', aft_won=True, impera=False, timeout=5)
        elif selected_conf == 4:
            self.m_checkBox27.SetValue(False)
            self.m_checkBox311.SetValue(False)
            self.m_checkBox28.SetValue(True)
            # self.m_checkBox26.SetValue(False)
            self.m_checkBox56.SetValue(False)
            self.m_textCtrl23.SetEditable(True)
            self.m_textCtrl23.SetValue(u'0.05')
            self.m_checkBox62.SetValue(False)
            self.m_checkBox39.SetValue(False)
            self.m_checkBox391.SetValue(True)
            self.m_checkBox42.SetValue(False)
            # self.m_checkBox57.SetValue(False)
            self.m_textCtrl22.SetValue('01')
            self.m_textCtrl24.SetValue('2')
            # if self.m_choice7.GetSelection() > 0:
            #     libs.udp.send('conf_update', ip=self.device.ip, section='SAS', aft_won=True, impera=False, timeout=5)
        elif selected_conf == 5:
            self.m_checkBox27.SetValue(False)
            self.m_checkBox311.SetValue(False)
            self.m_checkBox28.SetValue(True)
            # self.m_checkBox26.SetValue(False)
            self.m_checkBox56.SetValue(False)
            self.m_textCtrl23.SetEditable(True)
            self.m_textCtrl23.SetValue(u'0.04')
            self.m_checkBox62.SetValue(True)
            self.m_checkBox39.SetValue(False)
            self.m_checkBox391.SetValue(True)
            self.m_checkBox42.SetValue(False)
            self.m_textCtrl22.SetValue('01')
            self.m_textCtrl24.SetValue('2')
            # if self.m_choice7.GetSelection() > 0:
            #     libs.udp.send('conf_update', ip=self.device.ip, section='SAS', aft_won=True, impera=False, timeout=5)
        elif selected_conf == 6:
            self.m_checkBox27.SetValue(False)
            self.m_checkBox311.SetValue(False)
            self.m_checkBox28.SetValue(False)
            # self.m_checkBox26.SetValue(False)
            self.m_checkBox56.SetValue(False)
            self.m_textCtrl23.SetEditable(True)
            self.m_textCtrl23.SetValue(u'0.04')
            self.m_checkBox62.SetValue(True)
            self.m_checkBox39.SetValue(False)
            self.m_checkBox391.SetValue(True)
            self.m_checkBox42.SetValue(False)
            self.m_textCtrl22.SetValue('01')
            self.m_textCtrl24.SetValue('2')
            # if self.m_choice7.GetSelection() > 0:
            #     libs.udp.send('conf_update', ip=self.device.ip, section='SAS', aft_won=False, impera=False, timeout=5)
        elif selected_conf == 7:
            self.m_checkBox27.SetValue(True)
            self.m_checkBox311.SetValue(True)
            self.m_checkBox28.SetValue(True)
            # self.m_checkBox26.SetValue(True)
            self.m_checkBox56.SetValue(False)
            self.m_textCtrl23.SetValue(u'0.04')
            self.m_checkBox62.SetValue(True)
            self.m_checkBox39.SetValue(False)
            self.m_checkBox391.SetValue(False)
            self.m_checkBox42.SetValue(False)
            self.m_textCtrl22.SetValue('00')
            self.m_textCtrl24.SetValue('2')
            # if self.m_choice7.GetSelection() > 0:
            #     libs.udp.send('conf_update', ip=self.device.ip, section='SAS', aft_won=True, impera=True, timeout=5)

    def AutoplayEditable(self, event):
        if self.m_checkBox42.GetValue() is True:
            self.m_spinCtrl26.Enable(True)
            self.m_spinCtrl27.Enable(True)
        else:
            self.m_spinCtrl26.Enable(False)
            self.m_spinCtrl27.Enable(False)

    def TimeSleepEditable(self, event):
        if self.m_checkBox391.GetValue() is True:
            self.m_textCtrl23.SetEditable(True)
        else:
            self.m_textCtrl23.SetEditable(False)

    def OnSendMailIfWon(self, event):
        if self.m_checkBox341.GetValue() is True:
            self.m_spinCtrl24.Show()
        else:
            self.m_spinCtrl24.Hide()

    def load_all_smib(self):
        device = libs.DB.get_all_where(libs.models.Device, enable=True, order='nom_in_l', sas=True)
        self.selected_list = [gui_lib.msg.config_SMIB[1]]
        for i in device:
            self.selected_list.append(str(i.nom_in_l))
        self.m_choice7.SetItems(self.selected_list)
        self.m_choice7.SetSelection(0)

    def OnRFIDScanTime(self, event):
        timeout = self.m_spinCtrl23.GetValue()
        scan_time = self.m_spinCtrl22.GetValue()
        rc255 = self.m_checkBox63.GetValue()
        # if self.m_checkBox63.GetValue() is False:
        #     port = '/dev/rfid'
        # else:
        #     port = '/dev/spidev1.0'
        rfid_set = libs.udp.send('rfid_scan_time', ip=self.device.ip, my_timeout=timeout,
                                 scan_time=scan_time, rc255=rc255)
        if rfid_set is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            return

    def set_log_level(self):
        self.all_log_level = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        self.m_choice10.SetItems(self.all_log_level)
        self.m_choice11.SetItems(self.all_log_level)
        self.m_choice8.SetItems(self.all_log_level)
        self.m_choice9.SetItems(self.all_log_level)
        self.m_choice12.SetItems(self.all_log_level)
        self.m_choice13.SetItems(self.all_log_level)
        self.m_choice14.SetItems(self.all_log_level)
        self.m_choice15.SetItems(self.all_log_level)
        self.m_choice16.SetItems(self.all_log_level)

    def sas_proc(self, event):
        if self.m_checkBox20.GetValue() is True:
            response = libs.udp.send('sas_start', self.device.ip)
        else:
            response = libs.udp.send('sas_stop', self.device.ip)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'SAS Activ: %s' % (str(self.m_checkBox20.GetValue()))
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            # libs.udp.send('proc_check', self.device.ip, timeout=0)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def rfid_proc(self, event):
        if self.m_checkBox21.GetValue() is True:
            response = libs.udp.send('rfid_start', self.device.ip)
        else:
            response = libs.udp.send('rfid_stop', self.device.ip)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'RFID Activ: %s' % (str(self.m_checkBox21.GetValue()))
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            # libs.udp.send('proc_check', self.device.ip, timeout=0)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def keysystem_proc(self, event):
        if self.m_checkBox22.GetValue() is True:
            response = libs.udp.send('keysystem_start', self.device.ip)
        else:
            response = libs.udp.send('keysystem_stop', self.device.ip)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'KEYSYSTEM Activ: %s' % (str(self.m_checkBox22.GetValue()))
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            # libs.udp.send('proc_check', self.device.ip, timeout=0)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def bonus_proc(self, event):
        if self.m_checkBox23.GetValue() is True:
            response = libs.udp.send('bonus_start', self.device.ip)
        else:
            response = libs.udp.send('bonus_stop', self.device.ip)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'BONUS CART Activ: %s' % (str(self.m_checkBox23.GetValue()))
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            # libs.udp.send('proc_check', self.device.ip, timeout=0)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def client_proc(self, event):
        if self.m_checkBox24.GetValue() is True:
            response = libs.udp.send('client_cart_start', self.device.ip)
        else:
            response = libs.udp.send('client_cart_stop', self.device.ip)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'CLIENT Activ: %s' % (str(self.m_checkBox24.GetValue()))
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            # libs.udp.send('proc_check', self.device.ip, timeout=0)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def jp_proc(self, event):
        if self.m_checkBox25.GetValue() is True:
            response = libs.udp.send('jackpot_start', self.device.ip)
        else:
            response = libs.udp.send('jackpot_stop', self.device.ip)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'JACKPOT Activ: %s' % (str(self.m_checkBox25.GetValue()))
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            # libs.udp.send('proc_check', self.device.ip, timeout=0)
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def OnSave(self, event):
        nom_in_l = self.m_choice7.GetSelection()
        # self.conf['SYSTEM']['proto_sas'] = self.m_checkBox52.GetValue()
        try:
            self.conf['SAS']['sleep_time'] = float(self.m_textCtrl23.GetValue())
        except:
            self.conf['SAS']['sleep_time'] = 0.04
        try:
            self.conf['SAS']['sas_timeout'] = int(self.m_textCtrl24.GetValue())
        except Exception as e:
            # self.m_textCtrl24.GetValue()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            self.conf['SAS']['sas_timeout'] = 1
        self.conf['SAS']['aft_lock_time'] = self.m_spinCtrl30.GetValue()
        try:
            if self.m_checkBox56.GetValue() is False:
                self.conf['SAS']['aft_check_last_transaction'] = True
            else:
                self.conf['SAS']['aft_check_last_transaction'] = False
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            self.conf['SAS']['aft_check_last_transaction'] = False
        self.conf['SAS']['set_jp_mether_to_out'] = self.m_checkBox62.GetValue()
        lang = self.m_choice181.GetString(self.m_choice181.GetSelection())
        for i in libs.conf.ALL_LANGUAGE:
            if libs.conf.ALL_LANGUAGE[i] == lang:
                lang = i
        self.conf['SYSTEM']['block_bonus_by_bet'] = self.m_checkBox51.GetValue()
        # libs.conf.CONF.update_option('LANGUAGE', use_lang=lang)
        self.conf['SYSTEM']['lang'] = lang
        self.conf['PLAYER']['logo_name'] = self.m_textCtrl231.GetValue()
        self.conf['SAS']['sync_time'] = self.m_checkBox27.GetValue()
        self.conf['SAS']['aft'] = self.m_checkBox28.GetValue()
        self.conf['SAS']['security'] = self.m_checkBox26.GetValue()
        self.conf['SAS']['usb'] = self.m_checkBox281.GetValue()
        self.conf['SAS']['pay_jp_by_hand'] = self.m_checkBox31.GetValue()
        self.conf['SAS']['check_for_game'] = self.m_checkBox311.GetValue()
        self.conf['SAS']['mail_send'] = self.m_checkBox341.GetValue()
        self.conf['SAS']['mail_send_on_won'] = self.m_spinCtrl24.GetValue()
        self.conf['SAS']['delay_rill'] = self.m_checkBox39.GetValue()
        self.conf['SAS']['sleep_on_down'] = self.m_checkBox391.GetValue()
        self.conf['SAS']['last_aft_transaction_from_emg'] = self.m_checkBox80.GetValue()
        # print (self.conf['SAS']['last_aft_transaction_from_emg'])
        self.conf['SAS']['stop_autoplay'] = self.m_checkBox42.GetValue()
        self.conf['SAS']['stop_autoplay_on_won'] = self.m_spinCtrl26.GetValue()
        self.conf['SAS']['stop_autoplay_fix_after_time'] = self.m_spinCtrl27.GetValue() * 60
        self.conf['SAS']['emg_type'] = self.m_choice18.GetSelection()
        self.conf['LOGGING_FILE']['use'] = self.m_checkBox49.GetValue()
        # if self.m_checkBox63.GetValue() is False:
        #     port = '/dev/rfid'
        # else:
        #     port = '/dev/spidev1.0'
        # self.conf['RFID']['port'] = port
        # self.conf['RFID']['rc522'] = self.m_checkBox63.GetValue()
        # if self.m_checkBox37.GetValue() is True:
        #     self.conf['SAS']['aft_key'] = '43'
        # else:
        #     self.conf['SAS']['aft_key'] = '44'

        self.conf['JP_SERVER']['block_if_lost'] = self.m_checkBox29.GetValue()
        self.conf['JP_SERVER']['block_count'] = self.m_spinCtrl13.GetValue()
        self.conf['JP_SERVER']['down_if_credti'] = self.m_spinCtrl14.GetValue()
        self.conf['JP_SERVER']['down_by_aft'] = self.m_checkBox57.GetValue()

        self.conf['KEYSYSTEM']['multi_key'] = self.m_checkBox32.GetValue()
        self.conf['KEYSYSTEM']['aft'] = self.m_checkBox33.GetValue()
        self.conf['KEYSYSTEM']['credit'] = self.m_spinCtrl15.GetValue()
        self.conf['KEYSYSTEM']['report'] = self.m_spinCtrl16.GetValue()
        a = self.m_textCtrl26.GetValue()
        a = a.replace(',', '.')
        try:
            self.conf['KEYSYSTEM']['relay_timeout'] = float(a)
        except:
            self.conf['KEYSYSTEM']['relay_timeout'] = 1

        # self.conf['BONUS']['sas_timeout'] = self.m_spinCtrl17.GetValue()
        self.conf['BONUS']['out'] = self.m_spinCtrl19.GetValue()
        self.conf['BONUS']['pipe_clean'] = self.m_spinCtrl18.GetValue()
        # self.conf['BONUS']['forbiden_out_befor'] = self.m_spinCtrl25.GetValue()

        self.conf['WATCHDOG']['reboot_if_error'] = self.m_checkBox34.GetValue()
        self.conf['WATCHDOG']['check_interval'] = self.m_spinCtrl20.GetValue()
        self.conf['WATCHDOG']['critical_temp'] = self.m_spinCtrl21.GetValue()

        self.conf['WATCHDOG']['proc_chk'] = self.m_checkBox47.GetValue()
        self.conf['WATCHDOG']['net_chk'] = self.m_checkBox48.GetValue()
        self.conf['WATCHDOG']['sys_chk'] = self.m_checkBox50.GetValue()

        self.conf['LOGGING_LEVEL']['server'] = self.all_log_level[self.m_choice10.GetSelection()]
        self.conf['LOGGING_LEVEL']['rfid'] = self.all_log_level[self.m_choice11.GetSelection()]
        self.conf['LOGGING_LEVEL']['system'] = self.all_log_level[self.m_choice8.GetSelection()]
        self.conf['LOGGING_LEVEL']['sas'] = self.all_log_level[self.m_choice9.GetSelection()]
        self.conf['LOGGING_LEVEL']['keysystem'] = self.all_log_level[self.m_choice12.GetSelection()]
        self.conf['LOGGING_LEVEL']['bonus'] = self.all_log_level[self.m_choice13.GetSelection()]
        self.conf['LOGGING_LEVEL']['jpserver'] = self.all_log_level[self.m_choice14.GetSelection()]
        self.conf['LOGGING_LEVEL']['client_cart'] = self.all_log_level[self.m_choice15.GetSelection()]
        self.conf['PLAYER']['skin'] = self.m_spinCtrl29.GetValue()
        # self.conf['PLAYER']['use_touch'] = True
        # self.conf['PLAYER']['sas_timeout'] = self.m_spinCtrl191.GetValue()
        self.conf['PLAYER']['player_timeout'] = self.m_spinCtrl201.GetValue()
        self.conf['PLAYER']['bonus_on_credit'] = self.m_spinCtrl211.GetValue()
        self.conf['PLAYER']['lock_emg_if_no_cust'] = self.m_checkBox321.GetValue()
        self.conf['PLAYER']['anime_use'] = self.m_checkBox54.GetValue()
        self.conf['PLAYER']['anime_num'] = self.m_spinCtrl28.GetValue()
        self.conf['PLAYER']['lock_bill_if_no_cust'] = self.m_checkBox30.GetValue()
        self.conf['PLAYER']['show_monybeck_pay'] = self.m_checkBox79.GetValue()

        self.conf['LOGGING_SERVER']['server_ip'] = self.m_textCtrl14.GetValue()
        self.conf['LOGGING_SERVER']['use'] = self.m_checkBox35.GetValue()
        self.conf['LOGGING_SERVER']['level'] = self.all_log_level[self.m_choice16.GetSelection()]
        try:

            int(self.m_textCtrl22.GetValue(), 16)
            self.conf['SAS']['sas_n'] = self.m_textCtrl22.GetValue()
        except:
            self.conf['SAS']['sas_n'] = u'00'

        # self.conf['RFID']['timeout'] = self.m_spinCtrl23.GetValue()
        # self.conf['RFID']['scan_time'] = self.m_spinCtrl22.GetValue()
        if nom_in_l > 0:
            libs.udp.send('backup_conf', ip=self.device.ip)
            system_response = libs.udp.send('conf_update', ip=self.device.ip, section='SYSTEM',
                                            lang=self.conf['SYSTEM']['lang'],
                                            block_bonus_by_bet=self.conf['SYSTEM']['block_bonus_by_bet'],
                                            )

            sas_response = libs.udp.send('conf_update', ip=self.device.ip, section='SAS',
                                         sync_time=self.conf['SAS']['sync_time'],
                                         aft=self.conf['SAS']['aft'], security=self.conf['SAS']['security'],
                                         usb=self.conf['SAS']['usb'], pay_jp_by_hand=self.conf['SAS']['pay_jp_by_hand'],
                                         check_for_game=self.conf['SAS']['check_for_game'],
                                         mail_send_on_won=self.conf['SAS']['mail_send_on_won'],
                                         mail_send=self.conf['SAS']['mail_send'],
                                         # aft_key=self.conf['SAS']['aft_key'],
                                         delay_rill=self.conf['SAS']['delay_rill'],
                                         sleep_on_down=self.conf['SAS']['sleep_on_down'],
                                         stop_autoplay=self.conf['SAS']['stop_autoplay'],
                                         stop_autoplay_on_won=self.conf['SAS']['stop_autoplay_on_won'],
                                         stop_autoplay_fix_after_time=self.conf['SAS']['stop_autoplay_fix_after_time'],
                                         sas_n=self.conf['SAS']['sas_n'],
                                         sleep_time=self.conf['SAS']['sleep_time'],
                                         sas_timeout=self.conf['SAS']['sas_timeout'],
                                         aft_check_last_transaction=self.conf['SAS']['aft_check_last_transaction'],
                                         set_jp_mether_to_out = self.conf['SAS']['set_jp_mether_to_out'],
                                         emg_type = self.conf['SAS']['emg_type'],
                                         aft_lock_time = self.conf['SAS']['aft_lock_time'],
                                         last_aft_transaction_from_emg = self.conf['SAS']['last_aft_transaction_from_emg'],
                                         )

            jp_response = libs.udp.send('conf_update', ip=self.device.ip, section='JP_SERVER',
                                        block_if_lost=self.conf['JP_SERVER']['block_if_lost'],
                                        block_count=self.conf['JP_SERVER']['block_count'],
                                        down_if_credti=self.conf['JP_SERVER']['down_if_credti'],
                                        down_by_aft=self.conf['JP_SERVER']['down_by_aft']
                                        )
            ks_response = libs.udp.send('conf_update', ip=self.device.ip, section='KEYSYSTEM',
                                        multi_key=self.conf['KEYSYSTEM']['multi_key'],
                                        aft=self.conf['KEYSYSTEM']['aft'],
                                        credit=self.conf['KEYSYSTEM']['credit'],
                                        report=self.conf['KEYSYSTEM']['report'],
                                        relay_timeout=self.conf['KEYSYSTEM']['relay_timeout'],
                                        )
            bonus_response = libs.udp.send('conf_update', ip=self.device.ip, section='BONUS',
                                           # sas_timeout=self.conf['BONUS']['sas_timeout'],
                                           out=self.conf['BONUS']['out'],
                                           pipe_clean=self.conf['BONUS']['pipe_clean'],
                                           # forbiden_out_befor=self.conf['BONUS']['forbiden_out_befor'],
                                           )
            watchdog_response = libs.udp.send('conf_update', ip=self.device.ip, section='WATCHDOG',
                                              reboot_if_error=self.conf['WATCHDOG']['reboot_if_error'],
                                              check_interval=self.conf['WATCHDOG']['check_interval'],
                                              critical_temp=self.conf['WATCHDOG']['critical_temp'],
                                              proc_chk=self.conf['WATCHDOG']['proc_chk'],
                                              net_chk=self.conf['WATCHDOG']['net_chk'],
                                              sys_chk=self.conf['WATCHDOG']['sys_chk'],
                                              )
            log_level_response = libs.udp.send('conf_update', ip=self.device.ip, section='LOGGING_LEVEL',
                                               server=self.conf['LOGGING_LEVEL']['server'],
                                               rfid=self.conf['LOGGING_LEVEL']['rfid'],
                                               system=self.conf['LOGGING_LEVEL']['system'],
                                               sas=self.conf['LOGGING_LEVEL']['sas'],
                                               keysystem=self.conf['LOGGING_LEVEL']['keysystem'],
                                               bonus=self.conf['LOGGING_LEVEL']['bonus'],
                                               jpserver=self.conf['LOGGING_LEVEL']['jpserver'],
                                               client_cart=self.conf['LOGGING_LEVEL']['client_cart']
                                               )

            player_response = libs.udp.send('conf_update', ip=self.device.ip,
                                            # use_touch=self.conf['PLAYER']['use_touch'],
                                            # sas_timeout=self.conf['PLAYER']['sas_timeout'],
                                            player_timeout=self.conf['PLAYER']['player_timeout'],
                                            bonus_on_credit=self.conf['PLAYER']['bonus_on_credit'],
                                            section='PLAYER',
                                            lock_emg_if_no_cust=self.conf['PLAYER']['lock_emg_if_no_cust'],
                                            logo_name=self.conf['PLAYER']['logo_name'],
                                            anime_use=self.conf['PLAYER']['anime_use'],
                                            anime_num=self.conf['PLAYER']['anime_num'],
                                            skin=self.conf['PLAYER']['skin'],
                                            lock_bill_if_no_cust=self.conf['PLAYER']['lock_bill_if_no_cust'],
                                            show_monybeck_pay=self.conf['PLAYER']['show_monybeck_pay']
                                            )

            logging_server = libs.udp.send('conf_update', ip=self.device.ip, section='LOGGING_SERVER',
                                           use=self.conf['LOGGING_SERVER']['use'],
                                           level=self.conf['LOGGING_SERVER']['level'],
                                           server_ip=self.conf['LOGGING_SERVER']['server_ip'])
            log_file = libs.udp.send('conf_update', ip=self.device.ip, section='LOGGING_FILE',
                                     use=self.conf['LOGGING_FILE']['use'])
            # rfid_response = libs.udp.send('conf_update', ip=self.device.ip, section='RFID',
            #                               rc522=self.conf['RFID']['rc522'], rfid_port=self.conf['RFID']['port'])
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'Config SMIB Change'
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            # print logging_server == None, player_response == None, sas_response == None, jp_response==None, ks_response==None, bonus_response==None, watchdog_response==None, log_level_response == None
            if system_response == None or log_file == None or logging_server == None or player_response == None or sas_response == None or jp_response == None or ks_response == None or bonus_response == None or watchdog_response == None or log_level_response == None:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
                dial.ShowModal()
                return
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.UPDATE_SMIB_AFTER_REBOOT)
                dial.ShowModal()
                # self.OnReboot(event)
        else:
            dlg = wx.MessageBox(gui_lib.msg.CHANGE_ALL_SMIB_CONF, 'Warning',
                                wx.YES_NO | wx.ICON_QUESTION)
            if dlg == wx.NO:
                return
            mashin = libs.DB.get_all_where(libs.models.Device, enable=True, sas=True)
            my_section = SaveSection(self)
            my_section.ShowModal()
            if my_section.close == True:
                return
            save_section = my_section.all_section
            # raise KeyError, save_section
            RFID = {'my_timeout': self.m_spinCtrl23.GetValue(),
                    'scan_time': self.m_spinCtrl22.GetValue(),
                    'rc255': self.m_checkBox63.GetValue()}
            PROC = {'SAS':self.m_checkBox20.GetValue(),
                    'RFID':self.m_checkBox21.GetValue(),
                    'JP':self.m_checkBox25.GetValue(),
                    'Client':self.m_checkBox24.GetValue(),
                    'Keysystem':self.m_checkBox22.GetValue(),
                    'Bonus':self.m_checkBox23.GetValue()}

            dial = AllSMIBConf(self, mashin=mashin, user=self.parent.GetParent().GetParent().USER, conf=self.conf, save_section=save_section,
                               RFID=RFID, PROC=PROC)
            dial.ShowModal()

    def OnLoad(self, event):
        self.m_choice18.SetSelection(0)
        nom_in_l = self.m_choice7.GetSelection()
        if nom_in_l > 0:
            nom_in_l = self.selected_list[nom_in_l]
        elif nom_in_l > -1:
            self.conf = {'SYSTEM': {},
                         'JP_SERVER': {},
                         'LOGGING_SERVER': {},
                         'RFID': {},
                         'KEYSYSTEM': {},
                         'BONUS': {},
                         'LOGGING_FILE': {},
                         'SAS': {},
                         'WATCHDOG': {},
                         'LOGGING_LEVEL': {},
                         'PLAYER': {}}
            return
        else:
            return

        self.device = libs.DB.get_one_where(libs.models.Device, nom_in_l=nom_in_l, enable=True)
        try:
            self.db = libs.udp.send('db_get', self.device.ip, key='WORKING_MODULE')
            self.conf = {}
            all_section = ['SYSTEM',
                           'JP_SERVER',
                           'LOGGING_SERVER',
                           'RFID',
                           'KEYSYSTEM',
                           'BONUS',
                           'LOGGING_FILE',
                           'SAS',
                           'WATCHDOG',
                           'LOGGING_LEVEL',
                           'PLAYER']

            for i in all_section:
                self.conf[i] = libs.udp.send('get_conf', self.device.ip, section=i)
                if self.conf[i] == None:
                    dial = wx.MessageDialog(self, *gui_lib.msg.NO_MASHIN_CONNECTION)
                    dial.ShowModal()
                    return
            if 'show_monybeck_pay' not in self.conf['PLAYER']:
                self.m_checkBox79.SetValue(False)
            else:
                if self.conf['PLAYER']['show_monybeck_pay'] == 'False':
                    self.m_checkBox79.SetValue(False)
                else:
                    self.m_checkBox79.SetValue(True)
            self.m_choice181.SetSelection(
                self.choises.index(libs.conf.ALL_LANGUAGE[self.conf['SYSTEM']['lang']]))
            if self.conf['JP_SERVER']['down_by_aft'] == 'False':
                self.m_checkBox57.SetValue(False)
            else:
                self.m_checkBox57.SetValue(True)
            if self.conf['SYSTEM']['block_bonus_by_bet'] == 'False':
                self.m_checkBox51.SetValue(False)
            else:
                self.m_checkBox51.SetValue(True)

            # if self.conf['SYSTEM']['proto_sas'] == 'False':
            #     self.m_checkBox52.SetValue(False)
            # else:
            self.m_checkBox52.SetValue(True)

            self.m_textCtrl26.SetValue(self.conf['KEYSYSTEM']['relay_timeout'])
            self.m_checkBox22.SetValue(self.db['WORKING_MODULE']['keysystem'])
            self.m_checkBox20.SetValue(self.db['WORKING_MODULE']['sas'])
            self.m_checkBox21.SetValue(self.db['WORKING_MODULE']['rfid'])
            self.m_checkBox25.SetValue(self.db['WORKING_MODULE']['jackpot'])
            self.m_checkBox23.SetValue(self.db['WORKING_MODULE']['bonus_cart'])
            self.m_checkBox24.SetValue(self.db['WORKING_MODULE']['client_cart'])
            self.m_spinCtrl22.SetValue(int(self.conf['RFID']['scan_time']))
            self.m_spinCtrl23.SetValue(int(self.conf['RFID']['rfid_timeout']))
            self.m_textCtrl231.SetValue(self.conf['PLAYER']['logo_name'])
            if self.conf['RFID']['rc522'] == 'True':
                self.m_checkBox63.SetValue(True)
            else:
                self.m_checkBox63.SetValue(False)
            if self.conf['PLAYER']['anime_use'] == 'True':
                self.m_checkBox54.SetValue(True)
            else:
                self.m_checkBox54.SetValue(False)
            self.m_spinCtrl28.SetValue(int(self.conf['PLAYER']['anime_num']))
            if self.conf['LOGGING_FILE']['use'] == 'True':
                self.m_checkBox49.SetValue(True)
            else:
                self.m_checkBox49.SetValue(False)
            if self.conf['SAS']['stop_autoplay'] == 'True':
                self.m_checkBox42.SetValue(True)
                self.m_spinCtrl26.Enable(True)
                self.m_spinCtrl27.Enable(True)
            else:
                self.m_checkBox42.SetValue(False)
                self.m_spinCtrl26.Enable(False)
                self.m_spinCtrl27.Enable(False)
            if 'aft_lock_time' in self.conf['SAS']:
                self.m_spinCtrl30.SetValue(self.conf['SAS']['aft_lock_time'])
            self.m_textCtrl24.SetValue(str(self.conf['SAS']['sas_timeout']))
            self.m_spinCtrl26.SetValue(int(self.conf['SAS']['stop_autoplay_on_won']))
            self.m_spinCtrl27.SetValue(int(self.conf['SAS']['stop_autoplay_fix_after_time']) / 60)
            # try:
            self.m_textCtrl22.SetValue(self.conf['SAS']['sas_n'])
            # except KeyError:
            #     self.m_textCtrl22.SetValue(u'00')
            self.m_choice18.SetSelection(int(self.conf['SAS']['emg_type']))
            self.m_textCtrl23.SetValue(str(self.conf['SAS']['sleep_time']))
            if self.conf['WATCHDOG']['proc_chk'] == 'True':
                self.m_checkBox47.SetValue(True)
            else:
                self.m_checkBox47.SetValue(False)
            if self.conf['WATCHDOG']['net_chk'] == 'True':
                self.m_checkBox48.SetValue(True)
            else:
                self.m_checkBox48.SetValue(False)
            if self.conf['WATCHDOG']['sys_chk'] == 'True':
                self.m_checkBox50.SetValue(True)
            else:
                self.m_checkBox50.SetValue(False)
            if self.conf['SAS']['set_jp_mether_to_out'] == 'False':
                self.m_checkBox62.SetValue(False)
            else:
                self.m_checkBox62.SetValue(True)

            if self.conf['SAS']['set_jp_mether_to_out'] == 'False':
                self.m_checkBox62.SetValue(False)
            else:
                self.m_checkBox62.SetValue(True)

            if self.conf['SAS']['last_aft_transaction_from_emg'] == 'False':
                self.m_checkBox80.SetValue(False)
            else:
                self.m_checkBox80.SetValue(True)
            if self.conf['SAS']['sleep_on_down'] == 'True':
                self.m_checkBox391.SetValue(True)
                self.m_textCtrl23.SetEditable(True)
            else:
                self.m_checkBox391.SetValue(False)
                self.m_textCtrl23.SetEditable(False)
            if self.conf['SAS']['delay_rill'] == 'True':
                self.m_checkBox39.SetValue(True)
            else:
                self.m_checkBox39.SetValue(False)
            if self.conf['SAS']['check_for_game'] == 'True':
                check_for_game = True
            else:
                check_for_game = False
            self.m_checkBox311.SetValue(check_for_game)

            # if self.conf['SAS']['aft_key'] == '43':
            #     self.m_checkBox37.SetValue(True)
            # else:
            #     self.m_checkBox37.SetValue(False)
            try:
                if self.conf['PLAYER']['lock_bill_if_no_cust'] == 'True':
                    lock_bill_if_no_cust = True
                else:
                    lock_bill_if_no_cust = False
            except:
                lock_bill_if_no_cust = False
            if self.conf['PLAYER']['lock_emg_if_no_cust'] is True:
                lock_emg_if_no_cust = True
            else:
                lock_emg_if_no_cust = False
            self.m_checkBox321.SetValue(lock_emg_if_no_cust)
            self.m_checkBox30.SetValue(lock_bill_if_no_cust)
            # self.m_spinCtrl191.SetValue(int(self.conf['PLAYER']['sas_timeout']))
            self.m_spinCtrl201.SetValue(int(self.conf['PLAYER']['player_timeout']))
            # try:
            self.m_spinCtrl29.SetValue(int(self.conf['PLAYER']['skin']))
            # except:
            #     pass
            #             self.m_spinCtrl201.SetValue(int(self.conf['PLAYER']['timeout']))
            self.m_spinCtrl211.SetValue(int(self.conf['PLAYER']['bonus_on_credit']))

            if self.conf['SAS']['sync_time'] == 'True':
                sync_time = True
            else:
                sync_time = False
            self.m_checkBox27.SetValue(sync_time)
            if self.conf['SAS']['aft'] == 'True':
                aft = True
            else:
                aft = False
            if self.conf['SAS']['mail_send'] == 'True':
                mail_send = True
                self.m_checkBox341.Show()
            else:
                mail_send = False
                self.m_spinCtrl24.Hide()

            if mail_send is True:
                self.m_spinCtrl24.SetValue(int(self.conf['SAS']['mail_send_on_won']))
                self.m_checkBox341.SetValue(True)
                # self.m_spinCtrl24.SetValue(int(self.conf['SAS']['mail_send_on_won']))
                self.m_spinCtrl24.Show()
            else:
                self.m_checkBox341.SetValue(False)
                self.m_spinCtrl24.SetValue(2000)
                self.m_spinCtrl24.Hide()
            self.m_checkBox28.SetValue(aft)
            if self.conf['SAS']['security'] == 'True':
                security = True
            else:
                security = False
            self.m_checkBox26.SetValue(security)
            if self.conf['SAS']['usb'] == 'True':
                usb = True
            else:
                usb = False
            self.m_checkBox281.SetValue(usb)
            if self.conf['SAS']['pay_jp_by_hand'] == 'False':
                pay_jp_by_hand = False
            else:
                pay_jp_by_hand = True
            self.m_checkBox31.SetValue(pay_jp_by_hand)
            if self.conf['JP_SERVER']['block_if_lost'] == 'False':
                block_if_lost = False
            else:
                block_if_lost = True
            self.m_checkBox29.SetValue(block_if_lost)
            self.m_spinCtrl13.SetValue(int(self.conf['JP_SERVER']['block_count']))
            self.m_spinCtrl14.SetValue(int(self.conf['JP_SERVER']['down_if_credti']))
            if self.conf['KEYSYSTEM']['multi_key'] == 'False':
                multi_key = False
            else:
                multi_key = True
            self.m_checkBox32.SetValue(multi_key)
            if self.conf['KEYSYSTEM']['aft'] == 'False':
                aft = False
            else:
                aft = True
            self.m_checkBox33.SetValue(aft)
            self.m_spinCtrl15.SetValue(int(self.conf['KEYSYSTEM']['credit']))
            self.m_spinCtrl16.SetValue(int(self.conf['KEYSYSTEM']['report']))

            # self.m_spinCtrl17.SetValue(int(self.conf['BONUS']['sas_timeout']))
            self.m_spinCtrl19.SetValue(int(self.conf['BONUS']['out']))
            self.m_spinCtrl18.SetValue(int(self.conf['BONUS']['pipe_clean']))
            # self.m_spinCtrl25.SetValue(int(self.conf['BONUS']['forbiden_out_befor']))

            if self.conf['WATCHDOG']['reboot_if_error'] == 'False':
                reboot_if_error = False
            else:
                reboot_if_error = True
            self.m_checkBox34.SetValue(reboot_if_error)
            self.m_spinCtrl20.SetValue(round(float(self.conf['WATCHDOG']['check_interval'])))
            self.m_spinCtrl21.SetValue(round(float(self.conf['WATCHDOG']['critical_temp'])))
            if self.conf['LOGGING_SERVER']['use'] == 'False':
                use = False
            else:
                use = True
            self.m_checkBox35.SetValue(use)
            try:
                self.m_textCtrl14.SetValue(self.conf['LOGGING_SERVER']['server_ip'])
            except KeyError:
                self.conf['LOGGING_SERVER']['server_ip'] = self.conf['LOGGING_SERVER']['ip']

            level = {}
            for i in self.conf['LOGGING_LEVEL']:
                if self.conf['LOGGING_LEVEL'][i] == 'DEBUG':
                    level[i] = 0
                elif self.conf['LOGGING_LEVEL'][i] == 'INFO':
                    level[i] = 1
                elif self.conf['LOGGING_LEVEL'][i] == 'WARNING':
                    level[i] = 2
                elif self.conf['LOGGING_LEVEL'][i] == 'ERROR':
                    level[i] = 3
                elif self.conf['LOGGING_LEVEL'][i] == 'CRITICAL':
                    level[i] = 4
                else:
                    level[i] = 2
            self.m_choice10.SetSelection(level['server'])
            self.m_choice11.SetSelection(level['rfid'])
            self.m_choice8.SetSelection(level['system'])
            self.m_choice9.SetSelection(level['sas'])
            self.m_choice12.SetSelection(level['keysystem'])
            self.m_choice13.SetSelection(level['bonus'])
            self.m_choice14.SetSelection(level['jpserver'])
            self.m_choice15.SetSelection(level['client_cart'])
            level = 3
            if self.conf['LOGGING_SERVER']['level'] == 'DEBUG':
                level = 0
            elif self.conf['LOGGING_SERVER']['level'] == 'INFO':
                level = 1
            elif self.conf['LOGGING_SERVER']['level'] == 'WARNING':
                level = 2
            elif self.conf['LOGGING_SERVER']['level'] == 'ERROR':
                level = 3
            elif self.conf['LOGGING_SERVER']['level'] == 'CRITICAL':
                level = 4
            else:
                level = 1
            self.m_choice16.SetSelection(level)

        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            return

    def OnDisableDenom(self, event):
        if not self.device:
            return False
        # game_n = libs.udp.send('sas.get_single_meter', self.device.ip, command='selected game')
        response = libs.udp.send('sas.game_disable_denomination', self.device.ip, disable=True)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'Stop game denomination'
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def enable_denomination(self, event):
        if not self.device:
            return False
        # game_n = libs.udp.send('sas.get_single_meter', self.device.ip, command='selected game')
        response = libs.udp.send('sas.game_disable_denomination', self.device.ip, disable=False)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'Enable game denomination'
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def jackpot_enable(self, event):
        if not self.device:
            return False
        response = libs.udp.send('sas.enable_game_from_jackpot', self.device.ip)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'Disable game from jackpot'
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def OnDisableJP(self, event):
        if not self.device:
            return False
        response = libs.udp.send('sas.disable_game_from_jackpot', self.device.ip)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'Disable Game from jackpot'
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def OnLogGet(self, event):
        if not self.device:
            return False
        dial = ShowLog(self, self.device)
        dial.ShowModal()

    # def OnResizeVar(self, event):
    #     if not self.device:
    #         return False
    #     response = libs.udp.send('resize_var', self.device.ip)
    #     if response is True:
    #         dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
    #         dial.ShowModal()
    #         err = libs.DB.make_obj(libs.models.GetCounterError)
    #         err.user_id = self.parent.GetParent().GetParent().USER.id
    #         err.mashin_nom_in_l = self.device.nom_in_l
    #         err.info = 'SMIB' + ': ' + u'Resize var partition'
    #         libs.DB.add_object_to_session(err)
    #         libs.DB.commit()
    #     else:
    #         dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
    #         dial.ShowModal()
    #     return True

    def OnReset(self, event):
        if not self.device:
            return False
        libs.udp.send('smib_reset', self.device.ip)
        # libs.udp.send('db_del', self.device.ip)
        # libs.udp.send('conf_del', self.device.ip)
        # response = libs.udp.send('resize_var', self.device.ip)
        # if response is not True:
        libs.udp.send('reboot', self.device.ip)
        err = libs.DB.make_obj(libs.models.GetCounterError)
        err.user_id = self.parent.GetParent().GetParent().USER.id
        err.mashin_nom_in_l = self.device.nom_in_l
        err.info = 'SMIB' + ': ' + u'Reset SMIB'
        libs.DB.add_object_to_session(err)
        libs.DB.commit()
        # libs.udp.send('reboot', self.device.ip)
        return True

    def OnReboot(self, event):
        if not self.device:
            return False
        response = libs.udp.send('soft_reboot', self.device.ip)
        if response is True:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'Reboot SMIB'
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        return True

    def OnAutoUpdate(self, event):
        if not self.device:
            return False
        dial = UpdateRev(self)
        dial.ShowModal()
        if dial.close is True:
            return
        rev = dial.rev
        response = None
        # for i in range(3):
        dlg = wx.MessageBox(gui_lib.msg.REBOOT_YES_NO, 'Info',
                            wx.YES_NO | wx.ICON_QUESTION)
        if dlg == wx.YES:
            soft_reboot = True
        else:
            soft_reboot = False
        if rev == None:
            response = libs.udp.send('svn_update', self.device.ip, soft_reboot=soft_reboot)
        else:
            response = libs.udp.send('svn_update', self.device.ip, rev=rev, soft_reboot=soft_reboot)
        if response == None or response is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'UPDATE SMIB Error'
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
        else:
            dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().GetParent().USER.id
            err.mashin_nom_in_l = self.device.nom_in_l
            err.info = 'SMIB' + ': ' + u'UPDATE rev ' + str(response)
            libs.DB.add_object_to_session(err)
            libs.DB.commit()
            # response = libs.udp.send('soft_reboot', self.device.ip)

            # return self.OnReboot(event)
            # dial = wx.MessageDialog(self, *gui_lib.msg.UPDATE_SMIB_AFTER_REBOOT)
            # dial.ShowModal()
        return True

    def OnRelayTest(self, event):
        response = libs.udp.send('relay_test', self.device.ip)
        if response is not True:
            dial = wx.MessageDialog(None, *gui_lib.msg.PROCES_FINISH_NOT_OK)
            dial.ShowModal()
        else:
            dial = wx.MessageDialog(None, *gui_lib.msg.PROCES_FINISH)
            dial.ShowModal()
        return response

    def on_resize(self, event):
    #     self.resize = True
    #
    # def OnIdle(self, event):
    #     if not self.resize:
    #         return
    #     self.resize = False
        self.width, self.height = self.parent.GetParent().GetParent().GetSize()
        self.SetSize((self.width, self.height * 0.8))
        self.m_scrolledWindow2.SetMinSize((self.width * 0.97, self.height * 0.50))
        self.m_scrolledWindow2.SetSize((self.width * 0.97, self.height * 0.50))
        self.m_textCtrl14.SetSize((self.width * 0.10, -1))
        self.m_textCtrl14.SetMinSize((self.width * 0.10, -1))

        self.m_spinCtrl14.SetSize((self.width * 0.10, -1))
        self.m_spinCtrl13.SetSize((self.width * 0.10, -1))
        self.m_spinCtrl14.SetMinSize((self.width * 0.10, -1))
        self.m_spinCtrl13.SetMinSize((self.width * 0.10, -1))
        self.m_choice16.SetSize((self.width * 0.10, -1))
        self.m_choice16.SetMinSize((self.width * 0.10, -1))
        self.m_spinCtrl19.SetSize((self.width * 0.1, -1))
        self.m_spinCtrl18.SetSize((self.width * 0.1, -1))
        self.m_spinCtrl19.SetMinSize((self.width * 0.1, -1))
        self.m_spinCtrl18.SetMinSize((self.width * 0.1, -1))
        self.m_spinCtrl24.SetSize((self.width * 0.1, -1))
        self.m_spinCtrl24.SetMinSize((self.width * 0.1, -1))
        self.m_choice10.SetSize((self.width * 0.1, -1))

        self.m_choice11.SetSize((self.width * 0.1, -1))
        self.m_choice8.SetSize((self.width * 0.1, -1))
        self.m_choice9.SetSize((self.width * 0.1, -1))
        self.m_choice12.SetSize((self.width * 0.1, -1))
        self.m_choice13.SetSize((self.width * 0.1, -1))
        self.m_choice14.SetSize((self.width * 0.1, -1))
        self.m_choice15.SetSize((self.width * 0.1, -1))
        self.Fit()


class Sys(gui.Sys):
    '''
        Отваря просореца Система

    '''

    def __init__(self, parent):
        '''
            Конструктор
            Зарежда всички табчета за настройки на системата
        '''
        gui.Sys.__init__(self, parent)
        self.parent = parent
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.config_Sys['name'])
        self.USER = self.parent.USER
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.reboot = False

        page1 = SystemConf(self.m_notebook1)
        page2 = NetworkConf(self.m_notebook1)
        page3 = PrinterRFIDConf(self.m_notebook1)
        #         page4 = RFIDConf(self.m_notebook1)
        page4 = POS(self.m_notebook1)
        page5 = KeySystem(self.m_notebook1)
        page6 = DB(self.m_notebook1)
        page7 = SMIB(self.m_notebook1)
        page8 = Update(self.m_notebook1)

        self.m_notebook1.AddPage(page1, gui_lib.msg.config_Sys[1])
        self.m_notebook1.AddPage(page2, gui_lib.msg.config_Sys[2])
        self.m_notebook1.AddPage(page3, gui_lib.msg.config_Sys[3])
        self.m_notebook1.AddPage(page4, gui_lib.msg.config_Sys[4])
        self.m_notebook1.AddPage(page5, gui_lib.msg.config_Sys[5])

        self.m_notebook1.AddPage(page6, gui_lib.msg.config_Sys[6])
        self.m_notebook1.AddPage(page7, gui_lib.msg.config_Sys[7])
        self.m_notebook1.AddPage(page8, gui_lib.msg.config_Sys[8])
        self.on_resize(None)

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        if event != None:
            for i in self.m_notebook1.GetChildren():
                if (type(i) == SystemConf or
                        type(i) == PrinterRFIDConf or
                        type(i) == NetworkConf or
                        type(i) == POS or
                        type(i) == Update or
                        type(i) == KeySystem or
                        type(i) == DB or
                        type(i) == SMIB):
                    wx.PostEvent(i, event)
            if event == None:
                self.m_notebook1.Layout()
        self.m_toolBar1.SetMinSize((self.width, -1))
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height * 0.95))
        self.m_notebook1.SetMinSize((self.width, self.height))
        if event != None:
            event.Skip()
            self.Layout()

    def OnClose(self, event):
        '''
            Затваря прозореца
        '''
        # dial = wx.MessageDialog(self, *gui_lib.msg.UPDATE_SMIB_AFTER_REBOOT)
        # dial.ShowModal()
        if self.reboot is True:
            dlg = wx.MessageBox(gui_lib.msg.REBOOT_YES_NO, 'Info',
                                wx.YES_NO | wx.ICON_QUESTION)
            if dlg == wx.YES:
                self.reboot = False
                libs.conf.CONF.reload_conf()
                self.parent.OnConfig(None)
                self.Destroy()
                libs.restart_program(user_clean=True, user=self.USER)
            else:
                self.reboot = False
                libs.conf.CONF.reload_conf()
                self.parent.OnConfig(None)
                self.Destroy()
        else:
            # libs.conf.CONF.reload_conf()
            self.parent.OnConfig(None)
            self.Destroy()

    def OnPageClose(self, event):
        '''
            Не позволява да се затвори някой таб по погрешка
        '''
        pass


class AddBonusCart(gui.AddBonusCart, gui_lib.keybords.Keyboard):
    def __init__(self, parent, cart_id=None, edit_key=None):
        self.parent = parent
        self.edit_key = edit_key
        self.cart_id = cart_id
        gui.AddBonusCart.__init__(self, parent)
        self.SetTitle(gui_lib.msg.config_AddBonusCart['name'])
        self.m_staticText38.SetLabel(gui_lib.msg.config_AddBonusCart['m_staticText38'])
        self.m_checkBox52.SetLabel(gui_lib.msg.config_AddBonusCart['m_checkBox52'])
        self.m_staticText39.SetLabel(gui_lib.msg.config_AddBonusCart['m_staticText39'])
        self.m_staticText69.SetLabel(gui_lib.msg.config_AddBonusCart['m_staticText69'])
        self.m_radioBtn7.SetLabel(gui_lib.msg.config_AddBonusCart['m_radioBtn7'])
        self.m_radioBtn8.SetLabel(gui_lib.msg.config_AddBonusCart['m_radioBtn8'])
        self.m_staticText46.SetLabel(gui_lib.msg.config_AddBonusCart['m_staticText46'])
        self.m_staticText47.SetLabel(gui_lib.msg.config_AddBonusCart['m_staticText47'])
        self.m_button28.SetLabel(gui_lib.msg.config_AddBonusCart['m_button28'])
        self.m_button29.SetLabel(gui_lib.msg.config_AddBonusCart['m_button29'])

        self.m_checkBox52.SetToolTip(gui_lib.msg.config_AddBonusCart['m_checkBox52t'])

        self.m_radioBox1.SetString(0, gui_lib.msg.config_AddBonusCart['m_radioBox1'][0])
        self.m_radioBox1.SetString(1, gui_lib.msg.config_AddBonusCart['m_radioBox1'][1])
        self.m_radioBox1.SetString(2, gui_lib.msg.config_AddBonusCart['m_radioBox1'][2])
        self.m_radioBox1.SetString(3, gui_lib.msg.config_AddBonusCart['m_radioBox1'][3])
        self.m_radioBox1.SetString(4, gui_lib.msg.config_AddBonusCart['m_radioBox1'][4])
        self.m_radioBox1.SetString(5, gui_lib.msg.config_AddBonusCart['m_radioBox1'][5])
        self.m_radioBox1.SetString(6, gui_lib.msg.config_AddBonusCart['m_radioBox1'][6])

        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_textCtrl14.Bind(wx.EVT_LEFT_UP, self.OnKeyboard)
            self.m_spinCtrl12.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)
            self.m_spinCtrl26.Bind(wx.EVT_LEFT_UP, self.OnIntKeyboard)

        if self.edit_key != None:
            self.m_staticText47.SetLabel(self.edit_key.cart)
            self.cart_id = self.edit_key.cart
            self.m_textCtrl14.SetValue(self.edit_key.name)
            self.m_spinCtrl12.SetValue(self.edit_key.mony)
            self.m_spinCtrl26.SetValue(self.edit_key.no_bonus_out_befor)
            if self.edit_key.must_have_cust == None:
                self.m_checkBox52.SetValue(False)
            else:
                self.m_checkBox52.SetValue(self.edit_key.must_have_cust)
            if self.edit_key.active is False:
                self.m_radioBtn8.SetValue(True)
            if self.edit_key.cart_type == 'x2':
                self.m_radioBox1.SetSelection(4)
            elif self.edit_key.cart_type == 'x2_hold':
                self.m_radioBox1.SetSelection(5)
            elif self.edit_key.cart_type == 'static':
                self.m_radioBox1.SetSelection(0)
            elif self.edit_key.cart_type == 'static_hold':
                self.m_radioBox1.SetSelection(1)
            elif self.edit_key.cart_type == '1x1':
                self.m_radioBox1.SetSelection(2)
            elif self.edit_key.cart_type == '1x1_hold':
                self.m_radioBox1.SetSelection(3)
            elif self.edit_key.cart_type == 'restricted':
                self.m_radioBox1.SetSelection(6)
                self.m_spinCtrl26.Disable()
        else:
            self.m_staticText47.SetLabel(cart_id)
            self.cart_id = cart_id

    def OnRestricted(self, event):
        if self.m_radioBox1.GetSelection() == 6:
            self.m_spinCtrl26.Disable()
        else:
            self.m_spinCtrl26.Enable()

    def OnSave(self, event):
        #         obj = libs.DB.make_obj(libs.models.BonusCart)
        name = self.m_textCtrl14.GetValue()
        mony = self.m_spinCtrl12.GetValue()
        selection = self.m_radioBox1.GetSelection()
        cart_types = ['static', 'static_hold', '1x1', '1x1_hold', 'x2', 'x2_hold', 'restricted']
        selection = cart_types[selection]
        active = self.m_radioBtn7.GetValue()

        if self.edit_key == None:
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().USER.id
            err.info = 'NEW BONUS CART'
            libs.DB.add_object_to_session(err)
            obj = libs.DB.get_one_where(libs.models.BonusCart, name=name)
            if obj != None:
                dial = wx.MessageDialog(self, *gui_lib.msg.DB_HAVE_THIS_NAME)
                dial.ShowModal()
                return
            obj = libs.DB.make_obj(libs.models.BonusCart)
            obj.name = name
            obj.mony = mony
            obj.cart = self.cart_id
            obj.active = active
            obj.cart_type = selection
            obj.must_have_cust = self.m_checkBox52.GetValue()
            obj.no_bonus_out_befor = self.m_spinCtrl26.GetValue()
            libs.DB.add_object_to_session(obj)
        else:
            err = libs.DB.make_obj(libs.models.GetCounterError)
            err.user_id = self.parent.GetParent().USER.id
            err.info = 'CHANGE BONUS CART: name %s, mony %s, id %s, type %s, cust %s, block out %s' % (self.edit_key.name, self.edit_key.mony, self.edit_key.cart, self.edit_key.cart_type, self.edit_key.must_have_cust, self.edit_key.no_bonus_out_befor)
            libs.DB.add_object_to_session(err)
            self.edit_key.name = name
            self.edit_key.mony = mony
            self.edit_key.cart = self.cart_id
            self.edit_key.active = active
            self.edit_key.cart_type = selection
            self.edit_key.must_have_cust = self.m_checkBox52.GetValue()
            self.edit_key.no_bonus_out_befor = self.m_spinCtrl26.GetValue()
            libs.DB.add_object_to_session(self.edit_key)
        libs.DB.commit()
        self.OnClose(event)

    def OnClose(self, event):
        self.Destroy()


class BonusCartSave(gui.BonusCartSave):
    def __init__(self, parent):
        self.parent = parent
        gui.BonusCartSave.__init__(self, parent)
        self.SetTitle(gui_lib.msg.config_BonusCartSave['name'])
        self.m_button23.SetLabel(gui_lib.msg.config_BonusCartSave['m_button23'])
        self.width, self.height = wx.GetDisplaySize()
        self.cart = libs.DB.get_all_where(libs.models.BonusCart, active=True)
        self.all_mashin = libs.DB.get_all_where(libs.models.Device, enable=True, sas=True)
        # self.write_dict = {}
        self.SetSize((self.width * 0.45, -1))
        self.m_gauge1.SetMinSize((self.width * 0.45, -1))
        self.Fit()
        # for i in self.cart:
        #     self.write_dict[i.cart] = {'model':i.cart_type, 'mony': i.mony, 'no_bonus_out_befor':i.no_bonus_out_befor}
        # print self.write_dict[i.cart]
        self.m_gauge1.SetRange(len(self.all_mashin))
        self.loop = 0
        self.worker = task.BonusCartWork(self, self.cart, self.all_mashin, self.parent.GetParent().USER)
        task.EVT_BONUS_CART(self, self.GetCount)
        self.error = []

    def GetCount(self, event):
        try:
            if type(event.data) == int:
                self.loop = self.loop + event.data
                self.m_gauge1.SetValue(self.loop)
            else:
                dial = wx.MessageDialog(self, *gui_lib.msg.PROCES_FINISH)
                dial.ShowModal()
                self.error = event.data
        except NameError:
            pass

    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.worker:
            self.worker.abort()

    def OnClose(self, event):
        self.OnTaskStop(event)
        self.Destroy()


class ReadBonusCart(gui.ReadBonusCart):
    def __init__(self, parent):
        self.parent = parent
        gui.ReadBonusCart.__init__(self, parent)
        self.SetTitle(gui_lib.msg.config_ReadBonusCart['name'])
        self.m_button7.SetLabel(gui_lib.msg.config_ReadBonusCart['m_button7'])
        self.m_button8.SetLabel(gui_lib.msg.config_ReadBonusCart['m_button8'])
        self.m_staticText13.SetLabel(gui_lib.msg.config_ReadBonusCart[1])
        self.m_button8.Hide()
        self.cart_id = None
        if self.parent.login.with_rfid_in is True:
            self.parent.rfid_bind(self)
        else:
            self.worker = task.RFIDWork(self, timeout=libs.conf.RFID_TIMEOUT)  # @UndefinedVariable
            task.EVT_RFID_RESULT(self, self.OnCard)

    def OnCard(self, event):
        abort = False
        # print(e)vent.data
        if event.data == 'ERROR':
            dial = wx.MessageDialog(self, *gui_lib.msg.NO_RFID)
            dial.ShowModal()
            self.OnClose(event)
            # return
        elif event.data == None or event.data == False:
            abort = True
        # elif libs.DB.get_one_where(libs.models.User, cart=event.data) != None:
        #     abort = True
        if abort is True:
            pass

        else:
            if libs.DB.get_one_where(libs.models.BonusCart, cart=event.data) == None:
                self.cart_id = event.data
                self.m_staticText13.SetLabel(gui_lib.msg.config_ReadBonusCart[2])
                self.m_button8.Show()
                self.m_staticText13.SetForegroundColour(wx.Colour(0, 135, 11))
            else:
                self.m_staticText13.SetLabel(gui_lib.msg.config_ReadBonusCart[3])
        self.Fit()

    def OnTaskStop(self, event):
        """Stop Computation."""
        if self.parent.login.with_rfid_in is True:
            self.parent.rfid_unbind()
            return
        try:
            #         if self.worker:
            self.worker.abort()
        except AttributeError:
            pass

    def OnClose(self, event):
        self.cart_id = None
        #         if  self.parent_worker is False:
        # #         except AttributeError:
        #             self.OnTaskStop(event)
        #         else:
        self.OnTaskStop(event)
        # self.parent.rfid_task_start(event)
        self.Destroy()

    def OnSave(self, event):
        # if  self.parent_worker is False:
        #         except AttributeError:
        self.OnTaskStop(event)
        # else:
        #     self.OnTaskStop(event)
        #     self.parent.rfid_task_start(event)
        self.Destroy()


class BonusCart(gui.BonusCart):
    def __init__(self, parent):
        gui.BonusCart.__init__(self, parent)
        self.parent = parent
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.config_BonusCart['name'][0])
        self.m_listCtrl1.InsertColumn(0, gui_lib.msg.config_BonusCart[1])
        self.m_listCtrl1.InsertColumn(1, gui_lib.msg.config_BonusCart[2])
        self.m_listCtrl1.InsertColumn(2, gui_lib.msg.config_BonusCart[3])
        self.m_listCtrl1.InsertColumn(3, gui_lib.msg.config_BonusCart[4])
        self.m_listCtrl1.SetToolTip(gui_lib.msg.config_BonusCart[17])
        self._set_tools()
        self._add_tree()
        self.on_resize(None)

    def OnActive(self, event):
        gui.BonusCart.OnActive(self, event)

    def OnIinactive(self, event):
        gui.BonusCart.OnIinactive(self, event)

    def _set_tools(self):
        self.m_toolBar3.ClearTools()
        self.m_tool12 = self.m_toolBar3.AddTool(wx.ID_ANY, gui_lib.msg.config_BonusCart[5], wx.Bitmap(
            libs.conf.IMG_FOLDER + u"64x64/Gnome-Emblem-Documents-64.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                     wx.ITEM_NORMAL, gui_lib.msg.config_BonusCart[14], wx.EmptyString,
                                                     None)

        self.m_tool13 = self.m_toolBar3.AddTool(wx.ID_ANY, gui_lib.msg.config_BonusCart[6], wx.Bitmap(
            libs.conf.IMG_FOLDER + u"64x64/Gnome-Software-Update-Available-64.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                     wx.ITEM_NORMAL, gui_lib.msg.config_BonusCart[15], wx.EmptyString,
                                                     None)

        self.m_tool1 = self.m_toolBar3.AddTool(wx.ID_ANY, gui_lib.msg.config_BonusCart[7], wx.Bitmap(
            libs.conf.IMG_FOLDER + u"64x64/dialog-error.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                    gui_lib.msg.config_BonusCart[16], wx.EmptyString, None)

        self.Bind(wx.EVT_TOOL, self.OnSaveInSMIB, id=self.m_tool13.GetId())

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_TOOL, self.OnAdd, id=self.m_tool12.GetId())
        self.Bind(wx.EVT_TOOL, self.OnClose, id=self.m_tool1.GetId())
        self.m_toolBar3.Realize()

    def _add_tree(self):
        '''
           Създава трея като рефрешва елементите
           Ако се добави нова програма която да може да се свързва
           Опреснява елементите и я показва в прозореца.
           Държи всички елементи в текущо състояние
        '''
        self.tree = libs.DB.get_all(libs.models.BonusCart, order='id')

        self.treeDict = {}
        self.index = 0
        for i in self.tree:
            self.treeDict[self.index] = i
            self.m_listCtrl1.InsertItem(self.index, str(i.id))
            self.m_listCtrl1.SetItem(self.index, 1, i.name)
            self.m_listCtrl1.SetItem(self.index, 2, str(i.mony))
            if i.cart_type == 'static':
                self.m_listCtrl1.SetItem(self.index, 3, gui_lib.msg.config_BonusCart[8])
            elif i.cart_type == 'static_hold':
                self.m_listCtrl1.SetItem(self.index, 3, gui_lib.msg.config_BonusCart[9])
            elif i.cart_type == 'x2':
                self.m_listCtrl1.SetItem(self.index, 3, gui_lib.msg.config_BonusCart[10])
            elif i.cart_type == 'x2_hold':
                self.m_listCtrl1.SetItem(self.index, 3, gui_lib.msg.config_BonusCart[11])
            elif i.cart_type == '1x1':
                self.m_listCtrl1.SetItem(self.index, 3, gui_lib.msg.config_BonusCart[12])
            elif i.cart_type == '1x1_hold':
                self.m_listCtrl1.SetItem(self.index, 3, gui_lib.msg.config_BonusCart[13])
            elif i.cart_type == 'restricted':
                self.m_listCtrl1.SetItem(self.index, 3, gui_lib.msg.config_BonusCart[20])
            if i.active is True:
                self.m_listCtrl1.SetItemTextColour(item=self.index, col=wx.Colour(0, 135, 11))
            elif i.active is False:
                self.m_listCtrl1.SetItemTextColour(item=self.index, col=wx.Colour(199, 16, 29))
            self.index += 1

    def tree_refresh(self, tree=None):
        '''
            Премахва старите елементи от трея.
            И ги заменя с нови ( След промяна )
        '''
        self.m_listCtrl1.DeleteAllItems()
        self._add_tree()

    def on_resize(self, event):
        self.width, self.height = self.parent.GetSize()
        self.m_listCtrl1.SetMinSize((self.width * 0.95, self.height * 0.75))
        self.m_toolBar3.SetMinSize((self.width, -1))
        self.m_listCtrl1.SetColumnWidth(1, self.width * 0.40)
        self.m_listCtrl1.SetColumnWidth(2, self.width * 0.20)
        self.m_listCtrl1.SetColumnWidth(3, self.width * 0.40)
        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height * 0.95))
        if event != None:
            event.Skip()
            self.Layout()

    def OnClose(self, event):
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.config_BonusCart['name'][1])
        self.parent.OnConfig(None)
        self.Destroy()

    def OnEdit(self, event):
        dial = AddBonusCart(self, edit_key=self.treeDict[self.m_listCtrl1.GetFirstSelected()])
        dial.ShowModal()
        self.tree_refresh(self.treeDict)

    def OnAdd(self, event):
        if libs.conf.RFID_USE_WORK is False:
            dial = wx.MessageDialog(self, *gui_lib.msg.RFID_NOT_ENABLE)
            dial.ShowModal()
            return
        dial = ReadBonusCart(self.parent)
        dial.ShowModal()
        self.cart_id = dial.cart_id
        if self.cart_id != None:
            dial = AddBonusCart(self, cart_id=self.cart_id)
            dial.ShowModal()
        self.tree_refresh(self.treeDict)

    def OnSaveInSMIB(self, event):
        dial = BonusCartSave(self)
        dial.ShowModal()
        err = dial.error

        if err != [] and err != 'DONE':
            msg = ''
            for i in err:
                msg += str(i.nom_in_l) + ', '
            text = gui_lib.msg.config_BonusCart[18] + u': \n' + msg
            dlg = wx.MessageDialog(self, text, gui_lib.msg.config_BonusCart[19], wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()


class Abaut(gui.Abaut):
    def __init__(self, parent):
        gui.Abaut.__init__(self, parent)
        self.m_staticText55.SetLabel(libs.conf.VERSION)
        self.m_staticText57.SetLabel(libs.DB.get_one(libs.models.Alembic).version_num)
        version = libs.udp.send(evt='get_rev', ip=libs.conf.SERVER)
        if version == None:
            version = [None, None]
        if version[1] == 0:
            version[1] = u'update'
        self.m_staticText59.SetLabel(u'V_%s, rev_%s' % (version[0], version[1]))
        self.SetTitle(gui_lib.msg.config_Abaut['name'])
        self.m_staticText54.SetLabel(gui_lib.msg.config_Abaut['m_staticText54'])
        self.m_button52.SetLabel(gui_lib.msg.config_Abaut['m_button52'])
        self.m_staticText56.SetLabel(gui_lib.msg.config_Abaut['m_staticText56'])
        self.m_staticText58.SetLabel(gui_lib.msg.config_Abaut['m_staticText58'])
        self.m_staticText60.SetLabel(gui_lib.msg.config_Abaut['m_staticText60'])
        self.m_staticText62.SetLabel(gui_lib.msg.config_Abaut['m_staticText62'])
        self.m_button38.SetLabel(gui_lib.msg.config_Abaut['m_button38'])
        self.m_staticText73.SetLabel(gui_lib.msg.config_Abaut['m_staticText73'])
        self.m_staticText74.SetLabel(libs.conf.REV)

    def ChangeLog(self, event):
        if libs.conf.DOCS_DEBUG is False:
            frame = libs.helps.Help(
                r'%s%s/colibri/v%s/new.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE, libs.conf.VERSION))
        else:
            frame = libs.helps.Help(
                r'http://127.0.0.1:5000/%s/colibri/v%s/new.html' % (libs.conf.USE_LANGUAGE, libs.conf.VERSION))

    def OnClose(self, event):
        self.Destroy()


class MainConf(gui.ConfPanel):  # @UndefinedVariable
    '''
        Основен панел на конфигурацията
    '''

    def __init__(self, parent):
        '''
            Конструктур
            Изгражда всички елементи
        '''
        gui.ConfPanel.__init__(self, parent)  # @UndefinedVariable
        self.parent = parent
        self.parent.help_name = 'config.html'
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.config_MainConf['name'][0])
        self.resize = True
        self.width, self.height = self.parent.GetSize()
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.USER = self.parent.USER
        self._set_right()
        self.on_resize(None)

    #         self.SetSize((self.width, self.height*0.90))

    def on_resize(self, event):
        width, height = self.parent.GetSize()
        if self.width != width or self.height != height:
            self.resize = True

    def OnIdle(self, event):
        if not self.resize:
            return
        self.resize = False
        self.width, self.height = self.parent.GetSize()
        if event != None:
            for sizerItem in self.GetChildren():
                if (type(sizerItem) == users.main.UserConf or
                        type(sizerItem) == mashin.main.Mashin or
                        # type(sizerItem) == licenz.main.Licenz or
                        type(sizerItem) == Sys or
                        type(sizerItem) == BonusCart):
                    wx.PostEvent(sizerItem, event)

        #             self.m_notebook1.Layout()
        self.m_toolBar1.SetMinSize((self.width, -1))

        if os.name == 'posix':
            self.SetSize((self.width, self.height))
        else:
            self.SetSize((self.width, self.height * 0.95))
        #         self.m_notebook1.SetMinSize((self.width, self.height))
        if event != None:
            event.Skip()
            self.Layout()

    #             self.Center()
    #         if libs.conf.FULSCREEAN is True:
    #             self.SetWindowStyle(wx.STAY_ON_TOP)

    def _set_right(self):
        '''
            Създава менщто с опциите
            Определя правата за достъп
            Ако текущия потребител няма права бутона в менюто изчезва
        '''
        self.m_toolBar1.ClearTools()
        if self.USER.grup.right != None:
            right = self.parent.USER.grup.from_json()
            if 1 in right['config']:
                self.m_tool1 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool1,
                                                            wx.Bitmap(libs.conf.IMG_FOLDER + u"64x64/kopete.png",
                                                                      wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.config_MainConf[1], wx.EmptyString,
                                                            None)
                self.Bind(wx.EVT_TOOL, self.OnUser, id=self.m_tool1.GetId())
            if 2 in right['config']:
                self.m_tool2 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool2,
                                                            wx.Bitmap(
                                                                libs.conf.IMG_FOLDER + u"64x64/network-server.png",
                                                                wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.config_MainConf[2], wx.EmptyString,
                                                            None)
                self.Bind(wx.EVT_TOOL, self.OnMashin, id=self.m_tool2.GetId())

            if 7 in right['config']:
                self.m_tool10 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool10,
                                                             wx.Bitmap(
                                                                 libs.conf.IMG_FOLDER + u"64x64/Gnome-Contact-New-64.png",
                                                                 wx.BITMAP_TYPE_ANY),
                                                             wx.NullBitmap, wx.ITEM_NORMAL,
                                                             gui_lib.msg.config_MainConf[3], wx.EmptyString,
                                                             None)
                self.Bind(wx.EVT_TOOL, self.OnTalon, id=self.m_tool10.GetId())

            if 5 in right['config']:
                self.m_tool16 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool16, wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/Gnome-Security-High-64.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                             wx.ITEM_NORMAL, gui_lib.msg.config_MainConf[4],
                                                             wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.JPConf, id=self.m_tool16.GetId())

            if 6 in right['config']:
                self.m_tool22 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool22, wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/Gnome-Applications-Utilities-64.png", wx.BITMAP_TYPE_ANY),
                                                             wx.NullBitmap,
                                                             wx.ITEM_NORMAL, gui_lib.msg.config_MainConf[5],
                                                             wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnSystemConf, id=self.m_tool22.GetId())

            if 3 in right['config']:
                self.m_tool4 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool4, wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/Gnome-Application-Certificate-64.png", wx.BITMAP_TYPE_ANY),
                                                            wx.NullBitmap, wx.ITEM_NORMAL,
                                                            gui_lib.msg.config_MainConf[6], wx.EmptyString,
                                                            None)
                self.Bind(wx.EVT_TOOL, self.OnLicenz, id=self.m_tool4.GetId())

            if 4 in right['config']:
                self.m_tool7 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool7, wx.Bitmap(
                    libs.conf.IMG_FOLDER + u"64x64/Gnome-Undelete-64.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                            wx.ITEM_NORMAL, gui_lib.msg.config_MainConf[7],
                                                            wx.EmptyString, None)
                self.Bind(wx.EVT_TOOL, self.OnReboot, id=self.m_tool7.GetId())

        self.m_tool5 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool5, wx.Bitmap(
            libs.conf.IMG_FOLDER + u"64x64/Gnome-Help-Browser-64.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, gui_lib.msg.config_MainConf[8], wx.EmptyString,
                                                    None)
        self.Bind(wx.EVT_TOOL, self.OnHelp, id=self.m_tool5.GetId())

        self.m_tool6 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool6, wx.Bitmap(
            libs.conf.IMG_FOLDER + u"64x64/preferences-desktop-notification.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, gui_lib.msg.config_MainConf[9], wx.EmptyString,
                                                    None)
        self.Bind(wx.EVT_TOOL, self.OnInfo, id=self.m_tool6.GetId())

        self.m_tool3 = self.m_toolBar1.AddTool(wx.ID_ANY, gui_lib.msg.conf_m_tool3, wx.Bitmap(
            libs.conf.IMG_FOLDER + u"64x64/dialog-error.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                    gui_lib.msg.config_MainConf[10], wx.EmptyString, None)
        self.Bind(wx.EVT_TOOL, self.OnInfo, id=self.m_tool6.GetId())

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_TOOL, self.OnClose, id=self.m_tool3.GetId())
        self.m_toolBar1.Realize()

    def OnReboot(self, event):
        '''
            Рестартира програмата
        '''
        self.parent.OnClose(event)
        libs.restart_program()

    #         sys.exit()

    def OnUser(self, event):
        '''
            Отваря панела за настройки на потребители и групи
        '''
        self.Hide()
        panel = users.main.UserConf(self.parent)
        panel.Show()
        #         if libs.conf.FULSCREEAN is True:
        #             panel.ShowFullScreen(True,  style=wx.FULLSCREEN_NOCAPTION)
        #         else:
        #             panel.ShowModal()
        self.parent.login_user_refresh()

    def OnMashin(self, event):
        '''
            Отваря панела за настройки на машините
        '''
        self.Hide()
        panel = mashin.main.Mashin(self.parent)
        panel.Show()
        #         if libs.conf.FULSCREEAN is True:
        #             panel.ShowFullScreen(True,  style=wx.FULLSCREEN_NOCAPTION)
        #         else:
        #             panel.ShowModal()
        #         self.parent.chk_mashin_worker.all_mashin = None
        self.parent.all_mashin_refresh()

    def OnLicenz(self, event):
        '''
            Отваря панела за добавяне или удължаване на лиценз
        '''
        self.Hide()
        panel = licenz.main.Licenz(self.parent)
        panel.Show()

    def OnSystemConf(self, event):
        '''
            Отваря панела за настройки на програмата и кей системата
        '''
        self.Hide()
        panel = Sys(self.parent)
        panel.Show()

    def OnClose(self, event):
        '''
            Затваря прозореца
        '''
        self.parent.help_name = 'main.html'
        # self.parent.on_resize(event)
        self.parent.show_panel()
        self.parent.SetTitle(libs.conf.CASINO_NAME + ': ' + gui_lib.msg.config_MainConf['name'][1])

        self.Destroy()

    def OnTalon(self, event):
        self.Hide()
        dialog = BonusCart(self.parent)
        dialog.Show()

    def OnHelp(self, event):
        if libs.conf.DOCS_DEBUG is False:
            frame = libs.helps.Help(r'%s%s/index.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE))
        else:
            frame = libs.helps.Help('http://127.0.0.1:5000/%s/index.html' % (libs.conf.USE_LANGUAGE))

    def OnInfo(self, event):
        dial = Abaut(self)
        dial.ShowModal()

    def JPConf(self, event):
        dial = jpmain.JPMain(self)
        dial.ShowModal()


class NRA(gui.NRA):
    def __init__(self, parent):
        gui.NRA.__init__(self, parent)
        self.SetTitle(gui_lib.msg.conf_NRA['name'])
        self.m_staticText82.SetLabel(gui_lib.msg.conf_NRA['m_staticText82'])
        self.m_staticText83.SetLabel(gui_lib.msg.conf_NRA['m_staticText83'])
        self.m_staticText84.SetLabel(gui_lib.msg.conf_NRA['m_staticText84'])
        self.m_button59.SetLabel(gui_lib.msg.conf_NRA['m_button59'])
        self.m_button60.SetLabel(gui_lib.msg.conf_NRA['m_button60'])
        self.m_textCtrl27.SetValue(libs.DB.get_one_where(libs.models.Config, name='nra_client_id').value)
        self.m_textCtrl28.SetValue(libs.DB.get_one_where(libs.models.Config, name='nra_token').value)
        date = libs.DB.get_one_where(libs.models.Config, name='nra_token_valid')
        if date:
            try:
                self.m_calendar3.SetDate(libs.models.TZ.str_to_date(date.value, '%Y-%m-%d'))
            except:
                pass

    def OnClose( self, event ):
        self.Destroy()

    def OnGo( self, event ):
        client_id = self.m_textCtrl27.GetValue()
        token = self.m_textCtrl28.GetValue()
        dates = self.m_calendar3.GetDate()
        dates = dates.Format('%Y-%m-%d')

        db_client_id = libs.DB.get_one_where(libs.models.Config, name='nra_client_id')
        db_token = libs.DB.get_one_where(libs.models.Config, name='nra_token')
        valid_to = libs.DB.get_one_where(libs.models.Config, name='nra_token_valid')

        db_client_id.value = client_id
        db_token.value = token
        valid_to.value = dates

        libs.DB.add_object_to_session(db_token)
        libs.DB.add_object_to_session(db_client_id)
        libs.DB.add_object_to_session(valid_to)

        libs.DB.commit()
        self.OnClose(event)
