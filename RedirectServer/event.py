# -*- coding:utf-8 -*-
'''
Created on 12.03.2019

@author: dedal
'''

import models
import datetime
import os
import pickle
import conf
import json
import multiprocessing
import libs
import time
import client
import log
import cups
import binascii
from sqlalchemy.exc import InvalidRequestError
# import ban_proc
# from email.mime.text import MIMEText
import threading
# import chk_proc



# bonus_is_open = {}

def real_time_look_get(mem_db=None, log=None, **kwargs):
    while True:
        real_time_look_get_data = mem_db.get('real_time_look_get_data')
        for i in list(real_time_look_get_data.keys()):
            try:
                time.sleep(0.1)
                var = client.send(evt='chk_alife', ip=i, port=5025, timeout=4, log=log)
                if var:
                    tmp = client.send('real_time_look', ip=i, port=5025, log=log, timeout=conf.TIMEOUT_2-4)
                    if tmp == {}:
                        tmp = None
                else:
                    tmp = None
            except Exception as e:
                tmp = None
                log.debug(e, exc_info=True)
            mem_db.set(i, tmp)

class Evant(multiprocessing.Process):
    def __init__(self, pipe=[], mem_db=None):
        self.log = log.get_log()
        self.get_mony = {}
        self.db = models.DBCtrl(my_session=True)
        self.lk_check = self.db.get_one_where(models.Config, name='lk_check')
        if self.lk_check is None:
            self.lk_check = []
            obj = self.db.make_obj(models.Config)
            obj.name = 'lk_check'
            obj.value = json.dumps([])
            self.db.add_object_to_session(obj)
            self.db.commit()
        else:
            self.lk_check = json.loads(self.lk_check.value)
        # self.q = q
        # self.q2 = q2
        self.in_nra_cheked = {}
        self.pipe = pipe
        self.card_is_in = {}
        self.bonus_init_time = {}
        self.client_bonus_init_time = {}
        self.my_init_time = {}
        self.client_hold_bonus = {}
        self.mem_db = mem_db
        multiprocessing.Process.__init__(self, name='EVENT')
        self.block_user = []
        self.uuid = libs.uuid_maker.mk_soft_id()
        self.log.info('event load')
        # self.bonus_init_time = {}
        # self.hold_bonus_init_time = {}
        self.db_direct = libs.db.sql_db.PostgreSQL(dbname=conf.DB_NAME, user=conf.DB_USER, host=conf.DB_IP,
                                                   passwd=conf.DB_PASS,
                                                   port=conf.DB_PORT)
        self.day_reset_player = False
        self.real_time_look_get_data = {}
        self.mony_back_block = {}
        self.event = {
            'day_order_reset_player':self.day_order_reset_player,
            'get_date_times': self.get_date_time,
            'set_date_time': self.set_date_time,
            # 'SET_DATE_TIME': self.set_date_time,
            'bonus_init': self.bonus_init,
            'get_db_info': self.get_db_info,
            'get_client': self.get_client,
            'set_client': self.set_client,
            'send_mail': self.send_mail,
            'write_log': self.write_log,
            'client_want_bonus': self.client_want_bonus,
            'activ_bonus': self.activ_bonus,
            'last_bonus': self.last_bonus,
            'activ_bonus_update_mony': self.activ_bonus_update_mony,
            'activ_bonus_update': self.activ_bonus_update,
            'aft_in': self.aft_in,
            'revert_current_mony':self.revert_current_mony,
            'aft_out': self.aft_out,
            'version': self.version,
            'send_mail_won': self.send_mail_won,
            'reboot_server': self.reboot_server,
            'soft_reboot_server':self.soft_reboot,
            'get_crc': self.get_crc,
            'get_soft_id': self.get_soft_id,
            'mod_active': self.mod_active,
            'update_redirect': self.svn_update,
            'server_alive': self.server_alive,
            'ssh_port': self.ssh_port,
            'db_iptables': self.db_iptables,
            'set_pos':self.set_pos,
            'get_all_user':self.get_all_user,
            'chk_pos':self.chk_pos,
            'pos_inactive':self.pos_inactive,
            'license_chk':self.license_chk,
            'hold_client_cart_bonus': self.hold_client_cart_bonus,
            'cms_load_conf':self.cms_load_conf,
            'cms_save_conf':self.cms_save_conf,
            'print_on_server':self.print_on_server,
            'print_on_server_pos': self.print_on_server_pos,
            'get_printer':self.get_printer,
            'set_printer':self.set_printer,
            'i_get_player':self.i_get_player,
            # 'set_printer_pos': self.set_printer_pos,
            'open_in_other_device_bonus':self.open_in_other_device_bonus,
            # 'server_reset_player':self.server_reset_player,
            'run_linux_cmd_on_redirect':self.run_linux_cmd_on_redirect,
            'chk_for_bonus_warning':self.chk_for_bonus_warning,
            'clean_all_bonus': self.clean_all_bonus,
            'clean_current_mony':self.clean_current_mony,
            'get_player_mony':self.get_player_mony,
            'ping_smib': self.ping_smib,
            'get_real_ip':self.real_ip,
            'get_tz':self.get_tz,
            'get_bonus_cart_to_init':self.get_bonus_cart_to_init,
            'server_reset_player':self.server_reset_player,
            'clean_cust_tombula':self.clean_cust_tombula,
            'clean_won_print_rko':self.clean_won_print_rko,
            'get_next_time_bonus':self.get_next_time_bonus,
            'get_rev':self.get_rev,
            'write_in_out':self.write_in_out,
            'user_block': self.user_block,
            'unblock_user': self.unblock_user,
            'clean_tombula_in_mony':self.clean_tombula_in_mony,
            'nasko_print':self.nasko_print,
            'replace_cust_group':self.replace_cust_group,
            'chk_nra':self.chk_nra,
            'lk_set': self.lk_check_set,
            'del_all_lk': self.del_all_lk,
            'change_vnc_passwd': self.change_vnc_passwd,
            'del_get_mony':self.del_get_mony,
            # 'real_time_look_get':self.real_time_look_get,
            'mony_back_clear':self.mony_back_clear,
            'get_user_mony_back':self.get_user_mony_back,
            'del_monuback_user':self.del_monuback_user,
            'get_cpu_time':self.get_cpu_time,
            'get_croupie_bonus_hold':self.get_croupie_bonus_hold,
            # 'get_mony_from_cart':self.get_mony_from_cart,
            # 'set_mony_to_cart': self.set_mony_to_cart,
            # 'calc_total_for_player':self.calc_total_for_player,
        }

    def get_user_mony_back(self, **kwargs):
        if kwargs['id'] not in self.mony_back_block:
            self.mony_back_block[kwargs['id']] = time.time()
            user = self.db.get_one_where(models.CustUser, id=kwargs['id'])
            return int(user.total_mony_back)
        else:
            return 0

    def del_monuback_user(self, **kwargs):
        try:
            del self.mony_back_block[kwargs['id']]
        except KeyError:
            pass
        return True

    def mony_back_clear(self, **kwargs):
        try:
            del self.mony_back_block[kwargs['id']]
        except KeyError:
            pass
        user = self.db.get_one_where(models.CustUser, id=kwargs['id'])
        user.total_mony_back -= kwargs['mony']
        obj = self.db.make_obj(models.MonuBackPay)
        obj.mony = kwargs['mony']
        obj.cust_id = user.id
        obj.chk = True
        self.db.add_object_to_session(user)
        self.db.add_object_to_session(obj)
        return self.db.commit()

    def real_time_look_get(self, **kwargs):
        self.real_time_look_get_data = self.mem_db.get('real_time_look_get_data')
        if kwargs['get_from'] not in self.real_time_look_get_data:
            var = client.send(evt='chk_alife', ip=kwargs['get_from'], port=conf.PORT, timeout=4, log=self.log)
            if var is not None:
                tmp = client.send('real_time_look', ip=kwargs['get_from'],
                                  port=conf.PORT, log=self.log,
                                  timeout=conf.TIMEOUT_2 - 4)
            else:
                tmp = None
            if tmp == {}:
                tmp = None
            self.real_time_look_get_data[kwargs['get_from']] = kwargs['get_from']
            self.mem_db.set('real_time_look_get_data', self.real_time_look_get_data)
            self.mem_db.set(kwargs['get_from'], tmp)
        return self.mem_db.get(kwargs['get_from'])


    def change_vnc_passwd(self, **kwargs):
        os.system('chown colibri:colibri /home/olimex/.vnc/passwd')
        os.system('echo %s | vncpasswd -f > /home/olimex/.vnc/passwd' % kwargs['passwd'])
        os.system('chown olimex:olimex /home/olimex/.vnc/passwd')
        return True

    def lk_check_set(self, **kwargs):
        player = self.db.get_one_where(models.CustUser, personal_egn=kwargs['EGN'])
        if kwargs['EGN'] not in self.lk_check:
            self.lk_check.append(kwargs['EGN'])
            obj = self.db.get_one_where(models.Config, name='lk_check')
            obj.value = json.dumps(self.lk_check)
            self.db.add_object_to_session(obj)
            obj2 = self.db.make_obj(models.EGNCheck)
            if 'user_id' in kwargs:
                obj2.user_id = kwargs['user_id']
            if 'by_hand' in kwargs:
                obj2.by_hand = kwargs['by_hand']
            else:
                obj2.by_hand = False
            obj2.egn = kwargs['EGN']
            if player is not None:
                obj2.player_id = player.id
            self.db.add_object_to_session(obj2)
            #raise KeyError (obj2.egn, obj2.user_id, obj2.by_hand, obj2.player_id)
            self.db.commit()
        if player:
            if player.forbiden is True:
                return 'CANT_PLAY'
        return True

    def del_all_lk(self, **kwargs):
        self.lk_check = []
        self.in_nra_cheked = {}
        obj = self.db.get_one_where(models.Config, name='lk_check')
        obj.value = json.dumps(self.lk_check)
        self.db.add_object_to_session(obj)
        self.db.commit()
        return True

    def IsEGNValid(self, egn):
        try:
            int(egn)
            if len(egn) != 10:
                return False
            else:
                mounth = int(str('%s%s' % (egn[2:3], egn[3:4])))
                if mounth >= 40:
                    mounth = mounth - 40
                    year = int('20' + egn[0:1] + egn[1:2])
                else:
                    year = int('19' + egn[0:1] + egn[1:2])
                day = int(egn[4:5] + egn[5:6])
                # my_sity = int(egn[6:7] + egn[7:8]+egn[8:9])
                tmp = []
                for i in egn:
                    tmp.append(int(i))
                egn = tmp
                my_date = datetime.datetime.now()
                if mounth > 12 or mounth < 0:
                    return False
                if year < my_date.year - 100:
                    return False
                if my_date.year - 18 < year:
                    return 'LITLE'
                elif my_date.year - 18 == year:
                    if my_date.month < mounth:
                        return 'LITLE'
                    elif my_date.month == mounth:
                        if my_date.day <= day:
                            return 'LITLE'
                coef = [2, 4, 8, 5, 10, 9, 7, 3, 6]
                sum = 0.0
                for i in range(0, len(egn)):
                    if i < 9:
                        sum += egn[i] * coef[i]
                sum = sum % 11
                sum = int(sum)
                if sum == 10:
                    sum = 0
                if sum != egn[9]:
                    return False
                # burt_date = '%s.%s.%s' % (day, mounth, year)
                return True
        except Exception as e:
            self.log.error(e, exc_info=True)
            return False

    def chk_nra(self, **kwargs):
        try:
            client_id = self.db.get_one_where(models.Config, name='nra_client_id')
            token = self.db.get_one_where(models.Config, name='nra_token')
            if not client_id or not token:
                self.in_nra_cheked[kwargs['egn']] = False
                return False
            elif not client_id.value or not token.value:
                self.in_nra_cheked[kwargs['egn']] = False
                return False
            if kwargs['egn'] in self.in_nra_cheked:
                return self.in_nra_cheked[kwargs['egn']]
            egn_valid = self.IsEGNValid(kwargs['egn'])
            if egn_valid != True:
                if egn_valid == 'LITLE':
                    self.in_nra_cheked[kwargs['egn']] = 'LITLE'
                    return 'LITLE'
                else:
                    return 'ERROR'
            player = self.db.get_one_where(models.CustUser, personal_egn=kwargs['egn'])
            # if player:
            #     if player.in_nra is True:
            #         return True
            try:
                if 'timeout' in kwargs:
                    nra = libs.nra.NRA(client_id.value, token.value, conf.NRA_DEBUG, timeout=kwargs['timeout'])
                else:
                    nra = libs.nra.NRA(client_id.value, token.value, conf.NRA_DEBUG)
                nra_chk = nra.chk_egn(kwargs['egn'])
            except libs.nra.BadNRArequest as e:
                self.log.warning(e, exc_info=True)
                return 'ERROR'
            except Exception as e:
                self.log.warning(e, exc_info=True)
                return 'ERROR'
            if nra_chk is None:
                return 'ERROR'
            if 'disable' in kwargs:
                if kwargs['disable'] == True:
                    # obj = self.db.get_one_where(models.CustUser, personal_egn=kwargs['egn'])
                    if player is not None:
                        if nra_chk != player.in_nra:
                            player.in_nra = nra_chk
                            self.db.add_object_to_session(player)
                            self.db.commit()
            else:
                if player is not None:
                    if nra_chk != player.in_nra:
                        player.in_nra = nra_chk
                        self.db.add_object_to_session(player)
                        self.db.commit()
            if nra_chk == False or nra_chk == True:
                self.in_nra_cheked[kwargs['egn']] = nra_chk
            return nra_chk
        except Exception as e:
            self.log.error(e, exc_info=True)
        return 'ERROR'

    def day_order_reset_player(self, **kwargs):
        self.day_reset_player = kwargs['end_date']
        return True

    def user_block(self, **kwargs):
        self.block_user.append(kwargs['cust_id'])
        return True

    def unblock_user(self, **kwargs):
        self.block_user = []
        return True

    def nasko_print(self, **kwargs):
        user = self.db.get_one_where(models.CustUser, id=kwargs['cust_id'])
        if user is None:
            return False
        elif user.forbiden is True:
            return False
        if user.id in self.block_user:
            return False
        # self.block_user.append(user.id)
        full_total = 0
        time_format = libs.rtc.date_format.BG(None)
        end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        last_day_order = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
        if last_day_order == None:
            start_time = '2010-01-01'
        else:
            start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
        get_statistic = self.db.get_all_where(models.CustStatistic, cust_id=user.id,
                                              pub_time__btw=(start_time, end_time))
        full_total = self.calc_full_total(get_statistic)
        # self.log.error('get_statistic=%s, start_time=%s end_time=%s, user_name=%s' % (get_statistic, start_time, end_time, user.name))
        if full_total <= 0:
            return False
        conf = {}
        tmp = 0
        for i in kwargs['conf']:
            # print i, kwargs['conf'][i], conf
            if "p" not in kwargs['conf'][i]:
                tmp = float(kwargs['conf'][i])
            else:
                # kwargs['conf'][i] = kwargs['conf'][i].replace('%', '')
                tmp = str(kwargs['conf'][i])
            i = i.replace('m', '')
            # i = i.replace('_', '.')
            i = int(i)
            conf[i] = tmp
        mony = False
        for i in sorted(list(conf.keys())):
            if full_total >= i:
                mony = conf[i]
        if mony is False:
            return False
        obj = self.db.get_one_where(models.PointInMonyPrinted, cust_id=user.id, pub_time__gte=start_time)
        if obj:
            return False
        obj = self.db.make_obj(models.PointInMonyPrinted)
        if type(mony) == str:
            mony = int(mony.replace('p', ''))
            mony = float(round((full_total * mony)*0.01, 0))
        obj.point_sum = float(round(mony,2))
        obj.cust_id = user.id
        obj.pub_user_id = 1
        self.db.add_object_to_session(obj)
        # self.db.add_object_to_session(user)
        dates = datetime.datetime.now()
        dates = time_format.date_to_str(dates, '%d.%m%Y %H:%M:%S')
        casino = self.db.get_one_where(models.Config, name='pos_printer_info')
        if casino == None:
            object = u''
            sity = u''
            adress = u''
        else:
            casino = json.loads(casino.value)
            object = casino['object']
            sity = casino['sity']
            adress = casino['adress']
        name = user.name
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
        id = self.db.get_one(models.PointInMonyPrinted, order='id', descs=True)
        if id == None:
            ID = 1
        else:
            ID = id.id + 1
        ID = str(ID)
        ID = ('0' * (9 - len(ID))) + ID
        cust_adress = user.personal_addres
        if user.persona_sity_id:
            cust_sity = user.persona_sity.name
        else:
            cust_sity = ''
        data = {'count': "{:.2f}".format(obj.point_sum), 'sity': sity, 'copy': True, 'objects': object,
                'adress': adress,
                'name': name, 'dates': dates, 'ID': ID, 'len': len(user.name), 'user_id': 1,
                'cust_adress': cust_adress,
                'cust_sity': cust_sity, 'original': True}
        self.db.commit()
        return data

    def get_next_time_bonus(self, reset_group=False, **kwargs):
        if reset_group is False:
            reset_group = 0
            if 'del_cart' in kwargs:
                mashin = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
                if not mashin:
                    return False
            else:
                if kwargs['my_name'] != 'term':
                    mashin = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
                    if kwargs['cart_id'] in self.card_is_in:
                        return False
                    if not mashin:
                        return False
                else:
                    # pass
                    mashin = self.db.get_one_where(models.Device, enable=True, sas=True)
                    # if not mashin:
                    #     return False
                    # self.i_get_player(cart_id=kwargs['cart_id'])
                    # mashin = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
                    # if not mashin:
                    #     return False
            try:
                cart = self.db.get_one_where(models.CustCart, catr_id=kwargs['cart_id'])
            except Exception as e:
                self.log.warning(e, exc_info=True)
                return False

            if not cart:
                return False
        user = cart.user

        if not user:
            return False
        if user.forbiden:
            return False
        # if kwargs['cart_id'] in self.card_is_in:
        #     return False
        # else:
        #     if kwargs['my_name'] != 'term':
        #         self.card_is_in[kwargs['cart_id']] = kwargs['my_name']

        full_total = 0
        activ_bonus = self.activ_bonus(cust_id=user.id, grup=user.grup.name)
        if user.bonus_one_per_day is True:
            down_bonus_count = 1
            last_bonus = self.last_bonus(cust_id=user.id, grup=user.grup.name)
        else:
            down_bonus_count = self.last_bonus(cust_id=user.id, count=True)
            if down_bonus_count >= 0:
                down_bonus_count = 1
            last_bonus = True
        rtc = libs.rtc.date_format.BG(None)
        if user.bonus_on_day == '':
            bonus_on_day = True
        else:
            # bonus_on_day = True
            bonus_on_day = json.loads(user.bonus_on_day)
            date_now = datetime.datetime.now() + datetime.timedelta(days=1)
            sm_day = datetime.date.weekday(date_now)
            if sm_day in bonus_on_day:
                pub_time = rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d')
                last_day_report = self.db.get_one_where(models.DayReport, day_report=True, pub_time__btw=(
                    pub_time + ' 00:00:00', rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')))
                if last_day_report == None:
                    if sm_day > 0 and sm_day - 1 in bonus_on_day:
                        bonus_on_day = True
                    elif sm_day == 0 and 6 in bonus_on_day:
                        bonus_on_day = True
                    else:
                        bonus_on_day = False
                else:
                    bonus_on_day = True
            elif sm_day > 0 and sm_day - 1 in bonus_on_day:
                pub_time = rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d')
                last_day_report = self.db.get_one_where(models.DayReport, day_report=True, pub_time__btw=(
                    pub_time + ' 00:00:00', rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')))
                if last_day_report == None:
                    bonus_on_day = True
                else:
                    bonus_on_day = False
            elif sm_day == 0 and 6 in bonus_on_day:
                pub_time = rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d')
                last_day_report = self.db.get_one_where(models.DayReport, day_report=True, pub_time__btw=(
                    pub_time + ' 00:00:00', rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')))
                if last_day_report == None:
                    bonus_on_day = True
                else:
                    bonus_on_day = False
            else:
                bonus_on_day = False
        time_format = libs.rtc.date_format.BG(None)
        end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        last_day_order = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
        if last_day_order == None:
            start_time = '2010-01-01'
        else:
            start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
        if user.bonus_warning_use is True:
            bonus_warning_initial = self.db.get_one_where(models.BonusCartLog, pub_time__btw=(start_time, end_time),
                                                          cust_id=user.id, bonus_hold=False)
            if bonus_warning_initial == None:
                bonus_warning_initial = True
            else:
                bonus_warning_initial = False
        else:
            bonus_warning_initial = False
        try:
            bonus_row = json.loads(user.bonus_row)
        except:
            bonus_row = {}
        if user.man is None:
            try:
                egn = int(user.personal_egn)
                if len(user.personal_egn) != 10:
                    raise KeyError
                if int(user.personal_egn[8]) % 2 > 0:
                    user.man = False
                else:
                    user.man = True
            except Exception:
                user.man = True
            self.db.add_object_to_session(user)
            self.db.commit()
        bonus_if_man = user.bonus_if_man
        tmp = {
            'come_on_emg_time': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
            'last_bonus': last_bonus,
            'in_nra': user.in_nra,
            'bonus_hold': user.bonus_hold,
            'down_bonus_count': down_bonus_count,
            'activ_bonus': activ_bonus,
            'cart_id': kwargs['cart_id'],
            'id': user.id,
            'full_total': full_total,
            'name': user.name,
            'pin': user.pin,
            'curent_mony': user.curent_mony,
            'forbiden': user.forbiden,
            'use_group_conf': user.use_group_conf,
            'mony_back_use': user.mony_back_use,
            'mony_back_pr': user.mony_back_pr,
            'bonus_on_day': bonus_on_day,
            'tombola_use': user.tombola_use,
            'tombola_coef': user.tombola_coef,
            'tombola_on_in': user.tombola_on_in,
            'no_out_befor': user.no_out_befor,
            'bonus_use': user.bonus_use,
            'bonus_by_in': user.bonus_by_in,
            'bonus_direct': user.bonus_direct,
            'bonus_one_per_day': user.bonus_one_per_day,
            'one_day_back_total': user.one_day_back_total,
            'mount_total': user.month_back,
            'bonus_on_mony': user.bonus_on_mony,
            'bonus_waith_for_in': user.bonus_waith_for_in,
            'bonus_row': bonus_row,
            'bonus_waith_for_in_mony': user.bonus_waith_for_in_mony,
            # 'x2':user.x2,
            # 'bonus_row_1_count': user.bonus_row_1_count,
            # 'bonus_row_2_mony': user.bonus_row_2_mony,
            # 'bonus_row_2_count': user.bonus_row_2_count,
            # 'bonus_row_3_mony': user.bonus_row_3_mony,
            # 'bonus_row_3_count': user.bonus_row_3_count,
            # 'bonus_row_4_mony': user.bonus_row_4_mony,
            # 'bonus_row_4_count': user.bonus_row_4_count,
            'grup_id': user.grup_id,
            'grup': user.grup.name,
            'total_bonus': user.total_bonus,
            'total_mony_back': user.total_mony_back,
            'total_tombula': user.total_tombula,
            'bonus_warning_use': user.bonus_warning_use,
            'bonus_warning_mony': user.bonus_warning_mony,
            'bonus_revert_by_bet': user.bonus_revert_by_bet,
            'bonus_warning_initial': bonus_warning_initial,
            'restricted_bonus': user.restricted_bonus,
            'use_total_procent': user.use_total_procent,
            'total_procent': user.total_procent,
            'from_redirect': False,
            'more_than_one_from_redirect': user.more_than_one_from_redirect,
            'region_id': mashin.flor_id,
            'group_region': user.region_id,
            'mony_back_min_pay': user.mony_back_min_pay,
            'mony_back_pay': user.mony_back_pay,
            'bonus_if_man': bonus_if_man,
            'man': user.man,
            # 'from_redirect_name':
        }
        if tmp['bonus_if_man'] != None:
            if tmp['bonus_if_man'] != user.man:
                tmp['bonus_use'] = False

        tmp = self.replace_cust_group(tmp, up_dates=True)
        # print tmp['mount_total']
        # raise Exception, tmp
        # self.log.error('bonus_one_per_day %s', tmp['bonus_one_per_day'])
        if tmp['bonus_one_per_day'] is True:
            if tmp['one_day_back_total'] is False and tmp['mount_total'] is False:
                end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                if last_day_order == None:
                    start_time = '2010-01-01'
                else:
                    start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
            elif tmp['one_day_back_total'] is True:
                end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                if last_day_order == None:
                    start_time = '2010-01-01'
                else:
                    start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
                #
            elif tmp['mount_total'] is True:
                last_mounth = self.db.get_one_where(models.DayReport, day_report=False, descs=True, order='id')
                if last_mounth != None:
                    start_time = time_format.date_to_str(last_mounth.pub_time, '%Y-%m-%d %H:%M:%S')
                else:
                    start_time = '2010-01-01'
                if last_day_order == None:
                    end_time = '2010-01-01'
                else:
                    end_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
            else:
                end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                if last_day_order == None:
                    start_time = '2010-01-01'
                else:
                    start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
            self.log.info('start_time: %s, end_time:%s' % (start_time, end_time))
            get_statistic = self.db.get_all_where(models.CustStatistic, cust_id=user.id,
                                                  pub_time__btw=(start_time, end_time))

            full_total = self.calc_full_total(get_statistic)
        else:
            full_total = 0
        tmp['full_total'] = full_total

        # self.log.info('%s %s %s' % (tmp['bonus_one_per_day'], tmp['one_day_back_total'] , full_total))
        if tmp['bonus_one_per_day'] is True and tmp['one_day_back_total'] is True:
            tmp = self.replace_cust_group(tmp, full_total, up_dates=True)
            # self.log.info('%s', tmp)
        elif tmp['bonus_one_per_day'] is True and tmp['mount_total'] is True:
            tmp = self.replace_cust_group(tmp, full_total, up_dates=True)
        else:
            tmp['mount_total'] = False
            tmp['one_day_back_total'] = False

        if tmp['use_total_procent'] is True and full_total > 0:
            total_procent = tmp['total_procent'] * 0.01
            bonus = int(round(tmp['full_total'] * total_procent, 0))
            tmp['bonus_row'] = {"{:.2f}".format(bonus):10}
            # tmp['x2'] = False
            # tmp['bonus_row_2_mony'] = bonus
            # tmp['bonus_row_3_mony'] = bonus
            # tmp['bonus_row_4_mony'] = bonus
        self.log.info('tmp: %s', tmp)
        return tmp


    def clean_won_print_rko(self, **kwargs):
        player = self.db.get_one_where(models.CustUser, id=kwargs['cust_id'], forbiden=False)
        if player == None:
            return False
        rtc = libs.rtc.date_format.BG(None)
        casino = self.db.get_one_where(models.Config, name='pos_printer_info')
        if casino == None:
            objects = u''
            sity = u''
            objects_adress = u''
        else:
            casino = json.loads(casino.value)
            objects = casino['object']
            sity = casino['sity']
            objects_adress = casino['adress']
        object_info = self.db.get_one_where(models.Config, name='object_info')
        object_info = json.loads(object_info.value)
        self.start_date = self.db.get_one_where(models.CashOutPrinted, cust_id=player.id, order='id', descs=True)
        if self.start_date == None:
            self.start_date = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
        if self.start_date != None:
            self.start_date = self.start_date.pub_time
        else:
            self.start_date = datetime.datetime.now()

        self.end_date = rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        self.start_date = rtc.date_to_str(self.start_date, '%Y-%m-%d %H:%M:%S')
        # print self.start_date, self.end_date
        statistic = self.db.get_all_where(models.CustStatistic, order='id', cust_id=player.id, descs=True,
                                          pub_time__btw=(self.start_date, self.end_date))
        statistic_mony = 0

        if statistic != None:
            for i in statistic:
                ins = i.ins + i.curent_credit_on_in
                out = i.out + i.curent_credit
                statistic_mony += ins - out
        # print statistic_mony
        if statistic_mony >= 0:
            return [-1, -1]
        else:
            statistic_mony = statistic_mony * -1
        EIK = object_info['EIK']
        company = object_info['company']
        mony = "{:.2f}".format(statistic_mony)
        egn = player.personal_egn
        cust_name = player.name
        user_id = u'...'
        dates = rtc.date_to_str(formats='%d.%m.%Y %H:%M:%S')
        id = self.db.get_one(models.CashOutPrinted, order='id', descs=True)
        if id == None:
            ID = 1
        else:
            ID = id.id + 1
        ID = str(ID)
        ID = ('0' * (9 - len(ID))) + ID
        rko = self.db.make_obj(models.CashOutPrinted)
        rko.mony = float(mony)
        rko.cust_id = player.id
        rko.pub_user_id = 1
        self.db.add_object_to_session(rko)
        self.db.commit()
        if player.persona_sity_id:
            cust_sity = player.persona_sity.name
        else:
            cust_sity = ''
        cust_adress = player.personal_addres
        data = {'company': company, 'EIK': EIK, 'objects': objects, 'sity': sity, 'objects_adress': objects_adress,
                    'name': cust_name, 'egn': egn, 'mony': [mony], 'user_id': user_id, 'ID': [ID], 'dates': dates,
                    'cust_sity': cust_sity,
                    'cust_adress': cust_adress, 'count': 1, 'my_copy':False}
        return [data, statistic_mony]
        # return False

    def clean_cust_tombula(self, **kwargs):
        # kwargs = kwargs[1]
        player = self.db.get_one_where(models.CustUser, id=kwargs['cust_id'], forbiden=False)
        if player == None:
            return False
        if player.total_tombula <= 0:
            return False
        player.total_tombula -= kwargs['tombula_print_count']
        time_format = libs.rtc.date_format.BG(None)
        end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        last_day_order = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
        if last_day_order == None:
            start_time = '2010-01-01'
        else:
            start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
        if player.tombola_on_in is True:
            obj = self.db.get_one_where(models.TombulaPrinted, cust_id=player.id, pub_time__gte=start_time)
            if obj:
                return False
        self.db.add_object_to_session(player)
        obj = self.db.make_obj(models.TombulaPrinted)
        obj.tombula_count = kwargs['tombula_print_count']
        obj.cust_id = player.id
        obj.pub_user_id = 1
        self.db.add_object_to_session(obj)
        # self.db.add_object_to_session(player)
        casino = self.db.get_one_where(models.Config, name='pos_printer_info')
        if casino == None:
            object = u''
            sity = u''
            adress = u''
        else:
            casino = json.loads(casino.value)
            object = casino['object']
            sity = casino['sity']
            adress = casino['adress']
        name = player.name
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
        rtc = libs.rtc.date_format.BG(None)
        dates = datetime.datetime.now()
        dates = rtc.date_to_str(dates, formats='%d.%m.%Y')
        data = {'count': obj.tombula_count, 'sity': sity, 'copy': False, 'object': object, 'adress': adress,
                'name': name, 'dates': dates, 'ID': obj.id, 'len': len(player.name)}
        # if self.db.get_one_where(libs.models.Config, name='block_cust_if_print_tombula') == 'True':
        #     self.block_user.append(player.id)
        self.db.commit()
        return data

    def clean_tombula_in_mony(self, **kwargs):
        player = self.db.get_one_where(models.CustUser, id=kwargs['cust_id'], forbiden=False)
        if player == None:
            return False
        if player.total_tombula <= 0:
            return False
        player.total_tombula -= kwargs['tombula_print_count']
        time_format = libs.rtc.date_format.BG(None)
        end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        last_day_order = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
        if last_day_order == None:
            start_time = '2010-01-01'
        else:
            start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
        if player.tombola_on_in is True:
            obj = self.db.get_one_where(models.PointInMonyPrinted, cust_id=player.id, pub_time__gte=start_time)
            if obj:
                return False
        obj = self.db.make_obj(models.PointInMonyPrinted)
        obj.point_sum = float(round(kwargs['tombula_print_count'] * player.bonus_in_mony_sum, 2))
        obj.cust_id = player.id
        obj.pub_user_id = 1
        self.db.add_object_to_session(obj)
        self.db.add_object_to_session(player)
        rtc = libs.rtc.date_format.BG(None)
        dates = datetime.datetime.now()
        dates = rtc.date_to_str(dates, '%d.%m%Y %H:%M:%S')
        casino = self.db.get_one_where(models.Config, name='pos_printer_info')
        if casino == None:
            object = u''
            sity = u''
            adress = u''
        else:
            casino = json.loads(casino.value)
            object = casino['object']
            sity = casino['sity']
            adress = casino['adress']
        name = player.name
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
        id = self.db.get_one(models.PointInMonyPrinted, order='id', descs=True)
        if id == None:
            ID = 1
        else:
            ID = id.id + 1
        ID = str(ID)
        ID = ('0' * (9 - len(ID))) + ID
        cust_adress = player.personal_addres
        if player.persona_sity_id:
            cust_sity = player.persona_sity.name
        else:
            cust_sity = ''
        data = {'count': "{:.2f}".format(obj.point_sum), 'sity': sity, 'copy': False, 'objects': object,
                    'adress': adress,
                    'name': name, 'dates': dates, 'ID': ID, 'len': len(player.name), 'user_id': 1,
                    'cust_adress': cust_adress,
                    'cust_sity': cust_sity, 'original': True}
        # if self.db.get_one_where(models.Config, name='block_cust_if_print_tombula') == 'True':
        #     self.block_user.append(player.id)
        self.db.commit()
        return data

    def get_tz(self, **kwargs):
        return os.popen('cat /etc/timezone').read()[:-1]

    def real_ip(self, **kwargs):
        return {self.uuid: libs.diagnostic.arm.OlimexMicro().get_real_ip()}

    def del_get_mony(self, **kwargs):
        try:
            del self.get_mony[kwargs['player_id']]
        except:
            pass
        return True

    def get_player_mony(self, **kwargs):
        if kwargs['player_id'] in self.get_mony:
            return 0
        self.get_mony[kwargs['player_id']] = kwargs['my_name']
        player = self.db.get_one_where(models.CustUser, id=kwargs['player_id'])
        return player.curent_mony


    def clean_current_mony(self, **kwargs):
        player = self.db.get_one_where(models.CustUser, id=kwargs['player_id'])
        if kwargs['out'] is True:

            # del self.get_mony[kwargs['player_id']]
            data = self.aft_out(cust_id=kwargs['player_id'], mony=kwargs['mony'], my_name=kwargs['my_name'])
            player.curent_mony += kwargs['mony']
            self.db.add_object_to_session(player)
            self.db.commit()
        else:
            try:
                del self.get_mony[kwargs['player_id']]
            except KeyError:
                pass
            data = self.aft_in(cust_id=kwargs['player_id'], mony=kwargs['mony'], my_name=kwargs['my_name'])
            player.curent_mony -= kwargs['mony']
            self.db.add_object_to_session(player)
            self.db.commit()
        return player.curent_mony, data


    def version(self, **kwargs):
        return conf.VERSION

    def chk_for_bonus_warning(self, **kwargs):
        time_format = libs.rtc.date_format.BG(None)
        end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        last_day_order = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
        if last_day_order == None:
            start_time = '2010-01-01'
        else:
            start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
        data = self.db.get_one_where(models.BonusCartLog, cust_id=kwargs['player_id'], pub_time__btw=(start_time, end_time), bonus_hold=False)
        if not data:
            return True
        return False

    def run_linux_cmd_on_redirect(self,**kwargs):
        if kwargs['cmd'] == 'RTC_write':
            libs.rtc.olimex_mod.RTC_BUG_FIX = conf.RTC_BUG
            libs.rtc.olimex_mod.RTC_TIME_ZONE = conf.TZ
            libs.rtc.olimex_mod.RTC_Bus = conf.RTC_BUS
            return libs.rtc.olimex_mod.Write_RTC()
        elif kwargs['cmd'] == 'RTC_read':
            libs.rtc.olimex_mod.RTC_BUG_FIX = conf.RTC_BUG
            libs.rtc.olimex_mod.RTC_TIME_ZONE = conf.TZ
            libs.rtc.olimex_mod.RTC_Bus = conf.RTC_BUS
            return libs.rtc.olimex_mod.Read_RTC()
        elif kwargs['cmd'] == 'RTC_sync':
            libs.rtc.olimex_mod.RTC_BUG_FIX = conf.RTC_BUG
            libs.rtc.olimex_mod.RTC_TIME_ZONE = conf.TZ
            libs.rtc.olimex_mod.RTC_Bus = conf.RTC_BUS
            return libs.rtc.olimex_mod.Sync_RTC()
        return os.popen(kwargs['cmd']).read()

    def server_reset_player(self, **kwargs):
        self.card_is_in = {}
        return True

    # def set_printer_pos(self, **kwargs):
    #     conf.DEFAULT_PRINTER_POS = kwargs['printer']
    #     conf.CONF.update_option('PRINTER', default_pos=kwargs['printer'])
    #     return True

    def set_printer(self, **kwargs):
        conf.DEFAULT_PRINTER = kwargs['printer']
        conf.DEFAULT_PRINTER_POS = kwargs['printer_pos']
        conf.CONF.update_option('PRINTER', default=kwargs['printer'])
        conf.CONF.update_option('PRINTER', default_pos=kwargs['printer_pos'])
        return True

    def get_printer(self, **kwargs):
        try:
            conn = cups.Connection()
            printers = conn.getPrinters()
            all_printer = ['']
            for printer in printers:
                all_printer.append(printer)
            return all_printer, conf.DEFAULT_PRINTER, conf.DEFAULT_PRINTER_POS
        except Exception as e:
            self.log.error(e, exc_info=True)
            return [''], conf.DEFAULT_PRINTER

    def print_on_server_pos(self, **kwargs):
        if conf.DEFAULT_PRINTER_POS == '':
            return False
        my_pdf = open('/tmp/server1.pdf', 'wb')
        my_pdf.write(binascii.unhexlify(kwargs['tmp_file']))
        my_pdf.close()
        time.sleep(2)
        cmd = 'lp -d %s %s' % (conf.DEFAULT_PRINTER_POS, '/tmp/server1.pdf')
        if 'ranges' in kwargs:
            for i in range(kwargs['ranges']):
                os.system(cmd)
        else:
            os.system(cmd)
        return True

    def print_on_server(self, **kwargs):
        if conf.DEFAULT_PRINTER == '':
            return False

        my_pdf = open('/tmp/server.pdf', 'wb')
        my_pdf.write(binascii.unhexlify(kwargs['tmp_file']))
        my_pdf.close()
        time.sleep(2)
        cmd = 'lp -d %s %s' % (conf.DEFAULT_PRINTER, '/tmp/server.pdf')
        if 'ranges' in kwargs:
            for i in range(kwargs['ranges']):
                os.system(cmd)
        else:
            os.system(cmd)
        return True

    def soft_reboot(self, **kwargs):
        os.system('sudo service colibri restart')
        return True

    def cms_load_conf(self, **kwargs):
        tmp = {
            # 'gmail':conf.SEND_GMAIL,
            'tcp': conf.TCP,
            'iptables': conf.IPTASBLES,
            'ban': conf.BAN_PROC,
            'log_server': conf.LOG_SERVER,
            'rtc': conf.RTC,
            'mail_to': conf.MAIL_ON_WON,
            'mail_subject': conf.MAIL_ON_WON_SUBJECT,
            'thread': conf.IN_THREAD,
            'iv_jump': conf.COMUNICATION_IV_JUMP,
            'nra_debug': conf.NRA_DEBUG,
            'ocr_use': conf.OCR_UNLOCK,
        }
        return tmp

    def cms_save_conf(self, **kwargs):
        data = kwargs['data']
        # conf.CONF.update_option('SYSTEM', in_thread=data['in_thread'])
        conf.CONF.update_option('SYSTEM', log_server=data['log_server'])
        # conf.CONF.update_option('SYSTEM', gmail=data['gmail'])
        conf.CONF.update_option('SYSTEM', rtc=data['rtc'])
        conf.CONF.update_option('SYSTEM', tcp=data['tcp'])
        conf.CONF.update_option('BAN', iptables=data['iptables'])
        conf.CONF.update_option('BAN', ban_proc_run=data['ban'])
        conf.CONF.update_option('SYSTEM', mail_on_won=data['mail_to'])
        conf.CONF.update_option('SYSTEM', mail_on_won_subject=data['mail_subject'])
        conf.CONF.update_option('SYSTEM', in_thread=data['thread'])
        conf.CONF.update_option('SYSTEM', iv_jump=data['iv_jump'])
        conf.CONF.update_option('NRA', debug=data['nra_debug'])
        conf.CONF.update_option('OCR', unlock=data['ocr_use'])
        return True

    def license_chk(self, **kwargs):
        rsa = libs.rsa.RSAKey()
        rsa.load_key(conf.PUB)
        data = kwargs['data']
        signature = kwargs['signature']
        my_data = json.loads(data)
        if my_data['uuid'] != self.uuid:
            self.log.error('uuid')
            return False
        elif datetime.datetime.strptime(my_data['end_time'], '%d.%m.%Y') < datetime.datetime.now():
            self.log.error('end_time')
            return False
        elif rsa.verify(data, signature) is False:
            self.log.error('sig %s', signature)
            return False
        else:
            return True

    def chk_pos(self, **kwargs):
        pos = self.db.get_one_where(models.Config, name='pos')
        if pos == None:
            pos = self.db.make_obj(models.Config)
            pos.name = 'pos'
            pos.value = json.dumps({kwargs['pos_id']: 'INIT'})
            self.db.add_object_to_session(pos)
            return self.db.commit()
            # return True
        else:
            pos = json.loads(pos.value)
            # raise KeyError, (kwargs, pos)
            if pos == {}:
                pos = self.db.get_one_where(models.Config, name='pos')
                # pos.name = 'pos'
                pos.value = json.dumps({kwargs['pos_id']: 'INIT'})
                self.db.add_object_to_session(pos)
                return self.db.commit()
                # return True
            if kwargs['pos_id'] not in pos:
                return 'INSTALL'
            else:
                return True
        return False

    def get_all_user(self, **kwargs):
        user = self.db.get_all_where(models.User, enable=True)
        all_user = []
        for i in user:
            all_user.append(i.name)
        return all_user

    def set_pos(self, **kwargs):
        pos = self.db.get_one_where(models.Config, name='pos')
        new_data = json.loads(pos.value)
        user = self.db.get_one_where(models.User, name=kwargs['user'], enable=True)
        if user == None:
            return 'BAD NAME'
        if kwargs['passwd'] != user.passwd:
            return 'BAD PASSWD'
        right = user.grup.from_json()
        if 5 not in right['config']:
            return 'NO RIGHT'
        if kwargs['name'] in new_data.values():
            return 'BAD NAME'
        elif kwargs['pos_id'] in new_data:
            return 'BAD POS ID'
        else:
            new_data[kwargs['pos_id']] = kwargs['name']
            pos.value = json.dumps(new_data)
            self.db.add_object_to_session(pos)
            return self.db.commit()

    def pos_inactive(self, **kwargs):
        obj = self.db.get_one_where(models.Config, name=kwargs['pos_id'])
        if obj != None:
            data = json.loads(obj.value)
            data['activ'] = False
            obj.value = json.dumps(data)
            # obj.to_json()
            # obj.from_json()
            self.db.add_object_to_session(obj)
            return self.db.commit()
        # else:
        #     obj = self.db.make_obj(models.Config)
        #     obj = self.db.make_obj(models.Config)
        #     obj.name = kwargs['pos_id']
        #     # obj.value =
        #     obj.value = json.dumps({'ip': kwargs['unblock_ip'].keys()[0], 'activ': True, 'ban': False})
        #     self.db.add_object_to_session(obj)
        return False

    def ping_smib(self, **kwargs):
        data = libs.diagnostic.arm.OlimexMicro().network(kwargs['new_ip'], count=1)
        return data

    def db_iptables(self, **kwargs):
        if conf.IPTASBLES == True:
            # return True
            ip = list(kwargs['unblock_ip'].keys())[0]
            cmd_tcp = 'sudo iptables -A INPUT -p tcp -s %s' + ' --dport %s -j ACCEPT' % (conf.DB_PORT)
            cmd_tcp_drop = 'sudo iptables -A INPUT -s %s -j DROP'
        # raise Exception, kwargs['pos_id']
        chk = self.chk_pos(pos_id=kwargs['pos_id'])
        if chk is False:
            return False
        elif chk == 'INSTALL':
            # raise Exception, chk
            return 'INSTALL'
        if conf.IPTASBLES == False:
            return True
        conf.OPEN_IP = conf.CONF.get('OPEN_IP')
        # import ban_proc
        # for i in ban_proc.IP_TABLESS:
        #     print 'SET ROW', i
        #     os.system(i)
        obj = self.db.get_one_where(models.Config, name=kwargs['pos_id'])
        if obj == None:
            obj = self.db.make_obj(models.Config)
            obj.name = kwargs['pos_id']
            # obj.value =
            obj.value = json.dumps({'ip': list(kwargs['unblock_ip'].keys())[0], 'activ':True, 'ban':False})
            self.db.add_object_to_session(obj)
            self.db.commit()
        else:
            value = json.loads(obj.value)
            value['ip'] = list(kwargs['unblock_ip'].keys())[0]
            value['activ'] = True
            obj.value = json.dumps(value)
            self.db.add_object_to_session(obj)
            self.db.commit()
                # raise Exception, obj
                # if '192.168.1.' in ip:
                #     return True
            # if 'NEW_SVN_IP' == ip:
            #     return True
            # elif '127.0.0.1' == ip:
            #     return True
            # if conf.IPTASBLES is False:
            #     return True
            if value['ban'] is True:
                kwargs['unblock_ip'][list(kwargs['unblock_ip'].keys())[0]] = False
                try:
                    conf.CONF.add_option('OPEN_IP', **kwargs['unblock_ip'])
                    conf.OPEN_IP[ip] = 'False'
                        # return False
                except libs.config.ConfWarning:
                    conf.CONF.update_option('OPEN_IP', **kwargs['unblock_ip'])
                os.system('sudo iptables -D INPUT -j DROP')
                os.system(cmd_tcp % (ip))
                os.system('sudo iptables -A INPUT -j DROP')
                return False
            # obj.value = value

        # if '192.168.1.' in ip:
        #     return True
        # if 'NEW_SVN_IP' == ip:
        #     return True
        # elif '127.0.0.1' == ip:
        #     return True
        # if conf.IPTASBLES is False:
        #     return True
        if ip not in list(conf.OPEN_IP.keys()):
            try:
                conf.CONF.add_option('OPEN_IP', **kwargs['unblock_ip'])
                conf.OPEN_IP[ip] = 'True'
                os.system('sudo iptables -D INPUT -j DROP')
                os.system(cmd_tcp % (ip))
                os.system('sudo iptables -A INPUT -j DROP')
                return True
            except libs.config.ConfWarning:
                return False
        elif conf.OPEN_IP[ip] == 'False':
            return False
        elif conf.OPEN_IP[ip] == 'True':
            return True
        # raise Exception, conf.OPEN_IP[ip]
        return False

    def ssh_port(self, **kwargs):
        cmd = 'sudo grep Port /etc/ssh/sshd_config'
        data = os.popen(cmd).read()
        data = data.replace('Port ', '')
        try:
            data = int(data)
        except ValueError:
            try:
                cmd = 'sudo grep "\<Port\>" /etc/ssh/sshd_config'
                data = os.popen(cmd).read()[:-1]
                data = data.replace('Port ', '')
                data = int(data)
            except ValueError:
                return None
        return data

    def server_alive(self, **kwargs):
        return True

    def get_rev(self, **kwargs):
        return [conf.VERSION, conf.REV]

    def svn_update(self, **kwargs):
        if 'url' not in kwargs:
            if os.uname()[-1] == 'armv7l':
                var = 'ARM'
            else:
                var = 'Linux'
            url = 'svn://NEW_SVN_IP/home/svn/RedirectServer_BIN/%s/%s' % (conf.VERSION, var)
        else:
            url = kwargs['url']

        if 'my_dir' not in kwargs:
            my_dir = os.getcwd()
        else:
            my_dir = kwargs['my_dir']
        if 'user' in kwargs:
            user = kwargs['user']
        else:
            user = 'smib'
        if 'passwd' in kwargs:
            passwd = kwargs['passwd']
        else:
            passwd = 'smib_update'
        connect = libs.subversion.SubVersion(folder=my_dir, user=user, passwd=passwd, url=url)
        # try:
        # except Exception as e:
        #     self.log.error(e, exc_info=True)
        #     return None
        if 'rev' in kwargs:
            rev = kwargs['rev']
        else:
            rev = None
        connect.checkout()
        rev = connect.update(rev=rev)
        if 'migrate' in kwargs:
            if kwargs['migrate'] is True:
                os.system('sudo alembic revision --autogenerate')
                db = libs.db.sql_db.PostgreSQL(dbname=conf.DB_NAME, user=conf.DB_USER, host=conf.DB_IP, passwd=conf.DB_PASS, port=conf.DB_PORT)
                db.connect()
                db.close_all_session()
                os.system('sudo alembic upgrade head')

        # try:
        conf.CONF.update_option('SYSTEM', rev=rev)
        if conf.OLD_REV != conf.REV:
            conf.CONF.update_option('SYSTEM', old_rev=conf.REV)
        t = threading.Thread(target=self.soft_reboot_shedult)
        t.start()
        return rev

    def soft_reboot_shedult(self, times=10, **kwargs):
        time.sleep(times)
        self.soft_reboot()
        return True

    def _run_registred_licenz(self, ip_to_run, name):
        for i in ip_to_run:
            if name == 'base':
                client.send('sas_start', ip=i, port=conf.PORT, log=self.log)
                client.send('rfid_start', ip=i, port=conf.PORT, log=self.log)
            elif name == 'keysystem':
                client.send('keysystem_start', ip=i, port=conf.PORT, log=self.log)
            elif name == 'bonus_cart':
                client.send('bonus_start', ip=i, port=conf.PORT, log=self.log)
            elif name == 'client':
                client.send('client_cart_start', ip=i, port=conf.PORT, log=self.log)
            elif name == 'jackpot':
                client.send('jackpot_start', ip=i, port=conf.PORT, log=self.log)

    def run_regirtrez_license(self, ip_to_run, name):
        b = threading.Thread(target=self._run_registred_licenz, args=[ip_to_run, name])
        b.start()
        return True

    def mod_active(self, **kwargs):
        rsa = libs.rsa.RSAKey()
        rsa.load_key(conf.PUB)
        # data = kwargs['data']
        signature = kwargs['signature']
        my_data = json.loads(kwargs['data'])
        if my_data['uuid'] != self.uuid:
            self.log.error('uuid')
            return False
        # elif my_data['init_time'] + 86400 < time.time():
        #     self.log.error('init_time')
        #     return False
        elif datetime.datetime.strptime(my_data['end_time'], '%d.%m.%Y') < datetime.datetime.now():
            self.log.error('end_time')
            return False
        # elif my_data['work'] is False:
        #     print 'work'
        #     return False
        elif rsa.verify(kwargs['data'], signature) is False:
            self.log.error('sig %s', signature)
            return False
        else:
            # self.db.expire()
            all_ip = self.db.get_all_where(models.Device, enable=True, sas=True)
            ip_to_run = []
            for i in all_ip:
                ip_to_run.append(i.ip)
            self.run_regirtrez_license(ip_to_run, my_data['name'])
            return True
        # return False

    def get_soft_id(self, **kwargs):
        data = self.uuid
        return data

    def get_crc(self, **kwargs):
        return libs.uuid_maker.mk_crc()

    def reboot_server(self, **kwargs):
        cmd = 'sudo shutdown -r 1'
        os.system(cmd)
        return True

    # def alive(self, **kwargs):
    #     return True

    # def svn_update(self, **kwargs):
    #     client.send(evt=data[0], ip=ip, port=port, **data[1])

    # def aft_bonus(self, **kwargs):
    #     devise = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True)
    #     if devise == None:
    #         return False
    #     obj = self.db.make_obj(models.BonusInLog)
    #     obj.mashin_id = devise.id
    #     obj.mony = kwargs['mony']
    #     self.db.add_object_to_session(obj)
    #         return True
    #     else:
    #         return None

    def write_log(self, **kwargs):
        devise = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        if devise == None:
            return False
        obj = self.db.make_obj(models.GetCounterError)
        # obj.user_id = 1
        obj.mashin_nom_in_l = devise.nom_in_l
        obj.info = kwargs['msg']
        self.db.add_object_to_session(obj)
        return self.db.commit()
        # print data
        # return data

    def get_bonus_cart_to_init(self, **kwargs):
        device = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        if device == None:
            return False
        data = self.db.get_one_where(models.BonusCart, active=True, cart=kwargs['cart_id'])
        if data != None:
            return {kwargs['cart_id']:{'model': data.cart_type, 'mony': data.mony, 'no_out_befor': data.no_bonus_out_befor, 'must_have_cust': data.must_have_cust}}
        return False

    def all_event(self, evt, **kwargs):
        data = self.event[evt](**kwargs)
        return data

    def revert_current_mony(self, **kwargs):
        obj = self.db.get_one_where(models.CustInOutAFT, id=kwargs['my_id'])
        cust = self.db.get_one_where(models.CustUser, id=obj.cust_id)
        cust.curent_mony += obj.mony
        self.db.add_object_to_session(cust)
        self.db.delete_object(obj)
        return self.db.commit()

    def aft_in(self, **kwargs):
        devise = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        cust_id = kwargs['cust_id']
        mony = kwargs['mony']
        obj = self.db.make_obj(models.CustInOutAFT)
        obj.mony = mony
        obj.cust_id = cust_id
        obj.device_id = devise.id
        obj.chk = False
        obj.out = False
        self.db.add_object_to_session(obj)
        self.db.flush()
        self.db.commit()
        return obj.id

    def aft_out(self, **kwargs):
        devise = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        cust_id = kwargs['cust_id']
        mony = kwargs['mony']
        obj = self.db.make_obj(models.CustInOutAFT)
        obj.mony = mony
        obj.cust_id = cust_id
        obj.device_id = devise.id
        obj.chk = False
        obj.out = True
        self.db.add_object_to_session(obj)
        self.db.commit()
        return obj.id

    def _send_mail(self, mail, to_mail, subject=None, **kwargs):
        # conf.SEND_GMAIL = conf.CONF.get('SYSTEM', 'gmail', 'bool')
        my_mail = to_mail.split(',')
        try:
            for i in my_mail:
                # if conf.SEND_GMAIL is True:
                response = libs.sendmail.Gmail(msg=mail, to_mail=i, subject=subject)
                # else:
                #     response = libs.sendmail.sendMail(msg=mail, to_mail=i, subject=subject)
        except Exception as e:
            self.log.error(e, exc_info=True)
            response = None
        return response

    def send_mail(self, mail, to_mail, subject=None, **kwargs):
        t = threading.Thread(target=self._send_mail, args=[mail, to_mail, subject])
        t.start()
        return True

    def send_mail_won(self, **kwargs):
        if conf.MAIL_ON_WON == '':
            return False
        devise = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        time_format = libs.rtc.date_format.BG(None)
        my_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M')

        if devise != None:
            if 'cash_out' in kwargs:
                mail = u'Time: %s SMIB: %s Cash out:%s' % (my_time, devise.nom_in_l, kwargs['won'])
            else:
                mail = u'Time: %s SMIB: %s WON:%s' % (my_time, devise.nom_in_l, kwargs['won'])
            to_mail = conf.MAIL_ON_WON
            subject = conf.MAIL_ON_WON_SUBJECT
            t = threading.Thread(target=self._send_mail, args=[mail, to_mail, subject])
            t.start()
            return True
        return False

    def get_db_info(self, **kwargs):
        return {'user': conf.DB_USER,
                'pass': conf.DB_PASS,
                'port': conf.DB_PORT,
                'name': conf.DB_NAME,
                'timeout': conf.DB_TIMEOUT}

    def get_date_time(self, **kwargs):
        now = datetime.datetime.now()
        dates = '%s-%s-%s' % (now.year, now.month, now.day)
        times = '%s:%s:%s' % (now.hour, now.minute, now.second)
        return {'dates': dates, 'times': times}

    def bonus_init(self, **kwargs):
        # global bonus_init_time
        cart = self.db.get_one_where(models.BonusCart, cart=kwargs['bonus_id'])
        devise = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        if cart == None:
            return False
        if devise == None:
            return False
        # Предпазва от повторение на бонус
        # if 'bonus_init_time' in kwargs:
        #     global bonus_init_time
        #     if devise.id in bonus_init_time:
        #         if bonus_init_time[devise.id] == kwargs['bonus_init_time']:
        #             return True
        #         else:
        #             del bonus_init_time[devise.id]
        #     else:
        #         bonus_init_time[devise.id] = kwargs['bonus_init_time']
        # if devise.id not in bonus_init_time:
        if 'bonus_init_time' in kwargs:
            if devise.id not in self.bonus_init_time:
                self.bonus_init_time[devise.id] = kwargs['bonus_init_time']
            else:
                if self.bonus_init_time[devise.id] == kwargs['bonus_init_time']:
                    return True
                else:
                    self.bonus_init_time[devise.id] = kwargs['bonus_init_time']
        # else:
        #     if 'myinit_time' not in kwargs:
        #         pass
        #     elif bonus_init_time[devise.id] == kwargs['myinit_time']:
        #         return True
        #     else:
        #         bonus_init_time[devise.id] = kwargs['myinit_time']
        obj = self.db.make_obj(models.BonusCartLog)
        obj.cart_id = cart.id
        obj.mashin_id = devise.id
        obj.bonus = cart.mony
        obj.bonus_hold = kwargs['hold']
        if 'player' in kwargs:
            if kwargs['player'] != None:
                obj.cust_id = kwargs['player']
        if kwargs['hold'] is True:
            obj.credit = kwargs['credit']
        if cart.cart_type == 'x2' or cart.cart_type == 'x2_hold':
            obj.mony = cart.mony
        else:
            obj.mony = 0
        self.db.add_object_to_session(obj)
        return self.db.commit()

    def set_date_time(self, **kwargs):
        cmd = 'sudo date -s %s' % (kwargs['dates'])
        os.system(cmd)
        cmd = 'sudo date -s %s' % (kwargs['times'])
        os.system(cmd)
        if conf.RTC is True:
            libs.rtc.olimex_mod.Write_RTC()
        return True

    # def replase_bonus(self, tmp, full_total):
    #     pass
    #
    def replace_cust_group(self, tmp, full_total=None, up_dates=None, one_day_back=False, reset_group=False, **kwargs):
        if not reset_group:
            reset_group = 0
        if full_total != None:
            full_total += reset_group
        if tmp['use_group_conf'] is False:
            return tmp
        # if reset_group is True:
        #     tmp['grup'] = self.db.get_one_where(models.CustGrup, id=tmp['grup_id']).name
        # user = self.db.get_one_where(models.CustUser, id=tmp['id'])
        # tmp['activ_bonus'] = self.activ_bonus(cust_id=tmp['id'], grup=tmp['grup'])
        # tmp['last_bonus'] = self.last_bonus(cust_id=tmp['id'], grup=tmp['grup'])
        # tmp['bonus_hold'] = user.bonus_hold
        # tmp['full_total'] = full_total
        # tmp['mony_back_use'] = user.mony_back_use
        # tmp['mony_back_pr'] = user.mony_back_pr
        # tmp['tombola_use'] = user.tombola_use
        # tmp['tombola_coef'] = user.tombola_coef
        # tmp['tombola_on_in'] = user.tombola_on_in
        # tmp['no_out_befor'] = user.no_out_befor
        # tmp['bonus_use'] = user.bonus_use
        # tmp['bonus_by_in'] = user.bonus_by_in
        # tmp['bonus_direct'] = user.bonus_direct
        # tmp['bonus_one_per_day'] = user.bonus_one_per_day
        # tmp['one_day_back_total'] = user.one_day_back_total
        # tmp['mount_total'] = user.month_back
        # tmp['bonus_on_mony'] = user.bonus_on_mony
        # tmp['bonus_waith_for_in'] = user.bonus_waith_for_in
        # tmp['bonus_row'] = json.loads(user.bonus_row)
        # tmp['grup_id'] = user.grup_id
        # tmp['grup'] = user.grup.name
        # tmp['total_bonus'] = user.total_bonus
        # tmp['total_mony_back'] = user.total_mony_back
        # tmp['total_tombula'] = user.total_tombula
        # tmp['bonus_warning_use'] = user.bonus_warning_use
        # tmp['bonus_warning_mony'] = user.bonus_warning_mony
        # tmp['bonus_revert_by_bet'] = user.bonus_revert_by_bet
        # tmp['restricted_bonus'] = user.restricted_bonus
        # tmp['use_total_procent'] = user.use_total_procent
        # tmp['total_procent'] = user.total_procent
        # tmp['more_than_one_from_redirect'] = user.more_than_one_from_redirect
        # i_change = False
        replace_cust_group = self.db.get_one_where(models.Config, name='replace_cust_group')
        row_name = []
        grup_to_redirect = []
        if replace_cust_group == None:
            tmp['activ_bonus'] = self.activ_bonus(cust_id=tmp['id'], grup=tmp['grup'])
            tmp['last_bonus'] = self.last_bonus(cust_id=tmp['id'], grup=tmp['grup'])
            return tmp
        else:
            replace_cust_group = json.loads(replace_cust_group.value)
            if replace_cust_group == {}:
                tmp['activ_bonus'] = self.activ_bonus(cust_id=tmp['id'], grup=tmp['grup'])
                tmp['last_bonus'] = self.last_bonus(cust_id=tmp['id'], grup=tmp['grup'])
                return tmp
            else:
                if full_total == None:
                    for i in sorted(list(replace_cust_group.keys())):
                        # raise KeyError, (tmp['grup'], replace_cust_group[i]['from_group'])
                        if tmp['grup'] == replace_cust_group[i]['from_group']:
                            if up_dates:
                                date_now = datetime.datetime.now() + datetime.timedelta(days=1)
                            else:
                                date_now = datetime.datetime.now()
                            sm_day = datetime.date.weekday(date_now)
                            if 'total' in replace_cust_group[i]:
                                if replace_cust_group[i]['total'] is True:
                                    pass
                                else:
                                    if 'ALL' in list(replace_cust_group[i]['replace'].keys()):
                                        if replace_cust_group[i]['replace']['ALL'] is True:
                                            row_name.append(i)
                                            # i_change = True
                                            # tmp['grup'] = replace_cust_group[row_name]['to_group']
                                        elif str(sm_day) not in replace_cust_group[i]['replace']:
                                            pass
                                        else:
                                            if replace_cust_group[i]['replace'][str(sm_day)][
                                                'from_time'] <= date_now.hour and \
                                                    replace_cust_group[i]['replace'][str(sm_day)][
                                                        'to_time'] > date_now.hour:
                                                row_name.append(i)
                                                # i_change = True
                                                # tmp['grup'] = replace_cust_group[row_name]['to_group']
                                    else:
                                        if str(sm_day) not in replace_cust_group[i]['replace']:
                                            pass
                                        else:

                                            if replace_cust_group[i]['replace'][str(sm_day)][
                                                'from_time'] <= date_now.hour and \
                                                    replace_cust_group[i]['replace'][str(sm_day)][
                                                        'to_time'] > date_now.hour:
                                                row_name.append(i)
                                                # raise row_name
                                                # i_change = True
                                                # tmp['grup'] = replace_cust_group[row_name]['to_group']
                            else:
                                if 'ALL' in list(replace_cust_group[i]['replace'].keys()):
                                    if replace_cust_group[i]['replace']['ALL'] is True:
                                        row_name.append(i)
                                        # i_change = True
                                        # tmp['grup'] = replace_cust_group[row_name]['to_group']
                                    elif str(sm_day) not in replace_cust_group[i]['replace']:
                                        pass
                                    else:
                                        if replace_cust_group[i]['replace'][str(sm_day)][
                                            'from_time'] <= date_now.hour and \
                                                replace_cust_group[i]['replace'][str(sm_day)][
                                                    'to_time'] > date_now.hour:
                                            row_name.append(i)
                                            # i_change = True
                                            # tmp['grup'] = replace_cust_group[row_name]['to_group']
                                else:
                                    if str(sm_day) not in replace_cust_group[i]['replace']:
                                        pass
                                    else:
                                        if replace_cust_group[i]['replace'][str(sm_day)][
                                            'from_time'] <= date_now.hour and \
                                                replace_cust_group[i]['replace'][str(sm_day)][
                                                    'to_time'] > date_now.hour:
                                            row_name.append(i)
                                            # i_change = True
                                            # tmp['grup'] = replace_cust_group[row_name]['to_group']
                else:
                    my_mony = 0
                    for i in sorted(list(replace_cust_group.keys())):
                        grup_to_redirect.append(replace_cust_group[i]['from_group'])
                        if 'total' not in replace_cust_group[i]:
                            replace_cust_group[i]['total'] = False
                        if 'one_day_back' not in replace_cust_group[i]:
                            replace_cust_group[i]['one_day_back'] = False
                        if tmp['grup'] == replace_cust_group[i]['from_group']:
                            if replace_cust_group[i]['total'] is False:
                                pass
                            elif one_day_back != replace_cust_group[i]['one_day_back']:
                                pass
                            else:
                                if up_dates:
                                    date_now = datetime.datetime.now() + datetime.timedelta(days=1)
                                else:
                                    date_now = datetime.datetime.now()
                                sm_day = datetime.date.weekday(date_now)
                                if 'ALL' in list(replace_cust_group[i]['replace'].keys()):
                                    # raise Exception, (my_mony, replace_cust_group[i]['total_mony'])
                                    if replace_cust_group[i]['replace']['ALL'] is True and replace_cust_group[i][
                                        'total'] == True and replace_cust_group[i][
                                        'total_mony'] <= full_total and my_mony < replace_cust_group[i]['total_mony']:
                                        # raise Exception, (replace_cust_group[i]['total_mony'], full_total, i)
                                        row_name.append(i)
                                        # i_change = True
                                        my_mony = replace_cust_group[i]['total_mony']
                                        # tmp['grup'] = replace_cust_group[row_name]['to_group']
                                    elif str(sm_day) not in replace_cust_group[i]['replace']:
                                        pass
                                    else:
                                        if replace_cust_group[i]['replace'][str(sm_day)][
                                            'from_time'] <= date_now.hour and \
                                                replace_cust_group[i]['replace'][str(sm_day)][
                                                    'to_time'] > date_now.hour and replace_cust_group[i]['replace'][
                                            'ALL'] is True and replace_cust_group[i]['total'] == True and \
                                                replace_cust_group[i]['total_mony'] <= full_total and my_mony < \
                                                replace_cust_group[i]['total_mony']:
                                            row_name.append(i)
                                            # i_change = True
                                            my_mony = replace_cust_group[i]['total_mony']
                                            # tmp['grup'] = replace_cust_group[row_name]['to_group']
                                            # raise Exception, (replace_cust_group[i]['total_mony'], full_total, i)
                                else:
                                    if str(sm_day) not in replace_cust_group[i]['replace']:
                                        pass
                                    else:
                                        if replace_cust_group[i]['replace'][str(sm_day)][
                                            'from_time'] <= date_now.hour and \
                                                replace_cust_group[i]['replace'][str(sm_day)][
                                                    'to_time'] > date_now.hour and replace_cust_group[i][
                                            'total'] == True and replace_cust_group[i][
                                            'total_mony'] <= full_total and my_mony < replace_cust_group[i][
                                            'total_mony']:
                                            row_name.append(i)
                                            # i_change = True
                                            my_mony = replace_cust_group[i]['total_mony']
        self.log.info('start redirect: row_name %s full_total %s, one_day_back %s, group %s' % (
            row_name, full_total, one_day_back, tmp['grup']))
        my_row_tmp = []
        if row_name:
            for i in range(len(row_name)):
                # self.log.error('%s %s' % (i, row_name))
                new_group_conf = self.db.get_one_where(models.CustGrup,
                                                       name=replace_cust_group[row_name[i]]['to_group'])
                # self.log.error('%s %s %s' % (new_group_conf.bonus_if_man, tmp['man'], row_name[i]))
                if new_group_conf.bonus_if_man is not None:
                    if tmp['man'] != new_group_conf.bonus_if_man:
                        my_row_tmp.append(row_name[i])
                    else:
                        tmp['bonus_use'] = new_group_conf.bonus_use
                else:
                    tmp['bonus_use'] = new_group_conf.bonus_use
                if tmp['region_id']:
                    if new_group_conf.region_id:
                        if tmp['region_id'] != new_group_conf.region_id:
                            my_row_tmp.append(row_name[i])
                        else:
                            tmp['bonus_use'] = new_group_conf.bonus_use
                            tmp['group_region'] = new_group_conf.region_id
                    else:
                        tmp['bonus_use'] = new_group_conf.bonus_use
                        tmp['group_region'] = new_group_conf.region_id
                else:
                    tmp['bonus_use'] = new_group_conf.bonus_use
                    tmp['group_region'] = new_group_conf.region_id
        for i in my_row_tmp:
            if i in row_name:
                del row_name[row_name.index(i)]
        if row_name:
            row_name = row_name[-1]
        else:
            row_name = False
        # if row_name:
        #     new_group_conf = self.db.get_one_where(models.CustGrup,
        #                                            name=replace_cust_group[row_name]['to_group'])
        #     if tmp['region_id']:
        #         if new_group_conf.region_id:
        #             if tmp['region_id'] != new_group_conf.region_id:
        #                 return tmp
        #             else:
        #                 tmp['bonus_use'] = new_group_conf.bonus_use
        #         else:
        #             tmp['bonus_use'] = new_group_conf.bonus_use
        #         tmp['group_region'] = new_group_conf.region_id
        #     else:
        #         # tmp['region_id'] = new_group_conf.region_id
        #         tmp['bonus_use'] = new_group_conf.bonus_use
        #         tmp['group_region'] = new_group_conf.region_id
        #     if new_group_conf.bonus_if_man is not None:
        #         if tmp['man'] != new_group_conf.bonus_if_man:
        #             pass
        #         else:
        #             tmp['bonus_use'] = new_group_conf.bonus_use
        #     else:
        #         tmp['bonus_use'] = new_group_conf.bonus_use

        if full_total != None and row_name is False and tmp['grup'] in grup_to_redirect:
            tmp['mount_total'] = False
            tmp['one_day_back_total'] = False
            time_format = libs.rtc.date_format.BG(None)
            last_day_order = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
            end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            if last_day_order == None:
                start_time = '2010-01-01'
            else:
                start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
            get_statistic = self.db.get_all_where(models.CustStatistic, cust_id=tmp['id'],
                                                  pub_time__btw=(start_time, end_time))

            full_total = self.calc_full_total(get_statistic, tmp['group_region'])
            tmp['full_total'] = full_total
            # self.log.error('1 row_name %s full_total %s, one_day_back %s' % (
            #     row_name, full_total, one_day_back,))
        elif full_total != None and row_name is not False and tmp['grup'] in grup_to_redirect and self.activ_bonus(
                cust_id=tmp['id'], grup=replace_cust_group[row_name]['to_group']) is not False:
            tmp['mount_total'] = False
            tmp['one_day_back_total'] = False
            time_format = libs.rtc.date_format.BG(None)
            last_day_order = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
            end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            if last_day_order == None:
                start_time = '2010-01-01'
            else:
                start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
            get_statistic = self.db.get_all_where(models.CustStatistic, cust_id=tmp['id'],
                                                  pub_time__btw=(start_time, end_time))

            full_total = self.calc_full_total(get_statistic, new_group_conf.region_id)
            tmp['full_total'] = full_total
        elif full_total != None and row_name is not False and tmp['grup'] in grup_to_redirect and self.last_bonus(
                cust_id=tmp['id'], grup=replace_cust_group[row_name]['to_group']) is True:
            tmp['mount_total'] = False
            tmp['one_day_back_total'] = False
            time_format = libs.rtc.date_format.BG(None)
            last_day_order = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
            end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            if last_day_order == None:
                start_time = '2010-01-01'
            else:
                start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
            get_statistic = self.db.get_all_where(models.CustStatistic, cust_id=tmp['id'],
                                                  pub_time__btw=(start_time, end_time))

            full_total = self.calc_full_total(get_statistic, new_group_conf.region_id)
            tmp['full_total'] = full_total
            # self.log.error('2 row_name %s full_total %s, one_day_back %s' % (
            #     row_name, full_total, one_day_back,))

        if full_total is None and row_name is not False:
            tmp['grup'] = replace_cust_group[row_name]['to_group']
        elif row_name is not False and self.activ_bonus(cust_id=tmp['id'],
                                                        grup=replace_cust_group[row_name]['to_group']) is not False:
            tmp['grup'] = replace_cust_group[row_name]['to_group']
        elif row_name is not False and self.last_bonus(cust_id=tmp['id'],
                                                       grup=replace_cust_group[row_name]['to_group']) is False:
            tmp['grup'] = replace_cust_group[row_name]['to_group']
        else:
            row_name = False

        self.log.info('end redirect: row_name %s full_total %s, one_day_back %s group %s' % (
            row_name, full_total, one_day_back, tmp['grup']))

        if row_name is not False:
            new_group_conf = self.db.get_one_where(models.CustGrup, name=replace_cust_group[row_name]['to_group'])
            # if tmp['region_id']:
            #     if new_group_conf.region_id:
            #         if tmp['region_id'] != new_group_conf.region_id:
            #             return tmp
            #             # tmp['bonus_use'] = False
            #         else:
            #             tmp['bonus_use'] = new_group_conf.bonus_use
            #     else:
            #         tmp['bonus_use'] = new_group_conf.bonus_use
            # else:
            #     if new_group_conf.region_id:
            #         if tmp['region_id'] != new_group_conf.region_id:
            #             return tmp
            #             # tmp['bonus_use'] = False
            #         else:
            #             tmp['bonus_use'] = new_group_conf.bonus_use
            #     else:
            #         tmp['bonus_use'] = new_group_conf.bonus_use
            tmp['bonus_hold'] = new_group_conf.bonus_hold
            tmp['mony_back_use'] = new_group_conf.mony_back_use
            tmp['mony_back_pr'] = new_group_conf.mony_back_pr
            tmp['tombola_use'] = new_group_conf.tombola_use
            tmp['tombola_coef'] = new_group_conf.tombola_coef
            tmp['tombola_on_in'] = new_group_conf.tombola_on_in
            tmp['no_out_befor'] = new_group_conf.no_out_befor
            tmp['bonus_use'] = new_group_conf.bonus_use
            tmp['bonus_by_in'] = new_group_conf.bonus_by_in
            tmp['bonus_direct'] = new_group_conf.bonus_direct
            tmp['bonus_one_per_day'] = new_group_conf.bonus_one_per_day
            tmp['from_redirect'] = True
            tmp['region_id'] = new_group_conf.region_id
            # 'from_redirect_name':

            if full_total == None:
                tmp['one_day_back_total'] = new_group_conf.one_day_back_total
                tmp['mount_total'] = new_group_conf.month_back
                tmp['more_than_one_from_redirect'] = new_group_conf.more_than_one_from_redirect
            tmp['bonus_on_mony'] = new_group_conf.bonus_on_mony
            tmp['bonus_waith_for_in'] = new_group_conf.bonus_waith_for_in
            try:
                bonus_row = json.loads(new_group_conf.bonus_row)
            except:
                bonus_row = {}
            tmp['bonus_row'] = bonus_row
            tmp['bonus_if_man'] = new_group_conf.bonus_if_man
            # tmp['x2'] = new_group_conf.x2
            tmp['bonus_waith_for_in_mony'] = new_group_conf.bonus_waith_for_in_mony
            # tmp['bonus_row_2_mony'] = new_group_conf.bonus_row_2_mony
            # tmp['bonus_row_2_count'] = new_group_conf.bonus_row_2_count
            # tmp['bonus_row_3_mony'] = new_group_conf.bonus_row_3_mony
            # tmp['bonus_row_3_count'] = new_group_conf.bonus_row_3_count
            # tmp['bonus_row_4_mony'] = new_group_conf.bonus_row_4_mony
            # tmp['bonus_row_4_count'] = new_group_conf.bonus_row_4_count
            tmp['bonus_warning_use'] = new_group_conf.bonus_warning_use
            tmp['bonus_warning_mony'] = new_group_conf.bonus_warning_mony
            tmp['bonus_revert_by_bet'] = new_group_conf.bonus_revert_by_bet
            # if full_total != None:

            tmp['use_total_procent'] = new_group_conf.use_total_procent
            tmp['total_procent'] = new_group_conf.total_procent
            if new_group_conf.bonus_use is False:
                tmp['activ_bonus'] = False
            else:
                tmp['activ_bonus'] = self.activ_bonus(cust_id=tmp['id'], grup=tmp['grup'])
                tmp['last_bonus'] = self.last_bonus(cust_id=tmp['id'], grup=tmp['grup'])
        else:
            tmp['activ_bonus'] = self.activ_bonus(cust_id=tmp['id'], grup=tmp['grup'])
            tmp['last_bonus'] = self.last_bonus(cust_id=tmp['id'], grup=tmp['grup'])
        # self.log.critical('%s', tmp)
        return tmp

    def calc_full_total(self, statistic, region_id=False):
        full_total = 0
        if not region_id:
            for i in statistic:
                total = 0
                # self.log.info('%s', i.ins)
                total = i.ins - i.out
                # total = i['ins'] - i['out']
                if i.curent_credit > 1:
                    total -= i.curent_credit
                if i.curent_credit_on_in > 1:
                    total += i.curent_credit_on_in
                full_total += total
        else:
            for i in statistic:
                total = 0
                # self.log.info('%s', region_id==i.device.flor_id)
                if i.device.flor_id == region_id:
                    # self.log.info('%s %s %s %s' % (i.ins, i.out, i.curent_credit, i.curent_credit_on_in))
                    total = i.ins - i.out
                    # total = i['ins'] - i['out']
                    if i.curent_credit > 1:
                        total -= i.curent_credit
                    if i.curent_credit_on_in > 1:
                        total += i.curent_credit_on_in
                    # self.log.info('%s', total)
                full_total += total

        self.log.info('full_total %s', full_total)
        return full_total

    def i_get_player(self, **kwargs):
        if kwargs['my_name'] != 'term':
            self.card_is_in[kwargs['cart_id']] = kwargs['my_name']
        return True

    def _nra_thread(self, egn, user_id, ip):
        egn_valid = self.chk_nra(egn=egn)
        if egn_valid == 'ERROR':
            egn_valid = self.chk_nra(egn=egn)
        if egn_valid is True:
            self.db_direct.connect()
            cmd = 'UPDATE "Cust_user" SET in_nra=True WHERE id=%s;' % (user_id)
            self.db_direct.set(cmd)
            self.db_direct.commit()
            self.db_direct.close()
            client.send('block_nra', ip=ip, port=conf.PORT, log=self.log)
            client.send('sas.get_single_meter', command='halt', ip=ip, port=conf.PORT, log=self.log)
        elif egn_valid == 'LITLE':
            client.send('block_nra', ip=ip, port=conf.PORT, log=self.log)
            client.send('sas.get_single_meter', command='halt', ip=ip, port=conf.PORT, log=self.log)
        return

    def get_croupie_bonus_hold(self, **kwargs):
        return self.db.get_one_where(models.Config, name='bonus_cart_hold').value

    def get_client(self, reset_group=False, **kwargs):
        # global card_is_in
        # global block_all_smib_for_user
        if reset_group is False:
            reset_group = 0
            if 'del_cart' in kwargs:
                mashin = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
                if not mashin:
                    return False
            else:
                if kwargs['my_name'] != 'term':
                    mashin = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
                    if kwargs['cart_id'] in self.card_is_in:
                        return False
                    if not mashin:
                        return False
                else:
                    # pass
                    mashin = self.db.get_one_where(models.Device, enable=True, sas=True)
                    # if not mashin:
                    #     return False
                    # self.i_get_player(cart_id=kwargs['cart_id'])
                    # mashin = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
                    # if not mashin:
                    #     return False
            try:
                cart = self.db.get_one_where(models.CustCart, catr_id=kwargs['cart_id'])
            except Exception as e:
                self.log.warning(e, exc_info=True)
                return False

            if not cart:
                return False

            user = cart.user

            # if not user:
            #     return False
            if user.forbiden:
                return False

            if user.id in self.block_user:
                return False
        else:
            mashin = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
            cart = self.db.get_one_where(models.CustCart, catr_id=kwargs['cart_id'])
            user = cart.user
            # if user.one_day_back_total is True or user.month_back is True:
            #     reset_group = 0

        time_format = libs.rtc.date_format.BG(None)
        end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        last_day_order = self.db.get_one_where(models.DayReport, day_report=True, descs=True, order='id')
        if user.in_nra is False and user.personal_egn not in self.in_nra_cheked:
            a = threading.Thread(target=self._nra_thread, args=(user.personal_egn, user.id, kwargs['my_name']))
            a.start()
        #     if self.chk_nra(egn=user.personal_egn) is True:
        #         user.in_nra = True
        #         self.db.add_object_to_session(user)
        #         self.db.commit()

        full_total = 0
        if conf.OCR_UNLOCK is True:
            if user.personal_egn not in self.lk_check:
                return False
        activ_bonus = self.activ_bonus(cust_id=user.id, grup=user.grup.name)
        if user.bonus_one_per_day is True:
            down_bonus_count = 1
            last_bonus = self.last_bonus(cust_id=user.id, grup=user.grup.name)
        else:
            down_bonus_count = self.last_bonus(cust_id=user.id, count=True)
            if down_bonus_count >= 0:
                down_bonus_count = 1
            last_bonus = True
        # if user.bonus_one_per_day is True and last_bonus is True:
        #    activ_bonus = None
        rtc = libs.rtc.date_format.BG(None)
        if user.bonus_on_day == '':
            bonus_on_day = True
        else:
            # bonus_on_day = True
            bonus_on_day = json.loads(user.bonus_on_day)
            date_now = datetime.datetime.now()
            sm_day = datetime.date.weekday(date_now)
            if sm_day in bonus_on_day:
                pub_time = rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d')
                last_day_report = self.db.get_one_where(models.DayReport, day_report=True, pub_time__btw=(
                    pub_time + ' 00:00:00', rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')))
                if last_day_report == None:
                    if sm_day > 0 and sm_day - 1 in bonus_on_day:
                        bonus_on_day = True
                    elif sm_day == 0 and 6 in bonus_on_day:
                        bonus_on_day = True
                    else:
                        bonus_on_day = False
                else:
                    bonus_on_day = True
            elif sm_day > 0 and sm_day - 1 in bonus_on_day:
                pub_time = rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d')
                last_day_report = self.db.get_one_where(models.DayReport, day_report=True, pub_time__btw=(
                    pub_time + ' 00:00:00', rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')))
                if last_day_report == None:
                    bonus_on_day = True
                else:
                    bonus_on_day = False
            elif sm_day == 0 and 6 in bonus_on_day:
                pub_time = rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d')
                last_day_report = self.db.get_one_where(models.DayReport, day_report=True, pub_time__btw=(
                    pub_time + ' 00:00:00', rtc.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')))
                if last_day_report == None:
                    bonus_on_day = True
                else:
                    bonus_on_day = False
            else:
                bonus_on_day = False

        if last_day_order == None:
            start_time = '2010-01-01'
        else:
            start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
        if user.bonus_warning_use is True:
            bonus_warning_initial = self.db.get_one_where(models.BonusCartLog, pub_time__btw=(start_time, end_time),
                                                          cust_id=user.id, bonus_hold=False)
            # raise KeyError, (start_time, end_time)
            if bonus_warning_initial == None:
                bonus_warning_initial = True
            else:
                bonus_warning_initial = False
        else:
            bonus_warning_initial = False
        # print user.month_back

        try:
            bonus_row = json.loads(user.bonus_row)
        except:
            bonus_row = {}
        if user.man is None:
            try:
                egn = int(user.personal_egn)
                if len(user.personal_egn) != 10:
                    raise KeyError
                if int(user.personal_egn[8]) % 2 > 0:
                    user.man = False
                else:
                    user.man = True
            except Exception:
                user.man = True
            self.db.add_object_to_session(user)
            self.db.commit()
        bonus_if_man = user.bonus_if_man
        tmp = {
            'come_on_emg_time': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
            'last_bonus': last_bonus,
            'in_nra': user.in_nra,
            'bonus_hold': user.bonus_hold,
            'down_bonus_count': down_bonus_count,
            'activ_bonus': activ_bonus,
            'cart_id': kwargs['cart_id'],
            'id': user.id,
            'full_total': full_total,
            'name': user.name,
            'pin': user.pin,
            'curent_mony': user.curent_mony,
            'forbiden': user.forbiden,
            'use_group_conf': user.use_group_conf,
            'mony_back_use': user.mony_back_use,
            'mony_back_pr': user.mony_back_pr,
            'bonus_on_day': bonus_on_day,
            'tombola_use': user.tombola_use,
            'tombola_coef': user.tombola_coef,
            'tombola_on_in': user.tombola_on_in,
            'no_out_befor': user.no_out_befor,
            'bonus_use': user.bonus_use,
            'bonus_by_in': user.bonus_by_in,
            'bonus_direct': user.bonus_direct,
            'bonus_one_per_day': user.bonus_one_per_day,
            'one_day_back_total': user.one_day_back_total,
            'mount_total': user.month_back,
            'bonus_on_mony': user.bonus_on_mony,
            'bonus_waith_for_in': user.bonus_waith_for_in,
            'bonus_row': bonus_row,
            'bonus_waith_for_in_mony':user.bonus_waith_for_in_mony,
            # 'x2':user.x2,
            # 'bonus_row_1_count': user.bonus_row_1_count,
            # 'bonus_row_2_mony': user.bonus_row_2_mony,
            # 'bonus_row_2_count': user.bonus_row_2_count,
            # 'bonus_row_3_mony': user.bonus_row_3_mony,
            # 'bonus_row_3_count': user.bonus_row_3_count,
            # 'bonus_row_4_mony': user.bonus_row_4_mony,
            # 'bonus_row_4_count': user.bonus_row_4_count,
            'grup_id': user.grup_id,
            'grup': user.grup.name,
            'total_bonus': user.total_bonus,
            'total_mony_back': user.total_mony_back,
            'total_tombula': user.total_tombula,
            'bonus_warning_use': user.bonus_warning_use,
            'bonus_warning_mony': user.bonus_warning_mony,
            'bonus_revert_by_bet': user.bonus_revert_by_bet,
            'bonus_warning_initial': bonus_warning_initial,
            'restricted_bonus': user.restricted_bonus,
            'use_total_procent': user.use_total_procent,
            'total_procent': user.total_procent,
            'from_redirect': False,
            'more_than_one_from_redirect': user.more_than_one_from_redirect,
            'region_id': mashin.flor_id,
            'group_region': user.region_id,
            'mony_back_min_pay': user.mony_back_min_pay,
            'mony_back_pay':user.mony_back_pay,
            'bonus_if_man': bonus_if_man,
            'man': user.man,
            # 'from_redirect_name':
        }
        if tmp['bonus_if_man'] != None:
            if tmp['bonus_if_man'] != user.man:
                tmp['bonus_use'] = False
        # if tmp['group_region']:
        #     if mashin.flor_id != tmp['group_region']:
        #         tmp['bonus_use'] = False
        tmp['full_total'] = full_total
        if user.one_day_back_total is False and user.month_back is False:
            tmp = self.replace_cust_group(tmp, reset_group=reset_group)
        else:
            tmp = self.replace_cust_group(tmp)
        # print tmp['mount_total']
        # raise Exception, tmp
        # self.log.error('bonus_one_per_day %s', tmp['bonus_one_per_day'])
        if tmp['bonus_one_per_day'] is True:
            if tmp['one_day_back_total'] is False and tmp['mount_total'] is False:
                end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                if last_day_order == None:
                    start_time = '2010-01-01'
                else:
                    start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
                get_statistic = self.db.get_all_where(models.CustStatistic, cust_id=user.id,
                                                      pub_time__btw=(start_time, end_time))

                full_total = self.calc_full_total(get_statistic, tmp['group_region'])
            elif tmp['one_day_back_total'] is True:
                date_from_statistic = self.db.get_one_where(models.CustStatistic, cust_id=user.id,
                                                            pub_time__lte=time_format.date_to_str(
                                                                last_day_order.pub_time, '%Y-%m-%d %H:%M:%S'),
                                                            descs=True, order='pub_time')
                if date_from_statistic != None:
                    date_from_statistic = time_format.date_to_str(
                        date_from_statistic.pub_time + datetime.timedelta(seconds=1), '%Y-%m-%d %H:%M:%S')
                    last_day_order_new = self.db.get_one_where(models.DayReport, pub_time__lte=date_from_statistic,
                                                               day_report=True, descs=True, order='id')

                    if last_day_order_new == None:
                        end_time = date_from_statistic
                        start_time = '2010-01-01'
                    else:
                        end_time = date_from_statistic
                        start_time = time_format.date_to_str(last_day_order_new.pub_time, '%Y-%m-%d %H:%M:%S')
                else:
                    start_time = time_format.date_to_str(last_day_order.pub_time - datetime.timedelta(days=1),
                                                         '%Y-%m-%d')
                    if last_day_order == None:
                        end_time = '2010-01-01'
                    else:
                        end_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
                self.log.info('start_time: %s, end_time: %s' % (start_time, end_time))
                get_statistic = self.db.get_all_where(models.CustStatistic, cust_id=user.id,
                                                      pub_time__btw=(start_time, end_time))

                full_total = self.calc_full_total(get_statistic, tmp['group_region'])
                # raise KeyError
                #
            elif tmp['mount_total'] is True:
                last_mounth = self.db.get_one_where(models.DayReport, day_report=False, descs=True, order='id')
                if last_mounth != None:
                    start_time = time_format.date_to_str(last_mounth.pub_time, '%Y-%m-%d %H:%M:%S')
                else:
                    start_time = '2010-01-01'
                if last_day_order == None:
                    end_time = '2010-01-01'
                else:
                    end_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
                self.log.info('start_time: %s, end_time: %s' % (start_time, end_time))
                get_statistic = self.db.get_all_where(models.CustStatistic, cust_id=user.id,
                                                      pub_time__btw=(start_time, end_time))

                full_total = self.calc_full_total(get_statistic, tmp['group_region'])
            else:
                end_time = time_format.date_to_str(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                if last_day_order == None:
                    start_time = '2010-01-01'
                else:
                    start_time = time_format.date_to_str(last_day_order.pub_time, '%Y-%m-%d %H:%M:%S')
                self.log.info('start_time: %s, end_time: %s' % (start_time, end_time))
                get_statistic = self.db.get_all_where(models.CustStatistic, cust_id=user.id,
                                                      pub_time__btw=(start_time, end_time))

                full_total = self.calc_full_total(get_statistic, tmp['group_region'])
        else:
            full_total = 0
        tmp['full_total'] = full_total

        # self.log.info('%s %s %s' % (tmp['bonus_one_per_day'], tmp['one_day_back_total'] , full_total))
        # if tmp['bonus_one_per_day'] is True:
        # FIXME: Редирект по предходен и текъщ тотал
        my_group = tmp['grup']
        if tmp['mount_total'] is True or tmp['one_day_back_total'] is True and tmp['bonus_one_per_day'] is True:
            tmp = self.replace_cust_group(tmp, full_total, one_day_back=False)
        if my_group == tmp['grup'] and tmp['bonus_one_per_day'] is True:
            tmp = self.replace_cust_group(tmp, tmp['full_total'], one_day_back=True, reset_group=reset_group)
        if tmp['use_total_procent'] is True and tmp['full_total'] > 0 and tmp['bonus_one_per_day'] is True:
            total_procent = tmp['total_procent'] * 0.01
            bonus = int(round(tmp['full_total'] * total_procent, 0))
            tmp['bonus_row'] = {"{:.2f}".format(bonus): 10}
        else:
            tmp['mount_total'] = False
            tmp['one_day_back_total'] = False
        if tmp['group_region']:
            if mashin.flor_id != tmp['group_region']:
                tmp['bonus_use'] = False
        if tmp['bonus_if_man'] != None:
            if tmp['bonus_if_man'] != user.man:
                tmp['bonus_use'] = False

        self.log.info('tmp: %s', tmp)
        if len(tmp['bonus_row']) < 1:
            tmp['bonus_use'] = False

        return tmp

    def clean_all_bonus(self, **kwargs):
        data = self.db.get_all_where(models.BonusPay, cust_id=kwargs['cust_id'], activ=True)
        commit = False
        for i in data:
            commit = True
            i.activ = False
            i.use_it = False
            i.last = True
            self.db.add_object_to_session(i)
        if commit is True:
            return self.db.commit()
        else:
            return True

    def open_in_other_device_bonus(self, **kwargs):
        if 'count' != kwargs:
            user = self.db.get_one_where(models.CustUser, id=kwargs['cust_id'])
            if user.more_than_one_from_redirect is True:
                data = self.db.get_all_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'], activ=False, from_redirect_name=kwargs['grup'])
            else:
                data = self.db.get_all_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'], activ=False, from_redirect_name=kwargs['grup'])
            if data == []:
                return False
            # elif len(data) <= 1:
            #     return False
            return True
        else:
            data = self.db.get_all_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'], activ=False)
            if data == []:
                return 1
            return len(data)

    # def open_in_other_device_bonus(self, **kwargs):
    #     device = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True)
    #     if 'count' not in kwargs:
    #         data = self.db.get_all_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'])
    #         var = False
    #         for i in data:
    #             if i.device_id!=device.id:
    #                 var = True
    #         # if data == None:
    #         #     return False
    #         # elif data.device_id == device.id:
    #         #     return False
    #         return var
    #     else:
    #         data = self.db.get_all_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'])
    #         if data == []:
    #             return 1
    #         elif data.device_id == device.id:
    #             return len(data)-1
    #         return len(data)

    def last_bonus(self, **kwargs):
        if 'count' != kwargs:
            user = self.db.get_one_where(models.CustUser, id=kwargs['cust_id'])
            if user.more_than_one_from_redirect is True and 'grup' in kwargs:
                data = self.db.get_one_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'], from_redirect_name=kwargs['grup'])
            else:
                if 'grup' in kwargs:
                    data = self.db.get_one_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'], from_redirect_name=kwargs['grup'])
                else:
                    data = self.db.get_one_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'])
                tmp = self.db.get_one_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'], use_it=True)
                if tmp:
                    return True
                # elif 'grup' in kwargs:
                #     return False
            if data == None:
                return False
            return True
        else:
            data = self.db.get_all_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'])
            if data == None:
                return 1
            return len(data)

    def hold_client_cart_bonus(self, **kwargs):
        # global client_hold_bonus
        device = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        if device == None:
            return False
        if 'hold_init_time' in kwargs:
            if device.id not in self.client_hold_bonus:
                self.client_hold_bonus[device.id] = kwargs['hold_init_time']
            elif self.client_hold_bonus[device.id] == kwargs['hold_init_time']:
                return True
            else:
                self.client_hold_bonus[device.id] = kwargs['hold_init_time']
        obj = self.db.make_obj(models.ClienBonusHold)
        obj.mony = kwargs['mony']
        obj.bonus_hold = True
        obj.cart_id = kwargs['cust_id']
        obj.credit = kwargs['credit']
        obj.mashin_id = device.id
        obj.chk = False
        if 'bonus' in kwargs:
            obj.bonus = kwargs['bonus']
        else:
            obj.mony = kwargs['mony']
        self.db.add_object_to_session(obj)
        return self.db.commit()


    def activ_bonus(self, **kwargs):
        user = self.db.get_one_where(models.CustUser, id=kwargs['cust_id'])
        # print user.more_than_one_from_redirect
        if user.more_than_one_from_redirect is True:
            data = self.db.get_one_where(models.BonusPay, activ=True, cust_id=kwargs['cust_id'], from_redirect_name=kwargs['grup'])
            if data == None:
                return False
        else:
            data = self.db.get_one_where(models.BonusPay, activ=True, cust_id=kwargs['cust_id'], from_redirect_name=kwargs['grup'])
            if data == None:
                return False
            # if 'grup' in kwargs:
            #     if data.from_redirect_name != kwargs['grup'] and data.from_redirect_name is not None:
            #         if data.activ == True:
            #             data.last = False
            #             data.use_it = False
            #             data.activ = False
            #         self.db.add_object_to_session(data)
            #         self.db.commit()
            #         return False
        data = {'id': data.id, 'mony': data.mony}
        return data

    def activ_bonus_update_mony(self, **kwargs):
        data = self.db.get_one_where(models.BonusPay, activ=True, id=kwargs['bonus_id'])
        # self.db.expire(data)
        device = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        if data == None:
            return False
        if device == None:
            return False
        data.mony = kwargs['mony']
        data.device_id = device.id
        self.db.add_object_to_session(data)
        self.db.commit()
        return data.id
        #     return True
        # else:
        #     return None

    def activ_bonus_update(self, **kwargs):
        # global block_all_smib_for_user
        data = self.db.get_one_where(models.BonusPay, id=kwargs['bonus_id'])
        # try:
        #     del block_all_smib_for_user[block_all_smib_for_user.index(data.cust_id)]
        # except ValueError:
        #     pass
        device = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        if data == None:
            return False
        elif device == None:
            return False
        else:
            if data.cust.more_than_one_from_redirect is False:
                all = self.db.get_all_where(models.BonusPay, cust_id=data.cust_id, activ=True, use_it=False)
                for i in all:
                    if i.id != data.id:
                        i.use_it = False
                        i.activ = False
                        self.db.add_object_to_session(i)

            data.activ = False
            data.use_it = True
            # if data.device_id != device.id:
            #     data.initial_on_device_id = data.device_id
            # data.initial_pub_time = data.pub_time
            data.pub_time = datetime.datetime.now()
            data.device_id = device.id
            self.db.add_object_to_session(data)

            my_data = self.db.commit()
            # if 'clean_all' in kwargs:
            #     if kwargs['clean_all'] is True:
            #         try:
            #             return self.clean_all_bonus(cust_id=data.cust_id)
            #         except Exception as e:
            #             self.log.error(e, exc_info=True)
            return my_data

    def client_want_bonus(self, **kwargs):
        # global client_bonus_init_time
        # card_is_in[kwargs['cust_id']] = True
        if 'bonus_one_per_day' in kwargs:
            if kwargs['bonus_one_per_day'] is True:
                data = self.db.get_all_where(models.BonusPay, last=True, cust_id=kwargs['cust_id'],
                                     from_redirect_name=kwargs['goup'])
                if data:
                    return False
        device = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        if device == None:
            return False
        if 'my_init_time' in kwargs:
            if device.id not in self.client_bonus_init_time:
                self.client_bonus_init_time[device.id] = [kwargs['my_init_time'], ]
            else:
                if self.client_bonus_init_time[device.id][0] == kwargs['my_init_time']:
                    return self.client_bonus_init_time[device.id][1]
                else:
                    self.client_bonus_init_time[device.id] = [kwargs['my_init_time']]
        obj = self.db.make_obj(models.BonusPay)
        obj.initial_on_device_id = device.id
        obj.initial_pub_time = datetime.datetime.now()
        obj.cust_id = kwargs['cust_id']
        obj.device_id = device.id
        obj.use_it = False
        obj.mony = kwargs['mony']
        if 'from_redirect' in kwargs:
            obj.from_redirect = kwargs['from_redirect']
        if 'goup' in kwargs:
            obj.from_redirect_name = kwargs['goup']
        obj.from_in = kwargs['from_in']
        obj.chk = False
        self.db.add_object_to_session(obj)
        self.db.commit()
        self.client_bonus_init_time[device.id].append(obj.id)
        return obj.id

    def set_client(self, **kwargs):
        # global card_is_in

        # global block_all_smib_for_user
        player = kwargs['player']
        # if player['bonus_one_per_day'] is True:
        #     data = self.db.get_all_where(models.BonusPay, last=True, cust_id=player['id'],
        #                           from_redirect_name=player['grup'])
        #     if len(data) > 1:
        #         for i in data[1:]:
        #             if i.activ is True:
        #                 i.activ = False
        #                 i.use_it = False
        #                 self.db.add_object_to_session(i)

        # try:
        #     del block_all_smib_for_user[block_all_smib_for_user.index(player['id'])]
        # except ValueError:
        #     pass
        # print player['cart'], self.card_is_in
        #
        mashin = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        user = self.db.get_one_where(models.CustUser, id=player['id'])
        if user != None and mashin != None:
            if None in player['new_meter']:
                self.log.warning('no new_meter')
                return False
            if None in player['old_meter']:
                self.log.warning('no old_meter')
                return False
            # Предпазва от повторен запис
            if 'come_on_emg_time' in player:
                get_statistic = self.db.get_one_where(models.CustStatistic, cust_id=player['id'], come_on_emg_time=player['come_on_emg_time'] )
                if get_statistic != None:
                    try:
                        del self.card_is_in[kwargs['player']['cart_id']]
                    except KeyError:
                        pass
                    return True
            if player['mony_back_use'] is True:
                user.total_mony_back += round(
                    (player['new_meter']['bet'] - player['old_meter']['bet']) * player['mony_back_pr'], 2)
                if user.total_mony_back > user.mony_back_min_pay and user.mony_back_min_pay > 0:
                    user.total_mony_back = user.mony_back_min_pay
                user.total_mony_back = round(user.total_mony_back, 2)
            if player['tombola_use'] is True:
                if player['tombola_on_in'] is True:
                    user.total_tombula += round(
                        ((player['new_meter']['in'] - player['old_meter']['in']) * player['tombola_coef']) * 0.01, 2)
                else:
                    user.total_tombula += round(
                        ((player['new_meter']['bet'] - player['old_meter']['bet']) * player['tombola_coef']) * 0.01, 2)
            statistic = self.db.make_obj(models.CustStatistic)
            statistic.ins = round(player['new_meter']['in'] - player['old_meter']['in'], 2)
            statistic.out = round(player['new_meter']['out'] - player['old_meter']['out'], 2)
            statistic.won = round(player['new_meter']['won'] - player['old_meter']['won'], 2)
            statistic.bill = player['new_meter']['bill'] - player['old_meter']['bill']
            statistic.game_played = player['new_meter']['games played'] - player['old_meter']['games played']
            statistic.cust_id = user.id
            statistic.device_id = mashin.id
            statistic.curent_credit = player['new_meter']['curent credit']
            statistic.bet = round(player['new_meter']['bet'] - player['old_meter']['bet'], 2)
            statistic.curent_credit_on_in = player['old_meter']['curent credit']
            if self.day_reset_player != False:
                if player['come_on_emg_time'] < self.day_reset_player:
                    statistic.pub_time = self.day_reset_player
                    statistic.curent_credit_on_in = 0
                    statistic.curent_credit = 0
                else:
                    statistic.curent_credit_on_in = player['old_meter']['curent credit']
                    statistic.curent_credit = player['new_meter']['curent credit']
            else:
                statistic.curent_credit_on_in = player['old_meter']['curent credit']
                statistic.curent_credit = player['new_meter']['curent credit']
            #     else:
            #         statistic.come_on_emg_time = player['come_on_emg_time']
            # else:
            #     statistic.come_on_emg_time = player['come_on_emg_time']
            # if 'end_date' in kwargs:
            #     if kwargs['end_date'] is not False:
            #         statistic.pub_time = kwargs['end_date']
            if 'come_on_emg_time' in player:
                statistic.come_on_emg_time = player['come_on_emg_time']

            if statistic.bet >= 0:

                if user.mony_back_use is True:
                    statistic.total_mony_back = round(
                        (player['new_meter']['bet'] - player['old_meter']['bet']) * user.mony_back_pr, 2)
                if user.tombola_use is True and player['tombola_on_in'] is False:
                    statistic.total_tombula = round(
                        ((player['new_meter']['bet'] - player['old_meter']['bet']) * user.tombola_coef) * 0.01, 2)
                elif user.tombola_use is True and player['tombola_on_in'] is True:
                    ins = player['new_meter']['in'] - player['old_meter']['in']
                    out = player['new_meter']['out'] - player['old_meter']['out']
                    total = ins - out
                    if ins > 0:
                        statistic.total_tombula = round(
                        (total * user.tombola_coef) * 0.01, 2)
            else:
                statistic.bet = 0
            try:
                self.db.add_object_to_session(user)
                self.db.add_object_to_session(statistic)
                self.db.commit()
                if 'del_cart' in kwargs:
                    pass
                else:
                    try:
                        del self.card_is_in[kwargs['player']['cart_id']]
                    except KeyError:
                        pass
                return True
            except Exception as e:
                # self.db.rollback()
                raise e
        return False

    def write_in_out(self, **kwargs):
        mashin = self.db.get_one_where(models.Device, ip=kwargs['my_name'], enable=True, sas=True)
        if mashin == None:
            return True
        if kwargs['ins'] > 0:
            obj = self.db.make_obj(models.InOut)
            obj.device_id = mashin.id
            if kwargs['ins'] > 0:
                obj.mony = kwargs['ins']
                obj.out = False
                if kwargs['bill'] > 0:
                    obj.bill = True
                else:
                    obj.bill = False
            if kwargs['player']:
                obj.player_id = kwargs['player']
            self.db.add_object_to_session(obj)
        if kwargs['out'] > 0:
            obj2 = self.db.make_obj(models.InOut)
            obj2.device_id = mashin.id
            obj2.mony = kwargs['out']
            obj2.out = True
            obj2.bill = False
            if kwargs['player']:
                obj2.player_id = kwargs['player']
            self.db.add_object_to_session(obj2)
        return self.db.commit()
        # return True

    def get_cpu_time(self, **kwargs):
        return time.time()

    # def get_mony_from_cart(self, **kwargs):
    #     user = self.db.get_one_where(models.CustUser, id=kwargs['cust_id'])
    #     # if not cart:
    #     #     return False
    #     # user = cart.user
    #     if not user:
    #         return False
    #     if user.forbiden:
    #         return False
    #     # mony = user.curent_mony
    #     user.curent_mony = kwargs['mony']
    #     self.db.add_object_to_session(user)
    #     return True

    def run(self):
        user = self.db.get_all(models.User)
        for i in user:
            i.login = False
            self.db.add_object_to_session(i)
        self.db.commit()
        # for i in self.pipe:
        #     while i.poll(0.5):
        #         i.recv()
                # i.send(None)
        # all_dev = self.db.get_all_where(models.Device, enable=True, sas=True)
        # for i in all_dev:
        #     # for b in range(3):
        #     client.send('soft_reboot', ip=i.ip, port=conf.PORT, log=self.log, timeout=0)
        while True:
            try:
                for i in self.pipe:
                    if i.poll(0.2):
                        data = i.recv()
                        # print data
                        try:
                            if data[2]+(conf.TIMEOUT_2-6) >= time.time():
                                if 'my_name' not in data[1] or 'my_init_time' not in data[1]:
                                    response = self.all_event(data[0], **data[1]), data
                                elif data[1]['my_name'] not in self.my_init_time:
                                    response = self.all_event(data[0], **data[1]), data
                                    self.my_init_time[data[1]['my_name']] = {}
                                    self.my_init_time[data[1]['my_name']][data[0]] = [data[1]['my_init_time'], response[0]]
                                else:
                                    if data[0] in self.my_init_time[data[1]['my_name']]:
                                        if data[1]['my_init_time'] == self.my_init_time[data[1]['my_name']][data[0]][0]:
                                            response = self.my_init_time[data[1]['my_name']][data[0]][1], data
                                            self.log.warning('old request')
                                        else:
                                            response = self.all_event(data[0], **data[1]), data
                                            self.my_init_time[data[1]['my_name']][data[0]] = [data[1]['my_init_time'], response[0]]
                                    else:
                                        response = self.all_event(data[0], **data[1]), data
                                        self.my_init_time[data[1]['my_name']][data[0]] = [data[1]['my_init_time'],response[0]]
                                self.log.debug('%s', self.all_event)
                                i.send(response)
                            else:
                                response = None
                                i.send(response)
                                while i.poll():
                                    i.recv()
                        except Exception as e:
                            self.log.error(e, exc_info=True)
                            self.log.error(data)
                            response = None

                            try:
                                self.db.rollback()
                            except Exception as e:
                                self.log.critical(e, exc_info=True)
                            while i.poll():
                                i.recv()

            except Exception as e:
                self.log.critical(e, exc_info=True)
                # try:
                #     self.db.rollback()
                # except:
                #     self.log.critical(e, exc_info=True)
