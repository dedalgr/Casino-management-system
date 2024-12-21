#-*- coding:utf-8 -*-
'''
Created on 31.05.2017 г.

@author: dedal
'''
import threading
import time

import wx
import libs  # @UnresolvedImport

ID_RFID_WORK_ID = wx.NewId()
ID_RFID_WORK_RUN = wx.NewId()
ID_RFID_WORK_STOP = wx.NewId()


# ID_RFID_CUST_ID = wx.NewId()
# ID_RFID_CUST_RUN = wx.NewId()
# ID_RFID_CUST_STOP = wx.NewId()

# def EVT_CUST_RFID_RESULT(win, func):
#     """Define Result Event."""
#     win.Connect(-1, -1, ID_RFID_CUST_ID, func)

# class RFIDCustResultEvent(wx.PyEvent):
#     """Simple event to carry arbitrary result data."""
#     def __init__(self, data):
#         """Init Result Event."""
#         wx.PyEvent.__init__(self)
#         self.SetEventType(ID_RFID_CUST_ID)
#         self.data = data

# class RFIDCust(threading.Thread):
#     """Worker Thread Class."""
#     def __init__(self, notify_window, timeout=False):
#         if timeout is True:
#             self.timeout = libs.conf.RFID_TIMEOUT
#         else:
#             self.timeout = False
#         """Init Worker Thread Class."""
#         threading.Thread.__init__(self)
#         self._notify_window = notify_window
#         self._want_abort = 0
#         self.start()
#
#     def run(self):
#         """Run Worker Thread."""
#         port = libs.conf.RFID_CUST_PORT
#         baud = libs.conf.RFID_BAUD
#         cart = libs.rfid.RFID(port, baud, self.timeout)
#         cart.open()
#         while True:
#             if cart.ser.isOpen() is False:
#                 cart.open()
#             else:
#                 try:
#                     data = cart.get_id()
#                     if data is False:
#                         data = None
#                     if self._want_abort:
#                         break
#                     else:
#                         try:
#                             wx.PostEvent(self._notify_window, RFIDWorkResultEvent(data))
#                         except:
#                             pass
#                 except Exception as e:
#                     print e
#                     cart.close()
#                     try:
#                         wx.PostEvent(self._notify_window, RFIDWorkResultEvent(None))
#                     except:
#                         pass
#
#     def abort(self):
#         """abort worker thread."""
#         self._want_abort = 1


def EVT_WORK_RFID_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_RFID_WORK_ID, func)


class RFIDWorkResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_RFID_WORK_ID)
        self.data = data


class RFIDWork(threading.Thread):
    """Worker Thread Class."""

    def __init__(self, notify_window, timeout=libs.conf.RFID_TIMEOUT, post_false=False):
        self.timeout = timeout
        self.port = libs.conf.RFID_WORK_PORT
        self.baud = libs.conf.RFID_BAUD
        self.post_false = post_false
        # self.cust = cust

        """Init Worker Thread Class."""
        threading.Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        self.start()

    def run(self):
        """Run Worker Thread."""

        cart = libs.rfid.RFID(self.port, self.baud, self.timeout)
        # block_write = True
        while True:
            if self._want_abort:
                try:
                    cart.close()
                except:
                    pass
                return
            if cart.ser.isOpen() is False:
                try:
                    cart.open()
                    # cart.write_key(a='FFFFFFFFFFFF', b='FFFFFFFFFFFF')

                except libs.rfid.RFIDOpenError as e:
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
                    try:
                        wx.PostEvent(self._notify_window, RFIDWorkResultEvent('ERROR'))
                        # time.sleep(1)
                    except Exception as e:
                        print(e)
                        libs.log.stderr_logger.critical(e, exc_info=True)
                        try:
                            cart.close()
                        except:
                            pass
                    return

            else:
                try:
                    # try:
                    # if os.name == 'posix':
                    #     fcntl.flock(cart.ser.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    data = cart.get_id()

                    # except TypeError:
                    # pass
                    if self._want_abort:
                        cart.close()
                        return
                    elif not data and self.post_false is True:
                        wx.PostEvent(self._notify_window, RFIDWorkResultEvent(False))
                    elif data == None and self.post_false is True:
                        wx.PostEvent(self._notify_window, RFIDWorkResultEvent(None))
                    else:
                        try:
                            # if self.cust is True and block_write is True:
                            #     block_write = False
                            #
                            #     block = cart.get_block(14)
                            #     if block is not False:
                            #         cart.write_key_to_cart(a='102055600310', b='102055600616')
                            wx.PostEvent(self._notify_window, RFIDWorkResultEvent(data))
                        except:
                            cart.close()
                    # if self._want_abort:
                    #     cart.close()
                    #     break
                    # old_data = data
                except Exception as e:
                    print(e)
                    libs.log.stderr_logger.critical(e, exc_info=True)
                    try:
                        cart.close()
                        wx.PostEvent(self._notify_window, RFIDWorkResultEvent(None))
                        # time.sleep(1)
                    except:
                        pass
                    if self._want_abort:
                        return

    def abort(self):
        """abort worker thread."""
        self._want_abort = 1