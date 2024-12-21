# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FlorSelect
###########################################################################

class FlorSelect ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Етаж", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,200 ), wx.LC_REPORT )
		self.m_listCtrl1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer1.Add( self.m_listCtrl1, 0, wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		gSizer1.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		fgSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnGo )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.OnAdd )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


	def OnAdd( self, event ):
		event.Skip()


###########################################################################
## Class FlorAdd
###########################################################################

class FlorAdd ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави етаж", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer2 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer2.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()
		gSizer2.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class AddMashin
###########################################################################

class AddMashin ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		fgSizer8 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.FULL_REPAINT_ON_RESIZE|wx.HSCROLL|wx.TAB_TRAVERSAL|wx.VSCROLL|wx.WANTS_CHARS|wx.BORDER_RAISED )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		gSizer24 = wx.GridSizer( 0, 3, 0, 0 )

		fgSizer17 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer18 = wx.GridSizer( 2, 2, 0, 0 )

		self.m_staticText18 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Сериен номер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer18.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer18.Add( self.m_textCtrl12, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText49 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"SMIB IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		self.m_staticText49.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText49.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer18.Add( self.m_staticText49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl37 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"192.168.1.9", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer18.Add( self.m_textCtrl37, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		fgSizer17.Add( gSizer18, 0, wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 3, 3, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText30 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Етаж", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer9.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		fgSizer9.Add( self.m_choice3, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton4 = wx.BitmapButton( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton4.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer9.Add( self.m_bpButton4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText29 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Модел", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer9.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		fgSizer9.Add( self.m_choice2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton3 = wx.BitmapButton( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton3.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer9.Add( self.m_bpButton3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText28 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Производител", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer9.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		fgSizer9.Add( self.m_choice1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton2 = wx.BitmapButton( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton2.SetBitmap( wx.Bitmap( u"img/22x22/list-add.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer9.Add( self.m_bpButton2, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer17.Add( fgSizer9, 0, wx.EXPAND, 5 )


		gSizer24.Add( fgSizer17, 0, wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"SAS " ), wx.VERTICAL )

		self.m_radioBtn1 = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"SAS наличен", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_radioBtn1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_radioBtn2 = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"SAS липсва", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_radioBtn2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox1 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Работеща", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True)
		sbSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Превъртане в дясно", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox31 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Използвай AFT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox31.Hide()

		sbSizer1.Add( self.m_checkBox31, 0, wx.ALL, 5 )

		self.m_button20 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Вземи информация", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_staticText19 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Номер в лиценз", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText19.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		sbSizer1.Add( self.m_staticText19, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl13 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_textCtrl13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"SMIB Device" ), wx.VERTICAL )

		self.m_staticText50 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"SMIB IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		sbSizer2.Add( self.m_staticText50, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Няма", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText51.SetForegroundColour( wx.Colour( 154, 0, 0 ) )

		sbSizer2.Add( self.m_staticText51, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button13 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Ново IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button13, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText25 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"UUID: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		sbSizer2.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_staticText44 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Няма", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		self.m_staticText44.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText44.SetForegroundColour( wx.Colour( 154, 0, 0 ) )

		sbSizer2.Add( self.m_staticText44, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button11 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Ново UUID", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button11, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText26 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Версия: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		sbSizer2.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Няма", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		self.m_staticText45.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText45.SetForegroundColour( wx.Colour( 154, 0, 0 ) )

		sbSizer2.Add( self.m_staticText45, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText221 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		sbSizer2.Add( self.m_staticText221, 0, wx.ALL, 5 )


		sbSizer1.Add( sbSizer2, 0, wx.EXPAND, 5 )


		gSizer24.Add( sbSizer1, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		fgSizer91 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer91.SetFlexibleDirection( wx.BOTH )
		fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer45 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText91 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Вход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		self.m_staticText91.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText91.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer45.Add( self.m_staticText91, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText101 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Изход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText101.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer45.Add( self.m_staticText101, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl211 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer45.Add( self.m_textCtrl211, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl221 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer45.Add( self.m_textCtrl221, 1, wx.ALL|wx.EXPAND, 5 )


		fgSizer91.Add( gSizer45, 1, wx.EXPAND, 5 )

		gSizer47 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText9 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"М.Вход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer47.Add( self.m_staticText9, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"М.Изход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer47.Add( self.m_staticText10, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer47.Add( self.m_textCtrl21, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer47.Add( self.m_textCtrl22, 1, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		fgSizer91.Add( gSizer47, 1, wx.EXPAND, 5 )

		gSizer20 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText22 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"BET", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText22.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer20.Add( self.m_staticText22, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText23 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WON", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		self.m_staticText23.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText23.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer20.Add( self.m_staticText23, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer20.Add( self.m_textCtrl16, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer20.Add( self.m_textCtrl17, 1, wx.ALL|wx.EXPAND, 5 )


		fgSizer91.Add( gSizer20, 1, wx.EXPAND, 5 )

		gSizer49 = wx.GridSizer( 2, 3, 0, 0 )

		self.m_staticText47 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Бил", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		self.m_staticText47.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText47.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer49.Add( self.m_staticText47, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText55 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Коеф", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		self.m_staticText55.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText55.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer49.Add( self.m_staticText55, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText57 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"М.Коеф", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		self.m_staticText57.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText57.SetForegroundColour( wx.Colour( 73, 120, 179 ) )

		gSizer49.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl35 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer49.Add( self.m_textCtrl35, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl39 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer49.Add( self.m_textCtrl39, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl40 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer49.Add( self.m_textCtrl40, 1, wx.ALL|wx.EXPAND, 5 )


		fgSizer91.Add( gSizer49, 1, wx.EXPAND, 5 )


		gSizer24.Add( fgSizer91, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( gSizer24 )
		self.m_scrolledWindow1.Layout()
		gSizer24.Fit( self.m_scrolledWindow1 )
		fgSizer8.Add( self.m_scrolledWindow1, 0, wx.ALL, 5 )

		gSizer25 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button18, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer25.Add( self.m_button19, 1, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer8.Add( gSizer25, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer8 )
		self.Layout()
		fgSizer8.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.OnSize )
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.OnSetShow )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.OnSetShow )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnGetInfo )
		self.m_button13.Bind( wx.EVT_BUTTON, self.OnFind )
		self.m_button11.Bind( wx.EVT_BUTTON, self.OnGetNewUUID )
		self.m_button18.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button19.Bind( wx.EVT_BUTTON, self.OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnSize( self, event ):
		event.Skip()

	def OnSetShow( self, event ):
		event.Skip()


	def OnGetInfo( self, event ):
		event.Skip()

	def OnFind( self, event ):
		event.Skip()

	def OnGetNewUUID( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnSave( self, event ):
		event.Skip()


###########################################################################
## Class AddMaker
###########################################################################

class AddMaker ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави Производител", pos = wx.DefaultPosition, size = wx.Size( 340,110 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer2 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		gSizer2.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class AddModel
###########################################################################

class AddModel ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добави Модел", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl14, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,200 ), wx.LC_REPORT )
		self.m_listCtrl1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer1.Add( self.m_listCtrl1, 0, wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()
		fgSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class MashinPanel
###########################################################################

class MashinPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer3 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool2 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Добави машина", wx.Bitmap( u"img/64x64/network-server.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Добави етаж", wx.Bitmap( u"img/64x64/network-server-database.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool5 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Добави модел", wx.Bitmap( u"img/64x64/cpu.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Добави производител", wx.Bitmap( u"img/64x64/xarchiver-add.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool6 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Зпис в джакпот", wx.Bitmap( u"img/64x64/Add-Files-To-Archive-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool1 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()

		fgSizer3.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer4 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_listCtrl5 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl5.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_listCtrl5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_listCtrl6 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl6.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_listCtrl6, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer4.Add( gSizer4, 1, wx.EXPAND, 5 )

		self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl2.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer4.Add( self.m_listCtrl2, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()
		fgSizer3.Fit( self )

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnAddMashin, id = self.m_tool2.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnAddFlor, id = self.m_tool3.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnAddModel, id = self.m_tool5.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnAddMaker, id = self.m_tool4.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnSendToJP, id = self.m_tool6.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool1.GetId() )
		self.m_listCtrl5.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnShowMaker )
		self.m_listCtrl6.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnShowEnableDisable )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnAddMashin( self, event ):
		event.Skip()

	def OnAddFlor( self, event ):
		event.Skip()

	def OnAddModel( self, event ):
		event.Skip()

	def OnAddMaker( self, event ):
		event.Skip()

	def OnSendToJP( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnShowMaker( self, event ):
		event.Skip()

	def OnShowEnableDisable( self, event ):
		event.Skip()


###########################################################################
## Class DevType
###########################################################################

class DevType ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Тип на машина", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		gSizer15 = wx.GridSizer( 2, 1, 0, 0 )

		m_choice4Choices = []
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		self.m_choice4.SetMinSize( wx.Size( 250,-1 ) )

		gSizer15.Add( self.m_choice4, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer16 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_button13, 0, wx.ALL, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer16.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer15.Add( gSizer16, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer15 )
		self.Layout()
		gSizer15.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button13.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


