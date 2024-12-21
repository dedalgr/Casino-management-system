#-*- coding:utf-8 -*-
'''
Created on 27.05.2017 г.

@author: dedal
'''
import wx
from .gui import KeyBordINT, KeyBordB, SelectLang  # @UnresolvedImport
from libs.conf import ALL_LANGUAGE, USE_LANGUAGE, DEBUG  # @UnresolvedImport

class SelectLanguage(SelectLang):
    def __init__(self, parent):
        SelectLang.__init__(self, parent)
        self.m_choice1Choices = []
        for item in ALL_LANGUAGE:
            self.m_choice1Choices.append(ALL_LANGUAGE[item])
        self.m_choice1.SetItems(self.m_choice1Choices)
        self.m_choice1.SetSelection(self.m_choice1Choices.index(ALL_LANGUAGE[USE_LANGUAGE]))

    def OnClose(self, event):
        self.lang = None
        self.Destroy()

    def OnGo(self, event):
        lang = self.m_choice1.GetSelection()
        lang = self.m_choice1Choices[lang]
        for item in ALL_LANGUAGE:
            if lang == '':
                self.lang = None
            elif lang == ALL_LANGUAGE[item]:
                self.lang = item

        self.Destroy()


class IntKeybord(KeyBordINT):
    def __init__(self, parent, value=u'', passwd=False, math=False, hex_val=False):
        KeyBordINT.__init__(self, parent)
        if passwd is True:
            self.m_textCtrl2.SetWindowStyleFlag(style=wx.TE_PASSWORD)
        self.m_textCtrl2.SetValue(value)
        self.old_val = value
        self.value = value
        self.math = math
        self.hex = hex
        if self.math is True:
            self.m_button20.Show()
            self.m_button21.Show()
            self.m_button22.Show()
            self.m_button23.Show()
            self.m_button24.Show()
            self.m_button20.Disable()
            self.m_button92.Show()
        else:
            self.m_button20.Disable()
            self.m_button21.Disable()
            self.m_button22.Disable()
            self.m_button23.Disable()
            self.m_button24.Disable()
            self.m_button20.Disable()
            self.m_button92.Disable()
        if self.hex is True:
            self.m_button19.SetLabel('-')
            self.m_button31.Show()
            self.m_button32.Show()
            self.m_button33.Show()
            self.m_button38.Show()
            self.m_button39.Show()
            self.m_button40.Show()
        self.m_textCtrl2.SetEditable(False)
        self.Fit()

    def OnInt(self, event):
        #         id = event.GetEventObject()
        self.value = self.value + event.GetEventObject().GetLabel()
        self.m_textCtrl2.SetValue(self.value)

    def OnRavno(self, event):
        try:
            value = "%.2f" % round(eval('1.0*' + self.value), 2)
        except ZeroDivisionError:
            value = '0'
        else:
            self.value = value
            self.m_textCtrl2.SetValue(self.value)

    def OnDel(self, event):
        #         id = event.GetEventObject()
        self.value = self.value[:-1]
        self.m_textCtrl2.SetValue(self.value)

    def OnClear(self, event):
        self.m_textCtrl2.SetValue('')
        self.value = ''
        self.m_textCtrl2.SetValue(self.value)

    def OnClose(self, event):
        self.value = self.old_val
        self.Destroy()

    def OnGo(self, event):
        self.Destroy()
        self.value = self.m_textCtrl2.GetValue()
        return True


class KeyBord(KeyBordB):
    def __init__(self, parent, value=u'', lang=USE_LANGUAGE):
        KeyBordB.__init__(self, parent)
        self.value = value
        self.old_val = value
        self.big = False
        self.lang = lang
        if self.lang == 'bg':
            self.OnBG()
        elif self.lang == 'en':
            self.OnEN()
        else:
            self.OnEN()
        self.MS = False
        self.m_textCtrl2.SetValue(value)
        self.m_textCtrl2.SetEditable(False)

    def OnNewRow( self, event ):
        self.value = self.value + u'\n'
        self.m_textCtrl2.SetValue(self.value)

    def OnBG(self):
        self.m_button32.Enable()
        self.m_button38.Enable()
        self.m_button48.Enable()
        self.m_button69.Enable()
        self.m_button66.SetLabel(u' ')
        if self.big is True:
            self.m_button27.SetLabel(u'Я')
            self.m_button28.SetLabel(u'В')
            self.m_button29.SetLabel(u'Е')
            self.m_button30.SetLabel(u'Р')
            self.m_button31.SetLabel(u'Т')
            self.m_button32.SetLabel(u'Ъ')
            self.m_button33.SetLabel(u'У')
            self.m_button34.SetLabel(u'И')
            self.m_button35.SetLabel(u'О')
            self.m_button36.SetLabel(u'П')
            self.m_button37.SetLabel(u'Ч')

            self.m_button38.SetLabel(u'А')
            self.m_button39.SetLabel(u'С')
            self.m_button40.SetLabel(u'Д')
            self.m_button41.SetLabel(u'Ф')
            self.m_button42.SetLabel(u'Г')
            self.m_button43.SetLabel(u'Х')
            self.m_button44.SetLabel(u'Й')
            self.m_button45.SetLabel(u'К')
            self.m_button46.SetLabel(u'Л')
            self.m_button47.SetLabel(u'Ш')
            self.m_button48.SetLabel(u'Щ')

            self.m_button50.SetLabel(u'З')
            self.m_button51.SetLabel(u'ь')
            self.m_button52.SetLabel(u'Ц')
            self.m_button53.SetLabel(u'Ж')
            self.m_button54.SetLabel(u'Б')
            self.m_button55.SetLabel(u'Н')
            self.m_button56.SetLabel(u'М')
            self.m_button69.SetLabel(u'Ю')
        elif self.big is False:
            self.m_button27.SetLabel(u'я')
            self.m_button28.SetLabel(u'в')
            self.m_button29.SetLabel(u'е')
            self.m_button30.SetLabel(u'р')
            self.m_button31.SetLabel(u'т')
            self.m_button32.SetLabel(u'ъ')
            self.m_button33.SetLabel(u'у')
            self.m_button34.SetLabel(u'и')
            self.m_button35.SetLabel(u'о')
            self.m_button36.SetLabel(u'п')
            self.m_button37.SetLabel(u'ч')

            self.m_button38.SetLabel(u'а')
            self.m_button39.SetLabel(u'с')
            self.m_button40.SetLabel(u'д')
            self.m_button41.SetLabel(u'ф')
            self.m_button42.SetLabel(u'г')
            self.m_button43.SetLabel(u'х')
            self.m_button44.SetLabel(u'й')
            self.m_button45.SetLabel(u'к')
            self.m_button46.SetLabel(u'л')
            self.m_button47.SetLabel(u'ш')
            self.m_button48.SetLabel(u'щ')

            self.m_button50.SetLabel(u'з')
            self.m_button51.SetLabel(u'ь')
            self.m_button52.SetLabel(u'ц')
            self.m_button53.SetLabel(u'ж')
            self.m_button54.SetLabel(u'б')
            self.m_button55.SetLabel(u'н')
            self.m_button56.SetLabel(u'м')
            self.m_button69.SetLabel(u'ю')
        else:
            pass

    def OnEN(self):
        self.m_button32.SetLabel('')
        self.m_button32.Disable()
        self.m_button38.SetLabel('')
        self.m_button38.Disable()
        self.m_button48.SetLabel('')
        self.m_button48.Disable()
        self.m_button69.SetLabel('')
        self.m_button69.Disable()
#         self.m_button70.SetSize((106, -1))
#         self.m_button50.SetLabel('')
#         self.m_button50.Disable()
#         self.m_button69.SetLabel('')
#         self.m_button69.Disable()
        if self.big is True:
            self.m_button27.SetLabel(u'Q')
            self.m_button28.SetLabel(u'W')
            self.m_button29.SetLabel(u'E')
            self.m_button30.SetLabel(u'R')
            self.m_button31.SetLabel(u'T')
            self.m_button33.SetLabel(u'Y')
            self.m_button34.SetLabel(u'U')
            self.m_button35.SetLabel(u'I')
            self.m_button36.SetLabel(u'O')
            self.m_button37.SetLabel(u'P')

            self.m_button39.SetLabel(u'A')
            self.m_button40.SetLabel(u'S')
            self.m_button41.SetLabel(u'D')
            self.m_button42.SetLabel(u'F')
            self.m_button43.SetLabel(u'G')
            self.m_button44.SetLabel(u'H')
            self.m_button45.SetLabel(u'J')
            self.m_button46.SetLabel(u'K')
            self.m_button47.SetLabel(u'L')

            self.m_button50.SetLabel(u'Z')
            self.m_button51.SetLabel(u'X')
            self.m_button52.SetLabel(u'C')
            self.m_button53.SetLabel(u'V')
            self.m_button54.SetLabel(u'B')
            self.m_button55.SetLabel(u'N')
            self.m_button56.SetLabel(u'M')
        elif self.big is False:
            self.m_button27.SetLabel(u'q')
            self.m_button28.SetLabel(u'w')
            self.m_button29.SetLabel(u'e')
            self.m_button30.SetLabel(u'r')
            self.m_button31.SetLabel(u't')
            self.m_button33.SetLabel(u'y')
            self.m_button34.SetLabel(u'u')
            self.m_button35.SetLabel(u'i')
            self.m_button36.SetLabel(u'o')
            self.m_button37.SetLabel(u'p')

            self.m_button39.SetLabel(u'a')
            self.m_button40.SetLabel(u's')
            self.m_button41.SetLabel(u'd')
            self.m_button42.SetLabel(u'f')
            self.m_button43.SetLabel(u'g')
            self.m_button44.SetLabel(u'h')
            self.m_button45.SetLabel(u'j')
            self.m_button46.SetLabel(u'k')
            self.m_button47.SetLabel(u'l')

            self.m_button50.SetLabel(u'z')
            self.m_button51.SetLabel(u'x')
            self.m_button52.SetLabel(u'c')
            self.m_button53.SetLabel(u'v')
            self.m_button54.SetLabel(u'b')
            self.m_button55.SetLabel(u'n')
            self.m_button56.SetLabel(u'm')
        else:
            pass

    def OnSM(self, event):
        if self.MS is False:
            self.MS = True
            self.big = False
            self.m_button32.SetLabel('')
            self.m_button32.Disable()
            self.m_button48.SetLabel('')
            self.m_button48.Disable()
#             self.m_button69.SetLabel('')
#             self.m_button69.Disable()
            self.m_button38.Enable()

            self.m_button27.SetLabel(u'1')
            self.m_button28.SetLabel(u'2')
            self.m_button29.SetLabel(u'3')
            self.m_button30.SetLabel(u'4')
            self.m_button31.SetLabel(u'5')
            self.m_button33.SetLabel(u'6')
            self.m_button34.SetLabel(u'7')
            self.m_button35.SetLabel(u'8')
            self.m_button36.SetLabel(u'9')
            self.m_button37.SetLabel(u'0')

            self.m_button38.SetLabel(u'!')
            self.m_button39.SetLabel(u'@')
            self.m_button40.SetLabel(u'#')
            self.m_button41.SetLabel(u'$')
            self.m_button42.SetLabel(u'_')
            self.m_button43.SetLabel(u'-')
            self.m_button44.SetLabel(u'+')
            self.m_button45.SetLabel(u'(')
            self.m_button46.SetLabel(u')')
            self.m_button47.SetLabel(u'/')

            self.m_button50.SetLabel(u'=')
            self.m_button51.SetLabel(u'*')
            self.m_button52.SetLabel(u'"')
            self.m_button53.SetLabel(u"'")
            self.m_button54.SetLabel(u':')
            self.m_button55.SetLabel(u';')
            self.m_button56.SetLabel(u'!')
            self.m_button69.SetLabel(u'?')
        else:
            self.MS = False
            if self.lang == 'bg':
                self.OnBG()
            elif self.lang == 'en':
                self.OnEN()
            else:
                pass

    def OnCtrl(self, event):
        self.MS = False
        if self.big is True:
            self.big = False
        elif self.big is False:
            self.big = True
        if self.lang == 'bg':
            self.OnBG()
        elif self.lang == 'en':
            self.OnEN()
        else:
            pass

    def OnLang(self, event):
        frame = SelectLanguage(self)
        frame.ShowModal()
        self.MS = False
        if frame.lang:
            self.lang = frame.lang
        else:
            frame.lang = self.lang

        if frame.lang == 'bg':
            self.OnBG()
        elif frame.lang == 'en':
            self.OnEN()

    def OnB(self, event):
        #         id = event.GetEventObject()
        self.value = self.value + event.GetEventObject().GetLabel()
        self.m_textCtrl2.SetValue(self.value)

    def OnDel(self, event):
        self.value = self.value[:-1]
        self.m_textCtrl2.SetValue(self.value)

    def OnEnter(self, event):
        self.Destroy()
        self.value = self.m_textCtrl2.GetValue()

    def OnClose(self, event):
        self.value = self.old_val
        self.Destroy()

class Keyboard():
    
    def OnIntKeyboard(self, event):
        MyObject = self.FindWindowById(event.Id)
        keybord = IntKeybord(self, str(MyObject.GetValue()))
        keybord.ShowModal()
        try:
            MyObject.SetValue(keybord.value)
        except TypeError:
            MyObject.SetValue(int(keybord.value))
        self.Fit()
        
    def OnKeyboard(self, event):
        MyObject = self.FindWindowById(event.Id)
        keybord = KeyBord(self, MyObject.GetValue(), lang=USE_LANGUAGE)
        keybord.ShowModal()
        MyObject.SetValue(keybord.value)
        self.Fit()
    
    def OnIntWithPass(self, event):
        MyObject = self.FindWindowById(event.Id)
        keybord = IntKeybord(self, str(MyObject.GetValue()), passwd = True)
        keybord.ShowModal()
        try:
            MyObject.SetValue(keybord.value)
        except TypeError:
            MyObject.SetValue(int(keybord.value))
        self.Fit()
        
    def OnHexKeybord(self, event):
        MyObject = self.FindWindowById(event.Id)
        keybord = IntKeybord(self, str(MyObject.GetValue()), hex_val = True)
        keybord.ShowModal()
        try:
            MyObject.SetValue(keybord.value)
        except TypeError:
            MyObject.SetValue(int(keybord.value))
        self.Fit()
        
    def OnCalcKeybord(self, event):
        MyObject = self.FindWindowById(event.Id)
        keybord = IntKeybord(self, str(MyObject.GetValue()), math = True)
        keybord.ShowModal()
        try:
            MyObject.SetValue(keybord.value)
        except TypeError:
            MyObject.SetValue(int(keybord.value))
        self.Fit()
        
