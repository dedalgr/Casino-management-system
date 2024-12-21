#-*- coding:utf-8 -*-
'''
Created on 26.03.2017 г.

@author: dedal
'''
# import _gui
# import wx
import webbrowser
import os
from . import conf

class Help():
    def __init__(self, adress=None):
        # if adress == None:
        #     webbrowser.open_new_tab("http://127.0.0.1:5000/")
        # else:
        webbrowser.open_new_tab(adress)
