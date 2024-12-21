#-*- coding:utf-8 -*-
'''
Created on 21.10.2017 г.

@author: dedal
'''
import time  # @UnusedImport
from threading import *  # @UnusedWildImport
import wx
import libs  # @UnresolvedImport

KS_ID = wx.NewId() # Създава сигнал за промяна на кей системата
KS_RUN = wx.NewId() # сигнал за започване на промяна
KS_STOP = wx.NewId() # сигнал за спиране на процеза

ID_RFID_ID = wx.NewId()
ID_RFID_RUN = wx.NewId()
ID_RFID_STOP = wx.NewId()

ID_DEL_ID = wx.NewId()
ID_DEL_RUN = wx.NewId()
ID_DEL_STOP = wx.NewId()

ID_BONUS_CART = wx.NewId()
ID_BONUS_CART_RUN = wx.NewId()
ID_BONUS_CART_STOP = wx.NewId()

ID_BONUS_CART_ACTIVE = wx.NewId()
ID_BONUS_CART_ACTIVE_RUN = wx.NewId()
ID_BONUS_CART_ACTIVE_STOP = wx.NewId()


ID_REBOOT = wx.NewId()
ID_REBOOT_RUN = wx.NewId()
ID_REBOOT_STOP = wx.NewId()

ID_SMIB_CONFIG_ID = wx.NewId()
ID_SMIB_CONFIG_RUN = wx.NewId()
ID_SMIB_CONFIG_STOP = wx.NewId()

ID_SMIB_UNIXUPDATE_ID = wx.NewId()
ID_SMIB_UNIXUPDATE_RUN = wx.NewId()
ID_SMIB_UNIXUPDATE_STOP = wx.NewId()

ID_IVJUMP_ID = wx.NewId()
ID_IVJUMP_RUN = wx.NewId()
ID_IVJUMP_STOP = wx.NewId()

def EVT_IVJUMP_CONFIG_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_IVJUMP_ID, func)

def EVT_SMIB_UNIXUPDATE_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_SMIB_UNIXUPDATE_ID, func)

def EVT_SMIB_CONFIG_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_REBOOT, func)

def EVT_DEL_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_DEL_ID, func)

class DelresultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_DEL_ID)
        self.data = data

class IVJUMPresultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_IVJUMP_ID)
        self.data = data

class SMIBUNIXUPDATEresultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_SMIB_UNIXUPDATE_ID)
        self.data = data

class SMIBCONFIGresultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_REBOOT)
        self.data = data

def EVT_REBOOT_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_REBOOT, func)

class REBOOTresultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_REBOOT)
        self.data = data
        
def EVT_RFID_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_RFID_ID, func)
    
class RFIDResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_RFID_ID)
        self.data = data
        
def EVT_BONUS_CART_ACTIVE(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_BONUS_CART_ACTIVE, func)
    
class BonusCartActiveEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_BONUS_CART_ACTIVE)
        self.data = data
        
        
def EVT_BONUS_CART(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_BONUS_CART, func)

def EVT_KS(win, func):
    """Дефинира евънта който трябва да се прихване"""
    win.Connect(-1, -1, KS_ID, func)

class KsCommandPost(wx.PyEvent):
    """Поства информаьията получена от евънта"""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(KS_ID)
        self.data = data
        
class BonusCartEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_BONUS_CART)
        self.data = data

class IvJump(Thread):
    def __init__(self, notify_window, devise, data):
        Thread.__init__(self)
        self._want_abort = 0
        self.data = data
        self.devise = devise
        self._notify_window = notify_window
        self.start()

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1

    def run(self):
        for i in self.devise:
            request = False
            if self._want_abort:
                break
            for b in range(3):
                if self._want_abort:
                    break
                request = libs.udp.send('smib_if_jump', ip=i, iv_jump=self.data)
                if request:
                    break
            wx.PostEvent(self._notify_window, IVJUMPresultEvent(1))
        wx.PostEvent(self._notify_window, IVJUMPresultEvent('DONE'))

class DelOld(Thread):
    def __init__(self, notify_window, date, user, table, **kwargs):
        self.user = user
        self.date = date
        self.table = table
        self._notify_window = notify_window
        Thread.__init__(self)
        self._want_abort = 0
        self.db = libs.models.DBCtrl()
        self.start()

    def run(self):
        # libs.conf.LOCK.acquire()
        for i in self.table:
            old_data = self.db.get_all_where(i, pub_time__lte=self.date)
            for b in old_data:
                libs.DB.delete_object(b)
            self.db.flush()
            wx.PostEvent(self._notify_window, DelresultEvent(1))
        try:
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
        wx.PostEvent(self._notify_window, DelresultEvent('DONE'))



class SmibUnixUpdate(Thread):
    def __init__(self, notify_window, mashin, user, src, **kwargs):
        self.mashin = mashin
        self.user = user
        self._notify_window = notify_window
        Thread.__init__(self)
        self._want_abort = 0
        self.src = src
        self.start()

    def run(self):
        pass

class SmibConfig(Thread):
    def __init__(self, notify_window, mashin, user, conf, **kwargs):
        self.mashin = mashin
        self.user = user
        self.conf = conf
        self.RFID = kwargs['RFID']
        self.PROC = kwargs['PROC']
        self.save = kwargs['save_section']
        self.db = libs.models.DBCtrl()
        self._notify_window = notify_window
        Thread.__init__(self)
        self._want_abort = 0
        self.start()

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1

    def run(self):
        # libs.conf.LOCK.acquire()
        for i in self.mashin:
            libs.udp.send('backup_conf', ip=i.ip)
            if self.save['System'] is True:
                system_response = libs.udp.send('conf_update', ip=i.ip, section='SYSTEM',
                                            lang=self.conf['SYSTEM']['lang'], block_bonus_by_bet=self.conf['SYSTEM']['block_bonus_by_bet'])
            else:
                system_response = True
            if self.save['SAS'] is True:
                # system_response = libs.udp.send('conf_update', ip=i.ip, section='SYSTEM',
                #                                 proto_sas=self.conf['SYSTEM']['proto_sas'])
                sas_response = libs.udp.send('conf_update', ip=i.ip, section='SAS',
                                         sync_time=self.conf['SAS']['sync_time'],
                                         aft=self.conf['SAS']['aft'], security=self.conf['SAS']['security'],
                                         usb=self.conf['SAS']['usb'], pay_jp_by_hand=self.conf['SAS']['pay_jp_by_hand'],
                                         check_for_game=self.conf['SAS']['check_for_game'],
                                         # mail_send_on_won=self.conf['SAS']['mail_send_on_won'],
                                         # mail_send=self.conf['SAS']['mail_send'],
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
                                         set_jp_mether_to_out=self.conf['SAS']['set_jp_mether_to_out'],
                                         emg_type=self.conf['SAS']['emg_type'],
                                         aft_lock_time=self.conf['SAS']['aft_lock_time'],
                                         last_aft_transaction_from_emg=self.conf['SAS']['last_aft_transaction_from_emg'],
                                         )
            else:
                sas_response = True
                system_response = True
            if self.save['Mail Send'] is True:
                mail_send = libs.udp.send('conf_update', ip=i.ip, section='SAS',
                          mail_send_on_won=self.conf['SAS']['mail_send_on_won'],
                          mail_send=self.conf['SAS']['mail_send'])
            else:
                mail_send = True
            # raise KeyError, self.save['Jackpot']
            if self.save['Jackpot'] is True:
                jp_response = libs.udp.send('conf_update', ip=i.ip, section='JP_SERVER',
                                        block_if_lost=self.conf['JP_SERVER']['block_if_lost'],
                                        block_count=self.conf['JP_SERVER']['block_count'],
                                        down_if_credti=self.conf['JP_SERVER']['down_if_credti'],
                                        down_by_aft=self.conf['JP_SERVER']['down_by_aft']
                                        )
            else:
                jp_response = True
            if self.save['Keysystem'] is True:
                ks_response = libs.udp.send('conf_update', ip=i.ip, section='KEYSYSTEM',
                                        multi_key=self.conf['KEYSYSTEM']['multi_key'],
                                        aft=self.conf['KEYSYSTEM']['aft'],
                                        credit=self.conf['KEYSYSTEM']['credit'],
                                        report=self.conf['KEYSYSTEM']['report'],
                                        relay_timeout=self.conf['KEYSYSTEM']['relay_timeout'],
                                        )
            else:
                ks_response = True
            if self.save['Bonus'] is True:
                bonus_response = libs.udp.send('conf_update', ip=i.ip, section='BONUS',
                                           # sas_timeout=self.conf['BONUS']['sas_timeout'],
                                           out=self.conf['BONUS']['out'],
                                           pipe_clean=self.conf['BONUS']['pipe_clean'],
                                           # forbiden_out_befor=self.conf['BONUS']['forbiden_out_befor'],
                                           )
            else:
                bonus_response = True
            if self.save['System'] is True:
                watchdog_response = libs.udp.send('conf_update', ip=i.ip, section='WATCHDOG',
                                              reboot_if_error=self.conf['WATCHDOG']['reboot_if_error'],
                                              check_interval=self.conf['WATCHDOG']['check_interval'],
                                              critical_temp=self.conf['WATCHDOG']['critical_temp'],
                                              proc_chk=self.conf['WATCHDOG']['proc_chk'],
                                              net_chk=self.conf['WATCHDOG']['net_chk'],
                                              sys_chk=self.conf['WATCHDOG']['sys_chk'],
                                              )
                log_file = libs.udp.send('conf_update', ip=i.ip, section='LOGGING_FILE',
                                         use=self.conf['LOGGING_FILE']['use'])
            else:
                watchdog_response = True
                log_file = True
            if self.save['Log Config'] is True:
                log_level_response = libs.udp.send('conf_update', ip=i.ip, section='LOGGING_LEVEL',
                                               server=self.conf['LOGGING_LEVEL']['server'],
                                               rfid=self.conf['LOGGING_LEVEL']['rfid'],
                                               system=self.conf['LOGGING_LEVEL']['system'],
                                               sas=self.conf['LOGGING_LEVEL']['sas'],
                                               keysystem=self.conf['LOGGING_LEVEL']['keysystem'],
                                               bonus=self.conf['LOGGING_LEVEL']['bonus'],
                                               jpserver=self.conf['LOGGING_LEVEL']['jpserver'],
                                               client_cart=self.conf['LOGGING_LEVEL']['client_cart']
                                               )
            else:
                log_level_response = True
            if self.save['Client'] is True:
                system_response = libs.udp.send('conf_update', ip=i.ip, section='SYSTEM',
                                                lang=self.conf['SYSTEM']['lang'], block_bonus_by_bet=self.conf['SYSTEM']['block_bonus_by_bet'])
                player_response = libs.udp.send('conf_update', ip=i.ip, section='PLAYER',
                                            # use_touch=self.conf['PLAYER']['use_touch'],
                                            # sas_timeout=self.conf['PLAYER']['sas_timeout'],
                                            player_timeout=self.conf['PLAYER']['player_timeout'],
                                            bonus_on_credit=self.conf['PLAYER']['bonus_on_credit'],
                                            lock_emg_if_no_cust=self.conf['PLAYER']['lock_emg_if_no_cust'],
                                            logo_name=self.conf['PLAYER']['logo_name'],
                                            anime_use=self.conf['PLAYER']['anime_use'],
                                            anime_num=self.conf['PLAYER']['anime_num'],
                                            skin=self.conf['PLAYER']['skin'],
                                            lock_bill_if_no_cust=self.conf['PLAYER']['lock_bill_if_no_cust'],
                                            show_monybeck_pay=self.conf['PLAYER']['show_monybeck_pay']
                                            )
            else:
                player_response = True
                if system_response is True:
                    system_response = True
            if self.save['Log Server'] is True:
                logging_server = libs.udp.send('conf_update', ip=i.ip, section='LOGGING_SERVER',
                                           use=self.conf['LOGGING_SERVER']['use'],
                                           level=self.conf['LOGGING_SERVER']['level'],
                                           server_ip=self.conf['LOGGING_SERVER']['server_ip'])
            else:
                logging_server = True
            if self.save['RFID'] is True:
                rfid_set = libs.udp.send('rfid_scan_time', ip=i.ip, my_timeout=self.RFID['my_timeout'],
                                        scan_time=self.RFID['scan_time'], rc255=self.RFID['rc255'])
            else:
                rfid_set = True
            proc_response = []
            if self.save['PROC'] is True:
                if self.PROC['SAS'] is True:
                    proc_response.append(libs.udp.send('sas_start', i.ip))
                else:
                    proc_response.append(libs.udp.send('sas_stop', i.ip))
                if self.PROC['RFID'] is True:
                    proc_response.append(libs.udp.send('rfid_start', i.ip))
                else:
                    proc_response.append(libs.udp.send('rfid_stop', i.ip))
                if self.PROC['JP'] is True:
                    proc_response.append(libs.udp.send('jackpot_start', i.ip))
                else:
                    proc_response.append(libs.udp.send('jackpot_stop', i.ip))
                if self.PROC['Bonus'] is True:
                    proc_response.append(libs.udp.send('bonus_start', i.ip))
                else:
                    proc_response.append(libs.udp.send('bonus_stop', i.ip))
                if self.PROC['Client'] is True:
                    proc_response.append(libs.udp.send('client_cart_start', i.ip))
                else:
                    proc_response.append(libs.udp.send('client_cart_stop', i.ip))
                if self.PROC['Keysystem'] is True:
                    proc_response.append(libs.udp.send('keysystem_start', i.ip))
                else:
                    proc_response.append(libs.udp.send('keysystem_stop', i.ip))
            if system_response == None or None in proc_response or rfid_set == None or mail_send == None or log_file == None or logging_server == None or player_response == None or sas_response == None or jp_response == None or ks_response == None or bonus_response == None or watchdog_response == None or log_level_response == None:
                err = libs.DB.make_obj(libs.models.GetCounterError)
                err.user_id = self.user.id
                err.mashin_nom_in_l = i.id
                err.info = 'Change SMIB config'
                libs.DB.add_object_to_session(err)
                libs.DB.flush()

            if not self._want_abort:
                wx.PostEvent(self._notify_window, REBOOTresultEvent(1))
            else:
                break

        try:
            libs.DB.commit()
        except Exception as e:
            libs.DB.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
        if not self._want_abort:
            wx.PostEvent(self._notify_window, REBOOTresultEvent('DONE'))



class Reboot(Thread):
    def __init__(self, notify_window, mashin, user, reboot_time=1, soft=True):
        self.mashin = mashin 
        self.db = libs.models.DBCtrl()
        Thread.__init__(self)
        self._notify_window = notify_window
        self.user = user
        self.reboot_time=reboot_time
        self.soft = soft
        self._want_abort = 0
        self.start()
    
    def abort(self):
        """abort worker thread."""
        self._want_abort = 1
    
    def run(self):
        # libs.conf.LOCK.acquire()
        for item in self.mashin:

            if not self._want_abort:
                for i in range(3):  # @UnusedVariable
                    if self.soft is False:
                        data = libs.udp.send('reboot', ip=item.ip, time=self.reboot_time)
                        if data != None:
                            break
                    else:
                        data = libs.udp.send('soft_reboot', ip=item.ip)
                        if data != None:
                            break
                    time.sleep(1)
                err = self.db.make_obj(libs.models.GetCounterError)#(self.USER.id, i)
                err.user_id = self.user.id  # @UndefinedVariable
                err.mashin_nom_in_l = item.nom_in_l
                err.info = 'SMIB REBOOT' + ': ' + u'user %s time: %s.' % (self.user.name, self.reboot_time)
                self.db.add_object_to_session(err)

                if not self._want_abort:
                    wx.PostEvent(self._notify_window, REBOOTresultEvent(1))
                else:
                    break
        try:
            self.db.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            self.db.rollback()
        if not self._want_abort:
            wx.PostEvent(self._notify_window, REBOOTresultEvent('DONE'))

class UpdateSMIB(Thread):
    def __init__(self, notify_window, mashin, user, rev=None, reboot=False):
        self.mashin = mashin
        self.rev = rev
        self.db = libs.models.DBCtrl()
        Thread.__init__(self)
        self._notify_window = notify_window
        self.user = user
        self.reboot = reboot

        self._want_abort = 0
        self.start()

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1

    def run(self):
        # libs.conf.LOCK.acquire()
        for item in self.mashin:
            response = None
            if not self._want_abort:
                # for i in range(3):  # @UnusedVariable
                if self.rev == None:
                    response = libs.udp.send('svn_update', item.ip, soft_reboot=self.reboot)
                else:
                    response = libs.udp.send('svn_update', item.ip, rev=self.rev, soft_reboot=self.reboot)
                # if response != None and response is not False:
                #     # print response
                #     break
            if response == None or response is False:
                err = self.db.make_obj(libs.models.GetCounterError)
                err.user_id = self.user.id
                err.mashin_nom_in_l = item.id
                err.info = 'Error update SMIB'
                self.db.add_object_to_session(err)
            else:
                err = self.db.make_obj(libs.models.GetCounterError)
                err.user_id = self.user.id
                err.mashin_nom_in_l = item.id
                err.info = 'SMIB' + ': ' + u'UPDATE rev ' + str(response)
                self.db.add_object_to_session(err)
                # response = libs.udp.send('soft_reboot', item.ip)
            wx.PostEvent(self._notify_window, REBOOTresultEvent(1))
            if not self._want_abort:
                pass
            else:
                break
        try:
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
        # libs.conf.LOCK.release()
        wx.PostEvent(self._notify_window, REBOOTresultEvent('DONE'))
# class BonusCartActiv(Thread):
#     def __init__(self, notify_window, mashin, user, activ):
#         self.mashin = mashin 
#         self.activ = activ
#         self.user = user
#         Thread.__init__(self)
#         self._notify_window = notify_window
#         self._want_abort = 0
#         self.start()
#     
#     def run(self):
#         for item in self.mashin:
#             if not self._want_abort:
#                 for i in range(3):
#                     data = libs.udp.send('BONUS_CART_PROK', ip=item.ip, work=self.activ)
#                     if data != None:
#                         break
#                 wx.PostEvent(self._notify_window, BonusCartActiveEvent(1))
#                 if data == None:
#                     obj = self.db.make_obj(libs.models.GetCounterError)
#                     obj.user_id = self.user.id
#                     obj.mashin_nom_in_l = i.nom_in_l
#                     obj.info = _(u'Неуспех при актижиране на бонус карти.')
#                     self.db.add_object_to_session(obj)
#             else:
#                 break
#         self.db.commit()
#         wx.PostEvent(self._notify_window, BonusCartEvent('DONE'))
#             
#     def abort(self):
#         """abort worker thread."""
#         self._want_abort = 1
        
class BonusCartWork(Thread):
    """Worker Thread Class."""
    def __init__(self, notify_window, dict_for_write, mashin, user):
#         if timeout is True:
        self.my_dict_for_write = []
        for i in dict_for_write:
            self.my_dict_for_write.append(i.cart)# = {'model':i.cart_type, 'mony':i.mony, 'no_out_befor':i.no_bonus_out_befor, 'must_have_cust':i.must_have_cust}
        self.mashin = mashin
        # raise Exception, self.my_dict_for_write
#         else:
#             self.timeout = False
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        # self.evt_get = 'db_get_key'
        self.evt_set = 'bonus_add'
        # self.key = 'BONUSCART'
        self.error = []
        self.user = user
        self.db = libs.models.DBCtrl()
        self.start()

    def run(self):
        """Run Worker Thread."""
        # libs.conf.LOCK.acquire()
        for item in self.mashin:
            # data = self.dict_for_write
            # print data
            for i in range(3):
                data = libs.udp.send(self.evt_set, ip=item.ip, bonus=self.my_dict_for_write)
                if data != None and data is not False:
                    break
                # elif data is False:
                #     data = None
                #     break
            if data == None and data is False:
                self.error.append(item.nom_in_l)
            wx.PostEvent(self._notify_window, BonusCartEvent(1))
                
#        if not self._want_abort:
        for i in self.error:
            obj = self.db.make_obj(libs.models.GetCounterError)
            obj.user_id = self.user.id
            obj.mashin_nom_in_l = self.error[i]
            obj.info = u'ERROR bonus catr write'
            self.db.add_object_to_session(obj)
        try:
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)

        # libs.conf.LOCK.release()
        wx.PostEvent(self._notify_window, BonusCartEvent('DONE'))
            
    def abort(self):
        """abort worker thread."""
        self._want_abort = 1
        
class RFIDWork(Thread):
    """Worker Thread Class."""
    def __init__(self, notify_window, timeout=False):
#         if timeout is True:
        self.timeout = timeout 
#         else:
#             self.timeout = False
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self.start()

    def run(self):
        """Run Worker Thread."""
        port = libs.conf.RFID_WORK_PORT
        baud = libs.conf.RFID_BAUD
        cart = libs.rfid.RFID(port, baud, self.timeout)
        # try:
        #     cart.open()
        # except libs.rfid.RFIDReadError:
        #     wx.PostEvent(self._notify_window, RFIDResultEvent('ERROR'))
        #     return
        while True:
            if cart.isOpen() is False:
                try:
                    cart.open()
                except libs.rfid.RFIDOpenError:
                    wx.PostEvent(self._notify_window, RFIDResultEvent('ERROR'))
                    return
            else:
#                 try:
                try:
                    data = cart.get_id()
                    if data is False:
                        data = None
                except TypeError:
                    data = None
                if self._want_abort:
                    break
                else:
                    try:
                        wx.PostEvent(self._notify_window, RFIDResultEvent(data))
                    except:
                        pass
        
    def abort(self):
        """abort worker thread."""
        self._want_abort = 1
        



class KsSendCommand(Thread):
    '''
        Променя кей системата
    '''
    def __init__(self, notify_window, mashin, evt, command, user, **kwargs):
        """
            Конструктор
            Създава трейд или процес на заден фон
            приема име на прозореца който трябва да уведомява до къде е стигнал 
            всички машини на които трябва да се смени кей системата
            командата която трябва да се изпълни
            аргументи на командата report_id = номер на карта за отчет
            
            Сигнала който нота чака за да изпълни действието
        """
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self.mashin = mashin
        self.evt = evt
        self.command = command
        self.kwargs = kwargs
        self.user = user
        self.db = libs.models.DBCtrl()
        self.start()
    
    def abort(self):
        """Спира процеса за промяна"""
        self._want_abort = 1
        
    def run(self):
        '''
            Стартира процеса за промяна
            подава информация до къде е стигнал към прозореца за уведомяване
            При грешка пище в таблица лог какво се е случило
        '''
        # libs.conf.LOCK.acquire()
        for item in self.mashin:
            if not self._want_abort:
                for i in range(3):  # @UnusedVariable
                    if self.command == 'ACTIVE':
                        data = libs.udp.send(libs.smib.KS_ACTIVE, ip=item.ip)
                    elif self.command == 'DEACTIVE':
                        data = libs.udp.send(libs.smib.KS_DEACTIV, ip=item.ip)
#                         if data != None or data is False:
#                             break
                    elif self.command == 'KREDIT KEY CHANGE':
                        data = libs.udp.send(self.evt, ip=item.ip, credit_id=self.kwargs['cart'])
                    elif self.command == 'OWNER KEY CHANGE':
                        data = libs.udp.send(self.evt, ip=item.ip, report_id=self.kwargs['cart'])
                        
                    elif self.command == 'KEY SYSTEM RESET':
                        data = libs.udp.send(self.evt, ip=item.ip)
                    elif self.command == 'KS_RELAY_PORT':
                        data = libs.udp.send(self.evt, ip=item.ip, port=self.kwargs['port'])
                    else:
                        data = libs.udp.send(self.evt, ip=item.ip)
                    if data is True:
                        break
                    elif data is False:
                        pass
                    else:
                        pass
                if not self._want_abort:
                    wx.PostEvent(self._notify_window, KsCommandPost(1))
                
            if data == None or data is False:
                err = self.db.make_obj(libs.models.GetCounterError)#(self.USER.id, i)
                err.user_id = self.user.id  # @UndefinedVariable
                err.mashin_nom_in_l = item.nom_in_l
                err.info = self.command + ': ' + u'ERROR write keysystem'
                self.db.add_object_to_session(err)
            if self._want_abort:
                # libs.conf.LOCK.release()
                break

        try:
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
        # libs.conf.LOCK.release()
        if not self._want_abort:
            wx.PostEvent(self._notify_window, KsCommandPost('DONE'))



if __name__ == '__main__':
    pass
