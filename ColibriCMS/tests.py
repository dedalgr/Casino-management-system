#-*- coding:utf-8 -*-
'''
Created on 6.02.2018 г.

@author: dedal
'''

import unittest
import demon
import wx
import libs
libs.conf.SERVER = '127.0.0.1'
libs.conf.UNITEST = True
import threading
# if libs.conf.UNITEST:
#     wx.CallLater(libs.conf.UNITEST, dial.EndModal, wx.ID_OK)
# libs.conf.UNITEST = 250
import task
import mashin
import time
from Queue import Queue
Q = Queue()

# class T(threading.Thread):
#     def __init__(self, Q):
#         threading.Thread.__init__(self)
#         self.Q = Q
#
#     def run(self):
#         while True:
#             time.sleep(1)
#             data = self.Q.get()
#             for i in data.GetChildren():
#                 try:
#                     wx.CallLater(250, i.EndModal, wx.ID_OK)
#                 except:
#                     pass


class TestMyDialog(unittest.TestCase):

    def setUp(self):
        self.app = wx.App()
        self.frame = demon.MainFrame(None)
        # global Q
        # self.Q = Q
        # t = T(Q)
        # t.start()
        self.frame.Show()

    
    def login(self):
        self.frame.login.m_choice1.SetSelection(1)
        self.frame.login.m_textCtrl5.SetValue('102055')
        self.frame.login.OnIn(None)

        
    def logout(self):
        self.frame.login.panel.OnLogOut(None)
        
    def tearDown(self):
        self.frame.OnClose(None)
        wx.CallAfter(self.app.Exit)

    def florSelect(self):
        self.frame.login.panel.OnFlor(None)
        for i in self.frame.GetChildren():
            if type(i) == mashin.main.FlorSelect:
                break
        i.OnAdd(None)
        for b in i.GetChildren():
            if type(b) == mashin.main.FlorAdd:
                break
        b.m_textCtrl1.SetValue('UNITEST')
        b.OnGo(None)

        i.m_listCtrl1.Select(1)
        i.m_listCtrl1.Focus(1)
        i.OnGo(None)


    def test_App(self):
        self.login()
        self.florSelect()
        self.logout()
        self.tearDown()
        
        
        
if __name__ == "__main__":
    unittest.main()