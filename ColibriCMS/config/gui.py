# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.aui
import wx.richtext

###########################################################################
## Class PosConf
###########################################################################

class PosConf ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer1 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		fgSizer1.Add( self.m_notebook1, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		fgSizer1.Fit( self )

	def __del__( self ):
		pass


###########################################################################
## Class SystemConf
###########################################################################

class SystemConf ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer9 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer8 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer14 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer16 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_calendar2 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 300,-1 ), wx.adv.CAL_SHOW_HOLIDAYS )
		fgSizer16.Add( self.m_calendar2, 0, wx.ALL, 5 )


		fgSizer14.Add( fgSizer16, 1, wx.EXPAND, 5 )

		fgSizer15 = wx.FlexGridSizer( 2, 4, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Час", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer15.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.SP_ARROW_KEYS, 0, 23, 0 )
		fgSizer15.Add( self.m_spinCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer15.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), wx.SP_ARROW_KEYS, 0, 59, 4 )
		fgSizer15.Add( self.m_spinCtrl2, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Свери", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer14.Add( fgSizer15, 1, wx.EXPAND, 5 )


		fgSizer8.Add( fgSizer14, 1, wx.EXPAND, 5 )


		fgSizer9.Add( fgSizer8, 0, 0, 5 )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		gSizer9 = wx.GridSizer( 0, 1, 0, 0 )

		fgSizer21 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer10 = wx.FlexGridSizer( 9, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText13 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Език", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer10.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		fgSizer10.Add( self.m_choice2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText122 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Организатор", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText122.Wrap( -1 )

		self.m_staticText122.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText122.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer10.Add( self.m_staticText122, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText131 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Адрес", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		self.m_staticText131.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText131.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer10.Add( self.m_staticText131, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText141 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Игрална зала", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		self.m_staticText141.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText141.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer10.Add( self.m_staticText141, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText151 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Адрес зала", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		self.m_staticText151.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText151.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer10.Add( self.m_staticText151, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText1511 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Управител", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1511.Wrap( -1 )

		self.m_staticText1511.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText1511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer10.Add( self.m_staticText1511, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl14, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText79 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"ЕИК", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		fgSizer10.Add( self.m_staticText79, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl26, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer21.Add( fgSizer10, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox1 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Дебъг", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox11 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"ДБ Дебъг", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox11, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Цял Екран", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Клавиатура", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox4, 0, wx.ALL, 5 )

		self.m_checkBox35 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Зачисли удържане", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox35, 0, wx.ALL, 5 )

		self.m_checkBox38 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Вход веднъж", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox38, 0, wx.ALL, 5 )

		self.m_checkBox50 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Печат на ордер", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox50, 0, wx.ALL, 5 )

		self.m_checkBox56 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Крупие/име на отчет", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox56, 0, wx.ALL, 5 )

		self.m_checkBox561 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Пари преди отчет", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox561, 0, wx.ALL, 5 )

		self.m_checkBox61 = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Блокирай при точки", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox61, 0, wx.ALL, 5 )


		fgSizer21.Add( bSizer10, 1, wx.EXPAND, 5 )

		self.m_button58 = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"NRA Токен", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button58, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer9.Add( fgSizer21, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( gSizer9 )
		self.m_scrolledWindow2.Layout()
		gSizer9.Fit( self.m_scrolledWindow2 )
		fgSizer9.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( fgSizer9 )
		self.Layout()
		fgSizer9.Fit( self )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnClockSet )
		self.m_button58.Bind( wx.EVT_BUTTON, self.OnNRA )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClockSet( self, event ):
		event.Skip()

	def OnNRA( self, event ):
		event.Skip()

	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class NetworkConf
###########################################################################

class NetworkConf ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 517,422 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer47 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer47.SetFlexibleDirection( wx.BOTH )
		fgSizer47.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_scrolledWindow5 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		fgSizer18 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"UDP" ), wx.VERTICAL )

		self.m_checkBox38 = wx.CheckBox( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Отвори порт", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_checkBox38, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Буфер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		sbSizer10.Add( self.m_staticText32, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_spinCtrl7 = wx.SpinCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1024, 50000, 4096 )
		sbSizer10.Add( self.m_spinCtrl7, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Таймаут", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		sbSizer10.Add( self.m_staticText33, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_spinCtrl8 = wx.SpinCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 10, 1000, 12 )
		sbSizer10.Add( self.m_spinCtrl8, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer26 = wx.StaticBoxSizer( wx.StaticBox( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Redirect" ), wx.VERTICAL )

		fgSizer45 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer45.SetFlexibleDirection( wx.BOTH )
		fgSizer45.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox42 = wx.CheckBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Logging", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.m_checkBox42, 0, wx.ALL, 5 )

		self.m_checkBox40 = wx.CheckBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Часовник", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.m_checkBox40, 0, wx.ALL, 5 )

		self.m_checkBox39 = wx.CheckBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"TCP", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.m_checkBox39, 0, wx.ALL, 5 )

		self.m_checkBox54 = wx.CheckBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Трейд", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.m_checkBox54, 0, wx.ALL, 5 )

		self.m_checkBox74 = wx.CheckBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Скачащ код", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.m_checkBox74, 0, wx.ALL, 5 )

		self.m_checkBox75 = wx.CheckBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"NRA Test", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.m_checkBox75, 0, wx.ALL, 5 )

		self.m_checkBox77 = wx.CheckBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Отключи с OCR", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.m_checkBox77, 0, wx.ALL, 5 )


		fgSizer45.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button61 = wx.Button( sbSizer26.GetStaticBox(), wx.ID_ANY, u"SVN", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer45.Add( self.m_button61, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		fgSizer49 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer49.SetFlexibleDirection( wx.BOTH )
		fgSizer49.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button48 = wx.Button( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Зареди", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.m_button48, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button49 = wx.Button( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.m_button49, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )

		m_radioBox2Choices = [ u"IPTables", u"Ban", u"None" ]
		self.m_radioBox2 = wx.RadioBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Security", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox2.SetSelection( 0 )
		fgSizer49.Add( self.m_radioBox2, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer45.Add( fgSizer49, 1, wx.EXPAND, 5 )


		sbSizer26.Add( fgSizer45, 1, wx.EXPAND, 5 )

		self.m_staticText71 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"E-mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		sbSizer26.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( sbSizer26.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer26.Add( self.m_textCtrl18, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText72 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Subject", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )

		sbSizer26.Add( self.m_staticText72, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( sbSizer26.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer26.Add( self.m_textCtrl19, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText75 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Принтер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		sbSizer26.Add( self.m_staticText75, 0, wx.ALL, 5 )

		m_choice17Choices = []
		self.m_choice17 = wx.Choice( sbSizer26.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice17Choices, 0 )
		self.m_choice17.SetSelection( 0 )
		sbSizer26.Add( self.m_choice17, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText79 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"POS ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		sbSizer26.Add( self.m_staticText79, 0, wx.ALL, 5 )

		m_choice19Choices = []
		self.m_choice19 = wx.Choice( sbSizer26.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice19Choices, 0 )
		self.m_choice19.SetSelection( 0 )
		sbSizer26.Add( self.m_choice19, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer10.Add( sbSizer26, 1, wx.EXPAND, 5 )


		fgSizer18.Add( sbSizer10, 1, wx.EXPAND, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"RTC" ), wx.VERTICAL )

		self.m_checkBox10 = wx.CheckBox( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Използвай RTC сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_checkBox10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		sbSizer11.Add( self.m_checkBox10, 0, wx.ALL, 5 )

		self.m_calendar1 = wx.adv.CalendarCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		sbSizer11.Add( self.m_calendar1, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer15 = wx.FlexGridSizer( 2, 4, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText11 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Час", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer15.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 23, 0 )
		fgSizer15.Add( self.m_spinCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer15.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 59, 4 )
		fgSizer15.Add( self.m_spinCtrl2, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button3 = wx.Button( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Свери", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		sbSizer11.Add( fgSizer15, 1, wx.EXPAND, 5 )


		fgSizer18.Add( sbSizer11, 1, wx.EXPAND, 5 )


		fgSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_scrolledWindow5.SetSizer( fgSizer18 )
		self.m_scrolledWindow5.Layout()
		fgSizer18.Fit( self.m_scrolledWindow5 )
		fgSizer47.Add( self.m_scrolledWindow5, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer14 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer47.Add( gSizer14, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer47 )
		self.Layout()

		# Connect Events
		self.m_checkBox39.Bind( wx.EVT_CHECKBOX, self.OnTCP )
		self.m_button61.Bind( wx.EVT_BUTTON, self.OnVNCPasswd )
		self.m_button48.Bind( wx.EVT_BUTTON, self.OnLoadConf )
		self.m_button49.Bind( wx.EVT_BUTTON, self.OnSaveConf )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnClockSet )
		self.m_button11.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnTCP( self, event ):
		event.Skip()

	def OnVNCPasswd( self, event ):
		event.Skip()

	def OnLoadConf( self, event ):
		event.Skip()

	def OnSaveConf( self, event ):
		event.Skip()

	def OnClockSet( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class PrinterRFIDConf
###########################################################################

class PrinterRFIDConf ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer11 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,500 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		fgSizer44 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer44.SetFlexibleDirection( wx.BOTH )
		fgSizer44.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"Print" ), wx.VERTICAL )

		fgSizer13 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_checkBox6 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Директен Печат", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_checkBox6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		sbSizer4.Add( self.m_checkBox6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox39 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"POS Printer", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBox39, 0, wx.ALL, 5 )

		self.m_checkBox44 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Печат на сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBox44, 0, wx.ALL, 5 )

		self.m_checkBox51 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Директен Печат POS", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBox51, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox52 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Печат на сървър POS", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBox52, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox58 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Мънибек на POS", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_checkBox58, 0, wx.ALL, 5 )

		sbSizer28 = wx.StaticBoxSizer( wx.StaticBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"OCR" ), wx.VERTICAL )

		self.m_checkBox76 = wx.CheckBox( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Наличен", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer28.Add( self.m_checkBox76, 0, wx.ALL, 5 )

		self.m_checkBox78 = wx.CheckBox( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Desko", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer28.Add( self.m_checkBox78, 0, wx.ALL, 5 )

		self.m_staticText85 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Порт", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		sbSizer28.Add( self.m_staticText85, 0, wx.ALL, 5 )

		self.m_textCtrl30 = wx.TextCtrl( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer28.Add( self.m_textCtrl30, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer4.Add( sbSizer28, 1, wx.EXPAND, 5 )


		fgSizer13.Add( sbSizer4, 1, wx.EXPAND, 5 )

		fgSizer12 = wx.FlexGridSizer( 9, 0, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText76 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Програма за PDF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )

		fgSizer12.Add( self.m_staticText76, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl6 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText18 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Принтер по подразбиране", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer12.Add( self.m_staticText18, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer14.Add( self.m_choice2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl28 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl28.Hide()

		bSizer14.Add( self.m_textCtrl28, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )

		self.m_staticText68 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"POS Принтер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		fgSizer12.Add( self.m_staticText68, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		m_choice15Choices = []
		self.m_choice15 = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice15Choices, 0 )
		self.m_choice15.SetSelection( 0 )
		bSizer13.Add( self.m_choice15, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl29 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl29.Hide()

		bSizer13.Add( self.m_textCtrl29, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )

		self.m_staticText69 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Размер на хартия", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		fgSizer12.Add( self.m_staticText69, 0, wx.ALL, 5 )

		gSizer19 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_spinCtrl24 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, u"72", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 10, 500, 0 )
		gSizer19.Add( self.m_spinCtrl24, 0, wx.ALL, 5 )

		self.m_spinCtrl25 = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, u"115", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 10, 2000, 0 )
		gSizer19.Add( self.m_spinCtrl25, 0, wx.ALL, 5 )


		fgSizer12.Add( gSizer19, 1, wx.EXPAND, 5 )

		gSizer20 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button47 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Тест POS Принтер", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer20.Add( self.m_button47, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button471 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Добави инфо", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer20.Add( self.m_button471, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer12.Add( gSizer20, 1, wx.EXPAND, 5 )


		fgSizer13.Add( fgSizer12, 1, wx.EXPAND, 5 )


		sbSizer5.Add( fgSizer13, 1, wx.EXPAND, 5 )


		fgSizer44.Add( sbSizer5, 1, wx.EXPAND, 5 )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"RFID" ), wx.VERTICAL )

		self.m_staticText20 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Порт", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		sbSizer6.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_checkBox8 = wx.CheckBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Използвай четец", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox8.SetValue(True)
		sbSizer6.Add( self.m_checkBox8, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, u"/dev/ttyACM0", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.m_textCtrl7, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"RFID" ), wx.VERTICAL )

		self.m_staticText26 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Скорост ( серийна комуникация )", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText26.Wrap( -1 )

		self.m_staticText26.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText26.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		sbSizer7.Add( self.m_staticText26, 0, wx.ALL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		sbSizer7.Add( self.m_choice3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText27 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Таймаут ( секунди )", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText27.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		sbSizer7.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_spinCtrl5 = wx.SpinCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 60, 1 )
		sbSizer7.Add( self.m_spinCtrl5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Време на сканиране ( мили секунди )", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		sbSizer7.Add( self.m_staticText22, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_spinCtrl3 = wx.SpinCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1000, 500 )
		sbSizer7.Add( self.m_spinCtrl3, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer27 = wx.StaticBoxSizer( wx.StaticBox( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Update RFID" ), wx.VERTICAL )

		self.m_filePicker3 = wx.FilePickerCtrl( sbSizer27.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer27.Add( self.m_filePicker3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button54 = wx.Button( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer27.Add( self.m_button54, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer7.Add( sbSizer27, 1, wx.EXPAND, 5 )


		sbSizer6.Add( sbSizer7, 1, wx.EXPAND, 5 )


		fgSizer44.Add( sbSizer6, 1, wx.EXPAND, 5 )

		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )


		fgSizer44.Add( sbSizer16, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow3.SetSizer( fgSizer44 )
		self.m_scrolledWindow3.Layout()
		fgSizer11.Add( self.m_scrolledWindow3, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )


		fgSizer11.Add( gSizer5, 1, wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer11.Add( gSizer6, 1, wx.EXPAND|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( fgSizer11 )
		self.Layout()
		fgSizer11.Fit( self )

		# Connect Events
		self.m_checkBox78.Bind( wx.EVT_CHECKBOX, self.PortChange )
		self.m_button47.Bind( wx.EVT_BUTTON, self.OnPosPrinterTest )
		self.m_button471.Bind( wx.EVT_BUTTON, self.OnAddPosPrinterInfo )
		self.m_button54.Bind( wx.EVT_BUTTON, self.UpdateRFID )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def PortChange( self, event ):
		event.Skip()

	def OnPosPrinterTest( self, event ):
		event.Skip()

	def OnAddPosPrinterInfo( self, event ):
		event.Skip()

	def UpdateRFID( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class POS
###########################################################################

class POS ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer14 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_listCtrl1.SetForegroundColour( wx.Colour( 0, 166, 6 ) )

		fgSizer14.Add( self.m_listCtrl1, 0, wx.ALL, 5 )

		fgSizer16 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Инсталирай", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_button7, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Премахни", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_button8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Инициализация", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_button20, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer14.Add( fgSizer16, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer14 )
		self.Layout()
		fgSizer14.Fit( self )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnInstall )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnRemove )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnReset )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnInstall( self, event ):
		event.Skip()

	def OnRemove( self, event ):
		event.Skip()

	def OnReset( self, event ):
		event.Skip()


###########################################################################
## Class POSInstall
###########################################################################

class POSInstall ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 299,249 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer24 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Име на терминала", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText30.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer24.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_textCtrl11.SetMinSize( wx.Size( 100,-1 ) )

		gSizer24.Add( self.m_textCtrl11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"ID на терминала", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText29.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer24.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_textCtrl10.SetMinSize( wx.Size( 100,-1 ) )

		gSizer24.Add( self.m_textCtrl10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		gSizer13 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_button9, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer24.Add( gSizer13, 0, wx.EXPAND, 5 )


		self.SetSizer( gSizer24 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button10.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class PosPrinterConf
###########################################################################

class PosPrinterConf ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Настройки POS Принтер", pos = wx.DefaultPosition, size = wx.Size( 467,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer21 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, u"Обект", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		gSizer21.Add( self.m_staticText69, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl15.SetMaxLength( 28 )
		gSizer21.Add( self.m_textCtrl15, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText70 = wx.StaticText( self, wx.ID_ANY, u"Населено място", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )

		gSizer21.Add( self.m_staticText70, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl16.SetMaxLength( 28 )
		gSizer21.Add( self.m_textCtrl16, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Адрес", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		gSizer21.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl17.SetMaxLength( 28 )
		gSizer21.Add( self.m_textCtrl17, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button50 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.m_button50, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button51 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.m_button51, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer21.Add( gSizer22, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer21 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button50.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button51.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class KeySystem
###########################################################################

class KeySystem ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer18 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_checkBox10 = wx.CheckBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Скачащ код", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.m_checkBox10, 0, wx.ALL, 5 )

		self.m_checkBox59 = wx.CheckBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Промени при отчет", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.m_checkBox59, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.m_button24, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer18.Add( sbSizer12, 1, wx.EXPAND, 5 )

		fgSizer20 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Избери машина", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		fgSizer20.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice6Choices = []
		self.m_choice6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		fgSizer20.Add( self.m_choice6, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer28 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer28.SetFlexibleDirection( wx.BOTH )
		fgSizer28.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Добави кредит", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer28.Add( self.m_button14, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Добави owner", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer28.Add( self.m_button12, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer20.Add( fgSizer28, 1, wx.EXPAND, 5 )

		self.m_button55 = wx.Button( self, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_button55, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer18.Add( fgSizer20, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer18 )
		self.Layout()
		fgSizer18.Fit( self )

		# Connect Events
		self.m_button24.Bind( wx.EVT_BUTTON, self.OnChangeConf )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnAddCredit )
		self.m_button12.Bind( wx.EVT_BUTTON, self.OnAddOwner )
		self.m_button55.Bind( wx.EVT_BUTTON, self.OnReset )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnChangeConf( self, event ):
		event.Skip()

	def OnAddCredit( self, event ):
		event.Skip()

	def OnAddOwner( self, event ):
		event.Skip()

	def OnReset( self, event ):
		event.Skip()


###########################################################################
## Class KSGuage
###########################################################################

class KSGuage ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		bSizer15.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button23, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()
		bSizer15.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button23.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class Update
###########################################################################

class Update ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer22 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"SMIB" ), wx.VERTICAL )

		self.m_filePicker2 = wx.FilePickerCtrl( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker2.Hide()

		sbSizer14.Add( self.m_filePicker2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button421 = wx.Button( sbSizer14.GetStaticBox(), wx.ID_ANY, u"Unix Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button421.Hide()

		sbSizer14.Add( self.m_button421, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button29 = wx.Button( sbSizer14.GetStaticBox(), wx.ID_ANY, u"Auto Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer14.Add( self.m_button29, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer22.Add( sbSizer14, 1, wx.EXPAND, 5 )

		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"CMS" ), wx.VERTICAL )

		self.m_checkBox43 = wx.CheckBox( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Добави минимална ревизия", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer16.Add( self.m_checkBox43, 0, wx.ALL, 5 )

		self.m_button31 = wx.Button( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Auto Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer16.Add( self.m_button31, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer22.Add( sbSizer16, 0, wx.EXPAND, 5 )

		sbSizer25 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"RedirectServer" ), wx.VERTICAL )

		self.m_checkBox54 = wx.CheckBox( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Миграция", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer25.Add( self.m_checkBox54, 0, wx.ALL, 5 )

		self.m_button41 = wx.Button( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Auto Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer25.Add( self.m_button41, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer22.Add( sbSizer25, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer22 )
		self.Layout()
		fgSizer22.Fit( self )

		# Connect Events
		self.m_button421.Bind( wx.EVT_BUTTON, self.SMIBUnixUpdate )
		self.m_button29.Bind( wx.EVT_BUTTON, self.SMIBAutoUpdate )
		self.m_button31.Bind( wx.EVT_BUTTON, self.OnMainAutoUpdate )
		self.m_button41.Bind( wx.EVT_BUTTON, self.OnRedirectUpdate )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def SMIBUnixUpdate( self, event ):
		event.Skip()

	def SMIBAutoUpdate( self, event ):
		event.Skip()

	def OnMainAutoUpdate( self, event ):
		event.Skip()

	def OnRedirectUpdate( self, event ):
		event.Skip()


###########################################################################
## Class DB
###########################################################################

class DB ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer9 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer8 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer13 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Архивиране", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer13.Add( self.m_staticText7, 0, wx.ALL, 5 )

		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker2.SetMinSize( wx.Size( 300,-1 ) )

		fgSizer19.Add( self.m_dirPicker2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Архивирай", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_button48, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_filePicker4 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fgSizer19.Add( self.m_filePicker4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button49 = wx.Button( self, wx.ID_ANY, u"Възтанови", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.m_button49, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer13.Add( fgSizer19, 1, wx.EXPAND, 5 )


		fgSizer8.Add( fgSizer13, 1, wx.EXPAND, 5 )

		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button43 = wx.Button( self, wx.ID_ANY, u"Почисти База", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.m_button43, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button50 = wx.Button( self, wx.ID_ANY, u"Почисти SMIBLog", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.m_button50, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer8.Add( gSizer22, 1, wx.EXPAND, 5 )

		gSizer18 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button46 = wx.Button( self, wx.ID_ANY, u"Вакумирай", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer18.Add( self.m_button46, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button47 = wx.Button( self, wx.ID_ANY, u"Ново индексиране", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer18.Add( self.m_button47, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer8.Add( gSizer18, 1, wx.EXPAND, 5 )


		fgSizer9.Add( fgSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer9 )
		self.Layout()
		fgSizer9.Fit( self )

		# Connect Events
		self.m_button48.Bind( wx.EVT_BUTTON, self.OnBackup )
		self.m_button49.Bind( wx.EVT_BUTTON, self.OnRestory )
		self.m_button43.Bind( wx.EVT_BUTTON, self.OnCleanOldData )
		self.m_button50.Bind( wx.EVT_BUTTON, self.SMIBLogClean )
		self.m_button46.Bind( wx.EVT_BUTTON, self.OnVakum )
		self.m_button47.Bind( wx.EVT_BUTTON, self.OnReindex )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnBackup( self, event ):
		event.Skip()

	def OnRestory( self, event ):
		event.Skip()

	def OnCleanOldData( self, event ):
		event.Skip()

	def SMIBLogClean( self, event ):
		event.Skip()

	def OnVakum( self, event ):
		event.Skip()

	def OnReindex( self, event ):
		event.Skip()


###########################################################################
## Class SMIB
###########################################################################

class SMIB ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer30 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer30.SetFlexibleDirection( wx.BOTH )
		fgSizer30.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer13 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"SMIB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText33.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer13.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		m_choice7Choices = []
		self.m_choice7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice7Choices, 0 )
		self.m_choice7.SetSelection( 0 )
		gSizer13.Add( self.m_choice7, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer30.Add( gSizer13, 1, wx.EXPAND, 5 )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 850,500 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		fgSizer32 = wx.FlexGridSizer( 3, 3, 0, 0 )
		fgSizer32.SetFlexibleDirection( wx.BOTH )
		fgSizer32.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"PROC" ), wx.VERTICAL )

		fgSizer391 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer391.SetFlexibleDirection( wx.BOTH )
		fgSizer391.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox21 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"RFID", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer391.Add( self.m_checkBox21, 0, wx.ALL, 5 )

		self.m_checkBox20 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"SAS", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer391.Add( self.m_checkBox20, 0, wx.ALL, 5 )

		self.m_checkBox25 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Джакпот сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer391.Add( self.m_checkBox25, 0, wx.ALL, 5 )

		self.m_checkBox24 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Клиентски карти", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer391.Add( self.m_checkBox24, 0, wx.ALL, 5 )

		self.m_checkBox22 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Кей Система", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer391.Add( self.m_checkBox22, 0, wx.ALL, 5 )

		self.m_checkBox23 = wx.CheckBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Бонус Карти", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer391.Add( self.m_checkBox23, 0, wx.ALL, 5 )


		sbSizer20.Add( fgSizer391, 1, wx.EXPAND, 5 )

		sbSizer261 = wx.StaticBoxSizer( wx.StaticBox( sbSizer20.GetStaticBox(), wx.ID_ANY, u"Client" ), wx.VERTICAL )

		self.m_staticText801 = wx.StaticText( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Език", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText801.Wrap( -1 )

		sbSizer261.Add( self.m_staticText801, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice181Choices = []
		self.m_choice181 = wx.Choice( sbSizer261.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice181Choices, 0 )
		self.m_choice181.SetSelection( 0 )
		sbSizer261.Add( self.m_choice181, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox51 = wx.CheckBox( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Превърти по бет", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer261.Add( self.m_checkBox51, 0, wx.ALL, 5 )

		self.m_checkBox30 = wx.CheckBox( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Заключи бил без клиент", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox30.SetValue(True)
		sbSizer261.Add( self.m_checkBox30, 0, wx.ALL, 5 )

		self.m_checkBox321 = wx.CheckBox( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Заключи без клиент", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer261.Add( self.m_checkBox321, 0, wx.ALL, 5 )

		self.m_checkBox54 = wx.CheckBox( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Зареди Видео", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer261.Add( self.m_checkBox54, 0, wx.ALL, 5 )

		self.m_checkBox79 = wx.CheckBox( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Мънибек", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer261.Add( self.m_checkBox79, 0, wx.ALL, 5 )

		fgSizer39 = wx.FlexGridSizer( 5, 2, 0, 0 )
		fgSizer39.SetFlexibleDirection( wx.BOTH )
		fgSizer39.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText522 = wx.StaticText( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Таймаут", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText522.Wrap( -1 )

		fgSizer39.Add( self.m_staticText522, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl201 = wx.SpinCtrl( sbSizer261.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 2, 50, 4 )
		fgSizer39.Add( self.m_spinCtrl201, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText682 = wx.StaticText( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Кредит", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText682.Wrap( -1 )

		fgSizer39.Add( self.m_staticText682, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl211 = wx.SpinCtrl( sbSizer261.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 1 )
		fgSizer39.Add( self.m_spinCtrl211, 0, wx.ALL, 5 )

		self.m_staticText77 = wx.StaticText( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Лого", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		self.m_staticText77.Hide()

		fgSizer39.Add( self.m_staticText77, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl231 = wx.TextCtrl( sbSizer261.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl231.Hide()

		fgSizer39.Add( self.m_textCtrl231, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText802 = wx.StaticText( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Номер на Видео", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText802.Wrap( -1 )

		fgSizer39.Add( self.m_staticText802, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl28 = wx.SpinCtrl( sbSizer261.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 0 )
		fgSizer39.Add( self.m_spinCtrl28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText81 = wx.StaticText( sbSizer261.GetStaticBox(), wx.ID_ANY, u"Skin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer39.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl29 = wx.SpinCtrl( sbSizer261.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10, 1 )
		fgSizer39.Add( self.m_spinCtrl29, 0, wx.ALL, 5 )


		sbSizer261.Add( fgSizer39, 1, wx.EXPAND, 5 )


		sbSizer20.Add( sbSizer261, 1, wx.EXPAND, 5 )


		fgSizer32.Add( sbSizer20, 1, wx.EXPAND, 5 )

		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"SAS" ), wx.VERTICAL )

		fgSizer33 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer33.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer49 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer49.SetFlexibleDirection( wx.BOTH )
		fgSizer49.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText80 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Конфигурация", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		fgSizer49.Add( self.m_staticText80, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice18Choices = []
		self.m_choice18 = wx.Choice( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice18Choices, 0 )
		self.m_choice18.SetSelection( 0 )
		fgSizer49.Add( self.m_choice18, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer33.Add( fgSizer49, 1, wx.EXPAND, 5 )


		fgSizer33.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_checkBox52 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"N0x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox52.SetValue(True)
		self.m_checkBox52.Hide()

		fgSizer33.Add( self.m_checkBox52, 0, wx.ALL, 5 )


		fgSizer33.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer33.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_checkBox27 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Свери час", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.m_checkBox27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox26 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"SAS Сигурност", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.m_checkBox26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox311 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Провери за игра", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.m_checkBox311, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox28 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"AFT", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.m_checkBox28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox56 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Без транзакция", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.m_checkBox56, 0, wx.ALL, 5 )

		self.m_checkBox62 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Джакпот към аут", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox62.SetValue(True)
		fgSizer33.Add( self.m_checkBox62, 0, wx.ALL, 5 )

		self.m_checkBox281 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"USB2RS", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.m_checkBox281, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox39 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Забави рилл", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.m_checkBox39, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox80 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Транзакция от ЕМГ", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.m_checkBox80, 0, wx.ALL, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		sbSizer301 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_checkBox42 = wx.CheckBox( sbSizer301.GetStaticBox(), wx.ID_ANY, u"Спри аутоплей", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer301.Add( self.m_checkBox42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl27 = wx.SpinCtrl( sbSizer301.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 86400, 0 )
		sbSizer301.Add( self.m_spinCtrl27, 0, wx.ALL, 5 )

		self.m_spinCtrl26 = wx.SpinCtrl( sbSizer301.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 0 )
		sbSizer301.Add( self.m_spinCtrl26, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer21.Add( sbSizer301, 1, wx.EXPAND, 5 )


		fgSizer33.Add( bSizer21, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText90 = wx.StaticText( sbSizer31.GetStaticBox(), wx.ID_ANY, u"SAS Номер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )

		sbSizer31.Add( self.m_staticText90, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( sbSizer31.GetStaticBox(), wx.ID_ANY, u"00", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer31.Add( self.m_textCtrl22, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer22.Add( sbSizer31, 1, wx.EXPAND, 5 )


		fgSizer33.Add( bSizer22, 1, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		sbSizer291 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText92 = wx.StaticText( sbSizer291.GetStaticBox(), wx.ID_ANY, u"Сериен таймаут", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )

		sbSizer291.Add( self.m_staticText92, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( sbSizer291.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer291.Add( self.m_textCtrl24, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer291.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer24.Add( sbSizer291, 1, wx.EXPAND, 5 )


		fgSizer33.Add( bSizer24, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox391 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Забави падане", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_checkBox391, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, u"0.04", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_textCtrl23, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer33.Add( bSizer25, 1, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText89 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"AFT заключване", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )

		bSizer26.Add( self.m_staticText89, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl30 = wx.SpinCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0 )
		bSizer26.Add( self.m_spinCtrl30, 0, wx.ALL, 5 )


		fgSizer33.Add( bSizer26, 1, wx.EXPAND, 5 )


		fgSizer33.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		sbSizer23.Add( fgSizer33, 1, wx.EXPAND, 5 )

		sbSizer26 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Bonus" ), wx.HORIZONTAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText43 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Удържане над", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		bSizer6.Add( self.m_staticText43, 0, wx.ALL, 5 )

		self.m_spinCtrl19 = wx.SpinCtrl( sbSizer26.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 1 )
		bSizer6.Add( self.m_spinCtrl19, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer251 = wx.StaticBoxSizer( wx.StaticBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"RFID" ), wx.VERTICAL )

		fgSizer42 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox63 = wx.CheckBox( sbSizer251.GetStaticBox(), wx.ID_ANY, u"RC255", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.m_checkBox63, 0, wx.ALL, 5 )


		fgSizer42.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText67 = wx.StaticText( sbSizer251.GetStaticBox(), wx.ID_ANY, u"Scantime", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( -1 )

		fgSizer42.Add( self.m_staticText67, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl22 = wx.SpinCtrl( sbSizer251.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1000, 500 )
		fgSizer42.Add( self.m_spinCtrl22, 0, wx.ALL, 5 )

		self.m_staticText68 = wx.StaticText( sbSizer251.GetStaticBox(), wx.ID_ANY, u"Timeout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		fgSizer42.Add( self.m_staticText68, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spinCtrl23 = wx.SpinCtrl( sbSizer251.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 60, 0 )
		fgSizer42.Add( self.m_spinCtrl23, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer251.Add( fgSizer42, 1, wx.EXPAND, 5 )

		self.m_button391 = wx.Button( sbSizer251.GetStaticBox(), wx.ID_ANY, u"Запиши Четец", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer251.Add( self.m_button391, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( sbSizer251, 1, wx.EXPAND, 5 )


		sbSizer26.Add( bSizer6, 0, 0, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText42 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Изтрий на буфдер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		bSizer7.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.m_spinCtrl18 = wx.SpinCtrl( sbSizer26.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 120, 2 )
		bSizer7.Add( self.m_spinCtrl18, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer252 = wx.StaticBoxSizer( wx.StaticBox( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Mail Send" ), wx.VERTICAL )

		self.m_checkBox341 = wx.CheckBox( sbSizer252.GetStaticBox(), wx.ID_ANY, u"Уведоми при печалба", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer252.Add( self.m_checkBox341, 0, wx.ALL, 5 )

		self.m_staticText681 = wx.StaticText( sbSizer252.GetStaticBox(), wx.ID_ANY, u"Сума", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText681.Wrap( -1 )

		sbSizer252.Add( self.m_staticText681, 0, wx.ALL, 5 )

		self.m_spinCtrl24 = wx.SpinCtrl( sbSizer252.GetStaticBox(), wx.ID_ANY, u"2000", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 100, 50000, 2000 )
		sbSizer252.Add( self.m_spinCtrl24, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( sbSizer252, 1, wx.EXPAND, 5 )


		sbSizer26.Add( bSizer7, 0, 0, 5 )


		sbSizer23.Add( sbSizer26, 1, wx.EXPAND, 5 )


		fgSizer32.Add( sbSizer23, 1, wx.EXPAND, 5 )

		sbSizer24 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Jackpot" ), wx.VERTICAL )

		self.m_checkBox31 = wx.CheckBox( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Изплащане на ръка", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer24.Add( self.m_checkBox31, 0, wx.ALL, 5 )

		self.m_checkBox57 = wx.CheckBox( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Използвай AFT", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer24.Add( self.m_checkBox57, 0, wx.ALL, 5 )

		fgSizer34 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox29 = wx.CheckBox( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Заключи при загуба", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer34.Add( self.m_checkBox29, 0, wx.ALL, 5 )

		gSizer23 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText37 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Брой Грешки", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		gSizer23.Add( self.m_staticText37, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_spinCtrl13 = wx.SpinCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 2, 100, 20 )
		gSizer23.Add( self.m_spinCtrl13, 0, wx.ALL|wx.EXPAND|wx.ALIGN_BOTTOM, 5 )


		fgSizer34.Add( gSizer23, 1, wx.EXPAND, 5 )

		gSizer24 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText38 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Падане при кредит", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		gSizer24.Add( self.m_staticText38, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_spinCtrl14 = wx.SpinCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 1 )
		gSizer24.Add( self.m_spinCtrl14, 0, wx.ALL|wx.EXPAND|wx.ALIGN_BOTTOM, 5 )


		fgSizer34.Add( gSizer24, 1, wx.EXPAND, 5 )


		sbSizer24.Add( fgSizer34, 1, wx.EXPAND, 5 )

		sbSizer29 = wx.StaticBoxSizer( wx.StaticBox( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Log Server" ), wx.VERTICAL )

		self.m_checkBox35 = wx.CheckBox( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Изпращай към сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer29.Add( self.m_checkBox35, 0, wx.ALL, 5 )

		self.m_staticText54 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		sbSizer29.Add( self.m_staticText54, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( sbSizer29.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer29.Add( self.m_textCtrl14, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText521 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Ниво", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText521.Wrap( -1 )

		sbSizer29.Add( self.m_staticText521, 0, wx.ALL, 5 )

		m_choice16Choices = []
		self.m_choice16 = wx.Choice( sbSizer29.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice16Choices, 0 )
		self.m_choice16.SetSelection( 0 )
		sbSizer29.Add( self.m_choice16, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer24.Add( sbSizer29, 1, wx.EXPAND, 5 )


		fgSizer32.Add( sbSizer24, 1, wx.EXPAND, 5 )

		sbSizer25 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Keysystem" ), wx.HORIZONTAL )

		fgSizer35 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox32 = wx.CheckBox( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Много ключове", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.m_checkBox32, 0, wx.ALL, 5 )

		self.m_checkBox33 = wx.CheckBox( sbSizer25.GetStaticBox(), wx.ID_ANY, u"AFT", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.m_checkBox33, 0, wx.ALL, 5 )

		self.m_button431 = wx.Button( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Тест на реле", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.m_button431, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer25.Add( fgSizer35, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText39 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Кредит", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer5.Add( self.m_staticText39, 0, wx.ALL, 5 )

		self.m_spinCtrl15 = wx.SpinCtrl( sbSizer25.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 2, 2 )
		bSizer5.Add( self.m_spinCtrl15, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText40 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Отчет", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		bSizer5.Add( self.m_staticText40, 0, wx.ALL, 5 )

		self.m_spinCtrl16 = wx.SpinCtrl( sbSizer25.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 2, 0 )
		bSizer5.Add( self.m_spinCtrl16, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText79 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Таймаут", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		bSizer5.Add( self.m_staticText79, 0, wx.ALL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( sbSizer25.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl26, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer25.Add( bSizer5, 1, wx.EXPAND, 5 )


		fgSizer32.Add( sbSizer25, 1, wx.EXPAND, 5 )

		sbSizer27 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"System" ), wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox47 = wx.CheckBox( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Проверка процеси", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox47, 0, wx.ALL, 5 )

		self.m_checkBox48 = wx.CheckBox( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Проверка нет", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox48, 0, wx.ALL, 5 )

		self.m_checkBox50 = wx.CheckBox( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Проверка система", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_checkBox50, 0, wx.ALL, 5 )


		sbSizer27.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox34 = wx.CheckBox( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Рестарт при грешка", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_checkBox34, 0, wx.ALL, 5 )

		self.m_checkBox49 = wx.CheckBox( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Лог фаил", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_checkBox49, 0, wx.ALL, 5 )


		sbSizer27.Add( bSizer11, 1, wx.EXPAND, 5 )

		fgSizer36 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText44 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Интервал на проверка", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		fgSizer36.Add( self.m_staticText44, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Критична температура", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		fgSizer36.Add( self.m_staticText45, 0, wx.ALL, 5 )

		self.m_spinCtrl20 = wx.SpinCtrl( sbSizer27.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 60, 5000, 600 )
		fgSizer36.Add( self.m_spinCtrl20, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_spinCtrl21 = wx.SpinCtrl( sbSizer27.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 75, 100, 90 )
		fgSizer36.Add( self.m_spinCtrl21, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer27.Add( fgSizer36, 1, wx.EXPAND, 5 )


		fgSizer32.Add( sbSizer27, 1, wx.EXPAND, 5 )


		fgSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		sbSizer30 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Control" ), wx.HORIZONTAL )

		fgSizer401 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer401.SetFlexibleDirection( wx.BOTH )
		fgSizer401.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_button38 = wx.Button( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Покажи лог", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button38, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button42 = wx.Button( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Включи деноминация", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button42, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer401.Add( bSizer18, 1, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_button39 = wx.Button( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Нулирай", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_button39, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button40 = wx.Button( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Изключи от джакпот", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_button40, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer401.Add( bSizer19, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_button37 = wx.Button( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Авто Ъпдейт", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button37, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button36 = wx.Button( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Рестарт", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button36, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer401.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button41 = wx.Button( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Изключи деноминация", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button41, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button43 = wx.Button( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Включи в джакпот", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button43, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer401.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer191 = wx.BoxSizer( wx.VERTICAL )

		self.m_button62 = wx.Button( sbSizer30.GetStaticBox(), wx.ID_ANY, u"SAS Tester", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.m_button62, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer401.Add( bSizer191, 1, wx.EXPAND, 5 )


		sbSizer30.Add( fgSizer401, 1, wx.EXPAND, 5 )


		fgSizer32.Add( sbSizer30, 1, wx.EXPAND, 5 )

		sbSizer28 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"Log config" ), wx.VERTICAL )

		fgSizer40 = wx.FlexGridSizer( 4, 4, 0, 0 )
		fgSizer40.SetFlexibleDirection( wx.BOTH )
		fgSizer40.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText48 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Сървър", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		fgSizer40.Add( self.m_staticText48, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice10Choices = []
		self.m_choice10 = wx.Choice( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice10Choices, 0 )
		self.m_choice10.SetSelection( 0 )
		fgSizer40.Add( self.m_choice10, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"RFID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		fgSizer40.Add( self.m_staticText49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice11Choices = []
		self.m_choice11 = wx.Choice( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		fgSizer40.Add( self.m_choice11, 0, wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Система", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		fgSizer40.Add( self.m_staticText46, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice8Choices = []
		self.m_choice8 = wx.Choice( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice8Choices, 0 )
		self.m_choice8.SetSelection( 0 )
		fgSizer40.Add( self.m_choice8, 0, wx.ALL, 5 )

		self.m_staticText47 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"SAS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		fgSizer40.Add( self.m_staticText47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice9Choices = []
		self.m_choice9 = wx.Choice( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice9Choices, 0 )
		self.m_choice9.SetSelection( 0 )
		fgSizer40.Add( self.m_choice9, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Кей система", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		fgSizer40.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice12Choices = []
		self.m_choice12 = wx.Choice( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice12Choices, 0 )
		self.m_choice12.SetSelection( 0 )
		fgSizer40.Add( self.m_choice12, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Бонус Карти", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer40.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice13Choices = []
		self.m_choice13 = wx.Choice( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice13Choices, 0 )
		self.m_choice13.SetSelection( 0 )
		fgSizer40.Add( self.m_choice13, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Джакпот", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer40.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice14Choices = []
		self.m_choice14 = wx.Choice( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice14Choices, 0 )
		self.m_choice14.SetSelection( 0 )
		fgSizer40.Add( self.m_choice14, 0, wx.ALL, 5 )

		self.m_staticText53 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Клиенти", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		fgSizer40.Add( self.m_staticText53, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice15Choices = []
		self.m_choice15 = wx.Choice( sbSizer28.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice15Choices, 0 )
		self.m_choice15.SetSelection( 0 )
		fgSizer40.Add( self.m_choice15, 0, wx.ALL, 5 )


		sbSizer28.Add( fgSizer40, 1, wx.EXPAND, 5 )


		fgSizer32.Add( sbSizer28, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( fgSizer32 )
		self.m_scrolledWindow2.Layout()
		fgSizer30.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button35 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_button35, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer30.Add( gSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer30 )
		self.Layout()
		fgSizer30.Fit( self )

		# Connect Events
		self.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice7.Bind( wx.EVT_CHOICE, self.OnLoad )
		self.m_choice7.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox21.Bind( wx.EVT_CHECKBOX, self.rfid_proc )
		self.m_checkBox21.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox20.Bind( wx.EVT_CHECKBOX, self.sas_proc )
		self.m_checkBox20.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox25.Bind( wx.EVT_CHECKBOX, self.jp_proc )
		self.m_checkBox25.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox24.Bind( wx.EVT_CHECKBOX, self.client_proc )
		self.m_checkBox24.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox22.Bind( wx.EVT_CHECKBOX, self.keysystem_proc )
		self.m_checkBox22.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox23.Bind( wx.EVT_CHECKBOX, self.bonus_proc )
		self.m_checkBox23.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox30.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox321.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl201.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl211.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice18.Bind( wx.EVT_CHOICE, self.OnConfig )
		self.m_checkBox27.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox26.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox311.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox28.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox281.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox42.Bind( wx.EVT_CHECKBOX, self.AutoplayEditable )
		self.m_checkBox391.Bind( wx.EVT_CHECKBOX, self.TimeSleepEditable )
		self.m_spinCtrl19.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl22.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl23.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button391.Bind( wx.EVT_BUTTON, self.OnRFIDScanTime )
		self.m_button391.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl18.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox341.Bind( wx.EVT_CHECKBOX, self.OnSendMailIfWon )
		self.m_checkBox31.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox29.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl13.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl14.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox35.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_textCtrl14.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice16.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox32.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox33.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button431.Bind( wx.EVT_BUTTON, self.OnRelayTest )
		self.m_button431.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl15.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl16.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_checkBox34.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl20.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_spinCtrl21.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button38.Bind( wx.EVT_BUTTON, self.OnLogGet )
		self.m_button38.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button42.Bind( wx.EVT_BUTTON, self.enable_denomination )
		self.m_button42.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button39.Bind( wx.EVT_BUTTON, self.OnReset )
		self.m_button39.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button40.Bind( wx.EVT_BUTTON, self.OnDisableJP )
		self.m_button40.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button37.Bind( wx.EVT_BUTTON, self.OnAutoUpdate )
		self.m_button37.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button36.Bind( wx.EVT_BUTTON, self.OnReboot )
		self.m_button36.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button41.Bind( wx.EVT_BUTTON, self.OnDisableDenom )
		self.m_button41.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button43.Bind( wx.EVT_BUTTON, self.jackpot_enable )
		self.m_button43.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button62.Bind( wx.EVT_BUTTON, self.SAS_Tester )
		self.m_choice10.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice11.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice8.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice9.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice12.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice13.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice14.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_choice15.Bind( wx.EVT_SET_FOCUS, self.OnPassFocus )
		self.m_button35.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnPassFocus( self, event ):
		event.Skip()

	def OnLoad( self, event ):
		event.Skip()


	def rfid_proc( self, event ):
		event.Skip()


	def sas_proc( self, event ):
		event.Skip()


	def jp_proc( self, event ):
		event.Skip()


	def client_proc( self, event ):
		event.Skip()


	def keysystem_proc( self, event ):
		event.Skip()


	def bonus_proc( self, event ):
		event.Skip()






	def OnConfig( self, event ):
		event.Skip()






	def AutoplayEditable( self, event ):
		event.Skip()

	def TimeSleepEditable( self, event ):
		event.Skip()




	def OnRFIDScanTime( self, event ):
		event.Skip()



	def OnSendMailIfWon( self, event ):
		event.Skip()










	def OnRelayTest( self, event ):
		event.Skip()







	def OnLogGet( self, event ):
		event.Skip()


	def enable_denomination( self, event ):
		event.Skip()


	def OnReset( self, event ):
		event.Skip()


	def OnDisableJP( self, event ):
		event.Skip()


	def OnAutoUpdate( self, event ):
		event.Skip()


	def OnReboot( self, event ):
		event.Skip()


	def OnDisableDenom( self, event ):
		event.Skip()


	def jackpot_enable( self, event ):
		event.Skip()


	def SAS_Tester( self, event ):
		event.Skip()









	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class Sys
###########################################################################

class Sys ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer1 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()

		fgSizer1.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )

		self.m_notebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )

		fgSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool3.GetId() )
		self.m_notebook1.Bind( wx.aui.EVT_AUINOTEBOOK_BUTTON, self.OnPageClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnPageClose( self, event ):
		event.Skip()


###########################################################################
## Class ConfPanel
###########################################################################

class ConfPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer1 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool1 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Потребители", wx.Bitmap( u"img/64x64/kopete.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool2 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Машини", wx.Bitmap( u"img/64x64/network-server.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Лицензи", wx.Bitmap( u"img/64x64/Gnome-Application-Certificate-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool7 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Рестарт", wx.Bitmap( u"img/64x64/Gnome-Undelete-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool16 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Джакпот", wx.Bitmap( u"img/64x64/Gnome-Security-High-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool22 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Системни", wx.Bitmap( u"img/64x64/Gnome-Applications-Utilities-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool10 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Бонус Карти", wx.Bitmap( u"img/64x64/Gnome-Contact-New-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool5 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Помощ", wx.Bitmap( u"img/64x64/Gnome-Help-Browser-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool6 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Относно", wx.Bitmap( u"img/64x64/preferences-desktop-notification.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()

		fgSizer1.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnReboot, id = self.m_tool7.GetId() )
		self.Bind( wx.EVT_TOOL, self.JPConf, id = self.m_tool16.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnSystemConf, id = self.m_tool22.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnHelp, id = self.m_tool5.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnInfo, id = self.m_tool6.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnReboot( self, event ):
		event.Skip()

	def JPConf( self, event ):
		event.Skip()

	def OnSystemConf( self, event ):
		event.Skip()

	def OnHelp( self, event ):
		event.Skip()

	def OnInfo( self, event ):
		event.Skip()


###########################################################################
## Class BonusCart
###########################################################################

class BonusCart ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer14 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar3 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_tool12 = self.m_toolBar3.AddTool( wx.ID_ANY, u"Нова карта", wx.Bitmap( u"img/64x64/Gnome-Emblem-Documents-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool13 = self.m_toolBar3.AddTool( wx.ID_ANY, u"Запиши в машини", wx.Bitmap( u"img/64x64/Gnome-Software-Update-Available-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool1 = self.m_toolBar3.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar3.Realize()

		fgSizer14.Add( self.m_toolBar3, 0, wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 490,180 ), wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_listCtrl1.SetForegroundColour( wx.Colour( 0, 166, 6 ) )

		gSizer6.Add( self.m_listCtrl1, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer14.Add( gSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer14 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnAdd, id = self.m_tool12.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnSaveInSMIB, id = self.m_tool13.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool1.GetId() )
		self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnEdit )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnAdd( self, event ):
		event.Skip()

	def OnSaveInSMIB( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnEdit( self, event ):
		event.Skip()


###########################################################################
## Class ReadBonusCart
###########################################################################

class ReadBonusCart ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добавяне на карта", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 540,112 ), wx.DefaultSize )

		gSizer14 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Моля поставете карта в четеца!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 197, 33, 33 ) )

		gSizer14.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer14.Add( gSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer14 )
		self.Layout()
		gSizer14.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class AddBonusCart
###########################################################################

class AddBonusCart ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добавяне на карта", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Имре за разпознаване", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		self.m_staticText38.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )
		self.m_staticText38.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer3.Add( self.m_staticText38, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl14, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Стойност", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		self.m_staticText39.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_LIGHT, False, wx.EmptyString ) )
		self.m_staticText39.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer3.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_spinCtrl12 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 2000, 0 )
		bSizer3.Add( self.m_spinCtrl12, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, u"Превърти", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		self.m_staticText69.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText69.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		bSizer3.Add( self.m_staticText69, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_spinCtrl26 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1000, 1 )
		bSizer3.Add( self.m_spinCtrl26, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox1Choices = [ u"Статична стойност", u"Статична с удържане", u"1 към 1", u"1 към 1 с удържане", u"Умножена по 2", u"Умножена по 2 с удържане", u"Не усвояем вход" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 4, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer3.Add( self.m_radioBox1, 0, wx.ALL, 5 )

		self.m_checkBox52 = wx.CheckBox( self, wx.ID_ANY, u"Задължителен клиент", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_checkBox52, 0, wx.ALL, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_radioBtn7 = wx.RadioButton( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Активна", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer18.Add( self.m_radioBtn7, 0, wx.ALL, 5 )

		self.m_radioBtn8 = wx.RadioButton( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Не активна", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer18.Add( self.m_radioBtn8, 0, wx.ALL, 5 )


		gSizer9.Add( sbSizer18, 1, wx.EXPAND, 5 )

		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText46 = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Номер на карта:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		sbSizer17.Add( self.m_staticText46, 0, wx.ALL, 5 )

		self.m_staticText47 = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Съществува", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		self.m_staticText47.SetForegroundColour( wx.Colour( 28, 89, 0 ) )

		sbSizer17.Add( self.m_staticText47, 0, wx.ALL, 5 )


		gSizer9.Add( sbSizer17, 1, wx.EXPAND, 5 )


		bSizer3.Add( gSizer9, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button28 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button28, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button29, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		bSizer3.Add( gSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()
		bSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.OnRestricted )
		self.m_button28.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button29.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnRestricted( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class BonusCartSave
###########################################################################

class BonusCartSave ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Запис на бонус карти", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer21 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		fgSizer21.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.m_button23, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( fgSizer21 )
		self.Layout()
		fgSizer21.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button23.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


###########################################################################
## Class ShowLog
###########################################################################

class ShowLog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ЛогФайл", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer41 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,400 ), 0|wx.VSCROLL|wx.HSCROLL|wx.WANTS_CHARS|wx.BORDER_NONE )
		fgSizer41.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button42 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer41.Add( self.m_button42, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( fgSizer41 )
		self.Layout()
		fgSizer41.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button42.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


###########################################################################
## Class Abaut
###########################################################################

class Abaut ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Относно", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer42 = wx.FlexGridSizer( 8, 0, 0, 0 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"Версия:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		fgSizer42.Add( self.m_staticText54, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"1.4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		fgSizer42.Add( self.m_staticText55, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText73 = wx.StaticText( self, wx.ID_ANY, u"Ревизия", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )

		fgSizer42.Add( self.m_staticText73, 0, wx.ALL, 5 )

		self.m_staticText74 = wx.StaticText( self, wx.ID_ANY, u"62", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		fgSizer42.Add( self.m_staticText74, 0, wx.ALL, 5 )

		self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"BD ревизия:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		fgSizer42.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"df85689568", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		fgSizer42.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Редирект сървър:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		fgSizer42.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"1.2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		fgSizer42.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText60 = wx.StaticText( self, wx.ID_ANY, u"Производител:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )

		fgSizer42.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Merilin 1 ltd.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		fgSizer42.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"E-mail:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		fgSizer42.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"grigor.kolev@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		fgSizer42.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button52 = wx.Button( self, wx.ID_ANY, u"Промени", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.m_button52, 0, wx.ALL, 5 )

		self.m_button38 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.m_button38, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( fgSizer42 )
		self.Layout()
		fgSizer42.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button52.Bind( wx.EVT_BUTTON, self.ChangeLog )
		self.m_button38.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def ChangeLog( self, event ):
		event.Skip()



###########################################################################
## Class UpdateRev
###########################################################################

class UpdateRev ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ревизия", pos = wx.DefaultPosition, size = wx.Size( 262,162 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer17 = wx.GridSizer( 3, 0, 0, 0 )

		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, u"Ревизия", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		gSizer17.Add( self.m_staticText68, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer17.Add( self.m_textCtrl16, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer18 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button41 = wx.Button( self, wx.ID_ANY, u"Отказ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer18.Add( self.m_button41, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button42 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer18.Add( self.m_button42, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer17.Add( gSizer18, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl16.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button41.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button42.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnGo( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()



###########################################################################
## Class SudoPasswd
###########################################################################

class SudoPasswd ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SudoPassud", pos = wx.DefaultPosition, size = wx.Size( 382,120 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, u"sudo passwd", wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		bSizer12.Add( self.m_textCtrl25, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer23 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button52 = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_button52, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button53 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer23.Add( self.m_button53, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		bSizer12.Add( gSizer23, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl25.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button52.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button53.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()




###########################################################################
## Class SaveSection
###########################################################################

class SaveSection ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Запиши конфигурация", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer46 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer46.SetFlexibleDirection( wx.BOTH )
		fgSizer46.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox66 = wx.CheckBox( self, wx.ID_ANY, u"SAS", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_checkBox66, 0, wx.ALL, 5 )

		self.m_checkBox68 = wx.CheckBox( self, wx.ID_ANY, u"Client", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_checkBox68, 0, wx.ALL, 5 )

		self.m_checkBox70 = wx.CheckBox( self, wx.ID_ANY, u"Mail Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_checkBox70, 0, wx.ALL, 5 )

		self.m_checkBox75 = wx.CheckBox( self, wx.ID_ANY, u"PROC", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_checkBox75, 0, wx.ALL, 5 )


		fgSizer46.Add( bSizer19, 1, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox67 = wx.CheckBox( self, wx.ID_ANY, u"Jackpot", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_checkBox67, 0, wx.ALL, 5 )

		self.m_checkBox69 = wx.CheckBox( self, wx.ID_ANY, u"Bonus", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_checkBox69, 0, wx.ALL, 5 )

		self.m_checkBox71 = wx.CheckBox( self, wx.ID_ANY, u"Log Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_checkBox71, 0, wx.ALL, 5 )

		self.m_checkBox76 = wx.CheckBox( self, wx.ID_ANY, u"RFID", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_checkBox76, 0, wx.ALL, 5 )


		fgSizer46.Add( bSizer20, 1, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox72 = wx.CheckBox( self, wx.ID_ANY, u"Keysystem", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_checkBox72, 0, wx.ALL, 5 )

		self.m_checkBox73 = wx.CheckBox( self, wx.ID_ANY, u"System", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_checkBox73, 0, wx.ALL, 5 )

		self.m_checkBox74 = wx.CheckBox( self, wx.ID_ANY, u"Log Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_checkBox74, 0, wx.ALL, 5 )


		bSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer46.Add( bSizer21, 1, wx.EXPAND, 5 )

		self.m_button58 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.m_button58, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer46.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button59 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.m_button59, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( fgSizer46 )
		self.Layout()
		fgSizer46.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button58.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button59.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class NRA
###########################################################################

class NRA ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"NRA Token", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer47 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer47.SetFlexibleDirection( wx.BOTH )
		fgSizer47.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"Клиент ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		fgSizer47.Add( self.m_staticText82, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl27 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.m_textCtrl27, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText83 = wx.StaticText( self, wx.ID_ANY, u"Токен PROD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer47.Add( self.m_staticText83, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl28 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,100 ), wx.TE_MULTILINE )
		fgSizer47.Add( self.m_textCtrl28, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText84 = wx.StaticText( self, wx.ID_ANY, u"Валиден до", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer47.Add( self.m_staticText84, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_calendar3 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		fgSizer47.Add( self.m_calendar3, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer25 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button59 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button59, 0, wx.ALL, 5 )

		self.m_button60 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button60, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		fgSizer47.Add( gSizer25, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer47 )
		self.Layout()
		fgSizer47.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button59.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button60.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class Sas_Tester
###########################################################################

class Sas_Tester ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"SAS Tester", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer26 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_scrolledWindow5 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1024,650 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		fgSizer48 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer48.SetFlexibleDirection( wx.BOTH )
		fgSizer48.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl30 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 700,600 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		fgSizer48.Add( self.m_textCtrl30, 0, wx.ALL, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_button64 = wx.Button( self.m_scrolledWindow5, wx.ID_ANY, u"Connect to EMG", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button64, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText87 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Gpoll Get", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )

		bSizer20.Add( self.m_staticText87, 0, wx.ALL, 5 )

		self.m_textCtrl31 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, u"0.4", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_textCtrl31, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button66 = wx.Button( self.m_scrolledWindow5, wx.ID_ANY, u"Gpoll Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button66, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button68 = wx.Button( self.m_scrolledWindow5, wx.ID_ANY, u"Gpoll Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button68, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText86 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Lpoll Func", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )

		bSizer20.Add( self.m_staticText86, 0, wx.ALL, 5 )

		m_choice20Choices = []
		self.m_choice20 = wx.Choice( self.m_scrolledWindow5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice20Choices, 0 )
		self.m_choice20.SetSelection( 0 )
		bSizer20.Add( self.m_choice20, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText88 = wx.StaticText( self.m_scrolledWindow5, wx.ID_ANY, u"Var", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )

		bSizer20.Add( self.m_staticText88, 0, wx.ALL, 5 )

		self.m_textCtrl32 = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,150 ), wx.TE_MULTILINE )
		bSizer20.Add( self.m_textCtrl32, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button65 = wx.Button( self.m_scrolledWindow5, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button65, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button67 = wx.Button( self.m_scrolledWindow5, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button67, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer48.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow5.SetSizer( fgSizer48 )
		self.m_scrolledWindow5.Layout()
		gSizer26.Add( self.m_scrolledWindow5, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( gSizer26 )
		self.Layout()
		gSizer26.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button64.Bind( wx.EVT_BUTTON, self.OnConnect )
		self.m_button66.Bind( wx.EVT_BUTTON, self.Gpoll_Start )
		self.m_button68.Bind( wx.EVT_BUTTON, self.Gpoll_Stop )
		self.m_choice20.Bind( wx.EVT_CHOICE, self.OnChoise )
		self.m_button65.Bind( wx.EVT_BUTTON, self.Run )
		self.m_button67.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnConnect( self, event ):
		event.Skip()

	def Gpoll_Start( self, event ):
		event.Skip()

	def Gpoll_Stop( self, event ):
		event.Skip()

	def OnChoise( self, event ):
		event.Skip()

	def Run( self, event ):
		event.Skip()



