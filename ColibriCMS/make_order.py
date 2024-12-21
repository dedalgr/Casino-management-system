# -*- coding:utf-8 -*-
'''
Created on 2.10.2017 г.

@author: dedal
'''
import wx
import gui
import gui_lib  # @UnresolvedImport
import libs  # @UnresolvedImport
from libs import models
import datetime
import json
import threading
import os


def send_mail(data, to_mail, subject):
    try:
        #             data = self.data_format()

        html = gui_lib.printer.render('day_report.html', data)
        send_to = to_mail
        mail_to_send = send_to.split(',')
        for i in mail_to_send:
            libs.sendmail.Gmail(html, i, subject)
    #             dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_OK)
    #             dlg.ShowModal()
    except Exception as e:
        #             dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_NOT_OK)
        #             dlg.ShowModal()
        print(e)
        libs.log.stderr_logger.critical(e, exc_info=True)

def reset_player(device, end_date):
    libs.udp.send('unblock_user', ip=libs.conf.SERVER)
    libs.udp.send('del_all_lk', ip=libs.conf.SERVER)
    # for item in device:
    libs.udp.send('day_order_reset_player', ip=libs.conf.SERVER, end_date=end_date)

class MakeOrder(gui.MakeOrder, gui_lib.keybords.Keyboard):

    def __init__(self, parent, object_info):
        self.parent = parent
        self.user = self.parent.GetParent().USER
        # reload(libs)
        # wx.Locale()
        gui.MakeOrder.__init__(self, self.parent)
        self.SetTitle(gui_lib.msg.make_order_Name)
        self.m_radioBtn2.SetLabel(gui_lib.msg.make_order_button['radioBtn2'])
        self.m_radioBtn1.SetLabel(gui_lib.msg.make_order_button['radioBtn1'])
        self.m_button5.SetLabel(gui_lib.msg.make_order_button['button5'])
        self.m_button6.SetLabel(gui_lib.msg.make_order_button['button6'])
        self.m_checkBox2.SetLabel(gui_lib.msg.make_order_button['checkBox2'])
        self.m_checkBox2.SetToolTip(gui_lib.msg.make_order_tooltip['checkBox2'])
        if libs.conf.POS_PRINTER_USE is True and libs.DB.get_one_where(
                libs.models.Config, name='print_cust_rko').value == 'True':
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
                mony = []
                egn = '.' * 45
                cust_name = '.' * 45
                user_id = str(self.user.id)
                dates = libs.models.TZ.date_to_str(formats='%d.%m.%Y')
                id = libs.DB.get_one(libs.models.CashOutPrinted, order='id', descs=True)
                if id == None:
                    self.ID = 1
                else:
                    self.ID = id.id + 1

                cust_sity = '.' * 45
                cust_adress = '.' * 45
                self.rko_data = {'company': company, 'EIK': EIK, 'objects': objects, 'sity': sity,
                                 'objects_adress': objects_adress,
                                 'name': cust_name, 'egn': egn, 'mony': mony, 'user_id': user_id, 'ID': [],
                                 'dates': dates,
                                 'cust_sity': cust_sity,
                                 'cust_adress': cust_adress}
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                self.rko_data = None
        else:
            object_info = json.loads(object_info.value)
            self.rko_data = None
        # self.sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, gui_lib.msg.make_order_text['sbSizer1'] ), wx.VERTICAL )
        # self.sbSizer1.SetLabel(gui_lib.msg.make_order_text['sbSizer1'])
        if libs.conf.USE_VIRTUAL_KEYBORD is True:
            self.m_spinCtrl6.Bind( wx.EVT_LEFT_UP, self.OnIntKeyboard )
            self.m_textCtrl10.Bind( wx.EVT_LEFT_UP, self.OnKeyboard )
            self.m_textCtrl11.Bind( wx.EVT_LEFT_UP, self.OnKeyboard )
        #             self.m_spinCtrl5.Bind( wx.EVT_LEFT_UP, self.OnIntKeyboard )
        #             self.m_spinCtrl6.Bind( wx.EVT_LEFT_UP, self.OnIntKeyboard )
        #             self.m_textCtrl4.Bind( wx.EVT_LEFT_UP, self.OnIntKeyboard )
        #             self.m_textCtrl5.Bind( wx.EVT_LEFT_UP, self.OnIntKeyboard )
        self.object = object_info
        self.USER_NAME_ON_DAY_ORDER = libs.DB.get_one_where(libs.models.Config, name='user_name_on_day_report')
        if self.USER_NAME_ON_DAY_ORDER == None:
            obj = libs.DB.make_obj(libs.models.Config)
            obj.name = 'user_name_on_day_report'
            obj.value = 'False'
            libs.DB.add_object_to_session(obj)
            libs.DB.commit()
            self.USER_NAME_ON_DAY_ORDER = 'False'
        else:
            self.USER_NAME_ON_DAY_ORDER = self.USER_NAME_ON_DAY_ORDER.value
        self.m_radioBtn2.Hide()
        self.m_spinCtrl6.Disable()
        self.edit_el_count = False
        right = self.user.grup.from_json()
        # self.m_checkBox2.Hide()
        if 21 in right['main']:
            self.m_radioBtn2.Show()
            self.m_spinCtrl6.Enable()
        if 1 in right['diff']:
            self.edit_el_count = True
            self.m_checkBox2.Show()
            self.m_textCtrl10.Show()
            self.m_textCtrl11.Show()
            # else:
            #     self.m_checkBox2.Hide()
            # else:
            #     self.m_checkBox2.Hide()

        # for i in self.right:
        #     if i.right.option == '27 month order':
        #
        #     if i.right.option == '10 edit el count':
        #         self.edit_el_count = True
        #         self.m_checkBox2.Show()
        #         self.m_datePicker1.Show()
        #         self.m_datePicker2.Show()
        self.OnDoc(None)

    #         self.mashin = libs.DB.get_all_where(libs.models.Device, enable=True, order='nom_in_l')
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

    def chk_for_order(self):
        ord_have = None
        ord_have = libs.DB.get_one_where(libs.models.Order, chk=False)
        # ord_have1 = libs.DB.get_one_where(libs.models.Prihod, chk=False)
        # ord_have2 = libs.DB.get_one_where(libs.models.Razhod, chk=False)
        if ord_have != None:  # or ord_have1 != None or ord_have2 != None :
            dial = wx.MessageDialog(self, *gui_lib.msg.NOT_ALL_ORDER_IS_FINISH)
            dial.ShowModal()
            return None

        if ord_have != None:
            return False
        else:
            return True

    def OnClose(self, event):
        self.Destroy()

    def OnDoc(self, event):
        choises = self.m_radioBtn1.GetValue()
        # if choises is True:
        #     self.m_checkBox2.Hide()
        #     self.m_datePicker1.Hide()
        #     self.m_datePicker2.Hide()
        # else:
        #     if self.edit_el_count is True:
        #         self.m_checkBox2.Show()
        #         self.m_datePicker1.Show()
        #         self.m_datePicker2.Show()
        #     else:
        #         self.m_checkBox2.Hide()
        #         self.m_datePicker1.Hide()
        #         self.m_datePicker2.Hide()
        my_time = datetime.datetime.now()
        if my_time.month == 1 and my_time.day == 2 and choises is True:
            self.m_spinCtrl6.SetValue(1)
            self.data = libs.DB.get_one_where(libs.models.DayReport, day_report=choises, descs=True, order='id')
        elif my_time.month == 2 and my_time.day == 1 and choises is False:
            self.m_spinCtrl6.SetValue(1)
            self.data = libs.DB.get_one_where(libs.models.DayReport, day_report=choises, descs=True, order='id')
        else:
            self.data = libs.DB.get_one_where(libs.models.DayReport, day_report=choises, descs=True, order='id')
            if self.data == None:
                self.m_spinCtrl6.SetValue(1)
            else:
                self.m_spinCtrl6.SetValue(self.data.doc_nom + 1)
        self.Fit()

    def print_rko(self, data):
        # commit = False
        if self.rko_data != None and self.m_radioBtn1.GetValue() is True:
            self.rko_data['count'] = 0
            for i in data['row']:
                tmp = float(data['row'][i]['total'])
                if tmp < 0 and tmp > -1783:
                    self.rko_data['mony'].append("{:.2f}".format(tmp * -1))
                else:
                    order = 1783
                    tmp = tmp * -1
                    count = 0
                    if tmp % 1783 != 0:
                        count = 1
                    count += int(tmp // 1783)
                    for b in range(count):
                        self.rko_data['mony'].append("{:.2f}".format(order))
                        tmp -= 1783
                        if tmp <= 0:
                            break
                        elif tmp <= 1783:
                            self.rko_data['mony'].append("{:.2f}".format(tmp))
                            break

                    for c in range(len(self.rko_data['mony'])):
                        self.ID += 1
                        my_id = ('0' * (9 - len(str(self.ID)))) + str(self.ID)
                        self.rko_data['ID'].append(my_id)
                        obj = libs.DB.make_obj(libs.models.CashOutPrinted)
                        obj.pub_user_id = self.user.id
                        obj.mony = float(self.rko_data['mony'][c])
                        libs.DB.add_object_to_session(obj)
                        # libs.DB.flush()

            self.rko_data['count'] = len(self.rko_data['mony'])
            if self.rko_data['count'] > 0:
                # libs.DB.commit()
                self.PrintRKO(self.rko_data)

    def OnGo(self, event):

        if self.m_radioBtn1.GetValue() is True:
            if self.chk_for_order() is True:
                pub_time = libs.models.TZ.date_to_str(libs.models.TZ.now(), '%Y-%m-%d')
                chk_for_report = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
                                                       pub_time__btw=(pub_time + ' 00:00:00', pub_time + ' 23:59:59'))
                if chk_for_report != None:
                    dial = wx.MessageDialog(self, *gui_lib.msg.HAVE_DAY_REPORT)
                    dial.ShowModal()
                    return
            else:
                return
        else:
            # if self.m_checkBox2.GetValue() is True:
            pub_time = libs.models.TZ.date_to_str(libs.models.TZ.now(), '%Y-%m-%d')
            chk_for_report = libs.DB.get_one_where(libs.models.DayReport, day_report=True,
                                                   pub_time__btw=(pub_time + ' 00:00:00', pub_time + ' 23:59:59'))
            if chk_for_report == None:
                dial = wx.MessageDialog(self, *gui_lib.msg.NO_DAY_REPORT)
                dial.ShowModal()
                return
        data = {}
        data['nom'] = self.m_spinCtrl6.GetValue()
        if self.data == None:
            start_date = '2001-01-01 00:00:00'
        else:
            start_date = self.data.pub_time
            start_date = libs.models.TZ.date_to_str(start_date, '%Y-%m-%d %H:%M:%S')
        if self.m_radioBtn2.GetValue() is True and self.m_checkBox2.GetValue() is True:
            my_old_date = self.m_textCtrl10.GetValue()
            my_old_date = libs.models.TZ.str_to_date(my_old_date, formats='%d.%m.%Y')
            my_old_date = libs.models.TZ.date_to_str(my_old_date, '%Y-%m-%d')
            start_date = libs.DB.get_one_where(libs.models.DayReport, day_report=True, pub_time__btw=(my_old_date + ' 00:00:00', my_old_date + ' 23:59:59'))
            start_date = my_old_date + ' ' + libs.models.TZ.date_to_str(start_date.pub_time, '%H:%M:%S')
            # my_old_date = '%s-%s-%s' % (my_old_date.GetYear(), my_old_date.GetMonth() + 1, my_old_date.GetDay())
            self.data = libs.DB.get_one_where(libs.models.DayReport, day_report=True, descs=True, order='id')
            my_new_date = self.m_textCtrl11.GetValue()
            my_new_date = libs.models.TZ.str_to_date(my_new_date, formats='%d.%m.%Y')
            my_new_date = libs.models.TZ.date_to_str(my_new_date, '%Y-%m-%d')
            end_date = my_new_date + ' ' + libs.models.TZ.date_to_str(self.data.pub_time, '%H:%M:%S')
        else:
            my_old_date = None
            my_new_date = None
        if self.m_checkBox2.GetValue() is False:
            end_date = libs.models.TZ.now()
            end_date = libs.models.TZ.date_to_str(end_date, '%Y-%m-%d %H:%M:%S')


        #         end_time = str(self.m_spinCtrl4.GetValue()) + ':' + str(self.m_spinCtrl5.GetValue())
        if my_new_date != None and my_old_date != None:
            end_date = my_new_date + end_date[10:]
            start_date = my_old_date + start_date[10:]
        if self.m_radioBtn1.GetValue() is True:
            data['doc_tupe'] = gui_lib.msg.make_order_text[1]
        else:
            data['doc_tupe'] = gui_lib.msg.make_order_text[2]
        # if self.m_checkBox2.GetValue() is False:
        new_doc_date = libs.models.TZ.str_to_date(end_date, '%Y-%m-%d %H:%M:%S')
        # else:
        #     new_doc_date = libs.models.TZ.str_to_date(end_date, '%Y-%m-%d')
        doc_date = new_doc_date - datetime.timedelta(1)
        data['doc_date'] = libs.models.TZ.date_to_str(doc_date, '%d-%m-%Y')
        if self.m_radioBtn1.GetValue() is False and libs.conf.NEW_ORDER is True:
            data['doc_year'] = data['doc_date'][6:]
            data['for_mounth'] = gui_lib.msg.mounths[data['doc_date'][3:5]]
        #         data['doc_date'] = doc_date
        data['row'] = {}
        data['total'] = 0
        data['total_in'] = 0
        data['total_out'] = 0
        data['len_row'] = 0
        data['doc_type'] = self.m_radioBtn1.GetValue()
        data['casino_info'] = self.object
        if self.USER_NAME_ON_DAY_ORDER == 'True' and self.m_radioBtn1.GetValue() is True:
            data['user_name'] = self.user.name
        if 'manager' in data['casino_info']:
            data['manager'] = data['casino_info']['manager']

        row = libs.DB.get_all_where(libs.models.Order, pub_time__btw=(start_date, end_date))
        if self.m_radioBtn1.GetValue() is True:
            all_ip = []
            for i in row:
                if i.mashin.enable is True and i.mashin.sas is True:
                    if i.mashin.ip not in all_ip:
                        reset_end_date = libs.models.TZ.date_to_str(i.pub_time, '%Y-%m-%d %H:%M:%S')
                        all_ip.append(i.mashin.ip)
            b = threading.Thread(target=reset_player, args=(all_ip, new_doc_date))
            b.start()
        my_old_dev = []

        for item in row:
            if item.mashin.enable is False:
                if int(item.mashin.nom_in_l) not in my_old_dev:
                    my_old_dev.append(item.mashin.nom_in_l)
                    item.mashin.nom_in_l += 0.1
        for item in row:
            # reset_end_date = libs.models.TZ.date_to_str(item.pub_time, '%Y-%m-%d %H:%M:%S')
            if item.mashin.nom_in_l not in data['row']:
                # if item.mashin.enable is False:
                #     item.mashin.nom_in_l += 0.1
                tmp = {}
                tmp['model'] = item.mashin.model.name
                tmp['serial'] = item.mashin.serial
                last_order = libs.DB.get_one_where(libs.models.Order, pub_time__btw=(start_date, end_date),
                                                   mashin_id=item.mashin.id, order='id', descs=True)
                #                         last_order.in_doc_from_date = data['doc_date']
                #                         libs.DB.add_object_to_session(last_order)
                if last_order == None:
                    tmp['new_el_in'] = item.mashin.el_in
                    tmp['new_el_out'] = item.mashin.el_out
                    tmp['new_mex_in'] = item.mashin.mex_in
                    tmp['new_mex_out'] = item.mashin.mex_out
                else:
                    tmp['new_el_in'] = last_order.new_enter
                    tmp['new_el_out'] = last_order.new_exit
                    tmp['new_mex_in'] = last_order.mex_new_enter
                    tmp['new_mex_out'] = last_order.mex_new_exit

                tmp['total_in'] = item.new_enter - item.old_enter
                tmp['total_out'] = item.new_exit - item.old_exit
                tmp['total'] = tmp['total_in'] - tmp['total_out']
                tmp['coef'] = item.mashin.el_coef
                data['row'][item.mashin.nom_in_l] = tmp
            else:
                data['row'][item.mashin.nom_in_l]['total_in'] = data['row'][item.mashin.nom_in_l]['total_in'] + (
                            item.new_enter - item.old_enter)
                data['row'][item.mashin.nom_in_l]['total_out'] = data['row'][item.mashin.nom_in_l]['total_out'] + (
                            item.new_exit - item.old_exit)
                data['row'][item.mashin.nom_in_l]['total'] = data['row'][item.mashin.nom_in_l]['total'] + (
                            (item.new_enter - item.old_enter) - (item.new_exit - item.old_exit))

        data['sum_all_total'] = 0
        for item in data['row']:
            data['total_in'] += data['row'][item]['total_in'] * data['row'][item]['coef']
            data['total_out'] += data['row'][item]['total_out'] * data['row'][item]['coef']
            data['row'][item]['total_in'] = "{:.2f}".format(data['row'][item]['total_in'] * data['row'][item]['coef'])
            data['row'][item]['total_out'] = "{:.2f}".format(data['row'][item]['total_out'] * data['row'][item]['coef'])
            data['sum_all_total'] = data['sum_all_total'] + (data['row'][item]['total'] * data['row'][item]['coef'])

            data['row'][item]['total'] = "{:.2f}".format(data['row'][item]['total'] * data['row'][item]['coef'])

        data['sum_all_total'] = "{:.2f}".format(data['sum_all_total'])
        data['total_in'] = "{:.2f}".format(data['total_in'])
        data['total_out'] = "{:.2f}".format(data['total_out'])
        data['new_order'] = libs.conf.NEW_ORDER
        if self.m_radioBtn1.GetValue() is True:
            db_ram_clear = libs.DB.get_all_where(libs.models.RamClear, pub_time__btw=(start_date, end_date), chk=False)
            ram_clear = {}
            for i in db_ram_clear:
                ram_clear[i.mashin.serial] = {'serial': i.mashin.serial, 'el_in': i.el_in, 'el_out': i.el_out,
                                              'mex_in': i.mex_in, 'mex_out': i.mex_out}
                i.chk = True
                libs.DB.add_object_to_session(i)
                # libs.DB.flush()

            if ram_clear != {}:
                data['ram_clear'] = ram_clear
                data['ram_clear_time'] = libs.models.TZ.date_to_str(db_ram_clear[0].pub_time, '%d.%m.%Y %H:%M')
            else:
                data['ram_cleat_time'] = ''
                data['ram_clear_count'] = [1]
        day_report = libs.DB.make_obj(libs.models.DayReport)
        day_report.user_id = self.user.id
        day_report.doc_data = json.dumps(data)
        day_report.day_report = self.m_radioBtn1.GetValue()
        day_report.doc_nom = int(self.m_spinCtrl6.GetValue())
        libs.DB.add_object_to_session(day_report)
        # libs.DB.flush()
        if self.m_radioBtn1.GetValue() is True:
            obj = libs.DB.get_all_where(libs.models.BonusPay, last=True)
            for i in obj:
                i.last = False
                if i.pub_time == 2010:
                    i.pub_time = libs.models.TZ.now()
                if i.activ is True:
                    i.activ = False
                    i.use_it = False
                libs.DB.add_object_to_session(i)
        try:
            libs.DB.commit()

            if self.user.grup.auto_mail is True:
                t = threading.Thread(target=send_mail, args=(data, self.user.grup.boss_mail, self.user.grup.subject))
                t.start()
            if libs.conf.PRINT_DIRECT is True:
                ranges = 2
            else:
                ranges = 1
            self.print_rko(data)
            try:
                gui_lib.printer.Print(self, 'day_report.html', data, ranges=ranges)
            except:
                dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_NOT_OK)
                dlg.ShowModal()

            if libs.conf.PRINT_DIRECT is True:
                dlg = wx.MessageDialog(self, *gui_lib.msg.PRINT_OK)
                dlg.ShowModal()
            self.Destroy()
        except Exception as e:
            print(e)
            libs.DB.rollback()
            libs.log.stderr_logger.critical(e, exc_info=True)
            dlg = wx.MessageDialog(self, *gui_lib.msg.DB_WRITE_ERROR)
            dlg.ShowModal()





