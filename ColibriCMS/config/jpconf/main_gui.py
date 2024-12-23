#-*- coding:utf-8 -*-
"""Subclass of Main, which is generated by wxFormBuilder."""

from . import _gui  # @UnresolvedImport
from . import user
from . import smib  # @UnresolvedImport
from . import visual  # @UnresolvedImport
from . import group
from . import server
# import helps
from . import down_log
import libs
import wx
from . import lrt
import pickle
import json
# import conf

class DBGet(_gui.GetDB):  # @UndefinedVariable
    def __init__(self, parent):
        _gui.GetDB.__init__(self, parent)
        self.parent = parent
        self.SetTitle(_(u'Изтегляне на информация от сървъра!'))
        for i in range(3):
            self.keys = libs.udp.send('GET_DB_KEYS', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT)
            if self.keys != None:
                break
        if self.keys == None:
            wx.MessageBox(_(u'Няма връзка със сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
            self.OnClose(None)
            # return None
        self.m_gauge1.SetRange(len(self.keys))
        self.loop = 0
        self.db = {}
        self.worker = lrt.GetDBWorker( self, self.keys )
        lrt.EVT_GET_DB(self, self.GetCount)
        
        
    def GetCount(self, event):
        if event.data == 'DONE':
            self.parent.DB = self.db
            for i in self.parent.DB:
                if self.parent.DB[i] == None:
                    self.parent.DB = None
            if self.parent.DB == None:
                wx.MessageBox(_(u'Грешка при изтегляне на информация!'), 'Error', wx.OK | wx.ICON_ERROR)
            else:
                wx.MessageBox(_(u'Информацията е изтеглена успешно!'), 'Info', wx.OK | wx.ICON_INFORMATION)
        elif event.data == 'ERROR':
            wx.MessageBox(_(u'Грешка при изтегляне на информация!'), 'Error', wx.OK | wx.ICON_ERROR)
            self.parent.DB = None
        else:
            self.loop = self.loop + 1
            self.m_gauge1.SetValue(self.loop)
            self.db[event.data[0]] = event.data[1]
            self.m_staticText69.SetLabel(event.data[0] + ': OK')
#         self.Fit()

    def OnTaskStop(self, event):
        """Stop Computation."""
        try:
            if self.worker:
                self.worker.abort()
                self.Destroy()
        except AttributeError:
            pass

    def OnClose(self, event):
        self.OnTaskStop(event)
        self.Destroy()
    
    def OnDestroy(self, event):
        self.Destroy()


class DBSet(_gui.GetDB):  # @UndefinedVariable
    def __init__(self, parent, db):
        _gui.GetDB.__init__(self, parent)
        self.parent = parent
        self.db = db
        self.SetTitle(_(u'Запис на информация към сървъра!'))
        self.keys = list(db.keys())
        
        self.m_gauge1.SetRange(len(self.keys)+1)
        self.loop = 0
        self.db = {}
        self.worker = lrt.SetDBWorker( self, db)
        lrt.EVT_GET_DB(self, self.GetCount)
          
          
    def GetCount(self, event):
        if event.data == 'DONE':
            wx.MessageBox(_(u'Информацията е записана успешно!'), 'Info', wx.OK | wx.ICON_INFORMATION)
        elif event.data == 'ERROR':
            wx.MessageBox(_(u'Грешка при запис на информация!'), 'Error', wx.OK | wx.ICON_ERROR)
        elif event.data == 'ERROR_VISUAL':
            wx.MessageBox(_(u'Промяната не е изпратена до визуализациите!'), 'Warning', wx.OK | wx.ICON_WARNING)
        elif event.data == 'ERROR_ROTATION':
            wx.MessageBox(_(u'Неуспешно разблокиране на сървър!'), 'Error', wx.OK | wx.ICON_ERROR)
#             self.parent.DB = None
        else:
            self.loop = self.loop + 1
            self.m_gauge1.SetValue(self.loop)
            self.m_staticText69.SetLabel(event.data[0] + ': OK')
#             self.db[event.data[0]] = event.data[1]
#         self.Fit()
  
    def OnTaskStop(self, event):
        """Stop Computation."""
        try:
            if self.worker:
                self.worker.abort()
                self.Destroy()
        except AttributeError:
            pass
  
    def OnClose(self, event):
        self.OnTaskStop(event)
        self.Destroy()
      
    def OnDestroy(self, event):
        self.Destroy()


# Implementing Main
class Main( _gui.Main ):
    def __init__( self, parent ):
        _gui.Main.__init__( self, parent )
        self.SetTitle(u'ColibriCMS')
        self.load_db = False
        self.m_bpButton5.SetLabel(_(u'Потребители'))
        self.m_staticText10.SetLabel(_(u"Потребители"))
        self.m_bpButton5.SetToolTip(_(u"Добавяне и премахване на потребители!"))
        
        self.m_bpButton4.SetLabel(_(u"Излез"))
        self.m_bpButton4.SetToolTip(_(u"Затваряне на програмата!"))
        self.m_staticText13.SetLabel(_(u"Излез"))
        
        self.m_staticText53.SetLabel(_(u'Машини'))
        self.m_bpButton6.SetLabel(_(u'Машини'))
        self.m_bpButton6.SetToolTip(_(u'Добавяне и премахване на машини!'))
        
        self.m_staticText54.SetLabel(_(u'Визуализации'))
        self.m_bpButton7.SetLabel(_(u'Визуализации'))
        self.m_bpButton7.SetToolTip(_(u'Добавяне и премахване на визуализации!'))
        
        self.m_staticText55.SetLabel(_(u'Групи'))
        self.m_bpButton8.SetLabel(_(u'Групи'))
        self.m_bpButton8.SetToolTip(_(u'Добавяне и премахване на групи джакпоти!'))
        
        self.m_staticText57.SetLabel(_(u'Сървър'))
        self.m_bpButton10.SetLabel(_(u'Сървър'))
        self.m_bpButton10.SetToolTip(_(u'Информация и регистрация на сървъра!'))
        
        self.m_staticText56.SetLabel(_(u'Събития'))
        self.m_bpButton9.SetLabel(_(u'Събития'))
        self.m_bpButton9.SetToolTip(_(u'Проверка на паднали джакпоти'))
        
        self.m_staticText42.SetLabel(_(u'Опресни'))
        self.m_bpButton111.SetLabel(_(u'Опресни'))
        self.m_bpButton111.SetToolTip(_(u'Изтегляне на информация от сървъра'))
        
        self.m_staticText43.SetLabel(_(u'Запис'))
        self.m_bpButton12.SetLabel(_(u'Запис'))
        self.m_bpButton12.SetToolTip(_(u'Запис на промените на сървъра'))
        
        self.m_staticText58.SetLabel(_(u'Помощ'))
        self.m_bpButton11.SetLabel(_(u'Помощ'))
        self.m_bpButton11.SetToolTip(_(u'Документация на програмата'))

        self.m_staticText131.SetLabel(_(u'Спри'))
        self.m_bpButton41.SetLabel(_(u'Спри'))
        self.m_bpButton41.SetToolTip(_(u'Сървъра спира да върти'))

        self.m_staticText132.SetLabel(_(u'Пусни'))
        self.m_bpButton42.SetLabel(_(u'Пусни'))
        self.m_bpButton42.SetToolTip(_(u'Сървъра започва да върти'))

        self.DB = None
        self.Fit()
    
    def OnStart(self, event):
        response = libs.udp.send('STOP_ROTATION', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, command=False)
        if response == False or response == None:
            wx.MessageBox(_(u'Неуспешно стартиране на сървър!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox(_(u'Успешно стартиране на сървър!'), 'Error', wx.OK | wx.ICON_INFORMATION)
        
    def OnStop(self, event):
        response = libs.udp.send('STOP_ROTATION', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, command=True)
        if response == False or response == None:
            wx.MessageBox(_(u'Неуспешно спиране на сървър!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox(_(u'Успешно спиране на сървър!'), 'Error', wx.OK | wx.ICON_INFORMATION)
        
    def OnGetDB(self, event):
        dial = DBGet(self)
        dial.ShowModal()
    
    def OnSetDB(self, event):
        if self.load_db != self.DB:
            dial = DBSet(self, self.DB)
            dial.ShowModal()
        else:
            dlg = wx.MessageBox(u'Всички настройки ще бъдат възстановени от архив!\nИскате ли да продължите?', 'Warning',
                                wx.YES_NO | wx.ICON_ERROR)

            if dlg == wx.NO:
                return False
            response = libs.udp.send('SET_DB', ip=libs.conf.JPSERVERIP, port=libs.conf.JPSERVERPORT, db=self.DB)
            if response == False or response == None:
                wx.MessageBox(_(u'Неуспешно спиране на сървър!'), 'Error', wx.OK | wx.ICON_ERROR)
            else:
                wx.MessageBox(_(u'Успешно спиране на сървър!'), 'Error', wx.OK | wx.ICON_INFORMATION)

    def OnClose( self, event ):
        self.GetParent().Show()
        self.Destroy()

    def OnUser( self, event ):
        if self.DB == None:
            wx.MessageBox(_(u'Моля изтеглете информация от сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            frame = user.User(self)  # @UndefinedVariable
            frame.ShowModal()

    def OnSMIB(self, event):
        if self.DB == None:
            wx.MessageBox(_(u'Моля изтеглете информация от сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            frame = smib.SMIB(self)
            frame.ShowModal()

    def OnVisual(self, event):
        if self.DB == None:
            wx.MessageBox(_(u'Моля изтеглете информация от сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            frame = visual.Visual(self)
            frame.ShowModal()

    def OnGroup( self, event ):
        if self.DB == None:
            wx.MessageBox(_(u'Моля изтеглете информация от сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            frame = group.Group(self)
            frame.ShowModal()
        
    def OnServer(self, event):
        if self.DB == None:
            wx.MessageBox(_(u'Моля изтеглете информация от сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            frame = server.Server(self)
            frame.ShowModal()
        
    def OnHelp(self, event):
        if libs.conf.DOCS_DEBUG == False:
            frame = libs.helps.Help(r'%s%s/colibri/v%s/jackpot.html' % (libs.conf.DOCS, libs.conf.USE_LANGUAGE, libs.conf.VERSION))
        else:
            frame = libs.helps.Help('http://127.0.0.1:5000/%s/colibri/v%s/jackpot.html' % (libs.conf.USE_LANGUAGE, libs.conf.VERSION))
        
    def OnLog(self, event):
        if self.DB == None:
            wx.MessageBox(_(u'Моля изтеглете информация от сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
#             udp.send('STOP_ROTATION', command=False)
            frame = down_log.LogSelector(self)
            frame.ShowModal()
    
    def OnSave(self, event):
        if self.DB == None:
            wx.MessageBox(_(u'Моля изтеглете информация от сървъра!'), 'Error', wx.OK | wx.ICON_ERROR)
        else:
            try:
                tmp = open(libs.conf.ROOT_PATH + 'jpdump.db', 'rb')
                DB = pickle.load(tmp)
                tmp.close()
                tmp = open(libs.conf.ROOT_PATH + 'jpdump.db', 'wb')
            except FileNotFoundError:
                tmp = open(libs.conf.ROOT_PATH + 'jpdump.db', 'wb')
                DB = {}
            # holder = pysos.Dict(libs.conf.BASE_DIR + '/jpdump.db')
            DB[libs.conf.CASINO_NAME] = self.DB
            pickle.dump(DB, tmp)
            tmp.close()
            # holder.sync()
            # holder.close()
            wx.MessageBox(_(u'Успешен запис на архив!'), 'Info', wx.OK | wx.ICON_INFORMATION)
        
    def OnLoad(self, event):
        try:
            tmp = open(libs.conf.ROOT_PATH + 'jpdump.db', 'rb')
            DB = pickle.load(tmp)
            self.DB = DB[libs.conf.CASINO_NAME]
            self.load_db = DB[libs.conf.CASINO_NAME]
            tmp.close()
        except Exception as e:
            wx.MessageBox(_(u'Липсва архив!'), 'Error', wx.OK | wx.ICON_ERROR)
            try:
                tmp.close()
            except:
                pass
        else:
            wx.MessageBox(_(u'Успешно зареждане на архив!'), 'Info', wx.OK | wx.ICON_INFORMATION)