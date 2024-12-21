'''
Created on 18.04.2019

@author: dedal
'''

from threading import *
import wx
import libs  # @UnresolvedImport
# import db_ctrl
# import mashin
# import mony

UPDATE_USER_GET = wx.NewId()
UPDATE_USER_RUN = wx.NewId()
UPDATE_USER_STOP = wx.NewId()

DEL_TALON_GET = wx.NewId()
DEL_TALON_RUN = wx.NewId()
DEL_TALON_STOP = wx.NewId()

ORC_GET = wx.NewId()
ORC_RUN = wx.NewId()
ORC_STOP = wx.NewId()

def EVT_ORC_GET(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ORC_GET, func)

class EvtORCGet(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ORC_GET)
        self.data = data

class ORCDataGet(Thread):
    def __init__(self, notify_window, parent):
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self.parent = parent

        self.start()

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1

    def run(self):
        while True:
            if self._want_abort:
                break
            data = self.parent.ocr_data
            if data != False:
                wx.PostEvent(self._notify_window, EvtORCGet(data))
                break


def EVT_DEL_TALON(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, DEL_TALON_GET, func)

def EVT_UPDATE_USER_GET(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, UPDATE_USER_GET, func)

class DelTalon(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(DEL_TALON_GET)
        self.data = data

class DellAllTalon(Thread):
    def __init__(self, notify_window, all_user):
        Thread.__init__(self)
        self.all_user = all_user
        self._notify_window = notify_window
        self._want_abort = 0
        # libs.DB.expire()

        self.start()

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1

    def run(self):
        for item in self.all_user:
            if self._want_abort:
                wx.PostEvent(self._notify_window, DelTalon('ERROR'))
                break
            item.total_tombula = 0
            libs.DB.add_object_to_session(item)
            wx.PostEvent(self._notify_window, DelTalon(1))
            libs.DB.flush()
            if self._want_abort:
                libs.DB.rollback()
                break
        if not self._want_abort:
            try:
                libs.DB.commit()
            except Exception as e:
                libs.DB.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                try:
                    wx.PostEvent(self._notify_window, DelTalon('ERROR'))
                except:
                    pass
                return
            try:
                wx.PostEvent(self._notify_window, DelTalon('DONE'))
            except:
                pass
        else:
            libs.DB.rollback()


class GetBUpdateUser(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(UPDATE_USER_GET)
        self.data = data


class UpdateUser(Thread):
    """Worker Thread Class."""
    def __init__(self, notify_window, all_user, group):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self.all_user = all_user
        self.db = libs.DB
        self.group = group
        # self.db.expire()
        self.start()
    
    def abort(self):
        """abort worker thread."""
        self._want_abort = 1
        
    def run(self):
        for item in self.all_user:
            if self._want_abort:
                wx.PostEvent(self._notify_window, GetBUpdateUser('ERROR'))
                break
            item.bonus_in_mony = self.group.bonus_in_mony
            item.bonus_in_mony_sum = self.group.bonus_in_mony_sum
            item.mony_back_use = self.group.mony_back_use
            item.mony_back_pr = self.group.mony_back_pr
            item.tombola_use = self.group.tombola_use
            item.tombola_coef = self.group.tombola_coef
            item.restricted_bonus = self.group.restricted_bonus
            item.bonus_if_man = self.group.bonus_if_man
            item.tombola_on_in = self.group.tombola_on_in
            item.bonus_by_in = self.group.bonus_by_in
            item.bonus_one_per_day = self.group.bonus_one_per_day
            item.one_day_back_total = self.group.one_day_back_total
            item.month_back = self.group.month_back
            item.bonus_waith_for_in = self.group.bonus_waith_for_in
            item.bonus_use = self.group.bonus_use
            item.bonus_on_mony = self.group.bonus_on_mony
            item.no_out_befor = self.group.no_out_befor
            item.mony_back_min_pay = self.group.mony_back_min_pay
            item.region_id = self.group.region_id
#                 self.edit.bonus_on_mony = group.bonus_on_mony
#             item.bonus_row = self.group.bonus_row
            item.bonus_hold = self.group.bonus_hold
            item.bonus_row = self.group.bonus_row
            # item.x2 = self.group.x2
            # item.bonus_row_1_count = self.group.bonus_row_1_count
            # item.bonus_row_2_mony = self.group.bonus_row_2_mony
            # item.bonus_row_2_count = self.group.bonus_row_2_count
            # item.bonus_row_3_mony = self.group.bonus_row_3_mony
            # item.bonus_row_3_count = self.group.bonus_row_3_count
            # item.bonus_row_4_mony = self.group.bonus_row_4_mony
            # item.bonus_row_4_count = self.group.bonus_row_4_count
            item.mony_back_pay = self.group.mony_back_pay
            item.bonus_direct = self.group.bonus_direct
            item.bonus_on_day = self.group.bonus_on_day
            item.bonus_warning_use = self.group.bonus_warning_use
            item.bonus_warning_mony = self.group.bonus_warning_mony
            item.bonus_revert_by_bet = self.group.bonus_revert_by_bet
            item.use_total_procent = self.group.use_total_procent
            item.total_procent = self.group.total_procent
            item.more_than_one_from_redirect = self.group.more_than_one_from_redirect
            item.bonus_waith_for_in_mony = self.group.bonus_waith_for_in_mony
            self.db.add_object_to_session(item)
            try:
                self.db.flush()
            except Exception as e:
                self.db.rollback()
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                self.abort()
                break
            try:
                wx.PostEvent(self._notify_window, GetBUpdateUser(item.id))
            except:
                pass
        if self._want_abort:
            self.db.rollback()
        else:
            try:
                self.db.commit()
            except Exception as e:
                print(e)
                libs.log.stderr_logger.critical(e, exc_info=True)
                try:
                    wx.PostEvent(self._notify_window, GetBUpdateUser('ERROR'))
                except:
                    pass
                return
            try:
                wx.PostEvent(self._notify_window, GetBUpdateUser('DONE'))
            except:
                pass
            # except Exception as e:
            #     self.db.rollback()
            #     print(e)
            #     libs.log.stderr_logger.critical(e, exc_info=True)
