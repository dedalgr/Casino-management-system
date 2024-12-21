#-*- coding:utf-8 -*-
'''
Created on 15.04.2018 г.

@author: dedal
'''
import time
from threading import *
import wx
import libs
import time

GET_DB = wx.NewId()
GET_DB_RUN = wx.NewId()
GET_DB_STOP = wx.NewId()

SET_DB = wx.NewId()
SET_DB_RUN = wx.NewId()
SET_DB_STOP = wx.NewId()

def EVT_GET_DB(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, GET_DB, func)
    
def EVT_KSET_DB(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, SET_DB, func)
    

class GetDBEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(GET_DB)
        self.data = data
        
class SetDBEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(SET_DB)
        self.data = data
        
class GetDBWorker(Thread):
    
    def __init__(self, notify_window, keys):
        Thread.__init__(self)
        self._want_abort = 0
        self._notify_window = notify_window
        self.keys = keys
        self.start()
    
    def abort(self):
        self._want_abort = 1
        
    def run(self):
        data = None
        for i in self.keys:
            if not self._want_abort:
                for b in range(3):
                    data = libs.udp.send('GET_DB_KEY', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, key=i)

                    if data != None:
                        break
                if data == None and not self._want_abort:
                    wx.PostEvent(self._notify_window, GetDBEvent('ERROR'))
                    return
                # if i == 'smib':
                if not self._want_abort:
                    wx.PostEvent(self._notify_window, GetDBEvent([i, data]))
            else:
                break
        if not self._want_abort:
            wx.PostEvent(self._notify_window, GetDBEvent('DONE'))
            
        
class SetDBWorker(Thread):
    
    def __init__(self, notify_window, db):
        Thread.__init__(self)
        self._want_abort = 0
        self.db = db
        self._notify_window = notify_window
        self.start()
        
    def abort(self):
        self._want_abort = 1
        
    def run(self):
        # response = None
        # for i in range(3):
        #     if response != True:
        #         response = libs.udp.send('STOP_ROTATION', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT,
        #                                  command=True)
        #     else:
        #         time.sleep(1)
        #         break
        data = None
        for i in sorted(list(self.db.keys())):
            if not self._want_abort:
                for b in range(3):
                    data = libs.udp.send('SET_DB_KEY',ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, key=i, data=self.db[i])
                    if data == True:
                        break
                    time.sleep(1)
                if data == None and not self._want_abort:
                    wx.PostEvent(self._notify_window, GetDBEvent('ERROR'))
                    self.abort()
                    break
                else:
                    if not self._want_abort:
                        wx.PostEvent(self._notify_window, GetDBEvent([i, data]))
            else:
                time.sleep(1)
                break
            # return
        # response = None
        # for i in range(3):
        #     if response != True:
        #         response = libs.udp.send('STOP_ROTATION', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT,
        #                                  command=False)
        #     else:
        #         time.sleep(1)
        #         break
        # if response != True:
        #     if not self._want_abort:
        #         wx.PostEvent(self._notify_window, GetDBEvent('ERROR_ROTATION'))
        #     return
        response = None
        for i in range(3):
            response = libs.udp.send('SET_DB_KEY', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, key='END')
            if response:
                if not self._want_abort:
                    wx.PostEvent(self._notify_window, GetDBEvent(['END', response]))
                break
        if response != True and not self._want_abort:
            wx.PostEvent(self._notify_window, GetDBEvent('ERROR_VISUAL'))
        else:
            if not self._want_abort:
                wx.PostEvent(self._notify_window, GetDBEvent('DONE'))
        
        