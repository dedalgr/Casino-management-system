# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.adv

###########################################################################
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer7 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL|wx.TB_TEXT )
		self.m_toolBar1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_tool2 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Клиенти", wx.Bitmap( u"img/64x64/system-users.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Машини", wx.Bitmap( u"img/64x64/network-server.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Крупиета", wx.Bitmap( u"img/64x64/kopete.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool6 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Джакпот", wx.Bitmap( u"img/64x64/Emblem-Money-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool9 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Печат", wx.Bitmap( u"img/64x64/Gnome-Printer-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool7 = self.m_toolBar1.AddTool( wx.ID_ANY, u"E-mail", wx.Bitmap( u"img/64x64/Gnome-Mail-Forward-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool8 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Експорт", wx.Bitmap( u"img/64x64/Gnome-X-Office-Spreadsheet-64.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool1 = self.m_toolBar1.AddTool( wx.ID_ANY, u"Затвори", wx.Bitmap( u"img/64x64/dialog-error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()

		fgSizer7.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )

		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE|wx.aui.AUI_NB_SCROLL_BUTTONS )

		fgSizer7.Add( self.m_auinotebook1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( fgSizer7 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnCustReport, id = self.m_tool2.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnMashinReport, id = self.m_tool3.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnUserReport, id = self.m_tool4.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnJackpotReport, id = self.m_tool6.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnPrint, id = self.m_tool9.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnSendMail, id = self.m_tool7.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnExport, id = self.m_tool8.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnClose, id = self.m_tool1.GetId() )
		self.m_auinotebook1.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnTabClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnCustReport( self, event ):
		event.Skip()

	def OnMashinReport( self, event ):
		event.Skip()

	def OnUserReport( self, event ):
		event.Skip()

	def OnJackpotReport( self, event ):
		event.Skip()

	def OnPrint( self, event ):
		event.Skip()

	def OnSendMail( self, event ):
		event.Skip()

	def OnExport( self, event ):
		event.Skip()

	def OnClose( self, event ):
		event.Skip()

	def OnTabClose( self, event ):
		event.Skip()


###########################################################################
## Class ListPanel
###########################################################################

class ListPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer2 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
		fgSizer2.Add( self.m_listCtrl1, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()
		fgSizer2.Fit( self )

		# Connect Events
		self.m_listCtrl1.Bind( wx.EVT_LIST_COL_CLICK, self.OnSort )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnSort( self, event ):
		event.Skip()


###########################################################################
## Class PicPanel
###########################################################################

class PicPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer3 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../../../../pic/Best-Of-Win/256x256/apps/xclock.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_bitmap1, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()
		fgSizer3.Fit( self )

	def __del__( self ):
		pass


###########################################################################
## Class ReportSelect
###########################################################################

class ReportSelect ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer8 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listbook2 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )

		fgSizer8.Add( self.m_listbook2, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer8 )
		self.Layout()
		fgSizer8.Fit( self )

	def __del__( self ):
		pass


###########################################################################
## Class UserReport
###########################################################################

class UserReport ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer6 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		sbSizer11.Add( fgSizer6, 1, wx.EXPAND, 5 )

		self.m_calendar1 = wx.adv.CalendarCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_MONDAY_FIRST|wx.adv.CAL_SHOW_HOLIDAYS )
		sbSizer11.Add( self.m_calendar1, 0, wx.ALL, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		sbSizer11.Add( fgSizer7, 1, wx.EXPAND, 5 )

		self.m_calendar2 = wx.adv.CalendarCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_MONDAY_FIRST|wx.adv.CAL_SEQUENTIAL_MONTH_SELECTION|wx.adv.CAL_SHOW_HOLIDAYS )
		sbSizer11.Add( self.m_calendar2, 0, wx.ALL, 5 )


		fgSizer9.Add( sbSizer11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.m_radioBtn9 = wx.RadioButton( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Активни потребители", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn9.SetValue( True )
		sbSizer8.Add( self.m_radioBtn9, 0, wx.ALL, 5 )

		self.m_radioBtn8 = wx.RadioButton( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Не активни потребители", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_radioBtn8, 0, wx.ALL, 5 )


		bSizer4.Add( sbSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer12 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn10 = wx.RadioButton( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Не обобщавай", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn10.SetValue( True )
		fgSizer12.Add( self.m_radioBtn10, 0, wx.ALL, 5 )

		self.m_radioBtn7 = wx.RadioButton( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Обобщена по ден", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.m_radioBtn7, 0, wx.ALL, 5 )

		self.m_radioBtn14 = wx.RadioButton( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Обобщена по потребител", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.m_radioBtn14, 0, wx.ALL, 5 )

		self.m_radioBtn15 = wx.RadioButton( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Обобщена по машини", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.m_radioBtn15, 0, wx.ALL, 5 )


		sbSizer13.Add( fgSizer12, 1, wx.EXPAND, 5 )


		bSizer4.Add( sbSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Потребител", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer4.Add( self.m_choice3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, u"Сортирай в обратен ред", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_checkBox6, 0, wx.ALL, 5 )

		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_radioBtn16 = wx.RadioButton( sbSizer15.GetStaticBox(), wx.ID_ANY, u"Генерирай таблица", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn16.SetValue( True )
		sbSizer15.Add( self.m_radioBtn16, 0, wx.ALL, 5 )

		self.m_radioBtn17 = wx.RadioButton( sbSizer15.GetStaticBox(), wx.ID_ANY, u"Генерирай графика", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.m_radioBtn17, 0, wx.ALL, 5 )


		bSizer4.Add( sbSizer15, 1, wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Генерирай", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		fgSizer9.Add( bSizer4, 0, 0, 5 )


		self.SetSizer( fgSizer9 )
		self.Layout()
		fgSizer9.Fit( self )

		# Connect Events
		self.m_radioBtn9.Bind( wx.EVT_RADIOBUTTON, self.OnRadioButtonUser )
		self.m_radioBtn8.Bind( wx.EVT_RADIOBUTTON, self.OnRadioButtonUser )
		self.m_radioBtn14.Bind( wx.EVT_RADIOBUTTON, self.OnTableSelect )
		self.m_radioBtn15.Bind( wx.EVT_RADIOBUTTON, self.OnTableSelect )
		self.m_checkBox6.Bind( wx.EVT_CHECKBOX, self.OnOrderBy )
		self.m_radioBtn16.Bind( wx.EVT_RADIOBUTTON, self.OnTableMaket )
		self.m_radioBtn17.Bind( wx.EVT_RADIOBUTTON, self.OnTableMaket )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnRadioButtonUser( self, event ):
		event.Skip()


	def OnTableSelect( self, event ):
		event.Skip()


	def OnOrderBy( self, event ):
		event.Skip()

	def OnTableMaket( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class MCurenState
###########################################################################

class MCurenState ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_checkBox9 = wx.CheckBox( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Текущ кредит", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox9.SetValue(True)
		sbSizer18.Add( self.m_checkBox9, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Вход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetValue(True)
		sbSizer18.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Изход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.SetValue(True)
		sbSizer18.Add( self.m_checkBox4, 0, wx.ALL, 5 )

		self.m_checkBox81 = wx.CheckBox( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Бил", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox81.SetValue(True)
		sbSizer18.Add( self.m_checkBox81, 0, wx.ALL, 5 )

		self.m_checkBox5 = wx.CheckBox( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Тотал", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox5.SetValue(True)
		sbSizer18.Add( self.m_checkBox5, 0, wx.ALL, 5 )

		self.m_checkBox7 = wx.CheckBox( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Печалба в игра ( won )", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox7.SetValue(True)
		sbSizer18.Add( self.m_checkBox7, 0, wx.ALL, 5 )

		self.m_checkBox6 = wx.CheckBox( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Залог ( bet )", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox6.SetValue(True)
		sbSizer18.Add( self.m_checkBox6, 0, wx.ALL, 5 )

		self.m_checkBox8 = wx.CheckBox( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Процент на възвръщаемост", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer18.Add( self.m_checkBox8, 0, wx.ALL, 5 )


		fgSizer9.Add( sbSizer18, 1, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 2, 0, 0, 0 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Време за опресняване", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"0 = Зависи от машината", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 135, 0, 0 ) )

		bSizer4.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Секунди на машина", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText4.SetForegroundColour( wx.Colour( 135, 0, 0 ) )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer4.Add( self.m_choice3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		gSizer2.Add( bSizer4, 0, 0, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Напред", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		gSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )


		fgSizer9.Add( gSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer9 )
		self.Layout()
		fgSizer9.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class RealTimeLock
###########################################################################

class RealTimeLock ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer11 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl3 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		fgSizer11.Add( self.m_listCtrl3, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer12 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.m_button20, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		fgSizer11.Add( fgSizer12, 0, wx.EXPAND, 5 )


		self.SetSizer( fgSizer11 )
		self.Layout()

		# Connect Events
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


###########################################################################
## Class RowSelect
###########################################################################

class RowSelect ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,404 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer29 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		fgSizer9 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		m_radioBox1Choices = [ u"Дневен", u"Месечен", u"Ордер" ]
		self.m_radioBox1 = wx.RadioBox( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox1.SetSelection( 0 )
		sbSizer11.Add( self.m_radioBox1, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer9.Add( sbSizer11, 0, 0, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_calendar1 = wx.adv.CalendarCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		gSizer6.Add( self.m_calendar1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_calendar2 = wx.adv.CalendarCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		gSizer6.Add( self.m_calendar2, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer9.Add( gSizer6, 1, wx.EXPAND, 5 )

		self.m_listCtrl2 = wx.ListCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		fgSizer9.Add( self.m_listCtrl2, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( fgSizer9 )
		self.m_scrolledWindow1.Layout()
		fgSizer9.Fit( self.m_scrolledWindow1 )
		fgSizer29.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer7 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Покажи", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		fgSizer29.Add( gSizer7, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer29 )
		self.Layout()

		# Connect Events
		self.m_listCtrl2.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnEdit )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnEdit( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class EditOrder
###########################################################################

class EditOrder ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Редакция на отчет", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_listCtrl4 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		fgSizer21.Add( self.m_listCtrl4, 0, wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button7.Hide()

		bSizer5.Add( self.m_button7, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Печат", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"E-MAIL", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button12, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Номер", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button17.Hide()

		bSizer5.Add( self.m_button17, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Дата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button18.Hide()

		bSizer5.Add( self.m_button18, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Ред ремонт", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button19.Hide()

		bSizer5.Add( self.m_button19, 0, wx.ALL, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Изтрий", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button20.Hide()

		bSizer5.Add( self.m_button20, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button9, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer21.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer21 )
		self.Layout()
		fgSizer21.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_SIZE, self._resize )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnSave )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnPrint )
		self.m_button12.Bind( wx.EVT_BUTTON, self.OnSendMail )
		self.m_button17.Bind( wx.EVT_BUTTON, self.OnN )
		self.m_button18.Bind( wx.EVT_BUTTON, self.OnDate )
		self.m_button19.Bind( wx.EVT_BUTTON, self.OnFixRow )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnDell )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def _resize( self, event ):
		event.Skip()

	def OnSave( self, event ):
		event.Skip()

	def OnPrint( self, event ):
		event.Skip()

	def OnSendMail( self, event ):
		event.Skip()

	def OnN( self, event ):
		event.Skip()

	def OnDate( self, event ):
		event.Skip()

	def OnFixRow( self, event ):
		event.Skip()

	def OnDell( self, event ):
		event.Skip()



###########################################################################
## Class JPDateSelect
###########################################################################

class JPDateSelect ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer22 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer24 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"От Дата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer24.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_calendar7 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		fgSizer24.Add( self.m_calendar7, 0, wx.ALL, 5 )


		fgSizer22.Add( fgSizer24, 1, wx.EXPAND, 5 )

		fgSizer23 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"До Дата", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer23.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_calendar8 = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		fgSizer23.Add( self.m_calendar8, 0, wx.ALL, 5 )


		fgSizer22.Add( fgSizer23, 1, wx.EXPAND, 5 )


		fgSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Покажи", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer22.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		self.SetSizer( fgSizer22 )
		self.Layout()
		fgSizer22.Fit( self )

		# Connect Events
		self.Bind( wx.aui.EVT_AUI_PANE_CLOSE, self.OnClose )
		self.m_button11.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class EditDayReportMashin
###########################################################################

class EditDayReportMashin ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Дедактиране на отчет", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.CAPTION|wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer4 = wx.FlexGridSizer( 4, 0, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Машина", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer10.Add( self.m_staticText15, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_staticText161 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		gSizer10.Add( self.m_staticText161, 1, wx.ALL|wx.EXPAND, 5 )


		fgSizer4.Add( gSizer10, 1, wx.EXPAND, 5 )

		fgSizer5 = wx.FlexGridSizer( 5, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Вход:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer5.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl8.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer5.Add( self.m_textCtrl8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl61 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl61, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Изход:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer5.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl9.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer5.Add( self.m_textCtrl9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"М.Вход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer5.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.m_textCtrl10.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer5.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText21.SetForegroundColour( wx.Colour( 175, 0, 0 ) )

		fgSizer5.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText181 = wx.StaticText( self, wx.ID_ANY, u"М.Изход", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		fgSizer5.Add( self.m_staticText181, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer4.Add( fgSizer5, 1, wx.EXPAND, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Тотал:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText22.SetForegroundColour( wx.Colour( 19, 145, 62 ) )

		fgSizer4.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Запис", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		fgSizer4.Add( gSizer9, 1, wx.EXPAND|wx.ALIGN_BOTTOM, 5 )


		self.SetSizer( fgSizer4 )
		self.Layout()
		fgSizer4.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_textCtrl8.Bind( wx.EVT_TEXT, self.OnMathIn )
		self.m_textCtrl61.Bind( wx.EVT_TEXT, self.TotalCalc )
		self.m_textCtrl9.Bind( wx.EVT_TEXT, self.OnMathOut )
		self.m_textCtrl7.Bind( wx.EVT_TEXT, self.TotalCalc )
		self.m_textCtrl6.Bind( wx.EVT_TEXT_ENTER, self.OnGo )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnMathIn( self, event ):
		event.Skip()

	def TotalCalc( self, event ):
		event.Skip()

	def OnMathOut( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()




###########################################################################
## Class H24
###########################################################################

class H24 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer6 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		sbSizer11.Add( fgSizer6, 1, wx.EXPAND, 5 )

		self.m_calendar1 = wx.adv.CalendarCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_MONDAY_FIRST|wx.adv.CAL_SHOW_HOLIDAYS )
		sbSizer11.Add( self.m_calendar1, 0, wx.ALL, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		sbSizer11.Add( fgSizer7, 1, wx.EXPAND, 5 )

		self.m_calendar2 = wx.adv.CalendarCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_MONDAY_FIRST|wx.adv.CAL_SEQUENTIAL_MONTH_SELECTION|wx.adv.CAL_SHOW_HOLIDAYS )
		sbSizer11.Add( self.m_calendar2, 0, wx.ALL, 5 )


		fgSizer9.Add( sbSizer11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		fgSizer36 = wx.FlexGridSizer( 5, 2, 0, 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox141 = wx.CheckBox( self, wx.ID_ANY, u"Машини IN/OUT", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.m_checkBox141, 0, wx.ALL, 5 )

		self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, u"Приходи / Разходи", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.m_checkBox6, 0, wx.ALL, 5 )

		self.m_checkBox14 = wx.CheckBox( self, wx.ID_ANY, u"Джакпоти / Бонус карти", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.m_checkBox14, 0, wx.ALL, 5 )

		self.m_checkBox17 = wx.CheckBox( self, wx.ID_ANY, u"Клиентски бонус", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.m_checkBox17, 0, wx.ALL, 5 )

		self.m_checkBox181 = wx.CheckBox( self, wx.ID_ANY, u"Обощена таблица", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox181.SetValue(True)
		fgSizer36.Add( self.m_checkBox181, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer36, 1, wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Генерирай", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		fgSizer9.Add( bSizer4, 0, 0, 5 )


		self.SetSizer( fgSizer9 )
		self.Layout()
		fgSizer9.Fit( self )

		# Connect Events
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class MashinReport
###########################################################################

class MashinReport ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer6 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		sbSizer11.Add( fgSizer6, 1, wx.EXPAND, 5 )

		self.m_calendar1 = wx.adv.CalendarCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_MONDAY_FIRST|wx.adv.CAL_SHOW_HOLIDAYS )
		sbSizer11.Add( self.m_calendar1, 0, wx.ALL, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		sbSizer11.Add( fgSizer7, 1, wx.EXPAND, 5 )

		self.m_calendar2 = wx.adv.CalendarCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_MONDAY_FIRST|wx.adv.CAL_SHOW_HOLIDAYS )
		sbSizer11.Add( self.m_calendar2, 0, wx.ALL, 5 )


		fgSizer9.Add( sbSizer11, 0, 0, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer20 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn9 = wx.RadioButton( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Производител", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn9.SetValue( True )
		fgSizer20.Add( self.m_radioBtn9, 0, wx.ALL, 5 )

		self.m_radioBtn41 = wx.RadioButton( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Регион", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_radioBtn41, 0, wx.ALL, 5 )

		self.m_radioBtn8 = wx.RadioButton( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Модел", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_radioBtn8, 0, wx.ALL, 5 )

		self.m_radioBtn21 = wx.RadioButton( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Потребител", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_radioBtn21, 0, wx.ALL, 5 )


		sbSizer8.Add( fgSizer20, 1, wx.EXPAND, 5 )


		bSizer4.Add( sbSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Производител", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer4.Add( self.m_choice3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		fgSizer16 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn28 = wx.RadioButton( self, wx.ID_ANY, u"По Bet и Won", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn28.SetValue( True )
		fgSizer16.Add( self.m_radioBtn28, 0, wx.ALL, 5 )

		self.m_radioBtn29 = wx.RadioButton( self, wx.ID_ANY, u"По IN и OUT", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_radioBtn29, 0, wx.ALL, 5 )


		bSizer4.Add( fgSizer16, 0, wx.EXPAND, 5 )

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer13 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn10 = wx.RadioButton( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Не обобщавай", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_radioBtn10, 0, wx.ALL, 5 )

		self.m_radioBtn42 = wx.RadioButton( sbSizer13.GetStaticBox(), wx.ID_ANY, u"По регион", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_radioBtn42, 0, wx.ALL, 5 )

		self.m_radioBtn7 = wx.RadioButton( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Обобщена по ден", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_radioBtn7, 0, wx.ALL, 5 )

		self.m_radioBtn14 = wx.RadioButton( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Обобщена по производител", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_radioBtn14, 0, wx.ALL, 5 )

		self.m_radioBtn15 = wx.RadioButton( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Обобщена по машини", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn15.SetValue( True )
		fgSizer13.Add( self.m_radioBtn15, 0, wx.ALL, 5 )

		self.m_checkBox15 = wx.CheckBox( sbSizer13.GetStaticBox(), wx.ID_ANY, u"За период", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox15.Hide()

		fgSizer13.Add( self.m_checkBox15, 0, wx.ALL, 5 )


		sbSizer13.Add( fgSizer13, 1, wx.EXPAND, 5 )


		bSizer4.Add( sbSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_radioBtn16 = wx.RadioButton( sbSizer15.GetStaticBox(), wx.ID_ANY, u"Генерирай таблица", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn16.SetValue( True )
		sbSizer15.Add( self.m_radioBtn16, 0, wx.ALL, 5 )

		self.m_radioBtn17 = wx.RadioButton( sbSizer15.GetStaticBox(), wx.ID_ANY, u"Генерирай графика", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.m_radioBtn17, 0, wx.ALL, 5 )


		bSizer4.Add( sbSizer15, 1, wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Генерирай", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		fgSizer9.Add( bSizer4, 0, 0, 5 )


		self.SetSizer( fgSizer9 )
		self.Layout()
		fgSizer9.Fit( self )

		# Connect Events
		self.m_radioBtn9.Bind( wx.EVT_RADIOBUTTON, self.OnRadioButton )
		self.m_radioBtn41.Bind( wx.EVT_RADIOBUTTON, self.OnRadioButton )
		self.m_radioBtn8.Bind( wx.EVT_RADIOBUTTON, self.OnRadioButton )
		self.m_radioBtn21.Bind( wx.EVT_RADIOBUTTON, self.OnRadioButton )
		self.m_radioBtn14.Bind( wx.EVT_RADIOBUTTON, self.OnTableSelect )
		self.m_radioBtn15.Bind( wx.EVT_RADIOBUTTON, self.OnTableSelect )
		self.m_checkBox15.Bind( wx.EVT_CHECKBOX, self.CalendarShow )
		self.m_radioBtn16.Bind( wx.EVT_RADIOBUTTON, self.OnTableMaket )
		self.m_radioBtn17.Bind( wx.EVT_RADIOBUTTON, self.OnTableMaket )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnGo )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnRadioButton( self, event ):
		event.Skip()




	def OnTableSelect( self, event ):
		event.Skip()


	def CalendarShow( self, event ):
		event.Skip()

	def OnTableMaket( self, event ):
		event.Skip()


	def OnGo( self, event ):
		event.Skip()


###########################################################################
## Class Xls
###########################################################################

class Xls ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Експорт", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 262,155 ), wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, u"/home/dedal", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer7.Add( self.m_dirPicker1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"tmp", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Затвори", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Експорт", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		bSizer7.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.m_button13.Bind( wx.EVT_BUTTON, self.OnClose )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnExport )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		event.Skip()


	def OnExport( self, event ):
		event.Skip()


