# -*- coding:utf-8 -*-
'''
Created on 23.06.2017 г.

@author: dedal
'''
import time
from threading import *
import wx
import libs
import datetime
from queue import Empty
# import db_ctrl
# import mashin
# import mony

COUNTER_GET = wx.NewId()
COUNTER_GET_RUN = wx.NewId()
COUNTER_GET_STOP = wx.NewId()

GUAGE_GET = wx.NewId()

BILL_GET = wx.NewId()
BILL_GET_RUN = wx.NewId()
BILL_GET_STOP = wx.NewId()


def EVT_BILL_GET(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, BILL_GET, func)


class GetBill(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(BILL_GET)
        self.data = data


class BillInfo(Thread):
    """Worker Thread Class."""

    def __init__(self, notify_window, mashin):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self.mashin = mashin
        # libs.DB.expire()
        self.start()

    def run(self):
        bill = None
        for item in self.mashin:
            libs.DB.expire(item)
            if item.sas is True:
                for i in range(3):
                    bill = libs.udp.send('sas.get_single_meter', command='bill', ip=item.ip)
                    # print bill, item.ip
                    if bill != None and bill >=0 and bill is not False:
                        break
                if bill != None and bill >=0 and bill is not False:
                    item.bill_mony = item.bill_in_device + round(bill - item.bill)
                    if item.bill_mony == 0:
                        item.bill_get = False
                else:
                    item.bill_get = None
                if self._want_abort:
                    break

            else:
                item.bill_mony = item.bill_in_device
            if not self._want_abort:
                if bill != None:
                    wx.PostEvent(self._notify_window, GetBill(item.nom_in_l))
                elif bill == None:
                    wx.PostEvent(self._notify_window, GetBill({'ERROR':item.nom_in_l}))
                bill = None
            else:
                break
        if not self._want_abort:
            mashin = self.mashin
            try:
                wx.PostEvent(self._notify_window, GetBill(mashin))
            except:
                pass

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1


class BillGet(Thread):
    """Worker Thread Class."""

    def __init__(self, notify_window, mashin, user):
        """Init Worker Thread Class."""
        self.db = libs.models.DBCtrl()
        # self.db.expire()
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        #         self.mashin = mashin
        self.user = user
        self.mashin = []
        for i in mashin:
            self.mashin.append(self.db.get_one_where(libs.models.Device, id=i.id))
        self.start()

    def run(self):
        error = []
        bill = None
        user_kasa = 0
        for item in self.mashin:
            bill = None
            self.db.expire(item)
            if item.sas is True:
                if item.bill_get is True:
                    for i in range(3):
                        try:
                            bill = libs.udp.send('sas.get_single_meter', command='bill', ip=item.ip)
                            if bill != None and bill >=0 and bill is not False:
                                break
                        except Exception as e:
                            libs.log.stderr_logger.critical(e, exc_info=True)
                            print(e)
                            bill = None
                    if bill != None and bill >=0 and bill is not False:
                        ords = libs.DB.make_obj(libs.models.Order)
                        ords.mashin_id = item.id
                        ords.flor_id = item.flor_id
                        ords.old_enter = item.el_in
                        ords.new_enter = item.el_in
                        ords.old_exit = item.el_out
                        ords.new_exit = item.el_out
                        ords.mex_old_enter = item.mex_in
                        ords.mex_new_enter = item.mex_in
                        ords.mex_old_exit = item.mex_out
                        ords.mex_new_exit = item.mex_out
                        ords.bill_old = item.bill
                        ords.bill_new = bill
                        ords.user_id = self.user.id
                        ords.old_won = item.won
                        ords.new_won = item.won
                        ords.old_bet = item.bet
                        ords.new_bet = item.bet

                        obj = self.db.make_obj(libs.models.BillTake)
                        obj.user_id = self.user.id
                        obj.mashin_id = item.id

                        obj.mony = item.bill_in_device + (bill - item.bill)
                        user_kasa = user_kasa - (bill - item.bill)
                        user_kasa += obj.mony
                        item.bill_in_device = 0
                        item.bill = bill

                        self.db.add_object_to_session(obj)
                        self.db.add_object_to_session(item)
                        # self.db.add_object_to_session(self.user)
                        libs.DB.add_object_to_session(ords)

                        if self.user.grup.bill_disable is True:
                            unlock_bill = libs.udp.send('sas.get_single_meter', ip=item.ip,
                                                        command='start bill')
                            if unlock_bill is not True:
                                cant_unlock = libs.DB.make_obj(libs.models.GetCounterError)
                                cant_unlock.user_id = self.user.id
                                cant_unlock.mashin_nom_in_l = item.nom_in_l
                                cant_unlock.info = u'BILL NOT START'
                                libs.DB.add_object_to_session(cant_unlock)
                        try:
                            self.db.flush()
                            wx.PostEvent(self._notify_window, GetBill(item.nom_in_l))
                        except:
                            pass
                    else:
                        error.append(item.nom_in_l)
                        obj = self.db.make_obj(libs.models.GetCounterError)
                        obj.user_id = self.user.id
                        obj.mashin_nom_in_l = item.nom_in_l
                        obj.info = u'NO SMIB CONNECTION IN ORDER'
                        self.db.add_object_to_session(obj)
                        try:
                            wx.PostEvent(self._notify_window, GetBill({'ERROR':item.nom_in_l}))
                        except:
                            pass
            if self._want_abort:
                break
            try:
                self.db.flush()
            except Exception as e:
                self.db.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                self.abort()
                break


        if self._want_abort:
            self.db.rollback()
            user_kasa = 0
            cant_unlock = libs.DB.make_obj(libs.models.GetCounterError)
            cant_unlock.user_id = self.user.id
            cant_unlock.info = u'BILL GET BREAK'
            libs.DB.add_object_to_session(cant_unlock)
            try:
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
        else:
            self.db.expire(self.user)
            self.user.kasa += user_kasa
            self.db.add_object_to_session(self.user)
            try:
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                try:
                    wx.PostEvent(self._notify_window, GetBill('ERROR'))
                except:
                    pass
                return
            try:
                wx.PostEvent(self._notify_window, GetBill('DONE'))
            except:
                pass


    def abort(self):
        """abort worker thread."""
        self._want_abort = 1


def EVT_GUAGE_GET(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, COUNTER_GET, func)


class GetGuage(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(GUAGE_GET)
        self.data = data


def EVT_COUNTER_GET(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, COUNTER_GET, func)


class GetCounter(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(COUNTER_GET)
        self.data = data


def mk_left_revert(mashins, counter):
    revert_index = 100000000
    #     print mashins.won, type(counter)
    while mashins.won > counter['won']:
        counter['won'] = counter['won'] + revert_index
    while mashins.bet > counter['bet']:
        counter['bet'] = counter['bet'] + revert_index
    while mashins.el_in > counter['in']:
        counter['in'] = counter['in'] + revert_index
    while mashins.el_out > counter['out']:
        counter['out'] = counter['out'] + revert_index
    return counter


def mk_right_revert(mashins, counter):
    while mashins.won > counter['won']:
        add_val = '0'
        counter['won'] = str(counter['won']) + add_val
        counter['won'] = int(counter['won'])
        add_val = add_val + '0'
    while mashins.bet > counter['bet']:
        add_val = '0'
        counter['bet'] = str(counter['bet']) + add_val
        counter['bet'] = int(counter['bet'])
        add_val = add_val + '0'
    while mashins.el_in > counter['in']:
        add_val = '0'
        counter['in'] = str(counter['in']) + add_val
        counter['in'] = int(counter['in'])
        add_val = add_val + '0'
    while mashins.el_out > counter['out']:
        #         revert_index = 0.1
        add_val = '0'
        counter['out'] = str(counter['out']) + add_val
        counter['out'] = int(counter['out'])
        add_val = add_val + '0'
    # revert_index = revert_index / 0.01
    return counter


class BillStart(Thread):
    def __init__(self, notify_window, mashin, user):
        Thread.__init__(self)
        #         self.mashin = mashin
        self._want_abort = 0
        self._notify_window = notify_window
        self.db = libs.models.DBCtrl()
        self.user = user
        self.mashin = mashin
        # self.db.expire()
        self.start()

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1

    def run(self):
        bill_start = None
        # libs.conf.LOCK.acquire()
        for item in self.mashin:
            bill_start = None
            for i in range(3):
                bill_start = libs.udp.send(libs.smib.SAS_F_METER_SINGLE, ip=item.ip, command=libs.smib.SAS_C_SINGLE_BILL_START)
                if bill_start is True:
                    break
            if bill_start == None and self.user.grup.bill_disable is True:
                obj = self.db.make_obj(libs.models.GetCounterError)
                obj.user_id = self.user.id
                obj.mashin_nom_in_l = item.nom_in_l
                obj.info = u'NO START BILL'
                self.db.add_object_to_session(obj)
            if self._want_abort:
                break
            else:
                try:
                    wx.PostEvent(self._notify_window, GetBill(item.nom_in_l))
                except Exception as e:
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
        try:
            self.db.commit()
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
        if not self._want_abort:
            try:
                wx.PostEvent(self._notify_window, GetBill('DONE'))
            except:
                pass


class CounterInfo(Thread):
    """Worker Thread Class."""

    def __init__(self, notify_window, mashin, user, cart):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.cart = cart
        self._notify_window = notify_window
        self._want_abort = 0
        self.mashin = mashin
        self.error = []
        self.db = libs.models.DBCtrl()
        self.user = user
        self.start()

    def run(self):
        """Run Worker Thread."""
        bonus_hold = self.db.get_one_where(libs.models.Config, name='bonus_cart_hold').value
        user_kasa = 0
        for item in self.mashin:
            counter = None
            bill = None
            for i in range(3):
                counter = libs.udp.send('sas.order', ip=item.ip, bill_block=self.user.grup.bill_disable)
                if counter != None:
                    try:
                        if None not in list(counter.values()):
                            bill = counter['bill']
                            break
                    except TypeError:
                        counter = None
                    except Exception as e:
                        libs.log.stderr_logger.critical(e, exc_info=True)
                        print(e)
                        counter = None
            self.db.expire(item)
            in_out_on_device = self.db.get_all_where(libs.models.InOut, user_id=None, device_id=item.id)
            for i in in_out_on_device:
                i.user_id = self.user.id
                self.db.add_object_to_session(i)
            bonus_cart = self.db.get_all_where(libs.models.BonusCartLog, mashin_id=item.id, user_id=None)
            row2 = libs.DB.get_all_where(libs.models.ClienBonusHold, user_id=None, mashin_id=item.id)
            for i in row2:
                i.user_id = self.user.id
                if i.pub_time.year <= 2010:
                    i.pub_time = datetime.datetime.now()
                if bonus_hold == 'True':
                    user_kasa = user_kasa + i.bonus
                self.db.add_object_to_session(i)
            for i in bonus_cart:
                i.user_id = self.user.id
                if i.pub_time.year <= 2010:
                    i.pub_time = datetime.datetime.now()

                if i.bonus_hold is True and bonus_hold == 'True':
                    user_kasa += i.bonus
                else:
                    if i.bonus_hold is False:
                        if i.cart.cart_type != 'restricted':
                            user_kasa += i.mony
                        else:
                            user_kasa -= i.bonus
                self.db.add_object_to_session(i)
            aft_in_out = self.db.get_all_where(libs.models.CustInOutAFT, device_id=item.id, user_id=None)
            for i in aft_in_out:
                i.user_id = self.user.id
                if i.pub_time.year <= 2010:
                    i.pub_time = datetime.datetime.now()
                if i.out is False:
                    user_kasa = user_kasa - i.mony
                else:
                    user_kasa = user_kasa + i.mony
                self.db.add_object_to_session(i)
            restricted_bonus = self.db.get_all_where(libs.models.BonusPay, device_id=item.id, user_id=None)
            for i in restricted_bonus:
                i.user_id = self.user.id
                if i.pub_time.year <= 2010:
                    i.pub_time = datetime.datetime.now()
                if i.from_in is True and i.activ is False:
                    user_kasa -= i.mony
                self.db.add_object_to_session(i)


            if counter != None and bill != None:
                if counter['bill_block'] is False:
                    obj = self.db.make_obj(libs.models.GetCounterError)
                    obj.user_id = self.user.id
                    obj.mashin_nom_in_l = item.nom_in_l
                    obj.info = u'NO STOP BILL'
                    self.db.add_object_to_session(obj)

                if item.by_hend_order is True:
                    wx.PostEvent(self._notify_window, GetCounter('ORDER BYHAND: %s' % (item.nom_in_l)))
                    self.error.append(item.nom_in_l)
                else:
                    if item.mk_revert is False:
                        counter = mk_left_revert(item, counter)
                    else:
                        counter = mk_right_revert(item, counter)

                    if self._want_abort:
                        break

                    total = round((counter['in'] - item.el_in) * item.el_coef, 2) - round((counter['out'] - item.el_out) * item.el_coef, 2)
                    mony_in_user = user_kasa + total
                    ords = self.db.make_obj(libs.models.Order)
                    ords.mashin_id = item.id
                    ords.flor_id = item.flor_id
                    ords.old_enter = item.el_in
                    ords.new_enter = counter['in']
                    ords.old_exit = item.el_out
                    ords.new_exit = counter['out']
                    ords.mex_old_enter = item.mex_in
                    ords.mex_old_exit = item.mex_out

                    m_in = int(counter['in'] - item.el_in) * item.el_coef
                    m_in = item.mex_in + m_in * item.mex_coef

                    m_out = int(counter['out'] - item.el_out) * item.el_coef
                    m_out = item.mex_out + m_out * item.mex_coef

                    ords.mex_new_enter = m_in
                    ords.mex_new_exit = m_out

                    ords.bill_old = item.bill
                    ords.bill_new = bill
                    ords.user_id = self.user.id
                    ords.old_won = item.won
                    ords.new_won = counter['won']
                    ords.old_bet = item.bet
                    ords.new_bet = counter['bet']

                    bill_in_device = bill - item.bill
                    mony_in_user = mony_in_user - (bill - item.bill)
                    item.bill_in_device = item.bill_in_device + bill_in_device

                    item.el_in = counter['in']
                    item.el_out = counter['out']
                    item.won = counter['won']
                    item.bet = counter['bet']
                    item.mex_in = m_in
                    item.mex_out = m_out
                    item.bill = bill

                    self.db.add_object_to_session(ords)
                    self.db.add_object_to_session(item)
                    user_kasa = mony_in_user

                    if self.cart is not False:
                        ks_key_change = None
                        for i in range(3):
                            if ks_key_change == None:
                                ks_key_change = libs.udp.send(libs.smib.KS_CHANGE_KEY, ip=item.ip, credit_id=self.cart)
                            else:
                                break
                    if not self._want_abort:
                        try:
                            wx.PostEvent(self._notify_window, GetCounter(item.nom_in_l))
                        except:
                            pass
            else:
                libs.log.stdout_logger.error('NO GET COUNTER FROM %s', item.ip)
                if not self._want_abort:
                    wx.PostEvent(self._notify_window, GetCounter({'ERROR':item.nom_in_l}))
                    self.error.append(item.nom_in_l)
                else:
                    break
            mony_in_user = 0
            counter = None
            bill = None
            bill_block = None
            try:
                self.db.flush()
            except Exception as e:
                self.db.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                self.abort()
                break

        if self._want_abort:
            self.db.rollback()
            self.db.expire()
            user_kasa = 0
            cant_unlock = self.db.make_obj(libs.models.GetCounterError)
            cant_unlock.user_id = self.user.id
            cant_unlock.info = u'ORDER GET BREAK'
            libs.DB.add_object_to_session(cant_unlock)
            # self.db.expire(self.user)
            # self.user.kasa += user_kasa
            # self.db.add_object_to_session(self.user)
            # self.db.expire(self.user)
            # self.user.kasa += user_kasa
            # self.db.add_object_to_session(self.user)
            try:
                self.db.commit()
            except Exception as e:
                libs.DB.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
        else:
            self.db.expire(self.user)
            self.user.kasa += user_kasa
            self.db.add_object_to_session(self.user)
            try:
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                try:
                    wx.PostEvent(self._notify_window, GetCounter('ERROR'))
                except:
                    pass
            try:
                wx.PostEvent(self._notify_window, GetCounter(self.error))
            except:
                pass
        return

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1


class BlockBill(Thread):
    def __init__(self, q):
        self.q = q
        Thread.__init__(self)
        # self._notify_window = notify_window
        self._want_abort = 0

    def abort(self):
        self._want_abort = 1

    def run(self):
        while True:
            try:
                data = None
                data = self.q.get_nowait()
                if data:
                    for i in range(3):
                        tmp = None
                        tmp = libs.udp.send(data[0], ip=data[1], command=data[2])
                        if tmp:
                            break
            except Empty:
                time.sleep(0.5)
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
            if self._want_abort:
                break