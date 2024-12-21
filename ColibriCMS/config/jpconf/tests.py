#-*- coding:utf-8 -*-
import wx  # @UnresolvedImport
from . import  _gui
from wx.lib.pubsub import pub  # @UnusedImport

class Count(_gui.Count):
    def __init__(self, parent):
        _gui.Count.__init__(self, parent)
        self.count = 0
            # create a pubsub listener
        
 
    #----------------------------------------------------------------------
    def updateProgress(self, msg=''):
        """
        Update the progress bar
        """
        self.count += 1
 
        if self.count >= 100:
            self.Destroy()
 
        self.m_gauge1.SetValue(self.count)
        self.Fit()
#     def OnProgres(self):
#         import time
#         count = 1
#         for i in range(100):
#             time.sleep(1)
#             self.m_gauge1.SetValue(count + i)
            
#         self.Destroy()

            
app = wx.App()
frame = Count(None)
frame.ShowModal()
for i in range(100):
    frame.updateProgress()

# import time
# count = 0
# for i in range(100):
#     frame.m_gauge1.SetValue(count + i)
#     time.sleep(1)
app.MainLoop()
