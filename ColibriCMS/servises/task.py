#-*- coding:utf-8 -*-
'''
Created on 17.12.2020 г.

@author: dedal
'''
import time
from threading import *
import wx
import libs

ID_COMAND = wx.NewId()
ID_COMAND_RUN = wx.NewId()
ID_COMAND_STOP = wx.NewId()

def EVT_COMAND(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, ID_COMAND, func)

class ComandEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(ID_COMAND)
        self.data = data

class ComandRun(Thread):
    def __init__(self, notify_window, comand, device, show_response=False):
        Thread.__init__(self)
        self.comand = comand
        self.show_response = show_response
        self.device = device
        self._notify_window = notify_window
        self._want_abort = 0
        self.msg = ''
        self.start()

    def abort(self):
        # print 'abort'
        self._want_abort = 1

    def run(self):
        for i in self.device:
            response = libs.udp.send('run_linux_cmd', i.ip, cmd=self.comand, show_response=self.show_response)
            self.msg += '%s: %s\n%s\n' % (i.nom_in_l, i.ip, response)
            try:
                wx.PostEvent(self._notify_window, ComandEvent(True))
            except Exception as e:
                pass
            if self._want_abort:
                wx.PostEvent(self._notify_window, ComandEvent('DONE'))
                break
        wx.PostEvent(self._notify_window, ComandEvent(self.msg))

