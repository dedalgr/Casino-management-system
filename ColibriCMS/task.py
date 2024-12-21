#-*- coding:utf-8 -*-
'''
Created on 12.07.2017 г.

@author: dedal
'''
import time
from threading import *
import wx
import libs  # @UnresolvedImport
import os
if os.name == 'posix':
    import fcntl
import json
from queue import Empty

# from sqlalchemy.orm import sessionmaker

ID_SET_TIME = wx.NewId()
ID_SET_TIME_RUN = wx.NewId()
ID_SET_TIME_STOP = wx.NewId()

ID_MASHIN_CHK = wx.NewId()
ID_MASHIN_CHK_RUN = wx.NewId()
ID_MASHIN_CHK_STOP = wx.NewId()

ID_LOG_OUT= wx.NewId()
ID_LOG_OUT_RUN = wx.NewId()
ID_LOG_OUT_STOP = wx.NewId()

KS_CHANGE = wx.NewId()
KS_CHANGE_RUN = wx.NewId()
KS_CHANGE_STOP = wx.NewId()

ID_OCR_DATA = wx.NewId()
ID_OCR_RUN = wx.NewId()
ID_OCR_STOP = wx.NewId()

def EVT_OCR_DATA(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_OCR_DATA, func)

class OCRDataEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_OCR_DATA)
        self.data = data

class OCTRead(Thread):
    def __init__(self, notify_window, port):
        self.port = port
        Thread.__init__(self)
        self._notify_window = notify_window
        # a = open(libs.conf.ROOT_PATH + 'ocr.dat', 'a')
        # # a.write(json.dumps(False))
        # a.close()
        self._want_abort = 0
        if libs.conf.OCR_DESKO == False:
            self.ocr = libs.ocr.OCR(self.port, timeout=libs.conf.OCR_TIMEOUT, lock=libs.conf.OCR_LOCK)
        else:
            self.ocr = libs.ocr.DeskoOCR(self.port, timeout=libs.conf.OCR_TIMEOUT, lock=libs.conf.OCR_LOCK)
        self.start()

    def abort(self):
        try:
            self.ocr.close()
        except Exception as e:
            libs.log.stderr_logger.critical(e, exc_info=True)
            print(e)
        self._want_abort = 1

    def run(self):
        ERROR = False
        # kill = False
        while True:
            try:
                if self._want_abort:
                    break
                data = False
                if self.ocr.isOpen() is False:
                    self.ocr.open()
                    # if os.name == 'posix':
                    #     fcntl.flock(self.ocr.ser.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

                data = self.ocr.get_ocr_data()
                try:
                    self.ocr.close()
                except:
                    pass
                if data:
                    ERROR = data
                    if data == 'LITLE' or data == 'EXPIRED':
                        wx.PostEvent(self._notify_window, OCRDataEvent([data, data]))
                    else:
                        forb = libs.udp.send('lk_set', ip=libs.conf.SERVER, EGN=data['EGN'])
                        if forb == 'CANT_PLAY':
                            wx.PostEvent(self._notify_window, OCRDataEvent(['CANT_PLAY', data]))
                        elif not forb:
                            wx.PostEvent(self._notify_window, OCRDataEvent(['ERROR', data]))
                        else:
                            chk_in_nra = libs.udp.send('chk_nra', ip=libs.conf.SERVER, egn=data['EGN'], disable=True)
                            if chk_in_nra == None:
                                chk_in_nra = 'ERROR'
                            if chk_in_nra == 'ERROR':
                                chk_in_nra = libs.udp.send('chk_nra', ip=libs.conf.SERVER, egn=data['EGN'], disable=True)
                            if chk_in_nra == True:
                                wx.PostEvent(self._notify_window, OCRDataEvent(['DISABLE', data]))
                            elif chk_in_nra == 'ERROR' or chk_in_nra == 'LITLE' or not chk_in_nra or not chk_in_nra == 'EXPIRED':
                                wx.PostEvent(self._notify_window, OCRDataEvent([chk_in_nra, data]))
                            else:
                                wx.PostEvent(self._notify_window, OCRDataEvent([chk_in_nra, data]))
                else:
                    if ERROR != False:
                        wx.PostEvent(self._notify_window, OCRDataEvent(False))
                        ERROR = False
                    try:
                        self.ocr.close()
                    except:
                        pass
            except Exception as e:

                if self._want_abort:
                    break
                try:
                    self.ocr.close()
                except:
                    pass
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                try:
                    wx.PostEvent(self._notify_window, OCRDataEvent(['ERROR', None]))
                except:
                    pass
                # time.sleep(1)
                # ERROR = data
                # try:
                #     if data != ERROR:
                #
                #     self.ocr.close()
                # except Exception as e:
                #     pass


def EVT_SET_TIME(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_SET_TIME, func)

def EVT_KS_CHANGE(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, KS_CHANGE, func)

class SetEvtTime(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_SET_TIME)
        self.data = data

class KsChangeEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(KS_CHANGE)
        self.data = data
        
def EVT_LOGOUT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_LOG_OUT, func)
    
class LogOutEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_LOG_OUT)
        self.data = data

class SetTime(Thread):
    def __init__(self, notify_window,):
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self.start()

    def abort(self):
        self._want_abort = 1

    def run(self):
        # date = libs.models.TZ.date_to_str(formats='%d.%m.%Y %H:%M')
        # wx.PostEvent(self._notify_window, SetEvtTime(date))
        self.date = None
        while True:
            # print 'run'
            if not self._want_abort:
                date = libs.models.TZ.date_to_str(formats='%d.%m.%Y %H:%M')
                try:
                    if self.date != date:
                        wx.PostEvent(self._notify_window, SetEvtTime(date))
                        self.date = date
                except Exception as e:
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
                    break
            else:
                break
            time.sleep(1)

class LogOut(Thread):
    def __init__(self, notify_window, user):
        Thread.__init__(self)
        # self.user = user
        self._notify_window = notify_window
        self._want_abort = 0
        self.db = libs.db.PostgreSQL(dbname=libs.conf.DB_NAME, user=libs.conf.DB_USER, host=libs.conf.DB_SERVER, passwd=libs.conf.DB_PASS, port=libs.conf.DB_PORT)
        self.db.connect()
        self.user = user
        self.LOGIN_EVENT = Event()
        self.start()

    def abort(self):
        # print 'abort'
        self._want_abort = 1

    def run(self):
        my_time = time.time()
        while True:
            self.LOGIN_EVENT.wait(timeout=20)
            user = self.db.get_all('select * from users where id=%s and enable=True' % self.user)
            if not self._want_abort:
                # if my_time + 30 < time.time():
                #     my_time = time.time()
                try:
                    if user[0][8] is False:
                        try:
                            # libs.DB.add_object_to_session(self.user)
                            # libs.DB.commit()
                            wx.PostEvent(self._notify_window, LogOutEvent(True))
                        except TypeError:
                            pass
                except libs.models.InvalidRequestError:
                    break

                        # break
                # if self.user.session + 1200 < time.time():
                #     wx.PostEvent(self._notify_window, LogOutEvent(True))
                #     break
            else:
                self.db.close()
                break

            # wx.PostEvent(self._notify_window, LogOutEvent(False))


# class MashinState(Thread):
#     def __init__(self, notify_window, all_mashin):
#         """Init Worker Thread Class."""
#         Thread.__init__(self)
#         self.all_mashin = all_mashin
#         self._notify_window = notify_window
#         self._want_abort = 0
#         self.start()
#     
#     def abort(self):
#         """abort worker thread."""
#         self._want_abort = 1
#         
#     def run(self):
#         while True:
#             data = []
#             for item in self.all_mashin:
#                 for i in range(2):
#                     credit = libs.udp.send(libs.smib.SAS_F_METER_SINGLE, ip=item.ip, command=libs.smib.SAS_C_SINGLE_CURENT_CREDIT)
#                     if credit != None:
#                         break
#                 if credit == None:
#                     credit = _(u"Няма информация!")
#                 else:
#                     credit = "{:.2f}".format(credit)
#                 data.append([str(item.nom_in_l), item.model.name, credit])
#             if not self._want_abort:
#                 wx.PostEvent(self._notify_window, MashinStateEvent(data))
#                 time.sleep(10)
#             else:
#                 break
                
class WorkStart(Thread):
    
    def __init__(self, notify_window, mashin, cart, user_id):
        Thread.__init__(self)
        self.user_id = user_id
        self._want_abort = 0
        self.mashin = mashin
        self.cart = cart
        self.db = libs.models.DBCtrl()
        self._notify_window = notify_window
        self.start()
    
    def abort(self):
        self._want_abort = 1
        
    def run(self):
        # libs.conf.LOCK.acquire()
        for item in self.mashin:
            ks_key_change = None
            for i in range(3):
                if ks_key_change == None:
                    ks_key_change = libs.udp.send(libs.smib.KS_CHANGE_KEY, ip=item.ip, credit_id=self.cart)
                else:
                    break
            if ks_key_change == None:
                obj = self.db.make_obj(libs.models.GetCounterError)
                obj.user_id = self.user_id
                obj.mashin_nom_in_l = item.nom_in_l
                obj.info = u'KEY SISTEM NOT CHANGE'
                self.db.add_object_to_session(obj)
                self.db.flush()

            if not self._want_abort:
                if ks_key_change != None:
                    wx.PostEvent(self._notify_window, KsChangeEvent(item.nom_in_l))
                else:
                    wx.PostEvent(self._notify_window, KsChangeEvent([item.nom_in_l]))
            else:
                self.db.rollback()
                break
        try:
            self.db.commit()
        except Exception as e:
            print(e)
            libs.log.stderr_logger.critical(e, exc_info=True)
            self.db.rollback()
        # libs.conf.LOCK.release()
        if not self._want_abort:
#             self.db.dispose()
            wx.PostEvent(self._notify_window, KsChangeEvent('DONE'))
        
def EVT_MASHIN_CHK(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_MASHIN_CHK, func)
    
class MashinChkResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data, all_mashin):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_MASHIN_CHK)
        self.data = data
        self.all_mashin = all_mashin
        
        
# class DBConnectionRecycle(Thread):
#     
#     def __init__(self, q):
#         Thread.__init__(self)
#         self._want_abort = 0
#         self.q = q
#         self.start()
#     
#     def abort(self):
#         self._want_abort = 1
#     
#     def run(self):
#         count = 0
#         while True:
# #             Session = sessionmaker(bind=libs.models.engine)
# #             SESSION = libs.models.Session()
#             libs.models.engine.dispose()
#             libs.models.SESSION.execute('SELECT 1')
#             try:
#                 data = self.q.get(timeout=1)
#             except Empty:
#                 count += 1
#                 if count == 3600:
#                     count = 0 
#                     libs.models.SESSION.execute('SELECT 1')
#             else:
#                 if data == 'want db abort':
#                     break
#             SESSION.close()
            
class MashinCHK(Thread):
    def __init__(self, notify_window, all_mashin):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.all_mashin = all_mashin
        self._notify_window = notify_window
        self._want_abort = 0
        self.start()
    
    
    def run(self):
        data = {}
        for i in self.all_mashin:
            data[i.ip] = [-1, False]
        for item in self.all_mashin:
#             libs.udp.send(libs.smib.SAS_F_METER_SINGLE, ip=item.ip, command=libs.smib.SAS_C_SINGLE_BILL_START)
            if self._want_abort:
                return
            time.sleep(0.1)
            var = libs.udp.send('rev_and_player', item.ip)
            if var == None:
                var = [None, None]
            if self._want_abort:
                return
            # if var != None:
            #
            #     player = libs.udp.send('get_player', ip=item.ip)
            #     # print time.time() -a
            #     if self._want_abort:
            #         return
            # else:
            #     player = None

            # if var == None:
            #     var = libs.udp.send(libs.smib.ALIFE, item.ip)
            # if var == None:
            #     var = False
            data[item.ip] = var
            if not self._want_abort:
                try:
                    wx.PostEvent(self._notify_window, MashinChkResultEvent(data, all_mashin=self.all_mashin))
                except TypeError:
                    return
            else:
                return
#             except TypeError:
#                 return
        if not self._want_abort:
            try:
                wx.PostEvent(self._notify_window, MashinChkResultEvent('Done', None))
            except TypeError:
                return
        else: 
            return
    
    def abort(self):
        """abort worker thread."""
        self._want_abort = 1
